provider "kubernetes" {
  config_path = "~/.kube/config"
}

module "k8s_service_dev" {
  source = "./modules/k8s-service"
  variables = "${var.service_variables_dev}"
}

module "k8s_service_prod" {
  source = "./modules/k8s-service"
  variables = "${var.service_variables_prod}"
}