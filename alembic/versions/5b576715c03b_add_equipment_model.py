"""empty message

Revision ID: 5b576715c03b
Revises: d8bad4d0117d
Create Date: 2023-07-01 12:16:22.663073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b576715c03b'
down_revision = 'd8bad4d0117d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('equipment',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('brand', sa.String(), nullable=False),
                    sa.Column('reference', sa.String(), nullable=False),
                    sa.Column('photo', sa.String(), nullable=True),
                    sa.Column('total_stock', sa.Integer(), nullable=False),
                    sa.Column('current_stock', sa.Integer(), nullable=False),
                    sa.Column('status', sa.String(), nullable=True),

                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_equipment_id'), 'equipment', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_equipment_id'), table_name='equipment')
    op.drop_table('equipment')
