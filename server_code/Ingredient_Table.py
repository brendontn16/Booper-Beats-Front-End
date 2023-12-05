# Import the Anvil dependencies
import anvil.server

@anvil.server.callable
def get_ingredient_data(ingredient_type):
    # Retrieve the ingredient data from the Data Table
    table = anvil.server.get_table('ingredients_table')
    ingredient_row = table.get_row(ingredient_type=ingredient_type)

    # Return a dictionary with ingredient name and price
    return {'name': ingredient_row['ingredient_name'], 'price': ingredient_row['ingredient_price']}