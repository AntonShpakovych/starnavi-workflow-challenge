from sqlalchemy import select, Select
from sqlalchemy.orm import selectinload

from api.workflow.models.workflow import Workflow
from api.workflow.repositories.repository import Repository


class WorkflowRepository(Repository):
    async def create(self, workflow: Workflow) -> Workflow:
        self.session.add(workflow)
        await self.session.commit()

        return workflow

    async def get_one(self, identifier: int | str) -> Workflow | None:
        base_stmt = self._load_options_many()

        stmt = base_stmt.where(
            Workflow.id == identifier
            if isinstance(identifier, int)
            else Workflow.name == identifier
        )
        result = await self.session.execute(stmt)
        workflow = result.scalar_one_or_none()

        return workflow

    async def get_all(self) -> list[Workflow]:
        stmt = self._load_options_many().order_by(Workflow.id)
        result = await self.session.execute(stmt)
        workflows = result.scalars().all()

        return workflows

    async def delete(self, workflow: Workflow) -> None:
        await self.session.delete(workflow)
        await self.session.commit()

    async def update(
        self,
        old_workflow: Workflow,
        new_workflow: Workflow
    ) -> Workflow:
        new_workflow.id = old_workflow.id

        await self.session.merge(new_workflow)
        await self.session.commit()

        return new_workflow

    @staticmethod
    def _load_options_many() -> Select:
        return select(Workflow).options(selectinload(Workflow.nodes))
