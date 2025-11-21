# Comment Préparer votre Template PowerPoint pour python-pptx

## 🎯 Problème Identifié

Le script précédent créait de nouveaux éléments au lieu d'utiliser les **placeholders** du template, ce qui:
- ❌ Ignorait les marges définies
- ❌ Ne respectait pas le design du template
- ❌ Créait des éléments en dehors des zones prévues

## ✅ Solution: Utiliser les Placeholders

### 1. **Structure de votre Template**

Votre template `Modele_Decalage.pptx` a **11 layouts** avec placeholders bien définis:

```
Layout 0: TITLE
  - CENTER_TITLE (2.03", 1.99") - 5.86" x 1.58"
  - SUBTITLE (2.03", 3.73") - 5.86" x 0.57"

Layout 2: TITLE_AND_BODY
  - TITLE (0.90", 0.92") - 8.21" x 1.04"
  - BODY (0.90", 2.18") - 8.21" x 2.68"

Layout 3: TITLE_AND_TWO_COLUMNS
  - TITLE (0.90", 0.92") - 8.21" x 1.04"
  - BODY gauche (0.90", 2.18") - 4.03" x 2.68"
  - BODY droite (5.07", 2.18") - 4.03" x 2.68"

Layout 4: TITLE_ONLY
  - TITLE (0.90", 0.92") - 8.21" x 1.04"
  - (Espace libre pour images/diagrammes)

Layout 9: BIG_NUMBER
  - TITLE (1.52", 1.51") - 6.97" x 1.51" (pour grands nombres)
  - BODY (1.52", 3.13") - 6.97" x 0.70"
```

### 2. **Comment le Script Doit Utiliser le Template**

#### ✅ CORRECT (Nouveau Script):

```python
# 1. Charger template
prs = Presentation("template.pptx")

# 2. Utiliser le bon layout
slide = prs.slides.add_slide(prs.slide_layouts[2])  # TITLE_AND_BODY

# 3. Remplir les placeholders EXISTANTS
slide.shapes.title.text = "Mon Titre"  # Utilise placeholder TITLE

# 4. Remplir BODY placeholder
body = slide.placeholders[1]  # Index du placeholder BODY
body.text = "Contenu ici"

# 5. Pour images: utiliser Layout 4 (TITLE_ONLY)
# Puis ajouter image dans la zone de contenu (même marges que BODY)
slide.shapes.add_picture("image.jpg", 
                        Inches(0.90), Inches(2.18),  # Même position que BODY
                        width=Inches(8.21), height=Inches(2.68))  # Même taille
```

#### ❌ INCORRECT (Ancien Script):

```python
# ❌ MAUVAIS: Créer de nouveaux textboxes
title_box = slide.shapes.add_textbox(Inches(1), Inches(2), ...)
# Problème: Ignore les marges du template!
```

### 3. **Marges de votre Template**

D'après l'inspection:
- **Largeur slide**: 10.0"
- **Hauteur slide**: 5.6"
- **Marge gauche**: 0.90"
- **Marge droite**: ~0.89" (10.0" - 0.90" - 8.21")
- **Zone de contenu**: 8.21" de large
- **Position titre**: 0.90" depuis gauche, 0.92" depuis haut
- **Position contenu**: 0.90" depuis gauche, 2.18" depuis haut

## 📋 Guide de Préparation du Template

### Étape 1: Vérifier les Layouts

1. Ouvrir votre template dans PowerPoint
2. Vérifier que chaque layout a des **placeholders** bien définis:
   - TITLE (titre)
   - BODY (contenu)
   - SUBTITLE (sous-titre, optionnel)

### Étape 2: Vérifier les Marges

1. S'assurer que tous les placeholders sont dans les marges
2. Marges typiques: **0.5" - 1"** de chaque côté
3. Votre template: **0.90"** marges (parfait ✓)

### Étape 3: Organiser les Layouts

**Layouts recommandés pour votre présentation:**

| Slide Type | Layout à Utiliser | Pourquoi |
|------------|-------------------|----------|
| Titre | Layout 0 (TITLE) | CENTER_TITLE + SUBTITLE |
| Contenu texte | Layout 2 (TITLE_AND_BODY) | TITLE + BODY avec puces |
| Comparaison | Layout 3 (TWO_COLUMNS) | Deux colonnes pour avant/après |
| Image/Diagramme | Layout 4 (TITLE_ONLY) | Titre + espace pour image |
| Métriques | Layout 9 (BIG_NUMBER) | Grand nombre + description |

### Étape 4: Tester les Placeholders

Dans PowerPoint:
1. Créer une nouvelle slide avec chaque layout
2. Vérifier que les placeholders sont bien positionnés
3. Tester avec du texte pour voir si ça déborde

## 🔧 Améliorations Possibles du Template

### Si vous voulez modifier le template:

#### Option 1: Ajouter un Layout "Image avec Légende"

1. Dupliquer Layout 4 (TITLE_ONLY)
2. Ajouter un placeholder BODY en bas pour légende
3. Position: (0.90", 4.5"), Taille: 8.21" x 0.8"

#### Option 2: Layout "Métriques" Amélioré

Layout 9 existe déjà, mais vous pouvez:
- Ajuster la taille du TITLE pour grands nombres
- Ajouter un sous-titre pour contexte

#### Option 3: Layout "Comparaison Visuelle"

1. Utiliser Layout 3 (TWO_COLUMNS)
2. S'assurer que les colonnes sont bien espacées
3. Ajouter des labels au-dessus de chaque colonne

## ✅ Checklist Template

Avant d'utiliser le template avec python-pptx:

- [ ] Tous les layouts ont des placeholders définis
- [ ] Les placeholders sont dans les marges (0.5"-1" de chaque côté)
- [ ] Les styles (polices, couleurs) sont cohérents
- [ ] Il y a un layout pour chaque type de contenu
- [ ] Les numéros de slide sont configurés
- [ ] Le thème de couleurs est défini

## 📐 Exemple: Positions Correctes

### Pour ajouter une image dans Layout 4 (TITLE_ONLY):

```python
# Titre est à: (0.90", 0.92"), Taille: 8.21" x 1.04"
# Image doit être en dessous, même marges:
slide.shapes.add_picture("image.jpg",
                        Inches(0.90), Inches(2.18),  # Même gauche, en dessous du titre
                        width=Inches(8.21), height=Inches(2.68))  # Même largeur que BODY
```

### Pour deux colonnes (Layout 3):

```python
# Colonne gauche: (0.90", 2.18"), 4.03" x 2.68"
slide.shapes.add_picture("before.jpg",
                        Inches(0.90), Inches(2.18),
                        width=Inches(4.03), height=Inches(2.68))

# Colonne droite: (5.07", 2.18"), 4.03" x 2.68"
slide.shapes.add_picture("after.jpg",
                        Inches(5.07), Inches(2.18),
                        width=Inches(4.03), height=Inches(2.68))
```

## 🎯 Résultat Attendu

Avec le script corrigé:
- ✅ Utilise les placeholders du template
- ✅ Respecte les marges (0.90" de chaque côté)
- ✅ Utilise les layouts appropriés
- ✅ Images positionnées correctement
- ✅ Design cohérent avec le template

## 🔄 Test

Le nouveau script `generate_with_template_correct.py`:
1. ✅ Utilise Layout 0 pour titre
2. ✅ Utilise Layout 2 pour contenu texte
3. ✅ Utilise Layout 3 pour comparaisons
4. ✅ Utilise Layout 4 pour images
5. ✅ Respecte les positions des placeholders
6. ✅ Images dans les marges définies

---

**Votre template est déjà bien préparé!** Il a tous les layouts nécessaires avec des placeholders bien positionnés. Le nouveau script utilise maintenant ces placeholders correctement.

