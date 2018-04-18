# PalindromeDatabase
Flask based application to evaluate a string input from user to see if it's a palindrome, then returns a list of palindromes 

Installation instrustions:

Clone the repository:
    git clone "repository_url"

Build the packages and install to venv
    sudo pip install --editable .

Now set the paths for the app (debug is optional but if you're manipulating the source then it's recommended)
    export FLASK_APP=PalDB
    export FLASK_DEBUG=true

Run the application!
    flask run

This should then start a local server which you can navigate to by typing in a browser "localhost:5000" (without the "")
 