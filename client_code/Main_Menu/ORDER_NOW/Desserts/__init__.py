from ._anvil_designer import DessertsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Desserts(DessertsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu.ORDER_NOW')
    pass
