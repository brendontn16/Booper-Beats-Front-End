from ._anvil_designer import BeveragesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Beverages(BeveragesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    
    # Any code you write here will run before the form opens.

    # ensure page data is clear before generation
    self.drink_menu.clear()

    # get a list of drinks from the fullmenu
    drinks_list = app_tables.fullmenu.search(Menu_Type='Drinks')

    # prepare an empty set for the unique food_item_type from fullmenu
    unique_food_item_types = set()

    # populate the set with the food_item_types for drinks (aka tea, soda, etc)
    for row in drinks_list:
      unique_food_item_types.add(row['Food_Item_Type'])

    current_row = 0
    # go through the loop and make a label for each group type
    for food_item_type in unique_food_item_types:
      
      current_col = 0
      row_panel = DataRowPanel()
      label = Label(text=food_item_type)
      row_panel.add_component(label)
      row_panel.border = "1px solid #888888"
      row_panel.background = "#ffffff"
      self.drink_menu.add_component(row_panel, row=current_row, column=current_col)
      
      specific_items = [row['Specific_Item'] for row in drinks_list 
                        if row['Food_Item_Type'] == food_item_type]

      max_columns = 4
      current_col = 0
      #put drinks of that type under the respective label
      for specific_item in specific_items:
        drinks_button = Button(text=specific_item)
        # add button interactions
        #drinks_button = add_event_handler('click', self.drinks_button_click)

        # ensure the buttons are spread amongst columns top_down
        if current_col < max_columns:
          row_panel.add_component(drinks_button, column= current_col)
          current_col = current_col +1
        else:
          #current_row = current_row +1
          current_col = 0
          row_panel.add_component(drinks_button, column=current_col)       

  
  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu.ORDER_NOW')
    pass
    
  #def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
  
    #alert(content = milk, title = "Item Quanity", large = False, buttons = [("-1", --milk),("+1",++milk)])
    #pass
