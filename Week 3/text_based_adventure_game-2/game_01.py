def say_hello():
    print("Hello!")

def say_name():
	print("lainey")

def say_age():
	print(13)

def favorite_foods(foods):
	print(foods)

def favorite_foods_list(foods):
	for food in foods:
		print(food)

def join_metals(metal_1, metal_2):
	print(metal_1+" "+metal_2)

if __name__ == '__main__':
    say_name()
    say_age()
    favorite_foods("apple")
    favorite_foods_list(["apple", "peanut", "bread"])
    join_metals("gold", "silver")