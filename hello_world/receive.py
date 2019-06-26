import pika
from pika import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel


# Connect to a broker on the local machine
connection: BlockingConnection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel: BlockingChannel = connection.channel()

# Make sure the queue exists. We can run this command as much as possible - we'll never have more than one of any queue
channel.queue_declare(queue='hello')

# See what queues are on our machine using CLI tool: `sudo rabbitmqctl list_queues`


def callback(ch, method, properties, body):
    print(f' [x] received {body}')


# Tell RMQ that callback should receive the messages
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
