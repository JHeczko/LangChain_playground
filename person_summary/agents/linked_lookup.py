import dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import Tool
from langchain import hub

from person_summary.tools.tools import get_profile_url_tavily

dotenv.load_dotenv("../.env")

def lookup_linkedin(name: str) -> str:
    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash")

    template = '''
    given the full name {full_name_person} i want you to get it me a link to their linkedin profile page. Your answer should contain only URL
    '''

    prompt_template = PromptTemplate(
        template=template,
        input_variables=['full_name_person'])

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the linkedin profile page URL"
        )
    ]

    react_prompt: PromptTemplate = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, prompt=react_prompt, tools=tools_for_agent)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input = {
            "input": prompt_template.format_prompt(full_name_person=name)
        }
    )

    linked_profile_url = result['output']
    return linked_profile_url

if __name__ == "__main__":
    linked_url = lookup_linkedin("Eden Marco")
    print(linked_url)