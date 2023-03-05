# django-orm-watching-storage #
Site that shows visitors and visits duration.

### How to install ###
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```python
pip install -r requirements.txt
```

### How to use ###

U need to set variables in .env file:
`ENGINE` - DB_Engine, `HOST` - DB_Host, `PORT` - DB_Port, `NAME` - DB_Name, `USER` - DB_User,
`PASSWORD` - DB_Password, `SECRET_KEY` - Your secret key, `DEBUG` - True or False, `ALLOWED_HOSTS`

```python
python main.py
```
Go to 127.0.0.1:8000 and u got list of active cards.

```Список пользователей в хранилище```
Let u know whom in storage right now.

When u click at any name  u will get information of his visits.

### Project goals ###
The code is written for educational purposes on online-course for web-developers dvmn.org.
