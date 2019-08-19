#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function
#from __future__ import unicode_literals

##import requests
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker, ActionExecutionRejection
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import Restarted
##from rasa_sdk.actions import Action
##from rasa_sdk.events import SlotSet

class GetTodaysHoroscope(Action):
    def name(self):
        return 'action_get_todays_horoscope'

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        #user_horoscope_sign = tracker.get_slot('horoscope_sign')
        #base_url = "http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}"
        url = "Test Message"#base_url.format(**{'day': "today", 'sign': user_horoscope_sign})
        #http://horoscope-api.herokuapp.com/horoscope/today/capricorn
        #res = requests.get(url).json
        #todays_horoscope = requests.get(url).json #res.json()['horoscope']
        response = "Your today's horoscope:\n {}".format(url)#todays_horoscope)

        dispatcher.utter_message(response)
        return []#SlotSet("horoscope_sign", user_horoscope_sign)]

    
class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        subscribe = tracker.get_slot('subscribe')
        if subscribe == "True":
            response = "You're successfully subscribed"
        if subscribe == "False":
            response = "You're successfully unsubscribed"

        dispatcher.utter_message(response)
        return [SlotSet("subscribe", subscribe)]
    
    
    