"""upd shop7

Revision ID: bfe2c10439eb
Revises: f2990708e797
Create Date: 2024-09-22 17:40:54.408250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfe2c10439eb'
down_revision: Union[str, None] = 'f2990708e797'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'category_id')
    # ### end Alembic commands ###
