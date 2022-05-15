import bs4.element
import requests
from bs4 import BeautifulSoup


def is_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, bs4.element.Comment):
        return False
    return True


class WebsiteFetcher:

    def __init__(self):
        self.website_texts = {}

    # this will check if the website has been parsed already, if it has been
    # return the text that exists, avoids querying the website again
    def get_website(self, website: str) -> str:
        if website[:3] == "www":
            website = "http://" + website
        if website not in self.website_texts:
            self.__add_website_data(website)
        return self.website_texts.get(website, "")

    # this function will get the data from the website
    def __add_website_data(self, website: str) -> None:
        try:
            response = requests.get(website)
        except ConnectionError as e:
            print(e)
        except requests.exceptions.MissingSchema as e:
            print("You have not entered in a valid website")
            print(e)
        else:
            if response.status_code != 200:
                print("There has been an issue with accessing the requested website.  There was a response code of "
                      + str(response.status_code) + " " + response.reason + " Please try again.")
                return None

            soup = BeautifulSoup(response.content, 'html.parser')
            texts = soup.findAll(text=True)
            visible_texts = filter(is_visible, texts)
            new_text = " ".join(t.strip() for t in visible_texts)

            self.website_texts[website] = new_text
