# 🚀 Two-Tier Flask CI/CD Pipeline

> A production-style DevOps project demonstrating a Flask + MySQL application deployed with Docker and automated using Jenkins on AWS EC2.

---

## 📌 Project Overview

This project showcases a complete CI/CD workflow for a two-tier Flask application.

### Objectives
- Build a Flask application
- Connect Flask with MySQL
- Containerize using Docker
- Automate deployment with Jenkins
- Deploy on AWS EC2
- Manage source code with Git & GitHub
- Validate code using GitHub Actions

---

## 🏗 Architecture

Client → Flask Application → MySQL Database

Jenkins builds Docker images and deploys the application using Docker Compose on AWS EC2.

---

## ✨ Features

- Flask Web Application
- MySQL Database Integration
- Dockerized Application
- Docker Compose
- Jenkins Pipeline
- GitHub Actions CI
- Health Check Endpoint
- Version Endpoint
- Metrics Endpoint
- REST API Endpoint

---

## 🛠 Tech Stack

- Python (Flask)
- MySQL
- Docker
- Docker Compose
- Jenkins
- GitHub
- GitHub Actions
- AWS EC2
- Linux (Ubuntu)

---

## 📂 Project Structure

```text
two-tier-flask-cicd/
├── .github/workflows/
├── app/
├── database/
├── docker/
├── docs/
├── diagrams/
├── jenkins/
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home Page |
| `/health` | Health Check |
| `/api/messages` | Returns Messages |
| `/version` | Application Version |
| `/metrics` | Application Metrics |

---

## ⚙️ Local Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
python app/app.py
```

---

## 🐳 Docker

```bash
docker build -t two-tier-flask-app -f docker/Dockerfile .
docker compose -f docker/docker-compose.yml up -d --build
```

Verify:

```bash
docker ps
docker images
curl http://localhost:5000/health
```

---

## ☁️ AWS EC2 Deployment

1. Launch Ubuntu EC2
2. Install Docker
3. Install Java 17
4. Install Jenkins
5. Add Jenkins to Docker group
6. Clone Repository
7. Configure Jenkins Pipeline
8. Run Build

---

## 🔄 Jenkins Pipeline

- Checkout Source
- Build Docker Image
- Deploy Containers
- Health Check
- Deployment Successful

---

## 🤖 GitHub Actions

- Checkout Repository
- Install Python Dependencies
- Validate Application
- Complete CI

---

## 📸 Screenshots

Add your screenshots here:

- Project Structure
- GitHub Repository
- Jenkins Success Build
- Docker Images
- Docker Containers
- Flask Home Page
- `/health`
- `/api/messages`
- `/version`
- `/metrics`

---

## 📖 Step-by-Step Project Build

### Step 1
Create the project folder.

> Screenshot

### Step 2
Create the Flask application.

> Screenshot

### Step 3
Create Dockerfile.

> Screenshot

### Step 4
Create docker-compose.yml.

> Screenshot

### Step 5
Create Jenkinsfile.

> Screenshot

### Step 6
Push to GitHub.

> Screenshot

### Step 7
Create Jenkins Pipeline Job.

> Screenshot

### Step 8
Deploy on AWS EC2.

> Screenshot

### Step 9
Verify deployment.

```bash
docker ps
curl http://localhost:5000/health
```

> Screenshot

---

## 🐞 Challenges Faced

During development I encountered and resolved several real-world DevOps issues:

- Jenkins GPG key verification failure (Ubuntu 24.04)
- Java installation and repository configuration
- Jenkinsfile path mismatch
- GitHub SSH vs HTTPS authentication
- Docker socket permission denied
- Jenkins user missing Docker group
- EC2 SSH private key permission issues
- Branch synchronization issues
- Docker Compose deployment troubleshooting

---

## ✅ Solutions Implemented

- Configured Jenkins repository correctly
- Installed Java 17
- Added Jenkins user to Docker group
- Restarted Docker and Jenkins services
- Corrected Jenkins Pipeline configuration
- Switched repository access where appropriate
- Verified deployment using health endpoint

---

## 📚 Lessons Learned

- Jenkins Pipeline fundamentals
- Docker container lifecycle
- Docker Compose orchestration
- AWS EC2 administration
- Linux troubleshooting
- CI/CD automation
- Git branching workflow

---

## 🚀 Future Improvements

- Kubernetes Deployment
- Terraform Infrastructure
- Prometheus Monitoring
- Grafana Dashboards
- NGINX Reverse Proxy
- SSL with Let's Encrypt

---

## 👨‍💻 Author

**Revanth B L**

GitHub: https://github.com/revanth-bl

LinkedIn: *([Add your LinkedIn URL](https://www.linkedin.com/in/revanth-b-l-05294a253/))*

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
