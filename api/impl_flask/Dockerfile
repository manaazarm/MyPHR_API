# Use the official Python image.
# https://hub.docker.com/_/python
FROM python

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .
COPY myphr-api-firebase-adminsdk-qfh5m-73a706148a.json myphr-api-firebase-adminsdk-qfh5m-73a706148a.json

# Install production dependencies.
RUN pip install Flask==1.0.2 \
    gunicorn \
    connexion==2.0.0 \
    python_dateutil==2.6.0 \
    passlib==1.7.1 \
    firebase-admin==2.16.0 \
    google-api-core==1.9.0 \
    google-auth==1.6.3 \
    google-cloud-core==0.29.1 \
    google-cloud-firestore==0.32.1 \
    google-cloud-storage==1.14.0 \
    google-resumable-media==0.3.2 \
    googleapis-common-protos==1.5.9 \
    grpcio==1.19.0



# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 4 wsgi:app
