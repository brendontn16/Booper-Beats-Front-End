# Import the Anvil dependencies
import anvil.server
from anvil import open_form

class MyForm(MyFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.total_price = 0  # Initialize the total price

    def update_order(self, ingredient, price):
        # Update the order menu with the selected ingredient and its price
        self.order_dropdown.items.append(f"{ingredient} - ${price:.2f}")
        # Update the total price
        self.total_price += price
        self.total_label.text = f"Total: ${self.total_price:.2f}"

    def button_crust_click(self, **event_args):
        # Call the server function to get the crust information
        crust_data = anvil.server.call('get_ingredient_data', 'Crust')
        # Update the order with the crust information
        self.update_order(crust_data['name'], crust_data['price'])

    def button_topping_click(self, **event_args):
        # Call the server function to get the topping information
        topping_data = anvil.server.call('get_ingredient_data', 'Topping')
        # Update the order with the topping information
        self.update_order(topping_data['name'], topping_data['price'])

    def button_sauce_click(self, **event_args):
        # Call the server function to get the sauce information
        sauce_data = anvil.server.call('get_ingredient_data', 'Sauce')
        # Update the order with the sauce information
        self.update_order(sauce_data['name'], sauce_data['price'])