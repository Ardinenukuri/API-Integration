# client/api_client.py

import requests
from typing import List, Optional
from .models import PriceData

class ApiClient:
    """A client to interact with the CoinGecko API."""
    
    BASE_URL = "https://api.coingecko.com/api/v3"

    def get_crypto_prices(
        self,
        crypto_ids: List[str],
        currency: str
    ) -> Optional[List[PriceData]]:
        """
        Fetches prices for a list of cryptocurrencies in a given currency.

        Args:
            crypto_ids: A list of cryptocurrency IDs (e.g., ['bitcoin', 'ethereum']).
            currency: The currency to get the price in (e.g., 'usd').

        Returns:
            A list of PriceData objects, or None if an error occurs.
        """
        if not crypto_ids:
            return []

        # Convert lists to comma-separated strings for the API
        ids_param = ",".join(crypto_ids)
        
        # Construct the full URL with query parameters
        url = f"{self.BASE_URL}/simple/price"
        params = {
            "ids": ids_param,
            "vs_currencies": currency
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            
            data = response.json()
            
            # Convert the JSON response into a list of PriceData objects
            price_list = []
            for crypto_id, price_data in data.items():
                if currency in price_data:
                    price_list.append(PriceData(
                        id=crypto_id,
                        price=price_data[currency],
                        currency=currency
                    ))
            return price_list

        except requests.exceptions.RequestException as e:
            print(f"❌ Network Error: Could not connect to the API. {e}")
            return None
        except KeyError:
            print(f"❌ Error: Invalid response format from the API. The currency '{currency}' might be unsupported.")
            return None