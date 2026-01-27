# Makefile - Prédiction Churn Orange

.PHONY: aide installer tester nettoyer

aide:
	@echo "📋 Commandes:"
	@echo "  make installer - Installe dépendances"
	@echo "  make tester    - Lance tests"
	@echo "  make nettoyer  - Nettoie fichiers temp"

installer:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

tester:
	pytest tests/ -v --cov=src

nettoyer:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache
