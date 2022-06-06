terraform {
  required_version = ">= 1.2.1" # terraform
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.11" # k8s
    }
  }
}
