# Images pour Présentation Thales Alenia Space

## 📥 Liens Directs pour Télécharger

### 1. **background_space.jpg** (Slide 1 - Arrière-plan)
**Taille recommandée:** 1920x1080px

**Liens Unsplash (gratuit, haute qualité):**
- https://unsplash.com/photos/E7q00J_8N7A (Earth from space)
- https://unsplash.com/photos/5E5e49Bcav8 (Satellite view)
- https://unsplash.com/photos/6EnTPPSP6TQ (Space technology)

**Alternative Pexels:**
- https://www.pexels.com/photo/earth-planet-87651/
- https://www.pexels.com/search/space/

**Instructions:**
1. Cliquer sur l'image
2. Cliquer "Download" (gratuit, pas besoin de compte)
3. Renommer en `background_space.jpg`
4. Placer dans ce dossier

---

### 2. **architecture_diagram.png** (Slide 4)
**Taille recommandée:** 1200x800px

**Option A: Créer avec Draw.io**
1. Aller sur https://app.diagrams.net/
2. Créer diagramme: Terre (haut) → Satellite (bas)
3. File → Export as → PNG
4. Résolution: 300 DPI
5. Sauvegarder comme `architecture_diagram.png`

**Option B: Exporter depuis LaTeX**
Si vous avez déjà des diagrammes TikZ dans votre document LaTeX, vous pouvez les exporter en PNG.

**Option C: Utiliser template**
- Le script utilise automatiquement un fallback si l'image n'existe pas

---

### 3. **anomaly_workflow.png** (Slide 5)
**Taille recommandée:** 1200x600px

**Créer avec Draw.io:**
1. https://app.diagrams.net/
2. Créer workflow: Capteur → IA → Décision → Action → Sol
3. Utiliser flèches et boîtes
4. Exporter en PNG 300 DPI
5. Sauvegarder comme `anomaly_workflow.png`

---

### 4. **before_processing.jpg** (Slide 6 - Avant)
**Taille recommandée:** 800x600px

**Liens Unsplash:**
- Image satellite agricole: https://unsplash.com/photos/green-crop-field-aerial-view-during-daytime-8uZPynIu-rQ
- Champs agricoles: https://unsplash.com/s/photos/agricultural-field-satellite
- Vue aérienne: https://unsplash.com/s/photos/aerial-view-farm

**Alternative:**
- Image satellite réelle depuis Google Earth ou services similaires
- Image de champ agricole vue du ciel

---

### 5. **after_processing.jpg** (Slide 6 - Après)
**Taille recommandée:** 800x600px

**Options:**
- Même image que "before" mais avec annotations/overlay montrant l'analyse IA
- Image traitée montrant zones de stress hydrique ou maladie
- Créer avec outils d'annotation (GIMP, Photoshop, ou même PowerPoint)

**Ou utiliser:**
- Image de champ sain/irrigué pour contraste
- Image avec overlay NDVI (indices de végétation)

---

### 6. **logo.png** (Slide 7)
**Taille recommandée:** 256x256px ou 512x512px
**Format:** PNG avec transparence

Votre logo personnel ou logo EliaGo

---

### 7. **photo.jpg** (Slide 7)
**Taille recommandée:** 400x400px (carré)
**Format:** JPG haute qualité

Votre photo professionnelle

---

## 🎨 Icônes (Optionnel)

**Dossier:** `images/icons/`

### Télécharger depuis Flaticon (gratuit):
1. Aller sur https://www.flaticon.com/
2. Rechercher et télécharger:
   - **icon_cost.png**: Rechercher "money" ou "dollar"
   - **icon_time.png**: Rechercher "time" ou "clock"
   - **icon_network.png**: Rechercher "network" ou "connection"
   - **icon_satellite.png**: Rechercher "satellite"
   - **icon_ai.png**: Rechercher "artificial intelligence"

3. Format: PNG 256x256px, fond transparent
4. Gratuit avec attribution (mentionner dans présentation si nécessaire)

---

## ✅ Checklist

- [ ] `background_space.jpg` - Image espace/Terre (1920x1080px)
- [ ] `architecture_diagram.png` - Diagramme architecture (1200x800px)
- [ ] `anomaly_workflow.png` - Workflow détection (1200x600px)
- [ ] `before_processing.jpg` - Image avant traitement (800x600px)
- [ ] `after_processing.jpg` - Image après traitement (800x600px)
- [ ] `logo.png` - Votre logo (256x256px, transparent)
- [ ] `photo.jpg` - Photo professionnelle (400x400px)

**Optionnel:**
- [ ] `icons/icon_cost.png`
- [ ] `icons/icon_time.png`
- [ ] `icons/icon_network.png`
- [ ] `icons/icon_satellite.png`
- [ ] `icons/icon_ai.png`

---

## 💡 Astuce

**Si vous n'avez pas toutes les images:**
- Le script fonctionne quand même avec des fallbacks (texte/formes)
- Vous pouvez ajouter les images plus tard et régénérer
- Les images sont optionnelles mais améliorent l'impact visuel

---

## 🔄 Après Téléchargement

Une fois les images téléchargées:

```bash
# Régénérer la présentation avec images
python generate_with_premium_template.py
```

La présentation utilisera automatiquement les images disponibles!

