
"""create companies, devs, freebies

Revision ID: 5f72c58bf48c
Revises: 7a71dbf71c64
Create Date: 2023-03-15 15:06:20.944586

"""
from alembic import op
import sqlalchemy as sa


revision = '5f72c58bf48c'
down_revision = '7a71dbf71c64'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('companies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('founding_year', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('devs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=True),
        sa.Column('value', sa.Integer(), nullable=True),
        sa.Column('company_id', sa.Integer(), nullable=True),
        sa.Column('dev_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name=op.f('fk_freebies_company_id_companies')),
        sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], name=op.f('fk_freebies_dev_id_devs')),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('freebies')
    op.drop_table('devs')
    op.drop_table('companies')
