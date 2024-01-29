"""new tables and entities  migration

Revision ID: f80db823e2da
Revises: 49d75cc6bc80
Create Date: 2024-01-28 21:25:52.815975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f80db823e2da"
down_revision: Union[str, None] = "49d75cc6bc80"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create Users table
    op.create_table(
        "Users",
        sa.Column(
            "user_id", sa.Integer, primary_key=True, autoincrement=True, nullable=False
        ),
        sa.Column("username", sa.String(255), unique=True, nullable=False),
        sa.Column("email", sa.String(255), unique=True, nullable=False),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column(
            "account_creation_date",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    # Create Roles table
    op.create_table(
        "Roles",
        sa.Column("role_id", sa.Integer, primary_key=True),
        sa.Column("role_name", sa.String(255)),
        sa.Column("permissions", sa.String(255)),
    )

    # Create UserRoles table
    op.create_table(
        "UserRoles",
        sa.Column(
            "user_id", sa.Integer, sa.ForeignKey("Users.user_id"), primary_key=True
        ),
        sa.Column(
            "role_id", sa.Integer, sa.ForeignKey("Roles.role_id"), primary_key=True
        ),
    )

    # Create URLs table
    op.create_table(
        "URLs",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("original_url", sa.String(2048), nullable=False),
        sa.Column("short_url", sa.String(255), nullable=False, unique=True),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
        sa.Column(
            "updated_at",
            sa.DateTime,
            server_default=sa.func.now(),
            onupdate=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.Column(
            "expiration_date",
            sa.DateTime,
            nullable=True,
            server_default=sa.text("(CURRENT_TIMESTAMP + INTERVAL '30 DAY')"),
        ),
        sa.Column("custom_alias", sa.String(255)),
        sa.Column("description", sa.String(2048)),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("Users.user_id")),
    )

    # Create Analytics table
    op.create_table(
        "Analytics",
        sa.Column("analytics_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("url_id", sa.Integer, sa.ForeignKey("URLs.id"), nullable=False),
        sa.Column("access_date", sa.DateTime, server_default=sa.func.now()),
        sa.Column("ip_address", sa.String(255)),
        sa.Column("referrer", sa.String(2048)),
        sa.Column("browser", sa.String(255)),
    )


def downgrade() -> None:
    op.drop_table("Analytics")
    op.drop_table("URLs")
    op.drop_table("UserRoles")
    op.drop_table("Roles")
    op.drop_table("Users")
