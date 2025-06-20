# Videoflix (backend)


## Table of Contents

1. [About the Project](#about-the-project)
2. [Technologies](#technologies)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [API Endpoints](#api-endpoints)

## About the Project

- This project is a RESTful API backend for a wb app video platform
- The user can register a account, verify the account, login, reset the password, request a new password
- You can upload videos and backend handles the formatting of the videos
- The videos can afterwards switch between 4 different qualities (120p, 360p, 720p, 1080p) or you can select "auto" and the best quality will be selected automatically

## Technologies

- Python (Version 3.12.4)
- Django (Version 5.1.5)
- Django REST Framework (Version 3.15.2)
- RQ for running complex tasks in the background
- PostgreSQL for database management

## Prerequisites

- Docker with docker-compose
- Docker Desktop
- Git

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/Tom5424/Videoflix-backend.git .
   ```

2. Create .env data with credentials


3. Paste credentials with your own values

   ```
   DJANGO_SUPERUSER_USERNAME=admin
   DJANGO_SUPERUSER_PASSWORD=adminpassword
   DJANGO_SUPERUSER_EMAIL=admin@example.com

   SECRET_KEY="django-insecure-lp6h18zq4@z30symy*oz)+hp^uoti48r_ix^qc-m@&yfxd7&hn"
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   CSRF_TRUSTED_ORIGINS=http://localhost:4200,http://127.0.0.1:4200

   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=db
   DB_PORT=5432

   REDIS_HOST=redis
   REDIS_PORT=6379

   CELERY_ACCEPT_CONTENT=json
   CELERY_TASK_SERIALIZER=json
   CELERY_RETRY_ON_STARTUP=True
   FLOWER_PORT=5555

   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend 
   EMAIL_HOST=smtp.example.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_email_user
   EMAIL_HOST_PASSWORD=your_email_user_password
   EMAIL_USE_TLS=True
   EMAIL_USE_SSL=False
   DEFAULT_FROM_EMAIL=default_from_email
   ```


4. Build and start the project using docker compose:

   ```
   docker compose up --build
   ```


5. Start celery in a running docker container:

   ```
   docker-compose exec web celery -A videoflix worker --loglevel=info
   ```    


## Usage


- First you need to upload videos in your backend, you need a video in .mp4 format
- Visit the admin dashboard http://localhost:8000/admin and log in with your superuser credentials
- Go to the Videos section and then, give your video a title, description, and a category. If no category exist add them
- Save your video, the backend will handle the process of converting the video automatically
- After creating a video for your app you can register about the frontend a new account, verify it in the email that will be sent then log in to Videoflix and enjoy watching your videos


## API Endpoints


#### Authentification Endpoints:


- METHOD POST ``` /api/auth/registration/ ``` Registers a new user

- METHOD POST ``` /api/auth/registration/verify-email/ ``` Verifies the email after registering

- METHOD POST ``` /api/auth/login/ ``` Login a user

- METHOD POST ``` /api/auth/guest-login/ ``` Login a guest user

- METHOD POST ``` /api/auth/guest-logout/ ``` Logout a user

- METHOD POST ``` /api/auth/password/reset/ ``` Sends a email with a link to reset the password.

- METHOD POST ``` /api/auth/password/reset/confirm/ ``` Resets the password after the inputs are valid


#### Video Endpoints:


- METHOD GET ``` /api/unwatched-videos/ ``` Returns a list of all unwatched videos

- METHOD GET ``` /api/watched-videos/ ``` Returns a list of all watched videos

- METHOD GET ``` /api/video/${videoId}/ ``` Returns single video with the corresponding id
