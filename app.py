from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    html_content = """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f0f8ff; }
            h1 { color: #2e8b57; }
            .box { border: 2px solid #2e8b57; padding: 20px; display: inline-block; border-radius: 10px; background-color: white; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 GitOps CI/CD Pipeline Success! 🚀</h1>
            <h2> signsoidingiodnr </h2>
            <h2>Version 2.0 is Live!</h2>
            <p>If you are seeing this, your GitHub Actions built the new Docker image,<br>
            updated the deployment file, and Argo CD automatically synced it to AWS.</p>
        </div>
    </body>
    </html>
    """
    return html_content

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
