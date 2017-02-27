# Now on LastFM 🎧

*NowOnLastFM* is a Python plug-in for Hexchat. Using the Hexchat wrapper for Python and the [pylast](https://github.com/pylast/pylast) fabulous library of tools to plug into the LastFM (and other similar services) API in a very easy way. 💖

Once you've configured and authorized the plugin for your LastFM account (running `/fmlogin <username>`), you'll be the coolest guy in the room. Whenever a cool song pops up, let everyone know you're listening to it by typing:

    /listening

No need to depend on network-side bots! 😜

## Dependencies and technical details

This has been written using Python 2, because Hexchat probably handles it better (I use it on OS X, via brew). Like mentioned above, you're going to need to install `pylast`. It's easily done as it's on pip, but the exact command depends on your Python setup. Generally, this will work:

```bash
$ sudo pip install pylast
```

If you can't figure it out, check out [pylast](https://github.com/pylast/pylast)'s GitHub repo for more info on how to get it. I believe you can also use `easy_install` - I personally had to install pip via `easy_install` but maybe I could've downloaded `pylast` straight from it. 🤔

Other than that, the Hexchat python library should already be installed and ready to use.

## Logging in, simpler than ever 🔐

You just need to download (as ZIP) or clone the plugin into whichever folder you want:

    $ git clone https://github.com/unrar/nowonlastfm

As of `v1.2.0`, you don't need to touch the code anymore! All you need to do to authenticate yourself, is run the `fmlogin` command:

    /fmlogin <username>

That should be it! It needs to be your username, because when you run this command you will be prompted to your browser in order to, being logged into that username, give permission for the plugin to access your account. Don't worry, it only allows to see your profile and your scrobbles; in order to change anything, your password would be required to use the API.

So that's pretty much it! Now just open Hexchat, and depending on your OS, find something like `File > Load plugin or script...` and browse to the folder named `nowonlastfm` where you downloaded the source, `nowonlastfm.py`. 

If you experience any problems, please get in touch with me! 💌

**NOTE**: This is obvious, but you need to be using a scrobbler so that you're sending LastFM information about the track you're playing.