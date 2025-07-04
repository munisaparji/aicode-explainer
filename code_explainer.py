from gpt4all import GPT4All

# Set these correctly
MODEL_NAME = "DeepSeek-R1-Distill-Llama-8B-Q4_0.gguf"
MODEL_PATH = "C:\\Users\\munis\\AppData\\Local\\nomic.ai\\GPT4All"

# Load the model
model = GPT4All(model_name=MODEL_NAME, model_path=MODEL_PATH)

def explain_code(code, language="Python"):
    prompt = f"Explain the following {language} code in simple terms for a beginner:\n\n{code}\n\nExplanation:"
    
    with model.chat_session():
        response = model.generate(
            prompt=prompt,
            temp=0.5,
            max_tokens=500
        )
    
    return response.strip()
