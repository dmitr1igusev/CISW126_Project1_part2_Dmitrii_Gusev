#CISW126 Dmitrii Gusev
#Inheritance Project 1

class Item:
    def __init__(self, description="None", price=0.0, quantity=0):
        self.description = description
        self.price = price
        self.quantity = quantity

    def display(self):
        return f"Item: {self.description}, price: {self.price}, quantity: {self.quantity}"


class Perishable(Item):
    def __init__(self, description="None", price=0.0, quantity=0, sellby="None", wt=0.0):
        super().__init__(description, price, quantity)
        self.sellby = sellby
        self.wt = wt

    def display(self):
       return super().display() + f" sell by: {self.sellby}, weight: {self.wt}\n"




class Electronics(Item):
    def __init__(self, description="None", price=0.0, quantity=0, warranty="None", power="None"):
        super().__init__(description, price, quantity)
        self.warranty = warranty
        self.power = power

    def display(self):
        return super().display() + f" warranty: {self.warranty}, power: {self.power}\n"




class Movies(Item):
    def __init__(self, description="None", price=0.0, quantity=0, director="None", release_year="None", rating=0.0):
        super().__init__(description, price, quantity)
        self.director = director
        self.release_year = release_year
        self.rating = rating

    def display(self):
        return super().display() + f" director: {self.director}, release year: {self.release_year}, rating: {self.rating}\n"




if __name__ == "__main__":

     shopping_cart = []

     tomatoes = Perishable("Tomatoes", 3.00, 34, "May 11, 2024", 16)
     bananas = Perishable("Bananas", 3.99, 12, "April 7, 2024", 30)
     AppleWatch = Electronics("Apple Watch",  429.99, 2, "1 year", "AAA")
     Iphone = Electronics("Iphone 15 pro max", 1199.39, 1, "6 months","AA")
     Movie1 = Movies("Harry Potter and the Prizoner of Azkaban", 2.59, 1, "Alfonso Cuarón", "2004", 7.9)
     Movie2 = Movies("Ocean's 8", 3.99, 1, "Gary Ross", "2018", 6.3)

     shopping_cart.append(tomatoes)
     shopping_cart.append(bananas)
     shopping_cart.append(AppleWatch)
     shopping_cart.append(Iphone)
     shopping_cart.append(Movie1)
     shopping_cart.append(Movie2)

     for i in range(0, len(shopping_cart)):
         print(shopping_cart[i].display())




