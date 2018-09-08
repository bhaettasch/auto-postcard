from connector import Connector
from pyquery import PyQuery as pq
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

    def get_random_office_for_location(self, location):
        "Return ID of random duty office for given location."

        p = pq('https://www.presseportal.de/blaulicht/dienststellen')
        office_elements = [
            i for sublist
            in [
                c.findall('div')
                for c in p('div.dienststellen-container')
            ]
            for i in sublist
        ]
        offices = [
            (
                dsel.find('a').text.strip(),
                dsel.find('div').text.strip(),
                int(dsel.find('a').attrib['href'].split('/')[-1])
            )
            for dsel in office_elements
            if dsel.find('div') != None
        ]
        office_ids = [
            ds[2]
            for ds in offices
            if location in ds[0]
        ]

        return random.choice(office_ids)

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

        try:
            dienststellen_nr = self.get_random_office_for_location(
                self.params['vacation_location']
            )
            return self.parse_announcement_from_overview(dienststellen_nr)
        except:
            # ¯\_(ツ)_/¯
            return f"\n\n{self.params['sender_name']}"


# DEBUG
if __name__ == "__main__":
    params = {"receiver_name": "Elwood Blues",
              "sender_name": "Jake Blues",
              "receiver_gender": "male",
              "sender_gender": "male",
              "lang": "DE",
              "formal": False,
              "vacation_location": "asdfafdas",
              "vacation_startdate": 1536314400,
              "vacation_enddate": 1536516000
              }

    print(PresseportalConnector(params).get_text())
