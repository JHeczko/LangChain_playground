import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from person_summary.scraping_tools.linkedln import scrape_linkedin
from agents.linked_lookup import lookup_linkedin

def ice_break_with(name: str):
    linkedin_url = lookup_linkedin(name=name)
    linkedin_data = scrape_linkedin(linkedin_url, mock=True)

    messege_template = """
            Given the information {info} about a person from linkedin i want you to create:
            1. Short summary of person
            2. Top 3 interesting fact about him
        """

    prompt_template = PromptTemplate(template=messege_template, input_variables=['info'])

    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash")

    chain = prompt_template | llm

    res = chain.invoke(input={
        "info": linkedin_data
    })

    print(res.content)


if __name__ == "__main__":

    dotenv.load_dotenv()

    print("Welcome to Person Summary AI")

    ice_break_with(name="Michał Jungiewicz Senior Data Scientist GenAI")