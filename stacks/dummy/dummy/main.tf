resource "null_resource" "dummy" {
  triggers = {
    github          = "This serve no purprose except bypass some GH actions limitations"
  }
}
