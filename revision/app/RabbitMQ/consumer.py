import pika
import json
import time

AMQP_URL = "amqps://laeaaptx:cETjj5F9MqhXLgVZ9pEuMnkIInQHNHQs@seal-01.lmq.cloudamqp.com:5671/laeaaptx"

def consume_logs():
    params = pika.URLParameters(AMQP_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue="logs", durable=True)

    def callback(ch, method, properties, body):
        data = json.loads(body)
        print(f"New log: {data['event']}, user_id: {data['user_id']}")
        time.sleep(1)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue="logs",
        on_message_callback=callback
    )

    print("Waiting for logs")
    channel.start_consuming()

if __name__ == "__main__":
    consume_logs()