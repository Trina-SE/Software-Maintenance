"""
Configuration Module - Refactored with dependency injection pattern.
"""

from typing import Dict, Optional, Protocol


class Manager(Protocol):
    """Protocol for manager classes (user, data, calculator managers)."""

    pass


class DatabaseConfig:
    """Encapsulates database configuration."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 5432,
        database: str = "app_db",
        max_connections: int = 100,
        timeout: int = 30,
    ):
        """Initialize database config.

        Args:
            host: Database host.
            port: Database port.
            database: Database name.
            max_connections: Maximum connections.
            timeout: Connection timeout in seconds.
        """
        self.host = host
        self.port = port
        self.database = database
        self.max_connections = max_connections
        self.timeout = timeout

    def to_dict(self) -> Dict:
        """Convert to dictionary.

        Returns:
            Config as dict.
        """
        return {
            "host": self.host,
            "port": self.port,
            "database": self.database,
            "max_connections": self.max_connections,
            "timeout": self.timeout,
        }

    def setup(self) -> None:
        """Print setup information."""
        print(f"Connecting to {self.host}:{self.port}/{self.database}")
        print(f"Max connections: {self.max_connections}")
        print(f"Timeout: {self.timeout}")


class AppConfig:
    """Application configuration using dependency injection.

    Accepts manager instances instead of instantiating them directly,
    reducing tight coupling and improving testability.
    """

    def __init__(
        self,
        user_manager: Optional[Manager] = None,
        data_processor: Optional[Manager] = None,
        calculator: Optional[Manager] = None,
        db_config: Optional[DatabaseConfig] = None,
        retry_count: int = 3,
        log_level: str = "INFO",
        env: str = "development",
    ):
        """Initialize application config.

        Args:
            user_manager: UserManager instance (optional for dependency injection).
            data_processor: DataProcessor instance (optional).
            calculator: Calculator instance (optional).
            db_config: DatabaseConfig instance.
            retry_count: Retry count for operations.
            log_level: Logging level.
            env: Environment (development/production).
        """
        self.user_manager = user_manager
        self.data_processor = data_processor
        self.calculator = calculator
        self.db_config = db_config or DatabaseConfig()
        self.retry_count = retry_count
        self.log_level = log_level
        self.env = env

    def get_user_manager(self) -> Optional[Manager]:
        """Get user manager.

        Returns:
            UserManager instance or None.
        """
        return self.user_manager

    def get_data_processor(self) -> Optional[Manager]:
        """Get data processor.

        Returns:
            DataProcessor instance or None.
        """
        return self.data_processor

    def get_calculator(self) -> Optional[Manager]:
        """Get calculator.

        Returns:
            Calculator instance or None.
        """
        return self.calculator

    def get_config(self) -> Dict:
        """Get all configuration as dict.

        Returns:
            Full config dict.
        """
        return {
            "database": self.db_config.to_dict(),
            "retry_count": self.retry_count,
            "log_level": self.log_level,
            "env": self.env,
        }

    def setup_database(self) -> None:
        """Setup database connection."""
        self.db_config.setup()
