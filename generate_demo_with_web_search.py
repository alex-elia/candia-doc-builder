#!/usr/bin/env python3
"""
Generate demo video: PPTX presentation + Google Images search for satellite images
Alternates between slides and web navigation
"""

import subprocess
import time
import os
import sys
from pathlib import Path

try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except ImportError:
    PYAUTOGUI_AVAILABLE = False
    print("⚠️  pyautogui not installed. Install: pip install pyautogui")

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False
    print("⚠️  selenium not installed. Install: pip install selenium")

def open_presentation(presentation_path):
    """Open PowerPoint presentation"""
    if not os.path.exists(presentation_path):
        print(f"❌ Presentation not found: {presentation_path}")
        return False
    
    print(f"📊 Opening presentation: {presentation_path}")
    os.startfile(presentation_path)  # Windows
    time.sleep(4)  # Wait for PowerPoint to open
    return True

def start_powerpoint_presentation():
    """Start PowerPoint in presentation mode"""
    if not PYAUTOGUI_AVAILABLE:
        print("⚠️  pyautogui required. Install: pip install pyautogui")
        print("💡 Start presentation manually: Press F5 in PowerPoint")
        return False
    
    print("🎬 Starting PowerPoint presentation mode...")
    time.sleep(1)
    pyautogui.press('f5')  # Start slideshow
    time.sleep(2)
    print("   ✓ Presentation started")
    return True

def navigate_slide(direction='next', count=1):
    """Navigate slides in PowerPoint"""
    if not PYAUTOGUI_AVAILABLE:
        return False
    
    key = 'right' if direction == 'next' else 'left'
    for _ in range(count):
        pyautogui.press(key)
        time.sleep(0.3)
    return True

def open_google_images_search(query="images satellitaires"):
    """Open Google Images and search for satellite images"""
    if not SELENIUM_AVAILABLE:
        # Fallback: Use webbrowser
        import webbrowser
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}&tbm=isch"
        print(f"🌐 Opening Google Images: {query}")
        webbrowser.open(url)
        time.sleep(3)
        return None
    
    print(f"🌐 Opening Google Images: {query}")
    
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    try:
        # Try to use Chrome
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"⚠️  Chrome WebDriver not found: {e}")
        print("💡 Install ChromeDriver or use fallback method")
        # Fallback to webbrowser
        import webbrowser
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}&tbm=isch"
        webbrowser.open(url)
        time.sleep(3)
        return None
    
    # Navigate to Google Images
    driver.get("https://www.google.com/imghp")
    time.sleep(2)
    
    # Accept cookies if present (optional)
    try:
        accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Tout accepter') or contains(text(), 'Accept all')]")
        accept_button.click()
        time.sleep(1)
    except:
        pass
    
    # Search for query
    try:
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        print(f"   ✓ Search completed: {query}")
    except Exception as e:
        print(f"   ⚠️  Search failed: {e}")
    
    return driver

def scroll_images(driver, scrolls=2):
    """Scroll down to see more images"""
    if driver is None:
        return
    
    try:
        for i in range(scrolls):
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
        print("   ✓ Scrolled through images")
    except:
        pass

def switch_to_powerpoint():
    """Switch window focus to PowerPoint"""
    if not PYAUTOGUI_AVAILABLE:
        print("💡 Switch to PowerPoint manually (Alt+Tab)")
        return False
    
    # Alt+Tab to switch windows
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    return True

def switch_to_browser():
    """Switch window focus to browser"""
    if not PYAUTOGUI_AVAILABLE:
        print("💡 Switch to browser manually (Alt+Tab)")
        return False
    
    # Alt+Tab to switch windows
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    return True

def automate_demo_sequence():
    """
    Automate demo sequence:
    1. Open PowerPoint presentation
    2. Start slideshow
    3. Show slides
    4. Switch to browser - Google Images search
    5. Alternate between slides and browser
    6. Generate video
    """
    
    print("=" * 70)
    print("🎬 GÉNÉRATION VIDÉO DÉMO: PPTX + RECHERCHE GOOGLE IMAGES")
    print("=" * 70)
    
    # Configuration
    presentation_path = "presentation_thales_template_correct.pptx"
    output_video = "demo_pptx_google_images.mp4"
    
    # Check if presentation exists
    if not os.path.exists(presentation_path):
        # Try alternative names
        alternatives = [
            "presentation_thales_custom_template.pptx",
            "presentation_thales_premium.pptx"
        ]
        for alt in alternatives:
            if os.path.exists(alt):
                presentation_path = alt
                break
        else:
            print(f"❌ No presentation found. Looking for:")
            print(f"   - {presentation_path}")
            for alt in alternatives:
                print(f"   - {alt}")
            return
    
    print(f"\n📄 Using presentation: {presentation_path}")
    
    # Step 1: Open PowerPoint
    print("\n1️⃣ Opening PowerPoint presentation...")
    if not open_presentation(presentation_path):
        return
    time.sleep(2)
    
    # Step 2: Start presentation mode
    print("\n2️⃣ Starting presentation mode...")
    start_powerpoint_presentation()
    time.sleep(2)
    
    # Step 3: Show first slides
    print("\n3️⃣ Showing initial slides...")
    print("   → Slide 1: Title (4 seconds)")
    time.sleep(4)
    
    navigate_slide('next', 1)
    print("   → Slide 2 (4 seconds)")
    time.sleep(4)
    
    navigate_slide('next', 1)
    print("   → Slide 3 (4 seconds)")
    time.sleep(4)
    
    # Step 4: Switch to browser - Google Images
    print("\n4️⃣ Switching to browser - Google Images search...")
    driver = open_google_images_search("images satellitaires agriculture")
    time.sleep(3)
    
    # Scroll through images
    if driver:
        scroll_images(driver, 3)
        time.sleep(2)
    
    print("   → Showing satellite images (8 seconds)")
    time.sleep(8)
    
    # Step 5: Return to slides
    print("\n5️⃣ Returning to slides...")
    switch_to_powerpoint()
    time.sleep(1)
    
    navigate_slide('next', 1)
    print("   → Slide 4: Architecture (4 seconds)")
    time.sleep(4)
    
    navigate_slide('next', 1)
    print("   → Slide 5: Scénario (4 seconds)")
    time.sleep(4)
    
    # Step 6: Back to browser - More specific search
    print("\n6️⃣ Returning to browser - Specific search...")
    switch_to_browser()
    time.sleep(1)
    
    if driver:
        # New search
        try:
            search_box = driver.find_element(By.NAME, "q")
            search_box.clear()
            search_box.send_keys("satellite images disease detection agriculture")
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            scroll_images(driver, 2)
            print("   → Showing disease detection images (8 seconds)")
            time.sleep(8)
        except:
            pass
    
    # Step 7: Final slides
    print("\n7️⃣ Final slides...")
    switch_to_powerpoint()
    time.sleep(1)
    
    navigate_slide('next', 1)
    print("   → Slide 6: Contact (4 seconds)")
    time.sleep(4)
    
    # Close browser
    if driver:
        try:
            driver.quit()
        except:
            pass
    
    print("\n✅ Demo sequence completed!")
    print(f"\n💡 Next steps:")
    print(f"   1. If using OBS: Stop recording manually")
    print(f"   2. If using FFmpeg: Press Ctrl+C to stop")
    print(f"   3. Edit video if needed")
    print(f"   4. Output: {output_video}")

def create_interactive_guide():
    """Create interactive guide for manual recording"""
    
    print("=" * 70)
    print("🎬 GUIDE INTERACTIF: DÉMO PPTX + GOOGLE IMAGES")
    print("=" * 70)
    
    sequence = [
        ("Démarrer enregistrement", "OBS Studio ou FFmpeg", 0),
        ("Ouvrir présentation", "presentation_thales_template_correct.pptx", 0),
        ("Démarrer slideshow", "F5 dans PowerPoint", 0),
        ("Slide 1: Titre", "4 secondes", 4),
        ("Slide 2", "4 secondes", 4),
        ("Slide 3", "4 secondes", 4),
        ("Alt+Tab → Navigateur", "Ouvrir Google Images", 0),
        ("Recherche: 'images satellitaires agriculture'", "Scroller images", 8),
        ("Alt+Tab → PowerPoint", "Retour slides", 0),
        ("Slide 4: Architecture", "4 secondes", 4),
        ("Slide 5: Scénario", "4 secondes", 4),
        ("Alt+Tab → Navigateur", "Nouvelle recherche", 0),
        ("Recherche: 'satellite images disease detection'", "Scroller images", 8),
        ("Alt+Tab → PowerPoint", "Retour slides", 0),
        ("Slide 6: Contact", "4 secondes", 4),
        ("Arrêter enregistrement", "OBS ou Ctrl+C", 0),
    ]
    
    print("\n📋 SÉQUENCE DÉTAILLÉE:\n")
    total_time = 0
    for i, (action, details, duration) in enumerate(sequence, 1):
        print(f"{i:2d}. {action}")
        print(f"    {details}")
        if duration > 0:
            print(f"    ⏱️  {duration} secondes")
            total_time += duration
        print()
    
    print(f"⏱️  Durée totale (sans transitions): ~{total_time} secondes")
    print(f"⏱️  Durée estimée (avec transitions): ~{total_time + 10} secondes")
    
    print("\n💡 INSTRUCTIONS:")
    print("1. Installer prérequis:")
    print("   pip install pyautogui selenium")
    print("   Installer ChromeDriver: https://chromedriver.chromium.org/")
    print()
    print("2. Démarrer OBS Studio enregistrement")
    print("3. Exécuter ce script:")
    print("   python generate_demo_with_web_search.py auto")
    print("4. Le script orchestrera tout automatiquement")
    print("5. Arrêter enregistrement à la fin")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "auto":
        if not PYAUTOGUI_AVAILABLE:
            print("❌ pyautogui required for automation")
            print("   Install: pip install pyautogui")
            sys.exit(1)
        
        print("\n⚠️  IMPORTANT: Start screen recording BEFORE running this script!")
        print("   Option 1: OBS Studio - Start recording")
        print("   Option 2: FFmpeg - Run in separate terminal")
        print()
        input("Press Enter when recording is started...")
        
        automate_demo_sequence()
    else:
        create_interactive_guide()
        print("\n" + "=" * 70)
        print("🚀 Pour exécuter automatiquement:")
        print("   python generate_demo_with_web_search.py auto")
        print("=" * 70)

