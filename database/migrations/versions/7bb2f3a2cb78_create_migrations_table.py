"""create migrations table

Revision ID: 7bb2f3a2cb78
Revises: c8d8a7166bfb
Create Date: 2024-08-09 18:13:24.463996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bb2f3a2cb78'
down_revision: Union[str, None] = 'c8d8a7166bfb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('migrations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('revision', sa.String(length=255), nullable=False),
    sa.Column('message', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_migrations_revision'), 'migrations', ['revision'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_migrations_revision'), table_name='migrations')
    op.drop_table('migrations')