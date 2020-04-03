# PoolDrillz - A pool billiard exercises database application

**Third milestone project; Data Centric Development - Full Stack Software Developer course - Code Institute**

PoolDrillz is a C.R.U.D.(create, read, update & delete) application. Users can find pool billiard exercises and make changes to them.
The user can:
- See an overview of all exercises
- Filter this overview on type of exercises
- Open each individual exercise in a page with all information
- Make changes to each exercise
- Add a new exercise
- Delete an exercise

The idea came to me because I'm a semi professional pool player. And for pool players, there is no clear path to
becoming a better player. There are many exercises and ideas floating around, but there's no clear overview. 
My eventual goal for PoolDrillz is for it to become an online community of pool players and trainers where information
is easily accessible and pool players of each level can find the right exercises for them based on which area of their 
game they want to improve on.

## Demo

[LIVE APPLICATION](https://pooldrillz.herokuapp.com/)

The application is hosted on Heroku.

![Image of PoolDrillz](/static/images/readmeimage.png)

## UX

### Users

Users of the application are pool players and trainers. They can use the application to find the right exercises for them.
And to share the exercises they know with others. 

#### User stories

Before starting to build the application. I wrote user stories so I knew which features the application needed to have.

[User stories](userstories.md)

### Mockup

I created a [mockup](https://ivarsaris.wixsite.com/pooldrillz) using Wix. I did this to decide how to style the application.
The layout of the mockup adapts to both desktop and mobile. For some reason, the mockup isn't responsive when using
chrome developer tools using the device toolbar. However, the layout is responsive on a mobile phone.

### Design

PoolDrillz is a simply designed application. The main purpose of this project was to build an application that connects to 
a database. The user can use this application to perform C.R.U.D. operations.

The main pages of the application can be accessed with one click from anywhere in the application. The links
are found in the navbar on top of the screen, and in the footer. I choose to use a sticky navbar, so it's always displayed 
on top of the screen. The navbar collapses on smaller screens, so it doesn't take up too much space. The user doesn't need to scroll up to the top to navigate to another page. 
The footer is stuck to the bottom, so it doesn't take up screen space when the user is scrolling through a page.

I started with blue(#0875c3) and orange(#FFA400) as the only colours used in the application. After a while, I decided that it was a little boring
and I wanted to add some more colours. I checked my favourite colour website [color-hex](https://www.color-hex.com/) to see which 
colors compliment orange and blue. Pink( #ff005b), and light green(#00ffa4) were recommended. I used these colours throughout the 
application. I also made the background of certain sections and of the exercise colums grey. I did this because I thought the whole
application was looking a little white.

I placed all forms in the center of the page. This because the forms are the most important part of the page. The attention 
needs to go there immediately. The same goes for the exercise information in the viewexercise template. The user can go straight back to the
exercises page from the viewexercise and editexercise template with a button.

I used Helvetica as font throughout the application. This for the simple reason that it's easy to read, and it looks neat as well. 

## Technologies used

The application has been made using the following Technologies:

* **HTML5** - Coding language used for creating the content and structure of the website
* **CSS** - Coding language used for styling the content
* **Python3** - Dynamic, object oriented programming language
* **Flask** - Open source Python framework used for building web applications
* **jQuery** - Used to simplify JavaScript for display purposes
* **MongoDB** - Online open source document oriented database
* **Google Chrome** - Used as browser and for developer tools
* [**Materialize**](https://materializecss.com/) - Framework library used for display, styling and icons
* **Git** - Used for version control
* [**Github**](https://github.com/) - Used to host the repository for the application
* [**Heroku**](https://www.heroku.com/) - Used to deploy the application

## Development process

I made the backed functionalities before I added the styling. I started with the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template)
for working in Gitpod. I created a repository in GitHub and linked this to the template. I had debug set to True throughout the development process. I changed it to false 
upon deployment in order to make sure no sensitive data could be retreived. I set my sensitive environment variables in Heroku settings, so they can't be retreived.

## Features

Features implemented, and left to be implemented later

### Features implemented

* Responsive layout and navigation
* Clear overview of all exercises
* User can filter this overview by type of exercise
* User can open each exercise in its own page
* User can create a new exercise and add it to the database
* User can make changes to an exercise
* User can delete an exercise from the database
* User can see some interesting statistics

### Features left to implement

There are some features that I could add with more time. One is another exercise filter, this one by skill level. 
Another feature would be some more interesting statistics. Lastly I would like to add pagination on the exercises page.
If many exercises are added, the page will become very long. Pagination will display the exercises by a certain amount
on the page. The user can click through the paginations. 

For other features I would like to implement, I would need a better understanding of the technology. Some features 
That I would like to add are the following:
* Allow user to create an account. In this account, the user can store exercises suitable for them.
* Password integration, so each user has a secure account.
* User can only delete an exercise he or she added to the database themself, this to avoid abuse.
* A forum on which users can discuss ideas and ask questions.
* An image template, where the user can drag balls onto an empty pool table to create an image for an exercise. 
* A high score table. Users can input their high score of an exercise, to create competition.
* Exercise review. Users can give a star rating to an exercise. The average of all ratings is displayed next to the exercise.

## Testing

I tested all parts of the application manually.

* All navigation buttons in the navbar lead to the intended page.
* All navigations buttons in the footer lead to the intended page.
* Exercises filter returns all exercises with the type of exercise filled out.
* Undo exercises filter returns all exercises again.
* Add exercise button leads to the add exercise page.
* A user can add an exercise to the database by filling out the form and submitting it.
* A user can leaves fields empty without causing issues. In this case, the default values I gave are shown.
* A user can input values and hit cancel. This will return the user to the exercises page.
* A user can make changes to an exercise by navigating to the edit exercise page.
* A user can make changes to an exercise, all new values replace the old ones in the database.
* A user can cancel making changes to an exercise. The exercise stays in the database with its original values.
* A user can delete an exercise. Before it's deleted, the user will see a pop up in which he has to confirm deleting this exercise.

I found it was easy to submit wrong information in the add exercise form. I implemented some defensive design 
in order to avoid this as much as possible. For example, I added a date picker, so the date format is always correct. This also ensures that the real latest added exercise
is displayed on the statistics page. When a user enters a name that's less than 3 or more than 30 characters, the add exercise page is reloaded with a warning message. The same goes 
if the user doesn't add a description, dificulty level, or skill type.

When a user clicks the delete button on the editexercise page, a pop up appears asking the user to confirm the deleting of the exercise. I did this to ensure no exercises
are deleted by accident.

When a user filters the exercises by a skill type which has no exercises in the database, an empty exercises page returned. I made sure when this happens, the exercises 
page is reloaded and a message is displayed stating there are no exercises of this type in the database.

When a user submitted a new exercise or made changes to an exising one, no feedback was gived. I added a feedback message so the user knows if an exercise 
was succesfully submitted or edited. 

### Responsiveness

I have used Chrome developer tools during the whole process of building the application. This to make sure the 
applications is responsive to all screen sizes and devices types. I have also run the application through https://responsivedesignchecker.com/
and checked many different devices. This to make sure the application looks good on all of them. I ensured the application
looks good on all devices from 320px width(smallest mobile device) and up. I also tested the application responsiveness manually on the following devices:

**Mobile** - Honor 10, Iphone 4, 7, and 10, and Samsung galaxy s9

**Tablet** - Ipad pro

**Desktop** - Lenovo 14 inch laptop, HP 15.6 inch laptop, and a 27 inch monitor 

### User interaction

### Browser compatibility

I ran the application in several browsers to make sure it's compatible with the most common ones. The application runs
well in Google Chrome, Mozilla Firefox, and Safari. 

### Code validation

I ran the code through several validators to make sure there are no mistakes. The HTML validators don't take Jinja template language into account,
so several errors were returned. I checked them and these were not mistakes.

**HTML5**

https://validator.w3.org/

https://html5.validator.nu/

**CSS**

https://codebeautify.org/cssvalidate

https://jigsaw.w3.org/css-validator/

**Python**

https://extendsclass.com/python-tester.html

http://pep8online.com/

## Installation

### Local Deployment

The application is deployed in Heroku. To get the app running locally, follow these steps:

1. Set up a workspace in your development environment
2. Clone the app from my GitHub repository with the following command: git clone https://github.com/ivarsaris/PoolDrillz-MS2
3. Change the directory with the following command: cd PoolDrillz
4. Install the required installations with the following command: sudo pip3 install -r requirements.txt
5. Create your own Mongo collection, and create your own Mongo URI**
6. in app.py, replace my Mongo URI with yours(line 13), and replace my mongo collection name with yours(line 12)
7. Save the file, and run it in the terminal with the following command: python3 app.py

Now your app is running locally

** create mongo collection:
1. Sign into [MongoDB](https://www.mongodb.com/)
2. Go to collections
3. Create database
4. Go to overview > connect > connect your application
5. copy the connection string and replace <password> with your mongo password

Now you have your own Mongo URI

### Deployment to Heroku

1. Set up an account in Heroku
2. Go to your dashboard and create a new app
3. Enter a name, this has to be a unique one in Heroku, and select your region
4. go to deploy > Manual deploy > deploy a GitHub branch
5. Select a branch to deploy and click "Deploy branch"
6. You can see the app live by clicking "view"
 
## Credits

### Content

All content and functionality in the application was written by me. 

### Media

Images were taken from Google or created by myself. I don’t own the copyright to any of the images.

### Acknowledgements

I took a navbar and footer snippet from Bootstrap and adapted it to fit the application.

I want to thanks Seun Owonikoko, my mentor, for her support and feedback. I also want to thank the tutors from Code Institute, 
especially Michael, for their help. They taught me a lot and were very patient with me.