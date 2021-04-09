# teacher_directory_app: 
Directory app containing all the Teachers in a given school.

#after clone the project: 
#create virtual environmenet
create virtualenv .

#activate it: 
.\Scripts\activate

#install requirements: 
pip install requirements.txt

#migrations: 
python manage.py makemigrations tdapp
python manage.py migrate

#Run it: 
python manage.py runserver

#ADMIN PANEL: 
username = admin
passwordv = admin

#AT THE 'REGISTER' SECTION YOU CAN REGISTER THE STAFF

#AT THE 'LOGIN' SECTION YOU CAN LOGIN THE STAFF: 
LOGIN USERS BY USERNAMES which are firstname and lastname combination e.g. LaticiaLanden, 
password will be the firstname of the user e.g. Laticia


#You can search user by any letter of the last name of some last name letters.

#You can see details at the details page.

#You can register/import new users by registering them into the site!



