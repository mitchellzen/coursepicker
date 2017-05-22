
Here's a simple, rapidly prototyped web application that uses React as a frontend and Django as a backend. 
This is very much unfinished, written in 2-3  hours and with a lot of "todos" to polish and complete.

To install the backend: 
- pip install -r requirements.txt

To install the frontend:
- npm install

To run: 
- python manage.py populate NUMBER_OF_NEW_COURSES
- python manage.py runserver (on backend)
- npm start (on frontend)

TODOs:

- This should probably exist in a Docker cluster via docker-compose (didn't get to)
- The enroll button should do something (didn't get to)
- There are bugs in the newest version of react-router clashing with the table library 
- Unit testing
- Bootstrap CSS to prettify


The manage.py populate script fills the database with random courses and professors derived from lorem ipsum. 
