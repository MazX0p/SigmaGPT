# SigmaGPT

SigmaGPT is a Python script that uses the OpenAI GPT-3.5 language model to analyze Windows Event Log (EVTX) files for security threats. It includes the following features:

- **Sigma rules support**: SigmaGPT takes one or more Sigma rules files as input, and compares each event in the EVTX file against each rule to determine if any potential security threats exist.
- **Highlighted output**: SigmaGPT outputs the results, highlighting any relevant text in both the Sigma rule and the EVTX event in red to make it easy to spot potential threats.
- **Customizable**: SigmaGPT allows you to use your own Sigma rules files or folders, as well as your own OpenAI GPT-3.5 API key.
- **Easy to use**: SigmaGPT prompts you for the path to the Sigma rules file/folder and the EVTX file, making it easy to get started.

SigmaGPT is designed to help security professionals and system administrators detect potential security threats in their Windows Event Log files. By using Sigma rules and the OpenAI GPT-3.5 language model, SigmaGPT provides a powerful way to analyze your logs and identify potential threats that may be present.

We understand that logs often contain sensitive information, and we take the security of your data seriously. That's why SigmaGPT does not upload your logs or any other sensitive information to our servers. All processing is done locally on your own machine.

The OpenAI GPT-3.5 language model is one of the most advanced language models available today, and it has been trained on a wide variety of data to ensure its accuracy and effectiveness. We believe that by using this model in conjunction with Sigma rules, we can help security professionals detect potential threats in their logs more quickly and accurately.

## Installation

To install SigmaGPT, follow these steps:

1. Clone this repository to your local machine: `git clone https://github.com/MazX0p/SigmaGPT.git`
2. Navigate to the cloned repository directory: `cd SigmaGPT`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Set the `CHATGPT_API_KEY` environment variable to your OpenAI GPT-3 API key: `export CHATGPT_API_KEY=<your_api_key>`
5. Run the `sigma_gpt.py` script: `python sigma_gpt.py`

## Usage

To use SigmaGPT, follow these steps:

1. Download one or more Sigma rules files from the [Sigma repository](https://github.com/Neo23x0/sigma/tree/master/rules), or a folder containing Sigma rules files.
2. Run the `sigma_gpt.py` script and follow the prompts to enter the path to the Sigma rules file/folder and the path to the EVTX file.
3. Review the output from the script, which will display each Sigma rule that matched an event in the EVTX file, as well as the text from both the Sigma rule and the EVTX event, with relevant text highlighted in red.

If you are unfamiliar with Sigma rules, please see the [Sigma documentation](https://github.com/Neo23x0/sigma/blob/master/README.md) for more information on how to download and use Sigma rules to detect security threats.

## Contributing

Contributions to SigmaGPT are welcome and appreciated! 
