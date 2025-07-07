import unittest
from unittest.mock import patch, Mock
import requests
from client.api_client import ApiClient
from client.models import PriceData

class TestApiClient(unittest.TestCase):

    def setUp(self):
        self.client = ApiClient()

    @patch('client.api_client.requests.get')
    def test_get_crypto_prices_success(self, mock_get):
        """Test a successful API call."""
        # Configure the mock to simulate a successful API response
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "bitcoin": {"usd": 50000.0},
            "ethereum": {"usd": 3000.0}
        }
        mock_get.return_value = mock_response

        # Call the method we are testing
        prices = self.client.get_crypto_prices(["bitcoin", "ethereum"], "usd")

        # Assert that the correct data was returned
        self.assertIsInstance(prices, list)
        self.assertEqual(len(prices), 2)
        self.assertEqual(prices[0], PriceData(id='bitcoin', price=50000.0, currency='usd'))
        self.assertEqual(prices[1], PriceData(id='ethereum', price=3000.0, currency='usd'))

        # Assert that requests.get was called with the correct URL and params
        mock_get.assert_called_once_with(
            "https://api.coingecko.com/api/v3/simple/price",
            params={'ids': 'bitcoin,ethereum', 'vs_currencies': 'usd'},
            timeout=10
        )

    

@patch('client.api_client.print')
@patch('client.api_client.requests.get')
def test_get_crypto_prices_network_error(self, mock_get, mock_print):
    """Test the handling of a network error without printing."""
    mock_get.side_effect = requests.exceptions.RequestException("Connection error")

    prices = self.client.get_crypto_prices(["bitcoin"], "usd")
    
    # Assert that print was called with the correct error message
    mock_print.assert_called_once_with("❌ Network Error: Could not connect to the API. Connection error")
    
    # Assert the function returned None
    self.assertIsNone(prices)