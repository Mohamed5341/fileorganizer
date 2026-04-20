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

extensions = []
for folder_name, folders_list, files_list in os.walk(working_dir):
    current_folder = Path(folder_name)

    for file_name in files_list:
        f = current_folder / file_name
        selected_dir = targets.get(f.suffix[1:], target_dir/"others")

        Path.mkdir(selected_dir, exist_ok=True)

        shutil.move(f, selected_dir)

print("Done")