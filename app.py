from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
        <head>
            <title>DevOps Stage 0</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 100px;
                    background-color: #f8f9fa;
                }}
                h1 {{
                    color: #007BFF;
                }}
                p {{
                    font-size: 18px;
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <h1>Welcome to DevOps Stage 0 - Emmanuel Justine / @kiev</h1>
            <p>Successfully deployed on <strong>Localhost (Ngrok Tunnel)</strong></p>
            <p>Deployed: {date.today().strftime('%B %d, %Y')}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)