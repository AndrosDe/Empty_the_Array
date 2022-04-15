<h1 align="center"> Empty the Array </h1>
<h2> Welcome </h2>

<h4> 
  This is the Python-based command-line game: "Empty the Array".<br>This game is a variant of Shut the box (also called canoga, batten down the hatches or trick-track) dice game.

  [More information on the dice game here](https://en.wikipedia.org/wiki/Shut_the_box).

  The user and the programm generated opponent have each an array with numbers from 1 - 9. The game will go for 9 rounds (one round for each number) or when one of the players has an empty array.<br>The score will be calculated by the sum of each players array.<br>The player with the lowest score wins.
  
  Only up to 3 numbers can be removed in one round and all number can only be used once.
  If you use 2 or 3 numbers, with one of the numbers already being removed from the arry, the input is invalid as only number can beremoved from the array, that are still in it.
<h4>

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
  - [Known Bugs](#known-bugs)
  - [Fixed Bugs](#fixed-bugs)
- ### [Deployment](#deployment-1)
  - [Heroku](#heroku)
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
    A frindly message and some ASCII art to state the name of the game and give a preview that it must be a game about tiles numbered from 1 to 9 and dice rolls.
    <h3><img src="assets/images/screenshots/screenshot_welcome.png" height="300" width="500"></h3>

  - #### Enter Name
    The input request for the players name. This input value will be later on used in the program to highlight user actions or output related to the user.<br>This input request has no validation, as the user is free to choose whatever name the user wants to use.
    <h3><img src="assets/images/screenshots/screenshot_name.png" height="40" width="500"></h3>

  - #### Start-Up
    The start-up has an input request where the player can select to read about the game ruels and understand how to play the game or to start playing the game right away but typing "game" or "rules" and confirming with 'Enter'.
    <h3><img src="assets/images/screenshots/screenshot_startup.png" height="150" width="500"></h3>
    
  - #### Start-Up-Validation
    In order to make sure that correct input was made, the input-value will be validated.<br>Only  "game" or "rules" are valid inputs, any other input will promt an error message, requesting the correct input-value.
    <h3><img src="assets/images/screenshots/screenshot_startup_val.png" height="150" width="500"></h3>
    
  - #### Game Rules
    New users, that are unfamilier with the game, can read up how this game is played and how the winner is calculated.<br>
    Unlike most games, the player with the least amount of points wins this game.<br>
    Additionally only the added sum of the dices are important and any combination of up to three diffrent numbers,<br>that would reproduce this sum, are valid if all of these number can be removed from the arry.<br>
    For example, if the total number is "8" the player may choose any of the following sets of numbers:
    - 8
    - 7, 1
    - 6, 2
    - 5, 3
    - 5, 2, 1
    - 4, 3, 1
    
    <br>
    <h3><img src="assets/images/screenshots/screenshot_startup_rules.png" height="150" width="500"></h3>

  - #### Press 'Enter' to continue
    The input request "Press 'Enter' to continue" was implemented throughout the program in order to prevent to much text being displayed at one.<br>This way an informational overload can be avoided at the cost of the player needing to press 'Enter' every now and then.<br>This input request in not validated and will accept other input, but ignores everything save for the 'Enter' input.
    <h3><img src="assets/images/screenshots/screenshot_wall_of_text_prevention.png" height="30" width="300"></h3>

  - #### Dice
    The dice roll is simiulated with the help of the random module, randomly creating a number between 1 and 6.<br>This is called up twice and than added to gether to provide the number for the respective player.
    <h3><img src="assets/images/screenshots/screenshot_game_player.png" height="250" width="500"></h3>

  - #### Input validation
    In order to make sure that the user is providing valid input, several inputvalidations have to be made and all must be passed in order to progress in the game:
    1. **Does the user want to pass this round?**<br>If the user dicided to risk it and wait for better numbers, passing a round is an option.<br>In this case an input of 'none' is required and the user will have the next player roll the dice.<br>Additonally to 'none':<br> 'None', 'pass', 'Pass' and pressing Enter with entering no value will be valid entries to pass the turn.<br>All other input will be validated in the next step.
        <h3><img src="assets/images/screenshots/screenshot_game_val_0.png" height="110" width="450"></h3>

    1. **Is the input a or multiple number(s)?**<br>As the first validation already filtered out all valid inputs, that are not numbers, only numbers are allowed from this point onward.<br>If the input is neither a number nor one of the approved non-number values, the player will get an error message explaining that number are needed and is requested to make a different input.
        <h3><img src="assets/images/screenshots/screenshot_game_val_1.png" height="90" width="750"></h3>
    
    1. **Does the number(s) add up to be equal to the sum of both dices?**<br>In order to make sure that the correct numbers are provided, the first test is to check if it matches the sum of both dices.<br>If there is a difference, an error message will appeare stating that the numbers provided do not match the combined value of dices.<br>
    The user is than requested to make a different input.
        <h3><img src="assets/images/screenshots/screenshot_game_val_2.png" height="110" width="600"></h3>

    1. **Are the numbers different?**<br>As stated in the rules, if more than one number is used, they must be diffrerent.<br>While five + five = ten, five can only be remove from the array once.<br>Therefor this would be an invalid input.<br>For example one + nine, would be fine at this stage, as they are different numbers.<br>If one of the number in the input is the same as another, an approproate error message will be displayed and a different input is requested.
        <h3><img src="assets/images/screenshots/screenshot_game_val_3.png" height="90" width="450"></h3>

    1. **How many number are provided?**<br>As by the rules of the game only up to 3 numbers can be used per turn, it is now checked how many numbers were provided by the user.<br>If the more than 3 numbers are verified an error message state how many numbers were proved and request an new inpu of only upto 3 numbers.
        <h3><img src="assets/images/screenshots/screenshot_game_val_4.png" height="100" width="500"></h3>

    1. **Is the number still in the array?**<br>Since only numbers that are still in the array can be closed, the last validation is, after going through all other steps an making sure that normally this input should be valid and remove the number from the array, to check if the number is still in the array.<br>This is especially important by multiple numbers, since all numbers have to be able to be used.<br>If the number 1,2,5 are entered however the players array down to [1, 3, 4, 5, 7], only 1 and 5 could be used.<br>Hence a new input request would made after displaying which number was invalid.
        <h3><img src="assets/images/screenshots/screenshot_game_val_5.png" height="120" width="400"></h3>

    Indeed only after passing all validations succesfully, will the programm continue, otherwise is will request a new valid entry from the player and will go through all steps again.

  - #### Display on Progress and vital information
    In order to make sure the player gets the information that the input was correctly processed, not only will a confirmation on the numbers removed appear as an out put on the screen, also an overview of the current state of his tiles will be shown.
    <h3><img src="assets/images/screenshots/screenshot_game_player_input.png" height="120" width="500"></h3>

  - #### Computer opponent
    This game comes with an automate oppenent that will be subject to the same random dice roll function as the player and will select numbers to close according to the same rule set.<br>The only thing 'Python' will not do is to pass a trun, if 'Python' could remove a number.<br>Stratgie is not 'Python' strongest ability in this instance.
    <h3><img src="assets/images/screenshots/screenshot_game_computer.png" height="200" width="500"></h3>

  - #### Score claculation
    After the 9th round or if one of the players managed to clead out the array, all values in the array will be added together.<br>
    The player scoring the least amount of points and therefor the one that was able to not only remove the most numbers, but also most of the biggest numbers.<br>
    Removing 1,3,5 is great, however removing 9 migth be better, as you might have the chance to close more tiles if you still have some rounds left to play.
    <h3><img src="assets/images/screenshots/screenshot_game_score.png" height="160" width="400"></h3>

  - #### Game End Message
    The game concludes with a 'Thank you' mesage to the user for playing the game, signaling that the game is completed.
    <h3><img src="assets/images/screenshots/screenshot_game_end.png" height="300" width="500"></h3>

- ### Features Left to Implement
  - #### Start a new match
    The program orginally was made with the intent to allow the player to select a new match after completeing the game the first time.<br>This is why the name input is in a sperate function and called before the main / main_game function.<br>The idea was that the player could call up the main_game function without needing to enter a name again and keepting the score for the previous round.<br>
    Finishing up this programm to the current stage, exposed two issues:
    1. Nine Rounds are quite long to play.
    2. Attempts to implement this feature had the problem, that the arrays could not be overwritten with a full set of numbers.<br>
    
    It was therefore decided to leave this feature out of the programm and implement it in a later version.
    
  - #### Exporting name and score
    Another feature for a later version is to connect this program with API or database and have the results of the game exported.

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
- The panorama mode on mobile devices will half the screen blocked by the "keyboard".

### Fixed Bugs
- The computer "try and error" value removal process:<br>The program does in indeed go trough the process of trying an action and upon receiving an error, continuing with the next action until one of the actions work. The last action avalible is to print out that no action could been taken.<br>At first the program only worked with clear set up values for each number from 1 - 12. Changes were made to consolidae and shorten the program for this process, which made the computer unable to close multiple values at once.
By creating extra variable for this process that could be trusted to deliver the needed values and plitting up the "try and error" process in three parts.<br>While it is heavily nested, it does work as intended.
- Function naming:<br> Some of the function have been renamed to state more clearly what they are supposed to accomplish.<br>However there were some shortening nessceary:
  - combinations -> combi
  - validation -> val
  - number -> num<br><br>
- The player input validation:<br>
At first the player input validation had been programmed similar to the "start-up" function for the "Game Rules / Start Game"-Option early in the game.<br>While the validations were displaying the correct error messages, input correction would lead to the programm to fail.<br>Somehow the first option picked was still in place and not overwritten by restarting the input process.<br>The first attempt on fixing this problem was done by consolidating all validations in the first validation function, instead of having a function call up other function in a string of pearls like fashion. The process of the computer going through "trial and error" for emtying the array is programmed that string of pearls like way, this part of the program is working as intended. Which added more to the confusion, as some functions seem to work just fine this way anothers did not.<br>The idea behind the consolidating was that the bug was caused by having to jump back to a previous function, hence a consolidating in one function would slove that problem.<br>
Alas it did not and the complete player input validation was rewritten.<br>
In the project [Love Sandwiches](https://github.com/AndrosDe/Love-Sandwiches) a validation was implemented that did exsactly what was needed forthis project, so I reviewed that part of the programm.<br>
By carefully programming this while-loop validation, which would be running as long as the conditions inside were "True", the functions were strongly atomised. As a lot of the validations are dependent on each other a nesting of if statements was needed.<br>In order to make sure that none of the validations would change the actual input and are just returning "True" or "False", the programm has now some similar looking functions.
Some of these functions are for validating, while the others to the intended changed to the input: 
  - creating an array
  - chaning the values from strings to inegeres
  - removing the correct value from the primary array)

  <br>These changes did help solving the previous problem and also improved the player input request, as the player is no longer required to starte seperatly how many values of the array are to be removed and then to specify the values.<br>Instead the player is now asked to input the values right away and will start valadating the input.


<hr>

## Deployment

### Heroku

The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:
  
1. **Log in to Heroku** or create an account if required.
1. **click** the button labeled **New** from the dashboard in the top right corner, just below the header.
1. From the drop-down menu **select "Create new app"**.
1. **Enter a unique app name**. I used the same name as the github repsitory (empty-the-array) for this project.
1. Once the web portal shows the green tick to confirm the name is original **select the relevant region.** In my case, I chose Europe as I am in Germany.
1.  When you are happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.
1. This will bring you to the project "Deploy" tab. From here, navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
1. **Click** the button labelled **"Reveal Config Vars"** and **enter** the **"key" as port**, the **"value" as 8000** and **click** the **"add"** button.
1. Scroll down to the **buildpacks section of the settings page** and click the button labeled **" add buildpack," select "Python," and click "Save Changes"**.
1. **Repeat step 9 but** this time **add "node.js" instead of python**. 
   * ***IMPORTANT*** The buildpacks must be in the correct order. If node.js is listed first under this section, you can click on python and drag it upwards to change it to the first buildpack in the list.
1. Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
1. From the deploy tab **select Github as the deployment method**.
1. **Confirm** you that want to **connect to GitHub**.
1. **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
1. From the bottom of the deploy page **select your preferred deployment type** by follow one of the below steps:  
   * Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment. 

<hr>

## Credits

### Code
- The repository was created with the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template).
- The creation of the README was influenced by [Code Institute SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME) and [Jousting](https://github.com/AndrosDe/Jousting)
- The code for the while-loop validation was influenced by [Love Sandwiches](https://github.com/AndrosDe/Love-Sandwiches).
- Deployment to Heroku was created and 98% copied from the README of [battleships](https://github.com/dnlbowers/battleships/blob/main/README.md).
- [w3schools.com](https://www.w3schools.com/python/python_arrays.asp) helped me reviewing sample codes with array, set, tuples and opperators.

### Content
-  All English content was written by the developer.

### Media
- The pictures are in the public domain, free of use, and have been modified a lot by the developer to make them useful for this project.

### Acknowledgements
-  My Mentor Mr. Dario Carrasquel for continuous helpful feedback.
-  The [Love Sandwiches](https://github.com/AndrosDe/Love-Sandwiches) for inspiring me and allowing me to look code up.
-  dnlbowers for the "Deployment to Heroku" README - Part of [battleships](https://github.com/dnlbowers/battleships/blob/main/README.md).
- Joan G. Stark fot thr ASCII [Dice Art](https://www.asciiart.eu/miscellaneous/dice).