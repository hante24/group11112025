import time

import config
import datetime
import ssl
import pika

ssl_context = ssl.create_default_context()

connection_params = pika.ConnectionParameters(
    host=config.RMQ_HOST,
    port=config.RMQ_PORT,
    virtual_host=config.RMQ_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=config.RMQ_USER, password=config.RMQ_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context),
)


def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)


def process_message(channel: pika.adapters.blocking_connection.BlockingChannel, method, properties, body):
    print(body)
    print(5555555555555555555555)
    time.sleep(1)
    channel.basic_ack(delivery_tag=method.delivery_tag)



def consume_message(channel: pika.adapters.blocking_connection.BlockingChannel):
    print(5555556666666666666666666)
    QUEUE = 'weather'
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_message,
        auto_ack=False
    )
    channel.start_consuming()



def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_message(channel)



if __name__ == "__main__":
    main()