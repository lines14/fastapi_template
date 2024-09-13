"""add currency id column to purchases

Revision ID: _2024_09_13_200441
Revises: _2024_09_13_181949
Create Date: 2024-09-13 20:04:42.002701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '_2024_09_13_200441'
down_revision: Union[str, None] = '_2024_09_13_181949'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("purchases", recreate='always') as batch_op:
        batch_op.add_column(
            sa.Column('currency_id', sa.Integer(), sa.ForeignKey('currencies.id', name='purchases_ibfk_2', ondelete='CASCADE'), nullable=False),
            insert_after="cost"
        )


def downgrade() -> None:
    with op.batch_alter_table('purchases') as batch_op:
        batch_op.drop_constraint('purchases_ibfk_2', type_='foreignkey')
    op.drop_index(op.f('ix_purchases_currency_id'), table_name='purchases')
    op.drop_column('purchases', 'currency_id')