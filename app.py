from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask API!"

@app.route('/health')
def health():
    return "Server is running!"

@app.route('/predict')
def predict():
    return {
        "model": "BERT Text Classifier",
        "status": "running",
        "accuracy": "94%",
        "description": "Terrorism text detection model"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)