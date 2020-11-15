# How to Get Started with SchooLinky
1. Clone the repo (https://github.com/alexander-jenkins/hackumbc-2020)
2. In your terminal run ```python SchooLinky.py```
3. Navigate to ```localhost:5000```

### How do I shut the site down?
- In the press ```ctrl+c``` in the Python shell that is running the test server.

# What is SchooLinky?
![Icon](https://raw.githubusercontent.com/alexander-jenkins/SchooLinky/main/static/images/iconBigger.png)
## Inspiration
Our team was inspired by the effort that educators put into making online education a worthwhile experience for students around the world. We noticed that the software that educators are provided is not always as conducive to a seamless learning experience and has lots of potential to be improved upon.

## What it does
SchooLinky is an online learning portal which gathers the URLs, times, and names of each one of a student’s classes, then arranges them in a way which is easy to access, and provides a link in the center of the page for the next class on a student’s schedule for instant access. This saves the student time by allowing them to go straight to their class, rather than having to click through several different pages to find what they are looking for to access assignments and join video lectures.

## How we built it
SchooLinky  is built using the Python Flask web framework to dynamically load classes from the database, provide template HTML pages that we can insert code into, and handle HTML form data. The user's classes are stored in a mySQL database which is filtered by day of the week and time of day. Lastly, Javascript handles other dynamic features of the application such as the configuration menu.

## Challenges we ran into
Some challenges that we ran into included the inability to include user authentication to enable multi user support. At this point in time all classes are displayed under one person's name and multiple users will all see the same classes. Another problem that we ran into was hosting the code on a server for testing. The app's Python file must be run locally and the development server can only be accessed from the machine it is running on.

## Accomplishments that we're proud of
The most obvious accomplishment that we are proud of is bringing our concept to life, from our minds, to a conversation, then to a diagram in MS Paint, and finally to code which we can access as a web page. We are also proud of being able to use our time at hackUMBC to learn new skills, such as Flask and SQL, to create a working prototype of a program which we feel could improve the quality of life for many students like ourselves around the world in some way.

## What we learned
This project taught us the basics of the web framework Flask, which is a micro web framework which is used for rapid prototyping and simple web apps. Additionally, we learned the basics of creating and managing a mySQL database using the Python programming language.

## What's next for SchooLinky
In the future, we would like to evolve SchooLinky by implementing a web server and a custom domain so that people can access our service from anywhere. We also have many smaller ideas that we would like to implement which together could take SchooLinky from a prototype of a concept to a truly useful and unique software that people will really enjoy. A few of these features would include using a weather API to display the current weather on the homepage, utilizing a drop-down menu for the time selection page rather than radio buttons, and a form encrypted user authentication to store students’ names and class  data separately--thus allowing students to safely access separate profiles. We also see a lot of  versatility in the idea and technology behind SchooLinky, such as perhaps expanding it to encompass peoples’ hobbies, which could come in the forms of setting the links to a user’s favorite video game streamers` scheduled streams, or TV shows they like to watch online, rather than just school classes. We believe that the current version of SchooLinky that we are submitting today is only achieving a fraction of the potential that SchooLinky has long-term.
