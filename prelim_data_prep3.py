import os

def rename(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)

    i = 0

    for filename in file_list:
        
        # Skip directories
        if not os.path.isfile(os.path.join(directory, filename)):
            continue
        
        if '1_' in filename:
            if 'B' in filename:
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '_1_B'+ '.tif'))
            if 'G' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '_1_G'+ '.tif'))
            if 'R' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '_1_R'+ '.tif'))
        elif '2_' in filename:
            if 'B' in filename:
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '_2_B'+ '.tif'))
            if 'G' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '_2_G'+ '.tif'))
            if 'R' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '_2_R'+ '.tif'))
        elif '3_' in filename:
            if 'B' in filename:
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '_3_B'+ '.tif'))
            if 'G' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '_3_G'+ '.tif'))
            if 'R' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '_3_R'+ '.tif'))
        else:
            i += 0
        i += 1

if __name__ == '__main__':
    directory_path = 'Data'
    rename(directory_path)