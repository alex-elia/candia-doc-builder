# PowerShell script to build and protect PDF with encryption
# This adds password protection and restricts copying/printing

param(
    [string]$Version = "latest",
    [string]$Password = ""
)

Write-Host "Building and protecting Thales Alenia Space pitch document..." -ForegroundColor Green

# Check if pdflatex is available and set PATH
$pdflatexPath = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
$pdflatexCmd = $null

if (Test-Path $pdflatexPath) {
    # MiKTeX found in default location, add to PATH
    $env:Path += ";$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
    $pdflatexCmd = "pdflatex"
    Write-Host "Found MiKTeX at: $pdflatexPath" -ForegroundColor Cyan
    
    # Update MiKTeX database to avoid update prompts
    Write-Host "Updating MiKTeX database..." -ForegroundColor Cyan
    & pdflatex --update-fndb 2>&1 | Out-Null
} else {
    # Try to find pdflatex in PATH
    $pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue
    if ($pdflatex) {
        $pdflatexCmd = "pdflatex"
        Write-Host "Found pdflatex in PATH" -ForegroundColor Cyan
    } else {
        Write-Host "Error: pdflatex is not installed or not in PATH." -ForegroundColor Red
        Write-Host "Please install MiKTeX or add pdflatex to your PATH." -ForegroundColor Yellow
        exit 1
    }
}

# Find latest versioned file or use specified
if ($Version -eq "latest") {
    $texFiles = Get-ChildItem -Path . -Filter "pitch_thales_alenia_v*.tex" | Sort-Object Name -Descending
    if ($texFiles.Count -gt 0) {
        $texFile = $texFiles[0].Name
        $pdfFile = $texFile -replace '\.tex$', '.pdf'
        $protectedFile = $texFile -replace '\.tex$', '_protected.pdf'
    } else {
        $texFile = "pitch_thales_alenia.tex"
        $pdfFile = "pitch_thales_alenia.pdf"
        $protectedFile = "pitch_thales_alenia_protected.pdf"
    }
} else {
    $texFile = "pitch_thales_alenia_v$Version.tex"
    $pdfFile = "pitch_thales_alenia_v$Version.pdf"
    $protectedFile = "pitch_thales_alenia_v$Version_protected.pdf"
    if (-not (Test-Path $texFile)) {
        Write-Host "Error: File $texFile not found." -ForegroundColor Red
        exit 1
    }
}

# Compile LaTeX document
Write-Host "Compiling LaTeX document..." -ForegroundColor Cyan
$baseName = $texFile -replace '\.tex$', ''

# First pass
Write-Host "First compilation pass..." -ForegroundColor Cyan
$result = & $pdflatexCmd -interaction=nonstopmode $texFile 2>&1
$output = $result | Out-String
if ($output -match "Output written") {
    Write-Host "PDF created successfully" -ForegroundColor Green
} elseif ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne 1) {
    Write-Host "Warning: LaTeX compilation had issues on first pass." -ForegroundColor Yellow
}

# Second pass for TOC
Write-Host "Second compilation pass (for TOC)..." -ForegroundColor Cyan
$result = & $pdflatexCmd -interaction=nonstopmode $texFile 2>&1
$output = $result | Out-String
if ($output -match "Output written") {
    Write-Host "PDF updated successfully" -ForegroundColor Green
} elseif ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne 1) {
    Write-Host "Warning: LaTeX compilation had issues on second pass." -ForegroundColor Yellow
}

# Wait a moment for file system to sync and verify PDF was created
Start-Sleep -Milliseconds 1000
$maxRetries = 5
$retryCount = 0
while (-not (Test-Path $pdfFile) -and $retryCount -lt $maxRetries) {
    Start-Sleep -Milliseconds 500
    $retryCount++
}

if (-not (Test-Path $pdfFile)) {
    Write-Host "Error: PDF file not found after compilation: $pdfFile" -ForegroundColor Red
    Write-Host "LaTeX compilation may have failed. Checking for any PDF files..." -ForegroundColor Yellow
    Get-ChildItem -Filter "*.pdf" | Select-Object Name | ForEach-Object { Write-Host "  Found: $($_.Name)" -ForegroundColor Yellow }
    exit 1
}

# Check for encryption tools
$qpdf = Get-Command qpdf -ErrorAction SilentlyContinue
if (-not $qpdf) {
    # Check common installation locations
    $qpdfPaths = @(
        "C:\Program Files\qpdf*\bin\qpdf.exe",
        "$env:ProgramFiles\qpdf*\bin\qpdf.exe",
        "$env:LOCALAPPDATA\Programs\qpdf*\bin\qpdf.exe"
    )
    foreach ($path in $qpdfPaths) {
        $found = Get-ChildItem -Path $path -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($found) {
            $qpdfPath = $found.FullName
            $env:Path += ";$($found.DirectoryName)"
            $qpdf = Get-Command qpdf -ErrorAction SilentlyContinue
            Write-Host "Found qpdf at: $qpdfPath" -ForegroundColor Cyan
            break
        }
    }
}
$pdftk = Get-Command pdftk -ErrorAction SilentlyContinue

if ($qpdf) {
    Write-Host "Using qpdf for PDF protection..." -ForegroundColor Cyan
    
    if ($Password -eq "") {
        # No user password (opens without password), but restrict copy-paste
        # Use empty user password and owner password for restrictions only
        $ownerPassword = -join ((65..90) + (97..122) + (48..57) | Get-Random -Count 16 | ForEach-Object {[char]$_})
        # Use newer qpdf syntax with flags (qpdf 11.7.0+)
        $qpdfArgs = @(
            '--linearize',
            '--encrypt',
            '--user-password=',  # Empty = no password to open
            "--owner-password=$ownerPassword",
            '--bits=256',         # 256-bit encryption (required by qpdf 12+)
            '--print=full',       # Allow printing
            '--modify=none',      # Prevent modification
            '--extract=n',        # Prevent copy-paste (text extraction)
            '--',
            "$pdfFile",
            "$protectedFile"
        )
        & qpdf $qpdfArgs
        if ($LASTEXITCODE -eq 0) {
            Write-Host "PDF protected: Opens without password, but copy-paste is disabled" -ForegroundColor Green
        } else {
            Write-Host "Warning: PDF protection failed, using unprotected PDF" -ForegroundColor Yellow
            $protectedFile = $pdfFile
        }
    } else {
        # With password
        # Use newer qpdf syntax with flags (qpdf 11.7.0+)
        $qpdfArgs = @(
            '--linearize',
            '--encrypt',
            "--user-password=$Password",
            "--owner-password=$Password",
            '--bits=256',         # 256-bit encryption (required by qpdf 12+)
            '--print=none',
            '--modify=none',
            '--extract=n',
            '--',
            "$pdfFile",
            "$protectedFile"
        )
        & qpdf $qpdfArgs
        if ($LASTEXITCODE -eq 0) {
            Write-Host "PDF protected with password" -ForegroundColor Green
        } else {
            Write-Host "Warning: PDF protection failed, using unprotected PDF" -ForegroundColor Yellow
            $protectedFile = $pdfFile
        }
    }
} elseif ($pdftk) {
    Write-Host "Using pdftk for PDF protection..." -ForegroundColor Cyan
    
    if ($Password -eq "") {
        Write-Host "Warning: pdftk requires a password. Generating random password..." -ForegroundColor Yellow
        $Password = -join ((65..90) + (97..122) + (48..57) | Get-Random -Count 16 | ForEach-Object {[char]$_})
        Write-Host "Generated password: $Password" -ForegroundColor Yellow
    }
    
    pdftk $pdfFile output $protectedFile user_pw "$Password" owner_pw "$Password" allow AllFeatures -restrict
    Write-Host "PDF protected with password: $Password" -ForegroundColor Green
} else {
    Write-Host "Warning: No PDF encryption tool found (qpdf or pdftk)." -ForegroundColor Yellow
    Write-Host "Installing qpdf (recommended) or pdftk for full protection." -ForegroundColor Yellow
    Write-Host "For now, using unprotected PDF: $pdfFile" -ForegroundColor Yellow
    $protectedFile = $pdfFile
}

# Clean up auxiliary files
Write-Host "Cleaning up auxiliary files..." -ForegroundColor Cyan
Remove-Item -Path "$baseName.aux", "$baseName.log", "$baseName.out", "$baseName.toc" -ErrorAction SilentlyContinue

Write-Host "Build complete! Output: $protectedFile" -ForegroundColor Green
if ($Password -ne "") {
    Write-Host "Password: $Password" -ForegroundColor Yellow
    Write-Host "IMPORTANT: Save this password securely!" -ForegroundColor Red
}

