# PS_Library

## Approach
Having minimal experience developing web applications in the past I took this chance as an oppourtunity to learn
a new framework and expose myself do different technologies. I chose to focus on the functionality of the build over the presentation as a result of this, using some bootstrap4 to handle most styling. 

Work flow involved initial research into how I would develop the application. With Python being my language of choice when at home, Django looked the most suitable framework. Looking into the framework in more detail, it appeared to have a lot of the desired functions I was looking for, alongside some significant benefits. These would include, SQLite, authentication and models, giving me prebuilt features and simplistic ways of building the deliverable. 

Github was utilised for development, splitting work into 3 smaller projects: master, User_Profile and Library. 

Master was initial set up and work, such as early html and urlpatterns being established.
User_Profile handled modelling for a user, creating the forms to handle the the user actions, alongside necessary html and urlpatterns.

Library controlled the modelling for the games and the links to the users profile. ClassViews took over the early functional views made in master, making greater usage of the django libraries available. Conditionals were introduced to limit what was available for one user to view, putting the focus on their own libraries. 

## Deliverable
The delivered solution sets out to meet the requirements given. 
It functionally enables a user to create and maintain their own game library, with the data being handled through SQLite.
The users themselves are able to create their own profile which owns the associated library, with django enabling authentification and validation to be done automatically within the necessary proccesses.
### Footage
Please follow this link to access the screenshots and video demo: https://drive.google.com/drive/folders/1lQezvg0QVy-YVJ2qkjH3XOVydIEOQ0qb?usp=sharing


## Further Work
Improvements are always possible and this project is no different. There are known bugs within, such as the release date being in the required format YYYY-MM-DD, or the game updates not giving the option to update box art. 

Aside from these, work the UI would greatly upgrade the users experience when using the websites.
This can include, but not limited to: 
* New colour scheme
* Improved UX, such as messages to make some functionality more obvious to users
* Further Playstation branding

The current iteration of the project leaves space for this growth and such improvements to be incorporated over time. 
