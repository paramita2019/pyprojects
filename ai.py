#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create GPTs using Openai API calls

@author: paramitapradhan

https://platform.openai.com/account/limits
"""

import openai
from secret_key import openai_key
import warnings
warnings.filterwarnings("ignore",message="Reloaded modules: secret_key")

openai.api_key = openai_key

def Job_sample():
    #prompt = 'Get the company name and job role'
    #API call
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {'role' : 'user','content' : 'Get the company name and job role'}
            # this is a dict - key value pair
            # role could be a user, system or assistant
        ],
        max_tokens = 1,
        # max number of words we're asking the API to send back in the response
        n=5,
        # controls the number of responses sent back by the API model
        temperature=0
        #controls how random or predictable you would like the response to be based on the GPT's purpose
        # 0 - very predictable & deterministic | 2 - very random & out there
    )
    #API response in hierarchical JSON format
    response.to_dict()
    
    # the choices field is what holds the response from this language model
    # here we're interested in the CONTENT of the first element at index 0
    # this is equivalent to going to ChatGPT and typing in 'Get the company name and job role'
    #print(response.choices[0]['message']['content'])
    


def Chatbot_sample():
    #prompt = 'Get the company name and job role'
    #API call
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {'role' : 'system','content' : 'Hi there! Anything i can help you with today?'},
            {'role' : 'user','content' : 'The Payments Tracker isnt loading for me. Can you help me?'},
            {'role' : 'assistant','content' : 'Thank you for catching that! Let me restart the Payments Tracker for you'},
            {'role' : 'assistant','content' : 'I have also opened an Incident to notify our helpers and track this issue'},
            {'role' : 'user','content' : 'The Tracker is back up now. Thanks for your welcome'},
            {'role' : 'assistant','content' : 'Glad its working for you. Please let me know if there\'s anything else i can help with'}
        ],
        max_tokens = 15,
        n=1,
        temperature=0
    )
    print(response.choices[0]['message']['content'])
    
    
    
if __name__ == '__main__':
    print(openai.Model.list())      # no api calls via token made here
    #Job_sample()
    #Chatbot_sample()