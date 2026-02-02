import pika
import json

AMQP_URL = "amqps://laeaaptx:cETjj5F9MqhXLgVZ9pEuMnkIInQHNHQs@seal-01.lmq.cloudamqp.com:5671/laeaaptx"

def produce_logs():
    params = pika.URLParameters(AMQP_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue="logs", durable=True)

    for i in range(100):
        message = {
            "event": "user_registered",
            "user_id": i
        }

        channel.basic_publish(
            exchange="",
            routing_key="logs",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )

        print(f"Sent: {message}")

    connection.close()

if __name__ == "__main__":
    produce_logs()