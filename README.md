# Swapi People Sorter

## Description
`Swapi People Sorter` is a Python microservice that consumes data from the Star Wars API, sorts it alphabetically by name, and exposes a RESTful endpoint for easy access.

## Technologies Used
- **Python 3.12**: Main programming language for the microservice.
- **Flask**: Lightweight framework for the web server.
- **Docker**: Used for building and containerizing the application.
- **Kubernetes (GKE)**: Google Kubernetes Engine cluster for deployment and orchestration.
- **Helm**: Package manager for Kubernetes.
- **GitHub Actions**: CI/CD pipeline automation.

## Project Architecture
The project follows the Model-View-Controller (MVC) design pattern for clear separation between business logic, presentation, and request handling.

## Deployment in GKE
The microservice is deployed in a Google Kubernetes Engine (GKE) cluster. This cluster is accessed via `gcloud` and deployed using the CI/CD GitHub Actions workflow.

### Deployment Details
- **GKE Cluster**: `cluster-1` in the project `custom-manifest-435411-u7`.
- **Authentication**: The GitHub Actions pipeline uses a service account JSON key (`GCP_SA_KEY`) for authentication.
- **Helm**: Used to install and manage the deployment.

### Deployment Command
The deployment is executed with the following command in the GitHub Actions pipeline:
```bash
helm install swapi-people-sorter .```
