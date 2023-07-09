"""empty message

Revision ID: c51377796f6a
Revises: d8bad4d0117d
Create Date: 2023-07-09 13:16:52.304237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c51377796f6a'
down_revision = 'd8bad4d0117d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('roles',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('code', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
        )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
