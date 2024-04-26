from pydantic import BaseModel, ConfigDict, Field

from api.workflow.constants.workflow import validations


class Workflow(BaseModel):
    name: str = Field(
        min_length=validations.WORKFLOW_NAME_MIN_LENGTH,
        max_length=validations.WORKFLOW_NAME_MAX_LENGTH,

    )
    description: str = Field(
        min_length=validations.WORKFLOW_DESCRIPTION_MIN_LENGTH,
        max_length=validations.WORKFLOW_DESCRIPTION_MAX_LENGTH,
    )


class WorkflowInDTO(Workflow):
    pass


class WorkflowOutDTO(WorkflowInDTO):
    id: int

    model_config = ConfigDict(from_attributes=True)


class WorkflowOutDetailDTO(WorkflowOutDTO):
    nodes: list["Node"]


class Node(BaseModel):
    name: str
