"""
The Poof Palace - Secure Configuration Loader
=============================================
This module safely loads configuration from environment variables and YAML files.
All sensitive data is kept in .env files and never committed to version control.
"""

import os
import yaml
from dotenv import load_dotenv
from typing import Dict, Any, Optional
import logging

class SecureConfig:
    """Secure configuration manager that loads secrets from environment variables."""
    
    def __init__(self, config_path: str = "config.yaml", env_path: str = ".env"):
        """
        Initialize the secure configuration loader.
        
        Args:
            config_path: Path to the YAML configuration file
            env_path: Path to the .env file containing secrets
        """
        self.config_path = config_path
        self.env_path = env_path
        self.config = {}
        self.secrets = {}
        
        # Load environment variables from .env file
        self._load_environment_variables()
        
        # Load YAML configuration
        self._load_yaml_config()
        
        # Merge configurations with environment variables taking precedence
        self._merge_configurations()
        
        # Validate required secrets
        self._validate_secrets()
    
    def _load_environment_variables(self):
        """Load environment variables from .env file."""
        if os.path.exists(self.env_path):
            load_dotenv(self.env_path)
            print(f"✅ Loaded environment variables from {self.env_path}")
        else:
            print(f"⚠️  Warning: {self.env_path} not found. Using system environment variables only.")
    
    def _load_yaml_config(self):
        """Load non-sensitive configuration from YAML file."""
        try:
            with open(self.config_path, 'r') as f:
                self.config = yaml.safe_load(f)
            print(f"✅ Loaded configuration from {self.config_path}")
        except FileNotFoundError:
            print(f"❌ Error: {self.config_path} not found!")
            raise
        except yaml.YAMLError as e:
            print(f"❌ Error parsing YAML configuration: {e}")
            raise
    
    def _merge_configurations(self):
        """Merge YAML config with environment variables."""
        # Environment variables take precedence over YAML config
        env_mappings = {
            # Google Cloud
            'GEMINI_API_KEY': 'GEMINI_API_KEY',
            'GOOGLE_API_KEY': 'GOOGLE_API_KEY', 
            'GOOGLE_CLIENT_ID': 'GOOGLE_CLIENT_ID',
            'GOOGLE_CLIENT_SECRET': 'GOOGLE_CLIENT_SECRET',
            'GOOGLE_CLOUD_PROJECT_ID': 'GOOGLE_CLOUD_PROJECT_ID',
            'GOOGLE_CLOUD_LOCATION': 'GOOGLE_CLOUD_LOCATION',
            
            # Social Media
            'INSTAGRAM_ACCESS_TOKEN': 'INSTAGRAM_ACCESS_TOKEN',
            'INSTAGRAM_USER_ID': 'INSTAGRAM_USER_ID',
            'TIKTOK_ACCESS_TOKEN': 'TIKTOK_ACCESS_TOKEN',
            'TIKTOK_CLIENT_KEY': 'TIKTOK_CLIENT_KEY',
            'TIKTOK_CLIENT_SECRET': 'TIKTOK_CLIENT_SECRET',
            'TWITTER_API_KEY': 'TWITTER_API_KEY',
            'TWITTER_API_SECRET': 'TWITTER_API_SECRET',
            'TWITTER_ACCESS_TOKEN': 'TWITTER_ACCESS_TOKEN',
            'TWITTER_ACCESS_SECRET': 'TWITTER_ACCESS_SECRET',
            'TWITTER_BEARER_TOKEN': 'TWITTER_BEARER_TOKEN',
            
            # E-commerce
            'SHOPIFY_API_KEY': 'SHOPIFY_API_KEY',
            'SHOPIFY_API_SECRET': 'SHOPIFY_API_SECRET',
            'SHOPIFY_STORE_URL': 'SHOPIFY_STORE_URL',
            'PRINTFUL_API_KEY': 'PRINTFUL_API_KEY',
            
            # Security
            'ENVIRONMENT': 'ENVIRONMENT',
            'DEBUG_MODE': 'DEBUG_MODE',
            'MAX_RETRY_ATTEMPTS': 'MAX_RETRY_ATTEMPTS',
        }
        
        # Override YAML config with environment variables
        for env_var, config_key in env_mappings.items():
            env_value = os.getenv(env_var)
            if env_value is not None:
                # Convert string booleans to actual booleans
                if env_value.lower() in ('true', 'false'):
                    env_value = env_value.lower() == 'true'
                # Convert string numbers to integers
                elif env_value.isdigit():
                    env_value = int(env_value)
                
                self.config[config_key] = env_value
                print(f"🔐 Loaded {config_key} from environment variable")
    
    def _validate_secrets(self):
        """Validate that all required secrets are present."""
        required_secrets = [
            'GEMINI_API_KEY',
            'GOOGLE_CLOUD_PROJECT_ID',
        ]
        
        missing_secrets = []
        for secret in required_secrets:
            if not self.config.get(secret) or self.config[secret] == f"your_{secret.lower()}_here":
                missing_secrets.append(secret)
        
        if missing_secrets:
            print(f"❌ Missing required secrets: {', '.join(missing_secrets)}")
            print("Please check your .env file and ensure all required API keys are set.")
            raise ValueError(f"Missing required secrets: {missing_secrets}")
        
        print("✅ All required secrets validated successfully")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        return self.config.get(key, default)
    
    def get_secret(self, key: str) -> str:
        """Get a secret value (with additional logging for security)."""
        value = self.config.get(key)
        if not value:
            raise ValueError(f"Secret '{key}' not found in configuration")
        
        # Log that we accessed a secret (but not the value)
        if self.get('DEBUG_MODE', False):
            print(f"🔐 Accessed secret: {key}")
        
        return value
    
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.get('ENVIRONMENT', 'development').lower() == 'production'
    
    def is_debug_mode(self) -> bool:
        """Check if debug mode is enabled."""
        return self.get('DEBUG_MODE', False)
    
    def get_all_config(self) -> Dict[str, Any]:
        """Get all configuration (excluding sensitive values for logging)."""
        safe_config = self.config.copy()
        
        # Remove or mask sensitive values
        sensitive_keys = [
            'GEMINI_API_KEY', 'GOOGLE_API_KEY', 'GOOGLE_CLIENT_SECRET',
            'INSTAGRAM_ACCESS_TOKEN', 'TIKTOK_ACCESS_TOKEN', 'TIKTOK_CLIENT_SECRET',
            'TWITTER_API_KEY', 'TWITTER_API_SECRET', 'TWITTER_ACCESS_TOKEN',
            'TWITTER_ACCESS_SECRET', 'TWITTER_BEARER_TOKEN',
            'SHOPIFY_API_KEY', 'SHOPIFY_API_SECRET', 'PRINTFUL_API_KEY'
        ]
        
        for key in sensitive_keys:
            if key in safe_config:
                safe_config[key] = "***MASKED***"
        
        return safe_config
    
    def print_config_summary(self):
        """Print a summary of the configuration (safe for logging)."""
        print("\n🏰 The Poof Palace Configuration Summary:")
        print("=" * 50)
        
        safe_config = self.get_all_config()
        for key, value in safe_config.items():
            print(f"  {key}: {value}")
        
        print(f"\n🔒 Security Status:")
        print(f"  Environment: {self.get('ENVIRONMENT', 'development')}")
        print(f"  Debug Mode: {self.is_debug_mode()}")
        print(f"  Production Mode: {self.is_production()}")
        print("=" * 50)

def load_secure_config(config_path: str = "config.yaml", env_path: str = ".env") -> SecureConfig:
    """
    Load secure configuration from files and environment variables.
    
    Args:
        config_path: Path to the YAML configuration file
        env_path: Path to the .env file containing secrets
        
    Returns:
        SecureConfig instance with merged configuration
    """
    return SecureConfig(config_path, env_path)

# Example usage and testing
if __name__ == "__main__":
    try:
        config = load_secure_config()
        config.print_config_summary()
        
        # Test accessing a secret
        gemini_key = config.get_secret('GEMINI_API_KEY')
        print(f"\n✅ Successfully loaded Gemini API key: {gemini_key[:10]}...")
        
    except Exception as e:
        print(f"❌ Configuration loading failed: {e}")
        print("\nPlease ensure:")
        print("1. Copy secrets_template.env to .env")
        print("2. Fill in your actual API keys in .env")
        print("3. Run this script again")
