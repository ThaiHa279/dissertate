variable "region" {
  description = "The region where resources should be created"
  type        = string
  default     = "us-west-2"
}

variable "cluster_name" {
  description = "The name of the Kubernetes cluster"
  type        = string
}

variable "service_name" {
  description = "The name of the Kubernetes service"
  type        = string
}