# Guide: Présentations LaTeX et Conversion vers Formats Éditables

## 📊 Créer des Présentations avec LaTeX

### 1. **Beamer** (Recommandé) ⭐

**Le plus populaire** - Classe LaTeX dédiée aux présentations

#### Avantages:
- ✅ Professionnel et élégant
- ✅ Thèmes prédéfinis (Madrid, Berlin, Warsaw, Copenhagen, etc.)
- ✅ Animations et transitions
- ✅ Support mathématiques natif
- ✅ Génère directement PDF
- ✅ Compatible avec TikZ pour diagrammes

#### Exemple de base:
```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}
\title{Votre Titre}
\author{Votre Nom}
\begin{document}
\frame{\titlepage}
\begin{frame}{Slide 1}
Contenu ici
\end{frame}
\end{document}
```

#### Compilation:
```bash
pdflatex presentation.tex
# (2 passes pour table of contents)
```

#### Thèmes populaires:
- `Madrid` - Moderne, professionnel
- `Berlin` - Minimaliste
- `Warsaw` - Coloré
- `Copenhagen` - Élégant
- `Darmstadt` - Technique

### 2. **Powerdot**

Alternative à Beamer, moins utilisé aujourd'hui

### 3. **TeXPower**

Pour présentations dynamiques en ligne

---

## 🔄 Conversion LaTeX → Formats Éditables

### Option 1: **Pandoc** (Recommandé) ⭐⭐⭐

**L'outil le plus puissant** pour conversion de documents

#### Installation:
```powershell
# Windows (via winget ou chocolatey)
winget install --id JohnMacFarlane.Pandoc
# ou
choco install pandoc
```

#### Conversion LaTeX → DOCX:
```bash
pandoc document.tex -o document.docx
```

#### Conversion LaTeX → PPTX:
```bash
# Note: Pandoc ne supporte pas directement LaTeX → PPTX
# Solution: Convertir via Markdown intermédiaire
pandoc document.tex -t markdown -o temp.md
pandoc temp.md -o presentation.pptx
```

#### Conversion Beamer → PPTX:
```bash
# Beamer → HTML → PPTX (workaround)
pandoc presentation.tex -t html5 -o temp.html
# Puis utiliser outil HTML → PPTX
```

#### Avantages Pandoc:
- ✅ Open source
- ✅ Multi-formats (DOCX, PPTX, HTML, EPUB, etc.)
- ✅ Préserve structure et formatage
- ✅ Support Markdown, LaTeX, HTML

#### Limitations:
- ⚠️ Beamer → PPTX: Pas de support direct
- ⚠️ Diagrammes TikZ: Peuvent être perdus
- ⚠️ Formatage complexe: Peut nécessiter ajustements

### Option 2: **TeX4ht**

Convertisseur LaTeX → HTML/XML → Autres formats

```bash
# Installation (MiKTeX)
miktex-package-manager --install=tex4ht

# Conversion
htlatex document.tex
# Génère HTML, peut être converti ensuite
```

### Option 3: **LaTeXML**

Convertisseur LaTeX → XML/HTML/EPUB

```bash
# Installation
# Via package manager ou pip
pip install latexml

# Conversion
latexml document.tex > document.xml
latexmlpost document.xml
```

### Option 4: **Outils en ligne**

- **Conholdate**: https://products.conholdate.app/conversion/latex-to-docx
- **CloudConvert**: https://cloudconvert.com/latex-to-docx
- **Zamzar**: https://www.zamzar.com/convert/latex-to-docx/

⚠️ **Attention**: Confidentialité des documents

---

## 📝 Formats Ouverts pour Présentations

### 1. **ODP (OpenDocument Presentation)**

Format ouvert standardisé (ISO/IEC 26300)

#### Avantages:
- ✅ Format ouvert (pas propriétaire)
- ✅ Éditable avec LibreOffice, OpenOffice
- ✅ Compatible avec Google Slides (import)
- ✅ Standard ISO

#### Conversion LaTeX → ODP:
```bash
# Via Pandoc (si supporté)
pandoc presentation.tex -t odp -o presentation.odp

# Ou via LibreOffice
# 1. Générer PDF depuis LaTeX
# 2. Importer PDF dans LibreOffice Impress
# 3. Exporter en ODP
```

### 2. **HTML5 Presentations**

Présentations web interactives

#### Outils:
- **Reveal.js**: https://revealjs.com/
- **Impress.js**: https://github.com/impress/impress.js
- **Slidy**: Généré par Pandoc

#### Conversion:
```bash
# Pandoc → Reveal.js
pandoc presentation.tex -t revealjs -o presentation.html

# Pandoc → Slidy
pandoc presentation.tex -t slidy -o presentation.html
```

#### Avantages:
- ✅ Accessible via navigateur
- ✅ Animations et interactivité
- ✅ Pas besoin de logiciel spécialisé
- ✅ Responsive

---

## 🎯 Workflow Recommandé

### Pour Présentations Éditables:

#### Option A: Beamer → PDF → LibreOffice → ODP/PPTX
```
1. Créer présentation avec Beamer
2. Compiler en PDF
3. Ouvrir PDF dans LibreOffice Impress
4. Exporter en ODP ou PPTX
5. Éditer dans PowerPoint/LibreOffice
```

#### Option B: LaTeX → Markdown → Pandoc → PPTX
```
1. Convertir LaTeX en Markdown (pandoc)
2. Éditer Markdown si nécessaire
3. Convertir Markdown en PPTX (pandoc)
4. Ajuster formatage dans PowerPoint
```

#### Option C: Beamer → HTML → Outil de conversion
```
1. Convertir Beamer en HTML (pandoc)
2. Utiliser outil HTML → PPTX
3. Éditer dans PowerPoint
```

---

## 🔧 Outils Utiles

### IguanaTex (PowerPoint Add-in)

**Pour insérer du LaTeX dans PowerPoint existant**

- ✅ Insère équations LaTeX dans PowerPoint
- ✅ Rendu haute qualité
- ✅ Gratuit et open source
- 📥 https://github.com/Jonathan-LeRoux/IguanaTex

**Usage:**
1. Installer add-in dans PowerPoint
2. Insérer équation LaTeX
3. Rendu automatique en image vectorielle

---

## 📋 Comparaison Formats

| Format | Éditable | Ouvert | Qualité | Compatibilité |
|--------|----------|--------|---------|---------------|
| **PDF (Beamer)** | ❌ | ✅ | ⭐⭐⭐⭐⭐ | Universelle |
| **PPTX** | ✅ | ❌ | ⭐⭐⭐⭐ | Microsoft |
| **ODP** | ✅ | ✅ | ⭐⭐⭐⭐ | LibreOffice, Google |
| **HTML5** | ✅ | ✅ | ⭐⭐⭐⭐ | Navigateurs |
| **Markdown** | ✅ | ✅ | ⭐⭐⭐ | Éditeurs texte |

---

## 💡 Recommandations

### Pour votre cas (Thales Alenia Space):

1. **Présentation principale**: **Beamer → PDF**
   - Professionnel
   - Haute qualité
   - Pas d'édition nécessaire après génération

2. **Si besoin d'édition**: **Beamer → PDF → LibreOffice → ODP**
   - Format ouvert
   - Éditable
   - Compatible avec PowerPoint

3. **Pour collaboration**: **Beamer → HTML5 (Reveal.js)**
   - Partageable via lien
   - Interactif
   - Accessible partout

4. **Pour intégration PowerPoint**: **IguanaTex**
   - Insérer équations LaTeX
   - Garder format PowerPoint existant

---

## 🚀 Exemple Pratique

### Créer une présentation Beamer basée sur votre pitch:

```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}
\usecolortheme{default}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{graphicx}
\usepackage{tikz}

\title{IA Embarquée pour Systèmes Satellitaires}
\subtitle{Présentation pour Thales Alenia Space}
\author{Alexandre GON}
\institute{Architecture \& Solutions IA}
\date{\today}

\begin{document}

\frame{\titlepage}

\begin{frame}{Plan}
\tableofcontents
\end{frame}

\section{Introduction}
\begin{frame}{Résumé Exécutif}
\begin{itemize}
    \item Approche architecturale pour IA embarquée
    \item Solutions conteneurisées
    \item Applications: Observation, Communications, Défense
\end{itemize}
\end{frame}

\section{Architecture}
\begin{frame}{Architecture Système}
% Diagramme TikZ ici (même que dans document)
\end{frame}

\section{Scénarios}
\begin{frame}{Scénario 1: Détection d'Anomalies}
\begin{block}{Défi}
Détecter et résoudre les anomalies de manière autonome
\end{block}
\begin{alertblock}{Solution}
Agent LLM à bord pour surveillance continue
\end{alertblock}
\end{frame}

\section{Conclusion}
\begin{frame}{Conclusion}
\begin{enumerate}
    \item Solution techniquement faisable
    \item Économiquement viable
    \item Alignée avec les objectifs Thales
\end{enumerate}
\end{frame}

\end{document}
```

---

## 📚 Ressources

- **Beamer User Guide**: https://ctan.org/pkg/beamer
- **Pandoc Manual**: https://pandoc.org/MANUAL.html
- **Reveal.js**: https://revealjs.com/
- **IguanaTex**: https://github.com/Jonathan-LeRoux/IguanaTex

---

## ⚠️ Limitations Importantes

1. **Beamer → PPTX direct**: ❌ Non supporté nativement
2. **Diagrammes TikZ**: Peuvent être perdus en conversion
3. **Formatage complexe**: Nécessite ajustements manuels
4. **Animations Beamer**: Ne se convertissent pas en PPTX

**Solution**: Utiliser PDF Beamer comme source de vérité, convertir seulement si nécessaire pour édition.

