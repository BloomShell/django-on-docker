aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 658435454654.dkr.ecr.us-east-1.amazonaws.com
docker pull 658435454654.dkr.ecr.us-east-1.amazonaws.com/django-on-docker-django:web
docker pull 658435454654.dkr.ecr.us-east-1.amazonaws.com/django-on-docker:nginx-proxy
docker-compose -f docker-compose.prod.yml up -d
