"""create users table

Revision ID: a7c5cf29ad2f
Revises: 
Create Date: 2024-11-14 19:22:31.156106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7c5cf29ad2f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('login', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50)),
    )


def downgrade() -> None:
    op.drop_table('users')
