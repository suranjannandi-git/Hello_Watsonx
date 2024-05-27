import os
from dotenv import load_dotenv, find_dotenv
from ibm_watson_machine_learning.foundation_models import Model

load_dotenv(find_dotenv())
model_id = "meta-llama/llama-2-70b-chat"

def get_credentials():
	return {
		"url" : os.getenv("WX_CLOUD_URL", None),
		"apikey" : os.getenv("IBM_API_KEY", None)
	}

def get_parameters():
	return {
		"decoding_method": "greedy",
		"min_new_tokens": 1,
		"max_new_tokens": 200,
		"repetition_penalty": 1
	}

def get_model():
	return Model(
		model_id = model_id,
		params = get_parameters(),
		credentials = get_credentials(),
		project_id = os.getenv("WX_PROJECT_ID", None)
		)

def execute_model(prompt):
	model = get_model()
	generated_response = model.generate_text(prompt=prompt, guardrails=True)
	return generated_response


# prompt_input = """Input: Is the battery car good for environment"""
prompt_input = "who is elon musk?"
print(f"LLM Response: {execute_model(prompt_input)}")
