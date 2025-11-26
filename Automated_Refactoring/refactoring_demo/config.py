"""
Configuration Module - Contains tight coupling and poor design
"""

from user_manager import UserManager
from data_processor import DataProcessor
from calculator import Calculator

class AppConfig:
    """Application configuration - tightly coupled"""
    
    def __init__(self):
        # Direct instantiation causes tight coupling
        self.user_mgr = UserManager()
        self.data_proc = DataProcessor()
        self.calc = Calculator()
        
        # Configuration values
        self.db_host = 'localhost'
        self.db_port = 5432
        self.db_name = 'app_db'
        self.max_connections = 100
        self.timeout = 30
        self.retry_count = 3
        self.log_level = 'INFO'
        self.env = 'development'
    
    def get_user_manager(self):
        """Get user manager"""
        return self.user_mgr
    
    def get_data_processor(self):
        """Get data processor"""
        return self.data_proc
    
    def get_calculator(self):
        """Get calculator"""
        return self.calc
    
    def setup_db(self):
        """Setup database connection"""
        print(f"Connecting to {self.db_host}:{self.db_port}/{self.db_name}")
        print(f"Max connections: {self.max_connections}")
        print(f"Timeout: {self.timeout}")
    
    def get_config(self):
        """Get all configuration"""
        return {
            'db_host': self.db_host,
            'db_port': self.db_port,
            'db_name': self.db_name,
            'max_connections': self.max_connections,
            'timeout': self.timeout,
            'retry_count': self.retry_count,
            'log_level': self.log_level,
            'env': self.env
        }
