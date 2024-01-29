"""Add user roles

Revision ID: 598777f92bcf
Revises: f80db823e2da
Create Date: 2024-01-29 08:29:42.070768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from model.role import Role


# revision identifiers, used by Alembic.
revision: str = "598777f92bcf"
down_revision: Union[str, None] = "f80db823e2da"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        sa.text(
            """
            INSERT INTO "Roles" (role_id, role_name, permissions) VALUES
            (1, 'admin', 'all'),
            (2, 'user', 'read,write'),
            (3, 'guest', 'read');
            """
        )
    )


def downgrade() -> None:
    op.execute(
        sa.text(
            """
            DELETE FROM Roles WHERE role_id IN (1, 2, 3);
            """
        )
    )
