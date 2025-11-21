# Guide: Enregistrement d'Écran avec Alternance Slides/Navigateur

## 🎯 Oui, c'est possible !

Vous pouvez créer une vidéo qui alterne entre:
- ✅ **Slides PowerPoint** (présentation)
- ✅ **Fonctionnalités dans navigateur** (démo logiciel)
- ✅ **Transitions fluides** entre les deux

---

## 🎬 Méthodes Disponibles

### 1. **Enregistrement Manuel avec OBS Studio** (Recommandé) ⭐⭐⭐

**Le plus simple et professionnel**

#### Installation:
1. Télécharger OBS Studio: https://obsproject.com/
2. Installer
3. Configurer:
   - Source: "Capture d'écran" (Display Capture)
   - Résolution: 1920x1080
   - FPS: 30

#### Workflow:
1. **Ouvrir OBS Studio**
2. **Démarrer enregistrement** (bouton "Démarrer l'enregistrement")
3. **Afficher slides** (PowerPoint en mode présentation)
4. **Alt+Tab** pour switcher vers navigateur
5. **Démontrer fonctionnalités**
6. **Alt+Tab** retour vers slides
7. **Continuer alternance**
8. **Arrêter enregistrement**

#### Avantages:
- ✅ Contrôle total du timing
- ✅ Qualité professionnelle
- ✅ Gratuit et open source
- ✅ Peut ajouter webcam, audio, etc.

---

### 2. **Enregistrement Automatisé avec Script Python** ⭐⭐

**Script qui orchestre tout automatiquement**

#### Prérequis:
```bash
pip install pyautogui
# Installer FFmpeg: https://ffmpeg.org/
```

#### Fonctionnalités du Script:
- ✅ Démarre enregistrement automatiquement
- ✅ Ouvre PowerPoint et démarre présentation
- ✅ Change de slide automatiquement
- ✅ Ouvre navigateur à URL spécifique
- ✅ Alterne entre slides et navigateur
- ✅ Arrête enregistrement

#### Utilisation:
```bash
python automated_screen_recording.py auto
```

#### Limitations:
- ⚠️ Nécessite que PowerPoint soit en mode présentation
- ⚠️ Nécessite que l'app soit accessible (localhost ou URL)
- ⚠️ Timing peut nécessiter ajustements

---

### 3. **Enregistrement avec Windows Game Bar** (Intégré) ⭐

**Simple mais basique**

#### Utilisation:
1. **Win + G** pour ouvrir Game Bar
2. **Win + Alt + R** pour démarrer/arrêter enregistrement
3. Alterner manuellement entre apps
4. **Win + Alt + R** pour arrêter

#### Avantages:
- ✅ Intégré Windows (pas d'installation)
- ✅ Simple et rapide

#### Limitations:
- ⚠️ Moins de contrôle que OBS
- ⚠️ Qualité limitée
- ⚠️ Pas d'édition intégrée

---

## 🎯 Workflow Recommandé pour votre Démo

### Séquence Type:

```
1. [REC START] Démarrer enregistrement OBS
2. [SLIDE 1] Titre - 3 secondes
3. [SLIDE 2] Le Défi - 5 secondes
4. [BROWSER] Alt+Tab → Ouvrir app → Démontrer détection anomalies - 15 secondes
5. [SLIDE 3] La Solution - 3 secondes
6. [BROWSER] Retour app → Démontrer traitement images - 15 secondes
7. [SLIDE 4] Architecture - 3 secondes
8. [SLIDE 5] Scénario 1 - 5 secondes
9. [BROWSER] Démontrer résultats/rapports - 15 secondes
10. [SLIDE 6] Contact - 3 secondes
11. [REC STOP] Arrêter enregistrement
```

**Durée totale:** ~1-2 minutes

---

## 🛠️ Script d'Automatisation Complet

J'ai créé `automated_screen_recording.py` qui:

1. **Démarre enregistrement** (FFmpeg ou OBS)
2. **Ouvre présentation** PowerPoint
3. **Démarre slideshow** (F5)
4. **Change de slides** automatiquement
5. **Ouvre navigateur** à votre URL
6. **Alterne** entre slides et navigateur
7. **Arrête enregistrement**

### Configuration:

```python
# Dans le script, modifier:
presentation_path = "presentation_thales_custom_template.pptx"
browser_url = "http://localhost:8080"  # Votre app
output_video = "complete_demo.mp4"
```

---

## 📋 Checklist pour Démo Parfaite

### Avant Enregistrement:

- [ ] Présentation PowerPoint prête
- [ ] Application fonctionnelle dans navigateur
- [ ] OBS Studio installé et configuré
- [ ] Écran propre (fermer apps inutiles)
- [ ] Résolution écran: 1920x1080 (recommandé)
- [ ] Script de timing préparé

### Pendant Enregistrement:

- [ ] Démarrer OBS enregistrement
- [ ] Suivre séquence (slides → browser → slides)
- [ ] Timing fluide (pas trop rapide)
- [ ] Parler clairement si narration
- [ ] Montrer fonctionnalités clés

### Après Enregistrement:

- [ ] Éditer vidéo (couper, ajouter transitions)
- [ ] Ajouter musique de fond (optionnel)
- [ ] Ajouter logo/watermark
- [ ] Exporter en qualité optimale

---

## 🎨 Améliorations Possibles

### 1. **Ajouter Narration**

```python
# Enregistrer audio séparément
# Puis combiner avec vidéo dans OBS ou avec moviepy
```

### 2. **Ajouter Webcam**

- OBS: Ajouter source "Video Capture Device"
- Position: Coin en bas à droite
- Taille: 320x240

### 3. **Transitions Animées**

- OBS: Ajouter transitions entre scènes
- Ou éditer dans post-production

### 4. **Annotations en Direct**

- OBS: Ajouter source "Image" pour flèches/highlights
- Ou utiliser outils comme "Pointer" dans OBS

---

## 🚀 Exemple: Démo Satellite AI Complète

### Séquence Proposée:

```
[0:00-0:03] Slide 1: Titre
[0:03-0:08] Slide 2: Le Défi
[0:08-0:23] Browser: Démontrer interface détection anomalies
            - Montrer dashboard
            - Montrer détection en temps réel
            - Montrer alertes
[0:23-0:26] Slide 3: La Solution
[0:26-0:41] Browser: Démontrer traitement images
            - Upload image satellite
            - Montrer traitement IA
            - Montrer rapport généré
[0:41-0:44] Slide 4: Architecture
[0:44-0:49] Slide 5: Scénario 1
[0:49-1:04] Browser: Démontrer résultats
            - Montrer métriques
            - Montrer comparaisons
[1:04-1:07] Slide 6: Contact
[STOP]
```

**Durée:** ~1 minute 10 secondes

---

## 💡 Astuces Pro

1. **Préparer Script**
   - Écrire script de narration
   - Noter timing pour chaque section
   - Répéter avant enregistrement

2. **Optimiser Affichage**
   - Fermer notifications
   - Masquer barre des tâches (optionnel)
   - Mode plein écran pour navigateur

3. **Qualité Vidéo**
   - Résolution: 1920x1080 minimum
   - FPS: 30 (fluide)
   - Bitrate: 5000-10000 kbps (OBS)

4. **Post-Production**
   - Couper silences
   - Ajouter transitions
   - Normaliser audio
   - Ajouter sous-titres (optionnel)

---

## 🔧 Installation Rapide

```bash
# Pour automatisation complète
pip install pyautogui

# FFmpeg (pour enregistrement programmatique)
# Télécharger: https://ffmpeg.org/download.html
# Ou via winget:
winget install ffmpeg
```

---

## 📝 Script Créé

J'ai créé `automated_screen_recording.py` qui peut:
- ✅ Démarrer enregistrement automatiquement
- ✅ Orchestrer slides et navigateur
- ✅ Alterner entre les deux
- ✅ Arrêter enregistrement

**Mode interactif** (recommandé pour débuter):
```bash
python automated_screen_recording.py
# Affiche guide et instructions
```

**Mode automatique** (avancé):
```bash
python automated_screen_recording.py auto
# Automatise tout (nécessite FFmpeg + pyautogui)
```

---

## ✅ Résultat

Vous obtiendrez une vidéo qui:
- ✅ Montre votre présentation PowerPoint
- ✅ Démontre votre logiciel dans le navigateur
- ✅ Alterne fluide entre les deux
- ✅ Qualité professionnelle
- ✅ Prête pour partage (YouTube, LinkedIn, etc.)

---

**Voulez-vous que je crée un script spécifique pour votre séquence de démo satellite AI?**

