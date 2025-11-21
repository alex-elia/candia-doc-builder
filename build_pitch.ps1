# PowerShell build script for Thales Alenia Space pitch document

param(
    [string]$Version = "latest"
)

Write-Host "Building Thales Alenia Space pitch document..." -ForegroundColor Green

# Check if pdflatex is available
$pdflatexPath = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
if (-not (Test-Path $pdflatexPath)) {
    $pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue
    if (-not $pdflatex) {
        Write-Host "Error: pdflatex is not installed." -ForegroundColor Red
        Write-Host "Please install a LaTeX distribution:" -ForegroundColor Yellow
        Write-Host "  - MiKTeX: https://miktex.org/download" -ForegroundColor Yellow
        Write-Host "  - TeX Live: https://www.tug.org/texlive/" -ForegroundColor Yellow
        exit 1
    }
    $pdflatexCmd = "pdflatex"
} else {
    $env:Path += ";$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64"
    $pdflatexCmd = "pdflatex"
}

# Find latest versioned file or use specified
if ($Version -eq "latest") {
    $texFiles = Get-ChildItem -Path . -Filter "pitch_thales_alenia_v*.tex" | Sort-Object Name -Descending
    if ($texFiles.Count -gt 0) {
        $texFile = $texFiles[0].Name
        $pdfFile = $texFile -replace '\.tex$', '.pdf'
        Write-Host "Using latest version: $texFile" -ForegroundColor Cyan
    } else {
        $texFile = "pitch_thales_alenia.tex"
        $pdfFile = "pitch_thales_alenia.pdf"
        Write-Host "Using: $texFile" -ForegroundColor Cyan
    }
} else {
    $texFile = "pitch_thales_alenia_v$Version.tex"
    $pdfFile = "pitch_thales_alenia_v$Version.pdf"
    if (-not (Test-Path $texFile)) {
        Write-Host "Error: File $texFile not found." -ForegroundColor Red
        exit 1
    }
}

# Compile LaTeX document (run twice for table of contents)
Write-Host "Compiling LaTeX document (first pass)..." -ForegroundColor Cyan
& $pdflatexCmd -interaction=nonstopmode $texFile | Out-Null

Write-Host "Compiling LaTeX document (second pass for TOC)..." -ForegroundColor Cyan
& $pdflatexCmd -interaction=nonstopmode $texFile | Out-Null

# Clean up auxiliary files
Write-Host "Cleaning up auxiliary files..." -ForegroundColor Cyan
$baseName = $texFile -replace '\.tex$', ''
Remove-Item -Path "$baseName.aux", "$baseName.log", "$baseName.out", "$baseName.toc" -ErrorAction SilentlyContinue

Write-Host "Build complete! Output: $pdfFile" -ForegroundColor Green

