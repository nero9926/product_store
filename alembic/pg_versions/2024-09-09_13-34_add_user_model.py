"""Add user model

Revision ID: 7546c1300603
Revises: 65c622dff9a7
Create Date: 2024-09-09 13:34:17.951933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7546c1300603'
down_revision: Union[str, None] = '65c622dff9a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
