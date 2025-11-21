#!/usr/bin/env python3
"""
Generate video from screenshots of PPTX slides and Google Images navigation
Alternative method: Take screenshots manually, then generate video
"""

from moviepy.editor import ImageClip, concatenate_videoclips, TextClip, CompositeVideoClip
import os
import glob
from pathlib import Path

def create_demo_video_from_screenshots(screenshots_dir="demo_screenshots", output="demo_final.mp4", fps=2):
    """
    Create demo video from manually taken screenshots
    
    Expected structure:
    demo_screenshots/
      ├── 01_slide1_title.png
      ├── 02_slide2.png
      ├── 03_slide3.png
      ├── 04_google_images_search.png
      ├── 05_google_images_results.png
      ├── 06_slide4_architecture.png
      ├── 07_slide5_scenario.png
      ├── 08_google_images_disease.png
      └── 09_slide6_contact.png
    """
    
    if not os.path.exists(screenshots_dir):
        print(f"❌ Directory not found: {screenshots_dir}")
        print(f"\n💡 Create directory and add screenshots:")
        print(f"   mkdir {screenshots_dir}")
        print(f"   Then take screenshots in order:")
        print(f"   1. PowerPoint slides (in presentation mode)")
        print(f"   2. Google Images search results")
        return None
    
    # Find all images
    image_extensions = ['*.png', '*.jpg', '*.jpeg']
    images = []
    for ext in image_extensions:
        images.extend(glob.glob(os.path.join(screenshots_dir, ext)))
        images.extend(glob.glob(os.path.join(screenshots_dir, ext.upper())))
    
    if not images:
        print(f"⚠️  No images found in {screenshots_dir}")
        return None
    
    # Sort by filename (assuming numbered filenames)
    images.sort()
    print(f"📸 Found {len(images)} screenshots")
    
    # Create clips with appropriate durations
    clips = []
    for i, img_path in enumerate(images):
        filename = os.path.basename(img_path)
        print(f"  Processing: {filename}")
        
        # Determine duration based on content
        if 'slide' in filename.lower():
            duration = 4  # Slides: 4 seconds
        elif 'google' in filename.lower() or 'search' in filename.lower():
            duration = 8  # Web searches: 8 seconds
        else:
            duration = 4  # Default: 4 seconds
        
        # Create image clip
        try:
            img_clip = ImageClip(img_path).set_duration(duration)
            
            # Resize if needed (optional - maintain aspect ratio)
            # img_clip = img_clip.resize(height=1080) if img_clip.h > 1080 else img_clip
            
            # Add step number overlay
            step_text = f"Étape {i+1}/{len(images)}"
            txt_clip = TextClip(step_text,
                              fontsize=30,
                              color='white',
                              bg_color='black',
                              size=(200, 40),
                              method='caption')
            txt_clip = txt_clip.set_position(('right', 'top')).set_duration(duration).set_start(0)
            
            # Combine image and text
            video = CompositeVideoClip([img_clip, txt_clip])
            clips.append(video)
        except Exception as e:
            print(f"   ⚠️  Error processing {filename}: {e}")
            continue
    
    if not clips:
        print("❌ No valid clips created")
        return None
    
    # Concatenate all clips
    print(f"\n🎬 Creating video from {len(clips)} clips...")
    final_video = concatenate_videoclips(clips, method="compose")
    
    # Export
    print(f"💾 Exporting to {output}...")
    final_video.write_videofile(output, fps=fps, codec='libx264', audio=False)
    
    print(f"✅ Video created: {output}")
    return final_video

def create_screenshot_guide():
    """Guide for taking screenshots manually"""
    
    print("=" * 70)
    print("📸 GUIDE: PRENDRE SCREENSHOTS POUR VIDÉO DÉMO")
    print("=" * 70)
    
    steps = [
        ("1. Ouvrir présentation", "presentation_thales_template_correct.pptx"),
        ("2. Démarrer slideshow", "F5 dans PowerPoint"),
        ("3. Prendre screenshot Slide 1", "Win+Shift+S ou Print Screen"),
        ("4. Naviguer Slide 2", "Flèche droite"),
        ("5. Prendre screenshot Slide 2", ""),
        ("6. Naviguer Slide 3", "Flèche droite"),
        ("7. Prendre screenshot Slide 3", ""),
        ("8. Alt+Tab → Navigateur", "Ouvrir Google Images"),
        ("9. Rechercher 'images satellitaires agriculture'", ""),
        ("10. Prendre screenshot résultats", ""),
        ("11. Scroller images", ""),
        ("12. Prendre screenshot images défilées", ""),
        ("13. Alt+Tab → PowerPoint", "Retour slides"),
        ("14. Naviguer Slide 4", "Flèche droite"),
        ("15. Prendre screenshot Slide 4", ""),
        ("16. Naviguer Slide 5", "Flèche droite"),
        ("17. Prendre screenshot Slide 5", ""),
        ("18. Alt+Tab → Navigateur", "Nouvelle recherche"),
        ("19. Rechercher 'satellite images disease detection'", ""),
        ("20. Prendre screenshot résultats", ""),
        ("21. Alt+Tab → PowerPoint", "Retour slides"),
        ("22. Naviguer Slide 6", "Flèche droite"),
        ("23. Prendre screenshot Slide 6", ""),
    ]
    
    print("\n📋 SÉQUENCE DE SCREENSHOTS:\n")
    for step in steps:
        if isinstance(step, tuple):
            print(f"{step[0]}")
            if step[1]:
                print(f"   {step[1]}")
        else:
            print(f"{step}")
        print()
    
    print("\n💡 CONSEILS:")
    print("- Nommer fichiers: 01_slide1.png, 02_slide2.png, etc.")
    print("- Utiliser Win+Shift+S pour sélectionner zone")
    print("- Ou Print Screen pour écran complet")
    print("- Sauvegarder dans dossier: demo_screenshots/")
    print("- Format: PNG (meilleure qualité)")
    print()
    print("📁 Structure recommandée:")
    print("demo_screenshots/")
    print("  ├── 01_slide1_title.png")
    print("  ├── 02_slide2.png")
    print("  ├── 03_slide3.png")
    print("  ├── 04_google_images_search.png")
    print("  ├── 05_google_images_results.png")
    print("  ├── 06_slide4_architecture.png")
    print("  ├── 07_slide5_scenario.png")
    print("  ├── 08_google_images_disease.png")
    print("  └── 09_slide6_contact.png")
    print()
    print("🚀 Après avoir pris les screenshots:")
    print("   python generate_video_from_screenshots.py")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "guide":
        create_screenshot_guide()
    else:
        print("🎬 Génération vidéo depuis screenshots")
        print("=" * 70)
        
        # Check if screenshots directory exists
        screenshots_dir = "demo_screenshots"
        if not os.path.exists(screenshots_dir):
            print(f"\n⚠️  Directory '{screenshots_dir}' not found")
            print("\n💡 Options:")
            print("   1. Create directory and take screenshots manually")
            print("   2. Run: python generate_video_from_screenshots.py guide")
            print("   3. Or use automated script: generate_demo_with_web_search.py")
        else:
            create_demo_video_from_screenshots(screenshots_dir, "demo_final.mp4", fps=2)

