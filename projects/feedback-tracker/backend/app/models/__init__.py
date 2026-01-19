"""
Import all models here so SQLAlchemy registers them.

This avoids errors like:
'failed to locate a name (Rejection)'
"""

from app.models.application import Application  # noqa: F401
from app.models.rejection import Rejection      # noqa: F401
from app.models.feedback import Feedback        # noqa: F401
