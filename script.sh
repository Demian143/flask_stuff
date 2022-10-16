#!/bin/bash

# remove old container
sudo docker rm postgres
# start new container
sudo docker-compose up

# start flask app
# flask run
