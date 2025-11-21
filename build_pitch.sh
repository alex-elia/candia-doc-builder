#!/bin/bash
# Build script for Thales Alenia Space pitch document

echo "Building Thales Alenia Space pitch document..."

# Check if pdflatex is available
if ! command -v pdflatex &> /dev/null; then
    echo "Error: pdflatex is not installed."
    echo "Please install a LaTeX distribution (e.g., TeX Live, MiKTeX)"
    exit 1
fi

# Compile LaTeX document (run twice for table of contents)
pdflatex -interaction=nonstopmode pitch_thales_alenia.tex
pdflatex -interaction=nonstopmode pitch_thales_alenia.tex

# Clean up auxiliary files
rm -f *.aux *.log *.out *.toc

echo "Build complete! Output: pitch_thales_alenia.pdf"

