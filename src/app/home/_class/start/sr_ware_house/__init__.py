"""Initialize Google's Gemini AI Api Key"""

# Include external packages and modules.
import google.generativeai as genai # type: ignore

# Configure API KEY
genai.configure(api_key="YOUR_API_KEY") # type: ignore
