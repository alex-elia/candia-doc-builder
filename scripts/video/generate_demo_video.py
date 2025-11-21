#!/usr/bin/env python3
"""
Generate software demo video from screenshots or diagrams
Example: Create demo video for Satellite AI prototype
"""

from moviepy.editor import ImageClip, concatenate_videoclips, TextClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
import os
import glob

def add_annotation_to_image(image_path, annotation_text, position=(50, 50)):
    """Add text annotation to image"""
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Try to load font, fallback to default
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    # Draw text with background
    bbox = draw.textbbox((0, 0), annotation_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Background rectangle
    draw.rectangle(
        [position[0]-10, position[1]-10, 
         position[0]+text_width+10, position[1]+text_height+10],
        fill=(0, 0, 0, 200)  # Semi-transparent black
    )
    
    # Text
    draw.text(position, annotation_text, fill=(255, 255, 255), font=font)
    
    # Save annotated image
    annotated_path = image_path.replace('.png', '_annotated.png').replace('.jpg', '_annotated.jpg')
    img.save(annotated_path)
    return annotated_path

def create_demo_video_from_images(image_dir="screenshots", output="demo.mp4", fps=2):
    """
    Create demo video from images
    
    Args:
        image_dir: Directory containing screenshots
        output: Output video filename
        fps: Frames per second (duration per image = 1/fps)
    """
    
    # Find all images
    image_extensions = ['*.png', '*.jpg', '*.jpeg']
    images = []
    for ext in image_extensions:
        images.extend(glob.glob(os.path.join(image_dir, ext)))
        images.extend(glob.glob(os.path.join(image_dir, ext.upper())))
    
    if not images:
        print(f"⚠️  No images found in {image_dir}")
        print(f"💡 Place screenshots in '{image_dir}/' directory")
        return None
    
    images.sort()  # Sort alphabetically
    print(f"📸 Found {len(images)} images")
    
    # Create clips
    clips = []
    for i, img_path in enumerate(images):
        print(f"  Processing: {os.path.basename(img_path)}")
        
        # Create image clip (2 seconds per image)
        img_clip = ImageClip(img_path).set_duration(2)
        
        # Resize if needed (optional)
        # img_clip = img_clip.resize((1920, 1080))
        
        # Add step number overlay
        step_text = f"Étape {i+1}/{len(images)}"
        txt_clip = TextClip(step_text,
                          fontsize=40,
                          color='white',
                          bg_color='black',
                          size=(300, 60),
                          method='caption')
        txt_clip = txt_clip.set_position(('right', 'top')).set_duration(2).set_start(0)
        
        # Combine image and text
        video = CompositeVideoClip([img_clip, txt_clip])
        clips.append(video)
    
    # Concatenate all clips
    print(f"\n🎬 Creating video from {len(clips)} clips...")
    final_video = concatenate_videoclips(clips, method="compose")
    
    # Export
    print(f"💾 Exporting to {output}...")
    final_video.write_videofile(output, fps=fps, codec='libx264', audio=False)
    
    print(f"✅ Video created: {output}")
    return final_video

def create_animated_diagram_video(diagrams_dir="diagrams", output="demo_animated.mp4"):
    """
    Create animated video from architecture diagrams
    Shows diagrams with transitions and annotations
    """
    
    # Find diagram images
    diagrams = glob.glob(os.path.join(diagrams_dir, "*.png"))
    diagrams.extend(glob.glob(os.path.join(diagrams_dir, "*.jpg")))
    
    if not diagrams:
        print(f"⚠️  No diagrams found in {diagrams_dir}")
        return None
    
    diagrams.sort()
    print(f"📊 Found {len(diagrams)} diagrams")
    
    clips = []
    for i, diagram_path in enumerate(diagrams):
        # Load diagram
        img_clip = ImageClip(diagram_path).set_duration(3)
        
        # Add title
        title = os.path.basename(diagram_path).replace('.png', '').replace('.jpg', '')
        title_clip = TextClip(title,
                            fontsize=50,
                            color='white',
                            bg_color='black',
                            size=(1920, 100))
        title_clip = title_clip.set_position(('center', 'top')).set_duration(3)
        
        # Fade in effect
        img_clip = img_clip.fadein(0.5)
        
        # Combine
        video = CompositeVideoClip([img_clip, title_clip])
        clips.append(video)
    
    # Add transitions between clips
    final_clips = []
    for i, clip in enumerate(clips):
        if i > 0:
            # Fade transition
            clip = clip.fadein(0.3)
        if i < len(clips) - 1:
            clip = clip.fadeout(0.3)
        final_clips.append(clip)
    
    # Concatenate
    final_video = concatenate_videoclips(final_clips, method="compose")
    final_video.write_videofile(output, fps=24, codec='libx264')
    
    print(f"✅ Animated video created: {output}")
    return final_video

def create_presentation_to_video(presentation_path, output="presentation_video.mp4", fps=1):
    """
    Convert PowerPoint presentation to video
    Requires: Export slides as images first
    """
    
    # This would require exporting PPTX to images first
    # Option 1: Use LibreOffice to export
    # Option 2: Use python-pptx to extract images
    # Option 3: Manual export from PowerPoint
    
    print("💡 To convert presentation to video:")
    print("   1. Export slides as images (PNG)")
    print("   2. Place in 'presentation_slides/' directory")
    print("   3. Run: create_demo_video_from_images('presentation_slides', 'presentation_video.mp4')")
    
    slides_dir = "presentation_slides"
    if os.path.exists(slides_dir):
        return create_demo_video_from_images(slides_dir, output, fps)
    else:
        print(f"⚠️  Directory '{slides_dir}' not found")
        return None

if __name__ == "__main__":
    import sys
    
    print("🎬 Générateur de Vidéo Démo")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        mode = "images"
    
    if mode == "images":
        # Create video from screenshots
        create_demo_video_from_images("screenshots", "software_demo.mp4", fps=2)
    elif mode == "diagrams":
        # Create animated video from diagrams
        create_animated_diagram_video("diagrams", "diagrams_demo.mp4")
    elif mode == "presentation":
        # Convert presentation to video
        create_presentation_to_video("presentation.pptx", "presentation_video.mp4")
    else:
        print("Usage:")
        print("  python generate_demo_video.py images      # From screenshots")
        print("  python generate_demo_video.py diagrams    # From diagrams")
        print("  python generate_demo_video.py presentation # From presentation slides")

