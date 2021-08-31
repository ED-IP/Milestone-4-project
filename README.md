<h1 align="center">The SCP Archives Book Store</h1>

The objective of this page is to promote a new book series based on the [SCP Universe](https://scp-wiki.wikidot.com/) and allow/accept direct sells for the book.
The home page include a short introduction to the current release products, the shop for the books and a link to the official SCP site.

## Features

### Existing Features

- __Navigation Menu__

    - Responsive Navigation menu, it's available on top of the page on all section of the web

- __Register User page__

    - In this section of the web an anonymous user can register to be able to do purchases
    - The user have to provide an username, e-mail and a password
    
- __Log In page__

    - In the Log In area the user have to provide a valid (already registered) Username and Password
    - Link to recover password    
    
- __User Profile__

    - Previous orders history
    - Possibility of update user details
    - Contact form to ask question to site staff
       
- __Product Detail__

    - It's possible to add the product to the bag
    - A button to return to main store
    - Open the image of the product in a dedicated tab


### Features to add

- __Log In page__

    - A link to the Register page in case that the user wants to register.

- __Product Detail__

    - Functional Wishlist


## User Experience (UX)

-   ### User stories

    -   #### Users

        1. As a User, I want to be able to buy book        
        2. As a User, I want to have a history of my previous orders
        3. As a user, I want to be able to update my address and other personal data
        4. As a User, I want to be able to contact with the staff/owner of the site        
	
    -   #### Owner

        1. As the Owner, I want the user to be able to maintain up to date shipping information
        2. As the Owner, I want the user to be able to register in the website


-   ### Design


    -   #### Colour Scheme
        -   
    -   #### Typography
        -   
    -   #### Imagery
        -   The kind of images I want for the site are those related to the nature of the SCP universe, supernatural themes, conspirations etc...

*   ### Wireframes    
   
## Technologies Used

### Languages

- **[HTML]**
	- **HTML** is used to create the structure of the web-page.

- **[JS]**
    - **JavaScript**

- **[Bootstrap](https://getbootstrap.com/)**
    - **Bootstrap** is used to provide css style and some JavaScript content.

- **[Font Awesome](https://fontawesome.com/)**
	- The website use several symbols from **Font Awesome** service.


### Frameworks, Libraries & Programs

- **[Django](https://www.djangoproject.com/)**

- **[Stripe](https://stripe.com/)**

- ~~**[Whitenoise](http://whitenoise.evans.io/en/stable/index.html)** not in use anymore~~
	

## Testing


### Testing User Stories from User Experience (UX) Section

The following test have been done on a Windows machine with the following browser:
- Brave Browser Version 1.28.106 Chromium: 92.0.4515.159 (Official Build) (64-bit) Windows
- Firefox 91.0.2 (64-bit) Windows

The mobile version of the web has been tested with the developers tools for the previously listed desktop Browsers

-   #### User Goals

    1. As a User, I want to be able to buy book:
        - Tested with an already created user, the order appears in the user profile and it's register in the orders table in the database.
        
    2. As a User, I want to have a history of my previous orders:
        - A list of previous orders is visible in the user profile section of the web

    3. As a user, I want to be able to update my address and other personal data:
        - Tested to be able to provide updated shipping information, it's possible to do it when the shipping information is provided

    4. As a User, I want to be able to contact with the staff/owner of the site:
        - Tested with an already created user, the data provided in the contact form is successfully recorded in the contact form table in the database
    
-   #### Owner Goals    
    
    1. As the Owner, I want the user to be able to update their information:
        - Test User stories number 4 proves that the users can update their information if it's needed.

    2. As the Owner, I want the user to be able to register in the website:
        - Tested creating several test user, seems that the user is correctly registered.

    
### Further Testing

- [W3C Validation tools](https://validator.w3.org/)
   - All the HTML files were tested with the W3C validator, some html errors were found and fixed.
   - Still there are errors that I think are related to the Jinja templates

- [CSS Validator](https://jigsaw.w3.org/css-validator/)
   - Base.css was tested with the css validator, no error was found

- [JSHint](https://jshint.com/)
   - slideShow.js was tested with JSHint a warning in line 11 is noticed, consulting the code with the one in W3School doesn't suggest anything wrong


### Known Bugs

- ~~Images are not working once the project is deployed to Heroku, I suspect is a problem with the paths and the configuration for Whitenoise~~
- ~~Sometimes is not possible to click in the options for the drop-down menu "My account" when a logged user is in the home page (I suspect is because a toast is an "invisible" on top of the menu option)~~
- Sorting by name not working
- Stripe Webhooks not working on Heroku (error 500 is visible in stripe website)
- "Order Total" doesn't appear in order history, it's not correctly recorded in the orders table for some orders
- Navigation options for the home page need adjustment, specially for the mobile site
- Wishlist function not finalized
- ~~It's not possible to click the logout/login, the inspect tools shows the body element on top of some of the buttons, fields not allowing interaction~~

### To do

- Change the typography for the main heading in the Introduction section to one more interesting
- In the mobile version the login, logout section need to be move down so the top navigation bar doesn't overlap some elements.
- Adjust the animation for the SlideShow in the intro section
- ~~Remove the "Home" option from the mobile navigation menu~~


## Deployment

### Heroku

These are the steps followed to deploy the project on Heroku

1. Create a requirements.txt, in Gitpod terminal:
    - pip3 freeze --local > requirements.txt
    
2. Create a Procfile, in Gitpod terminal:
    - echo web: python app.py > Procfile
    - open the Procfile and check that there is no trailing lines after the text

3. Add and push the files to GitHub:
    - git add requirements.txt
    - git add Procfile
    - git commit -m ""
    - git push

4. On the Heroku Dashboard click in the New button and choose "New App"

5. Choose a name and a region (for this project I used Europe) and click create

6. In the Resources tab add the Heroku Postgres add-on

7. Once the app is created click on the settings tab, and then click on "Reveal config Vars" button.
    - Add the following key, values pairs
        
        KEY | VALUES
        --------------|--------------
        AWS_ACCESS_KEY_ID | your aws_access key
        AWS_SECRET_ACCESS_KEY | your aws_secret_key
        SECRET_KEY | your django secret_key
        STRIPE_PUBLIC_KEY | your stripe public_key
        STRIPE_SECRET_KEY | your stripe secret_key
        STRIPE_WH_SECRET | your strike webhook_key
        USE_AWS | True
        DATABASE_URL | This field should be created automatically by Heroku when you install the Postgress add-on
        DISABLE_COLLECTSTATIC | 1
        
    
    - Note: The values used in the project are not present here as they include passwords and user

8. Go to the Deployment tab and in the Deployment Method section choose GitHub
    - In the connect to GitHub choose the correct repository and click connect
        
9. In the section Manual Deploys choose the branch to deploy (for this project was "main") and click Deploy Branch
    - As a side note I used Manual Deploys over Automatic to avoid reaching the Heroku limit.

10. After the building phase it should be deployed. You can open the app by clicking on the "View" button under Manual Deploys or on the Open App button at the top of the page

11. Remove "DISABLE_COLLECTSTATIC" from your Config Vars

12. Deploy again the project, it should connect to Amazon web services and copy the static files to your bucket

13. To login as superuser visit: "site address"/admin/


## Credits

### Special thanks

I would like to start by especially thanking my mentor and my brother for the extra time and patience they had trying to help me with this project.

Without their help I would not have been able to have reached this point in the project.

I also want to thank the tutors for their support to solve the problems that I have been encountering while trying to finish this.


### Code

- This project uses some of the code from the boutique-ado mini project from the course
- Tutorial about SlideShows, featured in the home page(https://www.w3schools.com/howto/howto_js_slideshow.asp)
- Tutorials about the use of [Whitenoise](http://whitenoise.evans.io/en/stable/index.html) to serve static files with Heroku
    - https://devcenter.heroku.com/articles/django-assets
    - https://dev.to/developerroad/tutorial-deploying-a-django-app-on-heroku-4k6o
    - http://whitenoise.evans.io/en/stable/django.html#

### Content

- Information about the SCP universe was found in the [SCP Wiki](https://scp-wiki.wikidot.com/)

### Media

- Control Videogame Wallpapers (Used in the intro section):
    (https://wall.alphacoders.com/big.php?i=1079669/)
    (https://wall.alphacoders.com/big.php?i=1037069)


- [Man Wearing Black Vest Near Crowded People](https://www.pexels.com/photo/man-wearing-black-vest-near-crowded-people-2348817/) by Aloïs Moubax

- [Empty white book on wooden table](https://www.pexels.com/photo/empty-white-book-on-wooden-table-6373289/) by Monstera, used as template for the book images in product section

- S.C.P. Foundation Logo from [Wikipedia](https://en.wikipedia.org/wiki/SCP_Foundation#/media/File:SCP_Foundation_(emblem).svg)

- G.O.C. Logo from [SCP Foundation Wiki](https://scp-wiki.wikidot.com/goc-hub-page)

### Acknowledgements

The following discussions/articles/tutorials were consulted to solve issues or add featured to the project during the development

- https://www.w3schools.com/howto/howto_js_slideshow.asp
- https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid
- https://learndjango.com/tutorials/django-email-contact-form
- https://getbootstrap.com/docs/4.0/utilities/spacing/
- https://getbootstrap.com/docs/4.0/utilities/text/#text-alignment
- https://getbootstrap.com/docs/4.0/layout/grid/#horizontal-alignment
- https://stackoverflow.com/questions/12615154/how-to-get-the-currently-logged-in-users-user-id-in-django
- https://www.youtube.com/watch?v=CVEKe39VFu8