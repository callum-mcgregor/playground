## playground
repo housing various experiments and tests, just for fun

### GitHub Actions Workflows
#### `semgrep.yml`
Semgrep is a powerful security tool with a various offerings. Here the `semgrep.yml` workflow runs a `semgrep ci` scan from a Docker container on the following events:
* On all Pull Request events (diff-based scan)
* On a Push to the main branch containing changes to the Semgrep workflow
* Daily at 08:00AM (against the entire repository)
* On manual trigger (workflow dispatch)

This implementation relies on a `SEMGREP_APP_TOKEN` created in the Semgrep Console and (in this case) added to repo/environment secrets - this workflow won't work without it. You can set this up completely for free though via [Semgrep](https://semgrep.dev/), they have a fully fledged free-tier, but it's designed for _very_ small teams/individuals

The Semgrep scan looks for code vulnerabilities, supply chain issues, and secrets that might've been accidentally committed. You can see some examples of detected code vulnerabilities in the comments of this dummy PR: https://github.com/callum-mcgregor/playground/pull/5. Note: I set up Semgrep within my Semgrep Console to exit with code 1 and comment on the PR when HIGH or CRITICAL vulnerabilities are found; then I set up a ruleset on my Repo to prevent PRs from being merged when certain CI/CD jobs fail (including the Semgrep scan). This prevents any HIGH or CRITICAL vulnerabilities from being merged to my main branch, and therefore (hypothetically) deployed to prod where they could be exploited. I also have a Semgrep policy that comments on a PR when any MEDIUM or LOW severity vulnerabilities are found, but not to block the PR

What you (the reader) can't see, is that these findings are also uploaded to my Semgrep console where I can review and manage findings from all repositories from a centralised location! 

Useful docs: https://docs.semgrep.dev/deployment/add-semgrep-to-ci#supported-ci-providers, https://docs.semgrep.dev/cli-reference#differences-between-semgrep-ci-and-semgrep-scan, https://docs.semgrep.dev/deployment/create-account-and-orgs

#### `trivy-test.yml`
I wanted to explore the Trivy tool for scanning Docker images for vulnerabilities. The `.github/workflows/trivy-test.yml` workflow does the following:
* builds one of two NGINX images and pushes it to the GitHub Container Registry tagged with the commit SHA
* runs a Trivy scan against the image
  * if the scan finds vulnerabilities, the SARIF is uploaded to the repository's Security page for review and the workflow exits
  * if the scan finds no or only acceptable vulnerabilities the workflow updates the image to be tagged with `preview-<commit-SHA>`
    * idea being that the image being tagged with `preview` marks it as having passed Trivy's scan and being ready to deploy to, e.g., an ephemeral preview environment
> [!NOTE] 
> The docker image is in the /trivy-testing directory. There are two `FROM` lines. One to build a vulnerable image, and another to build a secure image, so that Trivy's behaviour can be observed.

