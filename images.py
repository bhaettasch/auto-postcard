import flickrapi as flickrapi
import config

class Images:
    def __init__(self):

        pass

    def findImages(locationName):
        flickr = flickrapi.FlickrAPI(config.FLICKR_KEY, config.FLICKR_SECRET, format='etree')
        result = flickr.photos.search(per_page=100,
                                      text=locationName,
                                      tag_mode='all',
                                      content_type=1,
                                      tags=locationName,
                                      extras='url_o',
                                      sort='relevance')
        photos = [p for p in result[0]]
        if len(photos) == 0:
            return False;
        return photos[0].attrib['url_o']


