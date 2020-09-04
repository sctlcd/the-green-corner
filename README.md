# [The Green Corner](https://the-green-corner.herokuapp.com/)

<img src="https://github.com/sctlcd/the-green-corner/blob/master/wireframes/multi_device_website_mockups-min.png" alt="The Green Corner" width="700">
<dl>
<dd>Hey! Are you a plant lover?</dd>
<dd>and/or do you want to become the <strong>Christopher Columbus of plants</strong>?</dd>
<dd>Here you go! [The Green Corner](https://the-green-corner.herokuapp.com/)</dd>
<dt>A modern responsive Web tool for gathering plant specifications and identifying flora worldwide</dt><br>

---

# Table of Contents <a name="TableOfContents"></a>

1. [About](#About)
	- [Why this project?](#WhyThisProject)

1. [UX](#UX)

	- [User Stories](#UserStories)
	- [Design](#Design)
		- [Framework](#Framework)
		- [Color Scheme](#ColorScheme)
		- [Icons](#Icons)
		- [Typography](#Typography)
	- [Wireframes](#Wireframes)
	- [Data Integration](#Dataintegration)

2. [Features](#Features)

	- [Existing Features](#ExistingFeatures)
		- [Navigation bar](#Navigationbar)
		- [Footer](#Footer)
		- [Homepage](#Homepage)
		- [Base template](#Basetemplate)
		- [Plants page](#Plantspage)
		- [Add plant page](#Addplantpage)
		- [Edit plant page](#Editplantpage)
		- [Delete plant modal](#Deleteplantmodal)
		- [Add category page](#Addcategorypage)
		- [Edit category page](#Editcategorypage)
		- [Delete category modal](#Deletecategorymodal)
		- [No result found page](#Noresultfoundpage)
		- [404 error page](#404errorpage)
		- [Defensive features](#Defensivefeatures)
	- [Features Left to Implement](#FeaturesLeftToImplement)

3. [Technologies Used](#TechnologiesUsed)

	- [Front-End Technologies](#Front-end-technologies)
  - [Back-End Technologies](#Back-end-technologies)

4. [Testing](#Testing)

  - [User story validation](#UserStoryValidation)
	- [Layout responsiveness](#LayoutResponsiveness)
	- [Compatibility](#Compatibility)
	- [Testing left](#Testingleft)
	- [Validators](#Validators)
	- [Known Issues](#KnownIssues)

5. [Deployment](#Deployment)

	- [Deployment – Live website](#Deploymentlivewebsite)
	- [Deployment – Run locally](#Deploymentrunlocally)

6. [Credits](#Credits)

	- [Content](#Content)
	- [Media](#Media)
	- [Code](#Code)
	- [Acknowledgements](#Acknowledgements)

---

## About <a name="About"></a>

The general purpose of **[The Green Corner](https://the-green-corner.herokuapp.com/)** is gathering plant specifications and identifying flora across the globe. And this anytime, anywhere as this application is available on various devices as desktops, tablets and mobile.

I've decided to create a modern responsive Web tool for gathering plant specifications and identifying flora worldwide. Because I enjoy gardening and I look for information about plants depending on the season (planting, growth, potting, care, trimming, cutting, etc. ) which are located in different places (saved online, written in books/magazines, saved in a folder on my computer, etc.).<br />
This was the good opportunity to finally have a single application to gather all my botanic experiences and knowledge centralized in one site. A few friends and family members like plants as well and we like sharing information. With this app I can easily provide all my plant information from only one location and <em>My Green Corner</em> can easily be shared.<br />
In a future version of this app the users will have the possibility to authenticate so it will allow others to store their own plant information, <em>their own Green Corner</em> while having access to all plant data shared.

Back to [top](#TableOfContents)

---

### Why this project? <a name="WhyThisProject"></a>

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, the **Data Centric Development** module. The objective of this milestone project is building a full-stack site that allows your users to manage a common dataset about a particular domain using CRUD operations: **C**reate, **R**ead, **U**pdate, **D**elete the selected dataset.

For this project we could choose from one of the following ideas:
- Bring your own idea(s) to life, based on providing value to users to address a specific real or imagined need.
- Create an online cookbook
- Create a jargon glossary/dictionary for a particular domain
- Build a book review and recommendation site

My modern responsive Web tool for gathering plant specifications and identifying flora worldwide is built using HTML, CSS, Materialize CSS, JavaScript, jQuery, Flask, Jinja, Python and MongoDB.

Back to [top](#TableOfContents)

---

## UX  <a name="UX"></a>

### User Stories <a name="UserStories"></a>

"***As a user, I want to _____***"

- [x] *View* the site from any devices (mobile, tablet, desktop)
- [x] *View* the presentation home page
- [x] *View* all the plants
- [x] *Add* a plant
- [x] *Edit* a plant
- [x] *Delete* a plant
- [x] *View* all the categories
- [x] *Add* a category
- [x] *Edit* a category
- [x] *Delete* a category
- [x] *Search* by scientific name, common name, category
- [x] *View* a specific message if no search result found
- [x] *View* a error page if the page doesn't exist

<br>
- [x] *marked the item as implemented successfully*
<br>

Back to [top](#TableOfContents)

---

### Design <a name="Design"></a>

Ideas which pop up in my mind when people talk about **botanic** and
**gardening** are a calm and relaxing atmosphere, a sober and simple design, Green color obviously but not only, natural colors as well.    
This is why I have designed my entire project around **natural and sober colors** representing the **elements of Nature**.  

I choose first the website logo representing the idea of **identifying flora worldwide**. Then I selected the palette by using the color scheme generator from a photo of the website logo, named [Coolors.co](https://coolors.co/image-picker).<br />
From my opinion ( I might be wrong :) ) the logo, the colors, the pictures - the visual design of the website in general - are what people memorize first and it's what people will remember over time. It gives them a first impression and a first feeling. If the global visual design of the website looks and feels good - if the user like it - he/she will give the application a try. If not they are lot of chances he/she will probably look for another application among the numerous applications available on the market. So visual design and feeling is a significant aspect I believe.    

I used the [Parallax Template](https://materializecss.com/getting-started.html) from Materialize CSS which I customized in my vision of the concept of the **elements of Nature**. This template was a good base to the sober and simple design I wanted to create.  

Back to [top](#TableOfContents)

---

#### Framework <a name="Framework"></a>

- [Materialize CSS 0.100.2](https://materializecss.com/) - Responsive front-end framework based on Material Design
- [Flask 1.1.2](https://palletsprojects.com/p/flask/) - Lightweight (micro) framework for building web applications

Back to [top](#TableOfContents)

---

#### Color Scheme <a name="ColorScheme"></a>

In keeping with the **the elements of Nature** idea, I have chosen a natural and sober color scheme referring to the elements of Nature. I first choose my [logo](https://www.flaticon.com/free-icon/planet-earth_1598196?term=plant&page=1&position=41) from Flaticon(https://www.flaticon.com). From there, I used the color scheme generator [Coolors.co](https://coolors.co/image-picker) which generated the following [palette](https://coolors.co/98cae9-1c5925-31628b-3caf4e-000000) from my logo picture. And finally I selected pictures which fit well in my color scheme and in the space allocated.

- ![#98CAE9](https://placehold.it/15/98CAE9/98CAE9) `#98CAE9`- Light Cornflower Blue
- ![#1c5925](https://placehold.it/15/98CAE9/98CAE9) `#1c5925`- Lincoln Green
- ![#31628b](https://placehold.it/15/98CAE9/98CAE9) `#31628b`- Lapis Lazuli
- ![#3caf4e](https://placehold.it/15/3caf4e/3caf4e) `#3caf4e`- Green Pantone
- ![#000000](https://placehold.it/15/3caf4e/3caf4e) `#000000`- Black
- ![#fafafa](https://placehold.it/15/fafafa/fafafa) `#fafafa`
- ![#444](https://placehold.it/15/444/444) `#444`
- ![#3997e5](https://placehold.it/15/3997e5/3997e5) `#3997e5`
- ![rgba(0, 0, 0, 0.05)](https://placehold.it/15/0000000/000000) `rgba(0, 0, 0, 0.05)`
- ![rgba(0, 0, 0, 0.2)](https://placehold.it/15/0000000/000000) `rgba(0, 0, 0, 0.2)`
- ![rgba(0, 0, 0, 0.87)](https://placehold.it/15/0000000/000000) `rgba(0, 0, 0, 0.87)`

Back to [top](#TableOfContents)

---

#### Icons <a name="Icons"></a>

- [Font Awesome 5.14.0](https://fontawesome.com/)
 - It fits my needs for this project in complementary with Material Design icons
- [Material Design](https://material.io/resources/icons/?style=baseline)
  - It fits my needs for this project in complementary with Font Awesome icons

Back to [top](#TableOfContents)

---

#### Typography <a name="Typography"></a>

- I have decided to use the Google Font [B612](https://fonts.google.com/specimen/B612?query=B612) throughout the website. And I have imported the Google Font [Amatic SC](https://fonts.google.com/specimen/Amatic+SC?query=Amatic) as a secondary font for the 404 error page. Both fonts are easy to read.

Back to [top](#TableOfContents)

---

### Wireframes <a name="Wireframes"></a>

I have used [Balsamiq Wireframes](https://balsamiq.com/wireframes/) for my wireframes because:
- Code Institute have provided all students a free licence until end of 2020. I got to use this software a few year ago and I am pretty happy to get the chance to use it again.
- The simplicity, rapidity and ease of use by focusing on structure and content.

My wireframes for this project can be found [here](https://github.com/sctlcd/the-green-corner/tree/master/wireframes) in the wireframes sub-directory.

Back to [top](#TableOfContents)

---

### Data integration <a name="Dataintegration"></a>

I decided to use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for my project in case the website gets a big amount of data in the future. I also wanted the user to be able to choose what data they gather in the plant form. I believe MongoDB offers more flexibility concerning my website in the long run.
Moreover before this project I've never used MongoDB so it was the opportunity to get new knowledge and learning a new technology.

Back to [top](#TableOfContents)

---

## Features <a name="Features"></a>

### Existing Features <a name="ExistingFeatures"></a>

#####  Navigation bar <a name="Navigationbar"></a>

- The navigation menu is fixed on the top thus facilitating the access of the navigation from anywhere on the website without having to scroll.
- Clicking on the logo link reloads the Home page.
- Two dropdown menu items displaying 2 sub-menu items which are linked to the relevant page allowing the user to navigate smoothly between pages.
- Search bar allowing the user to search a plant by scientific name, common name and category. If the search field is empty or there are no search results matching with the search entry a message is shown letting the user know they are no results found.
- In mobile view the navigation bar is collapsed allowing the users more space on the screen. The users can click on the collapsed menu icon and still receive the full menu as a drop down function.
- On mobile view the side bar menu displays a background image with the logo in foreground, a search bar and the two dropdown menu items I mentioned above.

##### Footer <a name="Footer"></a>

- The footer contains a Company bio description, a Contact section with Github and Twitter icon links opening in a browser new tab, a Support description with a button redirecting to the [Patreon](https://www.patreon.com/europe) website (as no Patreon account has been created yet for this projet) in a browser new tab, a Contact description and a button redirecting to the [Gitter](https://gitter.im/) website (as no Gitter room has been created yet for this projet) in a browser new tab.
- A copyright mention is displayed with my name beside a GitHub icon link which opens my [Github](https://github.com/sctlcd) home page in a new browser tab.

Back to [top](#TableOfContents)

---

##### [Homepage](https://github.com/sctlcd/the-green-corner/blob/master/templates/home.html) <a name="Homepage"></a>

- This is an introduction page presenting the project and the application.
- A title section with the short description of the Website and a button "Get started", redirecting to the Plants page.  
- A section displaying the main motivations and benefits of the website
- A section displaying a Contact description and a button redirecting to the [Gitter](https://gitter.im/) website (as no Gitter account has been yet created for this project) in a browser new tab.

##### [Base template] <a name="Basetemplate"></a>

- A title section with the short description of the Website on the top of the page
- A content section which loads all the various pages I am going to detail below.
- A section with the short description of the Website at the bottom of the page are common elements of all pages.


##### [Plants page](https://github.com/sctlcd/the-green-corner/blob/master/templates/plants.html) <a name="Plantspage"></a>

- View all plant records. Scientific names and common names are displayed.
- Collapsible menu with all the plant fields organized in sections: Identity, Category, Botanic, Culture, Note.
- Delete and Edit buttons  

Back to [top](#TableOfContents)

---

##### [Add plant page](https://github.com/sctlcd/the-green-corner/blob/master/templates/addplant.html) <a name="Addplantpage"></a>

- Access to this page by clicking on the Plants dropdown and then on the sub-menu item "Add Plant"
- A form for adding a plant is displayed organized by sections, Identity, Category, Botanic, Culture, Note, with the relevant fields.
- Add plant and cancel buttons. Add plant button triggers the creation of the plant record in the database.

##### [Edit plant page](https://github.com/sctlcd/the-green-corner/blob/master/templates/editplant.html) <a name="Editplantpage"></a>

- Access to this page by clicking on the Edit button of the selected plant in the Plants page.
- A form for editing a plant is displayed organized by sections, Identity, Category, Botanic, Culture, Note, with the relevant fields.
- Edit plant and cancel buttons. Edit plant button triggers the update of the plant record in the database

Back to [top](#TableOfContents)

---

##### [Delete plant modal](https://github.com/sctlcd/the-green-corner/blob/master/templates/plants.html) <a name="Deleteplantmodal"></a>

- Access to this modal by clicking on the Delete button of the selected plant in the Plants page.
- The modal displays a delete confirmation message and two buttons. Yes triggers the suppression of the plant record in the database. No redirects the user to the Plants page.

##### [Categories page](https://github.com/sctlcd/the-green-corner/blob/master/templates/categories.html) <a name="Categoriespage"></a>

- View all category records. Category name is shown.
- Delete and Edit buttons  

##### [Add category page](https://github.com/sctlcd/the-green-corner/blob/master/templates/addcategory.html) <a name="Addcategorypage"></a>

- Access to this page by clicking on the Categories dropdown and then on the sub-menu item "Add Category"
- A form for adding a category is displayed
- Add plant and cancel buttons. Add plant button triggers the creation of the plant record in the database.

Back to [top](#TableOfContents)

---

##### [Edit category page](https://github.com/sctlcd/the-green-corner/blob/master/templates/editcategory.html) <a name="Editcategorypage"></a>

- Access to this page by clicking on the Edit button of the selected category in the Categories page.
- A form for editing a category is displayed
- Edit category and cancel buttons. Edit plant button triggers the update of the plant record in the database

##### [Delete category modal](https://github.com/sctlcd/the-green-corner/blob/master/templates/categories.html) <a name="Deletecategorymodal"></a>

- Access to this modal by clicking on the Delete button of the selected category in the Categories page.
- The modal displays a delete confirmation message and two buttons. Yes triggers the suppression of the category record in the database. No redirects the user to the Categories page.

##### [No result found page](https://github.com/sctlcd/the-green-corner/blob/master/templates/noresultsfound.html) <a name="Noresultfoundpage"></a>

- Message letting know the user No result have been found matching with his/her search.
- Link redirecting to Homepage.

Back to [top](#TableOfContents)

---

##### [404 error page](https://github.com/sctlcd/the-green-corner/blob/master/templates/404errorpage.html) <a name="404errorpage"></a>

- Humoristic picture and message letting know the user the page does not exist.
- Link redirecting to Homepage.

##### [Defensive features] <a name="Defensivefeatures"></a>

- All plants and categories fields throughout the various pages (View/Add/Edit/Delete pages) are mandatory except the *note* field. If the field is empty when submitting a message is display letting know the user the field has to be filled.
- If the search field is empty or there are no search results matching with the search entry a message is shown letting the user know they are no results found.
- If the page doesn't exit the 404 error page is displayed informing the user.  

Back to [top](#TableOfContents)

---

### Features Left to Implement <a name="FeaturesLeftToImplement"></a>

 - A "profile photo" of the plants to be displayed in the Plants list page.
 - User can upload photos of plants for making the identification easier.
 - User authentication

Back to [top](#TableOfContents)

---

## Technologies Used <a name="TechnologiesUsed"></a>

- [GitHub](https://github.com/) - Used as remote storage of my code online.
- [Atom](https://atom.io/) - Used as a local IDE.
- [Compressjpeg](https://compressjpeg.com/) - Used to compress images for loading faster
- [Techsini](https://techsini.com/multi-mockup/) - Used to generate multi-device website mockup

Back to [top](#TableOfContents)

---

##### Front-End Technologies <a name="Front-end-technologies"></a>

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [Materialize CS 0.100.2](https://materializecss.com/) - Used as responsive front-end framework, based on Material Design.
- [JavaScript](https://www.javascript.com/) - Used for user interactions.
- [jQuery 3.5.1](https://jquery.com/) - JavaScript library, used to simplify some of the DOM manipulations.

Back to [top](#TableOfContents)

---

##### Back-End Technologies <a name="Back-end-technologies"></a>

- Flask
	- [Flask 1.1.2](https://palletsprojects.com/p/flask/) - Used as a Lightweight (micro) framework for building web applications.
	- [Jinja 2.11.2](https://jinja.palletsprojects.com/en/2.10.x/) - Used for templating with Flask.

- Heroku
	- [Heroku](https://www.heroku.com/) - Used for app hosting.

- Python
	- [Python 3.8](https://www.python.org/) - Used as the back-end programming language.
	- [MongoDB Atlas]((https://www.mongodb.com/) - Used to store a document oriented database in the 'cloud'.
	- [PyMongo 3.10.1](https://pymongo.readthedocs.io/en/stable/) - Used as the Python API for MongoDB.

Back to [top](#TableOfContents)

---

## Testing <a name="Testing"></a>

My testing coverage for this project can be found [here](TO_ADD) in the testing sub-directory or below.

### User story validation <a name="UserStoryValidation"></a>

|  | Galaxy S5 | Pixel | Pixel 2 XL |iPhone 6/7/8 | iPhone 6/7/8 Plus | iPhone X | iPad | iPad Pro | Desktop 1024px | Desktop >1200px |
| :--- | :--- | :---| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
View the site from any devices (mobile, tablet, desktop)|  |  |  |  |  |  |  |  |  |  |  |
View the presentation home page|  |  |  |  |  |  |  |  |  |  |  |
View all the plants|  |  |  |  |  |  |  |  |  |  |  |
Add a plant|  |  |  |  |  |  |  |  |  |  |  |
Edit a plant|  |  |  |  |  |  |  |  |  |  |  |
Delete a plant|  |  |  |  |  |  |  |  |  |  |  |
View all the categories|  |  |  |  |  |  |  |  |  |  |  |
Add a category|  |  |  |  |  |  |  |  |  |  |  |
Edit a category|  |  |  |  |  |  |  |  |  |  |  |
Delete a category|  |  |  |  |  |  |  |  |  |  |  |
Search by scientific name, common name, category|  |  |  |  |  |  |  |  |  |  |  |
View a specific message if no search result found|  |  |  |  |  |  |  |  |  |  |  |
View a error page if the page doesn't exist|  |  |  |  |  |  |  |  |  |  |  |

Back to [top](#TableOfContents)

---

### Layout responsiveness <a name="LayoutResponsiveness"></a>

|  | Galaxy S5 | Pixel | Pixel 2 XL |iPhone 6/7/8 | iPhone 6/7/8 Plus | iPhone X | iPad | iPad Pro | Desktop 1024px | Desktop >1200px |
| :--- | :--- | :---| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| website is responsive < 767 px | Good | Good | Good | Good | Good | Good | n/a | n/a | n/a | n/a |
| website is responsive > 768 px | n/a | n/a | n/a | n/a | n/a | n/a | Good | Good | Good | Good |
|**home.html** |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| plants.html |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| addplant.html |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| editplant.html |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| categories.html |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| addcategory.html |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| editcategory.html |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| noresultsfound.html |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| plantsearchresults.html |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| 404errorpage.html |
| Navigation bar: logo / buttons / links / search | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Content page: Images / text / links / buttons | Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good |  | Good |

Back to [top](#TableOfContents)

---

### Compatibility <a name="Compatibility"></a>

I tested the website across the 6 main browsers in both desktop and mobile configuration to ensure a large number of users can use it successfully.

- Chrome v.84.0
- Edge v.85.0
- Firefox v.80.0
- Safari v.5.1.7 for Windows 10
- Opera v.70.0
- Internet Explorer v.11

|All pages | Chrome | Edge | Firefox | Safari | Opera | IE |
| :--- | :--- | :---| :--- | :--- | :--- | :--- |
| Expected appearance | Good | Fair | Good | Poor | Good | Poor |
| Expected responsiveness | Good | Good | Good | Poor | Good | Poor |

- IE: Some CSS3 properties and HTML5 elements are not fully supported

- Safari v.5.1.7: It’s an outdated version and lacks many of the features present in the latest version of Safari. The last version of Safari for Windows was released on May 9, 2012.

Back to [top](#TableOfContents)

---

### Testing left <a name="Testingleft"></a>

- There is no way to install the latest version of the Safari browser on Windows 10 as Apple stopped developing Safari for Windows operating system long ago.
For testing this website on the latest version of Safari, I will have to install the newest version of macOS on Windows 10 in a virtual machine.

Back to [top](#TableOfContents)

---

### Validators <a name="Validators"></a>

**HTML**
- [W3C HTML Validator](https://validator.w3.org/)
    - Jinja template syntax not understood. Relative errors shows : `{{ variables }}`, `{% for %} {% endfor %}`, etc.
		- No errors for the remaining code

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
	- No errors

**Javascript**
- [Javascript Validator](https://jshint.com/)
	- No errors

**Chrome DevTools**
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)
	- Console Navigating through the Website rendered no critical fails/errors in the console that were necessary to fix.

**Python**
- [Python validator](https://pythonbuddy.com/)
    - TO_ADD !!to_fix!!

Back to [top](#TableOfContents)

---

### Known Issues <a name="KnownIssues"></a>

TO_ADD

Back to [top](#TableOfContents)

---

## Deployment <a name="Deployment"></a>

### Deployment – Live Website <a name="Deploymentlivewebsite"></a>

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`
    - My file can be found [here](https://github.com/sctlcd/the-green-corner/blob/master/requirements.txt).
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python run.py > Procfile`
    - My file can be found [here](https://github.com/sctlcd/the-green-corner/blob/master/Procfile).
3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **PORT** : `5000`
    - **MONGO_URI** : `<link to your Mongo DB>`
5. Your app should be successfully deployed to Heroku at this point.

### Deployment – Run Locally <a name="Deploymentrunlocally"></a>

Please note - in order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- Any IDE.
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [MongoDB](https://www.mongodb.com) to develop your own database either locally or remotely on MongoDB Atlas.

Next, there's a series of steps to take in order to proceed with local deployment:

- Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (remember to unzip it first), or by entering the following into the Git CLI terminal:
    - `git clone TO_ADD`.
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- Create a `.env` file with your credentials. An example can be found [here](https://github.com/bravoalpha79/environment-variables#how-to-set-up-python-environment-variables-in-gitpod). Be sure to include your *MONGO_URI*
- Install all requirements from the [requirements.txt](TO_ADD) file using this command:
    - `sudo -H pip3 -r requirements.txt`
- Sign up for a free account on [MongoDB](https://www.mongodb.com) and create a new Database called **the_green_corner**. The *Collections* in that database should be as follows:  
	- [database documentation](TO_ADD) in the database sub-directory
	- [database diagram](https://app.quickdatabasediagrams.com/#/d/sYgu2Z) or [here](TO_ADD) in the database sub-directory


**plants**
```
_id PK int
scientific_name string
common_name string
genus string
species string
family string
category string FK >- categories.category_name
plant_type string FK >- plant_types.plant_type_name
shade_tolerance string FK >- shade_tolerance.shade_tolerance_name
note NULL string
```

**categories**
```
_id PK int
category_name string
```

**plant_types** as pt
```
_id PK int
plant_type_name string
```

**shade_tolerance** as st
```
_id PK int
shade_tolerance_name string
```

- You should now be able to launch your app using the following command in your terminal:
    - `python app.py`
- The app should now be running on *localhost* on an address similar to `http://127.0.0.1:5000`. Simply copy/paste this into the browser of your choice!

Back to [top](#TableOfContents)

---

## Credits <a name="Credits"></a>

- My inspiration comes from
	- [Pl@ntNet](https://plantnet.org), the "Shazam" of Botanic, allowing you to identify plants that you photograph during your country walks.  
	- [Aujardin](https://www.aujardin.info/), a site dedicated to gardening with advices on plant cultivation, maintenance and development of gardens, vegetable gardens, orchards,...
	- [Garden.com](https://garden.org/), a website for learning how to garden and grow plants successfully.
  - [Better home & garden](https://www.bhg.com/gardening/plant-dictionary/), inspiring ideas for gardening,...
  - [Garden.ie](https://www.garden.ie), a website which offers accurate horticultural advices.
	- [Bored panda - creative 404 error pages](https://www.boredpanda.com/50-cool-and-creative-404-error-pages/?utm_source=google&utm_medium=organic&utm_campaign=organic) for the [404 error page](https://github.com/sctlcd/the-green-corner/blob/master/templates/errors/404errorpage.html)

Back to [top](#TableOfContents)

---

### Content <a name="Content"></a>

- [Aujardin](https://www.aujardin.info/), a site dedicated to gardening with advices on plant cultivation, maintenance and development of gardens, vegetable gardens, orchards,...
- [Garden.com](https://garden.org/), a website for learning how to garden and grow plants successfully.

Back to [top](#TableOfContents)

---

### Media <a name="Media"></a>

Sources of the images used on this site:

- From images sub-directory - [Github](https://github.com/sctlcd/the-green-corner/tree/master/static/assets/images)
	- [garden-min](https://www.pexels.com/photo/bloom-blooming-country-countryside-145685/) - [Pexel](https://www.pexels.com/) | copyright [Mike](https://www.pexels.com/@mikebirdy)
	- [gooseberry-min](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=176450) - [Pixabay](https://pixabay.com/) | copyright [GLady](https://pixabay.com/users/glady-768/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=176450)
	- [leaves-min](https://pixabay.com/fr/photos/feuilles-%C3%A9t%C3%A9-vert-%C3%A9rable-saison-291024/) - [Pixabay](https://pixabay.com/) | copyright [Gregovish](https://pixabay.com/fr/users/gregovish-195074/)
	- [lemon-min](https://pixabay.com/fr/photos/citron-citronnier-arbre-fruit-852244/) - [Pixabay](https://pixabay.com/) | copyright [GregMontani](https://pixabay.com/fr/users/gregmontani-1014946/)
	- [meadow-min](https://www.pexels.com/photo/flowers-summer-meadow-wild-flowers-51548/) - [Pexel](https://www.pexels.com/) | copyright [Freddie Ramm](https://www.pexels.com/@freddie-ramm-6839)
	- [wild-flowers-min](https://pixabay.com/fr/photos/fleurs-sauvages-fleurs-plante-macro-571940/) - [Pixabay](https://pixabay.com/) | copyright [DreamyArt](https://pixabay.com/fr/users/dreamyart-512893/)
	- [the_green_corner_logo-min](https://www.flaticon.com/free-icon/planet-earth_1598196?term=earth&page=1&position=47) - [Flaticon](www.flaticon.com) | copyright [Free](https://www.flaticon.com/authors/freepik)  
	- [search-min](https://www.flaticon.com/free-icon/loupe_882988?term=magnifying%20glass&page=1&position=12) - [Flaticon](www.flaticon.com) | copyright [Free](https://www.flaticon.com/authors/freepik)
	- [humour404error](https://www.pinterest.ie/pin/226587424989226051/ ) - [Pinterest](https://www.pinterest.com/) | copyright [Joe Dunaway](http://www.modelzone.com/mangrasshopper/)
	- [favicon](https://www.flaticon.com/free-icon/planet-earth_1598196?term=earth&page=1&position=47) - [Flaticon](www.flaticon.com) | copyright [Free](https://www.flaticon.com/authors/freepik)

Back to [top](#TableOfContents)

---

### Code <a name="Code"></a>

- Parallax Template - [Materialize CSS](https://materializecss.com/)
- Parallax Materialize CSS - [Materialize CSS parallax](http://archives.materializecss.com/0.100.2/parallax.html)
- Flask 1.1 documentation - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- Jinja 2.11 documentation - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- MongoDB Atlas 3.10 documentation - [MongoDB Atlas](https://docs.atlas.mongodb.com/)
- Readme file information - [Tim Nelson](https://github.com/TravelTimN) Software Developer and Tutor at [Code Institute](http://codeinstitute.net)
- Environment variables - [Igor Basuga](https://github.com/bravoalpha79) Tutor at [Code Institute](http://codeinstitute.net)
- Environment variables - Code Institute archive resources

Back to [top](#TableOfContents)

---

### Acknowledgements <a name="Acknowledgements"></a>

- [Anthony Ngene](https://github.com/tonymontaro)
	- Thanks to my Code Institute mentor for his time, suggestions, and constructive feedback

Back to [top](#TableOfContents)

---
