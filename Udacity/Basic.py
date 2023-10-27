class Shirt:

  def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
    self.color=  shirt_color
    self.size =  shirt_size
    self.style = shirt_style
    self.price = shirt_price

  def change_price(self, new_price):
      self.price = new_price

  def discount(self, discount):
      return self.price * (1-discount)


Shirt('red', 'S', 'short sleeve', 15)

new_shirt = Shirt('red', 'S', 'short sleeve', 15)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_shirt.change_price(10)
print(new_shirt.price)

print(new_shirt.discount(.2))

shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

total = new_shirt.price + shirt_two.price

total_discount =  new_shirt.discount(.14) + shirt_two.discount(.06)