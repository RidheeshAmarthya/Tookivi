# Tookivi: Game Engine with Real-Time Super-Resolution

Tookivi is a project built upon the Hazel game engine, incorporating significant modifications to enhance graphics output. The primary feature is a Python script that performs real-time super-resolution upscaling of the game's output resolution.

## Features

- **Real-Time Super-Resolution**: Python script for upscaling output resolution
- **Multiple Upscaling Methods**: Nearest neighbor, median, and neural network-based approaches
- **Dynamic FPS Display**: Shows current frames per second and selected upscaling method
- **Adjustable Settings**: On-the-fly changes to resolution, window size, and position

## Requirements
- Python 3.x
- TensorFlow
- OpenCV (cv2)
- NumPy
- Pillow (PIL)
- MSS
- Win32GUI (for Windows)

## Installation

1. Clone the Tookivi repository: `git clone https://github.com/RidheeshAmarthya/Tookivi.git`
2. Install required Python packages: `pip install tensorflow numpy opencv-python mss pillow pywin32`

## Usage

1. **Start the Hazel Game Engine**:
   - Run the game engine

2. **Launch the Tookivi Python Script**:
   - Navigate to the Tookivi directory
   - Run the script: `python tookivi_upscaler.py`

3. **Controls**:
   - `0`: Toggle between upscaling methods (Normal, Median, Neural Network)
   - `1`: Set resolution to 1x1
   - `2`: Set resolution to 2x2
   - `r`: Toggle resize mode
   - `w/a/s/d`: Adjust window position
   - `i/j/k/l`: Adjust window size
   - `q`: Quit the application

## How It Works

1. The script captures the game window using Windows API calls
2. The captured image is processed and upscaled using one of three methods:
   - Nearest neighbor interpolation
   - Median-based super-resolution (RTSR_MEDIAN model)
   - Neural network-based super-resolution (RTSR_NEAREST model)
3. The upscaled image is displayed in a separate window with real-time FPS information

## Important Notes

- Ensure the game window is active when starting the script
- The script is designed for Windows and uses Windows-specific libraries
- Performance may vary based on your hardware capabilities

## Troubleshooting

- If the window capture fails, try running the game in windowed mode
- Adjust the `FPS` variable in the script if experiencing performance issues

## Contributing

Contributions to Tookivi are welcome. Please fork the repository and submit a pull request with your changes.

## Acknowledgments

- Hazel Game Engine developers
- TensorFlow and OpenCV communities
