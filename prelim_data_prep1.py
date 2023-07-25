import os

def rename_as_needed(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)

    for filename in file_list:
        # Skip directories
        if not os.path.isfile(os.path.join(directory, filename)):
            continue

        # Remove characters from the filename
        new_filename = filename[16:]

        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    directory_path = 'Data'
    rename_as_needed(directory_path)
