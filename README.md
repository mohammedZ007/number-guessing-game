# Number Guessing Game

A web-based number guessing game built with Python Flask, containerized with Docker, and deployed to AWS using Terraform, Amazon ECR, Amazon EC2, and GitHub Actions.

## Project Overview

The application generates a random number between 1 and 10.

The player gets 3 chances to guess the number.

Game behavior:

- Correct guess → Player wins
- Difference of 2 or less → "Near"
- Difference greater than 2 → "Far"
- Number outside 1–10 → Invalid input
- Non-numeric input → Invalid input

The application is available through a Flask web interface.

## Project Structure

```text
number-guessing-game/
├── app/
│   ├── app.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── .terraform.lock.hcl
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Docker
- Terraform
- AWS EC2
- Amazon ECR
- AWS IAM
- AWS Security Groups
- GitHub
- GitHub Actions

## Docker

### Build the Docker image

```bash
docker build -t number-guessing-game .
```

### Run locally

```bash
docker run -d -p 3000:3000 --name number-guessing-game number-guessing-game
```

Open:

```text
http://localhost:3000
```

### Stop the container

```bash
docker stop number-guessing-game
```

### Remove the container

```bash
docker rm number-guessing-game
```

## AWS Infrastructure

Terraform is used to provision the AWS infrastructure.

The infrastructure includes:

- EC2 instance
- Security Group
- IAM Role
- IAM Instance Profile
- Amazon ECR repository

The EC2 instance runs Ubuntu and Docker.

The EC2 instance uses an IAM role with permission to pull images from Amazon ECR.

## Amazon ECR

The Docker image is stored in Amazon ECR.

Repository:

```text
number-guessing-game
```

The image is tagged and pushed to ECR by the GitHub Actions CD pipeline.

## GitHub Actions CI

The Continuous Integration workflow is:

```text
.github/workflows/ci.yml
```

The CI pipeline:

1. Checks out the source code.
2. Builds the Docker image.
3. Starts the Docker container.
4. Tests the Flask application.
5. Stops and removes the test container.

The CI workflow runs when code is pushed to the `main` branch.

## GitHub Actions CD

The Continuous Deployment workflow is:

```text
.github/workflows/cd.yml
```

The CD pipeline:

1. Runs after the CI workflow completes successfully.
2. Configures AWS credentials.
3. Logs in to Amazon ECR.
4. Builds the Docker image.
5. Tags the image.
6. Pushes the image to Amazon ECR.
7. Connects to the EC2 instance through SSH.
8. Pulls the latest Docker image from ECR.
9. Stops the previous container.
10. Removes the previous container.
11. Starts the latest application container.

## CI/CD Flow

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions - CI
    |
    | Build & Test
    v
GitHub Actions - CD
    |
    v
Amazon ECR
    |
    | Pull Docker Image
    v
Amazon EC2
    |
    v
Docker Container
    |
    v
Flask Web Application
```

## Accessing the Deployed Application

The application is deployed on an AWS EC2 instance and exposed on port `3000`.

Application URL:

```text
http://65.1.107.133:3000
```

## Local Development

Clone the repository:

```bash
git clone https://github.com/mohammedz007/number-guessing-game.git
```

Enter the project directory:

```bash
cd number-guessing-game
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python3 app/app.py
```

Open:

```text
http://localhost:3000
```

## DevOps Concepts Demonstrated

This project demonstrates an end-to-end DevOps workflow involving:

- Git and GitHub
- Linux
- Python application deployment
- Docker
- Docker image management
- Terraform infrastructure provisioning
- AWS EC2
- Amazon ECR
- IAM roles
- Security Groups
- Remote server deployment
- Continuous Integration
- Continuous Deployment
- GitHub Actions
