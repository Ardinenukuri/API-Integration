# Crypto Price CLI

A command-line interface (CLI) tool, built with Python, to fetch and display the latest prices of cryptocurrencies from the CoinGecko API.

This project demonstrates professional development practices, including a clean, testable architecture, a robust CLI built with `argparse`, and the use of mocking for reliable, fast unit tests.

## Features

-   **Fetch Multiple Prices**: Get prices for one or more cryptocurrencies in a single command.
-   **Currency Selection**: Specify the currency for the price data (e.g., USD, EUR, JPY).
-   **User-Friendly Output**: Displays data in a clean, aligned, and readable format.
-   **Robust Error Handling**: Gracefully handles network errors and invalid API responses.
-   **Mocked Unit Tests**: The core API client is tested offline using `unittest.mock`, ensuring reliability without depending on the live API.

## Project Structure

```
api_project/
├── client/
│   ├── api_client.py       # Class that handles API communication
│   └── models.py           # The 'PriceData' dataclass
├── tests/
│   └── test_api_client.py  # Unit tests for ApiClient using mocking
├── main.py                 # The CLI entry point using argparse
├── requirements.txt        # Project dependencies
└── README.md               # This documentation file
```

## Getting Started

### Prerequisites

-   Python 3.7 or higher

### Installation

1.  Clone this repository to your local machine.
2.  Install the required Python packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

### How to Use

All commands are run from the terminal in the project's root directory.

**Get Help**
To see all available options:
```bash
python main.py -h
```

**Examples**

-   **Get prices for Bitcoin and Ethereum in USD (default):**
    ```bash
    python main.py bitcoin ethereum
    ```
    *Example Output:*
    ```
    --- 🪙 Crypto Prices ---
    Bitcoin         | 68,123.00 USD
    Ethereum        | 3,540.50 USD
    ------------------------
    ```

-   **Get the price for Solana in Euros:**
    ```bash
    python main.py solana --currency eur
    ```
    *Example Output:*
    ```
    --- 🪙 Crypto Prices ---
    Solana          | 150.75 EUR
    ------------------------
    ```

### How to Run Tests

This project includes unit tests for the `ApiClient` that simulate API calls. This allows testing of the core logic without making any actual network requests.

To run the tests, use Python's built-in `unittest` module:
```bash
python -m unittest discover
```
A successful run will show an "OK" status, confirming that the client logic is working as expected.

---

### **Disclaimer**

This tool relies on the free, public CoinGecko API. Please be respectful of their service and do not spam requests.