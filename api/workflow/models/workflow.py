from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from api.models import Base


class Workflow(Base):
    __tablename__ = "workflows"

    name: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[str] = mapped_column(String(255))

    nodes: Mapped[list["Node"]] = relationship(back_populates="workflow") # noqa
