from .countries import countries
class GoogleMapsMarkers(object):
    '''
    Use a list as expeted by GoogleMaps markers
    '''
    def __init__(self):
        self.markers = []

    def save_match(self, infobox, lat, lng):
        self.markers.append({
            'infobox': infobox,
            'lat': lat,
            'lng': lng
        })

    def save_with_url_or_twitId(self, twitt):
        '''
        Decides what metadata from the twitt will be displayed in the map
        '''
        if twitt.urls:
            return ''.join(["<p><a href=\"", twitt.urls[0].url,
                            "\">See article</a></p><p><a href=\"https://twitter.com/",
                            twitt.user.screen_name, "/status/", twitt.id_str,
                            "\">See twitt online</a></p>"])
        else:
            return ''.join(["<p><a href=\"https://twitter.com/", twitt.user.screen_name,
                            "/status/", twitt.id_str, "\">See twitt online</a></p>"])


    def find_coordinates(self, twittsstatuses):
        for twitt in twittsstatuses:
            for hashtag in twitt.hashtags:
                hashtag_lowc = hashtag.text.lower()
                if countries.get(hashtag_lowc, None):
                    infobox = self.save_with_url_or_twitId(twitt)
                    self.save_match(infobox, countries.get(hashtag_lowc)['lat'], countries.get(hashtag_lowc)['lng'])
            
            # # Search country by country code
            #     if twitt.place and twitt.place.get('country_code').lower() == country.name:
            #         infobox = self.save_with_url_or_twitId(twitt)
            #         self.save_match(infobox, country.lat, country.lng)

            # # Check if there are coordinates from Twitter API
            # if twitt.coordinates:
            #     lng, lat = twitt.coordinates.get('coordinates', None)
            #     infobox = self.save_with_url_or_twitId(twitt)
            #     self.save_match(infobox, lat, lng)
