import os
import requests
import json
import subprocess
import hmac
import hashlib
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

# Configuration
API_KEY = os.getenv("API_KEY")  # Doit être défini dans l'environnement
GITHUB_SECRET = os.getenv("GITHUB_SECRET")  # Assurez-vous que cette variable est définie
REPOSITORY = "https://github.com/Louiseprisca/Projet2.git"
BRANCH = "dev"

# Fonction pour vérifier la signature du webhook GitHub
def verify_signature(payload, signature):
    secret = os.getenv("GITHUB_SECRET")
    hash_message = hmac.new(secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha1).hexdigest()
    return hash_message == signature

# Fonction pour extraire les fichiers Python modifiés de la charge utile GitHub
def get_changed_python_files(payload):
    commits = payload.get('commits', [])
    changed_files = []
    for commit in commits:
        added_files = commit.get('added', [])
        modified_files = commit.get('modified', [])
        for file in added_files + modified_files:
            if file.endswith('.py'):
                changed_files.append(file)
    return changed_files

# Fonction pour envoyer une requête à l'API OpenAI et obtenir les suggestions
def get_suggestions(code):
    response = requests.post(
        'https://api.openai.com/v1/models/gemini/completions',
        headers={
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
        },
        json={
            'prompt': f"Veuillez examiner le code Python suivant et suggérer des améliorations:\n\n{code}\n\nSuggestions:",
            'max_tokens': 2000,
            'temperature': 0.8,
        }
    )
    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        print(f"Erreur lors de l'appel à l'API : {response.status_code} - {response.text}")
        return None

# Fonction pour formater le code avant de l'envoyer à l'API
def format_code(file_path):
    try:
        subprocess.run(["black", file_path], check=True)
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Erreur lors du formatage du code : {e}")
        return None

# Fonction principale
def main(payload):
    signature = os.environ.get('SIGNATURE')  # Récupérer la signature depuis les variables d'environnement
    if verify_signature(payload, signature):
        changed_files = get_changed_python_files(payload)
        for file in changed_files:
            file_path = os.path.join(REPOSITORY, BRANCH, file)
            code = format_code(file_path)
            if code:
                suggestions = get_suggestions(code)
                if suggestions:
                    print(f"Suggestions pour {file}:\n{suggestions}")
                    # Envoyer les suggestions à GitHub ou par email
                    send_to_github(REPOSITORY, os.getenv("GITHUB_TOKEN"), f"Suggestions pour {file}", suggestions)
                    send_email('boblagno6@gmail.com', 'Suggestions de code', suggestions)
    else:
        print("Signature de webhook invalide")

def send_to_github(repo, token, title, body):
    """Envoie une issue à un dépôt GitHub."""
    url = f"https://github.com/Louiseprisca/Projet2.git/{repo}/issues"
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
    message['From'] = os.getenv('EMAIL_USER')
    message['To'] = recipient
    message['Subject'] = subject
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASSWORD'))  # Récupérer le mot de passe depuis les variables d'environnement
            smtp.sendmail(os.getenv('EMAIL_USER'), recipient, message.as_string())
            print("Email envoyé avec succès")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

# Exécution principale

if __name__ == "__main__":
    # Récupérer la charge utile du webhook (adapter selon votre environnement)
    payload = json.loads(os.environ['PAYLOAD'])
    main(payload)