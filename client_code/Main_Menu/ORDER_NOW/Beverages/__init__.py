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

    #food_item_types = app_tables.fullmenu.search(Menu_Type='Drinks').distinct('Food_Item_Type')
    
    drinks_list = app_tables.fullmenu.search(Menu_Type='Drinks')

    unique_food_item_types = set()

    for row in drinks_list:
      unique_food_item_types.add(row['Food_Item_Type'])
    
    for food_item_type in unique_food_item_types:
      column_panel = ColumnPanel()
      label = Label(text=food_item_type)
      column_panel.add_component(label)

      self.drink_menu.add_component(column_panel)
      for i, row in drinks_list:
        if food_item_type == drinks_list[i]:
          
          

    self.drink_menu.clear()
    # Make some default columns to be populated within the card
    drink_columns = 4
    
    # prep the grid with columns
    self.drink_menu.columns = drink_columns
    
    #get a list of drinks from the fullmenu


    num_rows = (len(drinks_list) + drink_columns-1) // drink_columns
    button_index = 0

    #generate a button for each of these drinks into the columned panels
    for row_index in range(num_rows):
      
      for col_index in range(drink_columns):
          #button_index = row_index * drink_columns + col_index

          if button_index < len(drinks_list):
            drink_row = drinks_list[button_index]
            drink_text = drink_row['Specific_Item']
            drink_button = Button(text=drink_text)
            #give the button interactivity
        
            #place the button within the grid
            self.drink_menu.add_component(drink_button, row=row_index, column=col_index)
            button_index = button_index +1
      

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu.ORDER_NOW')
    pass
