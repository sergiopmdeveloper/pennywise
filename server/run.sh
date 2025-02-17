#!/bin/bash

docker build -t pennywise-backend-service .

docker run \
  --env-file .env \
  --rm \
  --name pennywise-backend-service \
  -p 80:80 \
  -v $(pwd)/db.sqlite:/app/db.sqlite \
  pennywise-backend-service
