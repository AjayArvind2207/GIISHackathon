# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Inspiration](#inspiration)
  - [What it does](#what-it-does)
  - [Key Features](#key-features)
  - [How we built it](#how-we-built-it)
  - [Challenges we ran into](#challenges-we-ran-into)
  - [Accomplishments that we're proud of](#accomplishments-that-were-proud-of)
  - [What's next for ReformBar](#whats-next-for-reformbar)


## Inspiration
The subject of drinking and driving always seems to be a hot subject. Whether it’s hearing about a recent accident on the news, seeing a billboard about lawyers that specialize in DUI Cases, or maybe knowing someone that passed away in a DUI incident. Also drinking in excess leads to inflammatory damage, Alcohol poisoning, Miscarriage and stillbirth, High blood pressure, mental health problems, etc.
Excessive alcohol use is responsible for more than 95,000 deaths in the United States each year, or 261 deaths per day. These deaths shorten the lives of those who die by an average of almost 29 years, for a total of 2.8 million years of potential life lost.
It is also surprising how common banes like underage drinking, binge drinking, and heavy alcohol use are which all affect the lives and health of millions.
This has to change and to do this we need to reform the way bars work. Here is where Reformbar comes into play.

## What it does

The customers get a QR code which is printed onto a band when they first sign up for the program.
Each time they enter a bar, they scan this QR code and the bars get updated about their information, like whether they are above the legal drinking age, as well as their gender, weight, and payment method (which are all confirmed at the time of registration and updated periodically and dynamically).
When the customers want to order a drink, they scan the QR code on their wristbands or mobile phones, which add the drink they ordered to their tab and update the approximated biometrics (We predict their BAC using mathematical models).

They can't buy drinks from the QR code once their drinking limit is reached or they run out of money. Furthermore, if the customer does not adhere to the policies of the bars, by either misbehaving or creating a nuisance, the bar can update their QR code with this information so subsequently, each time that customer visits the bar, the bar would get to know of these misdemeanors and can refuse to offer drinks.

This will restrict problems like overdrinking, underage drinking, etc to a great extent and will help reduce the burden on health care systems.

## Key Features

Reformbar contains 3 main applications which are interconnected. Firstly, we have created a QR-code-based client-side application based on a custom-made QR code recognition software written in Python. This app serves as the main UI/UX for the user and gives important information about the user, including their prescribed blood alcohol levels, their drinking habits, as well as their tabs. We have also incorporated a decentralized blockchain system so as to privatize the information of the individual

Our second app is a digital menu-card payment system. The app uses predictive analysis to determine the change in blood alcohol content after a drink. Upon placing an order, The customer scans his QR code and the transaction goes through based on a review of their age, monetary balance, predicted Blood Alcohol Levels, and even past misbehavior in bars.

Subsequently, An email confirmation of the order is sent to the user. The information from the order is dynamically updated on the FireBase database. Hence, the system forms an autonomous and contactless form of payment

To counter the crippling problem of alcohol addiction, we have crafted up an emailing system to send emails when a person is drinking irresponsibly, and allocate them to a de-addiction counselor upon their request

We have also made it so that the database is reset periodically, so as to reset their blood alcohol levels when the effects of the drinking phase-out.

Our third app involves a management system for each of the bars.
The management system serves as a platform for the bars to review the information of all the customers and ensure that each customer is adhering to the norms and regulations. This also provides an incentive for the bars to take up this software, as it acts as a centralized management system of the customers and ensures that no misuse of alcohol takes place

We have made an additional fourth page for individuals to review their alcohol usage, their predicted blood alcohol levels, as well as their personal information such as their height, weight, gender, or name.

## How we built it
Our frontend was built in html and css and we formed our backend in python using Flask. We served all our web pages dynamically using Flask and then integrated Firebase and general code logic by designing an API (Flask-CORS) and then querying it from our javascript using ajax.

Per page:
QR code scanner: scans the qr codes using javascript and then sends the recognised text to our python api along with the url which it was initiated from. The python api then runs the logic of whether the order will be successful or not and returns the answer.

Bar: We associated each drink with a document in our firebase database and when you click on the drinks they go to a dynamic url from where the qr code scanner is initiated. The python api gets the price and the alcohol content in the drink by using the id passed on by the QR code scanner page and then searching the firebase database.

Profile: The profile works by first reading the qr code of a person which returns the unique id of that individual. That unique id is then used to redirect to a dynamic url where the profile page of that individual is served. The data for the page is received by querying the firebase database for the id which the url had. (done through flask)

Management: We read the firebase document which contains all the users and then pass it off to a webpage as an iterable (list of dictionaries). Then jinja 2 loops are used to iterate over that iterable and display all the users.

## Challenges we ran into

We ran into many challenges while making this project. Firstly, we faced issues with our teammates backing out, which caused us to remain without a proper front-end developer. In addition, we had to learn more about several languaging structures like jQuery, firebase, and heroku, which took large amounts of effort. We also faced some difficulty with the QR code recognition system. However, through all these shortfalls, we are proud of being able to finish ReformBar
##What we learned

Technology Segment:

1. How to transfer data to and from javascript and python

2. How to use Jquery and Ajax (This was our first time using it)

3. Making and reading QR codes in Python

4. Use of Firebase in Python

Social Segment:

1. We learnt how to be adaptable and change our skillsets when we lacked a front end developer

2. We learnt the art of cooperative working, which assisted in just two of us finishing this gargantuan task in just a day

3. We learnt that optimism is a strong driving force towards motivation and kept us encouraged throughout the hackathon

## Accomplishments that we're proud of

1. Coming up with a finished and fully functional project

2. Completing all the tasks that we thought of for this idea

3. Maintaining “good coding” practices even in a time-constrained environment

4. Being able to deploy the code so that it is usable by others

## What's next for ReformBar
Planning to add banking APIs to make the contactless payment more secure

We would also like to scale this product further. Currently, our product is scaled at a small collection of bars. We would like it to become a standard for all the bars in the country. Our use of a dynamically updating database like FireBase is our first step working towards scalability, we wish to continue on this path.

In addition, we would like to incorporate a medical support functionality, where doctors may be asked to assist if extreme blood alcohol levels are detected in a person, which could lead to severe health ailments like liver diseases, heart diseases, and stroke; this early detection could save millions of lives
