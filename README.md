# ASCII Nova - Real-Time ASCII Video Player

**ASCII Nova** being a hobby project is an innovative tool/app that converts video frames into ASCII art in real-time and provides an interactive video playback experience with a graphical user interface. This project demonstrates the use of computer vision, image processing, and GUI development in Python.

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


## Reproducibility

The code is organized and well-documented to ensure clarity and ease of use. Key aspects include:

- **Logical Structure**: The project is structured to facilitate understanding and ease of navigation. Each module is purposefully designed to handle specific functionalities such as video playback, frame extraction, and ASCII rendering.

- **Comprehensive Comments**: Detailed comments and docstrings are included throughout the code. These comments explain the purpose of classes, methods, and key sections of the code, making it easier for others to follow and modify as needed.

- **Dependencies**: A `requirements.txt` file is provided to list all necessary Python libraries. This ensures that all dependencies can be easily installed and that the environment is correctly set up. You can install the required libraries using:

  ```bash
  pip install -r requirements.txt
  ```

- **Usage Instructions**: Clear instructions on how to run the code and utilize the main features are provided in the README. This includes setting up the environment, running the real-time ASCII player, and rendering video to ASCII.

- **Code Examples**: Examples of how to use key functions and classes are included in the README. These examples demonstrate how to initialize and use the `RealTimeAsciiVideoPlayer`, `VideoObject`, and other utility functions.

- **Data and Resources**: Instructions for setting up necessary data and resources (e.g., fonts and videos) are included to ensure that users can reproduce the results without missing components.

- **Testing and Validation**: The code includes built-in mechanisms to handle common errors and edge cases, such as invalid file paths and missing resources. For further validation, test cases can be added to ensure the functionality remains intact with future updates.

By following these guidelines and utilizing the provided documentation, users should be able to reproduce the results and understand the workings of the project with minimal effort.

Still, feel lost? Create an issue, I'll help.

## TODO

If you can create an executable(.exe) for this project, that'll be cool. Features that I missed can be added.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for bug fixes, features, or improvements. Make sure to follow the coding guidelines for new features.

## License

This project is licensed under the MIT License.

## Acknowledgement

Thanks to https://github.com/cosmologicon/pygame-text project for ptext code that served a major function in this developing ascii player functionality.
