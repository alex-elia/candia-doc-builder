# Showcase Implementation Plan

Step-by-step guide to add your Thales presentation showcase and make it visible on GitHub.

## 🎯 Goal

Add visual showcase content (screenshots, GIFs, example outputs) to demonstrate Candia Doc Builder's capabilities and enhance your GitHub profile.

## 📋 Prerequisites

- [x] Repository structure created (`showcase/` folder)
- [x] Documentation in place
- [ ] Thales presentation files ready
- [ ] Screenshot/GIF tools installed

## Phase 1: Prepare Your Assets (15-30 minutes)

### Step 1.1: Locate Your Thales Presentation Files

Find the generated presentation files:
- `presentation_thales_alenia.pptx` (or similar)
- `pitch_thales_alenia.pdf` (if you have LaTeX output)
- Any other generated files

**Location**: Check `examples/satellite/` or wherever you ran the generator.

### Step 1.2: Copy Files to Showcase Folder

```bash
# From repository root
cd C:\Users\alexg\source\repos\candia-doc-builder

# Copy presentation files
copy examples\satellite\presentation_thales_*.pptx showcase\thales-example\
copy examples\satellite\pitch_thales_*.pdf showcase\thales-example\
```

**Or manually**:
1. Navigate to `showcase/thales-example/`
2. Copy your `.pptx` and `.pdf` files there

### Step 1.3: Generate Slide Summary (Optional)

```bash
# Generate a summary of slides for reference
python scripts\showcase\create_showcase.py --presentation showcase\thales-example\presentation_thales_alenia.pptx
```

This creates `showcase/thales-example/presentation_summary.md` with slide titles.

## Phase 2: Create Visual Assets (30-60 minutes)

### Step 2.1: Identify Key Slides to Showcase

Open your presentation and identify these key slides:
- ✅ **Title slide** - Shows branding and topic
- ✅ **Architecture diagram** - Demonstrates technical capability
- ✅ **Value proposition** - Shows business impact
- ✅ **Metrics/Results** - Quantified benefits
- ✅ **Conclusion** - Professional closing

**Tip**: Choose 5-7 slides that best represent the quality and variety.

### Step 2.2: Take Screenshots

#### Option A: Manual Screenshots (Recommended for first time)

1. **Open the presentation** in PowerPoint or similar
2. **Navigate to each key slide**
3. **Take screenshot**:
   - **Windows**: `Win + Shift + S` (Snipping Tool) or use ShareX
   - **macOS**: `Cmd + Shift + 4` (select area)
   - **Linux**: Use Flameshot or similar
4. **Save with descriptive names**:
   - `thales-title-slide.png`
   - `thales-architecture-diagram.png`
   - `thales-value-proposition.png`
   - `thales-metrics.png`
   - `thales-conclusion.png`

5. **Save to**: `showcase/screenshots/`

#### Option B: Automated Screenshots (Advanced)

If you have many presentations, consider automating:
- Use `python-pptx` to extract slides as images
- Use headless browser tools
- Create a script to batch process

### Step 2.3: Create Animated GIF (Optional but Recommended)

An animated walkthrough shows the presentation flow:

1. **Record screen** while navigating through slides:
   - **Windows**: OBS Studio, ShareX, or LICEcap
   - **macOS**: QuickTime or ScreenFlow
   - **Linux**: OBS Studio or SimpleScreenRecorder

2. **Keep it short**: 10-15 seconds, showing 3-5 key slides

3. **Convert to GIF**:
   ```bash
   # Using FFMPEG (if installed)
   ffmpeg -i recording.mp4 -vf "fps=10,scale=800:-1" showcase/screenshots/thales-demo.gif
   ```
   
   Or use online tools:
   - [EZGIF](https://ezgif.com/video-to-gif)
   - [CloudConvert](https://cloudconvert.com/mp4-to-gif)

4. **Optimize**: Keep file size under 5MB

5. **Save to**: `showcase/screenshots/thales-demo.gif`

### Step 2.4: Optimize Images

Before committing, optimize images:

**For PNGs**:
- Use [TinyPNG](https://tinypng.com/) or [ImageOptim](https://imageoptim.com/)
- Target: < 500KB per image

**For GIFs**:
- Reduce colors if needed
- Target: < 5MB total

## Phase 3: Update Documentation (15 minutes)

### Step 3.1: Update showcase/README.md

Edit `showcase/README.md` and add your example:

```markdown
## Current Examples

### Thales Alenia Space Presentation
- **Source**: `examples/satellite/generate_thales_presentation.py`
- **Output**: Professional pitch deck for embedded AI on satellites
- **Highlights**: 
  - Architecture diagrams showing system design
  - Value propositions with quantified metrics
  - Technical specifications and deployment scenarios
- **Files**:
  - `thales-example/presentation_thales_alenia.pptx`
  - `thales-example/pitch_thales_alenia.pdf`
- **Screenshots**: See `screenshots/thales-*.png`
```

### Step 3.2: Update Main README.md

The README already references the showcase, but you can enhance it:

1. **Add specific image references** in the Showcase section:
   ```markdown
   ### Visual Examples
   
   ![Thales Architecture](showcase/screenshots/thales-architecture-diagram.png)
   *Architecture diagram from generated presentation*
   
   ![Thales Demo](showcase/screenshots/thales-demo.gif)
   *Animated walkthrough of the presentation*
   ```

2. **Or keep it simple** - The current README already links to showcase folder

### Step 3.3: Update docs/README.md (Optional)

Add showcase workflow to the documentation index if not already there.

## Phase 4: Commit and Push (5 minutes)

### Step 4.1: Review Changes

```bash
cd C:\Users\alexg\source\repos\candia-doc-builder
git status
```

You should see:
- New files in `showcase/thales-example/`
- New files in `showcase/screenshots/`
- Updated `showcase/README.md`

### Step 4.2: Stage and Commit

```bash
# Stage all showcase content
git add showcase/

# Commit with descriptive message
git commit -m "docs: add Thales presentation showcase with screenshots and examples"

# Push to GitHub
git push origin main
```

### Step 4.3: Verify on GitHub

1. Visit: `https://github.com/alex-elia/candia-doc-builder`
2. Navigate to `showcase/` folder
3. Verify images display correctly
4. Check that README links work

## Phase 5: Enhance (Optional, Future)

### Step 5.1: Add More Examples

As you create more presentations:
- Add them to `showcase/` with descriptive folders
- Update `showcase/README.md`
- Keep the gallery fresh

### Step 5.2: Enable GitHub Pages (Optional)

For a fancy gallery page:

1. Go to repository Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main` / `showcase/`
4. Your gallery will be at: `https://alex-elia.github.io/candia-doc-builder/showcase/`

### Step 5.3: Add Video Walkthrough (Advanced)

Create a short video (2-3 minutes):
- Screen recording of generating a presentation
- Voiceover explaining the process
- Upload to YouTube/Vimeo
- Embed in README

## ✅ Checklist

Use this checklist to track your progress:

### Preparation
- [ ] Thales presentation files located
- [ ] Files copied to `showcase/thales-example/`
- [ ] Slide summary generated (optional)

### Visual Assets
- [ ] Title slide screenshot taken
- [ ] Architecture diagram screenshot taken
- [ ] Value proposition screenshot taken
- [ ] Metrics slide screenshot taken
- [ ] Conclusion slide screenshot taken
- [ ] All screenshots saved to `showcase/screenshots/`
- [ ] Animated GIF created (optional)
- [ ] Images optimized (< 500KB PNG, < 5MB GIF)

### Documentation
- [ ] `showcase/README.md` updated with example description
- [ ] Main `README.md` enhanced (optional)
- [ ] All links verified

### Git & GitHub
- [ ] Changes reviewed with `git status`
- [ ] Files committed with descriptive message
- [ ] Pushed to GitHub
- [ ] Verified on GitHub website

## 🎯 Success Criteria

Your showcase is complete when:
- ✅ Screenshots visible in `showcase/screenshots/` on GitHub
- ✅ Example files available in `showcase/thales-example/`
- ✅ README updated with descriptions
- ✅ Links work correctly
- ✅ Images load quickly (< 2 seconds)

## 📝 Notes

- **File sizes**: Keep images reasonable for fast loading
- **Naming**: Use descriptive, consistent names
- **Updates**: Refresh showcase as you create new examples
- **Cursor workflow**: Continue using Cursor for content generation, showcase is just for display

## 🆘 Troubleshooting

### Images not showing on GitHub
- Check file paths are correct
- Verify images are committed (not in .gitignore)
- Use relative paths in markdown: `showcase/screenshots/image.png`

### Files too large
- Compress images before committing
- Use image optimization tools
- Consider using GitHub LFS for very large files

### Screenshots look blurry
- Use higher DPI settings
- Export at 2x resolution
- Use PNG format for better quality

---

**Estimated Total Time**: 1-2 hours for complete showcase setup

**Next Steps After Completion**: 
1. Share the repository link
2. Add to your portfolio/resume
3. Reference in professional profiles
4. Use as conversation starter in interviews

