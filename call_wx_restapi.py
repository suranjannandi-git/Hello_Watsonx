import os
import requests

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_access_token_url():
	url = "https://iam.cloud.ibm.com/identity/token"
	headers = {
		"Content-Type": "application/x-www-form-urlencoded"
	}
	data = {
		"grant_type": "urn:ibm:params:oauth:grant-type:apikey",
		"apikey": os.getenv("IBM_API_KEY", None) 
	}

	response = requests.post(url, headers=headers, data=data)
	return response.json()['access_token']

def get_response(prompt):
	ACCESS_TOKEN = get_access_token_url()
	
	body = {
		"input": prompt,
		"parameters": {
			"decoding_method": "greedy",
			"max_new_tokens": 900,
			"min_new_tokens": 0,
			"repetition_penalty": 1
		},
		"model_id": os.getenv("MODEL_ID", None), 
		"project_id": os.getenv("WX_PROJECT_ID", None) 
	}

	headers = {
		"Accept": "application/json",
		"Content-Type": "application/json",
		"Authorization": "Bearer " + ACCESS_TOKEN
	}

	url = os.getenv("WX_CLOUD_URL", None)
	url = url + "/ml/v1/text/generation?version=2023-05-29"
	response = requests.post(
		url,
		headers=headers,
		json=body
	)

	if response.status_code != 200:
		raise Exception("Non-200 response: " + str(response.text))

	generated_response = response.json()
	return generated_response['results'][0]['generated_text']
	
if __name__ == "__main__":
	prompt = "What is 1 + 1?"
	print(prompt, get_response(prompt))


