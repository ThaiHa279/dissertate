output "service_id" {
  description = "The ID of the created Kubernetes service"
  value       = kubernetes_service.my_service.id
}

output "service_url" {
  description = "The URL of the created Kubernetes service"
  value       = kubernetes_service.my_service.load_balancer_ingress.0.hostname
}