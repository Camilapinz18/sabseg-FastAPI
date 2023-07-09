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
        sa.Column('code', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('code')
        )
    op.create_index(op.f('ix_roles_code'), 'roles', ['code'], unique=False)

    op.add_column('user', sa.Column('role', sa.String(), nullable=True))
    op.create_foreign_key('fk_user_role', 'user', 'roles', ['role'], ['code'])

def downgrade() -> None:
    op.drop_constraint('fk_user_role', 'user', type_='foreignkey')
    op.drop_column('user', 'role')

    op.drop_index(op.f('ix_roles_code'), table_name='roles')
    op.drop_table('roles')
