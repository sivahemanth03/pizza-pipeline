# 🍕 Pizza Pipeline — CI/CD Project

A production-grade CI/CD pipeline built with Docker, Kubernetes, and GitHub Actions.

## 🏗️ Architecture
- **Service A** — Node.js REST API (Pizza Orders)
- **Service B** — Python Flask API (Pizza Tracker)
- **Docker** — Both services containerized
- **Kubernetes** — Deployed on Minikube
- **GitHub Actions** — Automated CI/CD pipeline

## 🚀 Pipeline Flow
Code Push → GitHub Actions → Docker Build → Kubernetes Deploy

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Node.js | Service A backend |
| Python Flask | Service B backend |
| Docker | Containerization |
| Kubernetes | Orchestration |
| GitHub Actions | CI/CD automation |

## ▶️ Run Locally
# Start Minikube
minikube start --driver=docker

# Deploy services
kubectl apply -f k8s/service-a.yaml
kubectl apply -f k8s/service-b.yaml

# Access services
minikube service service-a-svc --url
minikube service service-b-svc --url

## 👨‍💻 Author
Built by Siva Hemanth — learning cloud engineering 
