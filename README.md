<h1>The Book - Online Cookbook App Milestone Project 3</h1>
<hr>

<p>This project is the culmination of the material covered in the data-centric development module from the Code Institute. Given the brief of an online cookbook app, I decided to create a website where users could view recipes from around the world and act as a recipe database, also allowing for users to add their own creations to share with others.</p>

<h2>UX </h2>
</hr>

<p>This site was designed to allow users to view, edit and add new recipes. The recipes are grouped by name. It is also possible to find recipes that exclude a specific allergen.</p>

<h4>User Stories</h4>
<ul>
    <li>As a user, I want to be able to add, edit and/or delete recipes that I have created and shared.</li>
    <li>As a user with specific dietary requirements, I want to be able to search for recipes which exclude the things I am allergic to.</li>
    <li>As an aspiring cook, I want to be able to search for recipes that require different levels of skill.</li>
    <li>As a user, I want to be able to view different recipes to get ideas for meals to cook for a party/friends/family.</li>
</ul>

<h4>Wireframes</h4>
<ol>
    <li><a href="static/images/wireframes/Wireframe_1.jpg">Wireframe 1</a></li>
    <li><a href="static/images/wireframes/Wireframe_2.jpg">Wireframe 2</a></li>
    <li><a href="static/images/wireframes/Wireframe_3.jpg">Wireframe 3</a></li>
    <li><a href="static/images/wireframes/Wireframe_4.jpg">Wireframe 4</a></li>
</ol>

<h4>Schemas</h4>
<ol>
    <li><a href="static/schema/recipe_schema.json" target="_blank">Recipe Schema</a></li>
    <li><a href="static/schema/user_schema.json" target="_blank">User Schema</a></li>
</ol>

<h3>Existing Features</h3>

<p>I decided for this project to use a NoSql database as that seemed to be the best way to handle such a large store of information and it also meant that the user wasn't having to worry about measurments for ingredients, or that they were met with lots of dropdown menus which, from personal experience, reduces enjoyment on a website and feels cumbersome.

<a href="https://www.mongodb.com/cloud/atlas" target="_blank">MongoDB Atlas</a> was used to store the database.</p>

<h4>User Login and Registration</h4>

<ul>
    <li>A user can create an account and have their own unique username. This username will be used to log in and identify a recipe belonging to that user.</li>
    <li>The Log In page is the first page all users visiting the website will see. It contains a jumbotron with some information and directions for the user.</li>
    <li>Login and/or Registration gives the user the ability to add, edit and/or delete their own recipes.</li>
    <li>If a username already exists or login information does not match the input from the user, a message will flash to alert the user to this.</li>
</ul>

<h4>Navbar</h4>

<ul>
    <li>Contains the website name that, when clicked, links to the recipes page.</li>
    <li>A user button that opens a dropdown for login/sign up when a user is not logged in, and logout when the user session is active.</li>
    <li>Add recipe button that will only appear when the user has logged in.</li>
    <li>Button that links to the recipes page.</li>
</ul>

<h4>Recipes</h4>

<ul>
    <li>Page where the user can view all the recipes available. Recipes are ordered alphabetically.</li>
    <li>Contains search forms that allow the user to search for recipes by difficulty, ingredient or exclusion of an allergen.</li>
    <li>Pagination present so the user doesn't have to constantly scroll when looking for a recipe.</li>
</ul>

<h4>Single Recipe View</h4>

<ul>
    <li>Displays a chosen recipe in more detail. Shows ingredients, cook time, instructions etc.</li>
    <li>Back button to allow the user to revisit the previous page rather than clicking on the back arrow in the browser or having to click on the recipes button and travel through the pagination to get to where they were.</li>
    <li>If the recipe was created by the user, i.e the recipe author matches the session username, buttons for editing and/or deleting the recipe will be visible.</li>
</ul>

<h4>Forms and modals</h4>

<ul>
    <li>An add recipe form to allow the user to add their own recipes to the website to share with other users.</li>
    <li>Fields where multiple lines are required have buttons to allow the user to add or remove lines for these items as they require, such as ingredients and instructions.</li>
    <li>An edit recipe form that allows the user to edit recipes that match their username if they have changes they need to make to them.</li>
    <li>Delete recipe modal that pops up when a user clicks the delete recipe button. Ensures that the user doesn't click the button by accident and has to confirm if they want the deletion to continue.</li>
    <li>When a recipe is added, edited or deleted, a message will be shown at the top of the page to which they are redirected to inform the user that the process was successful.</li>
</ul>

<h3>Features to Implement in the Future</h3>

<ul>
    <li>Profile page for the user that displays all of the recipes that they have created and/or liked.</li>
    <li>A like system that shows the popularity of recipes.</li>
    <li>A system that will allow the user to filter recipes by likes, recency, difficulty, category etc.</li>
    <li>A comment section at the bottom of a recipe's page to allow users to say whether they made a dish and how it turned out.</li>
    <li>A print button to allow users to have physical copies of recipes rather than having to write the recipe down or constantly look back to the website for confirmation.</li>
    <li>A way for users to view a collection of recipes by a specific user.</li>
</ul>

<h2>Technologies Used</h2>

<h4>HTML 5</h4>
<ul>
    <li>positioning and format of html elements.</li>
</ul>
<h4>CSS</h4>
<ul>
    <li>Styling the HTML elements</li>
</ul>
<h4>JavaScript</h4>
<ul>
    <li>Handling of add and remove buttons in add and edit forms</li>
</ul>
<h4>Python</h4>
<ul>
    <li>Implement the logic, functionality and responses of the project.</li>
</ul>
<h4>Jquery</h4>
<ul>
    <li>Handling of loader</li>
    <li>Navbar on smaller screen sizes</li>
</ul>
<h4>FontAwesome</h4>
<ul>
    <li>Used for icons used in project</li>
</ul>
<h4>Bootstrap</h4>
<ul>
    <li>Used for formatting of HTML elements</li>
</ul>
<h4>Bootswatch</h4>
<ul>
    <li>Used to get theme for project</li>
</ul>
<h4>Flask</h4>
<ul>
    <li>Used to build the app and handle python logic in html</li>
</ul>
<h4>PyMongo</h4>
<ul>
    <li>The PyMongo distribution contains tools for interacting with MongoDB database from Python</li>
</ul>

<hr>

<h2>Deployment and Testing</h2>

<h3>Deployment</h3>
<p>My project was created in a cloud9 workspace and deployed heroku and is hosted on github pages. The link to the working heroku page can be found <a href="https://the-book-4.herokuapp.com" target="_blank">here.</a>The deployment process was as follows:</p>

<h4>In the cloud9 command line I entered the following:<h4>
<ul>
    <li><code>git init</code> to start a new git repository</li>
    <li><code>pip3 freeze --local > requirements.txt</code>Creates a .txt file which tells Heroku what dependencies the project is using.</li>
    <li><code>echo web: python run.py > Procfile</code>Tells Heroku that this project is a web app and that "app.py" is going the run it.</li>
    <li><code>git add .</code> to add all changes made</li>
    <li><code>git commit -m "initial commit"</code> to create an initial commit in the github repository</li>
    <li><code>git push</code> and enter username and password to push the commit to github</li>
</ul>
<h4>In app.py in cloud9 I added the following to allow Heroku to find the variables: <h4>
<ul>
    <li><code>app.secret_key = os.environ.get('SECRET_KEY')</code></li>
    <li><code>app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")</code></li>
    <li><code>app.config["MONGO_URI"] = os.environ.get("MONGO_URI")</code></li>
</ul>
<h4>In Heroku:<h4>
<ul>
    <li>I created a new app and named it <code>the-book-4</code></li>
    <li>I then went to the settings tab and clicked on config vars and entered the following:</li>
        <ul>
            <li><code>IP = 0.0.0.0</code></li>
            <li><code>PORT = 5000</code></li>
            <li><code>SECRET_KEY = |my_secret_key|</code></li>
            <li><code>MONGO_DBNAME = |database name|</code></li>
            <li><code>MONGO_URI = |mongodb+srv://|username|:|password|@projects-fyjqy.mongodb.net/|database name|?retryWrites=true|</code></li>
            <li><code>I then connected heroku to my github repository so that every commit I made to github, heroku would automatically be updated.</code></li>
        </ul>
</ul>

<h3>Testing</h3>

<p>I tested my CSS file using the Jigsaw validator and no errors were found.</p>
<p>I checked my HTML with W3C validator. Only Jinja related errors were returned due to the validation not programmed to read them.</p>
<p>I formatted my Python code with <code>autopep8</code> and validated it with <code>flake8</code>. No errors were found.</p>
    <ul>
        <li><code>sudo pip install --upgrade autopep8</code></li>
        <li><code>autopep8 --in-place --aggressive --aggressive app.py</code></li>
        <li><code>sudo pip install flake8</code></li>
        <li><code>flake8 app.py</code></li>
    <ul>
<p>I tested the app at different screen resolutions and across different browsers. The app was fully responsive and there were no evident bugs.</p>

<h2>Credits and Acknowledgements</h2>

<p>First and foremost, thanks must be given to my mentor Moosa Hassan who provided invaluable feedback and advice throughout this project. He helped keep me on track and ensured I didn't lose my way in the process.</p>
<p>Thanks also to my fellow coders and students in the slack channel for this project - having people at hand for immediate feedback on an implementation or help with a bugfix or code that isn't working was a big help and stress reliever.</p>
<p>Thank you to the tutor support team at the code institute for their help with more technical issues when I wasn't able to get a solution from my other sources or through google. They were really understanding and took the time to explain to me any advice that they were giving me so that I knew what the code was doing.</p>

<p>The loading screen was the creation of Peter Tichy (ihatetomatoes) and can be found <a href="https://ihatetomatoes.net/create-custom-preloading-screen/" target="_blank">here</a>The only changes made to the code were the colours displayed
<p>The images and recipes used in this project were all obtained from one of three sources, <a href="https://bbcgoodfood.com" target="_blank">BBC Good Food</a>, <a href="https://epicurious.com" target="_blank">Epicurious</a> and <a href="https://maangchi.com" target="_blank">Maangchi</a>
<p>Logic and code for the login and signup forms was gotten from <a href="https://wtforms.readthedocs.io/en/stable/" target="_blank">WTForms</a><p>
<p>Code for the back button on the single recipe page found <a href="https://www.w3schools.com/jsref/met_his_go.asp" target="_blank">here</a>