title = "Class Examples"
print(f"\n\n{title.center(50, '*')}\n")

from classes.all_classes import *

animal = Animal('abstract animal')
animal.get_description();


basanti = Cow('Basanti', 0)

pushpa = Cow('Pushpa', 3)
pushpa.age = 12

basanti.get_description();
basanti.walk();
basanti.eat();

pushpa.get_description();
pushpa.walk();
pushpa.eat();

