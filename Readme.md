First Commit test# GLOW UP & SPARKLE
(Developer: Kristijan Kolar)

![Mockup image](docs/responsive.png)


[View live website](https://deploye-77587ca1458a.herokuapp.com/)

## Table of Contents
0. [About](#about)
1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
3. [Design](#design)
    1. [Colours](#colours)
    2. [Fonts](#fonts)
    3. [Project Structure](#project-structure)
    4. [Database](#database)
    5. [Data Models](#data-models)
    6. [Wireframes](#wireframes)
    7. [Agile Design](#agile-design)
4. [Technologies Used](#technologies-used)
    1. [Languages & Frameworks](#languages--frameworks)
    2. [Libraries and Tools](#libraries--tools)
5. [Features](#features)
6. [Future Features](#future-features)

7. [Validation](#validation)
    1. [CSS](#css)
    2. [Html](#html)
    3. [Javascript](#javascript)
    4. [Python](#python)
    5. [Chrome Dev Tools Lighthouse](#lighthouse)
    6. [WAVE Validation](#wave)
8. [Testing](#testing)

9. [Bugs](#bugs)

10. [Deployment](#deployment)
    1. [Heroku](#heroku)
    2. [Forking GitHub Repo](#forking-the-github-repository)
    3. [Clone a GitHub Repo](#clone-a-github-repository)
12. [Credits](#credits)
    1. [Code](#code)
    2. [Tutorials](#tutorials)
    3. [Imagery](#imagery)
13. [Acknowledgements](#acknowledgements)

## About

Glow up & sparkle is a Django full stack e-commerce app for purposes of Project Portfolio 5 with Code Institute. Glow up & sparkle is a fictional e-commerce site which provides car enthusiasts with a selection of Car care products and accessories for different vehicles. 
***
## Project Goals

- To offer users purchase of products listed on a web-store.
- To allow site owner to add, edit and remove products.
- To give users a great user experience while visiting a web-store.
- To give users option to contact site owner as a guest or registered user.
- To allow user creating or updating an account.
- To give users option to check the order history.
- To give users option to signup for newsletter.

### User Goals

- View and search for products.
- Filter products based on criteria.
- Register and log into/out of an account.
- View and edit account profile.
- Add products to the shopping bag and make purchases.
- View order history.
- Contact the site owner or customer support.
- Sign up for a newsletter.


## Business Model
***

Glow up & sparkle project was developed out of want to help passionate car lover community to easily find new and cheap car care products and in future the cars as well.

- Value Proposition:
    - Offer a curated selection of most popular Car care products and accessories.
    - Make car care products more accessible to a broader range of customers who love their car and like to take good care of it.

- Target market:
    - Car enthusiasts of all ages.
    - Individuals seeking high-quality services for personal use or gifts.

- Customer Relationships:
    - Engage with customers through social media, email newsletters, and personalized communications to foster brand loyalty.
    -  Encourage customer feedback to continuously improve the product selection and overall shopping experience.

- Communication channels:
    - E-commerce website: Provide a user-friendly online platform where customers can browse, select, and purchase car accessories and products.
    - Social media platforms: Utilize platform as Facebook to engage with the audience, and drive traffic to the web-shop.

### SEO

![SEO keywords HTML](docs/SEO.png)


### Marketing

#### Facebook business page
- To assist with marketing the website and further boost its visibility, I have included a link to the web-shop's own Facebook Business Page in the footer section. This reciprocal link establishes a connection between the website and its social media presence, allowing visitors to easily access the Facebook page for additional updates, promotions, and engagement with the brand.

![Facebook business1](docs/facebook.png)


### Target audience

- Car enthusiasts.
- Individuals seeking popular and quality car care products and accessories for personal use or gifts.


##### Back to [top](#table-of-contents)

## User Experience

##### Back to [top](#table-of-contents)

### User stories

## Registered User

1. As a registered user, I want to be able to login or logout so that I can access my account information
2. As a registered user, I want to be able to receive an email confirmation after registering so that I can verify my account
3. As a registered user, I want to be able to have a personalized user profile so that I can view my personal order history and other info
4. As a registered user, I want to be able to to save my payment information so that I can my future purchases are faster
5. As a registered user, I want to be able to edit my profile info so that I can update my profile
6. As a registered user, I want to be able to delete my profile so that my profile does not exist on site anymore
7. As a registered user I want to filter products by category or price.

## Site Owner 

1. As a site owner, I want to be able to add a product so that I can add new items to my store
2. As a site owner, I want to be able to edit/update a product so that I can change prices, description, image and other
3. As a site owner, I want to be able to delete a product so that I can remove items that are no longer available
4. As a site owner, I want to be able to edit/remove reviews so that I can manage content on my web site.
5. As a site owner, I want to be notified if any new order is placed by any customer.


## Design
***
### Colours
In this project colour pallete is very simple. Creating a visually appealing and user-friendly experience. The use of dark background picture, black coloured footer and header with white text and elements provide a perfect balance showcasing the products effectively and providing an enjoyable browsing experience.

![Colour pallete](docs/colour_pallete.png)

### Fonts

- For this Project "Times New Roman', Times, serif" font-family was used from default fonts

##### Back to [top](#table-of-contents)

## Database
***

### Data Models

#### ER Diagram

![ER Diagram ](docs/schema.png)

#### User model

- User model as part of the Django allauth library contains basic information about authenticated user and contains following fields:
username, password, email

#### Category Model
The Category model is defined with the following field:
 
| Name  | Field Type  | Validation    |
| ----- | ----------- | ------------- |
| name  | CharField   | max_length=50  |

#### Contact message Model
The contact message model is defined with the following field:

| Name       | Field Type    | Validation          |
| ---------- | ------------- | -------------------- |
| first_name | CharField     | max_length=100       |
| last_name  | CharField     | max_length=100       |
| email      | EmailField    |                      |
| subject    | CharField     | max_length=200       |
| message    | TextField     |                      |

#### Customer Model
The customer model is defined with the following field:

| Name       | Field Type    | Validation          |
| ---------- | ------------- | -------------------- |
| first_name | CharField     | max_length=50        |
| last_name  | CharField     | max_length=50        |
| phone      | CharField     | max_length=15        |
| email      | EmailField    |                      |
| password   | CharField     | max_length=100       |

#### Subscriber Model
The subscriber model is defined with the following field:

| Name  | Field Type  | Validation          |
| ----- | ----------- | -------------------- |
| email | EmailField  | unique=True          |

#### Order Model
The order model is defined with the following field:

| Name      | Field Type         | Validation                              |
| --------- | ------------------ | --------------------------------------- |
| product   | ForeignKey(Products)| on_delete=models.CASCADE                |
| customer  | ForeignKey(Customer)| on_delete=models.CASCADE                |
| quantity  | IntegerField       | default=1                               |
| price     | IntegerField       |                                         |
| address   | CharField          | max_length=50, default='', blank=True   |
| phone     | CharField          | max_length=50, default='', blank=True   |
| date      | DateField           | default=datetime.datetime.today        |
| status    | BooleanField       | default=False                           |

#### Products Model
The Products model is defined with the following field:

| Name         | Field Type        | Validation                                          |
| ------------ | ----------------- | --------------------------------------------------- |
| name         | CharField         | max_length=60                                       |
| price        | IntegerField      | default=0                                           |
| category     | ForeignKey(Category)| on_delete=models.CASCADE, default=1                |
| description  | CharField         | max_length=250, default='', blank=True, null=True  |
| image        | ImageField        | upload_to='uploads/products/'                       |



### Wireframes

- Wireframe pro was used for creating wirefrimes. During the development style and inital idea slightly changed to accomodate better user experience and design.

#### Homepage

![Homepage](docs/webUI.png)
![Homepage](docs/mobileUI.png)

#### Product Details

![Product Details](docs/WebproductUI.png)
![Product Details](docs/mobileProductui.png)


## Technologies Used

### Languages & Frameworks

- HTML5
- CSS3
- JavaScript
- jQuery
- Python 3.11.6
- Django 5.0


### Libraries & Tools


- [Bootstrap 5.1](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer, Modal, Navbar)
- [AWS (Amazon Web Services)](https://aws.amazon.com/) was utilized in this project for hosting image files. An S3 bucket on AWS was created to store and serve the project's images, providing a reliable and scalable solution for managing and delivering the visual assets. With AWS, the project benefits from secure and efficient storage capabilities, ensuring seamless access to images throughout the application.
- [Stripe](https://stripe.com/) Stripe is integrated into the project to handle payment processing. It provides a secure and convenient way to handle online payments, including credit card transactions.
- [Wireframepro](https://balsamiq.com/) to create the projects wireframes
- [Am I Responsive](http://ami.responsivedesign.is/) was used for creating the multi-device mock-up at the top of this README.md file
- [dbdiagram.io](https://dbdiagram.io/home) for creating Entity relationship diagrams(ERD) of my project database
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Boostrap icons](https://fontawesome.com/) - Icons from Bootstrap icons  were used throughout the site
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/) - for typography in project
- [Unspalsh](https://unsplash.com/)
- [Pexel](https://www.pexels.com/)
- [Lucidcharts](https://lucid.app/) 


##### Back to [top](#table-of-contents)
## Validation
***

### CSS

- [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)was used  to validate the css in the project

#### Style.css

![style css](docs/stylecssTest.png)

### Html

-  [WC3 Validator](https://validator.w3.org/) was used for the validation of projects html code

#### Index

![Index html](docs/indexTest.png)


#### About

![about html](docs/aboutTest.png)


#### Base

![base details html](docs/baseTest.png)


#### Cancel

![cancel html](docs/cancelTest.png)


#### Cart

![cart html](docs/cartTest.png)


#### Checkout

![checkout html](docs/checkoutTest.png)


#### Contact

![contact html](docs/contactTest.png)

#### Footer

![footer html](docs/footerTest.png)

#### Login

![login html](docs/loginTest.png)

#### Navbar

![navbar html](docs/navbarTest.png)

#### News Letter Sub

![news letter sub html](docs/newslettersubTest.png)

#### Order details

![order details html](docs/orderdetailsTest.png)

#### Orders

![orders html](docs/ordersTest.png)

#### Privacy policy

![privacy policy html](docs/privacypolicyTest.png)

#### Product details

![product details html](docs/productdetailsTest.png)

#### Response

![response html](docs/responseTest.png)

#### SignUp

![SignUp html](docs/signupTest.png)

#### Store

![store html](docs/storeTest.png)

#### Success

![success html](docs/successTest.png)


### Javascript

### Python


## Deployment

- During the initial phases of development, Glow up & sparkle was deployed on Heroku. To avoid any potential deployment issues near the app's release, I made sure that the database and static files were accessible right from the start of the project.

###  Creating Database ==> ElephantSQL
1. To generate a managed PostgreSQL database, please proceed to [ElephantSQL](https://customer.elephantsql.com/) and either sign up or sign in to your account. Once you've logged in, click on the 'Create New Instance' button.


2. Name your database and select the 'Tiny Turtle' payment plan. Then, click on 'Select Region'

3. Select your preferred region and create the database instance.
    After creating the instance, navigate to the instances page and click on the name of the database you selected earlier. Then, in the details section on the following page, copy the PostgreSQL URL.

### Heroku Deployment

- Before deploying to Heroku there are a few things to have ready
ElephantSQL Database url, SECRET_KEY variable(generate key different from provided one), CLOUDINARY_URL variable(after logging in the Cloudinary website copy the 'cloudinary url' from your account dashboard as the value of a variable )
- Create env.py (at the root level of your project) This file contains the above mentioned
variables in a form of:
- os.environ['DATABASE_URL'] = 'value of ElephantSQL Database url'

- os.environ['SECRET_KEY'] = 'value of secret key'
    secret key could be generated [here](https://miniwebtool.com/django-secret-key-generator/)

-  os.environ['CLOUDINARY_URL'] = 'value of 'cloudinary url' from your  
   account dashboard'
   cloudinary url can be found [here](https://console.cloudinary.com/)

1. First, sign up or sign in to your Heroku account. Next, create a new app from the Heroku dashboard.

2. Choose a unique name for your app and enter the region.Then, click on the 
    'Create App' button.
    Once your app has been created, select the 'Settings' tab from the dashboard and navigate to 'Reveal Config Vars'. From there, paste the: 
    - ElephantSQL Database URL into the DATABASE_URL environment variable.
    - SECRET_KEY variable  into the SECRET_KEY environment variable.
    - CLOUDINARY_URL variable  into the CLOUDINARY_URL environment variable.
    - add DISABLE_COLLECTSTATIC variablewith value of 1 (for initial deployment, later this variable can be removed)
    - add variable named PORT with value of 8000


3. Select Deploy option from the 'tabs'

4. From Deployment method section choose Connect to GitHub and click on it

5. Find your github repository by name and connect

6. At the bottom of the page choose either automatic deployment manual 
   deployment(deploy by branch)

7. Click on the option you want, and you should be able to see the boiler process.
    and after a while, your app should be deployed.


### Forking the GitHub Repository

1. Login or Signup to [Github](https://github.com/)
2. Navigate to  the GitHub repository link  https://github.com/Chris4891/CI-PP5-GlowUpAndSparkle.git
2. Click on the Fork button in the top right corner
4. Copy of the repository will be in your own GitHub account.


### Clone a GitHub Repo

1. Go to the GitHub repository  https://github.com/Chris4891/CI-PP5-GlowUpAndSparkle.git
2. Locate the Code button above the list of files (next to 'Add file') and click it


3. choose a preferred cloning option by selecting either HTTPS or GitHub CLI.
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Contents](#table-of-contents)


## Credits


### Code

- [Glassmorphism](https://hype4.academy/tools/glassmorphism-generator) 
- [Stack Overflow](https://stackoverflow.com/)
- Code Institute Walkthrough Projects


### Tutorials

   - [Codemy.com](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
   - Code Institute Walkthrough Projects

## Acknowledgements

- Thanks to my girlfriend, family and friends for support
- Thanks to Code Institute and fellow students on Slack channels


[Back to Table Of Contents](#table-of-contents)
