from typing import Annotated

from fastapi import Depends

from api.dependencies import AsyncSession
from api.workflow.repositories.workflow import WorkflowRepository
from api.workflow.services.workflow import WorkflowService


def get_repository(session: AsyncSession) -> WorkflowRepository:
    return WorkflowRepository(session=session)


WorkflowRepositoryDep = Annotated[WorkflowRepository, Depends(get_repository)]


def get_service(repository: WorkflowRepositoryDep) -> WorkflowService:
    return WorkflowService(repository=repository)


WorkflowServiceDep = Annotated[WorkflowService, Depends(get_service)]
