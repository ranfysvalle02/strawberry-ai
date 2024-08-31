![](https://tii.imgix.net/production/articles/13494/3737c64b-90b1-4167-8d70-601b9670083c.png?auto=compress&fit=crop&auto=format)

# AI Counting Crisis

AI systems like **GPT-4o** and **Claude**, despite their advanced capabilities, struggle with seemingly simple tasks such as counting the number of times a letter appears in a word. 

For instance, they incorrectly state that the letter "r" appears twice in the word "strawberry". This might seem like a trivial mistake, but it's indicative of a larger truth: AI systems don't think like humans. They don't have brains, and they don't understand text in the way we do.

```
gpt-4o
The word "Strawberry" contains 2 instances of the letter 'r'.
------------
gpt-4o + exec
The word "Strawberry" contains 3 instances of the letter "r"
```

It's important to note that while large language models can process and generate text, they do not possess the same cognitive abilities as humans. They cannot truly "count" or perform arithmetic operations in the same way that humans do. Their ability to manipulate symbols is optimized for different tasks, such as language generation and understanding. While they can process numerical information, they do not have the same underlying understanding of quantity as humans.

## **Counting: A Philosophical Exploration**

The act of counting, a seemingly simple human ability, is rooted in complex cognitive processes and has profound cultural implications. While most cultures have developed sophisticated numerical systems, there are exceptions, such as the Pirahã tribe, who lack a robust system for counting beyond small numbers.

In classical physics, counting is straightforward. We can count the number of particles in a system, their locations, or their momentum. However, in quantum physics, the very act of counting becomes more complex due to superposition.

How do you count something that exists in multiple states at once? Is a particle in a superposition of states counted as one particle or many? These questions challenge our traditional understanding of counting and force us to rethink how we quantify the physical world.

**The Philosophy of Counting**

Counting involves the following steps:

1. **Identification:** Recognizing individual objects or events.
2. **Abstraction:** Focusing on the quantity rather than specific qualities.
3. **Sequencing:** Establishing an order for counting.
4. **Association:** Linking each object with a numerical label.
5. **Iteration:** Repeating the process for all objects.

## The Role of Transformers in LLMs

**Large Language Models (LLMs)** are built on **transformers**, a type of deep learning architecture. These transformers break text into tokens, which can be full words, syllables, or letters, depending on the model. However, they do not actually read text. 

Instead, they translate prompts into an encoding. For example, they understand the word "the" as a single encoding, but do not recognize the individual letters "T", "H", and "E". 

## Understanding Tokenization

Tokenization is a crucial process in LLMs. It is the process of breaking down text into smaller pieces, called tokens. These tokens can be as small as a single character or as large as a word. The way an LLM tokenizes text can greatly affect its understanding and interpretation of the text.

LLMs are good at semantically figuring out what they need to do. As the models get better at code generation, the connection between the 'thought' of what needs to happen in code will become increasingly better. This means that as LLMs improve, they will be able to generate more accurate and efficient code based on the prompts they receive.

## The Complexity of the Problem

This issue is deeply embedded in the architecture of these LLMs and is not easy to fix. The problem becomes even more complex as the LLM learns more languages, as different languages have different rules for tokenization.

## A Potential Solution: Code Generation

However, there may be a simple solution to this problem: having the LLM generate code, and then executing that code! LLMs are already good at code generation, and they are only improving with time and adoption. 

This approach could potentially bypass the limitations of the LLM's tokenization process, allowing it to perform tasks like counting the number of times a letter appears in a word with greater accuracy. 

By leveraging the LLM's ability to generate code, we can harness its strengths and mitigate its weaknesses, opening up new possibilities for AI applications.

## The Risks

There are several dangers associated with using Python's `exec` function in the way this example proposes:

**1. Security Risk:** 

* `exec` allows you to execute **arbitrary Python code**. This means if the LLM generates malicious code disguised as a function to answer the prompt, it could be executed by `exec` potentially compromising your system. This is especially risky if the LLM is exposed to untrusted user input.

**2. Unintended Behavior:**

* The LLM might not understand the full context of what it needs to generate. It could create a function that seems to work for the specific prompt ("counting r's in Strawberry") but fails for more complex scenarios. This could lead to unexpected results and errors down the line.

**3. Debugging Challenges:**

* If the generated code is complex or poorly written, debugging it becomes a challenge. You wouldn't have the benefit of a well-defined function written by a human developer, making it harder to track down issues.


[Why can't AI spell strawberry? by TechCrunch](https://techcrunch.com/2024/08/27/why-ai-cant-spell-strawberry/)

## Example: Code Generation in Action ~50 lines of code

```python

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
- Must use absolutely no librarys. Must be a pure python function.
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

```

