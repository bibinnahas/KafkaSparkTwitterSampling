# KafkaSparkTwitterSampling
Read tweets into kafka topic and consumer using spark

## Prerequisites
### Produce twitter credentials from developer console
- access_token = "****"
- access_token_secret = "****"
- consumer_key = "****"
- consumer_secret = "****"
### Install below packages
- pip3 install kafka-python
- pip3 install python-twitter
- pip3 install tweepy
### Start Kafka
- sudo bin/zookeeper-server-start.sh config/zookeeper.properties
- sudo bin/kafka-server-start.sh config/server.properties
### Create Sample topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic covid_tweets
#### Reference
https://github.com/kaantas/kafka-twitter-spark-streaming
