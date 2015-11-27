# Flask-Rest-Authentication
Proof of concept project on creating + securing Restful endpoints

#### About

 
#### Running the Project
Starting the service can be done by simply typing:

    python run.py
    
#### REST Services + Endpoints [In Progress]
There are current two applications/frameworks I am testing: Flask-Potion and Flask-Restless

#####Flask-Restless App
A simple user and task service implemented in Flask-Restful + Flask-Login. there is 2 ways to authenticate:
1. Stateless Access Token - Trade a username/password for an access token to use on requets
2. Stateful Session - Login with username/password and receive a session cookie which will be passed on requests

Get Access token:

    POST 127.0.0.1:5000/api/auth/access_token
    BODY: {"username":"", "password:""}
    
Get Task List:
    
    GET 127.0.0.1:5000/tasks?api_key=[ACCESS TOKEN]


#####Flask-Potion App
