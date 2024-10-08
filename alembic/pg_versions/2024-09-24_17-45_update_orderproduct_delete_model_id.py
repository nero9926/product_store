"""update orderProduct delete model id

Revision ID: 37333aa6c942
Revises: 9e51b9fc07db
Create Date: 2024-09-24 17:45:35.546884

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37333aa6c942'
down_revision: Union[str, None] = '9e51b9fc07db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order_product', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_product', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
