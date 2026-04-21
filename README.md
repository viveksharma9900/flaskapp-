# Flask REST API — AWS Cloud Deployment

A production-grade REST API built with Flask, deployed on AWS EC2 with S3 file storage, RDS MySQL database, IAM Role security, and Gunicorn production server.

## 🏗️ Architecture # Flask REST API — AWS Cloud Deployment
## 🛠️ Tech Stack

- **Backend:** Python, Flask, Gunicorn
- **Database:** AWS RDS MySQL
- **File Storage:** AWS S3
- **Security:** AWS IAM Role (keyless authentication)
- **Server:** AWS EC2 (Ubuntu, t3.micro)
- **CI/CD:** GitHub Actions
- **Container:** Docker

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home |
| GET | `/health` | Health check |
| POST | `/upload` | Upload file to S3 |
| GET | `/files` | List all S3 files |
| POST | `/users` | Add user to RDS |
| GET | `/users` | Get all users |

## 🚀 How to Run

### Prerequisites
- AWS Account
- EC2 instance (Ubuntu)
- RDS MySQL instance
- S3 Bucket
- IAM Role with S3 access

### Setup on EC2

```bash
# Install dependencies
pip install flask boto3 pymysql gunicorn

# Set environment variable
export AWS_BUCKET_NAME=your-bucket-name

# Run with Gunicorn
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

## 🧪 Test APIs

```bash
# Upload file
curl -X POST http://YOUR_EC2_IP:5000/upload -F "file=@test.txt"

# List files
curl http://YOUR_EC2_IP:5000/files

# Add user
curl -X POST http://YOUR_EC2_IP:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Your Name","email":"your@email.com"}'

# Get users
curl http://YOUR_EC2_IP:5000/users
```

## 🔐 Security

- IAM Role used instead of access keys
- Security groups configured for EC2
- RDS in private subnet
- No credentials in codebase

## 👤 Author

**Vivek Sharma**  
B.Tech CSE | CDLU Sirsa  
GitHub: [viveksharma9900](https://github.com/viveksharma9900)

