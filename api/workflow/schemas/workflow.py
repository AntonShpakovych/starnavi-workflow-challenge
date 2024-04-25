from pydantic import BaseModel


class Workflow(BaseModel):
    name: str
    description: str


class WorkflowInDTO(Workflow):
    pass


class WorkflowOutDTO(WorkflowInDTO):
    id: int
    nodes: list["Node"] # noqa
