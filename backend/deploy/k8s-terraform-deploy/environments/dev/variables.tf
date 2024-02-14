variable "namespace" {
  description = "The namespace for the Kubernetes service"
  default     = "dev"
}

variable "service_name" {
  description = "The name of the Kubernetes service"
}

variable "service_port" {
  description = "The port that the Kubernetes service will expose"
  type        = number
}