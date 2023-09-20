"""Adding access tokens table

Revision ID: 2d8d592e2851
Revises: d0b33d325844
Create Date: 2023-09-20 20:13:02.467467

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d8d592e2851'
down_revision: Union[str, None] = 'd0b33d325844'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('access_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_access_tokens_id'), 'access_tokens', ['id'], unique=False)
    op.create_index(op.f('ix_access_tokens_token'), 'access_tokens', ['token'], unique=False)
    op.create_index(op.f('ix_access_tokens_user_id'), 'access_tokens', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_access_tokens_user_id'), table_name='access_tokens')
    op.drop_index(op.f('ix_access_tokens_token'), table_name='access_tokens')
    op.drop_index(op.f('ix_access_tokens_id'), table_name='access_tokens')
    op.drop_table('access_tokens')
    # ### end Alembic commands ###