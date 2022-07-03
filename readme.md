
docker build demodocker

docker images

docker tag 811f93b628a0   demodocker:v1.1

docker run -dp 5555:5555  demodocker:v1.1

python3 zmp_client.py