from kafka import KafkaConsumer

# Kafka consumer setup
consumer = KafkaConsumer("LTC-USD", bootstrap_servers='localhost:9092')

# Consume messages
for message in consumer:
    print(message.value.decode('utf-8'))
