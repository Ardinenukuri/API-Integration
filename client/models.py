from dataclasses import dataclass

@dataclass
class PriceData:
    """A dataclass to hold the price information for a cryptocurrency."""
    id: str      
    price: float
    currency: str 