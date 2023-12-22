"""add content column

Revision ID: 63a73bdc7681
Revises: e0fc9728b963
Create Date: 2023-12-22 10:26:31.549947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "63a73bdc7681"
down_revision: Union[str, None] = "e0fc9728b963"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts",'content')
