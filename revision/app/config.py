import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ)


BETTERSTACK_TOKEN = os.getenv('BETTERSTACK_TOKEN')
BETTERSTACK_HOST = os.getenv('BETTERSTACK_HOST')