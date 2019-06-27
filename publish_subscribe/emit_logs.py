import sys

import pika
from pika import BlockingConnection
from pika.channel import Channel


connection: BlockingConnection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel: Channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(exchange='logs', routing_key='', body=bytes(message, encoding='utf8'))
print(" [x] Sent %r" % message)
connection.close()
