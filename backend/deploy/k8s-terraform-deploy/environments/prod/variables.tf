variable "namespace" {
  description = "The Kubernetes namespace to deploy the service in"
  type        = string
  default     = "production"
}

variable "replica_count" {
  description = "The number of replicas of the service to run"
  type        = number
  default     = 3
}