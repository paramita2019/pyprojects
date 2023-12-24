# Import prerequisite libraries
import os
import openai
import langchain
from langchain.llms import openai
from langchain.llms import OpenAI

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser

from secret_key import openai_key
openai.api_key = openai_key

llm = OpenAI(openai_api_key=(openai.api_key))

response = llm.invoke("List all the chinese zodiac animals")
print ("Lets play Langchain")
print (response)
