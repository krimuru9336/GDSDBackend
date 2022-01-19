
## Run ##

0. move to project root folder


1. Activate a virtualenv (Python 3) ( virtual env is already made and you just have to activate that)
```bash
pipenv --python 3 shell
```


2. Create a MySQL database
```sql
CREATE DATABASE chat CHARACTER SET utf8;
```
3. Download Redis (Download Redis for windows from here https://www.memurai.com/) 


4. Init database
```bash
./manage.py migrate
```

5. Create admin user
```bash
./manage.py createsuperuser
```

6. Run development server
```bash
./manage.py runserver
```

To override default settings, create a local_settings.py file in the chat folder.

Message prefetch config (load last n messages):
```python
MESSAGES_TO_LOAD = 15
```
