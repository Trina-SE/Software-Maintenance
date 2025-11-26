# Refactoring Demo Project

This project contains sample code with various code smells and refactoring opportunities for learning and practice.

## Project Structure

- `user_manager.py` - User management module with refactoring opportunities
- `data_processor.py` - Data processing module with code duplication
- `calculator.py` - Calculator module with magic numbers and poor error handling
- `config.py` - Configuration management with tight coupling

## Code Issues to Identify and Refactor

1. **Long functions** - Methods doing too many things
2. **Code duplication** - Similar code repeated across modules
3. **Poor naming** - Non-descriptive variable and function names
4. **Magic numbers** - Hard-coded values without explanation
5. **Tight coupling** - Classes depend directly on concrete implementations
6. **Poor error handling** - Missing validation and exception handling
7. **Single Responsibility Principle violations** - Classes doing multiple things

## How to Use

Review each file and identify the code smells. Then refactor the code to improve:
- Readability
- Maintainability
- Testability
- Performance

## Refactoring Goals

- Extract methods
- Remove duplication
- Improve naming
- Add proper error handling
- Follow SOLID principles
