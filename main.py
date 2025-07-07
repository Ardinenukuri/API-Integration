import argparse
from client.api_client import ApiClient

def main():
    """Main function to run the Crypto Price CLI."""

    parser = argparse.ArgumentParser(
        description="Fetch cryptocurrency prices from the CoinGecko API."
    )
    parser.add_argument(
        "ids",
        metavar="CRYPTO_ID",
        type=str,
        nargs='+',  
        help="The ID(s) of the cryptocurrency (e.g., bitcoin ethereum solana)."
    )
    parser.add_argument(
        "-c", "--currency",
        type=str,
        default="usd",
        help="The currency to display the price in (default: usd)."
    )

    args = parser.parse_args()
    

    api_client = ApiClient()
    prices = api_client.get_crypto_prices(args.ids, args.currency)

    if prices is not None:
        print("\n--- 🪙 Crypto Prices ---")
        if not prices:
            print("No data found for the given IDs.")
        else:
            for price_data in prices:
                
                print(f"{price_data.id.capitalize():<15} | {price_data.price:,.2f} {price_data.currency.upper()}")
        print("------------------------\n")

if __name__ == "__main__":
    main()