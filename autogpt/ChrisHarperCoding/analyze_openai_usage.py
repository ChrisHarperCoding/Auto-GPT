# Python script to analyze OpenAI API usage

import openai
import os

# Set up OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Analyze usage of OpenAI API key
usage = openai.Usage.retrieve()

# Print usage statistics
print(usage)