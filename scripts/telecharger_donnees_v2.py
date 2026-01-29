"""
Script téléchargement données - Version 2
Avec dataset Orange authentique
"""

import os
import urllib.request
from pathlib import Path
from loguru import logger
import kaggle  # Note: nécessite configuration Kaggle API

DOSSIER_BRUT = Path("donnees/brutes")
DOSSIER_BRUT.mkdir(parents=True, exist_ok=True)

DATASETS = {
    "telco_churn_ibm": {
        "url": "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv",
        "nom_fichier": "telco_customer_churn_ibm.csv",
        "description": "IBM Telco Customer Churn Dataset",
        "type": "direct"
    },
    "orange_churn_kaggle": {
        "dataset_id": "mnassrib/telecom-churn-datasets",
        "nom_fichier": "churn-bigml-80.csv",
        "description": "Orange Telecom's Churn Dataset (Kaggle)",
        "type": "kaggle"
    }
}

def telecharger_direct(url: str, destination: Path) -> bool:
    """Télécharge fichier depuis URL"""
    try:
        logger.info(f"📥 Téléchargement: {url}")
        urllib.request.urlretrieve(url, destination)
        taille = destination.stat().st_size / 1024
        logger.success(f"✅ Téléchargé: {destination.name} ({taille:.1f} KB)")
        return True
    except Exception as e:
        logger.error(f"❌ Erreur: {e}")
        return False

def telecharger_kaggle(dataset_id: str, destination_dir: Path) -> bool:
    """Télécharge dataset Kaggle"""
    try:
        logger.info(f"📥 Téléchargement Kaggle: {dataset_id}")
        # Note: nécessite kaggle.json configuré
        os.system(f"kaggle datasets download -d {dataset_id} -p {destination_dir} --unzip")
        logger.success(f"✅ Dataset Kaggle téléchargé")
        return True
    except Exception as e:
        logger.error(f"❌ Erreur Kaggle: {e}")
        logger.info("💡 Alternative: télécharger manuellement depuis kaggle.com")
        return False

def main():
    logger.info("="*70)
    logger.info("🚀 TÉLÉCHARGEMENT DATASETS - VERSION 2")
    logger.info("="*70 + "\n")
    
    for nom, config in DATASETS.items():
        logger.info(f"\n📊 {config['description']}")
        
        if config['type'] == 'direct':
            destination = DOSSIER_BRUT / config['nom_fichier']
            telecharger_direct(config['url'], destination)
        
        elif config['type'] == 'kaggle':
            # Téléchargement Kaggle
            logger.warning("⚠️  Dataset Kaggle nécessite API Key")
            logger.info("📝 Instructions:")
            logger.info("   1. Aller sur kaggle.com/settings")
            logger.info("   2. Créer nouvelle API Token (télécharge kaggle.json)")
            logger.info("   3. Placer kaggle.json dans ~/.kaggle/")
            logger.info(f"   4. Ou télécharger manuellement: kaggle.com/datasets/{config['dataset_id']}")
            
            reponse = input("\n   Tentative téléchargement automatique ? (o/N): ")
            if reponse.lower() == 'o':
                telecharger_kaggle(config['dataset_id'], DOSSIER_BRUT)

if __name__ == "__main__":
    main()
