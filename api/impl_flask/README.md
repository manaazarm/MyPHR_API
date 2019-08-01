# myphr

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m openapi_server
```
To run api.py:
in iTerm go to impl_flask folder and type:   conda activate python36
then: python3 api.py

## Docker Builds

    cd api/impl_flask/
    docker build -t myphr-test .

    # local run
    PORT=8080 && docker run -p 8080:${PORT} -e PORT=${PORT} myphr-test

## glcoud builds

    gcloud builds submit --tag gcr.io/myphr-api/myphr && \
    gcloud beta run deploy --image gcr.io/myphr-api/myphr

    