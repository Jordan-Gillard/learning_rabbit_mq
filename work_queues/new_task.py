import sys
import pika
from pika import BlockingConnection
from pika.channel import Channel


# Connect to a broker on the local machine
from work_queues.config import QUEUE_NAME

connection: BlockingConnection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel: Channel = connection.channel()

# Create a queue
channel.queue_declare(queue=QUEUE_NAME, durable=True)


message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key=QUEUE_NAME,
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2),  # makes message persistent
                      )

print(" [x] Sent %r" % message)


# Close our connection
connection.close()
