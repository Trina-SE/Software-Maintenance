"""
Main module - Example usage of the application
"""

from user_manager import UserManager
from data_processor import DataProcessor
from calculator import Calculator

def main():
    """Main entry point"""
    print("=== Refactoring Demo Project ===\n")
    
    # Test User Manager
    print("1. User Manager Demo:")
    um = UserManager()
    um.add_user("John Doe", "john@example.com", 25, "password123")
    um.add_user("Jane Smith", "jane@example.com", 30, "secret456")
    print(f"   Total users: {um.get_user_count()}")
    print(f"   Users: {um.list_users()}\n")
    
    # Test Data Processor
    print("2. Data Processor Demo:")
    dp = DataProcessor()
    numbers = [10, 20, 30, 40, 50]
    result = dp.process_numbers(numbers)
    print(f"   Processed: {result}\n")
    
    stats = dp.calc_stats(numbers)
    print(f"   Stats: {stats}\n")
    
    # Test Calculator
    print("3. Calculator Demo:")
    calc = Calculator()
    print(f"   10 + 5 = {calc.add(10, 5)}")
    print(f"   10 * 5 = {calc.multiply(10, 5)}")
    print(f"   10 / 5 = {calc.divide(10, 5)}")
    print(f"   Discount on 1000 (Type A): {calc.calc_discount(1000, 'A')}\n")
    
    # Test order processing
    print("4. Order Processing Demo:")
    order = calc.process_order(500, 2, 'B')
    print(f"   Order Result: {order}\n")

if __name__ == "__main__":
    main()
