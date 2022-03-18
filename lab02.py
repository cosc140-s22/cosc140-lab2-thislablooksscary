from enum import Enum

class FoodCategory(Enum):
  VEGETABLE=1
  FRUIT=2
  GRAIN=3
  PROTEIN=4
  DAIRY=5
  OIL=6
  OTHER=7
#name is vegetable, value is 1
#ex: FoodCategory.FRUIT

  #enumerated type-used to identify a fixed set of options
  #no innit method
  #class should inherit from enum, then use series of assignemtns inside class from each of the values

class FoodItem(object):
  def __init__(self, name, category, numcals):
    try:
      FoodCategory(category)
    except ValueError:
      print("That's not a food category!")
    
    self.numcals=int(numcals)
    self.name=name
    self.category=FoodCategory(category)

  def get_name(self):
    return self.name

  def get_category(self):
    return self.category

  def calories_per_100g(self):
    return self.numcals

  def __str__(self):
    return f'{self.name} ({self.category}) {self.numcals}cal/100g'
   


class FoodServing(object):
  def __init__(self, foods, amt):
    self.foods=foods
    self.amt=int(amt)

  def food(self):
    return self.foods

  def amount(self):
    return self.amt

  def calories(self):
    self.cals= self.amt/100* self.foods.calories_per_100g()
    return int(self.cals)

  def __str__(self):
    return f"{self.amt}g of {self.foods}"
    


class Meal(object):
  def __init__(self):
    self.servings=list()

  def addFood(self, FoodServing):
    self.servings.append(FoodServing)

  def calories(self):
    self.sum=0
    for serving in self.servings:
      self.sum+=serving.calories()
    return self.sum

  def __str__(self):
    self.represent=""
    for serv in self.servings:
      self.represent+= str(serv)+"\n"
    return self.represent
    