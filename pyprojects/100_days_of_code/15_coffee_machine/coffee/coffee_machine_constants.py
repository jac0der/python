EXIT_TRIGGER:str = "off"
ORDERED_COFFEE: str = ""

COINS:dict[str, float] = {
        'quarters': 0.25, 
        'dimes': 0.10, 
        'nickles': 0.05, 
        'pennies':0.01
    }

STOCK_TRIGGER:str = "stock"
EXIT_MESSAGE: str = "Goodbye!"
REPORT_TRIGGER: str = "report"
ORDER_CHANGE: str = "Here is ${} dollars in change."
COFFEE_ORDER: str = "Coffee order is {}: {}."
ORDER_SUCCESS: str = "Here is your {} ☕ Enjoy!"
ORDER_VALIDATION_WARNING: str = "Invalid coffee order {}."
INSUFFICIENT_FUNDS: str = "Sorry that's not enough money. Money refunded."
INSUFFICIENT_INGREDIENTS: str = "Sorry there is not enough {}"
COIN_AMOUNT_WARNING:str = "Invalid entry for {}. Please enter an integer value."
COIN_AMOUNT_NUMBER_WARNING:str = "Invalid entry for {}. Please enter a positive integer value."