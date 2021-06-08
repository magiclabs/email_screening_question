- [Overview](#overview)
  - [Requirements](#requirements)
- [Task](#task)
  - [How to check](#how-to-check)

# Overview
Usually it's more comfortable to use Terraform modules than just "long" manifests. This repo contains `state-metrics` K8s service namespace and deployment manifest. 

## Requirements
* Local K8s cluster

# Task 
* Install `state-metrics` with given terraform manifests (you may need to update `config_path` in the `_provider.tf` file)
* Modify code to make `state-metrics` to be presented as module.
* Migrate currently deployed service from "plain manifest" to terraform module.
  * No pod should be recreated during the migration
  * Module should have some input variables to customize created resources
* Provide module and all related migration commands in the solution

## How to check
1. Run some container inside K8s with shell. For example:
  ```
  
  ```
