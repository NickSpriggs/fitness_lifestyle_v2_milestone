# Milestone Full-Stack Framework Project

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/laptop-ipad_orig.png">

The following project was my attempt to create a fitness and nutrition website for users who are trying to get into better shape. 
Users can search through various nutrition or exercise plans and view the purchased product in their profile page in the form of an instructional
video. A standard user can register a profile, purchase and view products, and track their order history. 
The superuser can add, edit, and delete the products through the Django admin portal. This site currently makes use of HTML, CSS, Python, 
Jinja, and Javascript.

Test Standard Account -> User: guest / Pass: code-tester

SuperUser Account -> User: superuser / Pass: admin

[View live project](https://fitlyfe.herokuapp.com/)

# UX

(NEED)

## User Stories

-   #### First Time User Goals

    1. As a First Time User, I want to be able to register and make an account.
    2. As a First Time User, I'd like to be able to search the site for specific exercise programs and nutritions plans.
    3. As a First Time Superuser, I'd like to be able to easily add, edit, or delete exsisting products. 

-   #### Returning User Goals

    1. As a Returning User, I want to be able to purchase and checkout specific products and eventually view them in my profile. 
    2. As a Returning User, I'd like to be able to easily navigate the site without confusion or an extensive reintroduction. 
    3. As a Returning User, I'd like to review my previous orders and set default contact information for my account.

# Wireframes:
<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/wireframes_orig.png">

# Database Schema:
The relationship between the models can be seen below:

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/database-schema-image_orig.png">

Each user has a username and password, with a confirmation email being sent to confirm the account. When a confirmed user makes a purchase the product is put into an order and the order is then stored to a specified user account.

# Features

- Mobile, desktop, and tablet scalable.

- User can purchase video plans and view them on profile.

- Superuser can add/edit/delete products on the site or through Django. 

# Technology Used

## Languages

The following technologies have been used to achieve this project:

- HTML was used as the main writing language of this project.
- CSS was used for styling.
- JavaScript
    - Jquery is used for simplifying JavaScript.
- Jinja was utilized for templating Python in Django.

## Frameworks, Libraries, Websites & Programs Used

- [W3schools](https://www.w3schools.com/): This site provided many useful templates in their lessons.

- [Bootstrap](https://www.bootstrap.com/): Very helpful framework for figuring out initial design.

- [FontAwesome](https://fontawesome.com/): Provided icons for certain features.

- [Photoshop](https://photoshop.com/en): This was used to design the site's wireframes and database schema. 

- [FontMeme](https://www.fontmeme.com/): This was used to design the logo. 

- [Heroku](https://www.heroku.com/): Heroku was used to deploy the website.

- [Django](https://www.djangoproject.com/) is used as main web framework for the website.
    - Django Crispyforms
    - Django Allauth
    - Stripe
    - Gunicorn
    - Psycopg2
    - Django Countries
    
- [Amazon Web Services](https://aws.amazon.com/): Used to store all static files and images.

- [GitHub](https://github.com/): GitHub was used to code the program.
    - Dependencies List:
        - asgiref==3.4.1
        - boto3==1.20.42
        - botocore==1.23.42
        - dj-database-url==0.5.0
        - Django==3.2
        - django-allauth==0.41.0
        - django-countries==7.2.1
        - django-crispy-forms==1.13.0
        - django-storages==1.12.3
        - gunicorn==20.1.0
        - jmespath==0.10.0
        - oauthlib==3.1.1
        - Pillow==9.0.0
        - psycopg2-binary==2.9.3
        - python3-openid==3.2.0
        - pytz==2021.3
        - requests-oauthlib==1.3.0
        - s3transfer==0.5.0
        - sqlparse==0.4.2
        - stripe==2.64.0


# Testing
W3C Markup Validator, W3C CSS Validator, and Pep8Online were used to test the code. 

- WSC Markup - [Link to site](https://validator.w3.org/)
    - get_films.html - <a href="static/img/validation/get_films.html - Nu Html Checker.pdf"> Results PDF </a>
    - login.html - <a href="static/img/validation/login.html - Nu Html Checker.pdf"> Results PDF </a>
    - register.html - <a href="static/img/validation/register.html - Nu Html Checker.pdf"> Results PDF </a>
- W3C CSS - [Link to site](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - style.css - <a href="static/img/validation/W3C CSS Validator (CSS level 3 + SVG).pdf">Results PDF </a>
- Python - [Link to site](http://pep8online.com/)
    - app. py
        - <a href="static/img/validation/PEP8 online check - Results.pdf">Results PDF </a>
        - <a href="static/img/validation/result_20210812_193900.txt">Results TXT </a>


## Testing User Stories

-   #### First Time User Goals

    1. As a First Time User, I want to be able to register and make an account.
        - Login/Registrations tabs are visible in navigation bar on all pages and incorrect username/passwords will alert the user
        that a mistake has been made.
    3. As a First Time User, I'd like to be able to search the site for specific exercise programs and nutritions plans.
        - Site home page clearly presents links to nutrition and exercise plans.
            - The home page functions properly on all screen sizes. 
        - Search bar is available to both registered and unregistered users. 
            - Search bar functions on all screen sizes. 
    4. As a First Time Superuser, I'd like to be able to easily add, edit, or delete exsisting products.
        - Superuser is granted the ability to edit or delete products when viewing them in the product landing page
        or their specified product details page.
        - Includes feature on within member dropdown for superuser to create new products.

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/canvas_orig.png">

-   #### Returning User Goals

    1. As a Returning User, I want to be able to purchase and checkout specific products and eventually view them in my profile. 
       - All purchases are immediately stored in the user profile and available for viewing without restriction. 
    3. As a Returning User, I'd like to be able to easily navigate the site without confusion or an extensive reintroduction. 
       - Site layout is extremely simple and scales well on all devices with little to no errors. 
    4. As a Returning User, I'd like to review my previous orders and set default contact information for my account.
       - User profile has information tab dropdown which shows not only their preferred contact informatio but also
       a summary of all their prior orders. 



## Further Testing

- Tested using Chrome/Firefox/Safari.

- Tested on iPhone 7.

# Known Bugs / Potential Improvements

- Minor issue with error messages on profile page as a result of youtube links. It doesn't appear to affect the speed or functionality of the page though. 

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/fitlyfe-error_orig.png">

# Deployment 

## GitHub Cloning/Coding Environment

1. Log into GitHub.

2. Go to the project's repository.

3. To open it in GitPod simply click the green GitPod button and a new workspace will open. 

To Create your own copy:

4. On the menu bar, click "Settings" which will redirect you to a separate page.

3. Above the menu bar containing the "Settings" tab notice the three buttons to the right: "Unwatch", "Star", and "Fork".
Click the "Fork" button and refresh your browser. You will now have a copy of the repository in your own account.


## Heroku Deployment 

0. (Open project in GitHub.)

1. To deploy from Heroku first note down all neccesary dependencies the project requires to function. To do this create a requirements.txt file in the terminal with the command: pip freeze > requirements.txt

2. Create Procfile with the commmand echo web: python app.py > Procfile. This will let Heroku know it's going to run a python file. 

3. Push these files to GitHub then go to the Heroku site. 

4. Login and create a new app. 

5. Go to deploy and select github as the method. You will then be asked to link the heroku app to a repository. Select the name of project. 

6. Then go to settings > "reveal config vars" which is where you will store the environment variables which were not pushed to github.  
    - "IP": "0.0.0.0")
    - "PORT": "5000")
    - "SECRET_KEY": "mYt905thou1W")
    - "MONGO_URI": "mongodb+srv://pokemongoDB:Pikachu25@myfirstcluster.4i2hj.mongodb.net/readflix?retryWrites=true&w=majority"
    - "MONGO_DBNAME": "readflix")

7. Then go back to the deployment section of the app and click "deploy branch". 


# Credits

- Code
    - Code Institute (Boutique Ado Project)
        - The mini Boutique Ado assignment served as a helpful jumping off point for developing my code.

- Content
    - Men/Women Nutrition Videos:
        - Fit Father Project - Fitness For Busy Fathers (https://www.youtube.com/channel/UCKvJ_vxZZoN5yeWBU2CVGcQ)
        - Thomas DeLauer (https://www.youtube.com/channel/UC70SrI3VkT1MXALRtf0pcHg)
    - Strength Videos
        - Juice & Toya (https://www.youtube.com/channel/UCwrXi5ZknKThspJc-Gai04g)
    - Strength Videos
        - HASfit (https://www.youtube.com/channel/UCXIJ2-RSIGn53HA-x9RDevA)
    - Flexability Videos
        - Tom Merrick (https://www.youtube.com/channel/UCU0DZhN-8KFLYO6beSaYljg)


- Media
    - [FontMeme](https://fontmeme.com/permalink/210729/7c4f14820fc13e73ba00a7ff096daf55.png) This was used to create the site logo.
    - [Google Images](https://google.com): This was used by myself, and presumbably, the testers to find images icons for the products. 


- Acknowledgements
    - Thank you to FontMeme!
    - Thank you to Code Institute!
