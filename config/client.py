from langchain_aws import ChatBedrockConverse
from dotenv import load_dotenv
import os

load_dotenv()

profile_arn = os.getenv("BEDROCK_INFERENCE_PROFILE_ARN")
region = os.getenv("AWS_DEFAULT_REGION")

from google import genai

client = genai.Client(
        api_key= os.getenv('GOOGLE_API_KEY'),
)
model = "gemini-2.5-flash-lite"
# model = ChatBedrockConverse(
#     model=profile_arn,
#     provider="anthropic",
#     temperature=0.5,
#     region_name=region
# )
