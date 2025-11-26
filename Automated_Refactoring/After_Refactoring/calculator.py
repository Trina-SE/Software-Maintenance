"""
Calculator Module - Refactored with constants, split methods, and improved error handling.
"""

from typing import Dict, Optional, Union

Number = Union[int, float]

# Discount rate constants (replaces magic numbers)
DISCOUNT_RATES = {
    "A": 0.10,
    "B": 0.15,
    "C": 0.20,
    "VIP": 0.25,
}

# Tax rate constant
TAX_RATE = 0.18

# Shipping cost brackets: (max_weight, cost)
SHIPPING_BRACKETS = [
    (1, 50),
    (5, 100),
    (10, 150),
    (20, 200),
]
DEFAULT_SHIPPING_COST = 300

# Weight multiplier thresholds for order processing
WEIGHT_THRESHOLD_TOTAL = 1000
LIGHT_WEIGHT_MULTIPLIER = 1.5
HEAVY_WEIGHT_MULTIPLIER = 2.5


class Calculator:

    def add(self, a: Number, b: Number) -> Number:
        return a + b

    def multiply(self, a: Number, b: Number) -> Number:
        return a * b

    def divide(self, a: Number, b: Number) -> Optional[Number]:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def calc_discount(self, price: Number, discount_type: str) -> Number:
        rate = DISCOUNT_RATES.get(discount_type, 0)
        return price * rate

    def calc_tax(self, amount: Number) -> Number:
        return amount * TAX_RATE

    def calc_shipping(self, weight: Number) -> Number:
        for max_weight, cost in SHIPPING_BRACKETS:
            if weight <= max_weight:
                return cost
        return DEFAULT_SHIPPING_COST

    def calc_order_weight(self, quantity: Number, subtotal: Number) -> Number:
        multiplier = (
            HEAVY_WEIGHT_MULTIPLIER
            if subtotal > WEIGHT_THRESHOLD_TOTAL
            else LIGHT_WEIGHT_MULTIPLIER
        )
        return quantity * multiplier

    def process_order(
        self, price: Number, quantity: Number, discount_type: str
    ) -> Optional[Dict]:
        if price <= 0 or quantity <= 0:
            return None

        subtotal = price * quantity
        discount = self.calc_discount(subtotal, discount_type)
        after_discount = subtotal - discount
        tax = self.calc_tax(after_discount)
        subtotal_with_tax = after_discount + tax

        weight = self.calc_order_weight(quantity, subtotal)
        shipping = self.calc_shipping(weight)

        final_total = subtotal_with_tax + shipping

        return {
            "subtotal": subtotal,
            "discount": discount,
            "after_discount": after_discount,
            "tax": tax,
            "shipping": shipping,
            "total": final_total,
        }
