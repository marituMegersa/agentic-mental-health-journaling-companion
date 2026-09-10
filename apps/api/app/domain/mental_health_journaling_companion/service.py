from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.mental_health_journaling_companion.models import AgenticMentalHealthJournalingCompanionSession, AgenticMentalHealthJournalingCompanionItem
from app.domain.mental_health_journaling_companion.schemas import AgenticMentalHealthJournalingCompanionSessionCreate, AgenticMentalHealthJournalingCompanionItemCreate

class AgenticMentalHealthJournalingCompanionService:
    @staticmethod
    def create_session(db: Session, data: AgenticMentalHealthJournalingCompanionSessionCreate) -> AgenticMentalHealthJournalingCompanionSession:
        db_obj = AgenticMentalHealthJournalingCompanionSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticMentalHealthJournalingCompanionSession:
        return db.query(AgenticMentalHealthJournalingCompanionSession).filter(AgenticMentalHealthJournalingCompanionSession.id == session_id).first()
