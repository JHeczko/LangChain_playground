from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

info_person = """
Pope Leo XIV[a] (born Robert Francis Prevost,[b][c] September 14, 1955) is the head of the Catholic Church and sovereign of the Vatican City State. He is the first pope to have been born in the United States and North America, the first to hold American and Peruvian citizenships, the first from the Order of Saint Augustine, and the second from the Americas after his predecessor Pope Francis.
"""

load_dotenv()

if __name__ == '__main__':
    mess_template = """
        Given the information {info} about a person from i want you to create:
        1. Short summary of person
        2. Top 3 interesting fact about him
    """

    mess_prompt_template = PromptTemplate(input_variables=['info'], template=mess_template)

    llm = ChatOllama(model='phi3')

    chain = mess_prompt_template | llm

    res = chain.invoke(input={'info': info_person})

    print(res)
