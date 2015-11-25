# Flask-Rest-Authentication
Proof of concept project on creating + securing stateless endpoints

#### About
POC  to create simple and secure REST Api's in Flask using Potion. Exploring different authentication methods is
another goal of project. We will be using:

- Flask-Login; auth with basic username/password + session. It is built on the standard flask session model, meaning after a user authenticates, a session cookie 
        will be handed off to the client.

- Flask-Principle;

- JWT; Upon authenticating, a signed token will be sent to the client.
 
#### Running the Project
Starting the service can be done by simply typing:

    python run.py
    

#### Api Samples [In Progess]
Task Api
GET http://127.0.0.1:5000/task?where={"title":"learn potion"}

Auth Api
http://127.0.0.1:5000/login/session_login
    {"email":"tauren.kristich@gmail.com", "password":"test"}