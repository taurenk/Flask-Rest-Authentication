# Flask-Rest-Authentication
Proof of concept/Learning project on creating + securing stateless endpoints

#### About
Learning how to secure stateless services is very important. This project will highlight:
- Securing with basic username/password
- Securing with token based auth
 
#### Running the Project
Starting the service can be done by simply typing:

    python app.py
    
#### Session Based Login    
the endpoint "login/session_login" will create a session the user on the current server. 

#### Samples:

http://127.0.0.1:5000/task?where={"title":"learn potion"}
http://127.0.0.1:5000/login/session_login
    {"email":"tauren.kristich@gmail.com", "password":"test"}