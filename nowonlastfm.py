"""
	Usage: /listening
	Description: Tries to tell the channel what you're currently scrobbling on LastFM
	Creator: isomer <https://github.com/unrar>
	License: TPOL <https://bit.ly/tpolterms>
"""

import hexchat
import pylast
import os
import time

__module_name__ = "NowOnLastFM"
__module_version__ = "1.1.2"
__module_description__ = "Lets everyone know what you're scrobbling on LastFM"

# These API keys should remain unchanged; you only need to modify the USERNAME
API_KEY = "f7ecb9e71532280168393c165e7748a6"
API_SECRET = "98c2c83a6fec31fb47a947b4a8cb6a3e"
SESSION_KEY_FILE = os.path.join(os.path.expanduser("~"), ".session_key")

# Change this with your username.
USERNAME = "joszaynka" 

# Connect to the LastFM API via my application
network = pylast.LastFMNetwork(API_KEY, API_SECRET)

# On the first use, the user needs to authorize this application onto their account

if not os.path.exists(SESSION_KEY_FILE):
  skg = pylast.SessionKeyGenerator(network)
  url = skg.get_web_auth_url()

  hexchat.prnt("Please authorise the scrobbler: %s" % url)
  import webbrowser
  webbrowser.open(url)

  while True:
    try:
      session_key = skg.get_web_auth_session_key(url)
      fp = open(SESSION_KEY_FILE, "w")
      fp.write(session_key)
      fp.close()
      break
    except pylast.WSError:
      time.sleep(1)
else:
  session_key = open(SESSION_KEY_FILE).read()

# Now the user's been identified, so we have a session key
network.session_key = session_key
user = network.get_user(USERNAME)

# Now we just need to get the song
def get_song(word, word_eol, userdata):
  try:
    track = user.get_now_playing()
    hexchat.command('me is listening to ' + str(track.title) + ' by ' + str(track.artist) + '.')
  except:
    hexchat.prnt("Ground control to Major Tom, something's gone wrong! Are you sure you're scrobbling to lastfm?")
  return hexchat.EAT_ALL

# We also want to make it unload nicely
def unload_mod(userdata):
  print(__module_name__ + ' version ' + __module_version__ + ' unloaded. Come back soon!')

# Now we just need to hook this to Hexchat.
hexchat.hook_command('listening', get_song, help='Use /listening with no arguments')
hexchat.hook_unload(unload_mod)
print(__module_name__ + ' version ' + __module_version__ + ' loaded. Start scrobbling and type /listening on a channel :)')
