import praw
import sendgrid
import os
import datetime, time
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#define constants
username = os.environ.get('REDDIT_USERNAME')
password = os.environ.get('REDDIT_PASSWORD')
client_id = os.environ.get('REDDIT_CLIENT_ID')
client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
sendgrid_api_key = os.environ.get('SENDGRID_APIKEY')

user_agent = 'XboxOneGiveAways v0.1'
mail_from = os.environ.get('MAIL_FROM')
mail_to = os.environ.get('MAIL_TO')

giveaways_keywords = ['[ giveaway ]', 'free games', '[ giveaways ]', 'give', '[giveaway ]', 'away', 'giveaways', 'free', '[giveaway]', 'give away', '[ give away]', 'giveaway', '[ giveaway]', '[giveaways]', 'for free', '[ giveaways ]', '[giveaway]', 'givesaway', 'givethemall', 'giving', 'giving away', 'gives away']

already_sent = []

def send_mail(submission):
	client = sendgrid.SendGridClient(sendgrid_api_key)
	if submission and submission.id not in already_sent:
		subject = 'Giveaway on Reddit at '+datetime.datetime.now().strftime('%d-%b-%Y %I:%M %p')
		created_on = time.strftime('%d-%b-%Y %I:%M %p',time.localtime(submission.created_utc))
		mail_message = "Giveaway on Reddit: <b>"+ str(submission.title) + "</b></br> Click here: <a href='"+submission.url+"'>Reddit link</a> " +"</br>" + submission.selftext + "</br>"+ "Created on: "+str(created_on)
		
		message = sendgrid.Mail()
		message.add_to(mail_to)
		message.set_from(mail_from)
		message.set_subject(subject)
		message.set_html(mail_message)

		client.send(message)
		print "Email Sent for "+str(submission.title)
		already_sent.append(submission.id)



def process_submission(submission):
	submission_title = submission.title.lower()

	for words in submission_title.split(' '):
		#this is done for testing heroku one off dynos, checking if the process keeps on running or not
		print "Hearbeat..." + str(words.encode('ascii', 'ignore').decode('ascii'))
		if words.strip() in giveaways_keywords:
			send_mail(submission=submission)

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