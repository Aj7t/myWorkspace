 
from typing import Union

def total_price(price_1:int,price_2:int):
    return f"Your total bill is USD {price_1+price_2}"
        
price = total_price(30,40)
print(price)

def inr_to_usd(value:float) -> Union[float,None]:
    try:
        conversion_factor = 75
        value = value/conversion_factor
        return value
    except TypeError:
        return None

print(inr_to_usd('1200.5'))