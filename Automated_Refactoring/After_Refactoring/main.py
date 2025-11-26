"""
Main module - Example usage of the refactored application.
"""

from user_manager import UserManager
from data_processor import DataProcessor
from calculator import Calculator


def print_header(title: str) -> None:
    print(f"\n{title}")
    print("=" * 60)


def demo_user_manager(um: UserManager) -> None:
    print_header("1. User Manager Demo")
    um.add_user("John Doe", "john@example.com", 25, "password123")
    um.add_user("Jane Smith", "jane@example.com", 30, "secret456")
    print(f"Total users: {um.get_user_count()}")
    print(f"Users: {um.list_users()}\n")


def demo_data_processor(dp: DataProcessor) -> None:
    print_header("2. Data Processor Demo")
    numbers = [10, 20, 30, 40, 50]
    result = dp.process_numbers(numbers)
    print(f"Processed: {result}\n")

    stats = dp.calc_stats(numbers)
    print(f"Stats: {stats}\n")


def demo_calculator(calc: Calculator) -> None:
    print_header("3. Calculator Demo")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"Discount on 1000 (Type A): {calc.calc_discount(1000, 'A')}\n")


def demo_order_processing(calc: Calculator) -> None:
    print_header("4. Order Processing Demo")
    order = calc.process_order(500, 2, "B")
    print(f"Order Result: {order}\n")


def main() -> None:
    print("=== Refactoring Demo Project (Refactored) ===")

    um = UserManager()
    dp = DataProcessor()
    calc = Calculator()

    demo_user_manager(um)
    demo_data_processor(dp)
    demo_calculator(calc)
    demo_order_processing(calc)

    print_header("All Demos Complete")


if __name__ == "__main__":
    main()
