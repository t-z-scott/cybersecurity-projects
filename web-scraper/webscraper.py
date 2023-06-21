from bs4 import BeautifulSoup
import requests

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")    # gets html from the tweets, but it's not readable 'tweets'
#tweet = content.find_all('p',attrs={"class": "content"})   # only reads the first <p> tag with the class "context"
for tweet in content.find_all('p', attrs={"class": "context"}):print (tweet.text.encode('utf-8')) # views all tweets
# TODO: step 4c converting scraped data to JSON

print (content)