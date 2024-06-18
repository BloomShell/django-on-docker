aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 778427007994.dkr.ecr.us-east-1.amazonaws.com
docker pull 778427007994.dkr.ecr.us-east-1.amazonaws.com/ilovebees-django:web
docker pull 778427007994.dkr.ecr.us-east-1.amazonaws.com/ilovebees-django:nginx-proxy
docker-compose -f docker-compose.prod.yml up -d