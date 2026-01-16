"""
Application settings.

For now these are simple defaults.
Later we will read from environment variables (.env) for production safety.
"""

from pydantic import BaseModel


class Settings(BaseModel):
    # Shown in Swagger docs
    app_name: str = "Feedback Tracker API"

    # API version shown in docs
    version: str = "0.1.0"

    # Used later (logging, error details, etc.)
    debug: bool = True


settings = Settings()
