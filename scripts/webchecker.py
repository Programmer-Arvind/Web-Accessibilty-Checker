import subprocess
import json

# Replace this with the full path to your Lighthouse installation if necessary
lighthouse_path = 'lighthousepath'

# URL of the website you want to check
url = 'url to check'

# Command to run Lighthouse and output the results in JSON format
command = [
    lighthouse_path,
    url,
    '--output=json',
    '--output=html',
    '--output-path=report.json',
    # # '--quiet',
    # "--preset=desktop",
    "--view"
]

# Function to run the command and handle errors
def run_lighthouse_command(command):
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

# Run the command
result = run_lighthouse_command(command)

if result:
    # Load the Lighthouse report from the generated file with explicit UTF-8 encoding
    try:
        with open('report.json', 'r', encoding='utf-8') as f:
            lighthouse_report = json.load(f)

        # Print the results
        print(json.dumps(lighthouse_report, indent=2))

        # Save the results to a file
        with open('lighthouse_report.json', 'w', encoding='utf-8') as f:
            json.dump(lighthouse_report, f, indent=2)
    except Exception as e:
        print(f"Error reading the Lighthouse report: {e}")