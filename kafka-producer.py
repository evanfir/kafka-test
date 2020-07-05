from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
# producer.send('sample', b'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()
# producer.send('test', b'test123')