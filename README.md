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
helm install swapi-people-sorter .

```

## Horizontal Pod Autoscaler (HPA)
The deployment is configured with a **Horizontal Pod Autoscaler (HPA)** to ensure automatic scalability of the application. The HPA monitors CPU usage and adjusts the number of `Deployment` replicas between a defined minimum and maximum as specified in the `hpa.yaml` file.

### HPA Configuration
```yaml
minReplicas: 2
maxReplicas: 10
targetCPUUtilizationPercentage: 50

```

### Load balancing
In order to expose the application to the Internet, a nginx controller Helm chart has been deployed to the GKE cluster:
https://github.com/nginxinc/kubernetes-ingress

## CI/CD Pipeline
The project uses a **GitHub Actions** pipeline to automate building, pushing the Docker image to Google Artifact Registry, and deploying to GKE.

### Key Steps in the Pipeline
1. **Checkout code**.
2. **Authenticate with Google Cloud**.
3. **Build and push the Docker image**.
4. **Get GKE cluster credentials**.
5. **Deploy using Helm**.

### Manual Execution of the Pipeline
The pipeline is configured with `workflow_dispatch` to allow manual runs from GitHub's interface without needing to push to `main`.

## Local Installation
To run the microservice locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/swapi-people-sorter.git
   cd swapi-people-sorter
   
   ```

2. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   
   ```

3. Run the application:
   ```bash
   python app/app.py
   
   ```

## Accessing the Application via Ingress
This application is PUBLIC. To access the application through the configured Ingress at `http://swapi-people-sorter.local`, you need to update your local `/etc/hosts` file to map the domain to the external IP of your Ingress.

### Updating `/etc/hosts`
1. Open the `/etc/hosts` file with superuser privileges:
   ```bash
   sudo bash -c "echo 34.136.32.3 swapi-people-sorter.local >> /etc/hosts"
   
   ```
2. Navigate to http://swapi-people-sorter.local and you will get the JSON with the desired content
