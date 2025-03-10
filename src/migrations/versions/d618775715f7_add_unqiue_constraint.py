"""Add unqiue constraint

Revision ID: d618775715f7
Revises: 2d8d592e2851
Create Date: 2025-02-22 13:23:20.426390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd618775715f7'
down_revision: Union[str, None] = '2d8d592e2851'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        """
        DELETE FROM user_learning_collections
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM user_learning_collections
            GROUP BY user_id, learning_collection_id
        );
        """
    )
    op.create_unique_constraint('_user_id_learning_collection_id_uc', 'user_learning_collections', ['user_id', 'learning_collection_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('_user_id_learning_collection_id_uc', 'user_learning_collections', type_='unique')
    # ### end Alembic commands ###
