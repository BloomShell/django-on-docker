# Dockerized Django Project on AWS EC2

## Project Overview
This project involves the containerization of a Django web application using Docker. The stack includes Django for the web framework, PostgreSQL for the database, Gunicorn as the application server, and Nginx as the reverse proxy server. The deployment is managed on an Amazon Web Services (AWS) EC2 instance. This setup is ideal for scalable, production-grade web applications.

![Django](https://img.icons8.com/color/48/000000/django.png)
![Docker](https://img.icons8.com/color/48/000000/docker.png)
![AWS EC2](https://img.icons8.com/color/48/000000/amazon-web-services.png)

## Prerequisites
Before you begin, ensure you have the following:
- **Docker** installed on your local machine.
- **AWS Account** to create and manage EC2 instances.
- **Git** for version control.

## Architecture
The architecture consists of:
- **Django**: The backend framework handling requests and database interactions.
- **PostgreSQL**: A robust relational database system for storing application data.
- **Gunicorn**: A Python WSGI HTTP Server to serve the Django application.
- **Nginx**: A web server to act as a reverse proxy, handling client requests and forwarding them to Gunicorn.
- **AWS EC2**: The cloud environment where the application is hosted.

Each component runs in a separate Docker container, facilitating isolated environments and consistent behavior across different stages of development and deployment.

## Important Commands

* Build and run containers:
```bash
docker-compose up --build
```

* Stop containers:
```bash
docker-compose down
```

* View logs:
```bash
docker-compose logs -f
```

* Run a command inside a container:
```bash
docker-compose exec <service_name> <command>
```

## Credits and Resources

This project setup was inspired by and closely follows the comprehensive guide on [TestDriven.io](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/). It provides an in-depth look at containerizing Django applications and is a valuable resource for understanding the Docker ecosystem.

For more details and additional resources, visit:
- [Django Documentation](https://docs.djangoproject.com/)
- [Docker Documentation](https://docs.docker.com/)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
