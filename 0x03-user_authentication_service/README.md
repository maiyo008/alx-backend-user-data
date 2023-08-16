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

### Task 1. create user
Implement the add_user method, which has two required string arguments: email and hashed_password, and returns a User object. The method should save the user to the database. No validations are required at this stage.

Test result
<Details>
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_1.py
1
2
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# 
</Details>

### Task 2. Find user
In this task you will implement the DB.find_user_by method. This method takes in arbitrary keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments. No validation of input arguments required at this point.

Make sure that SQLAlchemy’s NoResultFound and InvalidRequestError are raised when no results are found, or when wrong query arguments are passed, respectively.

Test result
<Details>
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_2.py
1
1
Not found
Invalid
</Details>

### Task 3. Update user
In this task, you will implement the DB.update_user method that takes as argument a required user_id integer and arbitrary keyword arguments, and returns None.

The method will use find_user_by to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.

If an argument that does not correspond to a user attribute is passed, raise a ValueError.

Test result
<Details>
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_3.py
1
Password updated
</Details>

### Task 3. Hash password
In this task you will define a _hash_password method that takes in a password string arguments and returns bytes.

The returned bytes is a salted hash of the input password, hashed with bcrypt.hashpw.

Test result
<Details>
root@2c462bd13a86:~/alx-backend-user-data/0x03-user_authentication_service# python3 main_4.py
b'$2b$12$p6RYNO6jDLcFqfFkUbMh5OcRdFruSxcK967XCtRcAQ/3ShfxYLgnW'
</Details>