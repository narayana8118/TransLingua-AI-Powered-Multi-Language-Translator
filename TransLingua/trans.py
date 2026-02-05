import google.generativeai as genai

genai.configure(api_key="AIzaSyCaWFR0fKLt2BWGq5tEopsgDruNIbPHzbs")

for model in genai.list_models():
    print(model.name, model.supported_generation_methods)
