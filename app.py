from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

# S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name='ap-south-1'
)

BUCKET = os.environ.get('AWS_BUCKET_NAME')

@app.route('/')
def home():
    return 'Hello from AWS EC2 with S3!'

@app.route('/health')
def health():
    return 'Server is running on AWS!'

@app.route('/predict')
def predict():
    return {'model': 'BERT', 'status': 'running', 'accuracy': '94%'}

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    try:
        s3.upload_fileobj(file, BUCKET, file.filename)
        url = f"https://{BUCKET}.s3.ap-south-1.amazonaws.com/{file.filename}"
        return jsonify({'message': 'Uploaded!', 'url': url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/files')
def files():
    try:
        resp = s3.list_objects_v2(Bucket=BUCKET)
        files = [o['Key'] for o in resp.get('Contents', [])]
        return jsonify({'files': files, 'count': len(files)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
