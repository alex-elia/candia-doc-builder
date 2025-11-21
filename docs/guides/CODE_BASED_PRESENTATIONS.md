# Guide: Créer des Présentations Éditables avec du Code

## 🎯 Oui, c'est possible !

Comme **Gamma** (https://gamma.app), vous pouvez créer des présentations éditables programmatiquement.

---

## 📊 Format PPTX (Éditable dans PowerPoint)

### 1. **python-pptx** (Python) ⭐⭐⭐

**Le plus populaire** - Création programmatique de PPTX

#### Installation:
```bash
pip install python-pptx
```

#### Exemple de base:
```python
from pptx import Presentation
from pptx.util import Inches, Pt

# Créer présentation
prs = Presentation()

# Slide 1: Titre
slide1 = prs.slides.add_slide(prs.slide_layouts[0])
title = slide1.shapes.title
subtitle = slide1.placeholders[1]
title.text = "IA Embarquée pour Systèmes Satellitaires"
subtitle.text = "Alexandre GON - Architecture & Solutions IA"

# Slide 2: Contenu
slide2 = prs.slides.add_slide(prs.slide_layouts[1])
title2 = slide2.shapes.title
title2.text = "Architecture Système"
content = slide2.placeholders[1]
tf = content.text_frame
tf.text = "Système à bord"
p = tf.add_paragraph()
p.text = "Station terrestre"
p.level = 1

# Slide 3: Avec image
slide3 = prs.slides.add_slide(prs.slide_layouts[5])
slide3.shapes.add_picture('diagram.png', Inches(1), Inches(1), 
                         width=Inches(8), height=Inches(5))

# Sauvegarder
prs.save('presentation.pptx')
```

#### Avantages:
- ✅ **100% éditable** dans PowerPoint
- ✅ Contrôle total du formatage
- ✅ Ajout d'images, tableaux, graphiques
- ✅ Styles et thèmes personnalisables
- ✅ Open source

#### Fonctionnalités avancées:
```python
# Ajouter forme/forme personnalisée
from pptx.enum.shapes import MSO_SHAPE
shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, 
                                Inches(1), Inches(1), 
                                Inches(3), Inches(2))
shape.text = "Texte dans forme"

# Ajouter tableau
from pptx.enum.shapes import MSO_SHAPE
rows = 3
cols = 2
left = Inches(1)
top = Inches(2)
width = Inches(6)
height = Inches(3)
table = slide.shapes.add_table(rows, cols, left, top, width, height).table
table.cell(0, 0).text = "Cellule 1"
table.cell(0, 1).text = "Cellule 2"

# Formatage texte
from pptx.dml.color import RGBColor
paragraph = text_frame.paragraphs[0]
run = paragraph.runs[0]
run.font.bold = True
run.font.size = Pt(24)
run.font.color.rgb = RGBColor(15, 32, 66)  # Premium navy
```

### 2. **LibreOffice API** (Python/Java/C++)

Via **UNO API** de LibreOffice

```python
import uno
from com.sun.star.beans import PropertyValue

# Connexion à LibreOffice
localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext(
    "com.sun.star.bridge.UnoUrlResolver", localContext)
ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
smgr = ctx.ServiceManager

# Créer présentation
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
doc = desktop.loadComponentFromURL("private:factory/simpress", "_blank", 0, ())

# Ajouter slide
slides = doc.getDrawPages()
slide = slides.insertNewByIndex(0)

# Ajouter texte
textShape = doc.createInstance("com.sun.star.drawing.TextShape")
textShape.setPosition((1000, 1000))
textShape.setSize((10000, 2000))
textShape.String = "Titre de la slide"
slide.add(textShape)

# Sauvegarder
doc.storeAsURL("file:///path/to/presentation.odp", ())
```

### 3. **Apache POI** (Java)

Pour créer PPTX en Java

```java
import org.apache.poi.xslf.usermodel.*;

XMLSlideShow ppt = new XMLSlideShow();
XSLFSlide slide = ppt.createSlide();

// Titre
XSLFTextShape title = slide.createTextBox();
title.setAnchor(new java.awt.geom.Rectangle2D.Double(50, 50, 500, 100));
XSLFTextParagraph p = title.addNewTextParagraph();
XSLFTextRun r = p.addNewTextRun();
r.setText("Titre de la slide");
r.setFontSize(24.0);

// Sauvegarder
FileOutputStream out = new FileOutputStream("presentation.pptx");
ppt.write(out);
out.close();
```

---

## 🌐 Approches Web-Based (Comme Gamma)

### 1. **Gamma** (https://gamma.app) ⭐

**Approche moderne** - Présentations basées sur code/web

#### Caractéristiques:
- ✅ Éditable via interface web
- ✅ Code-like (Markdown + composants)
- ✅ Animations automatiques
- ✅ Responsive
- ✅ Partageable via lien

#### Format Gamma:
```markdown
# Titre Principal

## Slide 1
- Point 1
- Point 2

## Slide 2
![Image](diagram.png)

## Slide 3
**Texte en gras**
```

### 2. **Reveal.js** (HTML/JavaScript) ⭐⭐

**Présentations web interactives**

#### Exemple:
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="reveal.js/css/reveal.css">
    <link rel="stylesheet" href="reveal.js/css/theme/white.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section>
                <h1>IA Embarquée</h1>
                <p>Présentation pour Thales Alenia Space</p>
            </section>
            <section>
                <h2>Architecture Système</h2>
                <ul>
                    <li>Système à bord</li>
                    <li>Station terrestre</li>
                </ul>
            </section>
        </div>
    </div>
    <script src="reveal.js/js/reveal.js"></script>
    <script>Reveal.initialize();</script>
</body>
</html>
```

#### Avantages:
- ✅ Éditable (fichier HTML)
- ✅ Animations et transitions
- ✅ Responsive
- ✅ Open source

### 3. **Marp** (Markdown) ⭐⭐⭐

**Présentations depuis Markdown**

#### Installation:
```bash
npm install -g @marp-team/marp-cli
```

#### Exemple:
```markdown
---
marp: true
theme: default
---

# IA Embarquée pour Systèmes Satellitaires

## Architecture Système

- Système à bord
- Station terrestre

---

## Scénario 1: Détection d'Anomalies

![width:800px](diagram.png)
```

#### Compilation:
```bash
# Vers PDF
marp presentation.md -o presentation.pdf

# Vers PPTX (via HTML)
marp presentation.md -o presentation.html
# Puis convertir HTML → PPTX
```

#### Avantages:
- ✅ Syntaxe Markdown simple
- ✅ Thèmes personnalisables
- ✅ Export PDF, HTML, PPTX
- ✅ Éditable (fichier Markdown)

### 4. **Slidev** (Vue.js) ⭐⭐

**Présentations pour développeurs**

#### Installation:
```bash
npm install -g @slidev/cli
```

#### Exemple:
```markdown
---
theme: default
---

# IA Embarquée

## Architecture Système

- Système à bord
- Station terrestre

---

# Scénario 1

<v-clicks>

- Point 1
- Point 2
- Point 3

</v-clicks>
```

#### Avantages:
- ✅ Composants Vue.js
- ✅ Animations interactives
- ✅ Hot reload
- ✅ Export PDF, PPTX

### 5. **Quarto** (R/Python/Julia) ⭐⭐

**Présentations depuis code scientifique**

#### Exemple:
```markdown
---
title: "IA Embarquée"
format: revealjs
---

## Architecture Système

- Système à bord
- Station terrestre

```{python}
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.show()
```
```

#### Avantages:
- ✅ Intégration code (R/Python/Julia)
- ✅ Graphiques dynamiques
- ✅ Export multiple formats

---

## 🔄 Workflow Recommandé

### Pour PPTX Éditable (PowerPoint):

#### Option 1: python-pptx (Recommandé)
```
1. Écrire script Python
2. Générer PPTX
3. Ouvrir dans PowerPoint
4. Éditer manuellement si besoin
```

#### Option 2: Markdown → Marp → PPTX
```
1. Écrire Markdown
2. Compiler avec Marp
3. Convertir HTML → PPTX
4. Éditer dans PowerPoint
```

### Pour Présentations Web (Comme Gamma):

#### Option 1: Reveal.js
```
1. Écrire HTML
2. Déployer sur serveur web
3. Partageable via lien
4. Éditable (modifier HTML)
```

#### Option 2: Slidev
```
1. Écrire Markdown
2. Lancer serveur dev
3. Export PDF/PPTX
4. Éditable (modifier Markdown)
```

---

## 📋 Comparaison

| Outil | Format | Éditable | Code-Based | Export PPTX |
|-------|--------|----------|------------|-------------|
| **python-pptx** | PPTX | ✅ | ✅ | ✅ Direct |
| **Gamma** | Web | ✅ | ✅ | ⚠️ Via export |
| **Reveal.js** | HTML | ✅ | ✅ | ⚠️ Via conversion |
| **Marp** | Markdown | ✅ | ✅ | ✅ Oui |
| **Slidev** | Vue/MD | ✅ | ✅ | ✅ Oui |
| **Quarto** | MD/Code | ✅ | ✅ | ✅ Oui |

---

## 💡 Exemple Complet: python-pptx

### Créer présentation basée sur votre pitch:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# Couleurs premium
NAVY = RGBColor(15, 32, 66)
BLUE = RGBColor(30, 64, 124)
LIGHT = RGBColor(70, 130, 180)

# Créer présentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Slide 1: Titre
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "IA Embarquée pour Systèmes Satellitaires"
subtitle.text = "Alexandre GON\nArchitecture & Solutions IA"

# Slide 2: Résumé Exécutif
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Résumé Exécutif"
tf = content.text_frame
tf.text = "Opérations Autonomes"
p = tf.add_paragraph()
p.text = "Réduction des Coûts (80-99%)"
p = tf.add_paragraph()
p.text = "Maintenance Prédictive"
p = tf.add_paragraph()
p.text = "Solution Portfolio-Wide"

# Slide 3: Architecture
slide = prs.slides.add_slide(prs.slide_layouts[5])  # Blank
title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), 
                                     Inches(9), Inches(0.8))
title_frame = title_box.text_frame
title_frame.text = "Architecture Système"
title_frame.paragraphs[0].font.size = Pt(32)
title_frame.paragraphs[0].font.color.rgb = NAVY

# Ajouter diagramme (si image disponible)
# slide.shapes.add_picture('architecture.png', Inches(1), Inches(1.5),
#                          width=Inches(8), height=Inches(5))

# Slide 4: Scénarios
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Scénarios d'Usage"
tf = content.text_frame
tf.text = "Scénario 1: Détection d'Anomalies"
p = tf.add_paragraph()
p.text = "Scénario 2: Détection Agricole"
p.level = 1

# Sauvegarder
prs.save('presentation_thales.pptx')
print("Présentation créée: presentation_thales.pptx")
```

---

## 🚀 Avantages Code-Based

1. **Version Control**: Git pour suivre changements
2. **Automatisation**: Générer depuis données
3. **Réutilisabilité**: Templates et composants
4. **Consistance**: Formatage uniforme
5. **Intégration CI/CD**: Génération automatique

---

## 📚 Ressources

- **python-pptx**: https://python-pptx.readthedocs.io/
- **Gamma**: https://gamma.app
- **Reveal.js**: https://revealjs.com/
- **Marp**: https://marp.app/
- **Slidev**: https://sli.dev/
- **Quarto**: https://quarto.org/

---

## ⚠️ Limitations

1. **python-pptx**: 
   - ⚠️ Pas de support animations complexes
   - ⚠️ Formatage avancé nécessite code

2. **Web-based (Gamma, Reveal.js)**:
   - ⚠️ Export PPTX peut perdre formatage
   - ⚠️ Nécessite conversion

3. **Markdown-based (Marp, Slidev)**:
   - ⚠️ Limitations formatage vs PowerPoint natif
   - ⚠️ Diagrammes complexes nécessitent images

---

## 🎯 Recommandation Finale

**Pour votre cas (Thales Alenia Space):**

1. **PPTX Éditable**: **python-pptx**
   - Contrôle total
   - 100% compatible PowerPoint
   - Éditable après génération

2. **Présentation Web**: **Reveal.js** ou **Slidev**
   - Moderne et interactive
   - Partageable via lien
   - Éditable (code source)

3. **Rapidité**: **Marp**
   - Markdown simple
   - Export rapide
   - Bon compromis

**Voulez-vous que je crée un script python-pptx basé sur votre pitch document ?**

