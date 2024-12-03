import os 
import datetime
from datetime import timedelta
import json

with open('folder-delete-manager/config.json', 'r') as config_file:
    config = json.load(config_file)

ss_dir = config['screenshots_dir']

if not ss_dir:
    raise ValueError("directory not found")

# Get the creation time of the most recent file
most_recent = max(os.path.getctime(os.path.join(ss_dir, f)) for f in os.listdir(ss_dir))
most_recent_date = datetime.datetime.fromtimestamp(most_recent)

# Calculate the cutoff date (30 days before the most recent file)
cutoff_date = most_recent_date - timedelta(days=30)

for file in os.listdir(ss_dir):
    file_path = os.path.join(ss_dir, file)
    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

    if creation_time < cutoff_date:
        os.remove(file_path)