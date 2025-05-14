# Use a pipeline as a high-level helper
from transformers import pipeline

# Load the pre-trained model
pipe = pipeline("text-generation", model="Lugha-Llama/Lugha-Llama-8B-wura_math_")

# Test the pipeline with an example prompt
output = pipe("Once upon a time in a world where AI was the ruler, ")
print(output)
