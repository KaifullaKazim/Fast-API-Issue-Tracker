from pathlib import Path
import json

data_dir = Path("data")   # we are creating a folder named data in the root directory of the project to store the issues.json file
data_file = data_dir / "issues.json" # this is the path to the issues.json file inside the data folder

def load_data():   # 
    if data_file.exists():
        with open(data_file, "r") as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    return []

def save_data(data):
    data_dir.mkdir(parents=True, exist_ok=True)
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)