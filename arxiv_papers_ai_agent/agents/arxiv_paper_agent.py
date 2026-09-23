from pydantic_ai import Agent 
from tools.arxiv_tool import searchForPapers, writeHTML
from prompts.ap_prompt import SYSTEM_PROMPT

agent = Agent(
    model = 'openai:gpt-5.2',
    tools = [searchForPapers, writeHTML],
    system_prompt = SYSTEM_PROMPT 
)

async def analyseArxivPapers(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delt=True):
            print(token, end = '')