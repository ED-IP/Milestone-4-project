<h1 align="center">The SCP Archives Book Store</h1>

The objective of this page is to promote a new book series based on the [SCP Universe](https://scp-wiki.wikidot.com/) and allow/accept direct sells for new releases.
Also there will be information about future publications.


## User Experience (UX)

-   ### User stories

    -   #### Users

        1. As a User, I want to be able to buy book
        2. As a User, I want to the book to be send to the address I indicate
        3. As a User, I want to be able to have a history of my purchase
	
    -   #### Owner

        1. As the Owner, I want that only registered user can buy using the page
        2. As the Owner, I want the user to be able to maintain up to date information for their shipments


-   ### Design


    -   #### Colour Scheme
        -   
    -   #### Typography
        -   
    -   #### Imagery
        -   

*   ### Wireframes

    
## Features

### Existing Features

- __Register User page__

    - In this section of the web an anonymous user can register to be able to do purchases
    - The user have to provide a username, e-mail and a password
    
- __Log In page__

    - In the Log In area the user have to provide a valid (already registered) Username and Password
    - Link to recover password    
    

- __User Profile__

    - Previous orders history
    - Possibility of update user details

       
- __Product Detail__

    - It's possible to add to bag the product
    - Open the image of the product in a dedicated tab



### Features to add

- __Log In page__

    - There is a link to the Register page in case that the user wants to register.

- __Product Detail__

    - Functional Wishlist
    
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

-   #### User Goals

    
-   #### Owner Goals

    
### Further Testing (not tested yet)

- [W3C Validation tools](https://validator.w3.org/)
   - All the HTML files were tested with the W3C validator, some html errors were found and fixed.
   - Still there are errors that I think are related to the Jinja templates

- [CSS Validator](https://jigsaw.w3.org/css-validator/)
   - Style.css was tested with the css validator, no error was found

- [JSHint](https://jshint.com/)
   - script.js was tested with JSHint no warnings were given


### Known Bugs

- ~~Images are not working once the project is deployed to Heroku, I suspect is a problem with the paths and the configuration for Whitenoise~~
- ~~Sometimes is not posible to click in the options for the dropdown menu "My account" when a logged user is in the home page (I suspect is because a toast is an "invisible" on top of the menu option)~~
- Sorting by name not working
- Stripe Webhooks not working on Heroku (500 error is visible in stripe website)
- "Order Total" doesn't appear in order history
- Navigation option to the Introduction section need adjustment
- Wishlist function not finalized

### To do

- Change the typografy for the main heading in the Introduction section
- Add a link to Register user in the Login user section
- Adjust the animation for the SlideShow in the intro section


## Deployment

### GitHub Pages

### Heroku

These are the steps followed to deploy the proyect on Heroku

1. Create a requierements.txt, in Gitpod terminal:
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

6. In the Resources tab add the Heroku Postgres addon

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
        DATABASE_URL | This field should be created automatically by Heroku when you install the Postgress addon
        DISABLE_COLLECTSTATIC | 1
        
    
    - Note: The values used in the project are not present here as they include passwords and user

8. Go to the Deployment tab and in the Deployment Method section choose GitHub
    - In the connect to GitHub choose the correct repository and click connect
        
9. In the section Manual Deploys choose the branch to deploy (for this project was "main") and click Deploy Branch
    - As a side note I used Manual Deploys over Automatic to avoid reaching the Heroku limit.

10. After the building phase it should be deployed. You can open the app by clicking on the "View" button under Manual Deploys or on the Open App button at the top of the page

11. Remove "DISABLE_COLLECTSTATIC" from your Config Vars

12. Deploy again the project, it should connect to Amazon web services and copy the static files to your bucket

11. The project is deployed at the following address:


## Credits

### Code

- Tutorial about SlideShows, feautured in the home page(https://www.w3schools.com/howto/howto_js_slideshow.asp)
- Tutorials about the use of [Whitenoise](http://whitenoise.evans.io/en/stable/index.html) to serve static files with heroku
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