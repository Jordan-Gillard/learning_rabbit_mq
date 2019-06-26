import time

import pika
from pika import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel

from work_queues.config import QUEUE_NAME


# Connect to a broker on the local machine
connection: BlockingConnection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel: BlockingChannel = connection.channel()

# Make sure the queue exists. We can run this command as much as possible - we'll never have more than one of any queue
channel.queue_declare(queue=QUEUE_NAME, durable=True)


# See what queues are on our machine using CLI tool: `sudo rabbitmqctl list_queues`


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count('.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='hello', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
