from anvil import *
import anvil.server

class MusicPlayer(MusicPlayerTemplate):

    def __init__(self, **properties):
        self.init_components(**properties)

    def button_1_click(self, **event_args):
        result = anvil.server.call('play_preselected_playlist', self.spotify, "spotify:playlist:7Gk8MHzbGL1dyrEpCM6jgB", shuffle=True)
        self.label_1.text = result

    def button_2_click(self, **event_args):
        result = anvil.server.call('play_preselected_playlist', self.spotify, "spotify:playlist:3P2XUd8YlIQYCA6rECPGeN", shuffle=True)
        self.label_1.text = result

    def button_3_click(self, **event_args):
        result = anvil.server.call('play_preselected_playlist', self.spotify, "spotify:playlist:2mQ7IDZLJWImfQ9uFLAdDF", shuffle=True)
        self.label_1.text = result

    def button_4_click(self, **event_args):
        action = alert("Enter the action (play/pause/next/previous):", title="Control Playback", buttons=['play', 'pause', 'next', 'previous'])
        result = anvil.server.call('control_playback', self.spotify, action)
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