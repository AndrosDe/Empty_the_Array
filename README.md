<h1 align="center"> Empty the Array </h1>
<h2> Welcome </h2>

<h3> 
  This is the Python-based command-line game: "Empty the Array".<br>This game is a variant of Shut the box (also called canoga, batten down the hatches or trick-track) dice game.

  [More information on the dice game here](https://en.wikipedia.org/wiki/Shut_the_box).

  The user and the programm generated opponent have each an array with numbers from 1 - 9. The game will go for 9 rounds (one round for each number) or when one of the players has an empty array.<br>The score will be calculated by the sum of each players array.<br>The player with the lowest score wins.
  
  Only up to 3 numbers can be removed in one round and all number can only be used once.
  If you use 2 or 3 numbers, with one of the numbers already being removed from the arry, the input is invalid as only number can beremoved from the array, that are still in it.
<h3>

<h2 align="center"><img src="assets/images/screenshots/readme_title_pic.jpg" height="500" width="900"></h2>

[View the live project here](https://empty-the-array.herokuapp.com/)

<hr>

<h2> Table of content </h2>

- ### [User Experience (UX)](#user-experience-ux-1)
  - [Customer Focus](#customer-focus)
  - [Design](#design)
  - [Flowchard](#flowchard)
- ### [Features](#features-1)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- ### [Technologies Used](#technologies-used-1)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- ### [Testing](#testing-1)
  - [Testing the User Experience (UX)](#user-experience-ux)
  - [Further Testing](#further-testing)
- ### [Deployment](#deployment-1)
  - [GitHub Pages](#github-pages)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)
- ### [Credits](#credits-1)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

<hr>

## User Experience (UX) 

- ### Customer Focus
  1. The player needs to be able to enter a name to have a more personolized experiance.
  2. The player needs to be able to easily read trough the rules of the game.
  3. The player needs to be shown a clear messages about the game progress and errors.
  4. The player needs to be able to get a summary of game and outcome.

- ### Design
    
  - #### Readability
    As a command-line game the only output option is text.<br>
    Hence the text must be diplayed in a readable manner, with taking care to prevent informational overload and odd spacings.

- ### Flowchard
    - Program Flowchard
    <h2 align="center"><img src="assets/images/Dice Game.png" height="300" width="700"></h2>

<hr>

## Features
- ### Existing Features
  - #### Welcome Message

  - #### Enter Name

  - #### Game Rules

  - #### Press 'Enter' to continue

  - #### Dice

  - #### Input validation

  - #### Display on Progress and vital information

  - #### Computer opponent

  - #### Score claculation

  - #### Game End Message

- ### Features Left to Implement
  - #### Start a new match

  - #### Exporting name and score

<hr>

## Technologies Used
- ### Languages Used
    - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- ### Frameworks, Libraries & Programs Used
    1. [Git](https://git-scm.com/) - Git was used for version control by utilizing the [Gitpod](https://gitpod.io/) terminal to commit to Git and Push to GitHub.
    1. [GitHub:](https://github.com/) - GitHub was used to store the code of the project after being pushed from Git.
    1. [Heroku:](https://dashboard.heroku.com/apps) - Heroku was used to deploy the project.
    1. [Lucidchart:](https://lucid.app) - Lucidchart was used to create the flowchart of the program
    1. [tinypng:](https://tinypng.com/) - Tinypng was used to reduce the file size of pictures.
    1. [Paint 3D:](https://www.microsoft.com/de-de/p/paint-3d/9nblggh5fv99?activetab=pivot:overviewtab) - Paint 3D was used to work on the pictures.
    1. [Responsinator:](http://www.responsinator.com/) - Responsinator was used to review the website on different resolutions.
    1. [Grammarly:](https://app.grammarly.com/) - Grammarly was used for spell checking.
    1. [Notepad++:](https://notepad-plus-plus.org/) - Notepad++ for keeping notes for the project.

<hr>

## Testing

The PEP8 online was used to validate the code for PEP8 requirements
    <h3><img src="assets/images/screenshots/pep8_requirements.png" height="450" width="700"></h3>

### Testing the User Experience (UX)
- Friends and family members were asked to review the site:
  - The instructions are clear.
  - The game displays the correct message.
  - The input validation works as intended.
  - The score is added correctly.

### Further Testing
-  The Website was tested on Brave, Google Chrome, Internet Explorer, Microsoft Edge, and Safari browsers.
-  The Website was viewed on Responsinator to emulate: iPhone eXpensive, Android (Pixel 2), iPhone 6-8, iPhone 6-8 Plump, iPad
-  A large amount of testing was done to ensure that all pages were linking correctly.

### Known Bugs
- The text is hard to read on mobile devices and often does not fit in the portrait mode

<hr>

## Deployment

### Heroku

The project was deployed to GitHub Pages using the following steps...

<hr>

## Credits

### Code
- The repository was created with the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template).
- The creation of the README was influenced by [Code Institute SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME) and [Jousting](https://github.com/AndrosDe/Jousting)
- The code for the while-loop validation was influenced by [Love Sandwiches](https://github.com/AndrosDe/Love-Sandwiches).
- [w3schools.com](https://www.w3schools.com/python/python_arrays.asp) helped me reviewing sample codes with array, set, tuples and opperators.


### Content
-  All English content was written by the developer.

### Media
- The pictures are in the public domain, free of use, and have been modified a lot by the developer to make them useful for this project.

### Acknowledgements
-  My Mentor Mr. Dario Carrasquel for continuous helpful feedback.
-  The [Love Sandwiches](https://github.com/AndrosDe/Love-Sandwiches) for inspiring me and allowing me to look code up