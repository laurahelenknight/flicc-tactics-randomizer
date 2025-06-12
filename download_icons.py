#!/usr/bin/env python3
"""
FLICC Icons Download Script
Downloads all FLICC technique icons from Wikimedia Commons
"""

import os
import requests
from urllib.parse import quote
import time

def create_images_directory():
    """Create images directory if it doesn't exist"""
    if not os.path.exists('images'):
        os.makedirs('images')
        print("Created 'images' directory")

def download_icon(filename, max_retries=3):
    """Download a single icon from Wikimedia Commons"""
    # Wikimedia Commons direct file URL
    url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{quote(filename)}"
    
    file_path = os.path.join('images', filename)
    
    # Skip if file already exists
    if os.path.exists(file_path):
        print(f"✓ {filename} (already exists)")
        return True
    
    for attempt in range(max_retries):
        try:
            print(f"⬇ Downloading {filename}...", end=" ")
            
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Save the file
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            print("✓")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"✗ (Attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                print(f"  Retrying in 2 seconds...")
                time.sleep(2)
            else:
                print(f"  Failed to download {filename}: {e}")
                return False
    
    return False

def main():
    """Main download function"""
    print("🎯 FLICC Icons Downloader")
    print("=" * 40)
    
    # Create images directory
    create_images_directory()
    
    # Complete list of FLICC icons
    icons = [
        # Fake Experts
        "Bulk_Fake_Experts_Fallacy_Icon_Black.svg",
        "Magnified_Minority_Fallacy_Icon_Black.svg",
        "Fake_Debate_Fallacy_Icon_Black.svg",
        
        # Logical Fallacies
        "Ad_Hominem_Fallacy_Icon_Black.svg",
        "Misrepresentation_Fallacy_Icon_Black.svg",
        "Ambiguity_Fallacy_Icon_Black.svg",
        "Oversimplification_Fallacy_Icon_Black.svg",
        "False_Analogy_Fallacy_Icon_Black.svg",
        "Red_Herring_Fallacy_Icon_Black.svg",
        "Slippery_Slope_Fallacy_Icon_Black.svg",
        "Straw_Man_Fallacy_Icon_Black.svg",
        "False_Choice_Fallacy_Icon_Black.svg",
        "Single_Cause_Fallacy_Icon_Black.svg",
        "Blowfish_Fallacy_Icon_Black.svg",
        
        # Impossible Expectations
        "Impossible_Expectations_Fallacy_Icon_Black.svg",
        "Moving_Goalposts_Fallacy_Icon_Black.svg",
        
        # Cherry Picking
        "Cherry_Picking_Fallacy_Icon_Black.svg",
        "Quote_Mining_Fallacy_Icon_Black.svg",
        "Anecdote_Fallacy_Icon_Black.svg",
        "Slothful_Induction_Fallacy_Icon_Black.svg",
        
        # Conspiracy Theories
        "Conspiracy_Theory_Fallacy_Icon_Black.svg",
        "Contradictory_Fallacy_Icon_Black.svg",
        "Overriding_Suspicion_Fallacy_Icon_Black.svg",
        "Nefarious_Intent_Fallacy_Icon_Black.svg",
        "Something_Must_Be_Wrong_Fallacy_Icon_Black.svg",
        "Persecuted_Victim_Fallacy_Icon_Black.svg",
        "Immune_to_Evidence_Fallacy_Icon_Black.svg",
        "Re-interpreting_Randomness_Fallacy_Icon_Black.svg",
    ]
    
    print(f"Downloading {len(icons)} FLICC icons from Wikimedia Commons...")
    print()
    
    successful_downloads = 0
    failed_downloads = []
    
    for i, icon in enumerate(icons, 1):
        print(f"[{i:2d}/{len(icons)}] ", end="")
        
        if download_icon(icon):
            successful_downloads += 1
        else:
            failed_downloads.append(icon)
        
        # Small delay between downloads to be respectful
        time.sleep(0.5)
    
    print()
    print("=" * 40)
    print(f"✅ Download Complete!")
    print(f"   Successfully downloaded: {successful_downloads}/{len(icons)} icons")
    
    if failed_downloads:
        print(f"   Failed downloads: {len(failed_downloads)}")
        print("   Failed files:")
        for failed in failed_downloads:
            print(f"     - {failed}")
        print()
        print("💡 Tip: You can run this script again to retry failed downloads")
    else:
        print("   All icons downloaded successfully! 🎉")
    
    print()
    print("📁 Icons saved to: ./images/")
    print("🚀 Your FLICC randomizer is ready to use!")

if __name__ == "__main__":
    main()
