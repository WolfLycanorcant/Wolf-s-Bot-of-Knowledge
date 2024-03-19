import openai
from loguru import logger
import requests
import tempfile
import gradio as gr
from pdf2image import convert_from_path
import pytesseract
import json
from openai import OpenAI

# Configure Loguru logger
logger.add("app.log", rotation="500 MB", level="INFO")

# Simulated client setup for demonstration purposes. Replace with actual client setup.
# Configure OpenAI API
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# Replace these with your actual details
SERPER_API_KEY = "put_your_serper_api_wrapper_api_here"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

history = [
    {"role": "system", "content": "You are an intelligent assistant. Always provide well-reasoned answers that are both correct and helpful."},
]

def ocr_pdf(input_file_path):
    extracted_text = ""
    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path(input_file_path, output_folder=path)
        for image in images:
            extracted_text += pytesseract.image_to_string(image)
    return extracted_text

def search_the_web(query):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    logger.info(f"Searching the web for: {query}")
    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        data = response.json()
        results = []

        # Knowledge Graph
        kg = data.get('knowledgeGraph')
        if kg:
            kg_summary = f"**Knowledge Graph**\nTitle: {kg['title']}\nType: {kg['type']}\nWebsite: {kg['website']}\nDescription: {kg['description']}\n"
            results.append(kg_summary)

        # Organic Search Results
        organic_results = data.get('organic', [])
        if organic_results:
            results.append("**Top Organic Search Results:**")
            for result in organic_results[:5]:  # Limiting to top 5 results for brevity
                org_summary = f"- {result['title']}: {result['link']}\n{result['snippet']}"
                results.append(org_summary)

        # People Also Ask
        paa_results = data.get('peopleAlsoAsk', [])
        if paa_results:
            results.append("\n**People Also Ask:**")
            for paa in paa_results[:3]:  # Limiting to top 3 for brevity
                paa_summary = f"- {paa['question']} {paa['snippet']}"
                results.append(paa_summary)

        # Related Searches
        related_searches = data.get('relatedSearches', [])
        if related_searches:
            results.append("\n**Related Searches:**")
            for related in related_searches[:5]:  # Limiting to top 5 for brevity
                related_summary = f"- {related['query']}"
                results.append(related_summary)

        return "\n".join(results) if results else "No search results found."
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred for: {query} - {http_err}")
        return "Search failed due to an HTTP error."
    except Exception as err:
        logger.error(f"Unexpected error occurred for: {query} - {err}")
        return "Search failed due to an unexpected error."

from loguru import logger

def chat_with_bot(input_text):
    logger.info(f"User input: {input_text}")  # Log user input
    history.append({"role": "user", "content": input_text})
    
    try:
        completion = client.chat.completions.create(
            model="local-model",  # Adjust the model as necessary
            messages=history,
            temperature=0.7,
            stream=True,
        )

        new_message = {"role": "assistant", "content": ""}

        for chunk in completion:
            if chunk.choices[0].delta.content:
                new_message["content"] += chunk.choices[0].delta.content

        history.append(new_message)
        logger.info(f"Assistant response: {new_message['content']}")  # Log assistant response
        return new_message["content"]
    except Exception as e:
        logger.error(f"An error occurred while generating a response: {e}")  # Log any errors during the chat
        return "Sorry, I encountered an error generating a response."


def process_input(input_text=None, input_file=None):
    if input_file is not None:
        if input_file.name.lower().endswith('.pdf'):
            extracted_text = ocr_pdf(input_file.name)
            return chat_with_bot(extracted_text)
        else:
            return "Unsupported file format. Please upload a PDF document."
    elif input_text is not None:
        if "search for" in input_text.lower():
            search_query = input_text.lower().split("search for", 1)[-1].strip()
            search_results = search_the_web(search_query)
            return chat_with_bot(search_results)
        else:
            return chat_with_bot(input_text)
    else:
        return "Please enter some text or upload a PDF document."

iface = gr.Interface(fn=process_input,
                     inputs=[gr.Text(label="Enter your question"), gr.File(label="Or upload a PDF document")],
                     outputs="text",
                     title="Wolf's Bot of Knowledge")
iface.launch(share=True)

