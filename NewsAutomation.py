from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from newsapi import NewsApiClient
import random
import time
import datetime

NewsAPI = NewsApiClient(api_key='b3e1bef2482a487c8fae936d1daee143')

def RandomSources():
    global Articles

    Sources = ['abc-news','axios','bbc-news','breitbart-news','business-insider','buzzfeed','cbc-news','cbs-news','cnbc','cnn','daily-mail','engadget','espn','fox-news','google-news','hacker-news','ign','independent','mirror','time','wired']

    X = random.randint(0, 19)

    TopHeadlines = NewsAPI.get_top_headlines(sources=Sources.pop(X))
    Articles = TopHeadlines('articles')

def RandomArticles():
    global Articles
    global News

    Y = random.randint(0, 5)

    ArticlesP = Articles(Y)

    News = ArticlesP('title')+"\n\n"+ArticlesP('url')

def RandomHashTags():
    global HashTag
    global NewsN

    HashTag = ['Breaking Now','Just In','Daily Update','Update Now','News Now']

    Z = random.randint(0, 4)

    NewsN = News+"\n\n"+HashTag

def NewsStatus():
    global Status

    Status = NewsN+"\n\n"+"Posted Successfully"

time.sleep(5)
DriverTwitter = webdriver.Firefox()
waitTwitter = WebDriverWait(DriverTwitter, 10)

time.sleep(5)
DriverFacebook = webdriver.Firefox()
waitFacebook = WebDriverWait(DriverFacebook, 10)

time.sleep(5)
DriverYandex = webdriver.Firefox()
waitYandex = WebDriverWait(DriverYandex, 10)

DriverTwitter.get('https://www.twitter.com')
DriverFacebook.get('https://www.facebook.com')
DriverYandex.get('https://mail.yandex.com')

UsernameTwitterP = 'SeleniumAutoT'
PasswordTwitterP = 'SeleniumAutomation'

EmailFacebookP = 'seleniumautomation@yandex.com'
PasswordFacebookP = 'SeleniumAutomation'

EmailYandexP = 'seleniumauto@yandex.com'
PasswordYandexP = 'SeleniumAutomation'

ToYandexP = 'subhambaliarsingh@outlook.com,alokpattnaik1998@gmail.com,amitsanjib0007@gmail.com'

time.sleep(5)
LoginTwitter = waitTwitter.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]'))
LoginTwitter.click()

time.sleep(5)
UsernameTwitter = waitTwitter.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input'))
UsernameTwitter.clear()
UsernameTwitter.send_keys('UsernameTwitterP')

time.sleep(5)
PasswordTwitter = waitTwitter.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input'))
PasswordTwitter.clear()
PasswordTwitter.send_keys('PasswordTwitterP')

time.sleep(5)
LoginTwitterN = DriverTwitter.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button')
LoginTwitterN.click()

time.sleep(5)
EmailFacebook = waitFacebook.until(EC.visibility_of_element_located(By.XPATH,'//*[@id="email"]'))
EmailFacebook.clear()
EmailFacebook.send_keys(EmailFacebookP)

time.sleep(5)
PasswordFacebook = waitFacebook.until(EC.visibility_of_element_located(By.XPATH,'//*[@id="pass"]'))
PasswordFacebook.clear()
PasswordFacebook.send_keys(PasswordFacebookP)

time.sleep(5)
LoginFacebook = DriverFacebook.find_element_by_xpath('//*[@id="u_0_2"]')
LoginFacebook.click()

time.sleep(5)
LoginYandex = waitYandex.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div/div/div[2]/div/div/div[4]/a[2]'))
LoginYandex.click()

time.sleep(5)
EmailYandex = waitYandex.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/form/div[1]/label/input'))
EmailYandex.clear()
EmailYandex.send_keys(EmailYandexP)

time.sleep(5)
PasswordYandex = waitYandex.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/form/div[2]/label/input'))
PasswordYandex.clear()
PasswordYandex.send_keys(PasswordYandexP)

time.sleep(5)
SignInYandex = DriverYandex.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/form/div[4]/button[1]')
SignInYandex.click()

time.sleep(5)
TweetBox = waitTwitter.until(EC.visibility_of_element_located(By.XPATH,'//*[@id="tweet-box-home-timeline"]'))

time.sleep(5)
PostBox = waitFacebook.until(EC.visibility_of_element_located(By.XPATH,'//*[@id="js_5"]'))

Process = 'Start'

while Process is 'Start':
    RandomSources()
    RandomArticles()
    RandomHashTags()
    NewsStatus()

    Counter = 1

    NewsNumber = 'News Number : '+str(Counter)

    SubjectYandexP = ' NOTIFICATION '+NewsNumber

    TweetBox.clear()
    TweetBox.send_keys(NewsN)

    Tweet = DriverTwitter.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/form/div[3]/div[2]/button')
    Tweet.click()

    PostBox.clear()
    PostBox.send_keys(NewsN)

    Post = DriverFacebook.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div/button')
    Post.click()

    ComposeYandex = waitYandex.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div[2]/div[4]/div/div[2]/div[2]/div/div/a'))
    ComposeYandex.click()

    ToYandex = waitYandex.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div[2]/div[4]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/div[1]/label/div[3]/div'))
    ToYandex.clear()
    ToYandex.send_keys(ToYandexP)

    SubjectYandex = waitYandex.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div[2]/div[4]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/label/div[3]/input'))
    SubjectYandex.clear()
    SubjectYandex.send_keys(SubjectYandexP)

    MessageBodyYandex = waitYandex.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div[2]/div[4]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[2]/label/div[2]/div/div/div/div/div'))
    MessageBodyYandex.clear()
    MessageBodyYandex.send_keys(Status)

    SendYandex = DriverYandex.find_element_by_xpath('//*[@id="nb-42"]')
    SendYandex.click()

    now = datetime.datetime.now()
    print(NewsNumber)
    print(now.strftime("%Y-%m-%d %H:%M:%S \n"))

    time.sleep(900)


