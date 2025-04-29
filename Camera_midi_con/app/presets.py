import json
import os

class PresetManager:
    def __init__(self, preset_folder="assets/presets"):
        self.preset_folder = preset_folder
        if not os.path.exists(self.preset_folder):
            os.makedirs(self.preset_folder)

    def save_preset(self, settings, preset_name="default"):
        """Save the current settings to a preset file."""
        with open(os.path.join(self.preset_folder, f"{preset_name}.json"), "w") as f:
            json.dump(settings, f)

    def load_preset(self, preset_name="default"):
        """Load settings from a preset file."""
        preset_path = os.path.join(self.preset_folder, f"{preset_name}.json")
        if os.path.exists(preset_path):
            with open(preset_path, "r") as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"Preset '{preset_name}' not found.")


