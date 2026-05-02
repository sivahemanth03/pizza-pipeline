# Pizza Pipeline CI/CD Project

A production-grade CI/CD pipeline built from scratch.

## Tech Stack
- Node.js microservice (Service A)
- Python Flask microservice (Service B)
- Docker for containerization
- Kubernetes for orchestration
- GitHub Actions for CI/CD automation

## Pipeline Flow
Code Push to GitHub triggers GitHub Actions which builds Docker images and deploys to Kubernetes automatically.

## How to Run
minikube start --driver=docker
kubectl apply -f k8s/service-a.yaml
kubectl apply -f k8s/service-b.yaml
minikube service service-a-svc --url
