FROM nginxinc/nginx-unprivileged:1.30-alpine3.24@sha256:9b87ad3dd9f431c733f19dfb278c7eb3dba9dca381942c79818bb42f1a566a83

# Switch to root to perform package updates
USER root
RUN apk update && apk upgrade --no-cache   

# Switch back to unprivileged user
USER 101 

# Image with vulns to trigger Trivy
# FROM nginx:1.19-alpine