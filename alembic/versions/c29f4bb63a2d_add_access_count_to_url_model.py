"""Add access count to URL model

Revision ID: c29f4bb63a2d
Revises: 10d5af49495b
Create Date: 2024-01-29 14:07:49.461936

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c29f4bb63a2d"
down_revision: Union[str, None] = "10d5af49495b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "urls",
        sa.Column("access_count", sa.Integer(), nullable=False, server_default="0"),
    )


def downgrade() -> None:
    op.drop_column("urls", "access_count")
