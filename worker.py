import os
from kombu import Connection, Exchange, Queue

auth_exchange = Exchange('auth', 'direct', durable=True)
auth_failed_queue = Queue('user', exchange=auth_exchange, key='authentication_failed')
auth_success_queue = Queue('user', exchange=auth_exchange, key='authentication_success')

connection = Connection(os.getenv('RABBITMQ_DSN'))


def on_failed(body, message):
    label = 'on_success'
    if message.delivery_info['routing_key'] == 'authentication_failed':
        label = 'on_failed'

    message.ack()


# def on_success(body, message):
#     logging.info('on_success: '.format(body))
#     message.ack()


with connection.Consumer([auth_failed_queue, auth_success_queue], callbacks=[on_failed]) as consumer:
    while True:
        connection.drain_events()
