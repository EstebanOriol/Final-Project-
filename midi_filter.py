import cv2
import numpy as np
import mido

# Initialize the camera
cap = cv2.VideoCapture(0)

print("Available MIDI input devices:")
for name in mido.get_input_names():
    print(f"- {name}")
# Initialize MIDI input
print ("What input device do you want to use?")
midi_input_name = input("Enter the name of the MIDI input device: ")
midi_input = mido.open_input(midi_input_name)  # Automatically selects the first available MIDI input

# Variable to store brightness level (default is 1.0, no change)
brightness = 2.0

def adjust_brightness(frame, brightness):
    """Adjust the brightness of the frame."""
    return cv2.convertScaleAbs(frame, alpha=brightness, beta=0)

while True:
    # Read MIDI messages
    for msg in midi_input.iter_pending():
        if msg.type == 'control_change':  # Check for MIDI control change messages
            # Map the MIDI control value (0-127) to a brightness range (0.5 to 2.0)
            if msg.type == 'note_on' and msg.velocity > 0:  # Note on with velocity
                brightness = 0.5 + (msg.velocity / 127) * 1.5
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):  # Note off or note on with zero velocity
                brightness = 0.5  # Reset brightness to default
            print(f"Brightness adjusted to: {brightness}")

    # Capture a frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Adjust the brightness of the frame
    frame = adjust_brightness(frame, brightness)

    # Display the frame
    cv2.imshow('frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()