import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ)


BETTERSTACK_TOKEN = os.getenv('BETTERSTACK_TOKEN')
BETTERSTACK_HOST = os.getenv('BETTERSTACK_HOST')


RMQ_PORT=os.getenv('RMQ_PORT')
RMQ_USER=os.getenv('RMQ_USER')
RMQ_VIRTUAL_HOST=os.getenv('RMQ_VIRTUAL_HOST')
RMQ_HOST=os.getenv('RMQ_HOST')
RMQ_PASSWORD=os.getenv('RMQ_PASSWORD')