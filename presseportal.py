from connector import Connector
import random


class PresseportalConnector(Connector):
    """
    Load a random saying from a file
    """
    def get_text(self):
        # TODO


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

    # print(RandomSayingConnector(params).get_text())
