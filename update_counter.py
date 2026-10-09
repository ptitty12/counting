import datetime
import os
import subprocess

# Define the list of excluded dates (formatted as MM/DD/YYYY)
EXCLUDED_DATES = [
    "2/10/2025", "2/11/2025", "2/12/2025", "2/13/2025", "2/14/2025",
    "2/17/2025", "2/19/2025", "2/24/2025", "2/26/2025", "3/3/2025",
    "3/4/2025", "3/5/2025", "3/27/2025", "3/28/2025", "4/2/2025",
    "4/3/2025", "4/8/2025", "4/9/2025", "4/14/2025", "4/15/2025",
    "4/16/2025", "4/21/2025", "4/23/2025", "4/28/2025", "4/29/2025",
    "4/30/2025", "5/6/2025", "5/7/2025", "5/14/2025", "5/15/2025",
    "5/22/2025", "5/23/2025", "6/2/2025", "6/9/2025", "6/16/2025",
    "6/23/2025", "6/24/2025", "6/25/2025", "6/26/2025", "6/27/2025",
    "6/30/2025", "7/7/2025", "7/14/2025"
]

# Get the current date in MM/DD/YYYY format
current_date = datetime.datetime.now().strftime("%m/%d/%Y")

# Check if the current date is in the excluded list
if current_date in EXCLUDED_DATES:
    print(f"Script will not run on excluded date: {current_date}")
    exit()

# Path to the repository
REPO_PATH = os.environ.get('REPO_PATH', os.path.dirname(os.path.abspath(__file__)))

# Change directory to the repository
os.chdir(REPO_PATH)

# Path to the counter file
COUNTER_FILE = os.path.join(REPO_PATH, 'counter.txt')

# Append the current datetime to the file
with open(COUNTER_FILE, 'a') as f:
    f.write(f"{datetime.datetime.now()}\n")

# Stage, commit, and push changes
subprocess.run(['git', 'add', 'counter.txt'], check=True)
commit_message = f"Update counter.txt on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(['git', 'commit', '-m', commit_message], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)
