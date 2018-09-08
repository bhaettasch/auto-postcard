from connector import Connector
import requests

# Loading quotes from QuoteSalute
# https://correspsearch.net/quotesalute/
# Licensed under CC-BY-4.0

# More possible params
# https://correspsearch.net/quotesalute/abfrage.xql/?sender=s-m&receiver=r-f&type=informal&language=deu


class QuoteConnector(Connector):
    """
    Load a random quote from QuoteSalute
    """
    def get_text(self):
        lang_string = "deu" if self.params["lang"] == "DE" else "eng"
        request = requests.get(f"https://correspsearch.net/quotesalute/abfrage.xql/?language={lang_string}")
        if request.status_code == 200:
            answer_json = request.json()
            return f"\n\n{answer_json['quote']}\n{self.params['sender_name']}"
        else:
            return f"\n\n{self.params['sender_name']}"


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

    print(QuoteConnector(params).get_text())
