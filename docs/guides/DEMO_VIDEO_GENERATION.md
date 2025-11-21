# 🎬 Guide: Génération Vidéo Démo PPTX + Google Images

## 🎯 Objectif

Créer une vidéo de démo qui alterne entre:
- ✅ **Présentation PowerPoint** (slides Thales Alenia)
- ✅ **Navigation Google Images** (recherche images satellitaires)
- ✅ **Transitions fluides** entre les deux

---

## 🚀 Méthode 1: Automatisation Complète (Recommandé)

### Prérequis

```bash
# Installer dépendances Python
pip install pyautogui selenium moviepy

# Installer ChromeDriver
# Télécharger: https://chromedriver.chromium.org/
# Ou via winget:
winget install chromedriver
```

### Utilisation

1. **Démarrer enregistrement d'écran** (OBS Studio ou FFmpeg)
2. **Exécuter le script**:
   ```bash
   python generate_demo_with_web_search.py auto
   ```
3. **Le script orchestre automatiquement**:
   - Ouvre PowerPoint
   - Démarre présentation
   - Navigue entre slides
   - Ouvre Google Images
   - Effectue recherches
   - Alterne entre slides et navigateur
4. **Arrêter enregistrement** à la fin

### Séquence Automatique

```
[0:00-0:04] Slide 1: Titre
[0:04-0:08] Slide 2
[0:08-0:12] Slide 3
[0:12-0:20] Google Images: "images satellitaires agriculture"
[0:20-0:24] Slide 4: Architecture
[0:24-0:28] Slide 5: Scénario
[0:28-0:36] Google Images: "satellite images disease detection"
[0:36-0:40] Slide 6: Contact
```

**Durée totale:** ~40 secondes

---

## 📸 Méthode 2: Screenshots Manuels + Génération Vidéo

### Workflow

1. **Prendre screenshots manuellement**:
   - Slides PowerPoint (en mode présentation)
   - Pages Google Images
   - Nommer: `01_slide1.png`, `02_slide2.png`, etc.

2. **Placer dans dossier**:
   ```
   demo_screenshots/
     ├── 01_slide1_title.png
     ├── 02_slide2.png
     ├── 03_slide3.png
     ├── 04_google_images_search.png
     ├── 05_google_images_results.png
     ├── 06_slide4_architecture.png
     ├── 07_slide5_scenario.png
     ├── 08_google_images_disease.png
     └── 09_slide6_contact.png
   ```

3. **Générer vidéo**:
   ```bash
   python generate_video_from_screenshots.py
   ```

### Avantages

- ✅ Contrôle total sur chaque frame
- ✅ Pas besoin de Selenium/ChromeDriver
- ✅ Peut éditer screenshots avant génération
- ✅ Plus simple pour débuter

---

## 🛠️ Scripts Disponibles

### 1. `generate_demo_with_web_search.py`

**Fonctionnalités:**
- ✅ Ouvre PowerPoint automatiquement
- ✅ Démarre présentation (F5)
- ✅ Navigue entre slides
- ✅ Ouvre Google Images avec Selenium
- ✅ Effectue recherches automatiquement
- ✅ Alterne entre slides et navigateur
- ✅ Orchestre toute la séquence

**Utilisation:**
```bash
# Mode interactif (guide)
python generate_demo_with_web_search.py

# Mode automatique
python generate_demo_with_web_search.py auto
```

### 2. `generate_video_from_screenshots.py`

**Fonctionnalités:**
- ✅ Génère vidéo depuis screenshots
- ✅ Durées adaptées (slides: 4s, web: 8s)
- ✅ Ajoute numéros d'étape
- ✅ Export MP4 haute qualité

**Utilisation:**
```bash
# Générer vidéo
python generate_video_from_screenshots.py

# Afficher guide
python generate_video_from_screenshots.py guide
```

---

## 📋 Checklist Complète

### Avant Génération

- [ ] Présentation PowerPoint prête (`presentation_thales_template_correct.pptx`)
- [ ] OBS Studio installé (ou FFmpeg)
- [ ] Python dépendances installées (`pyautogui`, `selenium`, `moviepy`)
- [ ] ChromeDriver installé (pour Selenium)
- [ ] Écran propre (fermer apps inutiles)
- [ ] Résolution: 1920x1080 (recommandé)

### Pendant Génération

- [ ] Démarrer enregistrement OBS
- [ ] Exécuter script automatique
- [ ] Vérifier que tout fonctionne
- [ ] Laisser script s'exécuter
- [ ] Arrêter enregistrement à la fin

### Après Génération

- [ ] Vérifier vidéo générée
- [ ] Éditer si nécessaire (couper, transitions)
- [ ] Ajouter musique (optionnel)
- [ ] Exporter qualité optimale

---

## 🎨 Personnalisation

### Modifier Durées

Dans `generate_demo_with_web_search.py`:
```python
# Slides: 4 secondes
time.sleep(4)

# Web: 8 secondes
time.sleep(8)
```

### Modifier Recherches

```python
# Recherche 1
open_google_images_search("images satellitaires agriculture")

# Recherche 2
search_box.send_keys("satellite images disease detection agriculture")
```

### Modifier Présentation

```python
presentation_path = "presentation_thales_template_correct.pptx"
```

---

## 🔧 Dépannage

### Problème: Selenium ne trouve pas ChromeDriver

**Solution:**
```bash
# Installer ChromeDriver
winget install chromedriver

# Ou télécharger manuellement:
# https://chromedriver.chromium.org/downloads
```

### Problème: pyautogui ne fonctionne pas

**Solution:**
```bash
pip install pyautogui
# Vérifier que Python peut accéder à l'écran
```

### Problème: PowerPoint ne démarre pas

**Solution:**
- Vérifier que le fichier PPTX existe
- Ouvrir manuellement PowerPoint
- Démarrer présentation manuellement (F5)
- Script continuera avec navigation

### Problème: Vidéo de mauvaise qualité

**Solution:**
- Utiliser OBS Studio (meilleure qualité)
- Configurer OBS: 1920x1080, 30 FPS
- Bitrate: 5000-10000 kbps

---

## 📊 Comparaison Méthodes

| Méthode | Avantages | Inconvénients |
|---------|-----------|---------------|
| **Automatisation** | Rapide, répétable, fluide | Nécessite Selenium, plus complexe |
| **Screenshots** | Simple, contrôle total | Plus long, manuel |

---

## 🎬 Résultat Final

Vous obtiendrez une vidéo qui:
- ✅ Montre votre présentation Thales Alenia
- ✅ Démontre recherche Google Images satellitaires
- ✅ Alterne fluide entre slides et web
- ✅ Qualité professionnelle
- ✅ Prête pour partage (YouTube, LinkedIn, etc.)

**Durée:** ~40-60 secondes (selon configuration)

---

## 💡 Astuces Pro

1. **Répéter avant enregistrement final**
   - Tester séquence complète
   - Ajuster timing si nécessaire

2. **Optimiser affichage**
   - Mode plein écran pour navigateur
   - Masquer barre des tâches
   - Fermer notifications

3. **Post-production**
   - Ajouter transitions entre sections
   - Normaliser audio (si narration)
   - Ajouter logo/watermark

---

## 🚀 Quick Start

```bash
# 1. Installer dépendances
pip install pyautogui selenium moviepy

# 2. Installer ChromeDriver
winget install chromedriver

# 3. Démarrer OBS Studio enregistrement

# 4. Exécuter script
python generate_demo_with_web_search.py auto

# 5. Arrêter enregistrement à la fin
```

---

**✅ Prêt à générer votre vidéo de démo!**

