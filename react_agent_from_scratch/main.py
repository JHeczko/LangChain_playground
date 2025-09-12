from configparser import ParsingError
from typing import Union, List

from dotenv import load_dotenv
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain.tools import tool
from langchain_community.chat_models import ChatOpenAI
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import render_text_description, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from sqlalchemy.testing.plugin.plugin_base import stop_test_class

load_dotenv()

@tool
def get_text_length(text:str) -> int:
    '''
    The function take the string and return its length based on number of characters in it.
    :param text: the text give
    :return: returns the length of the text based on number of characters in it.
    '''

    if type(text) != str:
        try:
            text = str(text)
        except:
            raise ParsingError

    text.strip("'\n").strip('"')
    return len(text)

def find_tool(tools: List[Tool], tool_name: str) -> Tool | None:
    for tool in tools:
        if tool.name == tool_name:
            return tool

if __name__ == "__main__":
    tools = [get_text_length]

    whole_template = '''
    Answer the following questions as best you can. You have access to the following tools:

    {tools}
    
    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    Begin!
    
    Question: {input}
    Thought:
    '''

    template = '''
        Answer the following questions as best you can. You have access to the following tools:

        {tools}

        Use the following format:

        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action

        Begin!

        Question: {input}
        Thought:
        '''

    prompt = PromptTemplate.from_template(template=whole_template).partial(tools=render_text_description(tools), tool_names=", ".join([t.name for t in tools]))

    llm = ChatGoogleGenerativeAI(temperature=1.5, model="gemini-2.0-flash").bind(stop=["\nObservation", "Observation:", "Observation "])
    agent = {"input" : lambda x : x["input"]} | prompt | llm | ReActSingleInputOutputParser()

    agent_action: Union[AgentAction, AgentFinish] = agent.invoke({"input" : "What the length of word in characters: DOG "})
    print(agent_action)

    if isinstance(agent_action, AgentAction):
        tool_name = agent_action.tool
        tool_to_use = find_tool(tools, tool_name)
        tool_input = agent_action.tool_input

        observation = tool_to_use.func(tool_input)

        print(observation)

