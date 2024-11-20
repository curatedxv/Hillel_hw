"""Add a column

Revision ID: f5aea274adba
Revises: b502ad58d8da
Create Date: 2024-11-20 12:34:12.874066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5aea274adba'
down_revision: Union[str, None] = 'b502ad58d8da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
