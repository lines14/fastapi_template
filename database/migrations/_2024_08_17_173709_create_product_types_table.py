"""create product types table

Revision ID: _2024_08_17_173709
Revises: _2024_08_17_124155
Create Date: 2024-08-17 17:37:10.306231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '_2024_08_17_173709'
down_revision: Union[str, None] = '_2024_08_17_124155'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('product_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('group', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_types_group'), 'product_types', ['group'], unique=False)


def downgrade() -> None:
    op.drop_table('product_types')