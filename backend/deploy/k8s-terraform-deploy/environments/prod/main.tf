provider "kubernetes" {
  # Configure the Kubernetes provider
}

module "k8s_service" {
  source = "../../modules/k8s-service"

  # Pass in environment-specific variables
  service_name = var.service_name
  service_port = var.service_port
}