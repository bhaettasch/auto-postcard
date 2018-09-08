from connector import Connector
import requests


class BahnConnector(Connector):

    def get_text(self):
        url = ("https://dbf.finalrewind.org/" +
                params["train_station"] + "?mode=marudor&version=3")


        r = requests.get(url)
        j  = r.json()


        for departure in j['departures']:

            if departure['train'] == params["train_number"]:

                if departure['delayArrival'] < 10:
                    returnstring = "Entgegen jeglicher Erwartung kam mein Zug pünklich an"

                else:
                    returnstring = "Unser Zug nach " + params["vacation_location"] + " kam aufgrund von "

                    for message in departure['messages']['delay']:
                        returnstring += message['text'] + ", "
                        returnstring += "leider " + str(departure['delayArrival']) + " Minuten zu spät an. Deutsch Bahn halt. Was erwartet 1 Mensch? :->"

                return returnstring


if __name__ == "__main__":
    params = {  "receiver_name": "Elwood Blues",
                "sender_name": "Jake Blues",
                "receiver_gender": "male",
                "sender_gender": "male",
                "lang": "DE",
                "formal": False,
                "vacation_location": "Marburg",
                "vacation_startdate": 1536314400,
                "vacation_enddate": 1536516000,
                "train_number": "RB 42",
                "train_station": "Marburg(Lahn)"
                }
    print(BahnConnector(params).get_text())

