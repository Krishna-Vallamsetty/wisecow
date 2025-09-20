Wisecow Application: Containerization and Kubernetes Deployment
This project demonstrates the end-to-end process of containerizing a Go web application, setting up an automated CI/CD pipeline with GitHub Actions, and deploying it to a local Kubernetes (Minikube) cluster. This project was completed as part of a technical assessment.

🚀 Tech Stack
Application: Go

Containerization: Docker

Container Orchestration: Kubernetes (Minikube)

CI/CD Automation: GitHub Actions

📁 Repository Structure
.
├── .github/workflows/  # Contains the CI/CD pipeline configuration
│   └── ci-cd-pipeline.yaml
├── k8s/                # Contains Kubernetes manifest files
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile          # A multi-stage Dockerfile for a small, secure image
├── go.mod              # Go module file for dependency management
└── main.go             # The Go application source code

⚙️ How to Run This Project
Prerequisites
Docker Desktop

Minikube

kubectl

Steps
Clone the repository:

git clone [https://github.com/Krishna-Vallamsetty/wisecow.git](https://github.com/Krishna-Vallamsetty/wisecow.git)
cd wisecow

Start your local Kubernetes cluster:

minikube start

Deploy the application to the cluster: The deployment.yaml is pre-configured to use the public Docker image krishna2317/wisecow:latest.

kubectl apply -f k8s/

Verify the deployment: Wait a minute for the image to be pulled, then check that the pods are running.

kubectl get pods

You should see two wisecow-deployment pods with a Running status.

Access the application: This command will automatically open the application in your web browser.

minikube service wisecow-service

You should see the message: Moo! Hello from the Wisecow Go Application!

🤖 CI/CD Pipeline
This project features a fully automated Continuous Integration (CI) pipeline using GitHub Actions.

Trigger: The workflow is automatically triggered on every git push to the main branch.

Process:

The code is checked out.

The workflow securely logs in to Docker Hub using repository secrets.

A new Docker image is built using the Dockerfile.

The newly built image is tagged and pushed to the Docker Hub repository at krishna2317/wisecow:latest.


### **Push Your Updated README to GitHub**

Now that you have the correct content, you need to push this final change to your GitHub repository.

**Your Final Action:**
In your terminal, run these commands one last time:

1.  **Add the changed file:**
    ```bash
    git add README.md
    ```

2.  **Commit the change:**
    ```bash
    git commit -m "docs: Update README with professional project description"
    ```

3.  **Push to GitHub:**
    ```bash
    git push origin main
