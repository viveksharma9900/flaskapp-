from flask import Flask, request, jsonify
import boto3
import os
import pymysql

app = Flask(__name__)

# S3 client (IAM Role se chalega)
s3 = boto3.client('s3', region_name='ap-south-1')
BUCKET = os.environ.get('AWS_BUCKET_NAME')

# RDS connection
def get_db():
    return pymysql.connect(
        host='flask-db.cbwuuma4aliy.ap-south-1.rds.amazonaws.com',
        user='admin',
        password='Vivek1234!',
        database='flaskdb',
        cursorclass=pymysql.cursors.DictCursor
    )

# Database initialize karo
def init_db():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE DATABASE IF NOT EXISTS flaskdb
        ''')
        conn.select_db('flaskdb')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        print("DB initialized!")
    except Exception as e:
        print(f"DB Error: {e}")

@app.route('/')
def home():
    return 'Flask + S3 + RDS on AWS!'

@app.route('/health')
def health():
    return 'Server is running on AWS!'

# S3 endpoints
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400
    file = request.files['file']
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

# RDS endpoints
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (name, email) VALUES (%s, %s)',
            (data['name'], data['email'])
        )
        conn.commit()
        conn.close()
        return jsonify({'message': 'User added!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        conn.close()
        return jsonify({'users': users}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

