import os
from dotenv import load_dotenv, find_dotenv

from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watsonx_ai import Credentials

import warnings
warnings.filterwarnings('ignore')

load_dotenv(find_dotenv())

def get_response(prompt):
    credentials = Credentials.from_dict({
        'url': os.getenv("WX_CLOUD_URL", None),
        'apikey': os.getenv("IBM_API_KEY", None)
    })
    
    # To display example params enter
    GenParams().get_example_values()

    generate_params = {
        GenParams.MAX_NEW_TOKENS: 25
    }

    model = Model(
        model_id=os.getenv("MODEL_ID", None), #"ibm/granite-13b-instruct-v2",
        params=generate_params,
        credentials=credentials,
        project_id=os.getenv("WX_PROJECT_ID", None)
        )
    generated_response = model.generate(prompt=prompt)
    return generated_response['results'][0]['generated_text']

if __name__ == "__main__":
    prompt = "What is 1 + 1?"
    print(prompt, get_response(prompt))