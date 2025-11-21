# Guide: Préparation d'un Template PowerPoint pour python-pptx

## 🎯 Comment Préparer votre Template

### 1. **Structure du Template**

Votre template `Modele_Decalage.pptx` a **11 layouts** différents:

| Layout | Nom | Usage Recommandé |
|--------|-----|------------------|
| 0 | TITLE | Slide titre (centré) |
| 1 | SECTION_HEADER | En-têtes de section |
| 2 | TITLE_AND_BODY | Contenu standard (titre + texte) |
| 3 | TITLE_AND_TWO_COLUMNS | Deux colonnes |
| 4 | TITLE_ONLY | Titre seul |
| 5 | ONE_COLUMN_TEXT | Texte une colonne |
| 6 | MAIN_POINT | Point principal (grand titre) |
| 7 | SECTION_TITLE_AND_DESCRIPTION | Section avec description |
| 8 | CAPTION_ONLY | Légende seule |
| 9 | BIG_NUMBER | Métriques importantes |
| 10 | BLANK | Slide vierge |

### 2. **Placeholders dans votre Template**

Chaque layout a des **placeholders** avec positions et tailles définies:

- **TITLE**: Position (0.90", 0.92"), Taille 8.21" x 1.04"
- **BODY**: Position (0.90", 2.18"), Taille 8.21" x 2.68"
- **CENTER_TITLE**: Position (2.03", 1.99"), Taille 5.86" x 1.58"
- **SUBTITLE**: Position (2.03", 3.73"), Taille 5.86" x 0.57"

### 3. **Règles pour un Bon Template**

#### ✅ DO (À Faire):

1. **Définir des Placeholders Clairs**
   - Titre principal (TITLE)
   - Contenu (BODY)
   - Sous-titre (SUBTITLE)
   - Numéro de slide (SLIDE_NUMBER)

2. **Respecter les Marges**
   - Les placeholders sont déjà positionnés dans les marges
   - Ne pas créer de nouveaux éléments en dehors

3. **Utiliser les Layouts Appropriés**
   - Layout 0 (TITLE) pour slide titre
   - Layout 2 (TITLE_AND_BODY) pour contenu standard
   - Layout 9 (BIG_NUMBER) pour métriques
   - Layout 3 (TWO_COLUMNS) pour comparaisons

4. **Styles Cohérents**
   - Polices définies dans le template
   - Couleurs de thème
   - Espacements cohérents

#### ❌ DON'T (À Éviter):

1. **Ne pas créer de nouveaux TextBoxes**
   - Utiliser les placeholders existants
   - Ne pas ajouter d'éléments en dehors des placeholders

2. **Ne pas ignorer les Marges**
   - Les placeholders respectent déjà les marges
   - Ne pas utiliser `Inches()` fixes

3. **Ne pas mélanger les Layouts**
   - Choisir le bon layout pour chaque slide
   - Ne pas forcer un layout qui ne correspond pas

---

## 📋 Mapping Contenu → Layouts

### Pour votre Présentation Thales:

| Slide | Contenu | Layout Recommandé |
|-------|---------|-------------------|
| 1 | Titre | Layout 0 (TITLE) |
| 2 | Le Défi (liste) | Layout 2 (TITLE_AND_BODY) |
| 3 | La Solution (4 cards) | Layout 3 (TITLE_AND_TWO_COLUMNS) ou Layout 2 |
| 4 | Architecture (diagramme) | Layout 4 (TITLE_ONLY) + image |
| 5 | Scénario 1 (workflow) | Layout 2 (TITLE_AND_BODY) |
| 6 | Scénario 2 (métriques) | Layout 9 (BIG_NUMBER) ou Layout 2 |
| 7 | Contact | Layout 2 (TITLE_AND_BODY) |

---

## 🔧 Comment le Script Doit Utiliser le Template

### Méthode Correcte:

```python
# 1. Charger template
prs = Presentation("template.pptx")

# 2. Utiliser le bon layout
slide = prs.slides.add_slide(prs.slide_layouts[0])  # TITLE layout

# 3. Remplir les placeholders (PAS créer de nouveaux éléments)
slide.shapes.title.text = "Mon Titre"

# 4. Pour BODY placeholder
body = slide.placeholders[1]  # Index du placeholder BODY
body.text = "Contenu ici"

# 5. Pour images: utiliser Layout 4 (TITLE_ONLY) ou BLANK
# Puis ajouter image dans les marges définies
```

### Méthode Incorrecte (ce que je faisais):

```python
# ❌ MAUVAIS: Créer de nouveaux textboxes
title_box = slide.shapes.add_textbox(Inches(1), Inches(2), ...)  # Ignore les marges!
```

---

## 📐 Marges de votre Template

D'après l'inspection:
- **Largeur slide**: 10.0"
- **Hauteur slide**: 5.6"
- **Zone de contenu**: ~8.21" de large (0.90" marges gauche/droite)
- **Position titre**: 0.90" depuis gauche
- **Position contenu**: 0.90" depuis gauche, 2.18" depuis haut

---

## 💡 Recommandations pour Améliorer le Template

### Si vous voulez modifier le template:

1. **Ajouter un Layout pour Images**
   - Layout avec TITLE + grande zone pour image
   - Ou utiliser Layout 4 (TITLE_ONLY) + ajouter image

2. **Layout pour Métriques**
   - Layout 9 (BIG_NUMBER) existe déjà
   - Parfait pour slides avec chiffres importants

3. **Layout pour Comparaisons**
   - Layout 3 (TITLE_AND_TWO_COLUMNS)
   - Parfait pour avant/après

4. **Vérifier les Marges**
   - S'assurer que tous les placeholders sont dans les marges
   - Marges typiques: 0.5" - 1" de chaque côté

---

## 🎨 Exemple de Template Idéal

### Structure:

```
Layout 0: TITLE
  - CENTER_TITLE (titre centré)
  - SUBTITLE (sous-titre)

Layout 1: SECTION_HEADER
  - TITLE (grand titre de section)

Layout 2: TITLE_AND_BODY
  - TITLE (titre)
  - BODY (contenu avec puces)

Layout 3: TITLE_AND_TWO_COLUMNS
  - TITLE
  - BODY (colonne gauche)
  - BODY (colonne droite)

Layout 4: TITLE_ONLY
  - TITLE
  - (espace libre pour image/diagramme)

Layout 9: BIG_NUMBER
  - TITLE (grand nombre)
  - BODY (description)

Layout 10: BLANK
  - (slide vierge, pour diagrammes complexes)
```

---

## ✅ Checklist Template

- [ ] Layouts bien nommés et organisés
- [ ] Placeholders positionnés dans les marges
- [ ] Styles cohérents (polices, couleurs)
- [ ] Layout pour chaque type de contenu
- [ ] Marges respectées partout
- [ ] Numéro de slide configuré
- [ ] Thème de couleurs défini

---

## 🔄 Prochaines Étapes

1. **Inspecter votre template** (fait ✓)
2. **Réécrire le script** pour utiliser les placeholders
3. **Tester avec votre template**
4. **Ajuster si nécessaire**

