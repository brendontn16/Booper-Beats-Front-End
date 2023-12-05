from ._anvil_designer import BeveragesTemplate
from anvil import *
import anvil.server


class Beverages(BeveragesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu.ORDER_NOW')
    pass
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
  
    alert(content = milk, title = "Item Quanity", large = False, buttons = [("-1", --milk),("+1",++milk)])
    pass
