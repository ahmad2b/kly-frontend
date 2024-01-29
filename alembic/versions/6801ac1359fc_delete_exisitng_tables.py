"""delete exisitng tables

Revision ID: 6801ac1359fc
Revises: 598777f92bcf
Create Date: 2024-01-29 12:00:29.147478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6801ac1359fc"
down_revision: Union[str, None] = "598777f92bcf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("Roles")
    op.drop_table("url")
    op.drop_table("Analytics")
    op.drop_table("URLs")
    op.drop_table("UserRoles")
    op.drop_table("Users")


def downgrade() -> None:
    pass
