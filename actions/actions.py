from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class SurveyForm(FormAction):

    def name(self):
        return "survey_form"

    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot('confirm_nchi') == True:
            return ["confirm_nchi", "mkowa",
               "maks", "category", "feedback", "maoni"]
        else:
            return ["confirm_nchi", "maks",
              "category", "feedback", "maoni"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "confirm_nchi": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ],
            
            
       
            "feedback": [
                self.from_text(intent="inform"),
                self.from_intent(intent="deny", value="None"),
                
            ],
            "maoni": [
                self.from_text(intent="inform"),
                
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Asante, kwa kazi nzuri!")
        return []

