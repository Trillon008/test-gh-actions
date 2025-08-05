locals {
  policies = {
    "dummy-key" = {
      certificat = ["List", "Get"],
      secret     = "machin"
      key        = ["maclef"]
    }
    #mre_sry_data
    mry_data_priv =
      certificat = ["List", "delete"]
      key        = ["maclef"]
    }
  }

  mydict = {}
}

resource "null_resource" "check" {
  for_each = local.policies
  triggers = {
    tenant_id    = each.key
    certificates = each.value.certificat[0]
    secret       = lookup(each.value, "secret", "")
    key          = each.value.key[0]
  }
}
