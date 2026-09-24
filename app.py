from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Pobierz informacje o użytkowniku z nagłówków Azure Easy Auth
    user_name = request.headers.get('X-MS-CLIENT-PRINCIPAL-NAME', 'Gość')
    is_authenticated = request.headers.get('X-MS-CLIENT-PRINCIPAL-ID') is not None
    return render_template('index.html', user_name=user_name, is_authenticated=is_authenticated)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)