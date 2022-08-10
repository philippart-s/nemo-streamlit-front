# nemo-streamlit-front
Source code for the front for Nemo talk with streamlit

## Requirements 

    - install requirements with pip : `pip install requirements.txt`

## Docker

    - build image : `docker build . -t wilda/nemo-front-end:1.1.0` or for Mac M1 : `docker buildx build --platform linux/amd64 . -t wilda/nemo-front-end:1.1.0`
    - run image : `docker run -p 8501:8501 -e API_URL=<back-end URL> wilda/nemo-front-end:1.1.0`

## Local

    - create / update the following environment variables:
        - `export API_URL=https://c3e41ac3-d928-429e-a041-ab625f709aee.app.gra.training.ai.cloud.ovh.net`
        - `export PATH=$PATH:/Users/stef/Library/Python/3.8/bin`

## OVHcloud :

  - run : ` ovhai app run --name nemo-front-end --unsecure-http --cpu 1 -p 8501 -e API_URL=<URL back end> wilda/nemo-front-end:1.1.0`