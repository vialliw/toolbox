import os
import hashlib
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set

def calculate_file_hash(filepath: str) -> str:
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        # Read the file in chunks to handle large files efficiently
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def find_duplicate_files(directory: str) -> Dict[str, List[str]]:
    """
    Recursively scan directory for duplicate files.
    Returns a dictionary with hash as key and list of duplicate filepaths as value.
    """
    hash_map = defaultdict(list)
    scanned_files: Set[str] = set()  # Track already processed files
    
    # Walk through directory recursively
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            try:
                # Resolve any symbolic links and get absolute path
                absolute_path = str(Path(filepath).resolve())
                
                # Skip if we've already processed this file
                if absolute_path in scanned_files:
                    continue
                
                # Calculate file hash and store in hash map
                file_hash = calculate_file_hash(absolute_path)
                hash_map[file_hash].append(absolute_path)
                scanned_files.add(absolute_path)
                
            except (PermissionError, FileNotFoundError) as e:
                print(f"Error processing {filepath}: {str(e)}")
                continue
    
    # Filter out unique files (no duplicates)
    return {k: v for k, v in hash_map.items() if len(v) > 1}

def format_size(size: int) -> str:
    """Convert size in bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def main():
    # Get directory path from user
    directory = input("Enter directory path to scan: ").strip()
    
    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return
    
    print(f"\nScanning directory: {directory}")
    print("This might take a while depending on the number and size of files...\n")
    
    # Find duplicates
    duplicates = find_duplicate_files(directory)
    
    if not duplicates:
        print("No duplicate files found!")
        return
    
    # Print results
    total_sets = len(duplicates)
    total_duplicates = sum(len(files) - 1 for files in duplicates.values())
    
    print(f"Found {total_sets} sets of duplicate files ({total_duplicates} duplicate files total):\n")
    
    for hash_value, file_list in duplicates.items():
        size = os.path.getsize(file_list[0])
        print(f"\nDuplicate files (Size: {format_size(size)}):")
        for filepath in file_list:
            print(f"  - {filepath}")

if __name__ == "__main__":
    main()
