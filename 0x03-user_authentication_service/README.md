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
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
</Details>

### Task 1.1. create user
Implement the add_user method, which has two required string arguments: email and hashed_password, and returns a User object. The method should save the user to the database. No validations are required at this stage.

Test result
<Details>
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_1.py
1
2
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# 
</Details>