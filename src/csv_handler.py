import logging
import os
from typing import List
from dataclasses import asdict
import pandas as pd

from .models import Place


def save_places_to_csv(places: List[Place], output_path: str = "result.csv", append: bool = False):
    """Save places to CSV with data cleaning and logging"""
    
    if not places:
        logging.warning("⚠️ No data to save - no places were extracted")
        return
        
    logging.info(f"💾 Preparing to save {len(places)} places...")
    
    df = pd.DataFrame([asdict(place) for place in places])
    
    # Remove columns with only one unique value (usually empty)
    original_columns = len(df.columns)
    for column in df.columns:
        if df[column].nunique() == 1:
            df.drop(column, axis=1, inplace=True)
    
    removed_columns = original_columns - len(df.columns)
    if removed_columns > 0:
        logging.info(f"🧹 Cleaned data: removed {removed_columns} empty columns")
    
    # Save to CSV
    file_exists = os.path.isfile(output_path)
    mode = "a" if append else "w"
    header = not (append and file_exists)
    
    try:
        df.to_csv(output_path, index=False, mode=mode, header=header)
        
        # File size
        file_size = os.path.getsize(output_path)
        size_kb = file_size / 1024
        
        action = "Appended to" if append else "Saved to"
        logging.info(f"✅ {action} '{output_path}'")
        logging.info(f"📊 {len(df)} places, {len(df.columns)} columns, {size_kb:.1f} KB")
        
        # Show sample of what was saved
        if len(places) > 0 and places[0].name:
            sample_names = [p.name for p in places[:3] if p.name]
            if sample_names:
                sample_text = ", ".join(sample_names)
                if len(sample_names) < len(places):
                    sample_text += f" and {len(places) - len(sample_names)} more..."
                logging.info(f"📍 Sample: {sample_text}")
                
    except Exception as e:
        logging.error(f"❌ Failed to save CSV: {e}")
