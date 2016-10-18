# XboxOneGiveAways Bot

Simple reddit bot which crawls reddit submissions using praw4 and send emails based on keyword
to run : 
```python
python xbox_bot.py
```

To deploy on heroku create the required config vars:
* REDDIT_USERNAME
* REDDIT_PASSWORD
* REDDIT_CLIENT_ID
* REDDIT_CLIENT_SECRET
* SENDGRID_APIKEY
* MAIL_TO
* MAIL_FROM

## Prerequisites:
1. Sendgrid Api, signup here : [Signup on Sendgrid](https://app.sendgrid.com/signup)
2. Reddit App, how to create: [How to Create Reddit App](https://ssl.reddit.com/prefs/apps/)