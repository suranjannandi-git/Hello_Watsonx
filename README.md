## Accessing IBM watsonx foundation models

### Create virtual environment
python3.12 -m venv venv-dev
source venv-dev/bin/activate

### Environment Setup
Copy the .env.example file to a new file named .env and update the key values.

### Install libraries
pip install -r requirements.txt


### Execute the code
We have both SDK and API call code

##### Execute with SDK
python call_wx_restapi.py

##### Execute with API call
python call_wx_sdk.py


docker build -t hello_watsonx .
docker run hello_watsonx:latest       
docker run -d --env-file ~/.env -p 5000:5000 --name hello_watsonx hello_watsonx:latest
docker logs -f hello_watsonx