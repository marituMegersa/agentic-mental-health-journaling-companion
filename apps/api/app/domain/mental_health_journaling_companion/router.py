from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.mental_health_journaling_companion.schemas import AgenticMentalHealthJournalingCompanionSessionCreate, AgenticMentalHealthJournalingCompanionSessionResponse
from app.domain.mental_health_journaling_companion.service import AgenticMentalHealthJournalingCompanionService

router = APIRouter(prefix="/api/v1/mental_health_journaling_companion", tags=["Agentic Mental Health Journaling Companion Domain"])

@router.post("/sessions", response_model=AgenticMentalHealthJournalingCompanionSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticMentalHealthJournalingCompanionSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Mental Health Journaling Companion.
    """
    return AgenticMentalHealthJournalingCompanionService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticMentalHealthJournalingCompanionSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticMentalHealthJournalingCompanionService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
