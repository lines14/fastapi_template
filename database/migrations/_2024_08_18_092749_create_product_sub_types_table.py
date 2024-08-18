"""create product sub types table

Revision ID: _2024_08_18_092749
Revises: _2024_08_17_173709
Create Date: 2024-08-18 09:27:50.654266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '_2024_08_18_092749'
down_revision: Union[str, None] = '_2024_08_17_173709'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('product_sub_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sub_type', sa.String(length=255), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_sub_types_type'), 'product_sub_types', ['type'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_product_sub_types_type'), table_name='product_sub_types')
    op.drop_table('product_sub_types')