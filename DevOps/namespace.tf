resource "kubernetes_namespace" "mon_local" {
  provider = kubernetes.local

  metadata {
    name = "mon"
  }
}
