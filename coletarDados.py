
import facebook
import requests
import csv
import json
import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import urllib
import re
import sys



def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post['date'])


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
#access_token = 'CAACEdEose0cBANgKhe8lKFyNAZCiM58kfuGreionnmZC6b5dSHZCyxeaOjZCCP0qhrvZAXFj6h7DHqd3kRIZCDs00dtzy3e44hzzOYSi7SEnB4V7FdeBzbqfZCWbEV6rTxZBZB8xcIG4MvWW8jsoZAGTjXgZCxvINrLpMmK0KHpxWxQcoyB5ZBx7lu5uG57nHdZCmDMmjoueXoZBrXVQZDZD'
# Look at Bill Gates's profile for this example by using his Facebook id.

#user = 'BillGates'

#graph = facebook.GraphAPI(access_token)
#profile = graph.get_object(user)
#posts = graph.get_connections(profile['id'], 'posts')

# Wrap this block in a while loop so we can keep paginating requests until
# finished.
#while True:
   # try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
    #    [some_action(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
    #    posts = requests.get(posts['paging']['next']).json()
    #except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
     #   break


url = "https://graph.facebook.com/v2.5/search?pretty=0&q=belo_horizonte&type=event&limit=5000&after=MjQZD&access_token=CAACEdEose0cBACi4bCtN5ZAPgCJLlCt9S3YtJHhraRjg3e0QRmLXBdZAjw1u5m36mpag2J6fUdTbZBAsfGTo2dhWXmaIQC3mTwnxaCafbJ7Yyjtjb6EYzdbFdly58Xm3sUt5NeRvaynxIz6RsbkMjBNCTl8V3bz2nM21Rze9rpvk0zXc5fnW9ZC32vHfkUrxsVOv2eiKwQZDZD"
data = requests.get(url)
data.text
print (data.encoding)

print(data.encoding) 
print(data.text.decode('utf-8'))

with open('faceEventos','w') as saida:
	saida.write(data.text)
