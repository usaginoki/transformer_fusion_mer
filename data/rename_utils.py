import os

ravdess_index = {
    "01": "Neutral",
    "02": "Neutral",
    "03": "Happy",
    "04": "Sad",
    "05": "Angry",
    "06": "Fear",
    "07": "Disgust",
    "08": "Surprise",
}


def rename_ravdess_files(directory_path):
    file_counter = 1

    for filename in os.listdir(directory_path):
        if filename.endswith((".mp4", ".wav")):  # Handle both video and audio files
            # Split the original filename by '-'
            parts = filename.split("-")

            if len(parts) == 7:  # Verify it's a RAVDESS filename
                emotion_code = parts[2]
                emotion = ravdess_index.get(emotion_code, "Unknown")

                # Get file extension
                extension = os.path.splitext(filename)[1]

                # Create new filename
                new_filename = f"RAVDESS_{file_counter:03d}_{emotion}{extension}"

                # Full paths for old and new files
                old_file = os.path.join(directory_path, filename)
                new_file = os.path.join(directory_path, new_filename)

                # Rename the file
                os.rename(old_file, new_file)
                file_counter += 1


if __name__ == "__main__":
    # Replace with your RAVDESS directory path
    directory_path = "path/to/your/ravdess/files"
    rename_ravdess_files(directory_path)
