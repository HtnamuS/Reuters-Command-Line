from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,sys

driver = webdriver.PhantomJS()

def allNews(detail):
	print('Fetching Reuters\' Top News ...\n')
	driver.get('https://in.reuters.com/news/archive')
	headlines = driver.find_elements_by_class_name("story-title")
	print('TOP NEWS HEADLINES:\n')
	for headline in headlines:
		try:
			print('\t' + str(headlines.index(headline) + 1) + ': ' + headline.text, end = '\n\n')
		except UnicodeEncodeError:
			print('ERROR: Unable to print this headline\n')
def worldNews(detail):
	print('Fetching Reuters\' World News ...\n')
	driver.get('https://in.reuters.com/news/archive/worldNews?view=page')
	headlines = driver.find_elements_by_class_name("story-title")
	print('WORLD NEWS HEADLINES:\n')
	for headline in headlines:
		print('\t' + str(headlines.index(headline)+1) + ': ' + headline.text, end='\n\n')

def moneyNews(detail):
	print('Fetching Reuters\' Money News ...\n')
	driver.get('https://in.reuters.com/news/archive/businessNews?view=page')
	headlines = driver.find_elements_by_class_name("story-title")
	print('MONEY NEWS HEADLINES:\n')
	for headline in headlines:
		try:
			print('\t' + str(headlines.index(headline) + 1) + ': ' + headline.text, end = '\n\n')
		except UnicodeEncodeError:
			print('ERROR: Unable to print this headline\n')

def techNews(detail):
	print('Fetching Reuters\' Tech News ...\n')
	driver.get('https://in.reuters.com/news/archive/technologyNews?view=page')
	headlines = driver.find_elements_by_class_name("story-title")
	print('TECHNOLOGY NEWS HEADLINES:\n')
	for headline in headlines:
		try:
			print('\t' + str(headlines.index(headline) + 1) + ': ' + headline.text, end = '\n\n')
		except UnicodeEncodeError:
			print('ERROR: Unable to print this headline\n')

def scienceNews(detail):
	print('Fetching Reuters\' Science News ...\n')
	driver.get('https://in.reuters.com/news/archive/scienceNews?view=page')
	headlines = driver.find_elements_by_class_name("story-title")
	print('SCIENCE NEWS HEADLINES:\n')
	for headline in headlines:
		try:
			print('\t' + str(headlines.index(headline) + 1) + ': ' + headline.text, end = '\n\n')
		except UnicodeEncodeError:
			print('ERROR: Unable to print this headline\n')

def ndtvIndia(detail):
	print('\nFetching NDTV India News ...\n')
	driver.get('https://www.ndtv.com/india?pfrom=home-topnavigation')
	headlines = driver.find_elements_by_class_name("nstory_header")
	print('NDTV INDIA NEWS HEADLINES:\n')
	for headline in headlines:
		try:
			print('\t' + str(headlines.index(headline) + 1) + ': ' + headline.text, end = '\n\n')
		except UnicodeEncodeError:
			print('ERROR: Unable to print this headline\n')

def southAsiaNews(detail):
	print('Fetching Reuters\' South Asia News ...\n')
	driver.get('https://in.reuters.com/news/archive/southasiaNews?view=page')
	headlines = driver.find_elements_by_class_name("story-title")
	print('SOUTH-ASIA NEWS HEADLINES:\n')
	for headline in headlines:
		try:
			print('\t' + str(headlines.index(headline) + 1) + ': ' + headline.text, end = '\n\n')
		except UnicodeEncodeError:
			print('ERROR: Unable to print this headline\n')

def sportNews(detail):
	print('Fetching Reuters\' Sport News ...\n')
	driver.get('https://in.reuters.com/news/archive/sportsNews?view=page')
	headlines = driver.find_elements_by_class_name("story-title")
	print('SPORT NEWS HEADLINES:\n')
	for headline in headlines:
		try:
			print('\t' + str(headlines.index(headline) + 1) + ': ' + headline.text, end = '\n\n')
		except UnicodeEncodeError:
			print('ERROR: Unable to print this headline\n')

def marketsNews(detail):
	print('Fetching Reuters\' Markets News ...\n')
	driver.get('https://in.reuters.com/news/archive/marketsNews?view=page')
	headlines = driver.find_elements_by_class_name("story-title")
	print('MARKETS NEWS HEADLINES:\n')
	for headline in headlines:
		try:
			print('\t' + str(headlines.index(headline) + 1) + ': ' + headline.text, end = '\n\n')
		except UnicodeEncodeError:
			print('ERROR: Unable to print this headline\n')

def cricBuzz(detail):
	print('\nFetching cricbuzz News ...\n')
	driver.get('http://www.cricbuzz.com/cricket-news/latest-news')
	headlines = driver.find_elements_by_tag_name('h2')
	print('CRICKET NEWS HEADLINES:\n')
	for headline,count in zip(headlines,range(10)):
		try:
			print('\t' + str(headlines.index(headline) + 1) + ': ' + headline.text, end = '\n\n')
		except UnicodeEncodeError:
			print('ERROR: Unable to print this headline\n')

def helpmenu():
	print('REUTERS COMMAND-LINE APPLICATION:(unofficial)\n')
	print('This is a command line application to view the headlines of various columns of Reuters news\n')
	print('SYNTAX:\n')
	print('\treuters <arg>\n')
	print('The argument can be: \n')
	print('\t - No argument. Top news')
	print('\t world - Headlines of top world news')
	print('\t money/business - Headlines of top Business news')
	print('\t tech/technology - Headlines of top Tech news')
	print('\t science - Headlines of top Science news')
	print('\t india - Indian Reuters\' are unavailable at the moment. NDTV India news can be chosen to be displayed instead')
	print('\t southasia - Headlines of top news of Southasia')
	print('\t sport - Headlines of top Sport news')
	print('\t market - Headlines of news of Markets around the globe')
	print('\t cricket - Reuters\' Cricket news are unavailable at the moment. Cricbuzz news can be chosen to be displayed instead ')

if len(sys.argv) == 1:
	allNews(0)
elif 'world' in sys.argv[1] and len(sys.argv) == 2:
	worldNews(0)
elif ('money' in sys.argv[1] and len(sys.argv) == 2) or ('business' in sys.argv[1] and len(sys.argv) == 2):
	moneyNews(0)

elif ('technology' in sys.argv[1] and len(sys.argv) == 2) or ('tech' in sys.argv[1] and len(sys.argv) == 2):
	techNews(0)
elif 'science' in sys.argv[1] and len(sys.argv) == 2:
	scienceNews(0)
elif 'india' in sys.argv[1] and len(sys.argv) == 2:
	print('Reuters\' India News unavailable. Would you like news from NDTV instead(y/n): ')
	choice = input()
	if choice == 'n' or choice == 'N':
		print('Try reuters southasia instead')
	elif choice == 'y' or choice == 'Y':
		ndtvIndia(0)
	else:
		print('ERROR: Wrong input')
elif ('southasia' in sys.argv[1] and len(sys.argv) == 2) or ('south_asia' in sys.argv[1] and len(sys.argv) == 2):
	southAsiaNews(0)
elif ('sport' in sys.argv[1] and len(sys.argv) == 2) or ('sports' in sys.argv[1] and len(sys.argv) == 2):
	sportNews(0)
elif ('market' in sys.argv[1] and len(sys.argv) == 2) or ('markets' in sys.argv[1] and len(sys.argv) == 2):
	marketsNews(0)
elif 'cricket' in sys.argv[1] and len(sys.argv) == 2:
	print('Reuters\' cricket news unavailable. Would you like news from cricbuzz instead(y/n): ')
	choice = input()
	if choice == 'y' or choice == 'Y':
		cricBuzz(0)
	elif choice != 'n' and choice != 'N':
		print('ERROR: Wrong input')
elif 'porn' in sys.argv[1]:
	print('\nLook for it somewhere else you fucking pervert!\n')
elif '--help' in sys.argv[1] or 'help' in sys.argv:
	helpmenu()
else:
	print('Incorrect Arguments. Please try \'reuters --help\'')
driver.close()