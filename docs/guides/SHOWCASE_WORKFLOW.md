# Showcase Workflow Guide

How to create and maintain showcase content while using Cursor for content generation.

## Workflow Overview

```
1. Generate content in Cursor (AI-assisted)
   ↓
2. Run Candia Doc Builder scripts
   ↓
3. Generate presentation/output
   ↓
4. Create showcase assets (screenshots/GIFs)
   ↓
5. Update showcase gallery
```

## Step-by-Step Process

### 1. Generate Content with Cursor

Use Cursor's AI capabilities to:
- Write presentation content
- Generate architecture descriptions
- Create technical specifications
- Refine messaging and value propositions

**Save your content** in a format that Candia Doc Builder can consume:
- JSON/YAML for structured data
- Markdown for narrative content
- Python dictionaries for programmatic generation

### 2. Generate Presentation

```bash
# Example: Generate Thales presentation
python examples/satellite/generate_thales_presentation.py

# Or use your custom generator
python scripts/presentation/your_generator.py
```

### 3. Create Showcase Assets

#### Option A: Manual Screenshots
1. Open the generated presentation
2. Take screenshots of key slides:
   - Title slide
   - Architecture diagrams
   - Key metrics/features
   - Conclusion slide
3. Save to `showcase/screenshots/` with descriptive names

#### Option B: Automated Extraction
```bash
# Generate slide summary
python scripts/showcase/create_showcase.py \
    --presentation presentation_thales_alenia.pptx \
    --output showcase/thales-example
```

### 4. Create Animated GIF (Optional)

For dynamic demonstrations:
1. Use screen recording tools (OBS, LICEcap, etc.)
2. Record a walkthrough of the presentation
3. Convert to GIF (use tools like `ffmpeg` or online converters)
4. Save to `showcase/screenshots/`

### 5. Update Showcase Gallery

1. **Add images to showcase/screenshots/**
2. **Update showcase/README.md** with descriptions
3. **Update main README.md** Showcase section with links
4. **Commit and push** to GitHub

## Best Practices

### Image Guidelines
- **Resolution**: 1920x1080 or higher for presentations
- **Format**: PNG for screenshots, GIF for animations
- **Size**: Keep under 5MB per image
- **Naming**: Use descriptive names like `thales-architecture-diagram.png`

### Content Guidelines
- **Show variety**: Different slide types, use cases
- **Highlight quality**: Best examples that demonstrate capabilities
- **Keep updated**: Remove outdated examples, add new ones

### Cursor Integration
- **Version control**: Keep Cursor-generated content in separate files
- **Template separation**: Store templates separately from generated content
- **Documentation**: Comment in code where Cursor AI was used

## Example Workflow

```bash
# 1. Generate presentation (content from Cursor)
python examples/satellite/generate_thales_presentation.py

# 2. Create showcase assets
python scripts/showcase/create_showcase.py \
    --presentation presentation_thales_alenia.pptx

# 3. Take screenshots manually (or automate with tools)
# Save to showcase/screenshots/

# 4. Update documentation
# Edit showcase/README.md and main README.md

# 5. Commit
git add showcase/
git commit -m "docs: add Thales presentation showcase"
git push
```

## Tools for Screenshots/GIFs

### Screenshot Tools
- **Windows**: Snipping Tool, ShareX
- **macOS**: Screenshot app, CleanShot X
- **Linux**: Flameshot, Spectacle

### GIF Creation
- **LICEcap**: Simple screen-to-GIF
- **FFMPEG**: Command-line video to GIF
- **Online**: EZGIF, CloudConvert

### Screen Recording
- **OBS Studio**: Free, open-source
- **Camtasia**: Professional (paid)
- **QuickTime** (macOS): Built-in

## GitHub Pages Integration

To host the showcase gallery:

1. **Enable GitHub Pages** in repository settings
2. **Point to showcase/** folder or `docs/` folder
3. **Access at**: `https://alex-elia.github.io/candia-doc-builder/showcase/`

The `showcase/index.html` file provides a simple gallery interface.

## Troubleshooting

### Issue: Images too large
**Solution**: Compress images using tools like TinyPNG or ImageOptim

### Issue: GIF file size too big
**Solution**: Reduce frame rate, optimize colors, or use video format instead

### Issue: Screenshots look blurry
**Solution**: Use higher DPI settings, export at 2x resolution

## Next Steps

- Add more showcase examples
- Create video walkthroughs
- Build automated screenshot pipeline
- Integrate with CI/CD for auto-updates

