from typing import Optional
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Schema for basic service health check response."""

    status: str = Field(..., examples=["ok"], description="Status of the application service")
    service: str = Field(..., examples=["sovereign-ai-workbench"], description="Name of the running service")


class DatabaseHealthResponse(BaseModel):
    """Schema for database health check response."""

    status: str = Field(..., examples=["ok"], description="Status of the database health check ('ok' or 'error')")
    database: str = Field(..., examples=["connected"], description="Database connection state")
    detail: Optional[str] = Field(None, examples=["PostgreSQL connection verified successfully"], description="Additional connection details or error messages")
