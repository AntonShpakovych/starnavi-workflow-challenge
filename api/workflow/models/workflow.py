from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from api.models import Base

from api.workflow.constants.workflow import validations


class Workflow(Base):
    __tablename__ = "workflows"

    name: Mapped[str] = mapped_column(
        String(validations.WORKFLOW_NAME_MAX_LENGTH),
        unique=True
    )
    description: Mapped[str] = mapped_column(
        String(validations.WORKFLOW_DESCRIPTION_MAX_LENGTH)
    )

    nodes: Mapped[list["Node"]] = relationship(back_populates="workflow") # noqa
