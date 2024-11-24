"""add test data

Revision ID: 901d0abc3c06
Revises: a7c5cf29ad2f
Create Date: 2024-11-17 13:32:11.001440

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '901d0abc3c06'
down_revision: Union[str, None] = 'a7c5cf29ad2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

TEST_PWD = '$2b$12$bAkw2mR9MdqOBK2CB6VRFuUGFM0h40MSHIYbv0Uq91bvlZKMRMyLW'  # pwd = 123


def upgrade() -> None:
    op.execute(f"""INSERT INTO users (name, last_name, email, password, bday, sex, interests, city)
            VALUES ('name1', 'last_name1', 'user1@test.com', '{TEST_PWD}', '1999-11-11', 'male', array['i1', 'i2'], 'London'),
                    ('name2', 'last_name2', 'user2@test.com', '{TEST_PWD}', '1999-11-11', 'male', array['i3'], 'Madrid'),
                    ('name3', 'last_name3', 'user3@test.com', '{TEST_PWD}', '1999-11-11', 'male', array['i2', 'i3'], 'Paris')""")


def downgrade() -> None:
    pass
