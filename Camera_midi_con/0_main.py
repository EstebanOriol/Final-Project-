import wx

from app.ui import CameraMidiApp

if __name__ == "__main__":
    app = wx.App(False)
    frame = CameraMidiApp(None, title="Camera MIDI Controller")
    frame.Show()
    app.MainLoop()