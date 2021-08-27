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

- ~~Sometimes is not posible to click in the options for the dropdown menu "My account" when a logged user is in the home page (I suspect is because a toast is an "invisible" on top of the menu option)~~
- Sorting by name not working

## Deployment

### GitHub Pages

### Heroku


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