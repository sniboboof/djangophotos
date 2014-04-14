This is a photo viewing web app made with Django

django project: Album Project
Meant to be a web site for people to upload and organize their own photos and display them to the world. Displaying photos are largely open to the public but managing albums and photo tags are specific to the photo's owner.

album app:
the central app of the website that contains the main models for the photos, users, albums, and tags as well as the views related to photos, albums, and tags.

note that, currently, registration and logging in of users is not supported and database information must be managed on the admin side.

views written with much reference to lordsheepy's django app
deployment done with help from risingmoon

next steps to improve:
rewrite User model or straight-up remove it in lieu of django's login system and user
add editing views so users can upload photos and edit their metadata without asking an admin to do it
use some css to get the photos and albums to display in a grid
make some adjustments to the fabric so deployment isn't 90% my personal job.
