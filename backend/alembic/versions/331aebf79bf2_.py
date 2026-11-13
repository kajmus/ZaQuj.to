"""empty message

Revision ID: 331aebf79bf2
Revises: 5
Create Date: 2026-11-12 14:00:02.140622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6'
down_revision: Union[str, Sequence[str], None] = '5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

from alembic import op
import sqlalchemy as sa

# ... (pogrubione/istniejące nagłówki pliku)

def upgrade() -> None:
    # Używamy batch_alter_table, aby SQLite obsłużyło dodanie ograniczenia
    with op.batch_alter_table('UserSession', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_usersession_id_user', ['id_user'])

def downgrade() -> None:
    with op.batch_alter_table('UserSession', schema=None) as batch_op:
        batch_op.drop_constraint('uq_usersession_id_user', type_='unique')