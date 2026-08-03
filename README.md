## playground
repo housing various experiments and tests, just for fun

### Trivy Testing
I wanted to explore the Trivy tool for scanning Docker images for vulnerabilities. The `.github/workflows/trivy-test.yml` workflow does the following:
* workflow builds one of two NGINX images and pushes it to the GitHub Container Registry tagged with the commit SHA
* runs a Trivy scan against the image
  * if the scan finds vulnerabilities, the SARIF is uploaded to the repository's Security page for review and the workflow exits
  * if the scan finds no or only acceptable vulnerabilities the workflow updates the image to be tagged with `preview-<commit-SHA>`
    * idea being that the image being tagged with `preview` marks it as having passed Trivy's scan and being ready to deploy to, e.g., an ephemeral preview environment
> [!NOTE] The docker image is in the /trivy-testing directory. There are two `FROM` lines. One to build a vulnerable image, and another to build a secure image, so that Trivy's behaviour can be observed.

### info
update info by running `tree -a -I '.git' -L 3` from repo root
```bash
.
├── .editorconfig
├── .github
│   └── workflows
│       └── trivy-test.yml
├── README.md
└── trivy-testing
    └── Dockerfile
```