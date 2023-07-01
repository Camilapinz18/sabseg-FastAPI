"""empty message

Revision ID: f1ad93dbe0df
Revises: 5b576715c03b
Create Date: 2023-07-01 14:36:56.106370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1ad93dbe0df'
down_revision = '5b576715c03b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'room_category',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('name')
    )
    op.create_index(op.f('ix_room_category_id'), 'room_category', ['name'], unique=False)

    op.create_table(
        'room',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('category_name', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['category_name'], ['room_category.name'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('name')
    )
    op.create_index(op.f('ix_room_id'), 'room', ['name'], unique=False)
    


def downgrade() -> None:
    op.drop_index(op.f('ix_room_id'), table_name='room')
    op.drop_table('room')
    op.drop_index(op.f('ix_room_category_id'), table_name='room_category')
    op.drop_table('room_category')

