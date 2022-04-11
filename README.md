# RANGE BLOGGER

## A simple blog web app

### Starting the project:

1. Create a **virtual environment** with venv (install virtualenv, if its not installed).

    ```
    virtualenv venv
    ```

2. Clone the project in the virtual environment directory.

    ```
    git clone https://github.com/darkdeathgunn/range_blogger.git
    ```

3. Activate the virtual environemnt.

    #### For Linux/Mac OSX   
    ```
    source bin/activate
    ```

    #### For Windows
    ```
    .\Scripts\activate
    ```

4. Install the requirements.

    ```
    cd blog
    pip install -r requirements.txt
    ```


5. Run the Migrations
    ```
    python manage.py makemigrations
    
    python manage.py migrate
    ```
6. Run the development server
    ```
    python manage.py runserver
    ```
7. Head to server http://127.0.0.1:8000

HAVE FUN!!!!!

## For contributors

Range blogger uses the following technologies:

+ HTML/CSS/JavaScript
+ Pyhton(Django)
