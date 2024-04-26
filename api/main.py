from fastapi import FastAPI

from api.workflow.models.node import *  # for handling models in difference files # noqa
from api.workflow.models.workflow import *  # for handling models in difference files # noqa

from api.workflow.routers.workflow import router as workflow_router

app = FastAPI()
app.include_router(workflow_router)
