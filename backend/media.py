import sys
import spotipy
import spotipy.util as util

scope = 'streaming user-read-private user-library-modify user-read-playback-state user-top-read user-read-currently-playing user-modify-playback-state'
token = False
spotify = None

def getActiveDevice():
    global spotify
    devices = spotify.devices()
    print(len(devices))
    print("dic", devices)
    for device_list in devices.values():
        print(len(device_list))
        if len(device_list) == 0:
            raise ValueError("No devices available")
        for device in device_list:
            if (device['is_active']):
                return device['id']
def logIn():
    # username = 'andrewkurniawan'
    username = input("Enter Spotify Username:")
    print("The username received was:", username)
    global token, spotify
    token = util.prompt_for_user_token(username, scope=scope,
                                       client_id='cc4b59d921b646e2a2a55fe4c409e8ab',
                                       client_secret='0568ba6224d846acaa1969dd646f25f1',
                                       redirect_uri='http://localhost:8888/callback2/')
    print("Token is valid:", token)
    if token:
        spotify = spotipy.Spotify(auth=token)
        spotify.pause_playback(getActiveDevice())
    else:
        print("Can't get token for", username)

# def playbackButtons(cmd):
#     if cmd == 'play':
#     elif cmd == 'pause':

logIn()



