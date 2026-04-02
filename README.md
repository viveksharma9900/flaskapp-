# 🚀 Flask REST API — Dockerized with CI/CD

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=flat-square&logo=github-actions)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A production-ready **REST API** built with Flask, containerized using **Docker**, and deployed via an automated **GitHub Actions CI/CD pipeline**. Developed as part of a DevOps learning project demonstrating end-to-end application deployment workflow.

---

## 📌 Features

- ✅ RESTful API endpoints with proper HTTP methods (GET, POST, PUT, DELETE)
- ✅ Dockerized application for consistent environments across dev and prod
- ✅ Automated CI/CD pipeline using GitHub Actions
- ✅ Docker image auto-build and push on every commit to `main`
- ✅ Environment-based configuration support
- ✅ Lightweight and easy to extend

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10 |
| Framework | Flask |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
flaskapp-/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Multi-container orchestration
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions pipeline
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- Docker Desktop (or Docker Engine on Linux)
- Git

---

### ▶️ Option 1 — Run Locally (without Docker)

```bash
# 1. Clone the repository
git clone https://github.com/viveksharma9900/flaskapp-.git
cd flaskapp-

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

App will start at: `http://localhost:5000`

---

### 🐳 Option 2 — Run with Docker

```bash
# 1. Clone the repository
git clone https://github.com/viveksharma9900/flaskapp-.git
cd flaskapp-

# 2. Build the Docker image
docker build -t flaskapp .

# 3. Run the container
docker run -d -p 5000:5000 flaskapp
```

App will start at: `http://localhost:5000`

---

### 🐙 Option 3 — Run with Docker Compose

```bash
docker-compose up --build
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check — returns API status |
| GET | `/api/items` | Fetch all items |
| POST | `/api/items` | Create a new item |
| PUT | `/api/items/<id>` | Update an existing item |
| DELETE | `/api/items/<id>` | Delete an item |

### Sample Request

```bash
curl -X GET http://localhost:5000/api/items
```

### Sample Response

```json
{
  "status": "success",
  "data": [],
  "message": "Items fetched successfully"
}
```

---

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** for automated build and deployment.

### Pipeline Flow

```
Code Push to main
      ↓
GitHub Actions Triggered
      ↓
Run Tests
      ↓
Build Docker Image
      ↓
Push to Docker Hub (or GitHub Container Registry)
      ↓
Deploy
```

### Workflow file: `.github/workflows/ci-cd.yml`

The pipeline automatically:
1. Installs Python dependencies
2. Runs unit tests
3. Builds Docker image
4. Pushes image to registry on successful merge to `main`

---

## 🧪 Running Tests

```bash
# Run tests locally
python -m pytest tests/ -v
```

---

## 🌍 Environment Variables

Create a `.env` file in the root directory:

```env
FLASK_ENV=development
FLASK_DEBUG=1
PORT=5000
SECRET_KEY=your-secret-key-here
```

> ⚠️ Never commit `.env` to version control. It is already listed in `.gitignore`.

---

## 📸 Screenshots

> _Add screenshots of your API responses or Postman/cURL output here._

---

## 🚧 Future Improvements

- [ ] Add JWT-based authentication
- [ ] Connect to a PostgreSQL / MongoDB database
- [ ] Deploy to AWS EC2 or Render
- [ ] Add Swagger / OpenAPI documentation
- [ ] Implement rate limiting

---

## 👨‍💻 Author

**Vivek Sharma**
- 🎓 B.Tech CSE — Chaudhary Devi Lal University (CDLU), Sirsa
- 🔒 C-DAC Cybersecurity Internship
- 🤖 ML Projects: BERT Terrorism Detection | CNN Network Intrusion Detection
- 📌 NTSE Scholar

[![GitHub](https://img.shields.io/badge/GitHub-viveksharma9900-black?style=flat-square&logo=github)](https://github.com/viveksharma9900)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

> ⭐ If you found this useful, consider starring the repo!
