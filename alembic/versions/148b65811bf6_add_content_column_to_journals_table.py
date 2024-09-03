"""add content column to  journals table

Revision ID: 148b65811bf6
Revises: e749f5360dd6
Create Date: 2024-09-02 23:52:59.281860

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '148b65811bf6'
down_revision: Union[str, None] = 'e749f5360dd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('journals', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('journals', 'content')
    pass
