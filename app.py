from pathlib import Path
import os, shutil

working_dir = Path.cwd() / "examples"
target_dir = working_dir

targets = {}
targets["jpg"] = target_dir / "images"
targets["png"] = target_dir / "images"
targets["txt"] = target_dir / "documents"
targets["docx"] = target_dir / "documents"
targets["pdf"] = target_dir / "documents"
targets["mp4"] = target_dir / "videos"
targets["csv"] = target_dir / "sheets"
targets["xlsx"] = target_dir / "sheets"

sub_target = {}
sub_target["invoice*"] = "invoice"
sub_target["backup*"] = "backup"

extensions = []
# move files
for folder_name, folders_list, files_list in os.walk(working_dir):
    current_folder = Path(folder_name)

    for pattern in sub_target.keys():
        for file_name in current_folder.glob(pattern):
            if not file_name.is_file():
                continue
            selected_dir = targets.get(file_name.suffix[1:], target_dir/"others") / sub_target[pattern]

            Path.mkdir(selected_dir, exist_ok=True, parents=True)

            try:
                shutil.move(file_name, selected_dir)
            except Exception as e:
                print(f"Error occurred while moving {file_name}: {e}")

    for file_name in current_folder.glob("*"):
        if not file_name.is_file():
            continue
        selected_dir = targets.get(file_name.suffix[1:], target_dir/"others")

        Path.mkdir(selected_dir, exist_ok=True, parents=True)

        try:
            shutil.move(file_name, selected_dir)
        except Exception as e:
            print(f"Error occurred while moving {file_name}: {e}")


# remove empty folders
for folder_name, folders_list, files_list in os.walk(working_dir):
    current_folder = Path(folder_name)
    if not any(current_folder.iterdir()):
        Path.rmdir(folder_name)
print("Done")