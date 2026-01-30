# 🍊 Prédiction du Churn Client - Orange Cameroun

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ML](https://img.shields.io/badge/ML-XGBoost%20%7C%20LightGBM%20%7C%20CatBoost-orange)](https://github.com/)

> Système intelligent de prédiction et prévention du churn pour optimiser la rétention client chez Orange Cameroun

![Churn Prediction](https://img.shields.io/badge/Churn%20Rate-26.5%25-red)
![Clients](https://img.shields.io/badge/Clients-13%2C526-brightgreen)
![Accuracy](https://img.shields.io/badge/Target%20F1--Score-%E2%89%A50.75-success)

---

## 📊 Contexte Business

Le churn représente **15% des clients** annuellement chez Orange Cameroun, soit une perte estimée à **3 milliards FCFA**. 

**Objectif** : Réduire ce taux à **12%** grâce à l'intelligence artificielle et l'analyse prédictive.

### 💰 Impact Financier Estimé
- **Réduction churn** : 15% → 12% (-20%)
- **Gain annuel** : **450 millions FCFA**
- **ROI campagnes** : +300%
- **Clients sauvés** : ~14,400 clients/an

---

## 🎯 Objectifs du Projet

### Objectifs Techniques
- ✅ Prédire le churn avec **F1-score ≥ 0.75**
- ✅ Identifier clients à risque **60 jours avant** leur départ
- ✅ Temps de prédiction < 100ms par client
- ✅ Pipeline automatisé et déployable

### Objectifs Business
- 📊 Segmenter clients à risque en **5-7 profils actionnables**
- 🎯 Générer **recommandations personnalisées** par segment
- 📈 Calculer **ROI des campagnes** de rétention
- 💼 Dashboard interactif pour équipes marketing

---

## 📁 Structure du Projet
```
prediction-churn-orange/
│
├── donnees/                    # Données (gitignored)
│   ├── brutes/                # 4 datasets (13,526 clients)
│   ├── traitees/              # Données preprocessées
│   └── archives/              # Doublons archivés
│
├── notebooks/                  # Analyses Jupyter
│   ├── analyse_datasets.ipynb # Validation datasets
│   └── exploration_complete.ipynb # EDA complète
│
├── src/                        # Code source
│   ├── donnees/               # Chargement & preprocessing
│   ├── features/              # Feature engineering
│   ├── modeles/               # ML models
│   ├── visualisation/         # Dashboards
│   └── api/                   # API REST
│
├── modeles/                   # Modèles entraînés
├── rapports/                  # Livrables & visualisations
├── tests/                     # Tests unitaires
└── scripts/                   # Scripts utilitaires
```

---

## 📊 Datasets

### Datasets Validés (4)

| Dataset | Clients | Variables | Churn % | Usage |
|---------|---------|-----------|---------|-------|
| **IBM Telco** | 7,043 | 21 | 26.5% | Training principal |
| **Orange Kaggle Train** | 2,666 | 20 | 14.6% | Validation croisée |
| **Orange Kaggle Test** | 667 | 20 | 14.2% | Test final |
| **Orange Alt** | 3,150 | 14 | 15.7% | Robustesse |

**Total** : **13,526 clients** disponibles

### Variables Clés
- **Démographiques** : Âge, localisation, ancienneté
- **Comportementales** : Usage voix/data/SMS, fréquence
- **Contractuelles** : Type forfait, options souscrites
- **Financières** : ARPU, dépenses mensuelles

---

## 🚀 Installation & Utilisation

### Prérequis
- Python 3.10+
- Conda (recommandé)
- Git

### Installation Rapide
```bash
# Cloner le repository
git clone https://github.com/TON-USERNAME/prediction-churn-orange-cameroun.git
cd prediction-churn-orange-cameroun

# Créer environnement
conda create -n churn-orange python=3.10
conda activate churn-orange

# Installer dépendances
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Télécharger données (si nécessaire)
python scripts/telecharger_donnees.py
```

### Lancer Exploration
```bash
# Lancer JupyterLab
jupyter lab

# Ouvrir : notebooks/exploration_complete.ipynb
```

---

## 🤖 Stack Technique

### Machine Learning
- **Scikit-learn** : Modèles de base, preprocessing
- **XGBoost** : Gradient boosting optimisé
- **LightGBM** : Rapidité et performance
- **CatBoost** : Gestion catégorielles natives

### Tracking & Optimisation
- **MLflow** : Suivi expériences
- **Optuna** : Hyperparameter tuning

### Explicabilité
- **SHAP** : Interprétabilité globale/locale
- **LIME** : Explications instance par instance

### Visualisation & Dashboard
- **Streamlit** : Dashboard interactif
- **Plotly** : Graphiques dynamiques
- **Seaborn/Matplotlib** : Visualisations statiques

### API & Déploiement
- **FastAPI** : API REST performante
- **Uvicorn** : Serveur ASGI
- **Docker** : Containerisation

---

## 📈 Méthodologie

1. **Exploration & Validation Données** ✅
   - 4 datasets validés
   - 13,526 clients analysés
   - Encodages harmonisés

2. **Feature Engineering** ⏳
   - Variables RFM (Recency, Frequency, Monetary)
   - Ratios comportementaux
   - Agrégations temporelles

3. **Modélisation** ⏳
   - Baseline models (Logistic Regression, Random Forest)
   - Modèles avancés (XGBoost, LightGBM, CatBoost)
   - Ensemble methods & Stacking

4. **Optimisation** ⏳
   - Hyperparameter tuning (Optuna)
   - Cross-validation stratifiée
   - Gestion déséquilibre classes (SMOTE)

5. **Déploiement** ⏳
   - API REST (FastAPI)
   - Dashboard interactif (Streamlit)
   - Documentation complète

---

## 📊 Résultats (À venir)

**Métriques Cibles** :
- F1-Score ≥ 0.75
- AUC-ROC ≥ 0.82
- Precision@20% ≥ 0.70
- Recall ≥ 0.80

**Impact Business Estimé** :
- Clients sauvés : 14,400/an
- Gain financier : 450M FCFA/an
- ROI campagnes : +300%

---

## 👤 Auteur

**[Ton Nom]**  
Master 2 Data Science - Modélisation Statistique  
ISSEA Yaoundé

📧 [djoknonelaurent@gmail.com]  
💼 [LinkedIn](linkedin.com/in/laurent-djoknoné-9a124325a)  
🐙 [GitHub](https://github.com/DjoknoneLaurent))

---

## 📄 Licence

MIT License - Voir [LICENSE](LICENSE) pour détails

---

## 🙏 Remerciements

- Orange Cameroun pour l'inspiration du projet
- ISSEA Yaoundé pour la formation
- Communauté Kaggle pour les datasets

---

**⭐ Star ce projet si tu le trouves utile !**

**🔗 Projet créé dans le cadre d'un stage Data Scientist chez Orange Cameroun**
