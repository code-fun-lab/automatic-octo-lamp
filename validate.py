# validate.py

import os

# Get the username from the commit author (GitHub provides this information)
username = os.environ.get('GITHUB_ACTOR')

# Get the list of changed files
changed_files = os.environ.get('GITHUB_WORKSPACE')

# Define the path to the user's folder
user_folder = os.path.join(changed_files, username)

# Ensure the user's folder exists
if not os.path.exists(user_folder):
    raise Exception(f"User folder '{username}' does not exist.")

# Check if the user made changes outside their folder
for root, dirs, files in os.walk(changed_files):
    if root != user_folder:
        raise Exception(f"Changes made outside of user folder '{username}'.")

# Validation successful
print("Validation passed.")
