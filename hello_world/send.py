import pika
from pika import BlockingConnection
from pika.channel import Channel


# Connect to a broker on the local machine
connection: BlockingConnection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel: Channel = connection.channel()

# Create a queue
channel.queue_declare(queue='hello')

message: bytes = b"Hello Jordan!"

# Send a message to the exchange, which forwards it to the queue
channel.basic_publish(exchange='',
                      routing_key='hello',  # this is the queue to send the message to
                      body=message)
print(f"' [x] sent {message}!'")

# Close our connection
connection.close()
