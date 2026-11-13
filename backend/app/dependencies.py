#skrypty na zaleznosci do endpoitow
from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

# Dependency do wstrzykiwania sesji w endpointach FastAPI
DBSession = Depends(get_db)