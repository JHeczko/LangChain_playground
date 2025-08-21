from typing import Tuple

import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from person_summary.scraping_tools.linkedln import scrape_linkedin
from agents.linked_lookup import lookup_linkedin

from output_parsers.output_parser import summary_parser, Summary

def ice_break_with(name: str, mock: bool = True) -> Tuple[Summary, str]:
    linkedin_url = lookup_linkedin(name=name)
    linkedin_data = scrape_linkedin(linkedin_url, mock=mock)

    messege_template = """
            Given the information {info} about a person from linkedin i want you to create:
            1. Short summary of person
            2. Top 3 interesting fact about him
            
            {format_instructions}
        """

    prompt_template = PromptTemplate(
        template=messege_template,
        input_variables=['info'],
        partial_variables={'format_instructions': summary_parser.get_format_instructions()})

    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.0-flash")

    chain = prompt_template | llm | summary_parser

    res = chain.invoke(input={
        "info": linkedin_data
    })

    return res, linkedin_data['photoUrl']

if __name__ == "__main__":

    dotenv.load_dotenv()

    print("Welcome to Person Summary AI")

    ice_break_with(name="Michał Jungiewicz Senior Data Scientist GenAI")