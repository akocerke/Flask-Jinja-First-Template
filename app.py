# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Startseite")

@app.route('/about')
def about():  # <-- Hier den Funktionsnamen ändern!
    return render_template('about.html', title="Über Uns")

@app.route('/services')
def services():
    return render_template('services.html', title="Leistungen")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Hier könntest du die Daten per E-Mail versenden oder in einer Datei speichern
        print(f"Nachricht von {name} ({email}): {message}")
        return redirect(url_for('home', success=True))
    return render_template('contact.html', title="Kontakt")

if __name__ == '__main__':
    app.run(debug=True)
