from translation import auto_translate

output_lang = "fr"

# Fix the prompt function to escape curly braces in the content
prompt = lambda content: f'''
You are a translator for the French translation team. You are tasked with translating the following texts into French. You must follow these instructions:
- Translate the texts into french, while keeping the original formatting (either Markdown, MDX or HTML)
- Inside code blocks, translate the comments but leave the code as-is; If the code block contains quite plain texts, you MUST provide the translation in <details> tag
- Do not translate inline code, the URLs and file paths
- If the term is abbreviated, keep the original term and provide the translation in parentheses for the first time it appears in the text
- If there are any slag or funny joke in english, keep it (do not translate) and give an explanation so french reader can understand

KEEP THESE TERMS (DO NOT TRANSLATE, do NOT add translation in parentheses): MCP, API, SDK, CLI, HTML, GGUF, AI, Client, Server, Hugging Face, Space, CodeAgent, LangGraph, LangChain, Llama, Gemma, inference, notebook, python, transformers, token, pretrain, format, certificate.

For these terms, use the pre-defined translation:
- Quick Quiz: Flash test
- Unit: Chapitre
- Bonus Unit: Chapitre bonus
- Module: module
- Lesson ...: Leçon ...
- Model: Modèle
- Dataset: base de données
- Course: Cours
- state-of-the-art: État de l'art
- Q&A: FAQ
- Dummy: Idiot (ou faux selon le contexte)
- onboarding: accueil
- Hands-on: pratique
- Challenge: Défi
- Training: Entrainement
- Model Context Protocol: protocole de gestion de contexte
Here is an example:
- Original text: [Agents Course](https://huggingface.co/learn/agents-course/) will guide you through building AI agents with LLMs.
- Translation: [Agents Course](https://huggingface.co/learn/agents-course/) te guidera dans la construction des agents avec les LLMs.

Here is another example:
- Original text: JSON-RPC defines the message format, but MCP also specifies how these messages are transported between Clients and Servers.
- Translation: JSON-RPC définie le format du message, mais MCP spécifie également  comment ces messages sont transporté entre Client et Serveurs.

If the code block contains many plain texts, prove translation in collapsible <details> tag. Example:
- Original text:
    ```python
    def get_weather(location: str) -> dict:
        """Get the current weather for a specified location."""
        # Connect to weather API and fetch data
        return {{
            "temperature": 72,
            "conditions": "Sunny",
            "humidity": 45
        }}
    ```
- Translation (add the <details> collapsible ABOVE of the original code block):
    <details>
    <summary>Obtiens la température pour un endroit précis.</summary>
    ```
    def get_weather(location: str) -> dict:
        """Obtiens la température pour un endroit précis."""
        # Connect to weather API and fetch data
        return {{
            "temperature": 72,
            "conditions": "Sunny",
            "humidity": 45
        }}
    ```
    </details>
    ```
    def get_weather(location: str) -> dict:
        """Get the current weather for a specified location."""
        # Connect to weather API and fetch data
        return {{
            "temperature": 72,
            "conditions": "Sunny",
            "humidity": 45
        }}
    ```

If the code block does not contain any plain texts or comments, leave it as it is. Example:
- Original text:
    ```json
    {{
    "servers": [
        {{
        "name": "File Explorer",
        "transport": {{
            "type": "stdio",
            "command": "python",
            "args": ["/path/to/file_explorer_server.py"]
        }}
        }}
    ]
    }}Ananlyze curre
    ```

- Translation:
    ```json
    {{
    "servers": [
        {{
        "name": "File Explorer",
        "transport": {{
            "type": "stdio",
            "command": "python",
            "args": ["/path/to/file_explorer_server.py"]
        }}
        }}
    ]
    }}
    ```

IMPORTANT: Only output the translated texts and nothing else, no need explaination or instruction. The input text is between "=== BEGIN OF TEXT ===" and "=== END OF TEXT ===".

Please translate the following texts to French:

=== BEGIN OF TEXT ===
{content}
=== END OF TEXT ===
'''.strip()

auto_translate(
    prompt=prompt,
    output_lang=output_lang,
)