[![Coverage Status](https://coveralls.io/repos/github/drg-v/final_project/badge.svg)](https://coveralls.io/github/drg-v/final_project)
[![Build Status](https://app.travis-ci.com/drg-v/final_project.svg?branch=main)](https://app.travis-ci.com/drg-v/final_project)
# Football matches predictions(English Premier League)

# Description
This project consists of 2 applications:
- Flask server located in this repository
- Angular client located here: [Angular client link](https://github.com/drg-v/final-project-client-)


## Project topic
I have decided to make an application that lets us make football matches predictions.
These is the main functionality of the project:
1. The project requires registration and authorization implemented with JWT:
   - the server generates token during login;
   - the client saves the token and sends it in every request;
2. There are 2 types of users:
   - user which can see lists of existing teams, matches and get predictions;
   - admin which can also delete and create matches and teams, block and subscribe users;
3. After registration and authrization client redirects to teams page where:
   - user can see the list of teams and go to the team\`s page by clicking on it\`s name;
   - admin can also delete team or add a new team by clicking on appropriate button;
4. At the team\`s page we can get all matches or select 2 dates and receive matches only for a certain period:
   - admin has an ability to create a new match or delete existing;
5. Admin has an access to the page where he can see the list of all users, subscribe or block them.
 
## Let\`s see the flow with illustrations
1. Registration page
  ![Registration page](/images/registration.png)
  
2. Login page
  ![Login page](/images/login.png)
  
3. Teams page for user
  ![Login page](/images/teams_user.png)
  
4. Teams page for admin
  ![Login page](/images/teams_admin.png)
  
5. Team page for user
  ![Login page](/images/team_user.png)
  
6. Team page for admin
  ![Login page](/images/team_admin.png)
  
7. Admin add team form
  ![Login page](/images/add_team.png)
  
8. Team matches for user
  ![Login page](/images/matches_user.png)
  
9. Team matches for admin
  ![Login page](/images/matche_admin.png)
  
10. Admin add match form
  ![Login page](/images/add_match.png)
  
9. Admin\`s users page
  ![Login page](/images/users_admin.png)
  
9. Match predictions
  ![Login page](/images/prediction.png)
 
## How to build the project

1. Make sure that `python` interpreter >= 3.8.10 and `pip` are installed on your computer.
2. Then clone this repository
  ```
  git clone https://github.com/drg-v/final_project
  ```
3. Create and activate python virtual environment
   - `cd final-project`
   - `python -m venv venv`
   - `source venv/bin/activate`
4. Next install requirements
   - `pip install -r requirements.txt`
5. Then  install and configure `gunicorn` with `nginx`
   - `https://www.youtube.com/watch?v=BpcK5jON6Cg&t=796s`
6. Start nginx server
   - `sudo systemctl start nginx`
7. Start gunicorn server
   - `gunicorn -w 4 wsgi:app`
8. Now the server can be reached at `https://127.0.0.1:8000`
9. Next download Angular client [here](https://github.com/drg-v/final-project-client-)
10. In client\`s root folder type `ng serve --open`
11. Previous command will open the client which can be reached at `http:localhost:4200/`
12. **Well done!**
