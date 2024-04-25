from fastapi import FastAPI

from api.dependencies import AsyncSession
from api.workflow.models.workflow import Workflow

app = FastAPI()


@app.get("/")
async def check(session: AsyncSession):
    workflow = Workflow()
    session.add(workflow)
    await session.commit()
