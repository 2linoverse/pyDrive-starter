# pyDrive-starter
Setup Google Drive API on a Remote Server With Python

## step 1
setup google cloud console

- create a new project
- select the project
- enable google drive api

## step 2 setup oauth account
- go to apis and services -> credentials
- create new oauth 2.0 credentials
- configure oauth consent
- go to audience -> set your email as a test users

## step 3 setup oauth credential
- go to apis and service -> credentials
- create oauth 2.0 credentials
- select web application
- put this in authorized redirect url `http://localhost:8080/`
- create -> download credentials
- save to your folder
- rename as client_secret.json


## step 4
setup local python environment

download the files to a folder on your computer

create a python virtual environment
python -m venv .venv

activate it
source .venv/bin/activate

install requirements
pip install -r requirements.txt

get refresh token
- run get_refresh_token on your local machine
- python get_refresh_token.py
- copy the refresh token in the cli
- `ctrl + shift + c` to copy selected text in shell

## step 5

new empty replit project
bring files into project

set environment secrets
- set it as REFRESH_TOKEN secret environment variable in your replit project
- also get your CLIENT_ID and CLIENT_SECRET from client_secret.json

- make sure requirements are installed first
- run python google_drive.py

[] means it worked



## RESOURCES:

google drive api python quickstart:
https://developers.google.com/workspace/drive/api/quickstart/python

google drive api reference docs:
https://developers.google.com/workspace/drive/api/reference/rest/v3

google python samples:
https://github.com/googleworkspace/python-samples/blob/main/drive/quickstart/quickstart.py


checkout the coder world for windows/linux pc tutorials:
https://www.youtube.com/@thecoderworld/videos


and lastly checkout [MVP] Jie Jenn's tutorials on Google Cloud setup:
https://www.youtube.com/watch?v=6bzzpda63H0

and his whole Google Drive Api tutorials playlist!
https://www.youtube.com/watch?v=9K2P2bWEd90&list=PL3JVwFmb_BnTamTxXbmlwpspYdpmaHdbz


As always we are standing on the shoulders of giants

thanks for watching! ... or rather, for reading/following along with this tutorial
