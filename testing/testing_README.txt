# Testing <a name="Testing"></a>

## User story validation

|  | Galaxy S5 | Pixel | Pixel 2 XL |iPhone 6/7/8 | iPhone 6/7/8 Plus | iPhone X | iPad | iPad Pro | Desktop 1024px | Desktop >1200px |
| :--- | :--- | :---| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
View the site from any devices (mobile, tablet, desktop)| Pass | - | Pass | - | Pass | - | Pass | - | Pass | - | Pass |
View the presentation home page| Pass | - | - | - | - | - | - | - | - | - | |
View all the plants|  | Pass | - | - | - | - | - | - | - | - | - |
Add a plant| - | - | Pass | - | - | - | - | - | - | - | - |
Edit a plant| - | - | - | Pass | - | - | - | - | - | - | - |
Delete a plant| - | - | - | - | Pass | - | - | - | - | - | - |
View all the categories| - | - | - | - | - | Pass | - | - | - | - | - |
Add a category| - | - | - | - | - | - | Pass | - | - | - | - |
Edit a category| - | - | - | - | - | - | - | Pass | - | - | - |
Delete a category| - | - | - | - | - | - | - | - | Pass | - | - |
Search by scientific name, common name, category| - | - | - | - | - | - | - | - | - | Fail | - |
View a specific message if no search result found| Pass | - | - | - | - | - | - | - | - | - | Pass |
View a error page if the page doesn't exist| - | Pass | - | - | - | - | - | - | - | - | - |


| User Stories - As a user, I want to... | Steps | Expected outcome | Actual outcome |
| :--- | :--- | :---| :---|
| View the site from any devices (mobile, tablet, desktop) | - | The website should be responsible and displayed correctly | as expected |
| View all the plants | Click on Plants menu then View plant or on "Get started" button from the home page, the list of plants should be displayed | Each plant should have a collapsible menu containing fields organized by section (Identity, Category, Botanic, Culture, Note) and modify and delete buttons | as expected |
| Add a plant | Click on Plants menu then Add Plant sub-menu, fill all the fields and submit | The plant should be added in the Plants page and in the database | as expected |
| Edit a plant | Click on Edit button for the chosen plant in the Plants page, update fields and submit | The plant should be updated in the Plants page and in the database | as expected |
| Delete a plant | Click on Delete button for the chosen plant in the Plants page. A confirmation modal should pop up with yes and no buttons. Agree | The plant should be updated in the Plants page and in the database | as expected |
| View all the categories | Click on Categories menu then View category | The list of categories should be displayed and modify and delete buttons in the Categories page | as expected |
| Add a category | Click on Categories menu then Add category sub-menu, fill all the fields and submit | The category should be added in the Categories page and in the database | as expected |
| Edit a category | Click on Edit button for the chosen category in the Categories page, update fields and submit | The category should be updated in the Categories page and in the database | as expected |
| Delete a category | Click on Delete button for the chosen category in the Categories page. A confirmation modal should pop up. Agree | The category should be updated in the Categories page and in the database | as expected |
| Search by scientific name, common name, category | Enter a scientific plant name (or part of it) and submit. Redo this test case with a common plant name and a plant category (or part of it) | The result of the search should be displayed in the Plants page | as expected |
| View a specific message if no search result found | Enter a search which does not exist | The No results found page should be displayed (example: *aaaaa* ) | not as expected |
| View a error page if the page doesn't exist | Enter an URL which does not exist | The 404 error page should be displayed (example: *https://the-green-corner.herokuapp.com/get_plants/bb* ) | as expected |


## Layout responsiveness

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
| Footer: text / links / buttons| Good | Good | Good  | Good | Good | Good | Good | Good | Good | Good |


## Compatibility

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
