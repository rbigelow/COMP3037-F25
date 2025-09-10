# pip install flask
#pip freeze > requirements.txt
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    
    return render_template('services.html',services=" get coffee.")

@app.route('/news-api')
def news_api():
# Create a list of sample news items
    news_items = [
        {"title": "Breaking News 1", "description": "Sample news story 1", "date": "2024-01-01"},
        {"title": "Technology Update", "description": "New tech developments", "date": "2024-01-02"},
        {"title": "Science Discovery", "description": "Latest scientific findings", "date": "2024-01-03"},
        {"title": "Sports Results", "description": "Weekend match outcomes", "date": "2024-01-04"},
        {"title": "Business News", "description": "Market updates", "date": "2024-01-05"},
        {"title": "Entertainment", "description": "Celebrity news", "date": "2024-01-06"},
        {"title": "Health Update", "description": "Medical breakthroughs", "date": "2024-01-07"},
        {"title": "Education News", "description": "Academic achievements", "date": "2024-01-08"},
        {"title": "Environmental Report", "description": "Climate change updates", "date": "2024-01-09"},
        {"title": "Local News", "description": "Community events", "date": "2024-01-10"}
    ]

    # Format as RSS-like JSON feed
    return {"channel": {
        "title": "Sample News Feed",
        "description": "A sample RSS-like news feed",
        "items": news_items
    }}