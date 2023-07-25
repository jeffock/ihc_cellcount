import os

def rename(directory):
    # Get the list of files in the directory
    file_list = os.listdir(directory)

    i = 0

    for filename in file_list:
        
        # Skip directories
        if not os.path.isfile(os.path.join(directory, filename)):
            continue
        
        if '.1.' in filename:
            if 'ch00' in filename:
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '1_B_'+ '.tif'))
            if 'ch01' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '1_G_'+ '.tif'))
            if 'ch02' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '1_R_'+ '.tif'))
        elif '.2.' in filename:
            if 'ch00' in filename:
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '2_B_'+ '.tif'))
            if 'ch01' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '2_G_'+ '.tif'))
            if 'ch02' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '2_R_'+ '.tif'))
        elif '.3.' in filename:
            if 'ch00' in filename:
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '3_B_'+ '.tif'))
            if 'ch01' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '3_G_'+ '.tif'))
            if 'ch02' in filename:
                os.rename(os.path.join(directory, filename), os.path.join(directory, str(i)+ '3_R_'+ '.tif'))
        else:
            i += 0
        i += 1

if __name__ == '__main__':
    directory_path = 'Data'
    rename(directory_path)