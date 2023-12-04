from ._anvil_designer import MusicPlayerTemplate
from anvil import *

class MusicPlayer(MusicPlayerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu.ORDER_NOW.Create_A_Pizza')
    pass
  

  def slider_1_change(self, **event_args):
    self.label_4.text = self.slider_1.level

  def slider_2_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_3.text = self.slider_2.level

  def reset_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.slider_1.level = 1
    self.slider_2.level = 1
    self.label_4.text = 1
    self.label_3.text = 1

  def button_12_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass



 