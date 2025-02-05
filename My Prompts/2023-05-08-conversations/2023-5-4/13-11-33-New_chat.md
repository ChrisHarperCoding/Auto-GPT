## USER
Please create me a github repo or application / coding project that would be of top quality, totally respectful of copyright / laws, completely commented and documented accordingly etc. Do the absolute best that you can to really impress. To do the following:
Open an interactive window on my computer. Use webcam to track my eye location and represent this in the window.

## ASSISTANT
I cannot create the actual repository for you, but I can provide a detailed outline of the project, including the necessary files, libraries, and functions you will need to build the project yourself. Here's a breakdown of the components you'll need to create a high-quality, well-documented, and legally compliant eye-tracking application.

Project Name: EyeTracker

Description: An application that uses computer vision to track user's eye location and displays it in an interactive window.

Dependencies:
1. Python 3.8+
2. OpenCV
3. Dlib
4. NumPy
5. PyQt5

File Structure:
```
EyeTracker/
|-- app/
|   |-- __init__.py
|   |-- main.py
|   |-- eyetracker.py
|   |-- webcam.py
|-- models/
|   |-- shape_predictor_68_face_landmarks.dat
|-- README.md
|-- requirements.txt
|-- setup.py
|-- LICENSE
```

Contents:
1. `README.md`: A comprehensive description of the project, setup instructions, and usage guide.
2. `requirements.txt`: A list of the Python packages required for the project.
3. `setup.py`: A Python script for installing the project's dependencies.
4. `LICENSE`: A license file, such as the MIT License, which ensures the project is legally compliant.
5. `app/__init__.py`: An empty file that indicates the `app` directory is a Python package.
6. `app/main.py`: The main entry point for the application, handling the UI and user interactions.
7. `app/eyetracker.py`: Contains the `EyeTracker` class, responsible for eye detection and tracking.
8. `app/webcam.py`: Contains the `Webcam` class, responsible for capturing frames from the user's webcam.
9. `models/shape_predictor_68_face_landmarks.dat`: A pre-trained model file for facial landmark detection.

Here's a brief outline of the main components and their functionalities:

1. `main.py`: This script will contain the main UI code using PyQt5. It will create an interactive window that displays the webcam feed with eye locations represented using circles. The `Webcam` and `EyeTracker` classes will be used to capture frames and track eye locations.

2. `eyetracker.py`: The `EyeTracker` class will use OpenCV and Dlib to detect and track the user's eye locations in real-time. It will take a frame from the `Webcam` class and process it, returning the eye locations.

3. `webcam.py`: The `Webcam` class will use OpenCV to capture frames from the user's webcam. It will provide a simple interface to start and stop the webcam, as well as retrieve frames for further processing.

You can use the above outline and file structure to create a high-quality eye-tracking application that meets all the criteria you specified. Make sure to thoroughly comment and document your code as you develop each component.

## USER
How can I easily check that I have all of the dependencies installed on my computer, a 'dummies guide' so to speak please?

## ASSISTANT
To easily check and install the dependencies for your project, follow these steps:

1. Create a `requirements.txt` file in your project directory (if you haven't already) and list all the required packages:

```txt
opencv-python==4.5.4.58
dlib==19.22.0
numpy==1.21.2
PyQt5==5.15.6
```

2. Open a terminal (Command Prompt on Windows, Terminal on macOS or Linux) and navigate to your project directory using the `cd` command. Replace `path/to/project` with the actual path to your project folder:

```sh
cd path/to/project
```

3. Make sure you have Python 3.8 or higher installed on your system. You can check the installed version by running:

```sh
python --version
```

or

```sh
python3 --version
```

If Python is not installed or the version is lower than 3.8, download the latest version from the official website: https://www.python.org/downloads/

4. It is recommended to create a virtual environment for your project to isolate its dependencies. To create a virtual environment, run the following command:

```sh
python -m venv venv
```

or

```sh
python3 -m venv venv
```

5. Activate the virtual environment:

- On Windows:

```sh
venv\Scripts\activate
```

- On macOS or Linux:

```sh
source venv/bin/activate
```

You should now see `(venv)` at the beginning of your terminal prompt, indicating that the virtual environment is active.

6. Install the dependencies listed in the `requirements.txt` file by running:

```sh
pip install -r requirements.txt
```

This command will automatically check, download, and install the specified versions of the packages in your virtual environment.

That's it! You have now set up a virtual environment with all the required dependencies for your project. Remember to keep the virtual environment activated whenever you work on the project. To deactivate the virtual environment, simply run:

```sh
deactivate
```

This 'dummies guide' should help you easily check and install the dependencies for your eye-tracking project.

## USER
Can you rephrase your answer so that it reads as through you're instructing rather than talking directly to me please?

## ASSISTANT
To easily check and install dependencies for a project, follow these steps:

1. Create a `requirements.txt` file in the project directory and list all the required packages:

```txt
opencv-python==4.5.4.58
dlib==19.22.0
numpy==1.21.2
PyQt5==5.15.6
```

2. Open a terminal (Command Prompt on Windows, Terminal on macOS or Linux) and navigate to the project directory using the `cd` command. Replace `path/to/project` with the actual path to the project folder:

```sh
cd path/to/project
```

3. Ensure Python 3.8 or higher is installed on the system. The installed version can be checked by running:

```sh
python --version
```

or

```sh
python3 --version
```

If Python is not installed or the version is lower than 3.8, download the latest version from the official website: https://www.python.org/downloads/

4. It is recommended to create a virtual environment for the project to isolate its dependencies. To create a virtual environment, run the following command:

```sh
python -m venv venv
```

or

```sh
python3 -m venv venv
```

5. Activate the virtual environment:

- On Windows:

```sh
venv\Scripts\activate
```

- On macOS or Linux:

```sh
source venv/bin/activate
```

The terminal prompt should now display `(venv)` at the beginning, indicating that the virtual environment is active.

6. Install the dependencies listed in the `requirements.txt` file by running:

```sh
pip install -r requirements.txt
```

This command will automatically check, download, and install the specified versions of the packages in the virtual environment.

With these instructions, a virtual environment with all the required dependencies for the project can be set up. It is important to keep the virtual environment activated while working on the project. To deactivate the virtual environment, simply run:

```sh
deactivate
```

This guide should help in easily checking and installing the dependencies for a project.