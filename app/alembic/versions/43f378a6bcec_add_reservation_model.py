"""empty message

Revision ID: 43f378a6bcec
Revises: f1ad93dbe0df
Create Date: 2023-07-01 15:32:33.385178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43f378a6bcec'
down_revision = 'f1ad93dbe0df'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.create_table(
        'reservation_type',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('name')
    )
    op.create_index(op.f('ix_reservation_type_id'), 'reservation_type', ['name'], unique=False)
    
    op.create_table(
        'reservation',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('start_hour', sa.Time(), nullable=False),
        sa.Column('end_hour', sa.Time(), nullable=False),
        sa.Column('aditional', sa.String(), nullable=True),
        sa.Column('client_id', sa.Integer(), nullable=False),
        sa.Column('reservation_type', sa.String(), nullable=False),
        sa.Column('room', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['client_id'], ['user.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['reservation_type'], ['reservation_type.name'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['room'], ['room.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table(
        'reservation_equipments',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('reservation_id', sa.Integer(), nullable=False),
        sa.Column('equipment_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['reservation_id'], ['reservation.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('reservation_equipments')
    op.drop_table('reservation')
    op.drop_table('reservation_type')
    
    
