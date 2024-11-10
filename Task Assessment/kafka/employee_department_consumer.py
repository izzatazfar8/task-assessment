from confluent_kafka import Consumer, KafkaError
import json
import hashlib

# Kafka settings for department messages
consumer_config = {
    'bootstrap.servers': 'localhost:9092',        
    'group.id': 'new_employees_department',     
    'auto.offset.reset': 'earliest'               
}

# Initialize Kafka consumer 
consumer = Consumer(consumer_config)
consumer.subscribe(['department_messages'])

# Load previously processed messages (using content hashes) from a file
try:
    with open('/home/izzat/processed_department_messages.json', 'r') as f:
        processed_messages = json.load(f)
except FileNotFoundError:
    processed_messages = {}  # Start fresh if no file exists

# Consume messages in a loop
try:
    while True:
        # Poll Kafka for messages with a 1-second timeout
        msg = consumer.poll(1.0)

        if msg is None:
            continue  # No new message, continue polling
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"End of partition: {msg.topic()}[{msg.partition()}] at offset {msg.offset()}")
            else:
                print(f"Error: {msg.error()}")
            continue

        # Normalize and hash the message content to handle duplicate messages
        message_content = ' '.join(msg.value().decode('utf-8').split())
        message_hash = hashlib.sha256(message_content.encode()).hexdigest()

        # If the message is unique (not in processed_messages), print and save it
        if message_hash not in processed_messages:
            print(f"New message in department_messages: {message_content}")
            processed_messages[message_hash] = True

            # Save the processed messages to the file
            with open('/home/izzat/processed_department_messages.json', 'w') as f:
                json.dump(processed_messages, f)

except KeyboardInterrupt:
    print("Exiting department messages consumer...")

finally:
    consumer.close() 
