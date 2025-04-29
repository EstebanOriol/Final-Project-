import cv2

class CameraHandler:
    def __init__(self):
        self.current_filter = None
        self.current_intensity = 0
        self.cap = cv2.VideoCapture(0)  # Open the default camera
        self.is_recording = False
        self.video_writer = None

    def get_available_filters(self):
        return ["None", "Grayscale", "Invert"]

    def set_filter(self, filter_name):
        self.current_filter = filter_name

    def set_filter_intensity(self, intensity):
        self.current_intensity = intensity

    def get_current_settings(self):
        """Return the current filter settings."""
        return {
            "filter": self.current_filter,
            "intensity": self.current_intensity
        }

    def apply_settings(self, settings):
        """Apply the given filter settings."""
        self.set_filter(settings.get("filter", "None"))
        self.set_filter_intensity(settings.get("intensity", 0))

    def apply_filter(self, frame):
        """Apply the selected filter to the frame."""
        if self.current_filter == "Grayscale":
            return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif self.current_filter == "Invert":
            return cv2.bitwise_not(frame)
        return frame

    def start_recording(self, output_file="output.avi"):
        """Start recording video."""
        if not self.cap.isOpened():
            print("Camera is not opened.")
            return

        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        fps = int(self.cap.get(cv2.CAP_PROP_FPS)) or 30
        frame_size = (
            int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        )
        self.video_writer = cv2.VideoWriter(output_file, fourcc, fps, frame_size)
        self.is_recording = True
        print("Recording started.")

    def stop_recording(self):
        """Stop recording video."""
        if self.is_recording:
            self.is_recording = False
            self.video_writer.release()
            print("Recording stopped.")

    def capture_frame(self):
        """Capture a frame from the camera."""
        if not self.cap.isOpened():
            print("Camera is not opened.")
            return None

        ret, frame = self.cap.read()
        if not ret:
            print("Failed to capture frame.")
            return None

        # Apply the selected filter
        frame = self.apply_filter(frame)

        # Write the frame to the video file if recording
        if self.is_recording and self.video_writer:
            self.video_writer.write(frame)

        return frame

    def release_camera(self):
        """Release the camera and video writer."""
        if self.cap.isOpened():
            self.cap.release()
        if self.video_writer:

            self.video_writer.release()

