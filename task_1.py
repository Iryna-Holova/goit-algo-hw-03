"""
Recursively copies files from a source directory to a destination
directory, organizing them into subdirectories based on their file extensions.
It accepts two command-line arguments: the source directory path and the
destination directory path (default is 'dist' if not specified).
"""

import shutil
import sys
from pathlib import Path


def copy_files_recursively(src: str, dest: str) -> None:
    """
    Recursively copies files from the source directory to the destination
    directory, organizing them into subdirectories based on file extensions.

    Args:
        src (str): Path to the source directory.
        dest (str): Path to the destination directory.
    """
    try:
        src_path = Path(src)
        dest_path = Path(dest)
        dest_path.mkdir(parents=True, exist_ok=True)

        # Iterate through all items in the source directory
        for item in src_path.iterdir():
            if item.is_dir():
                # If the item is a directory, call this function recursively
                copy_files_recursively(item, dest)
            elif item.is_file():
                # Get the file extension or assign 'no_extension' if none
                file_extension = item.suffix.lower()
                target_dir = dest_path / (
                    file_extension[1:]
                    if file_extension
                    else 'no_extension'
                )

                # Create the subdirectory for this file type if not exists
                target_dir.mkdir(parents=True, exist_ok=True)

                # Copy the file to the appropriate subdirectory
                shutil.copy2(item, target_dir)
                print(f"Copied: {item} to {target_dir}")

    except PermissionError:
        print(f"Permission denied: {src}")
    except FileNotFoundError:
        print(f"File or directory not found: {src}")
    except Exception as e:
        print(f"Error processing {src}: {e}")


def main() -> None:
    """
    Parses command-line arguments and initiates the file copying process.
    """
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_dir> [destination_dir]")
        sys.exit(1)

    # Source directory from command-line argument
    source_dir = sys.argv[1]

    # Destination directory from command-line argument or default to 'dist'
    destination_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    # Check if the source directory exists
    if not Path(source_dir).exists() or not Path(source_dir).is_dir():
        print(f"Source directory does not exist or invalid: {source_dir}")
        sys.exit(1)

    # Start the copying process
    copy_files_recursively(source_dir, destination_dir)
    print(f"Files have been copied and sorted into {destination_dir}.")


if __name__ == "__main__":
    main()
