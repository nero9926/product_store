"""upd model order 2

Revision ID: 09aa7eda0367
Revises: e6c54196ca1b
Create Date: 2024-09-23 23:45:58.593945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '09aa7eda0367'
down_revision: Union[str, None] = 'e6c54196ca1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'deliver_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'deliver_date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    # ### end Alembic commands ###
