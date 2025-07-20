import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    load_dotenv(env_path, override=True)

class Config:
    """Configuration class for managing environment variables safely."""
    
    # Azure OpenAI Configuration
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY", "")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    AZURE_OPENAI_DEPLOYMENT_NAME: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")
    OPENAI_API_VERSION: str = os.getenv("OPENAI_API_VERSION", "2025-03-01-preview")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    FRED_API_KEY: str = os.getenv("FRED_API_KEY", "")
    
    @classmethod
    def validate(cls) -> bool:
        """Validate that all required environment variables are set."""
        required_vars = [
            "AZURE_OPENAI_API_KEY",
            "AZURE_OPENAI_ENDPOINT", 
            "AZURE_OPENAI_DEPLOYMENT_NAME",
            "TAVILY_API_KEY"
        ]
        
        missing_vars = []
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
        
        if missing_vars:
            print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
            print("Please set these variables in your .env file or environment.")
            return False
        
        print("✅ All required environment variables are set.")
        return True
    
    @classmethod
    def get_azure_config(cls) -> dict:
        """Get Azure OpenAI configuration as a dictionary."""
        return {
            "api_key": cls.AZURE_OPENAI_API_KEY,
            "endpoint": cls.AZURE_OPENAI_ENDPOINT,
            "deployment_name": cls.AZURE_OPENAI_DEPLOYMENT_NAME,
            "api_version": cls.OPENAI_API_VERSION
        }
    
    @classmethod
    def get_tavily_config(cls) -> dict:
        """Get Tavily configuration as a dictionary"""
        return{
            "api_key": cls.TAVILY_API_KEY
        }

# Create a global config instance
config = Config()

# Validate configuration on import
if __name__ == "__main__":
    config.validate()
