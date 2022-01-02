"""Create dolar and euro models

Revision ID: 0ca633c9bc82
Revises: de53536facba
Create Date: 2021-12-31 17:50:54.337328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ca633c9bc82'
down_revision = 'de53536facba'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('dolar_price',
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_dolar_price'))
    )
    op.create_index(op.f('ix_dolar_price_created'), 'dolar_price', ['created'], unique=False)
    op.create_index(op.f('ix_dolar_price_updated'), 'dolar_price', ['updated'], unique=False)
    op.create_table('euro_price',
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_euro_price'))
    )
    op.create_index(op.f('ix_euro_price_created'), 'euro_price', ['created'], unique=False)
    op.create_index(op.f('ix_euro_price_updated'), 'euro_price', ['updated'], unique=False)
    op.drop_index('my_index', table_name='models')
    op.drop_table('models')

def downgrade():
    op.create_table('models',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('value', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_models')
    )
    op.create_index('my_index', 'models', ['name'], unique=False)
    op.drop_index(op.f('ix_euro_price_updated'), table_name='euro_price')
    op.drop_index(op.f('ix_euro_price_created'), table_name='euro_price')
    op.drop_table('euro_price')
    op.drop_index(op.f('ix_dolar_price_updated'), table_name='dolar_price')
    op.drop_index(op.f('ix_dolar_price_created'), table_name='dolar_price')
    op.drop_table('dolar_price')
