# Génération de Présentation PPTX pour Thales Alenia Space

## 📋 Prérequis

### 1. Installer Python

**Windows:**
```powershell
# Option 1: Via Microsoft Store (recommandé)
# Chercher "Python" dans Microsoft Store

# Option 2: Via winget
winget install Python.Python.3.11

# Option 3: Télécharger depuis python.org
# https://www.python.org/downloads/
```

### 2. Installer python-pptx

```bash
pip install python-pptx
```

Ou si vous avez plusieurs versions Python:
```bash
pip3 install python-pptx
py -m pip install python-pptx
```

## 🚀 Utilisation

### Générer la présentation:

```bash
python generate_thales_presentation.py
```

Ou:
```bash
py generate_thales_presentation.py
python3 generate_thales_presentation.py
```

### Résultat:

Le script génère: `presentation_thales_alenia.pptx`

## 📊 Contenu de la Présentation

La présentation contient **12 slides**:

1. **Titre** - IA Embarquée pour Systèmes Satellitaires
2. **Le Défi** - Problèmes actuels (coûts, délais, pannes)
3. **La Solution** - 4 propositions de valeur avec métriques
4. **Architecture Système** - Vue d'ensemble Terre/Satellite
5. **Architecture IA à Bord** - Couches techniques
6. **Scénario 1** - Détection d'Anomalies (défi/solution/exemple)
7. **Scénario 2** - Détection Agricole (métriques impactantes)
8. **Faisabilité Technique** - OS & Performance
9. **Valeur par Type** - Observation/Communication/Défense
10. **Feuille de Route** - 3 phases avec timeline
11. **Call to Action** - Prochaines étapes
12. **Contact** - Informations de contact

## 🎨 Design

- **Couleurs Premium**: Navy, Blue, Light Blue, Gold (matching LaTeX doc)
- **Format 16:9**: Aspect ratio moderne
- **Design Impactant**: Boxes colorées, métriques en évidence
- **Orienté Pitch**: Structure narrative (Problème → Solution → Valeur)

## ✏️ Édition

Le fichier PPTX généré est **100% éditable** dans:
- Microsoft PowerPoint
- LibreOffice Impress
- Google Slides (après upload)

Vous pouvez:
- Modifier le texte
- Ajuster les couleurs
- Ajouter des images
- Réorganiser les slides
- Ajouter des animations

## 🔧 Personnalisation

Pour modifier la présentation, éditez `generate_thales_presentation.py`:

- **Couleurs**: Modifier les variables `NAVY`, `BLUE`, `LIGHT_BLUE`, `GOLD`
- **Contenu**: Modifier le texte dans chaque slide
- **Structure**: Ajouter/supprimer des slides
- **Formatage**: Ajuster les tailles de police, positions, etc.

## 📝 Notes

- Les diagrammes complexes (TikZ) ne sont pas inclus automatiquement
- Vous pouvez ajouter des images avec: `slide.shapes.add_picture('image.png', ...)`
- Le script utilise des formes simples pour les diagrammes (boxes, arrows)

## 🐛 Dépannage

### Python non trouvé:
```powershell
# Vérifier installation
py --version
python3 --version

# Si non installé, installer depuis Microsoft Store ou python.org
```

### Module python-pptx non trouvé:
```bash
pip install --upgrade python-pptx
```

### Erreur de permissions:
```powershell
# Exécuter PowerShell en tant qu'administrateur
# Ou installer dans user space:
pip install --user python-pptx
```

