import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType

openai_api_key = "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"

def load_csv(input_csv):
  df = pd.read_csv(input_csv)
  return df
  
# Generate LLM response
def generate_response(csv_file, input_query):
  try:
    llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key=openai_api_key)
    df = load_csv(csv_file)
    # Create Pandas DataFrame Agent
    agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)
    # Perform Query using the Agent
    response = agent.run(input_query)
    return response
  except Exception as e:
    print(f"An error occurred at generate_response: {e}")

print(generate_response("MSFT_1000_days_analysis.csv", "How Many Rows Are There?"))