from google import genai
from google.genai import types
from utils.file_reader import get_columnwise_content
import os

class GenAIWrapper:
    def __init__(self):
        self._client = genai.Client(api_key="ENTER_GEMINI_API_KEY_HERE")
        self._model_alias = "gemini-2.0-flash"
    
    def get_client(self):
        return self._client

    def get_model(self):
        return self._model_alias

def get_synopsis_of_csv_content(filename: str):
    LLM = GenAIWrapper()
    file_content = get_columnwise_content(filename=filename)
    llm_client = LLM.get_client()
    llm_model = LLM.get_model()
    llm_response = llm_client.models.generate_content(
        model=llm_model,
        config=types.GenerateContentConfig(
            system_instruction="Imagine you are a good data analyst. Now try to understand the following CSV Content."
        ),
        contents = file_content
    )
    return llm_response.text

    

if __name__ == '__main__':
    print(get_synopsis_of_csv_content('sample.csv'))
