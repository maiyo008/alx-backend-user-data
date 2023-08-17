# Tasks
----
### Task 0. User model
In this task you will create a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy).

The model will have the following attributes:

* id, the integer primary key
* email, a non-nullable string
* hashed_password, a non-nullable string
* session_id, a nullable string
* reset_token, a nullable string

Test result
<Details>

```
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
```
</Details>

### Task 1. create user
Implement the add_user method, which has two required string arguments: email and hashed_password, and returns a User object. The method should save the user to the database. No validations are required at this stage.

Test result
<Details>

```
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_1.py
1
2
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# 
```
</Details>

### Task 2. Find user
In this task you will implement the DB.find_user_by method. This method takes in arbitrary keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments. No validation of input arguments required at this point.

Make sure that SQLAlchemy’s NoResultFound and InvalidRequestError are raised when no results are found, or when wrong query arguments are passed, respectively.

Test result
<Details>

```
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_2.py
1
1
Not found
Invalid
```
</Details>

### Task 3. Update user
In this task, you will implement the DB.update_user method that takes as argument a required user_id integer and arbitrary keyword arguments, and returns None.

The method will use find_user_by to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.

If an argument that does not correspond to a user attribute is passed, raise a ValueError.

Test result
<Details>

```
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_3.py
1
Password updated
```
</Details>

### Task 3. Hash password
In this task you will define a _hash_password method that takes in a password string arguments and returns bytes.

The returned bytes is a salted hash of the input password, hashed with bcrypt.hashpw.

Test result
<Details>

```
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_4.py
b'$2b$12$p6RYNO6jDLcFqfFkUbMh5OcRdFruSxcK967XCtRcAQ/3ShfxYLgnW'
```
</Details>

### Task 5. Register user
Auth.register_user should take mandatory email and password string arguments and return a User object.

If a user already exist with the passed email, raise a ValueError with the message User <user's email> already exists.

If not, hash the password with _hash_password, save the user to the database using self._db and return the User object.

Test Result
<Details>

```
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_5.py
successfully created a new user!
could not create a new user: User me@me.com already exists
```
</Details>

### Task 6. Basic Flask app
In this task, you will set up a basic Flask app.

Create a Flask app that has a single GET route ("/") and use flask.jsonify to return a JSON payload of the form:

### 7. Register user
In this task, you will implement the end-point to register a user. Define a users function that implements the POST /users route.

Import the Auth object and instantiate it at the root of the module

The end-point should expect two form data fields: "email" and "password". If the user does not exist, the end-point should register it and respond with the following JSON payload:

`{"email": "<registered email>", "message": "user created"}`
If the user is already registered, catch the exception and return a JSON payload of the form

`{"message": "email already registered"}`
and return a 400 status code

Test result
Terminal 1.
<Details>

```
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [17/Aug/2023 11:16:56] "POST /users HTTP/1.1" 200 -
127.0.0.1 - - [17/Aug/2023 11:17:29] "POST /users HTTP/1.1" 200 -
```
</Details>
Terminal 2.
<Details>

```
root@2c462bd13a86:~# curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /users HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 36
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 36 out of 36 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 48
< Server: Werkzeug/2.0.3 Python/3.6.9
< Date: Thu, 17 Aug 2023 08:16:56 GMT
< 
{"email":"bob@me.com","message":"user created"}
* Closing connection 0
root@2c462bd13a86:~# curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd' -v
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /users HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 36
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 36 out of 36 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 39
< Server: Werkzeug/2.0.3 Python/3.6.9
< Date: Thu, 17 Aug 2023 08:17:29 GMT
< 
{"message":"email already registered"}
* Closing connection 0
root@2c462bd13a86:~# 
```
</Details>

### Task 8. Credentials validation
In this task, you will implement the Auth.valid_login method. It should expect email and password required arguments and return a boolean.

Try locating the user by email. If it exists, check the password with bcrypt.checkpw. If it matches return True. In any other case, return False.

Test run
<Details>

```
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_8.py
True
False
False
```
</Details>