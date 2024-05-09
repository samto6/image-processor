# Image Processor

A simple drag-and-drop image processor built using wxPython and Pillow. It allows you to resize images and remove metadata while specifying JPEG quality through a simple GUI.

## Features
- Drag-and-drop image files to process them.
- Optionally resize images to specified dimensions.
- Remove image metadata by converting to RGB.
- Adjust JPEG quality using a slider.
- Process multiple images at once.

## Requirements
- Python 3.x
- wxPython
- Pillow

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/samto6/image-processor.git
    cd image-processor
    ```

2. Install the dependencies:

    ```bash
    pip install wxPython Pillow
    ```

## Usage
1. Run the application:

    ```bash
    python image_processor.py
    ```

2. Drag and drop image files onto the window to process them.

3. Adjust the following options:
   - **JPEG Quality:** Use the slider to specify JPEG quality (0-100).
   - **Resize Image?:** Check this box to enable resizing.
     - **Resize Width:** Enter the desired width.
     - **Resize Height:** Enter the desired height.

4. Click "OK" on the success message box when processing is complete.

## Code Explanation
### `Mywin` Class
- **`on_resize_check`**: Shows or hides the resize options based on the checkbox state.
- **`on_close_window`**: Closes the application window.

### `MyFileDropTarget` Class
- **`OnDropFiles`**: Handles dropped files and processes each image:
  - Converts to RGB to remove metadata.
  - Optionally resizes images.
  - Saves images with a specified JPEG quality.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
