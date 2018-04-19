# PalindromeDatabase
Flask based application to evaluate a string input from user to see if it's a palindrome, then returns a list of palindromes 

Installation instrustions:

Clone the repository:
    git clone "repository_url"

Change directory into the cloned repository and project directory:
    cd PalindromeDatabase/PalDB

Run the python code:
    python Pal.py
 

I couldn't manage to get the time constraint from the task working. I would add another column which stored the
creation times of the palindromes, and then uses a python function to check whether the time was greater than 10
minutes old, and if so exclude it from the display list.
 
Unfortunatly due to my lack of experience with SQL I didn't know enough to excute it but the above is my thought process.
 
 
I've also created the unittests which require the app to be installed which can be done as follows:
 
Change into directory of the git clone:
    cd PalindromeDatabase
    
Then use pip to install it locally:
    pip install --editable .
    
To then run you need to export the flask app, so flask knows what to run
    export FLASK_APP=PalDB
    export FLASK_DEBUG=true
    flask run
