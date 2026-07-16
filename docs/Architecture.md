# Project Architecture

## Overview

This project follows a Two-Tier Architecture.

```
Client
   │
   ▼
Flask Application
   │
   ▼
MySQL Database
```

## Components

### Flask
- Serves the web application.
- Handles HTTP requests.
- Connects to MySQL.

### MySQL
- Stores application data.
- Persists data using Docker volumes.

### Docker
- Packages Flask and MySQL into containers.
- Ensures portability.

### Jenkins
- Automates build and deployment.

### GitHub Actions
- Performs CI validation before deployment.

## Future Improvements

- Kubernetes Deployment
- NGINX Reverse Proxy
- Monitoring with Prometheus & Grafana
- AWS ECS/EKS Deployment