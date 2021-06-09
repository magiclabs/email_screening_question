resource "kubernetes_service_account" "state_metrics_local" {
  provider = kubernetes.local

  automount_service_account_token = false

  metadata {
    name      = "state-metrics"
    namespace = kubernetes_namespace.mon_local.metadata[0].name

    labels = {
      app = "state-metrics"
    }
  }
}

resource "kubernetes_cluster_role" "state_metrics_local" {
  provider = kubernetes.local

  metadata {
    name = "state-metrics"

    labels = {
      app = "state-metrics"
    }
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = [""]
    resources = [
      "configmaps",
      "secrets",
      "nodes",
      "pods",
      "services",
      "resourcequotas",
      "replicationcontrollers",
      "limitranges",
      "persistentvolumeclaims",
      "persistentvolumes",
      "namespaces",
      "endpoints"
    ]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["extensions"]
    resources  = ["daemonsets", "deployments", "replicasets", "ingresses"]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["apps"]
    resources  = ["statefulsets", "daemonsets", "deployments", "replicasets"]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["batch"]
    resources  = ["cronjobs", "jobs"]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["autoscaling"]
    resources  = ["horizontalpodautoscalers"]
  }

  rule {
    verbs      = ["create"]
    api_groups = ["authentication.k8s.io"]
    resources  = ["tokenreviews"]
  }

  rule {
    verbs      = ["create"]
    api_groups = ["authorization.k8s.io"]
    resources  = ["subjectaccessreviews"]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["policy"]
    resources  = ["poddisruptionbudgets"]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["certificates.k8s.io"]
    resources  = ["certificatesigningrequests"]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["storage.k8s.io"]
    resources  = ["storageclasses", "volumeattachments"]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["admissionregistration.k8s.io"]
    resources  = ["mutatingwebhookconfigurations", "validatingwebhookconfigurations"]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["networking.k8s.io"]
    resources  = ["networkpolicies", "ingresses"]
  }

  rule {
    verbs      = ["list", "watch"]
    api_groups = ["coordination.k8s.io"]
    resources  = ["leases"]
  }
}

resource "kubernetes_cluster_role_binding" "state_metrics_local" {
  provider = kubernetes.local

  metadata {
    name = "state-metrics-binding"

    labels = {
      app = "state-metrics"
    }
  }

  role_ref {
    kind      = "ClusterRole"
    name      = kubernetes_cluster_role.state_metrics_local.metadata[0].name
    api_group = "rbac.authorization.k8s.io"
  }

  subject {
    kind      = "ServiceAccount"
    name      = kubernetes_service_account.state_metrics_local.metadata[0].name
    namespace = kubernetes_namespace.mon_local.metadata[0].name
    api_group = ""
  }
}

resource "kubernetes_deployment" "state_metrics_local" {
  provider = kubernetes.local

  metadata {
    name      = "state-metrics"
    namespace = kubernetes_namespace.mon_local.metadata[0].name

    labels = {
      app = "state-metrics"
    }
  }

  spec {
    replicas = 1

    strategy {
      type = "Recreate"
    }

    selector {
      match_labels = {
        app = "state-metrics"
      }
    }

    progress_deadline_seconds = 180

    template {
      metadata {
        namespace = kubernetes_namespace.mon_local.metadata[0].name
        labels = {
          app = "state-metrics"
        }

        annotations = {
          # Full DD integradion doc:
          # https://github.com/DataDog/integrations-core/blob/master/kubernetes_state/datadog_checks/kubernetes_state/data/conf.yaml.example
          "ad.datadoghq.com/state-metrics.check_names"  = jsonencode(["kubernetes_state"])
          "ad.datadoghq.com/state-metrics.init_configs" = "[{}]"
          "ad.datadoghq.com/state-metrics.instances" = jsonencode([{
            kube_state_url          = "http://%%host%%:18080/metrics"
            prometheus_timeout      = 30
            min_collection_interval = 30
            telemetry               = true
            label_joins = {
              kube_deployment_labels = {
                labels_to_match = ["deployment"]
                labels_to_get = [
                  "label_app",
                  "label_deploy_env",
                  "label_type",
                  "label_magic_net",
                  "label_canary",
                ]
              }
            }
            labels_mapper = {
              # We rename following labels because app and deploy_env are our "well known labels"
              label_app        = "app"
              label_deploy_env = "deploy_env"
            }
          }])
        }
      }

      spec {
        enable_service_links            = false
        service_account_name            = kubernetes_service_account.state_metrics_local.metadata[0].name
        automount_service_account_token = true

        host_network = true

        container {
          # docker run --rm -it k8s.gcr.io/kube-state-metrics/kube-state-metrics:v1.9.8 --help
          image                    = "k8s.gcr.io/kube-state-metrics/kube-state-metrics:v1.9.8"
          image_pull_policy        = "IfNotPresent"
          name                     = "state-metrics"
          termination_message_path = "/dev/termination-log"
          command = [
            "/kube-state-metrics",
            "--port=18080",
            "--telemetry-port=18081",
          ]

          readiness_probe {
            http_get {
              path = "/healthz"
              port = "18080"
            }

            initial_delay_seconds = 5
            timeout_seconds       = 5
          }

          resources {
            requests = {
              cpu    = "30m"
              memory = "30Mi"
            }

            limits = {
              cpu    = "60m"
              memory = "50Mi"
            }
          }
        }
      }
    }
  }

  depends_on = [
    kubernetes_cluster_role_binding.state_metrics_local,
  ]
}
