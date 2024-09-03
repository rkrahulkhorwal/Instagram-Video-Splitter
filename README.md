# Instagram Video Splitter

This Python script takes a long video file and splits it into multiple 30-second clips suitable for Instagram posts. It also adds a custom caption to each clip, fits the video into a 9:16 aspect ratio (1080x1920 pixels), and ensures the entire original video content is visible.

## Features

- Splits long videos into 30-second clips
- Fits videos to 9:16 aspect ratio (1080x1920 pixels) without cropping
- Adds black bars to maintain aspect ratio if needed
- Adds a custom caption to each clip
- Uses Mulish font for captions (falls back to default if not available)
- Centers captions in a black box at the top of each clip

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/rkrahulkhorwal/instagram-video-splitter.git
   cd instagram-video-splitter
   ```

2. Install the required Python packages:
   ```
   pip install moviepy numpy Pillow
   ```

3. Download the Mulish-Bold.ttf font file and place it in the same directory as the script. You can download it from [Google Fonts](https://fonts.google.com/specimen/Mulish).

## Usage

1. Place your input video file in a known location.

2. Open the script `instagram_video_splitter.py` and modify the following lines at the bottom of the file:

   ```python
   input_video = "path/to/your/video.mp4"
   output_folder = "path/to/output/folder"
   split_video_for_instagram(input_video, output_folder)
   ```

   Replace `"path/to/your/video.mp4"` with the path to your input video file, and `"path/to/output/folder"` with the path where you want the output clips to be saved.

3. Run the script:
   ```
   python instagram_video_splitter.py
   ```

4. The script will process your video and save the output clips in the specified output folder. Each clip will be named `[original_filename]_part_[number].mp4`.

## Customization

- To change the clip duration, modify the `clip_duration` parameter in the `split_video_for_instagram` function call.
- To adjust the font size or caption box height, modify the corresponding values in the `add_caption_to_frame` function.

## Contributing

Contributions to the Instagram Video Splitter are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [MoviePy](https://zulko.github.io/moviepy/) for video processing
- [Pillow](https://python-pillow.org/) for image manipulation
- [Mulish font](https://fonts.google.com/specimen/Mulish) by Vernon Adams
