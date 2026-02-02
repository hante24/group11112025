import redis
import os
from dotenv import load_dotenv

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)

print("Connected:", r.ping())

r.set("favorite_car", "Tesla")
car = r.get("favorite_car")
print("Favorite car:", car)

r.set("favorite_pet", "Cat", ex=7200)
pet = r.get("favorite_pet")
print("Favorite pet:", pet)

shopping_list = [
    "Milk",
    "Bread",
    "Eggs",
    "Cheese",
    "Apples"
]

for product in shopping_list:
    r.rpush("shopping_list", product)
r.expire("shopping_list", 604800)

first_three = r.lrange("shopping_list", 0, 2)
print("First three products:", first_three)

r.hset("cake_ingredients", "sugar", 300)
r.hset("cake_ingredients", "sugar", 500)
ingredients = r.hgetall("cake_ingredients")
print("Cake ingredients:", ingredients)
r.delete("cake_ingredients")