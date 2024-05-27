import os
from dotenv import load_dotenv, find_dotenv

from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watsonx_ai import Credentials

load_dotenv(find_dotenv())

def get_credentials():
    credentials = Credentials.from_dict({
        'url': os.getenv("WX_CLOUD_URL", None),
        'apikey': os.getenv("IBM_API_KEY", None)
    })
    return credentials

# To display example params enter
GenParams().get_example_values()

generate_params = {
    GenParams.MAX_NEW_TOKENS: 25
}

model = Model(
    model_id=ModelTypes.FLAN_UL2,
    params=generate_params,
    credentials=get_credentials(),
    project_id=os.getenv("WX_PROJECT_ID", None)
    )

prompt = "What is 1 + 1?"
generated_response = model.generate(prompt=prompt)
print(generated_response['results'][0]['generated_text'])