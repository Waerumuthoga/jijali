"""create journals table

Revision ID: e749f5360dd6
Revises: 
Create Date: 2024-09-02 23:32:11.238029

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e749f5360dd6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('journals', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_table('journals')
    pass
