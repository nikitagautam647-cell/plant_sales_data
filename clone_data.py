#!/usr/bin/env python3
"""
Plant Sales Data - Clone/Backup Script (Optional)
Simple utility to clone and backup the sales dataset
"""

import shutil
from pathlib import Path
from datetime import datetime

def clone_data():
    """Create backup copy of data files"""
    data_dir = Path(__file__).parent / "data"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(__file__).parent / "results" / f"backup_{timestamp}"
    
    try:
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy all data files
        for file in data_dir.glob("*.txt"):
            shutil.copy2(file, backup_dir / file.name)
            print(f"✓ Copied {file.name}")
        
        print(f"\n✓ Backup created: {backup_dir}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    print("Plant Sales Data - Backup Utility\n")
    clone_data()

