"""Added URL table

Revision ID: 10d5af49495b
Revises: 085e8ff2c599
Create Date: 2024-01-29 12:19:13.248063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "10d5af49495b"
down_revision: Union[str, None] = "085e8ff2c599"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "urls",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("original_url", sa.String(length=2048), nullable=False),
        sa.Column("short_url", sa.String(length=255), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("(CURRENT_TIMESTAMP AT TIME ZONE 'utc')"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("expiration_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column("custom_alias", sa.String(length=255), nullable=True),
        sa.Column("description", sa.String(length=2048), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("custom_alias"),
        sa.UniqueConstraint("short_url"),
    )


def downgrade() -> None:
    op.drop_table("urls")
