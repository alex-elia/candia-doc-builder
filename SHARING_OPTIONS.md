# Sharing Options - Demo Only

## The Question

**"What if I only want to share the demo to a client or potential employer?"**

Great question! You don't always need to share the entire repository. Here are several options:

---

## Option 1: Standalone Demo Package (Recommended)

Create a lightweight package with just the demo and essential files.

### Structure
```
satellite-ai-demo/
├── README.md                    # Simple demo instructions
├── docker-compose.yml           # Just demo setup
├── Dockerfile                   # Container definition
├── demo/                        # Demo scripts only
│   ├── run_demo.sh
│   ├── thales_demo.sh
│   ├── smart_agriculture_demo.sh
│   └── web_demo.html
├── scripts/
│   └── inference_server.sh     # Just the server
└── config/
    └── model_config.json        # Basic config
```

### ✅ Pros
- **Lightweight** - Only essential files
- **Easy to share** - Can zip and email
- **Focused** - Just the demo, no extra docs
- **Quick setup** - Client can run immediately

### How to Create
```bash
# Create demo package script
./scripts/create_demo_package.sh
```

---

## Option 2: Web-Based Demo (Easiest to Share)

Create a standalone HTML demo that works in a browser.

### Structure
```
satellite-ai-web-demo/
├── index.html                   # Single-page demo
├── demo.js                      # Demo logic
├── demo.css                     # Styling
└── README.md                    # Simple instructions
```

### ✅ Pros
- **No installation** - Just open HTML file
- **Works offline** - After initial setup
- **Professional** - Clean web interface
- **Easy to share** - Single file or small folder

### Implementation
- Embed demo scenarios in HTML
- Use mock API responses (no backend needed)
- Show pre-recorded AI responses
- Or connect to hosted API endpoint

---

## Option 3: Video Demo

Record a video of the demo running.

### ✅ Pros
- **Zero setup** - Client just watches
- **Controlled narrative** - You control what they see
- **Professional** - Polished presentation
- **No technical barriers** - Works for non-technical clients

### How to Create
1. Record screen while running demo
2. Add voiceover explaining key points
3. Edit to highlight important moments
4. Upload to YouTube (unlisted) or share file

---

## Option 4: Live Demo Session

Share your screen and run the demo live.

### ✅ Pros
- **Interactive** - Can answer questions
- **Personal** - Builds relationship
- **Flexible** - Can adapt to their interests
- **No sharing** - Nothing to download

### Tools
- Zoom, Teams, Google Meet
- Screen sharing
- Run demo locally, share screen

---

## Option 5: Docker Image (Portable)

Create a single Docker image with everything.

### Structure
```bash
# Build demo image
docker build -t satellite-ai-demo:latest .

# Export image
docker save satellite-ai-demo:latest | gzip > satellite-ai-demo.tar.gz

# Share the .tar.gz file
```

### ✅ Pros
- **Self-contained** - Everything in one file
- **Portable** - Works on any Docker system
- **No setup** - Just load and run
- **Professional** - Shows technical competence

### How to Use
```bash
# Client receives satellite-ai-demo.tar.gz
docker load < satellite-ai-demo.tar.gz
docker run -p 8080:8080 satellite-ai-demo:latest
```

---

## Option 6: GitHub Gist / Simple Repo

Create a minimal GitHub repository with just demo.

### Structure
```
satellite-ai-demo/               # Minimal repo
├── README.md                    # Quick start
├── docker-compose.yml
├── Dockerfile
└── demo/
    └── run_demo.sh
```

### ✅ Pros
- **Easy to share** - Just send GitHub link
- **Version control** - Can update easily
- **Professional** - Shows GitHub presence
- **Accessible** - Client can clone and run

---

## Recommendation by Use Case

### For Potential Employer (Job Interview)
**Best: Video Demo + GitHub Link**
- Video shows it working (no setup needed)
- GitHub link shows code quality
- Demonstrates both technical and communication skills

### For Client (Thales Alenia Space)
**Best: Standalone Demo Package + Live Demo**
- Package shows technical depth
- Live demo allows interaction
- Can answer questions in real-time

### For Portfolio/Showcase
**Best: Web Demo + GitHub Repo**
- Web demo is accessible to anyone
- GitHub repo shows full implementation
- Professional and complete

---

## Quick Implementation: Standalone Demo Package

Let me create a script to generate a demo-only package:

```bash
# Create demo package
./scripts/create_demo_package.sh

# This creates:
# satellite-ai-demo.zip
#   - Just demo files
#   - Simple README
#   - Docker setup
#   - No internal docs
```

---

## What to Include in Demo Package

### Essential Files
- ✅ `docker-compose.yml` - Easy setup
- ✅ `Dockerfile` - Container definition
- ✅ `demo/run_demo.sh` - Main demo
- ✅ `demo/thales_demo.sh` - Thales-specific demo
- ✅ `scripts/inference_server.sh` - Server script
- ✅ `README.md` - Simple instructions

### Exclude
- ❌ Internal documentation (architecture docs)
- ❌ Proposal templates
- ❌ Migration notes
- ❌ Development scripts
- ❌ Git history

---

## Example: Minimal README for Demo Package

```markdown
# Satellite AI Demo

## Quick Start

1. Download a model from https://huggingface.co/TheBloke
   - Search for "Phi-3-mini-GGUF"
   - Download Q4_K_M version
   - Place in ./models/ directory

2. Run demo:
   ```bash
   docker-compose up -d
   ./demo/run_demo.sh
   ```

## What This Demo Shows

- Autonomous AI inference (offline)
- Anomaly detection
- Real-time decision making

## Requirements

- Docker
- 4GB free disk space
```

---

## Action Items

1. **Create demo package script** - Automate the process
2. **Create web demo** - HTML-only version
3. **Record video demo** - For non-technical sharing
4. **Update main README** - Add sharing instructions

---

**Bottom Line:** For sharing with clients/employers, a **standalone demo package** or **web demo** is usually best. It's focused, easy to use, and doesn't overwhelm them with internal documentation.

