docker-compose -f docker-compose.prod.yml build
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 658435454654.dkr.ecr.us-east-1.amazonaws.com 
docker-compose -f docker-compose.prod.yml push
