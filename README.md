# PoolDrillz - A pool billiard exercises database application

**Third milestone project; Data Centric Development - Full Stack Software Developer course - Code Institute**

PoolDrillz is a C.R.U.D.(create, read, update & delete) application. Users can find exercises and make changes to them.
The user can:
- See an overview of all exercises
- Filter this overview on type of exercises
- Open each individual exercise in a page with all information
- Make changes to each exercise
- Add a new exercise
- Delete an exercsise

The idea came to me because I'm a semi professional pool player. And for pool players, there is not clear path to
becoming a better player. There are many exercises and ideas floating around, but there's no clear overview. 
My eventual goal for PoolDrillz is for it to become an online community of pool players and trainers where information
is easily accessible and pool players of each level can find the right exercises for them based on which area of their 
game they want to improve on.

![Image of PoolDrillz](/static/images/readmeimage.png)

LIVE APPLICATION (LINK)

## UX and UI

### Users

Users of the application are pool players and trainers. They can use the application to find the right exercises for them.
And to share the exercises they know with others. 

#### User stories

Before starting to build the application. I wrote user stories so I knew which features the application needed to have.

[User stories](userstories.md)

### Design

PoolDrillz is a simply designed application. The main purpose of this project was to build an application that connects to 
a database. The user can use this apllication to perform C.R.U.D. operations. 

#### Navigation

All pages of the apllication can be accessed with one click from anywhere in the application. On larger screens, the links
can be found in the navbar on top of the screen, and in the footer. On smaller screen only in the footer. I choose this 
because to have both a footer and a navbar at the top showing would take up too much screen space.

#### Color

The navigation bar and footer are dark blue (#393a4c). The add exercise button has the same color. 
The other buttons are standard blue and red from Materialize. All text on the white background is black. All other text is white. 

### Mockup

I created a mockup using [Wix](https://ivarsaris.wixsite.com/pooldrillz)

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
Another feature would be some more interesting statistics.

For other features I would like to implement, I would need a better understanding of the technology. Some features 
That I would like to add are the following:
* Allow user to create an account. In this account, the user can store exercises suitable for them.
* Password integration, so each user has a secure account.
* User can only delete an execise he or she added to the database themself, this to avoid abuse.
* A forum on which users can discuss ideas and ask questions.
* An image template, where the user can drag balls onto an empty pooltable to create an image for an exercise. 
* A high score table. Users can input their high score of an exercise, to create competition.
* Exercise review. Users can give a star rating to an exercise. The average of all ratings is displayed next to the exercise.

** Technologies used

The application has been made using the following Technologies:

* **HTML5** - Coding language used for creating the content and structure of the website
* **CSS** – Coding language used for styling the content
* **Python3** - Dynamic, object oriented programming language
* **Flask** - Open source Python framework user for building web applications
* **jQuery** - Used to simplify JavaScript for display purposes
* **Google Chrome** – Used as browser and for developer tools
* [**Materialize**](https://materializecss.com/) - Framework library used for display, styling and icons
* **Git** – Used for version control
* [**Github**](https://github.com/) – Used to host the repository for the application
* [**Heroku**](https://www.heroku.com/) - Used to deploy the application

## Testing

The application achieves the goal set out. Users can create, read, update and delete exercises from the database.
They can filter the exercises by type of exercise. The user can direct to any page of the application from anywhere 
with one click. 

### Responsiveness

I have used Chrome developer tools during the whole process of building the application. This to make sure the 
applications is responsive to all screen sizes and devices types. I have also run the application through https://responsivedesignchecker.com/
and checked many different devices. This to make sure the application looks good on all of them. I ensured the application
looks good on all deviced from 320px width(smallest mobile device) and up. I also tested the application responsiveness manually on the following devices:

**Mobile** - Honor 10, Iphone 4, 7, and 10, and Samsung galaxy s9

**Tablet** - Ipad pro

**Desktop** - Lenovo 14 inch laptop, HP 15.6 inch laptop, and a 27 inch monitor 

On some devices, the spacing between some buttons doesn't look very neat. With more time, this could easily be fixed. 
But because the main purpope of this applications is the functionality, I decided to spend my time focusing on that.

### Browser compatibility

I ran the apllication in several browsers to make sure it's compatible with the most common ones. The application runs
well in Google Chrome, Mozilla Firefox, and Safari. 

### Code validation

I ran the code through several validators to make sure there are no mistakes. The HTML validators don't take Flask into account,
so several errors were returned. But I checked them and these were not mistakes. 