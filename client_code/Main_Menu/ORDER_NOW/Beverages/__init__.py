from ._anvil_designer import BeveragesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Beverages(BeveragesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # ensure page data is clear before generation
    self.drink_menu.clear()
    # Make some default columns to be populated within the card
    drink_columns = 4
    
    # prep the grid with columns
    self.drink_menu.columns = drink_columns
    
    #get a list of drinks from the fullmenu
    drinks_list = app_tables.fullmenu.search(Menu_Type='Drinks')
    #buttons_per_column = len(drinks_list) // drink_columns

    #generate a button for each of these drinks into the columned panels
    for i, row in enumerate(drinks_list):
      drink_button = Button(text=row['Specific_Item'])
      #give the button interactivity
      drink_column_index = i % drink_columns
      drink_column_panels[drink_column_index].add_component(drink_button)
      

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu.ORDER_NOW')
    pass
