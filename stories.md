## story_001
* greeting
  - utter_greet
* get_horoscope{"horoscope_sign": "Gemini"}
  - slot{"horoscope_sign": "Gemini"}
  - action_get_todays_horoscope
  - utter_subscribe
  - utter_did_that_help
* subscription
  - slot{"subscribe": "True"}
  - subscribe_user

## story_002a
* greeting
  - utter_greet
* get_horoscope{"horoscope_sign": "Cancer"}
  - slot{"horoscope_sign": "Cancer"}
  - action_get_todays_horoscope
  - utter_subscribe
  - utter_did_that_help
* subscription
  - slot{"subscribe": "True"}
  - subscribe_user

## story_002c
* greeting
  - utter_greet
* get_horoscope{"horoscope_sign": "Aries"}
  - slot{"horoscope_sign": "Aries"}
  - action_get_todays_horoscope
  - utter_did_that_help
  - utter_subscribe
* subscription
  - slot{"subscribe": "True"}
  - subscribe_user

## Horoscope query with horoscope_sign
* greeting
    - utter_greet
* get_horoscope
    - utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign": "capricorn"}
    - slot{"horoscope_sign": "capricorn"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "capricorn"}
    - utter_subscribe
* subscription{"subscribe": "True"}
    - slot{"subscribe": "True"}
    - subscribe_user
    - slot{"subscribe": true}

## Horoscope with sign provided
* greeting
    - utter_greet
* get_horoscope{"horoscope_sign": "leo"}
    - slot{"horoscope_sign": "leo"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "leo"}
    - utter_subscribe
* subscription{"subscribe": "True"}
    - slot{"subscribe": "True"}
    - subscribe_user
    - slot{"subscribe": true}

## When user directly asks for subscription
* greeting
    - utter_greet
* subscription{"subscribe": "True"}
    - slot{"subscribe": "True"}
    - subscribe_user
    - slot{"subscribe": true}
