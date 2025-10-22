from flask import Flask, render_template
from datetime import date
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
                           name="Emmanuel Lemuel",
                           handle="@kiev",
                           platform="Railway",
                           deployed_date=date.today().strftime('%B %d, %Y'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)