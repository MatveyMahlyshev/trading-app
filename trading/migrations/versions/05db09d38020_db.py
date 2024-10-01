"""db

Revision ID: 05db09d38020
Revises: 
Create Date: 2024-10-01 18:16:57.643339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05db09d38020'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('permissions', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###