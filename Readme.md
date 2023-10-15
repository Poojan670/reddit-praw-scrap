# Reddit Scrap Using Python and PRAW API
    
Scrap posts and comments with their nested levels of multiple subreddits, and export it into csv using Python and PrawAPI.

## Recommended Setup:
    python 3.0+ 
    Praw 7+


## SETUP Your Redit App

To extract data from Reddit, we need to create a Reddit app. You can create a new Reddit app(https://www.reddit.com/prefs/apps).
![img.png](static%2Fimg.png)

Click on “are you a developer? create an app…”.

Enter the name and description, and select script. After entering the details, click on “create app”.

![app.png](static%2Fapp.png)

The Reddit app has been created. Now, we can use python and praw to scrape data from Reddit. Note down the client_id, secret, and user_agent values. These values will be used to connect to Reddit using python.

## Installation and Setup

    1. Setup a python virtual environment
        py -m venv env 
            OR  
        use virtualenv: virtulenv env
    
    2. Activate virtual environment
        env\Scripts\activate (Windows)
            OR  
        source env/bin/active (Linux)
    
    3. Install Requirements
        pip install -r requirements.txt
    
    4. Setup Constants File
        this application needs a few environment constant values, the smaple provided :

        CLIENT_ID = 'r'
        CLIENT_SECRET = ''
        USER_AGENT = ''
        USERNAME = ''
        PASSWORD = ''
        SUBREDDITS = [] // list of subreddits you want to scrap your posts or comments
        POSTS_LIMIT = 10

        Constants can't be null or blank, should be valid

    5. Run the python script
        py main.py


## Contact

For any inquiries or support, please contact [info@poojanpradhan.com.np](info@poojanpradhan.com.np)
Feel Free to message me at upwork, Thank you for hiring me!!

## License

This project is licensed under the [MIT License](LICENSE).

---

