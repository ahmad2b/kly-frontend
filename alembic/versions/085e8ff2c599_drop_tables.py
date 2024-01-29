"""drop tables

Revision ID: 085e8ff2c599
Revises: 6801ac1359fc
Create Date: 2024-01-29 12:09:54.941265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "085e8ff2c599"
down_revision: Union[str, None] = "6801ac1359fc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('DROP TABLE IF EXISTS "UserRoles" CASCADE')
    op.execute('DROP TABLE IF EXISTS "Roles" CASCADE')
    op.execute('DROP TABLE IF EXISTS "url" CASCADE')
    op.execute('DROP TABLE IF EXISTS "Analytics" CASCADE')
    op.execute('DROP TABLE IF EXISTS "URLs" CASCADE')
    op.execute('DROP TABLE IF EXISTS "Users" CASCADE')


def downgrade() -> None:
    pass
