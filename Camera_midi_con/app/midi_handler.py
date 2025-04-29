import mido
import threading

class MidiHandler:
    def __init__(self):
        self.midi_input = None

    def get_input_ports(self):
        """Get a list of available MIDI input ports."""
        return mido.get_input_names()
    
    def set_input_port(self, port_name):
        if self.midi_input:
            self.midi_input.close()
        self.midi_input = mido.open_input(port_name)
        threading.Thread(target = self.listen_to_midi, daemon=True).start()

    def listen_to_midi(self):
        for msg in self.midi_input:
            print(f"Recieved MIDI Control Change: {msg.control} {msg.value}")
            