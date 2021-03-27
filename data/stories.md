## say goodbye
* goodbye
  - utter_goodbye


## bot challenge
* bot_challenge
  - action_save_data
  
  
## survey happy path
* greet
    - utter_greet
* affirm
    - survey_form
    - form{"name": "survey_form"}
    - form{"name": null}
    - utter_slots_values	
 	

## survey stop
* greet
    - utter_greet
* affirm
    - survey_form
    - form{"name": "survey_form"}	
* survey_qb
    - utter_ask_qb
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_goodbye
	
## surveya stop
* greet
    - utter_greet
* affirm
    - survey_form
    - form{"name": "survey_form"}	
* survey_qa
    - utter_ask_qa
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_goodbye	

## survey continue
* greet
    - utter_greet
* affirm
    - survey_form
    - form{"name": "survey_form"}
* survey_qb
    - utter_ask_qb
* affirm
    - survey_form
    - form{"name": null}
    - utter_slots_values
	
## surveya continue
* greet
    - utter_greet
* affirm
    - survey_form
    - form{"name": "survey_form"}
* survey_qa
    - utter_ask_qa
* affirm
    - survey_form
    - form{"name": null}
    - utter_slots_values	

## no survey
* greet
    - utter_greet
* deny
    - utter_goodbye