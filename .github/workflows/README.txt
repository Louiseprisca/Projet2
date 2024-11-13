Workfow Action "Premier workflows"

Ce workflow GitHub Actions, nommé Code_Correction, est configuré pour s'exécuter automatiquement chaque fois qu'il y a un push sur la branche dev du projet. Voici un résumé de ce que chaque étape fait :

Initialisation du job :

Le job lint est exécuté sur un environnement ubuntu-latest.
Étapes du workflow :

Checkout code : Télécharge le code du dépôt GitHub pour l'analyse, en utilisant l'action actions/checkout@v2.

Set up Python : Configure Python 3.12 pour l'environnement en utilisant actions/setup-python@v2.

Install dependencies : Installe flake8, un outil de linting pour Python, qui analyse le code pour repérer les erreurs de syntaxe et les incohérences de style. D'autres outils peuvent être ajoutés ici selon les besoins, comme ESLint pour JavaScript.

Run Super-Linter : Utilise github/super-linter@v2, qui exécute une analyse statique sur le code. Super-Linter peut détecter les erreurs et les incohérences dans plusieurs langages.

Run code analysis : Exécute une analyse de code spécifique à Python avec flake8 sur tous les fichiers (flake8 .). D'autres commandes pourraient être ajoutées pour analyser différents langages.

Run AI correction : Appelle un script d’IA (ou une API IA) pour corriger le code, ici en lançant corrector_script.py. Cette étape utilise une variable d'environnement GITHUB_TOKEN (pour les autorisations GitHub) et la variable DEFAUT_BRANCH définie comme dev.

Ce workflow automatise les vérifications de qualité de code, exécute des analyses statiques, et applique éventuellement des corrections via un script IA, contribuant ainsi à maintenir un code propre et fonctionnel.