from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
    def test_homepage(self):
        """testing the homepage"""

        with self.client:
            response = self.client.get('/')
            #testing for getting the homepage
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))

            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    def test_valid_word(self):
        """Test if word created is valid"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["D", "O", "G", "Z", "X"],
                                ["D", "O", "G", "Z", "X"],
                                ["D", "O", "G", "Z", "X"],
                                ["D", "O", "G", "Z", "X"],
                                ["D", "O", "G", "Z", "X"]]
        response = self.client.get('/check-word?word=dog')
        self.assertEqual(response.json['result'], 'Good')

    def test_invalid_word(self):
        """Test if input word is part of dictionary"""

        self.client.get("/")
        response = self.client.get('/check-word?word=impossible')
        self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Test if word is on board"""

        self.client.get('/')
        response = self.client.get(
            '/check-word?word=asdfasdf'
        )
        self.assertEqual(response.json['result'], 'not-word')