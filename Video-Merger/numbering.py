import os 


path = input("Enter path: \n")
files = os.listdir(path)
mp4_files = [file for file in files if file.endswith(".mp4")]
for i, file in enumerate(mp4_files):
    old_file_name = os.path.basename(file)

    old_file_path = os.path.join(path, file)
    
    # Create the new file name and path
    new_file_name = f"{i+1}-{old_file_name}"
    new_file_path = os.path.join(path, new_file_name)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)
print("Done")