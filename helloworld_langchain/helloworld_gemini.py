from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

info_person = """
Pope Leo XIV[a] (born Robert Francis Prevost,[b][c] September 14, 1955) is the head of the Catholic Church and sovereign of the Vatican City State. He is the first pope to have been born in the United States and North America, the first to hold American and Peruvian citizenships, the first from the Order of Saint Augustine, and the second from the Americas after his predecessor Pope Francis.
"""

if __name__ == '__main__':
    mess_template = """
        Given the information {info} about a person from i want you to create:
        1. Short summary of person
        2. Top 3 interesting fact about him
    """

    mess_prompt_template = PromptTemplate(input_variables=["info"], template=mess_template)

    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash")

    chain = mess_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"info": info_person})

    print(res)