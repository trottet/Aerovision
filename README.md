# ✈️ AeroVision Pro

**AeroVision Pro** est une suite d'applications interactives de visualisation de données (Web Apps) dédiée à l'analyse et à la comparaison des performances aérodynamiques entre les **systèmes biologiques** (oiseaux, insectes, mammifères volants) et les **machines d'ingénierie** (avions, planeurs, drones, hypersonique).

Le but de ce projet est d'explorer l'espace paramétrique du vol, de repérer les innovations possibles et d'observer comment la nature et la technologie ont résolu les défis de la mécanique des fluides à différentes échelles (Nombres de Reynolds).

---

## 📂 Applications Incluses

### 1. 🦅 Comparateur Aérodynamique Complet (`aero-compare.html`)
L'application principale qui compare **25 entités volantes** (12 animaux, 13 machines).
- **Régimes de vitesse :** Du vol stationnaire du colibri (0 km/h) au X-43A Scramjet (11 265 km/h).
- **Polaires de vol :** Courbes interactives du taux de chute (Vz) en fonction de la vitesse (V) selon l'approximation parabolique.
- **Finesse (L/D) :** Comparaison de l'efficacité aérodynamique pure (Planeur ASW-22 à 60:1 vs Condor à 23:1).
- **Espace Paramétrique :** Nuages de points et graphiques à bulles croisant la masse, la charge alaire, l'allongement et le taux de chute.

### 2. 🍃 Analyse des Planeurs Ultra-Lents (`ultra-slow-gliders.html`)
Un focus exclusif sur le domaine de vol extrême des très basses vitesses (**Vmin ≤ 15 km/h**).
- Compare des entités comme le papillon monarque, la graine de Zanonia, les chauves-souris, face aux planeurs RC de compétition (F3K) et micro-drones.
- Analyse spécifique des masses et des polaires à très bas nombre de Reynolds.

### 3. 💡 Tableau de bord de l'Innovation (`index.html`)
Une vue orientée "Ingénierie & Design" évaluant 10 classes de machines sur 10 critères de performance (radar charts) pour identifier les "Gaps d'innovation" dans l'industrie aérospatiale actuelle.

---

## 🛠️ Technologie

- **Frontend pur :** HTML5, CSS3, JavaScript vanilla.
- **Visualisation de données :** Graphiques propulsés par [Chart.js (v4.4.0)](https://www.chartjs.org/).
- **Déploiement :** Conçu pour fonctionner entièrement côté client, hébergé via GitHub Pages.

## 🔗 Liens Publics (GitHub Pages)

Si GitHub Pages est activé sur la branche `main`, les applications sont directement consultables en ligne :
- App Principale : [https://trottet.github.io/Aerovision/aero-compare.html](https://trottet.github.io/Aerovision/aero-compare.html)
- Planeurs Ultra-Lents : [https://trottet.github.io/Aerovision/ultra-slow-gliders.html](https://trottet.github.io/Aerovision/ultra-slow-gliders.html)
- Innovation : [https://trottet.github.io/Aerovision/index.html](https://trottet.github.io/Aerovision/index.html)

## 📚 Sources des données
Les données proviennent de la littérature aéronautique et ornithologique (Pennycuick, UIUC Airfoil Data Site, NASA, Jane's All the World's Aircraft). Plus de détails dans l'onglet "Références" de l'application principale.
