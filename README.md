# Hackathons
Backend Apis for hackathon management platform

#### The Users app
This app handles user registration and authorization.It uses a custom user model which uses Email for authentication. Token based authentication system is implemented.The userprofile model stoes user information, mainly added keeping scalablity in mind.

#### The hackathon_api app
The hackathon_api app handles all fuctions for hackathon management.It allows creation,Listing and registraion of hackathons.The endpoints in this app are only accessable to authentiated user.

#### Submissions app

This app handels submissions.It allows to submit your submissions to hackathons as well as viewing your past submissions.Only accessable to authenticated user.


#### Available API endpoints

##### Users App
'users/register/' ->  Register user to the site.<br>
'users/login/' ->  Login user to the site.<br>
'users/logout/' ->  Logout user from the site.<br>

##### hackathon_api App

'api/hackathons' ->  List the available hackathons<br>
'api/create/' ->  Create a hackathon by registered user<br>
'api/register/<int:hackathon_id>' ->  Register user for a hackathon<br>
'api/enrolled' ->  List the hackkathons user is enrolled in<br>

##### Submission App


'submissions/create/<int:hackathon_id>' ->  Register user for a hackathon<br>
'submissions/my_submissions/<int:hackathon_id>' ->  List all the users submissions to a hakathon<br>


#### Steps To Run
Fork this repo<br>
Clone repo<br>
cd to cloned repo<br>
pip install -r requirements.txt<br>
python manage.py runserver

Improper commit messages will be fixed shortly :)
