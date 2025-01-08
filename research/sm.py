import os

# Set the environment variable directly in the script
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\kolla\\Desktop\\Jupyter\\task\\my_credentials.json"


# Check if the environment variable is set
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if credentials_path:
    print(f"Using credentials from: {credentials_path}")
    try:
        genai.configure(api_key="your_api_key_here")  # Configure the API key
        # Continue with your code
    except Exception as e:
        print("Error: Could not load the credentials.")
        print(e)
else:
    print("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")

