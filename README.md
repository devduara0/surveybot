# surveybot
This is a simple Rasa bot that uses a form to create a daily log of how the user would rate a site. The full tutorial is available here note: the tutorial is in Swahili

## Running the assistant
Install 

``pip install -r requirements.txt``


 Train the model:

``rasa train``

Open a second terminal window and start the action server:

``rasa run actions --debug``

Return to the first terminal window and start the assistant on the command line:

``rasa run -m models --endpoints endpoints.yml --enable-api --cors "*" --port 5002 --debug``

