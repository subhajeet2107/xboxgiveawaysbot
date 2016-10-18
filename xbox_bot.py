import praw
import os
import yagmail
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#define constants
username = os.environ.get('REDDIT_USERNAME')
password = os.environ.get('REDDIT_PASSWORD')
client_id = os.environ.get('REDDIT_CLIENT_ID')
client_secret = os.environ.get('REDDIT_CLIENT_SECRET')

gmail_email = os.environ.get('GMAIL_EMAIL')
gmail_password = os.environ.get('GMAIL_PASS')

user_agent = 'XboxOneGiveAways v0.1'
mail_to = os.environ.get('MAIL_TO')

giveaways_keywords = ["give", "away", "giveaway", "give away","free games", "free","for free","givethemall", "giveaways","givesaway"]


def send_mail(sub_title):
	if sub_title:
		message = "Giveaway on Reddit: "+ str(sub_title)
		yag = yagmail.SMTP(gmail_email, gmail_password)
		yag.send(mail_to, 'subject', message)



def process_submission(submission):
	submission_title = submission.title.lower()

	for words in submission_title.split(' '):
		if words in giveaways_keywords:
			send_mail(sub_title=submission.title)

def init_bot():
	bot = praw.Reddit(user_agent=user_agent,
                  client_id=client_id,
                  client_secret=client_secret,
                  username=username,
                  password=password)
	subreddit = bot.subreddit('xboxone')
	for submission in subreddit.stream.submissions():
		process_submission(submission)
	

if __name__ == '__main__':
	print "Bot Started.."
	init_bot()