"""url table

Revision ID: 49d75cc6bc80
Revises: 
Create Date: 2024-01-28 19:01:20.028243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "49d75cc6bc80"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "url",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("orignal_url", sa.String(200), nullable=False),
        sa.Column("short_url", sa.String(200), nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    pass
