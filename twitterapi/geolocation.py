class GoogleMapsMarkers(object):
    '''
    Use a list as expeted by GoogleMaps markers
    '''
    def __init__(self):
        self.markers = []

    def save_match(self, twittid, lat, lng):
        self.markers.append({
            'infobox': twittid,
            'lat': lat,
            'lng': lng
        })

    def save_with_url_or_twitId(self, twitt):
        '''
        Decides what metadata from the twitt will be displayed in the map
        '''
        if twitt.urls:
            return twitt.urls[0].url
        else:
            return twitt.id_str

    def check_hashtags(self, twitt, country):
        for hashtag in twitt.hashtags:
            if hashtag.text.lower() == country.name:
                infobox = self.save_with_url_or_twitId(twitt)
                self.save_match(infobox, country.lat, country.lng)

    def find_coordinates(self, twittsstatuses, countries):
        for twitt in twittsstatuses:
            for country in countries:
                self.check_hashtags(twitt, country)
                # there is no point about matching the same country twice
                # for the same twitt
                if twitt.place and twitt.place.get('country_code').upper() == country.name:
                    infobox = self.save_with_url_or_twitId(twitt)
                    self.save_match(infobox, country.lat, country.lng)
            if twitt.coordinates:
                lng, lat = twitt.coordinates.get('coordinates', None)
                infobox = self.save_with_url_or_twitId(twitt)
                self.save_match(infobox, lat, lng)
