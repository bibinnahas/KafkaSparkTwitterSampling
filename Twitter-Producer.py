import pykafka
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

"""API ACCESS KEYS"""
access_token = "****"
access_token_secret = "****"
consumer_key = "****"
consumer_secret = "****"

def authenticateTwitterApp():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

api = tweepy.API(authenticateTwitterApp())

# Twitter Stream Listener
class KafkaPushListener(StreamListener):
    def __init__(self):
        self.client = pykafka.KafkaClient("localhost:9092")
        self.producer = self.client.topics[bytes("covid_tweets", "ascii")].get_producer()

    def on_data(self, data):
        # Data comes from Twitter
        self.producer.produce(bytes(data, "ascii"))
        return True

    def on_error(self, status):
        print(status)
        return True
# Twitter Stream Config
twitter_stream = Stream(authenticateTwitterApp(), KafkaPushListener())
# Produce Data that has #covid
twitter_stream.filter(track=['#covid'])
