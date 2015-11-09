#!/usr/bin/env sh
docker build --no-cache=true -t python-rpm-builder .
mkdir -p dist
container=$(docker run -v `pwd`/dist:/rpms -d python-rpm-builder)
echo "Starter build container $container"
docker wait "$container"
echo "Build finished, deleting container and image"
docker rm "$container"
docker rmi python-rpm-builder
