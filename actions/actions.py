from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    ActionExecuted,
    UserUtteranceReverted,
)

class ActionStartConvo(Action):

    def name(self) -> Text:
        return "action_start_convo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        utterances = [e for e in tracker.events_after_latest_restart() if "parse_data" in e]
        
        # get info about user's original message
        entry_user_event = utterances[1]
        # get users first intent
        entry_intent = entry_user_event.get('parse_data').get('intent').get('name')
        

        print(entry_user_event)
        print("====BREAK======")
        print(entry_intent)    
        
        if len(utterances) > 1:
            events = [UserUtteranceReverted(), 
                      ActionExecuted("action_listen"), 
                      # set up the response to the user's first intent
                      entry_user_event]
        else:
            events = []

        return events
