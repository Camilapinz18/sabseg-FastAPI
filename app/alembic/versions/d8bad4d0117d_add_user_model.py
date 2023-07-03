
"""add_user_model

Revision ID: d8bad4d0117d
Revises:
Create Date: 2023-06-12 18:21:39.553664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8bad4d0117d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('default_data_version',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('version', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )
    op.create_index(op.f('ix_default_data_version_id'), 'default_data_version', ['id'], unique=False)
    
    op.create_table('user',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('attendance', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('surname', sa.String(), nullable=False),
                    sa.Column('phone', sa.String(), nullable=False),


                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)

    op.create_table(
        'equipment_category',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('name')
    )

    op.create_table(
        'equipment',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('brand', sa.String(), nullable=False),
        sa.Column('reference', sa.String(), nullable=False),
        sa.Column('photo', sa.String(), nullable=True),
        sa.Column('status', sa.String(), nullable=True),
        sa.Column('category_name', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['category_name'], ['equipment_category.name'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('id')
    )


    op.create_table(
        'room_category',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_room_category_id'), 'room_category', ['id'], unique=False)

    op.create_table(
        'room',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('category_name', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['category_name'], ['room_category.id'], ondelete='RESTRICT'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_room_id'), 'room', ['id'], unique=False)

    op.create_table(
        'reservation_type',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
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
        sa.Column('reservation_type', sa.Integer(), nullable=False),
        sa.Column('room_id', sa.Integer(), nullable=False),  # Changed column name from 'room' to 'room_id'
        sa.ForeignKeyConstraint(['client_id'], ['user.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['reservation_type'], ['reservation_type.id'], ondelete='CASCADE'),  # Changed reference from 'reservation_type.name' to 'reservation_type.id'
        sa.ForeignKeyConstraint(['room_id'], ['room.id'], ondelete='CASCADE'),  # Changed reference from 'room' to 'room.id'
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_index(op.f('ix_equipment_category_id'), 'equipment_category', ['id'], unique=False)  # Add index on 'equipment_category' table

    op.create_table(
        'reservation_equipments',
        sa.Column('reservation_id', sa.Integer(), nullable=False),
        sa.Column('equipment_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['reservation_id'], ['reservation.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], ondelete='CASCADE')
    )
        


def downgrade() -> None:
  
    op.drop_table('reservation')
    op.drop_table('reservation_type')
    
    
    op.drop_index(op.f('ix_room_id'), table_name='room')
    op.drop_table('room')
    op.drop_index(op.f('ix_room_category_id'), table_name='room_category')
    op.drop_table('room_category')

    op.drop_index(op.f('ix_equipment_id'), table_name='equipment')
    op.drop_table('equipment')
    op.drop_index(op.f('ix_equipment_category_id'), table_name='equipment_category')
    op.drop_table('equipment_category')

    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_default_data_version_id'), table_name='default_data_version')
    op.drop_table('default_data_version')