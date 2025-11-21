# Showcase Gallery

This folder contains example outputs and visual demonstrations of Candia Doc Builder.

📋 **Implementation Plan**: See [SHOWCASE_IMPLEMENTATION_PLAN.md](../SHOWCASE_IMPLEMENTATION_PLAN.md) for step-by-step instructions.

## Structure

```
showcase/
├── README.md              # This file
├── thales-example/        # Thales presentation example outputs
├── screenshots/           # Screenshots and GIFs for documentation
└── index.html             # Simple gallery page (optional)
```

## Adding Showcase Content

### For Screenshots/GIFs

1. **Generate your presentation** using the scripts
2. **Take screenshots** of key slides or create a GIF walkthrough
3. **Save to `screenshots/`** with descriptive names:
   - `thales-architecture-slide.png`
   - `thales-demo-animated.gif`
   - `before-after-comparison.png`

### For Example Outputs

1. **Run the generator** (e.g., `examples/satellite/generate_thales_presentation.py`)
2. **Copy the output** to `thales-example/`:
   - `presentation_thales_alenia.pptx`
   - `pitch_thales_alenia.pdf`
   - Any other generated files

### Best Practices

- **Keep file sizes reasonable** (< 5MB for images, < 20MB for presentations)
- **Use descriptive names** that explain what the example shows
- **Include a brief description** in this README for each example
- **Update README.md** in the root to link to new showcase content

## Current Examples

### Thales Alenia Space Presentation
- **Source**: `examples/satellite/generate_thales_presentation.py`
- **Output**: Professional pitch deck for embedded AI on satellites
- **Highlights**: Architecture diagrams, value propositions, technical specs

*Add your showcase content here as you create it.*

