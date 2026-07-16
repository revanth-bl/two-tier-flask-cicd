# CI/CD Pipeline

## Jenkins Pipeline

```
Checkout Source
      │
      ▼
Build Docker Image
      │
      ▼
Deploy Containers
      │
      ▼
Verify Deployment
      │
      ▼
Success
```

---

## GitHub Actions

```
Push Code
     │
     ▼
Checkout Repository
     │
     ▼
Install Dependencies
     │
     ▼
Validate Flask Application
```

---

## Future Pipeline

```
GitHub

↓

GitHub Actions

↓

Jenkins

↓

Docker

↓

AWS EC2

↓

Kubernetes
```