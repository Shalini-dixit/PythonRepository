import lizard,snake,gorilla,bear

liz = lizard.Lizard('Gecko')
print(liz.get_name())

snake = snake.Snake('Cobra')
print(snake.get_name())
gorilla = gorilla.Gorilla('Indian Gorilla')
print("{} is a mammal? {}".format(gorilla.get_name(), gorilla.is_mammal()))
print("{} is a reptile? {}".format(gorilla.get_name(), gorilla.is_reptile()))

bear = bear.Bear('Snow Bear')
print(bear.get_name())


