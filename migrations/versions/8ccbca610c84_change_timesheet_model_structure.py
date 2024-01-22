"""Change Timesheet model structure

Revision ID: 8ccbca610c84
Revises: 0ca586387911
Create Date: 2024-01-22 12:54:48.291024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8ccbca610c84'
down_revision: Union[str, None] = '0ca586387911'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('timesheets', 'input_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('timesheets', 'output_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('timesheets', 'output_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('timesheets', 'input_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###