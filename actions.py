# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests




#
#
class ActionPredictSalary(Action):

    def name(self) -> Text:
        return "action_salary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = 'http://localhost:5000/predict_api'
        r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})
        response = str(r.json())

        dispatcher.utter_message(response)

        return []
