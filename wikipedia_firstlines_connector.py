from connector import Connector
import requests
import wikipedia

# Loading quotes from QuoteSalute
# https://correspsearch.net/quotesalute/
# Licensed under CC-BY-4.0

# More possible params
# https://correspsearch.net/quotesalute/abfrage.xql/?sender=s-m&receiver=r-f&type=informal&language=deu


class WikipediaFirstlinesConnector(Connector):
    """
    Load a random quote from QuoteSalute
    """
    def get_text(self):
        wikipedia.set_lang(self.params["lang"])
        t = f"Ich bin hier in {self.params['vacation_location']}. " if self.params["lang"] == "DE" else f"I'm here in {self.params['vacation_location']}. "
        t += wikipedia.summary(self.params['vacation_location'], sentences=2)
        return t


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

    print(WikipediaFirstlinesConnector(params).get_text())
