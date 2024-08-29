
import json
from openai import AzureOpenAI

# Define constants
AZURE_OPENAI_ENDPOINT = ""
AZURE_OPENAI_API_KEY = "" 
az_client = AzureOpenAI(azure_endpoint=AZURE_OPENAI_ENDPOINT,api_version="2023-07-01-preview",api_key=AZURE_OPENAI_API_KEY)


ai_response = az_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "How many `r` in the word `Strawberry`?"},
    ]
)
print("gpt-4o")
print(ai_response.choices[0].message.content)
print("------------")
tricky_prompt = "How many `r` in the word `Strawberry`?"#input("Enter the tricky prompt: ")
#response_format={"type": "json_object"}
ai_response = az_client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "user", "content": "Return a JSON object that includes a Python function that can answer:`"+tricky_prompt+"`"},
        {"role": "user", "content": f"""
[function criteria]
- Must be valid Python 3. IMPORTANT!
- Must use absolutely no libraries. Must be a pure python function.
- Make sure to use proper PIP formatting.
- Think critically and step by step. You are an expert Python developer.
         
[response criteria]
- Must return a JSON object with a single key `new_fn` with the full function definition as a string.
- Must be valid Python 3.
- Please remember to use the function name `py_code` for the function name.
"""}
    ],
)
fn_1 = json.loads(ai_response.choices[0].message.content)
fn_1 = fn_1["new_fn"]
exec(fn_1)
result = py_code()
print("gpt-4o + exec")
print('The word "Strawberry" contains ' + str(result) + ' instances of the letter "r"')
