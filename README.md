# Flask BLog
---
This project walk through how you can generate a simple CRUD using flask python framework.

## Installing
- Make sure you have install python in your machine (recommended v 3.10.1)
- Download sorce code or clone this repo
- Generate virtual environment (Windows: `py -3 -m venv venv`, Linux/Mac: `python3 -m venv venv`) 
- Activate virtual environment (Windows: `venv\Scripts\activate`, Linux/Mac: `. venv/bin/activate`)
- Install dependecies using command `pip install -e .`
- Init database (Windows: run file **__init_db__.bat**, Linux/Mac: `flask --app flaskr init-db`)
- Under **intance** directory generate **__config__.py**
- Run command `python -c 'import secrets; print(secrets.token_hex())'` then copy hex encode token
- In **__config__.py** paste as `SECRET_KEY = <hex encode token>`
- Run the application and hit on [localhost](http://localhost:8080) (Windows: run file **__init__.bat**, Linux/Mac: `flask run --debug --port 8080`)

Application is ready to use.
