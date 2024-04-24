import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.models import Base


class Workflow(Base):
    __tablename__ = "workflows"

    nodes: Mapped[list["Node"]] = relationship(back_populates="workflow")


class NodeType(enum.Enum):
    START = "start"
    MESSAGE = "message"
    CONDITION = "condition"
    END = "end"


class MessageNodeStatus(enum.Enum):
    PENDING = "pending"
    SENT = "sent"
    OPENED = "opened"


class Node(Base):
    __tablename__ = "nodes"

    type: Mapped[NodeType]

    workflow_id: Mapped[int] = mapped_column(
        ForeignKey(
            "workflows.id",
            ondelete="CASCADE"
        )
    )
    workflow: Mapped["Workflow"] = relationship(back_populates="nodes")

    previous_nodes: Mapped[list["Node"]] = relationship(
        secondary="nodes_nodes",
        primaryjoin="Node.id == NodeNode.child_node_id",
        secondaryjoin="Node.id == NodeNode.parent_node_id",
        post_update=True,
    )

    __mapper_args__ = {
        "polymorphic_on": "type",
    }


class StartNode(Node):
    __tablename__ = "start_nodes"

    id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id"),
        primary_key=True
    )

    next_node_id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id"),
        nullable=True
    )
    next_node: Mapped["Node"] = relationship(
        foreign_keys=[next_node_id],
        back_populates="previous_nodes",
        post_update=True
    )

    __mapper_args__ = {
        "polymorphic_identity": NodeType.START,
        "inherit_condition": Node.id == id
    }


class MessageNode(Node):
    __tablename__ = "message_nodes"

    id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id"),
        primary_key=True
    )
    status: Mapped[MessageNodeStatus]
    text: Mapped[str]

    next_node_id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id"),
        nullable=True
    )
    next_node: Mapped["Node"] = relationship(
        foreign_keys=[next_node_id],
        back_populates="previous_nodes",
        post_update=True
    )

    __mapper_args__ = {
        "polymorphic_identity": NodeType.MESSAGE,
        "inherit_condition": Node.id == id
    }


class ConditionNode(Node):
    __tablename__ = "condition_nodes"

    id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id"),
        primary_key=True
    )

    yes_node_id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id"),
        nullable=True
    )
    no_node_id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id"),
        nullable=True
    )
    yes_node: Mapped["Node"] = relationship(
        foreign_keys=[yes_node_id],
        back_populates="previous_nodes",
        post_update=True
    )
    no_node: Mapped["Node"] = relationship(
        foreign_keys=[no_node_id],
        back_populates="previous_nodes",
        post_update=True
    )

    __mapper_args__ = {
        "polymorphic_identity": NodeType.CONDITION,
        "inherit_condition": Node.id == id
    }


class EndNode(Node):
    __tablename__ = "end_nodes"

    id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id"),
        primary_key=True
    )

    __mapper_args__ = {
        "polymorphic_identity": NodeType.END,
        "inherit_condition": Node.id == id
    }


class NodeNode(Base):
    __tablename__ = "nodes_nodes"

    id = None

    parent_node_id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id", ondelete="CASCADE"),
        primary_key=True
    )
    child_node_id: Mapped[int] = mapped_column(
        ForeignKey("nodes.id", ondelete="CASCADE"),
        primary_key=True
    )
