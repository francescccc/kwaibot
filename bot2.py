import tweepy
import random


consumer_key = 'masN5cb6qblUFfSaBiw5Trwh9'
consumer_secret = 'HZSVidytbH1XeXKyTSBqhHPE29nyBw0V0UHcyBVkiVnyhZDEaQ'

key = '1395480407462789125-18gZcCVsaeVeX1uk1LITrwjvWA76S4'
secret = 'zXtNcrlFvnUwAYZspKuEGd54xHSGaCa2afqkzTf5M8Dj5'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)



# xskm




def tweetsend2():
    print("oi")
    public_tweets = api.search(q='bts -filter:retweets', count=1, since="2018-06-09", tweet_mode="extended", geocode='-11.800399,-48.339055,1800km')
    for tweet in public_tweets:
        print(tweet.full_text)
        print(tweet.user.id)
        recipient_id = tweet.user.id
        text = "Oie, eu sei que é chato pedir, mas você poderia dar uma olhada no meu fixado? Eu to passando por umas situações meio complicadas, se você puder me ajudar, eu ficaria muito grata" + u'\U0001F684'
        try:
            api.send_direct_message(recipient_id, text)
        except:
            pass



while True:
            tweetsend2()
            import time
            time.sleep(180)