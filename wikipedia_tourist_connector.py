from connector import Connector
import random
import requests
import wikipedia


class WikipediaTourismConnector(Connector):
    """
    Load a random saying from a file
    """
    def get_text(self):
        wiki = wikipedia.page(self.params['vacation_location']).section('Tourism')
        text = '\n\nIt is very nice here. '
        if wiki:
            text += wiki.split('. ')[0] + '.'
        return text


# DEBUG
if __name__ == "__main__":
    params = {"receiver_name": "Elwood Blues",
              "sender_name": "Jake Blues",
              "receiver_gender": "male",
              "sender_gender": "male",
              "lang": "DE",
              "formal": False,
              "vacation_location": "Chicago",
              "vacation_startdate": 1536314400,
              "vacation_enddate": 1536516000
              }

    print(RandomSayingConnector(params).get_text())
