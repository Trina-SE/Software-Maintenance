"""
Calculator Module - Contains magic numbers and poor error handling
"""

class Calculator:
    
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return 0
        return a / b
    
    def calc_discount(self, price, discount_type):
        if discount_type == 'A':
            return price * 0.1
        elif discount_type == 'B':
            return price * 0.15
        elif discount_type == 'C':
            return price * 0.2
        elif discount_type == 'VIP':
            return price * 0.25
        else:
            return 0
    
    def calc_tax(self, amount):
        return amount * 0.18
    
    def calc_shipping(self, weight):
        if weight <= 1:
            return 50
        elif weight <= 5:
            return 100
        elif weight <= 10:
            return 150
        elif weight <= 20:
            return 200
        else:
            return 300
    
    def process_order(self, p, q, dt):
        if p <= 0 or q <= 0:
            return None
        
        subtotal = p * q
        
        if dt == 'A':
            discount = subtotal * 0.1
        elif dt == 'B':
            discount = subtotal * 0.15
        elif dt == 'C':
            discount = subtotal * 0.2
        else:
            discount = 0
        
        after_discount = subtotal - discount
        tax = after_discount * 0.18
        total = after_discount + tax
        
        if total > 1000:
            weight = q * 2.5
        else:
            weight = q * 1.5
        
        if weight <= 1:
            shipping = 50
        elif weight <= 5:
            shipping = 100
        elif weight <= 10:
            shipping = 150
        else:
            shipping = 200
        
        final_total = total + shipping
        
        return {
            'subtotal': subtotal,
            'discount': discount,
            'after_discount': after_discount,
            'tax': tax,
            'shipping': shipping,
            'total': final_total
        }
