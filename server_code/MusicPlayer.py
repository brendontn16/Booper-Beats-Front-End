import spotipy
import anvil.server
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "0d0fa1cb002742e2af55ffc57265278f"
CLIENT_SECRET = "86588df1a2924918b37a6ab61dd72002"
REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "user-library-read user-read-playback-state user-modify-playback-state playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public"

@anvil.server.callable
def authenticate_spotify():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))

@anvil.server.callable
def play_preselected_playlist(sp, playlist_uri, shuffle=False):
    try:
        sp.start_playback(context_uri=playlist_uri)
        return f"Playback started for playlist: {playlist_uri}"

        if shuffle:
            sp.shuffle(state=True)
            return "Shuffle play enabled."
    except spotipy.SpotifyException as e:
        return f"Error starting playback: {e}"

@anvil.server.callable
def control_playback(sp, action):
    if action == 'play':
        sp.start_playback()
    elif action == 'pause':
        sp.pause_playback()
    elif action == 'next':
        sp.next_track()
    elif action == 'previous':
        sp.previous_track()
    else:
        return "Invalid action. Please enter play/pause/next/previous."

@anvil.server.callable
def search_and_add_to_playlist(sp, playlist_uri, query):
    results = sp.search(q=query, type='track', limit=10)
    tracks = results['tracks']['items']

    if not tracks:
        return "No tracks found."

    return tracks

@anvil.server.callable
def select_track_from_results(tracks, index):
    if 0 <= index < len(tracks):
        selected_track = tracks[index]
        track_uri = selected_track['uri']
        return track_uri
    else:
        return "Invalid track index."