from fastapi import APIRouter, status

from api.workflow.dependencies.workflow import WorkflowServiceDep
from api.workflow.schemas.workflow import (
    WorkflowInDTO,
    WorkflowOutDTO,
    WorkflowOutDetailDTO,
)


router = APIRouter(prefix="/workflows", tags=["workflows"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_workflow(
    workflow: WorkflowInDTO,
    workflow_service: WorkflowServiceDep
) -> WorkflowOutDTO:
    return await workflow_service.create_workflow(workflow=workflow)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_workflows(
    workflow_service: WorkflowServiceDep
) -> list[WorkflowOutDTO]:
    return await workflow_service.get_workflows()


@router.get("/{workflow_id}", status_code=status.HTTP_200_OK)
async def get_workflow(
    workflow_id: int,
    workflow_service: WorkflowServiceDep
) -> WorkflowOutDTO:
    return await workflow_service.get_workflow(workflow_id=workflow_id)


@router.put("/{workflow_id}", status_code=status.HTTP_200_OK)
async def update_workflow(
    workflow_id: int,
    new_workflow: WorkflowInDTO,
    workflow_service: WorkflowServiceDep
) -> WorkflowOutDetailDTO:
    return await workflow_service.update_workflow(
        workflow_id=workflow_id,
        new_workflow=new_workflow
    )


@router.delete("/{workflow_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow(
    workflow_id: int,
    workflow_service: WorkflowServiceDep
) -> None:
    await workflow_service.delete_workflow(workflow_id=workflow_id)
