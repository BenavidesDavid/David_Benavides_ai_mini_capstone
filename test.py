from langchain.chat_models import AzureChatOpenAI
from langchain.callbacks import get_openai_callback
import os

os.environ['OPENAI_API_TYPE'] = 'azure'
os.environ['OPENAI_API_VERSION'] = '2023-07-01-preview'
os.environ['OPENAI_API_KEY'] = "999193bdb1534b8582ca4d521ae3f679"
os.environ['OPENAI_API_BASE'] = "https://intern-test.openai.azure.com/"

llm = AzureChatOpenAI(deployment_name="intern_deployment", model_name="gpt-35-turbo", temperature=0)
with get_openai_callback() as cb:
    result = llm.invoke("Tell me a joke")
    print(f"\n Total Tokens: {cb.total_tokens}")
    print(f" Prompt Tokens: {cb.prompt_tokens}")
    print(f" Completion Tokens: {cb.completion_tokens}")
    print(f" Total Cost (USD): ${cb.total_cost}")
    print(result)