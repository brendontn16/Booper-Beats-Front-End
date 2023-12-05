from ._anvil_designer import MusicPlayerTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.js.window import jQuery
from anvil.js import get_dom_node


class MusicPlayer(MusicPlayerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def card_9_show(self, **event_args):
    self.card_9.visible = True
    """This method is called when the column panel is shown on the screen"""
    pass
  def card_9_hide(self, **event_args):
    """This method is called when the column panel is removed from the screen"""
    self.card_9.visible = False
    pass

  def card_8_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    self.card_8.visible = True
    pass

  def card_8_hide(self, **event_args):
    self.card_8.visible = False
    """This method is called when the column panel is removed from the screen"""
    pass
    
  def card_7_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    self.card_7.visible = True
    pass

  def card_7_hide(self, **event_args):
    self.card_7.visible = False
    """This method is called when the column panel is removed from the screen"""
    pass
    

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu.ORDER_NOW.Create_A_Pizza')
    pass
    
  


  def reset_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu')
    pass
    def button_playlist1(self, **event_args):
        result = anvil.server.call('play_preselected_playlist', self.spotify, "spotify:playlist:7Gk8MHzbGL1dyrEpCM6jgB", shuffle=True)
        self.label_1.text = result

    def button_playlist2(self, **event_args):
        result = anvil.server.call('play_preselected_playlist', self.spotify, "spotify:playlist:3P2XUd8YlIQYCA6rECPGeN", shuffle=True)
        self.label_1.text = result
  def button_12_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.card_9_hide()
    self.card_7_hide()
    self.card_8_show()
    pass

  def button_13_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.card_9_show()
    self.card_8_hide()
    self.card_7_hide()
    pass

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.card_7_show()
    self.card_8_hide()
    self.card_9_hide()
    pass

  def button_14_click(self, **event_args):
    self.card_7_show()
    self.card_8_show()
    self.card_9_show()
    """This method is called when the button is clicked"""
    pass

  def Music_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass


    def button_playlist3(self, **event_args):
        result = anvil.server.call('play_preselected_playlist', self.spotify, "spotify:playlist:2mQ7IDZLJWImfQ9uFLAdDF", shuffle=True)
        self.label_1.text = result

    def __init__(self, **properties):
        self.init_components(**properties)
        self.playback_state = 'play'  # Initial state is play

    def button_play_pause_click(self, **event_args):
        # Toggle between play and pause
        if self.playback_state == 'play':
            result = anvil.server.call('control_playback', self.spotify, 'play')
            self.playback_state = 'pause'
        else:
            result = anvil.server.call('control_playback', self.spotify, 'pause')
            self.playback_state = 'play'

        self.label_1.text = result

    def button_next_click(self, **event_args):
        result = anvil.server.call('control_playback', self.spotify, 'next')
        self.label_1.text = result

    def button_previous_click(self, **event_args):
        result = anvil.server.call('control_playback', self.spotify, 'previous')
        self.label_1.text = result

    def button_5_click(self, **event_args):
        query = alert("Enter the track name:", title="Search and Add to Playlist 3")
        results = anvil.server.call('search_and_add_to_playlist', self.spotify, "spotify:playlist:2mQ7IDZLJWImfQ9uFLAdDF", query)
        if isinstance(results, list):
            index = alert("Select a track:", title="Search Results", buttons=[str(i + 1) for i in range(len(results))])
            track_uri = anvil.server.call('select_track_from_results', results, int(index) - 1)
            self.label_1.text = track_uri
        else:
            self.label_1.text = results
          
    def button_6_click(self, **event_args):
        self.close()

  def button_Search_click(self, **event_args):
    """This method is called when the button is clicked"""
    iframe = jQuery("<iframe width='100%' height='800px'>").attr("src","http://127.0.0.1:5000/")
    iframe.appendTo(get_dom_node(self.content_panel))
    pass

  def back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main_Menu')
    pass
