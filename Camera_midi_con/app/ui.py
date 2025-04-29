import wx
from app.midi_handler import MidiHandler
from app.audio_handler import AudioHandler
from app.camera_handler import CameraHandler
from app.presets import PresetManager
from threading import Thread

class CameraMidiApp(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 600))
        
        self.midi_handler = MidiHandler()
        self.audio_handler = AudioHandler()
        self.camera_handler = CameraHandler()
        self.preset_manager = PresetManager()

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # MIDI Devices
        midi_input_label = wx.StaticText(panel, label="MIDI Input Device:")
        self.midi_input_combo = wx.ComboBox(panel, choices=self.midi_handler.get_input_ports())
        self.midi_input_combo.Bind(wx.EVT_COMBOBOX, self.on_midi_input_selected)
        sizer.Add(midi_input_label, flag=wx.LEFT | wx.TOP, border=10)
        sizer.Add(self.midi_input_combo, flag=wx.LEFT | wx.EXPAND, border=10)

        # Filter Selection
        filter_label = wx.StaticText(panel, label="Camera Filter:")
        self.filter_combo = wx.ComboBox(panel, choices=self.camera_handler.get_available_filters())
        self.filter_combo.Bind(wx.EVT_COMBOBOX, self.on_filter_selected)
        sizer.Add(filter_label, flag=wx.LEFT | wx.TOP, border=10)
        sizer.Add(self.filter_combo, flag=wx.LEFT | wx.EXPAND, border=10)

        # Filter Intensity
        intensity_label = wx.StaticText(panel, label="Filter Intensity:")
        self.intensity_slider = wx.Slider(panel, value=0, minValue=0, maxValue=100)
        self.intensity_slider.Bind(wx.EVT_SLIDER, self.on_intensity_changed)
        sizer.Add(intensity_label, flag=wx.LEFT | wx.TOP, border=10)
        sizer.Add(self.intensity_slider, flag=wx.LEFT | wx.EXPAND, border=10)

        # Preset Buttons
        save_button = wx.Button(panel, label="Save Preset")
        save_button.Bind(wx.EVT_BUTTON, self.on_save_preset)
        load_button = wx.Button(panel, label="Load Preset")
        load_button.Bind(wx.EVT_BUTTON, self.on_load_preset)
        sizer.Add(save_button, flag=wx.LEFT | wx.TOP, border=10)
        sizer.Add(load_button, flag=wx.LEFT | wx.TOP, border=10)

        # Start Audio Stream
        self.audio_handler.start_audio_stream()

        # Timer for Audio-Based Intensity Adjustment
        self.audio_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_filter_intensity_from_audio, self.audio_timer)
        self.audio_timer.Start(100)  # Update every 100ms

        panel.SetSizer(sizer)

    def on_midi_input_selected(self, event):
        """Handle MIDI input device selection."""
        port_name = self.midi_input_combo.GetValue()
        self.midi_handler.set_input_port(port_name)

    def on_filter_selected(self, event):
        """Handle filter selection."""
        filter_name = self.filter_combo.GetValue()
        self.camera_handler.set_filter(filter_name)

    def on_intensity_changed(self, event):
        """Handle filter intensity changes."""
        intensity = self.intensity_slider.GetValue() / 100
        self.camera_handler.set_filter_intensity(intensity)

    def on_save_preset(self, event):
        """Save the current filter settings as a preset."""
        self.preset_manager.save_preset(self.camera_handler.get_current_settings())

    def on_load_preset(self, event):
        """Load a preset and apply its settings."""
        settings = self.preset_manager.load_preset("default")
        self.camera_handler.apply_settings(settings)
        # Update UI to reflect loaded settings
        self.filter_combo.SetValue(settings["filter"])
        self.intensity_slider.SetValue(int(settings["intensity"] * 100))

    def update_filter_intensity_from_audio(self, event):
        """Adjust filter intensity based on audio input."""
        audio_level = self.audio_handler.get_audio_level()
        self.camera_handler.set_filter_intensity(audio_level)
        self.intensity_slider.SetValue(int(audio_level * 100))

    def on_close(self, event):
        """Handle application close."""
        self.audio_timer.Stop()
        self.audio_handler.stop_audio_stream()
        self.Destroy()







