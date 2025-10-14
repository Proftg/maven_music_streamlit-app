# 🎵 Maven Music - Customer Churn Analysis Dashboard

## Vue d'ensemble du projet

Maven Music est une plateforme d'analyse avancée dédiée à l'investigation des facteurs contribuant à l'attrition des clients dans un service de streaming musical. Ce projet intègre des techniques d'analyse exploratoire des données (EDA), d'ingénierie des caractéristiques et de visualisation statistique pour identifier les patterns comportementaux associés au churn des utilisateurs.

## Objectifs

L'initiative repose sur les objectifs académiques et professionnels suivants :

- **Identification des facteurs de churn** : Déterminer les variables comportementales et structurelles corrélées à l'attrition
- **Analyse comparative** : Évaluer les taux de churn en fonction des tiers d'abonnement et des niveaux d'engagement
- **Feature engineering** : Construire des variables dérivées capturant les dynamiques utilisateur complexes
- **Insights stratégiques** : Développer des recommandations quantifiées pour les interventions de rétention

## Caractéristiques principales

### 📊 Pages du tableau de bord

1. **Home** - Aperçu du projet et métriques synthétiques
2. **Data Overview** - Analyse descriptive et qualité des données
3. **Exploratory Analysis** - Visualisations distributionnelles univariées et bivariées
4. **Churn Analysis** - Analyse segmentée du churn par tier et engagement
5. **Feature Engineering** - Documentation des variables créées et étapes de préparation
6. **Insights & Recommendations** - Résumé des découvertes et plan d'action

### 🔧 Technologies utilisées

- **Streamlit** : Framework de visualisation interactive
- **Pandas** : Manipulation et transformation des données
- **NumPy** : Calculs numériques vectorisés
- **Matplotlib & Seaborn** : Visualisation statistique
- **Python 3.8+** : Langage de programmation principal

## Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Clonez ou téléchargez le projet**
   ```bash
   git clone <repository_url>
   cd maven-music-churn-analysis
   ```

2. **Créez un environnement virtuel** (recommandé)
   ```bash
   python -m venv venv
   
   # Activation (Windows)
   venv\Scripts\activate
   
   # Activation (macOS/Linux)
   source venv/bin/activate
   ```

3. **Installez les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ajoutez le logo Maven Music**
   - Nommez votre image `maven_logo.png`
   - Placez-la dans le répertoire racine du projet

## Utilisation

### Lancer l'application

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse `http://localhost:8501`

### Navigation

Utilisez la barre latérale (sidebar) pour naviguer entre les différentes pages d'analyse. Chaque page offre une perspective distinct du phénomène de churn.

## Structure des données

### Variables du dataset

| Variable | Type | Description |
|----------|------|-------------|
| customer_id | Integer | Identifiant unique du client |
| subscription_tier | Categorical | Tier d'abonnement (Free, Premium, Student) |
| subscription_duration_days | Integer | Durée en jours depuis l'inscription |
| total_listens | Integer | Nombre total de titres écoutés |
| playlist_count | Integer | Nombre de playlists créées |
| days_since_activity | Integer | Jours écoulés depuis la dernière activité |
| churn | Binary | Statut de churn (0 = Conservé, 1 = Churné) |

### Variables dérivées

- **engagement_level** : Catégorisation trinaire basée sur la fréquence d'écoute
- **churn_rate** : Proportion d'utilisateurs ayant churné par segment

## Résultats clés

### Découvertes principales

1. **Impact de l'engagement** : Les utilisateurs avec engagement faible présentent des taux de churn significativement plus élevés
2. **Variation par tier** : Les patterns d'attrition diffèrent substantiellement entre les tiers d'abonnement
3. **Fenêtre critique** : L'inactivité prolongée (>30 jours) est fortement associée au churn
4. **Effet de la curation** : La création de playlists corrèle négativement avec l'attrition

### Recommandations stratégiques

| Priorité | Action | Segment cible | Impact anticipé |
|----------|--------|-----------------|-----------------|
| Haute | Campagnes de ré-engagement | Utilisateurs inactifs (>30j) | Réduction du churn de 15-20% |
| Haute | Incitations Premium | Conversion Free-to-Premium | Augmentation ARPU |
| Moyenne | Recommandations personnalisées | Utilisateurs faible engagement | +25% engagement |
| Moyenne | Tutoriels création playlists | Nouveaux utilisateurs | Rétention +90j améliorée |
| Basse | Fonctionnalités communautaires | Utilisateurs actifs | Renforcement du lien communautaire |

## Phases du projet

- ✅ **Collecte de données** - Agrégation historique des données d'abonnement
- ✅ **Nettoyage des données** - Assurance qualité et standardisation
- ◈ **Analyse exploratoire** - Identification de patterns et visualisations
- ◈ **Ingénierie des features** - Création de variables dérivées
- ⊗ **Préparation pour modélisation** - Structuration pour ML (à venir)

## Architecture du code

```
maven-music-churn-analysis/
├── app.py                 # Application Streamlit principale
├── maven_logo.png         # Logo Maven Music
├── requirements.txt       # Dépendances Python
├── README.md              # Documentation du projet
└── data/                  # Données (généré dynamiquement)
    └── sample_data.csv    # Données d'exemple
```

## Extensions futures

1. **Modélisation prédictive** : Développement de modèles de classification (Logistic Regression, Random Forest, XGBoost)
2. **Scoring de propension** : Calcul de scores de propension au churn par client
3. **Analyse de cohorte** : Suivi longitudinal par cohorte d'inscription
4. **A/B Testing** : Évaluation d'interventions de rétention
5. **Automatisation** : Pipeline ETL pour mise à jour quotidienne/hebdomadaire

## Configuration système recommandée

- **Processeur** : Dual-core minimum
- **Mémoire RAM** : 4 GB minimum (8 GB recommandé)
- **Espace disque** : 500 MB minimum
- **Navigateur** : Chrome, Firefox, Safari (version récente)

## Dépannage

### L'application ne se lance pas
```bash
# Vérifiez que Streamlit est correctement installé
pip install --upgrade streamlit

# Relancez l'application
streamlit run app.py
```

### Erreur concernant le logo
- Assurez-vous que `maven_logo.png` est dans le répertoire racine
- Vérifiez que le nom du fichier correspond exactement (majuscules/minuscules)

### Performance lente
- Réduisez la taille du dataset dans `load_sample_data()`
- Augmentez l'allocation mémoire de Python
- Fermez les autres applications consommatrices de ressources

## Contributeurs

Projet développé comme initiative de science des données pour Maven Music - 2025

## Licence

Ce projet est fourni à titre éducatif et professionnel. Tous les droits sont réservés à Maven Music.

## Contact et support

Pour toute question ou demande de fonctionnalités supplémentaires, veuillez consulter la documentation Streamlit ou contacter l'équipe de projet.

---

**Dernière mise à jour** : Octobre 2025  
**Version** : 1.0  
**Statut** : Phase de préparation des données