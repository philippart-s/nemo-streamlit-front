ARG GITPOD_IMAGE=gitpod/workspace-python-3.8:latest
FROM ${GITPOD_IMAGE}

## Install ovhai client
RUN curl https://cli.gra.training.ai.cloud.ovh.net/install.sh | bash