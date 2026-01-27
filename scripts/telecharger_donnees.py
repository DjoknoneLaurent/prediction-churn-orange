"""
Script de téléchargement automatique des données
Projet: Prédiction Churn Orange Cameroun
"""

import os
import urllib.request
import zipfile
from pathlib import Path
from loguru import logger

# Configuration
DOSSIER_BRUT = Path("donnees/brutes")
DOSSIER_BRUT.mkdir(parents=True, exist_ok=True)

# URLs des datasets
DATASETS = {
    "telco_churn_ibm": {
        "url": "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv",
        "nom_fichier": "telco_customer_churn_ibm.csv",
        "description": "IBM Telco Customer Churn Dataset"
    },
    "orange_churn_kaggle": {
        "url": "https://raw.githubusercontent.com/srivatsan88/YouTubeLI/master/dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv",
        "nom_fichier": "orange_telco_churn.csv",
        "description": "Orange Telecom Churn Dataset"
    }
}

def telecharger_fichier(url: str, destination: Path) -> bool:
    """Télécharge un fichier depuis URL"""
    try:
        logger.info(f"📥 Téléchargement depuis: {url}")
        urllib.request.urlretrieve(url, destination)
        taille = destination.stat().st_size / 1024  # KB
        logger.success(f"✅ Téléchargé: {destination.name} ({taille:.1f} KB)")
        return True
    except Exception as e:
        logger.error(f"❌ Erreur téléchargement: {e}")
        return False

def verifier_fichier_existe(chemin: Path) -> bool:
    """Vérifie si fichier existe déjà"""
    if chemin.exists():
        taille = chemin.stat().st_size / 1024
        logger.info(f"ℹ️  Fichier existe déjà: {chemin.name} ({taille:.1f} KB)")
        return True
    return False

def main():
    """Fonction principale"""
    logger.info("="*70)
    logger.info("🚀 TÉLÉCHARGEMENT DES DONNÉES - CHURN PREDICTION")
    logger.info("="*70 + "\n")
    
    succes = 0
    echecs = 0
    deja_present = 0
    
    for nom, config in DATASETS.items():
        logger.info(f"\n📊 Dataset: {config['description']}")
        destination = DOSSIER_BRUT / config['nom_fichier']
        
        # Vérifier si existe déjà
        if verifier_fichier_existe(destination):
            reponse = input("   Télécharger à nouveau ? (o/N): ").lower()
            if reponse != 'o':
                deja_present += 1
                continue
        
        # Télécharger
        if telecharger_fichier(config['url'], destination):
            succes += 1
        else:
            echecs += 1
    
    # Résumé
    logger.info("\n" + "="*70)
    logger.info("📊 RÉSUMÉ TÉLÉCHARGEMENT")
    logger.info("="*70)
    logger.info(f"✅ Téléchargés avec succès : {succes}")
    logger.info(f"ℹ️  Déjà présents         : {deja_present}")
    logger.info(f"❌ Échecs                : {echecs}")
    logger.info(f"📁 Emplacement           : {DOSSIER_BRUT.absolute()}")
    
    # Lister fichiers
    logger.info("\n📋 FICHIERS DISPONIBLES:")
    for fichier in sorted(DOSSIER_BRUT.glob("*.csv")):
        taille = fichier.stat().st_size / 1024
        logger.info(f"   • {fichier.name} ({taille:.1f} KB)")
    
    logger.info("\n" + "="*70)
    logger.success("✨ TÉLÉCHARGEMENT TERMINÉ !")
    logger.info("Prochaine étape: jupyter lab (lancer notebook exploration)")
    logger.info("="*70 + "\n")

if __name__ == "__main__":
    main()
