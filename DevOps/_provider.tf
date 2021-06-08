provider "kubernetes" {
  alias       = "local"
  config_path = pathexpand("~/.kube/config")
}
