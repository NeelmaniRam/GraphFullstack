import requests
import json
from config import GEMINI_API_KEY
from llm.prompts import SQL_PROMPT, ANSWER_PROMPT

# Use gemini-1.5-flash for faster, more accurate structured query generation
MODEL_ID = "gemini-2.5-flash"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_ID}:generateContent?key={GEMINI_API_KEY}"

def call_llm(prompt):
    # Updated payload structure to match Gemini 1.5 API requirements
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.1,  # Low temperature is critical for consistent SQL/Cypher generation
            "maxOutputTokens": 1024
        }
    }

    try:
        response = requests.post(
            GEMINI_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        
        # Raise an exception for 4XX or 5XX errors to help with debugging
        response.raise_for_status()
        data = response.json()
        
        # Return the specific text part from the response candidates
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "Error generating response"

def generate_sql(question):
    return call_llm(SQL_PROMPT.format(question=question))

def generate_answer(result):
    return call_llm(ANSWER_PROMPT.format(result=result))