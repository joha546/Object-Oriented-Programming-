class Shirt:

  def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
    self.color=  shirt_color
    self.size =  shirt_size
    self.style = shirt_style
    self.price = shirt_price

tshirt_collection = []
shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve', 10)


tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three )

for shirt in tshirt_collection:
   print(shirt.color)