terraform {
  required_version = "1.10.5"
  required_providers {
    null = {
      source = "hashicorp/null"
    }
    random = {
      source = "hashicorp/random"
    }
  }
}

provider "null" {}
provider "random" {}
