"""create currency rates table

Revision ID: _2024_08_24_200038
Revises: _2024_08_18_103126
Create Date: 2024-08-24 20:00:39.453605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '_2024_08_24_200038'
down_revision: Union[str, None] = '_2024_08_18_103126'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('currency_rates',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rate', sa.Float(), nullable=False),
    sa.Column('currency_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_currency_rates_currency_id'), 'currency_rates', ['currency_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_currency_rates_currency_id'), table_name='currency_rates')
    op.drop_table('currency_rates')