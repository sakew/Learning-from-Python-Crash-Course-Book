class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        for flavor in self.flavors:
            print("- " + flavor.title())




restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("Number of clients served: " + str(restaurant.number_served))

restaurant.number_served = 300
print("Number of clients served: " + str(restaurant.number_served))

restaurant.set_number_served(1288)
print("Number of clients served: " + str(restaurant.number_served))

restaurant.increment_number_served(255)
print("Number of clients served: " + str(restaurant.number_served))



iceCream = IceCreamStand('Il Gellato Bruno')
iceCream.flavors = ['vanilla', 'chocolate', 'cookies', 'raspberry']

iceCream.describe_restaurant()
iceCream.display_flavors()

