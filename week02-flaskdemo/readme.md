# Week 02 — Flask Demo (COMP3037-F25)

A minimal Flask application used to demonstrate core web concepts in Week 2:
- HTTP routing and request handling
- Rendering templates and serving static assets
- Returning JSON responses (simple API)
- Running locally with auto-reload/debug

## Requirements
- Python 3.10+ recommended
- pip (or pipx)
- Optional: virtual environment (venv)

## Setup
Windows (PowerShell):
1) python -m venv .venv
2) .\.venv\Scripts\Activate.ps1
3) pip install -r requirements.txt  (or: pip install flask)

macOS/Linux:
1) python3 -m venv .venv
2) source .venv/bin/activate
3) pip install -r requirements.txt  (or: pip install flask)

## Run
- If your Flask app object lives in a module named app (common):
    - flask --app app run --debug
- If it lives elsewhere, replace app with the module path:
    - flask --app src.main run --debug
- List routes:
    - flask --app app routes

Tip: If the CLI cannot find your app, open the code and locate where Flask(__name__) is created; use that module path after --app.

## Typical layout (yours may vary)
```
week02-flaskdemo/
├─ app.py                 # creates: app = Flask(__name__)
├─ templates/             # Jinja2 HTML templates
│  └─ index.html
├─ static/                # CSS/JS/images
├─ requirements.txt
└─ readme.md
```

## Common tasks
- Add a route:
    ```
    @app.get("/")
    def index():
            return "Hello, Flask!"
    ```
- Render a template:
    ```
    from flask import render_template

    @app.get("/hello/<name>")
    def hello(name):
            return render_template("hello.html", name=name)
    ```
- Return JSON:
    ```
    from flask import jsonify

    @app.get("/api/ping")
    def ping():
            return jsonify(status="ok")
    ```

## Notes
- Use --debug during development for auto-reload and error pages.
- See the source files for the exact routes implemented in this demo.
- Deactivate the venv with: deactivate