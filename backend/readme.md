Install in docker
1. docker-compose up -d
2. Migrate database 'python manage.py migrate'
3. Create admin user 'python manage.py createsuperuser'
4. In url http://localhost:8001/o/applications/register/
    Register a new application
    - Client type: Confidential
    - Authorization grant type: Resource owner password-base
    - Copy and Paste CLIENT_ID and CLIENT_SECRET in auth.py
5. Log to api