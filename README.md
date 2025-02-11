# **Flask** und **Jinja2** Templating Engine

Dieses Projekt ist eine einfache Website mit **Flask** und **Jinja2** als Templating Engine. Es nutzt **TailwindCSS** für das Styling und beinhaltet eine grundlegende Struktur für eine Unternehmens- oder Landingpage.

## 📂 Projektstruktur

```
/mein_projekt
│── static/
│   ├── css/
│   │   ├── styles.css  (Deine eigene Tailwind- oder CSS-Datei)
│   ├── js/
│   ├── images/
│   ├── videos/
│   ├── favicon.png   
│── templates/
│   ├── base.html      (Haupttemplate)
│   ├── head.html      (Meta-Tags, Tailwind, FontAwesome, Favicon)
│   ├── header.html    (Navigationsmenü)
│   ├── footer.html    (Footer mit Copyright etc.)
│   ├── index.html     (Startseite)
│   ├── about.html     (Über uns)
│   ├── services.html  (Leistungen)
│   └── contact.html   (Kontakt)
│── app.py             (Flask-Backend)
│── docs/              (Statische Version der Website für GitHub)
```

## Features

- ✅ Dynamische Projektkarten mit Jinja
- ✅ AOS Scroll-Animationen
- ✅ Responsive Design mit **Tailwind CSS**
- ✅ Statische Version für **GitHub Pages**
- ✅ Modernes Layout und benutzerfreundliche Navigation

## Installation

### Backend installieren:

1. Klone das Repository:
   ```bash
   git clone https://github.com/akocerke/Flask-Jinja-First-Template.git
   ```

2. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

3. Starte den Flask-Server:
   ```bash
   flask run
   ```

4. Besuche die Website unter [http://127.0.0.1:5000](http://127.0.0.1:5000)


## 🚀 Live Demo

Besuche die Live-Demo [hier](https://akocerke.github.io/Flask-Jinja-First-Template/).



## Fotos verwendet in der Website

- **Hero-Bereich**: Foto von [JOHN TOWNER](https://unsplash.com/de/@heytowner) auf [Unsplash](https://unsplash.com/de/fotos/leere-betonstrasse-die-von-hohen-baumen-mit-sonnenstrahlen-umgeben-ist-3Kv48NS4WUU)
- **Über uns**: Foto von [Elliott Engelmann](https://unsplash.com/de/@elliottengelmann) auf [Unsplash](https://unsplash.com/de/fotos/silhouette-des-berges-DjlKxYFJlTc)
- **Kontakt**: Foto von [JOHN TOWNER](https://unsplash.com/de/@heytowner) auf [Unsplash](https://unsplash.com/de/fotos/luftaufnahme-von-brown-mountains-JgOeRuGD_Y4)
- **Leistungen**: Foto von [Jonatan Pie](https://unsplash.com/de/@r3dmax) auf [Unsplash](https://unsplash.com/de/fotos/silhouette-eines-gelandewagens-h8nxGssjQXs)





