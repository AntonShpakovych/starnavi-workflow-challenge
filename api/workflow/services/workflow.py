from fastapi import HTTPException, status

from api.workflow.constants.workflow import messages
from api.workflow.models.workflow import Workflow
from api.workflow.repositories.workflow import WorkflowRepository
from api.workflow.schemas.workflow import WorkflowInDTO


class WorkflowService:
    def __init__(self, repository: WorkflowRepository):
        self.repository = repository

    async def create_workflow(self, workflow: WorkflowInDTO) -> Workflow:
        await self._validation_uniqueness(workflow_name=workflow.name)

        return await self.repository.create(
            workflow=Workflow(**workflow.model_dump())
        )

    async def get_workflow(self, workflow_id: int) -> Workflow:
        workflow = await self._get_by_id(workflow_id=workflow_id)

        if not workflow:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=messages.ERROR_WORKFLOW_DOESNT_EXIST
            )
        return workflow

    async def get_workflows(self) -> list[Workflow]:
        return await self.repository.get_all()

    async def update_workflow(
        self,
        workflow_id: int,
        new_workflow: WorkflowInDTO
    ) -> Workflow:
        old_workflow = await self.get_workflow(workflow_id=workflow_id)

        if new_workflow.name != old_workflow.name:
            await self._validation_uniqueness(workflow_name=new_workflow.name)

        return await self.repository.update(
            old_workflow=old_workflow,
            new_workflow=Workflow(**new_workflow.model_dump())
        )

    async def delete_workflow(self, workflow_id: int) -> None:
        workflow = await self.get_workflow(workflow_id=workflow_id)

        await self.repository.delete(workflow=workflow)

    async def _validation_uniqueness(self, workflow_name: str) -> None:
        if await self._get_by_name(workflow_name=workflow_name):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=messages.ERROR_WORKFLOW_ALREADY_EXISTS
            )

    async def _get_by_id(self, workflow_id: int) -> Workflow | None:
        return await self.repository.get_one(identifier=workflow_id)

    async def _get_by_name(self, workflow_name: str) -> Workflow | None:
        return await self.repository.get_one(identifier=workflow_name)
