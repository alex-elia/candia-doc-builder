#!/usr/bin/env python3
"""
Automated screen recording script
Records screen while showing slides and browser functionality
Alternates between presentation and software demo
"""

import subprocess
import time
import os
import sys
from pathlib import Path

def start_recording(output_file="demo_recording.mp4"):
    """
    Start screen recording using OBS or FFmpeg
    """
    print(f"🎬 Starting screen recording: {output_file}")
    
    # Option 1: OBS Studio (if installed and configured)
    # obs_path = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
    # if os.path.exists(obs_path):
    #     subprocess.Popen([obs_path, "--startrecording", "--minimize-to-tray"])
    #     return True
    
    # Option 2: FFmpeg (direct screen capture)
    try:
        # Windows: Use gdigrab (screen capture)
        ffmpeg_cmd = [
            "ffmpeg",
            "-f", "gdigrab",  # Windows screen capture
            "-framerate", "30",
            "-i", "desktop",  # Capture entire desktop
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "23",
            "-pix_fmt", "yuv420p",
            output_file
        ]
        
        print("📹 Starting FFmpeg recording...")
        print("   Press Ctrl+C to stop recording")
        process = subprocess.Popen(ffmpeg_cmd)
        return process
    except FileNotFoundError:
        print("⚠️  FFmpeg not found. Install from: https://ffmpeg.org/")
        print("💡 Alternative: Use OBS Studio manually")
        return None

def open_presentation(presentation_path):
    """Open PowerPoint presentation"""
    if os.path.exists(presentation_path):
        print(f"📊 Opening presentation: {presentation_path}")
        os.startfile(presentation_path)  # Windows
        time.sleep(3)  # Wait for PowerPoint to open
        return True
    return False

def open_browser(url):
    """Open browser to specific URL"""
    print(f"🌐 Opening browser: {url}")
    import webbrowser
    webbrowser.open(url)
    time.sleep(2)  # Wait for page to load
    return True

def switch_to_slide(slide_number):
    """Switch to specific slide in PowerPoint (requires PowerPoint in presentation mode)"""
    print(f"📑 Switching to slide {slide_number}")
    # Use keyboard shortcuts: Right arrow to go to next slide
    # This requires PowerPoint to be in focus
    import pyautogui
    try:
        # Press F5 to start presentation (if not already)
        # Then use arrow keys to navigate
        pyautogui.press('right', presses=slide_number-1)
        time.sleep(1)
    except ImportError:
        print("⚠️  pyautogui not installed. Install: pip install pyautogui")
        print("💡 Manual: Navigate slides manually")

def automate_demo_sequence():
    """
    Automate demo sequence:
    1. Start recording
    2. Show slides (presentation)
    3. Switch to browser (software demo)
    4. Alternate between slides and browser
    5. Stop recording
    """
    
    print("=" * 60)
    print("🎬 AUTOMATED DEMO RECORDING")
    print("=" * 60)
    
    # Configuration
    presentation_path = "presentation_thales_custom_template.pptx"
    browser_url = "http://localhost:8080"  # Your app URL
    output_video = "complete_demo.mp4"
    
    # Step 1: Start recording
    print("\n1️⃣ Starting screen recording...")
    recording_process = start_recording(output_video)
    
    if not recording_process:
        print("⚠️  Recording not started. Please start manually:")
        print("   - OBS Studio: Start recording")
        print("   - Or install FFmpeg")
        input("Press Enter when recording is started...")
    
    time.sleep(2)  # Wait for recording to start
    
    # Step 2: Open presentation
    print("\n2️⃣ Opening presentation...")
    if open_presentation(presentation_path):
        time.sleep(3)
        
        # Start presentation mode (F5)
        import pyautogui
        try:
            pyautogui.press('f5')  # Start slideshow
            time.sleep(2)
            print("   ✓ Presentation started")
        except:
            print("   ⚠️  Start presentation manually (F5)")
            time.sleep(2)
        
        # Show first few slides
        print("\n3️⃣ Showing slides 1-3...")
        for i in range(3):
            time.sleep(3)  # 3 seconds per slide
            pyautogui.press('right')  # Next slide
            print(f"   → Slide {i+2}")
    
    # Step 4: Switch to browser
    print("\n4️⃣ Switching to browser demo...")
    open_browser(browser_url)
    time.sleep(5)  # Show browser for 5 seconds
    
    # Step 5: Alternate back to slides
    print("\n5️⃣ Returning to slides...")
    # Alt+Tab to switch windows (or click on PowerPoint)
    try:
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)
        pyautogui.press('right')  # Next slide
        time.sleep(3)
    except:
        print("   ⚠️  Switch to PowerPoint manually")
        time.sleep(3)
    
    # Step 6: Final browser demo
    print("\n6️⃣ Final browser demo...")
    open_browser(browser_url)
    time.sleep(5)
    
    # Step 7: Stop recording
    print("\n7️⃣ Stopping recording...")
    if recording_process:
        recording_process.terminate()
        print("   ✓ Recording stopped")
    else:
        print("   ⚠️  Stop recording manually (OBS or Ctrl+C)")
    
    print(f"\n✅ Demo recording complete: {output_video}")
    print("💡 Edit video if needed (add transitions, music, etc.)")

def create_demo_script_interactive():
    """
    Create an interactive script that guides through demo
    User controls timing, script provides structure
    """
    
    print("=" * 60)
    print("🎬 INTERACTIVE DEMO RECORDING GUIDE")
    print("=" * 60)
    
    steps = [
        ("Start recording", "OBS Studio or FFmpeg"),
        ("Show Slide 1: Title", "3 seconds"),
        ("Show Slide 2: Le Défi", "5 seconds"),
        ("Switch to Browser", "Open your app"),
        ("Demo Feature 1", "Show anomaly detection", 10),
        ("Return to Slides", "Slide 3: Solution", 3),
        ("Switch to Browser", "Demo Feature 2", 10),
        ("Show Slide 4: Architecture", "3 seconds"),
        ("Show Slide 5: Scénario 1", "5 seconds"),
        ("Final Browser Demo", "Show results", 10),
        ("Show Slide 6: Contact", "3 seconds"),
        ("Stop recording", "")
    ]
    
    print("\n📋 Demo Sequence:")
    for i, (action, details, *duration) in enumerate(steps, 1):
        dur = duration[0] if duration else 0
        print(f"\n{i}. {action}")
        print(f"   {details}")
        if dur > 0:
            print(f"   Duration: {dur} seconds")
    
    print("\n💡 Instructions:")
    print("1. Start OBS Studio recording")
    print("2. Follow the sequence above")
    print("3. Use Alt+Tab to switch between PowerPoint and Browser")
    print("4. Stop recording when done")
    
    # Generate timing script
    script_content = """
# Demo Recording Timing Script
# Follow these timings for smooth demo

TIMINGS = {
    "slide_1": 3,      # Title slide
    "slide_2": 5,      # Le Défi
    "browser_1": 10,   # First browser demo
    "slide_3": 3,      # Solution
    "browser_2": 10,   # Second browser demo
    "slide_4": 3,      # Architecture
    "slide_5": 5,      # Scénario 1
    "browser_3": 10,   # Final demo
    "slide_6": 3,      # Contact
}

# Total duration: ~52 seconds
"""
    
    with open("demo_timing_script.py", "w") as f:
        f.write(script_content)
    
    print("\n✅ Timing script created: demo_timing_script.py")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "auto":
        # Fully automated (requires FFmpeg and pyautogui)
        automate_demo_sequence()
    else:
        # Interactive guide
        create_demo_script_interactive()
        print("\n💡 For automated recording, install:")
        print("   pip install pyautogui")
        print("   Install FFmpeg: https://ffmpeg.org/")
        print("   Then run: python automated_screen_recording.py auto")

