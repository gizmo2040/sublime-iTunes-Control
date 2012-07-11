import sys, sublime, sublime_plugin
from optparse import OptionParser

platform = sys.platform

if platform == "win32":
    import win32com.client
    iTunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")
else:
    from Foundation import *
    from ScriptingBridge import *
    iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")


#mute, nextTrack name pause playpause previousTack resume setSoundVolume_ setFixedIndexing_ setFrontmost_ visuals windows


class itunes_next(sublime_plugin.TextCommand):
    def run(self, edit):
        if platform == "win32":
             iTunes.NextTrack()
        else:
             iTunes.nextTrack()

class itunes_previous(sublime_plugin.TextCommand):
    def run(self, edit):
        if platform == "win32":
             iTunes.PreviousTrack()
        else:
             iTunes.previousTrack()

class itunes_pause(sublime_plugin.TextCommand):
    def run(self, edit):
        if platform == "win32":
             iTunes.Playpause()
        else:
             iTunes.playpause()