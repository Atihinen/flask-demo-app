import xml.etree.ElementTree as ET

class XMLParserLib(object):
    
    def get_movie_title(self, xml_conent, movie_index=1):
        root = ET.fromstring(xml_conent)
        movie_index -= 1
        shows = root.find('Shows').findall('Show')
        return self._parse_movie_titles(shows, movie_index)

    def _parse_movie_titles(self, shows, movie_index):
    	movies = {}
    	for show in shows:
    		event_id = show.find("EventID").text
    		title = show.find("Title").text
    		movies[event_id] = title
    	return movies[movies.keys()[movie_index]]