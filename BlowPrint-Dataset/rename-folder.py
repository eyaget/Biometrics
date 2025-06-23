import os

def rename_folders_in_current_directory(new_base_name):
    # Get the directory where the script is located
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Get all subdirectories in that location
    folders = [f for f in os.listdir(base_path)
               if os.path.isdir(os.path.join(base_path, f)) and f != os.path.basename(__file__)]

    for idx, folder in enumerate(folders, start=1):
        old_path = os.path.join(base_path, folder)
        new_folder_name = f"{new_base_name}-{idx}"
        new_path = os.path.join(base_path, new_folder_name)

        os.rename(old_path, new_path)
        print(f"Renamed: '{folder}' -> '{new_folder_name}'")
        
rename_folders_in_current_directory('Participant')
