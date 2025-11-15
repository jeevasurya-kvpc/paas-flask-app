from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PaaS Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        .info-box {
            background: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }
        .status {
            color: #4ade80;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 PaaS Deployment Experiment</h1>
        <div class="info-box">
            <h2>Welcome to Flask on PaaS!</h2>
            <p><strong>Status:</strong> <span class="status">✓ Application Running Successfully</span></p>
            <p><strong>Framework:</strong> Flask (Python)</p>
            <p><strong>Platform:</strong> Platform as a Service (PaaS)</p>
            <p><strong>Experiment:</strong> Deploying Python Web Application</p>
        </div>
        <div class="info-box">
            <h3>About This App</h3>
            <p>This is a simple Flask web application deployed on a PaaS platform as part of a cloud computing experiment.</p>
            <p><strong>Features:</strong></p>
            <ul>
                <li>Lightweight Python web framework</li>
                <li>Easy deployment process</li>
                <li>Automatic scaling capabilities</li>
                <li>No server management required</li>
            </ul>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Application is running'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
