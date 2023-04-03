"""create auth tables

Revision ID: 314f77c1449a
Revises: 
Create Date: 2023-01-07 02:37:01.418429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '314f77c1449a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )
    op.create_table('user_roles',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('user_roles')
    op.drop_table('users')
