# giftureframe_web_app
A web app version of my Giftureframe project.  Contains a small Flask server that searches through the Tenor API for gifs to display full screen in the web browser.


-Get your Tenor API key from www.tenor.com/gifapi/documentation

-Create a '.env' (without the single quotes) file in the project directory and add your Tenor API key as a varibable called 'api_key' (without the single quotes).

-Run in terminal:
  pip3 install python_dotenv
  pip3 install flask

-Open app.py in your favorite IDE and add change the 'ckey' variable in the get_gifs() function to the name of your app.
-Change the search term variable to a search term of your choice
-Set the interval to display gifs for
-Set the height and max-width of the <img> tag on the index.html inside the templates folder (default is 720px by 720px)

-To start the server run 'Python3 app.py' in your console / terminal.

-Navigate to localhost:5000 in your browser
