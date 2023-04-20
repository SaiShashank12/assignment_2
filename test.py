import unittest
import json
from weather_flask import app, db, WeatherRecord, Station, WeatherStats

class TestWeatherAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up test database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()
        cls.client = app.test_client()
        cls.station = Station(name='Test Station', state='CA', latitude=37.7749, longitude=-122.4194)
        db.session.add(cls.station)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        # Clean up test database
        db.session.remove()
        db.drop_all()

    def test_get_weather_records(self):
        # Test GET /api/weather
        record = WeatherRecord(station_id=self.station.id, date='2023-04-19', max_temp=25.0, min_temp=15.0, precipitation=0.0)
        db.session.add(record)
        db.session.commit()
        response = self.client.get('/api/weather?station_id={}'.format(self.station.id))
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['items']), 1)
        self.assertEqual(data['items'][0]['station_id'], self.station.id)

    def test_get_weather_stats(self):
        # Test GET /api/weather/stats
        stats = WeatherStats(station_id=self.station.id, year=2023, avg_max_temp=30.0, avg_min_temp=20.0, total_precipitation=0.0)
        db.session.add(stats)
        db.session.commit()
        response = self.client.get('/api/weather/stats?station_id={}'.format(self.station.id))
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['station_id'], self.station.id)
