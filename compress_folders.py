import os
import tarfile
import shutil

def compress_and_remove_folders(directory):
    """
    Compresses each folder in the specified directory into a separate .tar.gz file and then deletes the original folder.

    Parameters:
    - directory: The directory containing the folders to compress and remove.
    """
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        # Check if the item is a directory
        if os.path.isdir(folder_path):
            # Define the name of the tar.gz file
            output_filename = os.path.join(directory, f"{folder}.tar.gz")
            # Create a tar.gz file
            with tarfile.open(output_filename, "w:gz") as tar:
                tar.add(folder_path, arcname=folder)
                print(f"Compressed: {folder} into {output_filename}")
            # After successful compression, delete the original folder
            shutil.rmtree(folder_path)
            print(f"Removed original folder: {folder}")

# Example usage
directory = '/path/to/your/directory'  # Replace with the path to your directory containing folders
compress_and_remove_folders(directory)
