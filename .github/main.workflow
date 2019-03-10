workflow "Main Workflow" {
  on = "push"
  resolves = ["Install, Build, and Push"]
}

action "Master Only" {
  uses = "actions/bin/filter@d820d56839906464fb7a57d1b4e1741cf5183efa"
  args = "branch master"
}

action "Install, Build, and Push" {
  uses = "./gh-pages-pelican-action"
  needs = ["Master Only"]
  secrets = [
    "GIT_DEPLOY_KEY"
  ]
}
