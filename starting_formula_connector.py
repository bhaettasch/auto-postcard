from connector import Connector,LookupMixin


class StartingFormulaConnector(LookupMixin, Connector):
    """
    Greeting Formula Generator/Connector
    """

    def init(self):
        self.lookup_table = [
            ({"lang": "DE", "receiver_gender": "male", "formal": True}, f"Sehr geehrter {self.params['receiver_name']},\n\n"),
            ({"lang": "DE", "receiver_gender": "female", "formal": True}, f"Sehr geehrte {self.params['receiver_name']},\n\n"),
            ({"lang": "DE"}, f"Hallo {self.params['receiver_name']},\n\n"),
            ({"lang": "EN"}, f"Hi {self.params['receiver_name']},\n\n"),
        ]


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

    print(StartingFormulaConnector(params).get_text())
