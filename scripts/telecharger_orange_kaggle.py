"""
Téléchargement Dataset Orange depuis Kaggle
Utilise kagglehub (plus simple que API Kaggle)
"""

from pathlib import Path
from loguru import logger
import shutil

try:
    import kagglehub
except ImportError:
    logger.error("❌ kagglehub non installé")
    logger.info("📦 Installation: pip install kagglehub")
    exit(1)

# Configuration
DOSSIER_BRUT = Path("donnees/brutes")
DOSSIER_BRUT.mkdir(parents=True, exist_ok=True)

def telecharger_orange_kaggle():
    """Télécharge dataset Orange depuis Kaggle"""
    
    logger.info("="*70)
    logger.info("📥 TÉLÉCHARGEMENT DATASET ORANGE (KAGGLE)")
    logger.info("="*70)
    
    try:
        # Télécharger
        logger.info("\n🔄 Téléchargement en cours...")
        path = kagglehub.dataset_download("mnassrib/telecom-churn-datasets")
        logger.success(f"✅ Téléchargé dans: {path}")
        
        # Lister fichiers téléchargés
        source_path = Path(path)
        fichiers = list(source_path.glob("*.csv"))
        
        logger.info(f"\n📋 {len(fichiers)} fichiers trouvés:")
        for f in fichiers:
            taille = f.stat().st_size / 1024
            logger.info(f"   • {f.name} ({taille:.1f} KB)")
        
        # Copier dans notre structure projet
        logger.info(f"\n📁 Copie vers {DOSSIER_BRUT}...")
        fichiers_copies = []
        
        for fichier in fichiers:
            destination = DOSSIER_BRUT / fichier.name
            shutil.copy2(fichier, destination)
            logger.success(f"✅ Copié: {fichier.name}")
            fichiers_copies.append(destination)
        
        # Résumé
        logger.info("\n" + "="*70)
        logger.info("📊 RÉSUMÉ")
        logger.info("="*70)
        logger.info(f"✅ Fichiers téléchargés  : {len(fichiers_copies)}")
        logger.info(f"📁 Emplacement           : {DOSSIER_BRUT.absolute()}")
        
        logger.info("\n📋 FICHIERS DISPONIBLES:")
        for f in sorted(DOSSIER_BRUT.glob("*.csv")):
            taille = f.stat().st_size / 1024
            logger.info(f"   • {f.name} ({taille:.1f} KB)")
        
        logger.info("\n" + "="*70)
        logger.success("✨ TÉLÉCHARGEMENT TERMINÉ !")
        logger.info("="*70)
        
        return fichiers_copies
        
    except Exception as e:
        logger.error(f"❌ Erreur: {e}")
        logger.info("\n💡 SOLUTIONS:")
        logger.info("   1. Vérifier connexion internet")
        logger.info("   2. Accepter conditions Kaggle sur le site")
        logger.info("   3. pip install --upgrade kagglehub")
        return []

if __name__ == "__main__":
    telecharger_orange_kaggle()
