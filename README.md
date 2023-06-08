# Hackathons
Backend Apis for hackathon management platform

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
