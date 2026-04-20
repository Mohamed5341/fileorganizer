from pathlib import Path
import random, string

target_dir = Path.cwd() / 'examples'
Path.mkdir(target_dir, exist_ok=True)

N = 100
extensions = ["jpg", "png", "pdf", "txt", "docx", "mp4", "xlsx", "csv"]
keywords = ["invoice", "report", "photo", "data", "backup"]

for i in range(N):
    name = random.choice(keywords) + "_" + ''.join(random.choices(string.ascii_lowercase, k=5))
    ext = random.choice(extensions)
    file_path = target_dir / f"{name}.{ext}"

    with open(file_path, "w") as f:
        f.write("test content")
