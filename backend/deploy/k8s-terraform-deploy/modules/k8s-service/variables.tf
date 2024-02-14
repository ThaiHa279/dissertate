variable "service_name" {
  description = "The name of the Kubernetes service"
  type        = string
}

variable "service_port" {
  description = "The port that the service will expose"
  type        = number
}

variable "target_port" {
  description = "The port that the service will forward traffic to"
  type        = number
}

variable "selector" {
  description = "The selector to determine which pods will receive traffic"
  type        = map(string)
}