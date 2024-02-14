# Kubernetes Service Deployment with Terraform

This project contains Terraform configurations to deploy a Kubernetes service in different environments (development and production) using modules.

## Project Structure

- `modules/`: Contains the reusable Terraform modules.
  - `k8s-service/`: Contains the Terraform configuration for creating a Kubernetes service.
- `environments/`: Contains the Terraform configurations for different environments.
  - `dev/`: Contains the Terraform configuration for the development environment.
  - `prod/`: Contains the Terraform configuration for the production environment.
- `main.tf`: The main Terraform configuration file. It sets up the provider and calls the modules for each environment.
- `variables.tf`: Declares the variables used in `main.tf`.
- `outputs.tf`: Defines the outputs of the main Terraform configuration.

## Usage

1. Navigate to the desired environment directory (e.g., `environments/dev`).
2. Initialize Terraform with `terraform init`.
3. Plan the deployment with `terraform plan`.
4. Apply the plan with `terraform apply`.

Please ensure you have the necessary permissions and the correct environment variables set for your provider.

## Note

This is a basic example and does not include aspects like security, load balancing, etc. Please modify and use it according to your requirements.