from connector import Connector
from lxml import html
from re import search as re_search
import random
import requests


class PresseportalConnector(Connector):

    @staticmethod
    def parse_announcement_title(pm_location):
        "Returns title of PRESSEMITTEILUNG."
        
        req = requests.get(f"https://www.presseportal.de{pm_location}")
        if req.status_code == 200:
            content = html.fromstring(req.content)
            return content.findtext(".//title")
        else:
            return None

    def parse_announcement_from_overview(self, nr):
        """ Returns a random PRESSEMITTEILUNG for the region by the given number
            as present in the original URL.
        """

        req = requests.get(f"https://www.presseportal.de/blaulicht/nr/{nr}")
        if req.status_code != 200:
            return "\n\n{self.params['sender_name']}"

        content = html.fromstring(req.content)
        urls = [url for url in content.xpath("//a/@href")
                if url.startswith("/blaulicht/pm/")]

        # Ten tries, because dunno
        for i in range(10):
            try:
                rand_title = PresseportalConnector.parse_announcement_title(
                        random.choice(urls))

                title = re_search(":(.*) \| Presseportal", rand_title). \
                        group(1).strip()

                return f"\n\n{title}\n{self.params['sender_name']}"
            except:
                pass

        return f"\n\n{self.params['sender_name']}"

    def get_text(self):
        ''' Returns a random PRESSEMITTEILUNG (press release) from the German
            police or something similar for the requested region.
        '''

        dienststellen_nr = 43648  # TODO: select this by region
        return self.parse_announcement_from_overview(dienststellen_nr)


# DEBUG
if __name__ == "__main__":
    params = {"receiver_name": "Elwood Blues",
              "sender_name": "Jake Blues",
              "receiver_gender": "male",
              "sender_gender": "male",
              "lang": "DE",
              "formal": False,
              "vacation_location": "Darmstadt",
              "vacation_startdate": 1536314400,
              "vacation_enddate": 1536516000
              }

    print(PresseportalConnector(params).get_text())
