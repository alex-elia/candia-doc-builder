# Guide: Templates Visuels et Images pour Présentations PPTX

## 🎨 Utiliser des Templates PowerPoint

### 1. **Créer depuis un Template Existant**

```python
from pptx import Presentation

# Charger un template PowerPoint (.potx ou .pptx)
prs = Presentation("mon_template.potx")

# Ou utiliser un fichier PPTX comme template
prs = Presentation("template_existant.pptx")
```

### 2. **Où Trouver des Templates Professionnels**

#### Gratuits:
- **PowerPoint Templates (Microsoft)**: https://templates.office.com/
- **SlidesCarnival**: https://www.slidescarnival.com/ (gratuit, premium look)
- **Canva**: https://www.canva.com/presentations/templates/
- **Google Slides Templates**: https://slidesgo.com/
- **FreePPT**: https://www.free-powerpoint-templates-design.com/

#### Premium:
- **Envato Elements**: https://elements.envato.com/presentation-templates
- **GraphicRiver**: https://graphicriver.net/presentation-templates
- **24Slides**: https://24slides.com/templates

#### Spécifiques Technique/Spatial:
- **NASA Templates**: Rechercher "NASA PowerPoint template"
- **Space/Science Templates**: Sur SlidesCarnival, rechercher "space", "technology"

### 3. **Créer votre Propre Template**

1. Créer un fichier PowerPoint avec:
   - Couleurs de thème personnalisées
   - Polices (Charter, Helvetica)
   - Layouts de slides
   - Arrière-plans

2. Sauvegarder comme `.potx` (PowerPoint Template)

3. Utiliser dans le script:
```python
prs = Presentation("mon_template.potx")
```

---

## 🖼️ Intégrer des Images

### 1. **Méthode Basique**

```python
from pptx.util import Inches

# Ajouter image simple
slide.shapes.add_picture("image.png", Inches(1), Inches(1))

# Avec taille spécifique
slide.shapes.add_picture("image.png", Inches(1), Inches(1),
                        width=Inches(5), height=Inches(3))
```

### 2. **Images Recommandées pour votre Présentation**

#### Slide 1 - Titre:
- `background_space.jpg` - Image d'espace/satellite en arrière-plan
- Sources: Unsplash (https://unsplash.com/s/photos/space), Pexels

#### Slide 4 - Architecture:
- `architecture_diagram.png` - Diagramme d'architecture
- Créer avec: Draw.io, Lucidchart, ou exporter depuis LaTeX TikZ

#### Slide 5 - Scénario 1:
- `anomaly_workflow.png` - Diagramme de workflow
- `satellite_icon.png` - Icône satellite

#### Slide 6 - Scénario 2:
- `before_processing.jpg` - Image satellite avant traitement
- `after_processing.jpg` - Image après traitement IA
- `agricultural_field.jpg` - Champ agricole

#### Slide 7 - Contact:
- `logo.png` - Votre logo
- `photo.jpg` - Votre photo professionnelle

### 3. **Icônes pour Slides**

#### Sources d'Icônes Gratuites:
- **Flaticon**: https://www.flaticon.com/ (gratuit avec attribution)
- **Icons8**: https://icons8.com/ (gratuit avec attribution)
- **Font Awesome**: https://fontawesome.com/icons (gratuit)
- **Material Icons**: https://fonts.google.com/icons (gratuit)

#### Icônes Utiles:
- `icon_cost.png` - Dollar/euro
- `icon_time.png` - Horloge
- `icon_network.png` - Réseau/communication
- `icon_money.png` - Argent
- `icon_satellite.png` - Satellite
- `icon_ai.png` - Intelligence artificielle

### 4. **Optimisation des Images**

#### Formats Recommandés:
- **Photos**: JPG (compression 80-90%)
- **Diagrammes/Icônes**: PNG (transparence)
- **Logos**: PNG ou SVG (vectoriel)

#### Tailles Recommandées:
- **Arrière-plan**: 1920x1080px (16:9)
- **Diagrammes**: 1200x800px minimum
- **Icônes**: 256x256px ou 512x512px
- **Photos**: 800x600px minimum

#### Outils d'Optimisation:
- **TinyPNG**: https://tinypng.com/ (compression)
- **Squoosh**: https://squoosh.app/ (compression avancée)
- **GIMP/Photoshop**: Redimensionnement et optimisation

---

## 🎯 Structure de Dossiers Recommandée

```
satellite-ai-prototype/
├── docs/
│   ├── generate_thales_presentation_enhanced.py
│   ├── images/
│   │   ├── background_space.jpg
│   │   ├── architecture_diagram.png
│   │   ├── anomaly_workflow.png
│   │   ├── before_processing.jpg
│   │   ├── after_processing.jpg
│   │   ├── logo.png
│   │   ├── photo.jpg
│   │   └── icons/
│   │       ├── icon_cost.png
│   │       ├── icon_time.png
│   │       └── ...
│   └── templates/
│       └── thales_template.potx
```

---

## 💻 Utilisation du Script Amélioré

### 1. **Avec Images Seulement**

```bash
# Créer le dossier images et y placer vos images
mkdir images

# Générer la présentation
python generate_thales_presentation_enhanced.py
```

### 2. **Avec Template Personnalisé**

```bash
# Utiliser un template existant
python generate_thales_presentation_enhanced.py mon_template.potx
```

### 3. **Script Automatique**

Le script détecte automatiquement:
- ✅ Images présentes → les utilise
- ❌ Images absentes → utilise fallback (texte/formes)

---

## 🎨 Exemples de Templates Visuels

### Template "Space/Technology"

**Couleurs:**
- Fond: Noir profond (#0A0A0A)
- Accent: Bleu spatial (#00D4FF)
- Texte: Blanc/Gris clair

**Éléments:**
- Étoiles en arrière-plan
- Lignes de connexion animées
- Formes géométriques modernes

### Template "Professional Blue"

**Couleurs:**
- Fond: Blanc/Gris très clair
- Accent: Bleu professionnel (#1E3A8A)
- Texte: Noir/Gris foncé

**Éléments:**
- Bordures arrondies
- Ombres légères
- Gradients subtils

### Template "Minimalist"

**Couleurs:**
- Fond: Blanc pur
- Accent: Une seule couleur (Navy)
- Texte: Noir

**Éléments:**
- Beaucoup d'espace blanc
- Typographie forte
- Formes simples

---

## 🔧 Personnalisation Avancée

### 1. **Ajouter des Gradients**

```python
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR

shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, ...)
fill = shape.fill
fill.gradient()
fill.gradient_angle = 45.0
fill.gradient_stops[0].color.rgb = RGBColor(15, 32, 66)
fill.gradient_stops[1].color.rgb = RGBColor(70, 130, 180)
```

### 2. **Ajouter des Ombres**

```python
shadow = shape.shadow
shadow.inherit = False
shadow.style = 'outer'
shadow.color.rgb = RGBColor(0, 0, 0)
shadow.transparency = 0.5
```

### 3. **Ajouter des Bordures Arrondies**

```python
shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ...)
shape.adjustments[0] = 0.1  # Ajuster le rayon
```

### 4. **Superposer des Images avec Transparence**

```python
# Image de fond
bg = slide.shapes.add_picture("background.jpg", ...)

# Overlay semi-transparent
overlay = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, ...)
overlay.fill.solid()
overlay.fill.fore_color.rgb = RGBColor(0, 0, 0)
overlay.fill.transparency = 0.6  # 60% transparent
```

---

## 📊 Diagrammes et Graphiques

### 1. **Créer des Diagrammes avec Python**

```python
import matplotlib.pyplot as plt
import numpy as np

# Créer graphique
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(['Avant', 'Après'], [500, 1], color=['red', 'green'])
ax.set_ylabel('Taille (MB)')
plt.savefig('images/comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Ajouter à slide
slide.shapes.add_picture('images/comparison.png', Inches(2), Inches(2),
                        width=Inches(8), height=Inches(4))
```

### 2. **Exporter depuis LaTeX TikZ**

```latex
% Dans votre document LaTeX
\begin{tikzpicture}
% Votre diagramme
\end{tikzpicture}

% Compiler et exporter en PNG
% Utiliser pdftoppm ou convert (ImageMagick)
```

### 3. **Outils Externes**

- **Draw.io**: https://app.diagrams.net/ (gratuit, export PNG/SVG)
- **Lucidchart**: https://www.lucidchart.com/ (gratuit limité)
- **Excalidraw**: https://excalidraw.com/ (gratuit, style hand-drawn)

---

## 🚀 Workflow Complet

### Étape 1: Préparer les Assets

1. Télécharger/créer images
2. Optimiser tailles et formats
3. Organiser dans dossier `images/`

### Étape 2: Créer/Choisir Template

1. Créer template PowerPoint avec couleurs/thèmes
2. Sauvegarder comme `.potx`
3. Ou utiliser template existant

### Étape 3: Générer Présentation

```bash
python generate_thales_presentation_enhanced.py mon_template.potx
```

### Étape 4: Finaliser dans PowerPoint

1. Ouvrir présentation générée
2. Ajuster positions/images si nécessaire
3. Ajouter animations
4. Exporter en PDF si besoin

---

## 📝 Checklist Images

- [ ] Image arrière-plan titre (1920x1080px)
- [ ] Diagramme architecture (1200x800px)
- [ ] Diagramme workflow (1200x600px)
- [ ] Images avant/après traitement (800x600px)
- [ ] Logo (256x256px, PNG transparent)
- [ ] Photo professionnelle (400x400px)
- [ ] Icônes (256x256px, PNG transparent)
- [ ] Toutes images optimisées (< 500KB chacune)

---

## 🎯 Résultat Attendu

Avec images et template, votre présentation aura:
- ✅ Design professionnel et moderne
- ✅ Images impactantes
- ✅ Diagrammes clairs
- ✅ Cohérence visuelle
- ✅ Prêt pour présentation client

---

## 💡 Astuces

1. **Cohérence**: Utiliser même palette de couleurs partout
2. **Qualité**: Images haute résolution (300 DPI pour impression)
3. **Légèreté**: Optimiser images pour chargement rapide
4. **Accessibilité**: Bon contraste texte/fond
5. **Branding**: Utiliser vos couleurs/logo partout

---

## 🔗 Ressources Utiles

- **python-pptx Documentation**: https://python-pptx.readthedocs.io/
- **Unsplash (Photos gratuites)**: https://unsplash.com/
- **Pexels (Photos gratuites)**: https://www.pexels.com/
- **Flaticon (Icônes)**: https://www.flaticon.com/
- **Canva (Templates)**: https://www.canva.com/

