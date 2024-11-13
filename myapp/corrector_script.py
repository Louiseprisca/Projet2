import os
import sys
import requests
import json
import subprocess
import hmac
import hashlib
import requests
import smtplib
from email.mime.text import MIMEText


# Configuration
API_KEY = os.getenv("AIzaSyDP0InRAJ6nxdJbgYzWcYzlsKTFvo-guOU")
GITHUB_SECRET = os.getenv("GITHUB_SECRET")
REPOSITORY = "https://github.com/Louiseprisca/Projet2.git"
BRANCH = "dev"

# Fonction pour vérifier la signature du webhook GitHub
def verify_signature(payload, signature):
    """Vérifie la signature d'un webhook GitHub.

    Args:
        payload (str): La charge utile de la requête.
        signature (str): La signature HTTP envoyée par GitHub.

    Returns:
        bool: True si la signature est valide, False sinon.
    """

    # Récupérer le secret GitHub à partir de la variable d'environnement
    secret = os.getenv("GITHUB_SECRET")

    # Convertir la charge utile en bytes et calculer le hash HMAC-SHA1
    hash_message = hmac.new(secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha1).hexdigest()

    # Comparer le hash calculé avec la signature reçue
    return hash_message == signature

# Fonction pour extraire les fichiers Python modifiés de la charge utile GitHub
def get_changed_python_files(payload):
    commits = payload.get('commits', [])
    changed_files = []
    for commit in commits:
        for file in commit['added'] + commit['modified']:
            if file.endswith('.py'):
                changed_files.append(file)
    return changed_files

# Fonction pour envoyer une requête à l'API OpenAI et obtenir les suggestions
def get_suggestions(code):
    response = requests.post(
        'https://api.openai.com/v1/models/gemini:1.5-t/completions',
        headers={
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
        },
        json={
            'prompt':   
            f"Veuillez examiner le code Python suivant et suggérer des améliorations:\n\n{code}\n\nSuggestions:",
            'max_tokens': 2000,  
            'temperature': 0.8, 
        }
    )
    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        print(f"Erreur lors de l'appel à l'API GEMINI: {response.status_code}")
        return None

# Fonction pour formater le code avant de l'envoyer à l'API
def format_code(file_path):
    # Utilisez un formateur de code comme Black pour assurer la cohérence
    subprocess.run(["black", file_path])
    with open(file_path, 'r') as f:
        return f.read()

# Fonction principale
def main(payload):
    if verify_signature(payload, request.headers.get('X-Hub-Signature')):
        changed_files = get_changed_python_files(payload)
        for file in changed_files:
            file_path = os.path.join(REPOSITORY, BRANCH, file)
            code = format_code(file_path)
            suggestions = get_suggestions(code)
            if suggestions:
                print(f"Suggestions pour {file}:\n{suggestions}")
                # Envoyer les suggestions vers une plateforme de collaboration (e.g., GitHub Issues)
    else:
        print("Signature de webhook invalide")

def send_to_github(repo, token, title, body):
    """Envoie une issue à un dépôt GitHub."""
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    data = {"title": title, "body": body}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Issue créée avec succès")
    else:
        print(f"Erreur lors de la création de l'issue : {response.text}")

def send_email(recipient, subject, body):
    """Envoie un email."""
    message = MIMEText(body)
    message['From'] = 'your_email@example.com'  # Remplacer par votre adresse
    message['To'] = recipient
    message['Subject'] = subject
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_password')  # Remplacer par vos identifiants
        smtp.sendmail('your_email@example.com', recipient, message.as_string())
        print("Email envoyé avec succès")


# Exécution principale (à adapter à votre environnement)
if __name__ == "__main__":
    # Récupérer la charge utile du webhook (adapter selon votre environnement)
    payload = json.loads(os.environ['PAYLOAD'])
    main(payload)