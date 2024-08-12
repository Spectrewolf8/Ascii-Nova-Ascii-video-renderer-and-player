# ASCII Nova - Real-Time ASCII Video Player

**ASCII Nova** is an innovative tool that converts video frames into ASCII art in real-time and provides an interactive video playback experience with a graphical user interface. This project demonstrates the use of computer vision, image processing, and GUI development in Python.

## Project Overview

ASCII Nova is designed to convert video content into ASCII art and provide a dynamic and interactive playback experience. It includes tools for real-time playback, rendering video to ASCII, and handling audio extraction.

## Features

- Real-time ASCII art video playback with GUI
- Frame-by-frame video processing to ASCII art
- Audio extraction and encoding in base64 format
- JSON GZIP compression for video and audio data

## Installation

To set up the project, you need Python 3.x and several libraries. Follow the steps below:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Spectrewolf8/Ascii-Nova-Ascii-video-renderer-and-player.git
   cd ascii-nova
   ```

2. **Create and activate a virtual environment:**

   ```bash
    pipenv shell
   ```

3. **Install required dependencies(any method):**

   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   pipenv install
   ```

4. **Download and set up additional resources:**
   - Download fonts preffered for rendering and place them in the `fonts_dir` directory.
   - Ensure the `compress_json` module is available, or install it if necessary.

## Usage

### Running the app.py

Self explanatory screens attached:

Home screen[1]
![image](https://github.com/user-attachments/assets/55318dc4-ca94-4f8e-a3bd-1e0c8ab4b43b)

Player Screen[2]
![image](https://github.com/user-attachments/assets/40bba8bc-08c9-4a5b-abbb-6609638328ed)
![image](https://github.com/user-attachments/assets/a4786b96-d6cd-4185-ae75-c88864e31162)


Converter Screen[3]
![image](https://github.com/user-attachments/assets/a6c96885-0afc-4af0-8791-b74dd71bb0df)

Realtime player screen[4]
![image](https://github.com/user-attachments/assets/7b85619f-4261-4dcc-ad4c-d607026e803b)
![image](https://github.com/user-attachments/assets/2b84b0e1-452d-4c67-8b07-715640a3b36c)


Help screen[5]
![image](https://github.com/user-attachments/assets/2889813c-6c6a-4dcf-afd3-7f2c0334390d)


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for bug fixes, features, or improvements. Make sure to follow the coding guidelines for new features.

## License

This project is licensed under the MIT License.

## Acknowledgement

Thanks to https://github.com/cosmologicon/pygame-text project for ptext code that served a major function in this developing ascii player functionality.
