# 🎬 Guide Rapide: Générer Vidéo Démo

## Installation

```bash
# Installer moviepy
pip install moviepy

# Optionnel: Pour meilleure qualité
pip install imageio-ffmpeg
```

## 🚀 Utilisation Rapide

### 1. **Créer Vidéo depuis Screenshots**

```bash
# 1. Créer dossier screenshots
mkdir screenshots

# 2. Y placer vos captures d'écran
# (nommer: screen1.png, screen2.png, etc.)

# 3. Générer vidéo
python generate_demo_video.py images
```

### 2. **Créer Vidéo depuis Diagrammes**

```bash
# 1. Créer dossier diagrams
mkdir diagrams

# 2. Y placer vos diagrammes (PNG/JPG)

# 3. Générer vidéo animée
python generate_demo_video.py diagrams
```

### 3. **Convertir Présentation en Vidéo**

```bash
# 1. Exporter slides PPTX en images PNG
# (Dans PowerPoint: File → Export → Images)

# 2. Placer dans dossier presentation_slides

# 3. Générer vidéo
python generate_demo_video.py presentation
```

## 📋 Workflow Complet

### Pour Démo Satellite AI:

1. **Prendre Screenshots**
   - Interface du logiciel
   - Résultats de traitement
   - Diagrammes d'architecture

2. **Organiser**
   ```
   screenshots/
     ├── 01_intro.png
     ├── 02_architecture.png
     ├── 03_scenario1.png
     └── 04_results.png
   ```

3. **Générer Vidéo**
   ```bash
   python generate_demo_video.py images
   ```

4. **Résultat**: `software_demo.mp4`

## 🎨 Personnalisation

Le script peut être modifié pour:
- ✅ Ajouter annotations (flèches, highlights)
- ✅ Ajouter narration audio
- ✅ Ajuster timing par slide
- ✅ Ajouter transitions
- ✅ Ajouter logo/watermark

---

**Voulez-vous que je crée un script spécifique pour votre démo satellite AI?**

