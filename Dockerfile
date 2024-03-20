# Utilisez une image de Python comme base
FROM python:alpine

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers requis dans le conteneur
COPY seeder.py .
COPY grain.py .

# Installez les dépendances nécessaires
RUN pip install pymongo

# Exécutez le script seeder.py lors du démarrage du conteneur
CMD ["python", "seeder.py"]
