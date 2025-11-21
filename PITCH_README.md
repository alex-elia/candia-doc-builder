# Thales Alenia Space Pitch Document

## Overview

This LaTeX document presents an architecture-driven approach to deploying embedded AI on satellite systems, specifically designed for Thales Alenia Space. The document focuses on:

- **Architecture and approach** (not full implementation)
- **Technical feasibility** (VxWorks, Embedded Linux)
- **Two key scenarios** (Anomaly Detection, Agricultural Image Processing)
- **Value proposition** for Thales Alenia Space's satellite portfolio

## Document Structure

1. **Executive Summary** - Key value propositions and technical approach
2. **System Architecture** - High-level design and technology stack
3. **Use Case Scenarios** - Two detailed scenarios with examples
4. **Technical Feasibility** - OS compatibility, model optimization, performance
5. **Architecture & Development Methodology** - Approach and validation strategy
6. **Value Proposition** - Benefits for different satellite types
7. **Implementation Approach** - Phases and collaboration model
8. **Next Steps & Engagement** - Proposed timeline and deliverables

## Building the PDF

### Prerequisites

Install a LaTeX distribution:
- **Windows:** [MiKTeX](https://miktex.org/download)
- **Linux/macOS:** [TeX Live](https://www.tug.org/texlive/)

### Build Commands

**Windows (PowerShell):**
```powershell
cd docs
.\build_pitch.ps1
```

**Linux/macOS:**
```bash
cd docs
chmod +x build_pitch.sh
./build_pitch.sh
```

**Manual Build:**
```bash
pdflatex pitch_thales_alenia.tex
pdflatex pitch_thales_alenia.tex  # Run twice for TOC
```

## Architecture Diagrams

The document includes **TikZ diagrams** for:
- High-Level System Architecture (Earth + Satellite)
- On-Board AI Architecture (VxWorks/Embedded Linux)
- Scenario 1: Anomaly Detection Workflow
- Scenario 2: Agricultural Image Processing Pipeline

### Including External Images

If you prefer to use external images (PNG, PDF, etc.) instead of TikZ:

```latex
% Replace TikZ diagram with:
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{path/to/your/diagram.pdf}
\caption{Your Caption}
\label{fig:your-label}
\end{figure}
```

**Supported formats:** PDF (recommended), PNG, JPG

### Creating Custom Diagrams

You can create diagrams using:
- **TikZ** (already in document) - Programmatic diagrams
- **External tools** - Draw.io, Visio, Lucidchart, then export as PDF
- **Python** - matplotlib, graphviz, then export as PDF

## PDF Protection

### Basic Protection (Metadata)
The LaTeX document includes metadata protection. For full copy/paste protection, you need to encrypt the PDF after compilation.

### Full PDF Protection (Encryption)

To add password protection and restrict copying/printing:

**Option 1: Using qpdf (Recommended)**
```powershell
# Install qpdf first: winget install qpdf
.\build_pitch_protected.ps1
```

**Option 2: Using pdftk**
```powershell
# Install pdftk first
.\build_pitch_protected.ps1 -Password "YourPassword"
```

**Manual Protection:**
After building, use external tools:
- **qpdf**: `qpdf --encrypt "" "" 128 --print=n --modify=n --extract=n input.pdf output.pdf`
- **pdftk**: `pdftk input.pdf output output.pdf user_pw "password" owner_pw "password"`

**Note:** PDF protection is not foolproof - determined users can still extract text. However, it:
- Shows intent to protect intellectual property
- Deters casual copying
- Adds professional credibility
- Makes bulk extraction more difficult

## Fonts

The document uses professional fonts optimized for technical presentations:
- **Body Text**: Palatino (elegant, readable serif font)
- **Headings**: Helvetica (modern sans-serif for technical feel)
- **Math**: Sans-serif for consistency

This combination provides:
- Professional appearance suitable for job interviews
- Technical credibility
- Excellent readability
- Modern, clean aesthetic

## Customization

### Update Contact Information

Edit `pitch_thales_alenia.tex` and update:
```latex
\author{\Large Alexandre GON\\
\small Architecture \& AI Solutions\\
\small Leveraging Modern AI Tools for Space Systems}
```

And at the end:
```latex
\textbf{Contact:}\\
Alexandre GON\\
Architecture \& AI Solutions\\
\href{mailto:your-email@example.com}{your-email@example.com}
```

### Modify Content

The document is structured with clear sections. Key areas to customize:
- **Executive Summary:** Adjust value propositions
- **Use Case Scenarios:** Add Thales-specific examples
- **Value Proposition:** Include ROI calculations if available
- **Next Steps:** Update timeline based on discussions

## Document Philosophy

This document presents:
- **Alexandre GON** as the architect and AI solutions expert
- **Architecture skills** in system design for embedded environments
- **AI tools** (LLMs, Computer Vision) leveraged for rapid prototyping and validation
- **Approach and feasibility** rather than full implementation details

The goal is to demonstrate:
1. Understanding of satellite system constraints
2. Technical feasibility of the approach
3. Clear value proposition for Thales Alenia Space
4. Practical path to implementation

## Notes

- The document is designed to be **concise** (10-15 pages)
- Focus is on **architecture and approach**, not full demo
- **Technical feasibility** is emphasized (VxWorks, model optimization)
- **Value proposition** is tailored to Thales Alenia Space's portfolio
- **Next steps** provide clear engagement path

## Output

After building, you'll have:
- `pitch_thales_alenia.pdf` - The final PDF document
- Clean directory (auxiliary files removed)

The PDF is ready to share with Thales Alenia Space stakeholders.

