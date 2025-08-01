import os
import requests
import json
import dotenv

dotenv.load_dotenv(dotenv_path="../.env")

def scrape_linkedin(linked_url_profile: str, mock: bool = False):
    scraped_linked_info = None

    if mock:

        file_with_example = open("/Users/wrex/Documents/Projects/LangChain_playground/person_summary/scraping_tools/example.json")
        scraped_linked_info = json.load(file_with_example)["person"]

    else:
        api_scrapin_endpoint = "https://api.scrapin.io/v1/enrichment/profile"
        params = {
                "apikey" : os.environ["SCRAPIN_API_KEY"],
                "linkedInUrl": linked_url_profile,
        }
        response = requests.get(api_scrapin_endpoint, params=params)
        scraped_linked_info = response.json()["person"]

    scraped_linked_info = {
        k: v for k, v in scraped_linked_info.items()
        if v not in ([], "", '', None)
    }

    return scraped_linked_info

if __name__ == "__main__":
    print(scrape_linkedin("https://www.linkedin.com/in/jakub-heczko-316309327/", True))