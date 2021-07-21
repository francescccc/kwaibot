import tweepy
import random


consumer_key = 'wK3c6d2EG39jRykOOEDcDYnRn'
consumer_secret = 'fkLXbSW7k3yhzbIkd1ZEE4rYhBrQ9iVUNELe2I6yI5dF2BPHJ4'

key = '1393991480411316228-hEU1HkGqEqqsm05YiydYEtc7134hhL'
secret = 'djPgIpMJpFesXTusNpZNEUX6k7TQqnrdwjYbnAxnRkHCO'


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
        text = "Oiiie, você poderia por favor dar um olhada no meu fixado? Eu to passando por umas situações meio dificeis, e em 3 minutos você poderia me ajudar sem gastar nada, por favor, me ajuda muito"
        try:
            api.send_direct_message(recipient_id, text)       
        except:
            pass



while True:
            tweetsend2()
            import time
            time.sleep(200)