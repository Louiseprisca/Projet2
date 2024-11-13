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



Workflow Action "email-on-push"

Le workflow email-on-push a pour rôle d’envoyer une notification par email chaque fois qu'un utilisateur pousse (push) des changements sur la branche dev. Voici les étapes en détail :

Déclenchement :

Ce workflow est déclenché par un événement push sur la branche spécifiée dans le fichier (ici dev).
Checkout du code :

Le workflow utilise actions/checkout@v2 pour cloner le code du dépôt. Bien que l’envoi d’email ne nécessite pas forcément le code, cette étape est souvent incluse pour s'assurer que le contexte complet du dépôt est chargé si nécessaire.
Envoi de l'email :

Le workflow envoie un email en utilisant l’API de SendGrid (ou un autre service d’email configuré).
Dans l’exemple fourni :
Expéditeur (SENDER_EMAIL) : Une adresse email de l'expéditeur (comme "no-reply@example.com").
Destinataire (RECIPIENT_EMAIL) : L'email de l'utilisateur qui doit recevoir la notification.
Sujet de l'email : Inclut le nom de l'auteur du commit.
Contenu de l'email : Un message personnalisable qui informe du nouveau push et peut inclure des détails comme le message de commit.
Vérification d’erreur :

Si l’envoi de l’email échoue, une étape de vérification peut afficher un message d’erreur dans le log pour signaler l'échec.
Exemple de cas d'utilisation :
Ce workflow est utile pour :

Notifier les membres de l’équipe de nouvelles mises à jour sur le dépôt.
Automatiser la gestion des notifications de commits importants.
Suivi des contributions dans des projets collaboratifs sans passer par les notifications GitHub classiques.
Ce workflow permet donc de s'assurer qu'une notification par email est envoyée chaque fois qu'il y a un push sur la branche cible.