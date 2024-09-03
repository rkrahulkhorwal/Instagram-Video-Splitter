import os
import numpy as np
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, vfx
from PIL import Image, ImageDraw, ImageFont
import textwrap

def resize_frame(image, newsize):
    pil_image = Image.fromarray(image)
    resized_image = pil_image.resize(newsize, Image.LANCZOS)
    return np.array(resized_image)

def fit_video_to_aspect_ratio(video, target_width, target_height):
    target_ratio = target_height / target_width
    video_ratio = video.h / video.w

    if video_ratio > target_ratio:
        new_height = target_height
        new_width = int(target_height / video_ratio)
    else:
        new_width = target_width
        new_height = int(target_width * video_ratio)

    resized_video = video.fl_image(lambda image: resize_frame(image, (new_width, new_height)))
    
    background = ColorClip(size=(target_width, target_height), color=(0, 0, 0))
    
    x_center = (target_width - new_width) // 2
    y_center = (target_height - new_height) // 2
    
    return CompositeVideoClip([background, resized_video.set_position((x_center, y_center))])

def add_caption_to_frame(image, caption):
    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)
    
    # Use Mulish font if available, otherwise use a default font
    try:
        font = ImageFont.truetype("Mulish-Bold.ttf", 60)
    except IOError:
        font = ImageFont.load_default().font_variant(size=60)
    
    # Set the height of the black box
    box_height = 150
    
    # Wrap text to fit within the image width
    max_width = pil_image.width - 40  # 20 pixels padding on each side
    wrapped_text = textwrap.fill(caption, width=30)  # Adjust width as needed
    
    # Get text size
    bbox = font.getbbox(wrapped_text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate position to center text in the black box
    text_x = (pil_image.width - text_width) // 2
    text_y = (box_height - text_height) // 2
    
    # Draw black box at the top
    draw.rectangle([(0, 0), (pil_image.width, box_height)], fill=(0, 0, 0))
    
    # Draw text
    draw.text((text_x, text_y), wrapped_text, font=font, fill=(255, 255, 255), align="center")
    
    return np.array(pil_image)

def split_video_for_instagram(input_file, output_folder, clip_duration=30):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video = VideoFileClip(input_file)
    video_name = os.path.splitext(os.path.basename(input_file))[0]

    target_width = 1080
    target_height = 1920

    fitted_video = fit_video_to_aspect_ratio(video, target_width, target_height)

    total_duration = video.duration
    num_clips = int(total_duration // clip_duration) + 1

    for i in range(num_clips):
        start_time = i * clip_duration
        end_time = min((i + 1) * clip_duration, total_duration)
        
        clip = fitted_video.subclip(start_time, end_time)
        
        caption_text = f"{video_name} Part {i+1}"
        
        # Add caption to each frame
        clip_with_caption = clip.fl_image(lambda img: add_caption_to_frame(img, caption_text))
        
        output_file = os.path.join(output_folder, f"{video_name}_part_{i+1}.mp4")
        clip_with_caption.write_videofile(output_file, codec="libx264", audio_codec="aac")

    video.close()
    fitted_video.close()

# Example usage
input_video = "Yeh Vaada Raha.mp4"
output_folder = "path/to/output/folder"
split_video_for_instagram(input_video, output_folder)
