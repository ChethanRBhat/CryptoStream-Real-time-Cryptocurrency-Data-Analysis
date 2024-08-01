from kafka import KafkaConsumer

# Kafka consumer setup
consumer = KafkaConsumer("ETH-USD", bootstrap_servers='localhost:9092')

# Consume messages
for message in consumer:
    print(message.value.decode('utf-8'))
