# nemo-streamlit-front
Source code for the front for Nemo talk with streamlit

## Requirements GitPod

    - install libsndfile-dev : `sudo apt-get install libsndfile-dev`
    - install requirements with pip : `pip install requirements.txt`

## Requirements MacOs M1

    - installation de libsndfile : `brew install libsndfile`
    - add env variable : `export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"`
    - installation de tensorflow : `pip install tensorflow-macos`

## Docker

    - build image : `docker build . -t wilda/nemo-front-end:1.0.0 `
    - run image : `docker run -p 8501:8501 -e API_URL=<back-end URL> wilda/nemo-front-end:1.0.0`

## Local

    - create / update the following environment variables:
        - `export API_URL=https://c3e41ac3-d928-429e-a041-ab625f709aee.app.gra.training.ai.cloud.ovh.net`
        - `export PATH=$PATH:/Users/stef/Library/Python/3.8/bin`
