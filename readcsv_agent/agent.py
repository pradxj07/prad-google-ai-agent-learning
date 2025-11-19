from google.adk.agents.llm_agent import Agent

retry_config=types.HttpRetryOptions(
    attempts=2,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)
root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    name='readcsv_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge about csv'
)
