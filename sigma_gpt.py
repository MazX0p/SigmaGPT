import requests
import Evtxtract
import json
import os
import yaml
from colorama import init, Fore, Style

# Load the ChatGPT API key from an environment variable
api_key = os.environ.get('CHATGPT_API_KEY')
if not api_key:
    print('Error: ChatGPT API key is not set in the environment.')
    exit(1)

# Initialize the colorama module
init()

# Prompt the user for the Sigma rules file/folder path
sigma_rules_paths = []
while True:
    path = input('Enter the path to a Sigma rules file/folder (or type "done" when finished): ')
    if path.lower() == 'done':
        break
    elif os.path.isfile(path) or os.path.isdir(path):
        sigma_rules_paths.append(path)
    else:
        print('Invalid path, please try again.')

# Prompt the user for the EVTX file path
evtx_file_path = input('Enter the path to the EVTX file: ')

# Load the Sigma rules from one or more files/folders
sigma_rules = []
for path in sigma_rules_paths:
    if os.path.isfile(path):
        with open(path) as f:
            rules = yaml.safe_load(f)
            if rules:
                sigma_rules.extend(rules)
            else:
                print(f'Error: No rules found in file "{path}"')
    elif os.path.isdir(path):
        for filename in os.listdir(path):
            if filename.endswith('.yml') or filename.endswith('.yaml'):
                with open(os.path.join(path, filename)) as f:
                    rules = yaml.safe_load(f)
                    if rules:
                        sigma_rules.extend(rules)
                    else:
                        print(f'Error: No rules found in file "{os.path.join(path, filename)}"')

# Process each event in the EVTX file and compare against the Sigma rules
with Evtxtract.open(evtx_file_path) as evtx:
    for record in evtx.records():
        event = json.loads(record.json())

        for rule in sigma_rules:
            try:
                # Get the GPT-3.5 response for the Sigma rule and the EVTX event
                response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers={'Authorization': f'Bearer {api_key}'}, json={
                    'prompt': f'{rule}\nEvent: {event["Event"]["EventData"]}\n',
                    'max_tokens': 1024,
                    'n': 1,
                    'stop': '.'
                }).json()

                # Check if the response contains any redacted text (indicating a potential security threat)
                if '[REDACTED]' in response['choices'][0]['text']:
                    # Print the Sigma rule and the event data, with relevant text highlighted in red
                    print(Fore.RED + 'Rule: ' + str(rule))
                    print(Fore.RED + 'Event: ' + json.dumps(event["Event"]["EventData"], indent=4))
                    print(Fore.RESET)
            except Exception as e:
                print(f'Error processing Sigma rule: {e}')
