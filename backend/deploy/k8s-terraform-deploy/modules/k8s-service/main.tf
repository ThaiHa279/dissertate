resource "kubernetes_service" "example" {
  metadata {
    name = var.service_name
  }
  spec {
    selector = {
      App = kubernetes_pod.example.metadata.0.labels.App
    }
    session_affinity = "None"
    port {
      port        = var.service_port
      target_port = var.target_port
    }
  }
}

resource "kubernetes_pod" "example" {
  metadata {
    name = var.pod_name
    labels = {
      App = var.app_label
    }
  }
  spec {
    container {
      image = var.container_image
      name  = var.container_name
    }
  }
}