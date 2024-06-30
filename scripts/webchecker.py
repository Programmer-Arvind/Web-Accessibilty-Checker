import subprocess
import json


# URL of the website you want to check
url = 'https://www.youtube.com/'

# Command to run Lighthouse and output the results in JSON format
command = [
    "npx",
    "lighthouse",
    '--output=html',
    '--output-path=./templates/report.html'
]

# Function to run the command and handle errors
def run_lighthouse_command(url, view=None):
    command.append(url)
    if view:
        command.append("--preset=desktop")
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running Lighthouse: {result.stderr}")
            return None
        return result
    except FileNotFoundError as e:
        print(f"Command not found: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
