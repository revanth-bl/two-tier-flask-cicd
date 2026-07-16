# Deployment Guide

## Local Deployment

```bash
docker compose up -d --build
```

Application:

```
http://localhost:5000
```

---

## AWS Deployment

1. Launch EC2
2. Install Docker
3. Install Jenkins
4. Clone Repository
5. Build Docker Image
6. Deploy with Docker Compose

---

## Verify Deployment

```bash
docker ps
```

```bash
curl http://localhost:5000
```

Expected:

```
Application is running successfully.
```