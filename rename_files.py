import os

# get the current working directory
start_dir = os.getcwd()

# iterate over all directories and files in the start directory and its subdirectories
for dirpath, dirnames, filenames in os.walk(start_dir):
    for filename in filenames:
        # check if the filename contains a space
        if ' ' in filename:
            # replace the spaces with underscores
            new_filename = filename.replace(' ', '_')
            # construct the full paths to the old and new files
            old_path = os.path.join(dirpath, filename)
            new_path = os.path.join(dirpath, new_filename)
            # rename the file using the os.rename() function
            os.rename(old_path, new_path)
