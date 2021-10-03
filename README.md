**Postman link**
https://www.getpostman.com/collections/9da7c4ad5747d2137ebc

**Steps to start if you want to start project localy (enter to terminal):**

1 `pip install -r requirements.txt`

2 `python3 manage.py makemigrations comment`

`python3 manage.py makemigrations post`

3 `python3 manage.py migrate`

4 `python3 manage.py migrate django_cron`

5 `python3 manage.py migrate createsuperuser`

6 `python3 manage.py runserver`

7 `python3 manage.py runcrons`

8 **If you changed smth** enter to terminal

`black app`

`flake8 app`

9 **If you add library** enter to terminal

`pip freeze>requirements.txt`

