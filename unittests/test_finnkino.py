# -*- coding: utf-8 -*-
import unittest
from mock import patch, MagicMock
from services.finnkino import FinnKinoXML
class TestFinnKinoXML(unittest.TestCase):
	
	@patch("services.finnkino.requests")
	def setUp(self, mock_requests):
		self.mock_requests = mock_requests
		self.finnkinoXml = FinnKinoXML()

	@patch("services.finnkino.requests.get")
	def test_get_area_codes(self, mock_requests_get):
		self.assertEqual(len(self.finnkinoXml.areas), 0)
		mock_requests_get.return_value = MockAreaCodes()
		res = self.finnkinoXml.get_area_codes()
		self.assertTrue(isinstance(res, dict))
		self.assertEqual(len(res), 4)
		self.assertEqual("Espoo", res["1012"])

	@patch("services.finnkino.requests.get")
	def test_get_movies_from_area(self, mock_requests_get):
		mock_requests_get.return_value = MockGetMoviesFromArea()
		res = self.finnkinoXml.get_movies_from_area("1012")
		self.assertTrue(isinstance(res, dict))
		self.assertEqual(len(res), 1)
		movie = res[list(res.keys())[0]]
		self.assertTrue("title" in movie)
		self.assertTrue("rating" in movie)
		self.assertTrue("genres" in movie)
		self.assertEqual(movie["title"], "Lumotut")
		self.assertEqual(movie["rating"], 'https://media.finnkino.fi/images/rating_large_12.png')
		self.assertTrue(isinstance(movie["genres"], list))

class MockAreaCodes(object):
	content = """
	<TheatreAreas>
		<TheatreArea>
			<ID>1029</ID>
			<Name>Valitse alue/teatteri</Name>
		</TheatreArea>
		<TheatreArea>
			<ID>1014</ID>
			<Name>Pääkaupunkiseutu</Name>
		</TheatreArea>
		<TheatreArea>
			<ID>1012</ID>
			<Name>Espoo</Name>
		</TheatreArea>
		<TheatreArea>
			<ID>1039</ID>
			<Name>Espoo: Omena</Name>
		</TheatreArea>
	</TheatreAreas>
	"""

class MockGetMoviesFromArea(object):
	content = """
	<Schedule>
		<PubDate>2017-09-26T00:00:00+03:00</PubDate>
		<Shows>
			<Show>
				<ID>1095344</ID>
				<dtAccounting>2017-09-26T00:00:00</dtAccounting>
				<dttmShowStart>2017-09-26T12:15:00</dttmShowStart>
				<dttmShowStartUTC>2017-09-26T09:15:00Z</dttmShowStartUTC>
				<dttmShowEnd>2017-09-26T13:58:00</dttmShowEnd>
				<dttmShowEndUTC>2017-09-26T10:58:00Z</dttmShowEndUTC>
				<ShowSalesStartTime>2000-01-01T00:00:00</ShowSalesStartTime>
				<ShowSalesStartTimeUTC>2000-01-01T00:00:00Z</ShowSalesStartTimeUTC>
				<ShowSalesEndTime>2017-09-26T12:45:00</ShowSalesEndTime>
				<ShowSalesEndTimeUTC>2017-09-26T09:45:00Z</ShowSalesEndTimeUTC>
				<ShowReservationStartTime>2000-01-01T00:00:00</ShowReservationStartTime>
				<ShowReservationStartTimeUTC>2000-01-01T00:00:00Z</ShowReservationStartTimeUTC>
				<ShowReservationEndTime>2017-09-26T12:00:00</ShowReservationEndTime>
				<ShowReservationEndTimeUTC>2017-09-26T09:00:00Z</ShowReservationEndTimeUTC>
				<EventID>302335</EventID>
				<Title>Lumotut</Title>
				<OriginalTitle>The Beguiled</OriginalTitle>
				<ProductionYear>2017</ProductionYear>
				<LengthInMinutes>93</LengthInMinutes>
				<dtLocalRelease>2017-09-01T00:00:00</dtLocalRelease>
				<Rating>12</Rating>
				<RatingLabel>12</RatingLabel>
				<RatingImageUrl>https://media.finnkino.fi/images/rating_large_12.png</RatingImageUrl>
				<EventType>Movie</EventType>
				<Genres>Draama, Jännitys</Genres>
				<TheatreID>1056</TheatreID>
				<TheatreAuditriumID>1311</TheatreAuditriumID>
				<Theatre>Omena, Espoo</Theatre>
				<TheatreAuditorium>sali 4</TheatreAuditorium>
				<TheatreAndAuditorium>Omena, Espoo, sali 4</TheatreAndAuditorium>
				<PresentationMethodAndLanguage/>
				<PresentationMethod/>
				<EventSeries/>
				<ShowURL>http://www.finnkino.fi/Websales/Show/1095344/</ShowURL>
				<EventURL>http://www.finnkino.fi/Event/302335/</EventURL>
				<Images>
					<EventMicroImagePortrait>http://media.finnkino.fi/1012/Event_11680/portrait_micro/TheBeguiled_1080.jpg</EventMicroImagePortrait>
					<EventSmallImagePortrait>http://media.finnkino.fi/1012/Event_11680/portrait_small/TheBeguiled_1080.jpg</EventSmallImagePortrait>
					<EventMediumImagePortrait>http://media.finnkino.fi/1012/Event_11680/portrait_medium/TheBeguiled_1080.jpg</EventMediumImagePortrait>
					<EventLargeImagePortrait>http://media.finnkino.fi/1012/Event_11680/portrait_small/TheBeguiled_1080.jpg</EventLargeImagePortrait>
					<EventSmallImageLandscape>http://media.finnkino.fi/1012/Event_11680/landscape_small/TheBeguiled_444.jpg</EventSmallImageLandscape>
					<EventLargeImageLandscape>http://media.finnkino.fi/1012/Event_11680/landscape_large/TheBeguiled_670.jpg</EventLargeImageLandscape>
				</Images>
				<ContentDescriptors><ContentDescriptor>
				<Name>Disturbing</Name>
				<ImageURL>https://media.finnkino.fi/images/content_Disturbing.png</ImageURL>
				</ContentDescriptor></ContentDescriptors>
			</Show>
		</Shows>
	</Schedule>"""