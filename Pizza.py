#!/usr/bin/env python3
__NAME__ = "Pinion, Alexandro"
__EMAIL__ = "apinion1@students.kennesaw.edu"
__DESC__ = "Assignment 1 - Design Patterns - SWE6683 - Summer2023"

#: Classes for decorator design pattern
class Pizza():
    """
    This is the base component - it's operations can be changed by decorators.
    """
    def __init__(self) -> None:
        self.name: str = "Pizza"
        self.desc: str = ""
        self.current_price: float = 9.99
        self.current_ingredients: list = []

    def cost(self) -> float:
        return self.current_price
    
    def display(self) -> str:
        return f"This is a {self.name} with the following ingredients: {self.current_ingredients}.\n"
    

class Hawaiian(Pizza):
    """
    This is a concrete component - this provides a default operation for the base component.
    """
    def cost(self) -> float:
        self.current_price = 14.99
        return self.current_price
    
    def display(self) -> str:
        self.name = "Hawaiian Pizza"
        self.desc = "This is a pizza originating from Canada that is topped traditionally with pineapple, " \
                    "tomato sauce, cheese, ham and bacon"
        self.current_ingredients = ["Pineapple", "Ham", "Cheese", "Bacon", "Tomato Sauce"]
        return f"{self.name} with the following ingredients: {self.current_ingredients}.\n" \
               f"{self.desc}\n"
    
class GardenFresh(Pizza):
    """
    This is a concrete component - this provides a default operation for the base component.
    """
    def cost(self) -> float:
        self.current_price = 14.99
        return self.current_price
    
    def display(self) -> str:
        self.name = "Garden Fresh Pizza"
        self.desc = "This is a pizza with fresh ingredients and does not contain any meat!"
        self.current_ingredients = ["Olives", "Peppers", "Cheese", "Tomato Sauce"]
        return f"{self.name} with the following ingredients: {self.current_ingredients}.\n" \
               f"{self.desc}\n"
    
class Meatlovers(Pizza):
    """
    This is a concrete component - this provides a default operation for the base component.
    """
    def cost(self) -> float:
        self.current_price = 14.99
        return self.current_price
    
    def display(self) -> str:
        self.name = "Garden Fresh Pizza"
        self.desc = "This is a pizza with fresh ingredients and does not contain any meat!"
        self.current_ingredients = ["Olives", "Peppers", "Cheese", "Tomato Sauce"]
        return f"{self.name} with the following ingredients: {self.current_ingredients}.\n" \
               f"{self.desc}\n"
    
    
class GourmetToppings(Pizza):
    """
    This is the base decorator class that defines how the interface for concrete decorates will operate.
    """
    _pizza: Pizza = None  # The undecorated object Pizza
    
    def __init__(self, pizza: Pizza) -> None:
        self._pizza = pizza

    
    @property
    def pizza(self) -> str:
        """
        Ensures that the decorator will deelgate the work wrapped over the component, Pizza - this is the 
        undecorated object.
        """
        return self._pizza
    
    def cost(self) -> float:
        self._pizza.cost()

    def display(self) -> str:
        self._pizza.display()

class Bacon(GourmetToppings):
    """
    Concrete Decorator - executes the specific behavior for a topping
    """
    

    def cost(self) -> float:
        price = 1.49
        self.pizza.current_price = self.pizza.cost() + price
        return price
    
    def display(self) -> str:
        ingredient: str = "Bacon"
        self.pizza.current_ingredients.append(ingredient)
        return ingredient
    

class Sausage(GourmetToppings):
    """
    Concrete Decorator - executes the specific behavior for a topping
    """
    

    def cost(self) -> float:
        price = 2.99
        self.pizza.current_price = self.pizza.cost() + price
        return price
    
    def display(self) -> str:
        ingredient: str = "Sausage"
        self.pizza.current_ingredients.append(ingredient)
        return ingredient
    
class Jalapenos(GourmetToppings):
    """
    Concrete Decorator - executes the specific behavior for a topping
    """
    

    def cost(self) -> float:
        price = 0.99
        self.pizza.current_price = self.pizza.cost() + price
        return price
    
    def display(self) -> str:
        ingredient: str = "Jalapenos"
        self.pizza.current_ingredients.append(ingredient)
        return ingredient
    
class Chicken(GourmetToppings):
    """
    Concrete Decorator - executes the specific behavior for a topping
    """
    

    def cost(self) -> float:
        price = 3.49
        self.pizza.current_price = self.pizza.cost() + price
        return price
    
    def display(self) -> str:
        ingredient: str = "Chicken"
        self.pizza.current_ingredients.append(ingredient)
        return ingredient
    

class Meatball(GourmetToppings):
    """
    Concrete Decorator - executes the specific behavior for a topping
    """
    
    def cost(self) -> float:
        price = 3.99
        self.pizza.current_price = self.pizza.cost() + price
        return price
    
    def display(self) -> str:
        ingredient: str = "Meatball"
        self.pizza.current_ingredients.append("Meatball")
        return ingredient
    

    


#: Function(s) for interfacing with pizza component
def order_standard_pizza(pizza: Pizza) -> str:
    """
    This is how the user can interface to all of the objects in the component, Pizza.
    The function will use the concrete components to order default configurations of the
    base component, Pizza.
    """
    return f"The following pizza has been ordered: {pizza.display()}Total price: &{pizza.cost()}\n\n"

def order_custom_pizza(toppings: list) -> str:
    """
    This is how the user can interface to all of the objects in the base component, Pizza.
    This function will use the concrete decorator(s) that interface with the base component, Pizza,
    to make a custom order with specified toppings.
    """
    new_pizza: Pizza = Pizza()
    total_toppings: int = len(toppings)
    new_pizza.name = f"{total_toppings}-Topping Pizza"
    new_pizza.desc = f"Custom pizza with customer-specified toppings."
    

    for topping in range(total_toppings):
        new_topping = toppings[topping](pizza=new_pizza)
        print(f"Topping added: {new_topping.display()}----Price: +${new_topping.cost()}")
    

    return f"{new_pizza.display()}\nTotal price: ${new_pizza.cost()}"
   

if __name__ == "__main__":
    # (1) Order a hawaiian pizza
    hawaiian_pizza_receipt = order_standard_pizza(pizza=Hawaiian())
    print(hawaiian_pizza_receipt)

    # (2) Make pizza with 2 toppings
    custom_pizza_receipt = order_custom_pizza(toppings=[Meatball, Jalapenos, Sausage, Chicken, Bacon])
    print(custom_pizza_receipt)

    
