from pydantic import BaseModel

class GetCard(BaseModel):
    workflow_id: str