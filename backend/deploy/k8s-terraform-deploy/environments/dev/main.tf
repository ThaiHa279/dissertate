module "k8s_service" {
  source = "../../modules/k8s-service"

  // Pass in environment-specific variables here
  service_name = var.service_name
  service_port = var.service_port
}