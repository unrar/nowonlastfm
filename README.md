# Now on LastFM

*NowOnLastFM* is a Python plug-in for Hexchat. Using the Hexchat wrapper for Python and the [pylast](https://github.com/pylast/pylast) fabulous library of tools to plug into the LastFM (and other similar services) API in a very easy way.

## How to use?

For now, you need to manually change your username on the code - in further releases I'll try to make the authentication process a bit more separated, as in another command.

You just need to download (as ZIP) or clone the plugin into whichever folder you want:

    $ git clone https://github.com/unrar/nowonlastfm

And then edit the source file, `nowonlastfm.py`. Find line 24 and, if your username is `metalhead` you should replace it for:

```python
USERNAME = "metalhead"
```

That should be it! It needs to be your username, because when you first load the plugin into Hexchat you will be prompted to your browser in order to, being logged into that username, give permission for the plugin to access your account. Don't worry, it only allows to see your profile and your scrobbles; in order to change anything, your password would be required to use the API.

So that's pretty much it! Now just open Hexchat, and depending on your OS, find something like `File > Load plugin or script...` and browse to the folder named `nowonlastfm` where you downloaded and edited the source, `nowonlastfm.py`. 

If you experience any problems, please get in touch with me! 

**NOTE**: This is obvious, but you need to be using a scrobbler so that you're sending LastFM information about the track you're playing.