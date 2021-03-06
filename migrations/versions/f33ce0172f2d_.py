"""empty message

Revision ID: f33ce0172f2d
Revises: 064247722cf0
Create Date: 2022-01-13 22:10:50.811817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f33ce0172f2d'
down_revision = '064247722cf0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id_')
    )
    op.create_table('team',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('goals_for', sa.Integer(), nullable=False),
    sa.Column('goals_against', sa.Integer(), nullable=False),
    sa.Column('wins', sa.Integer(), nullable=False),
    sa.Column('losses', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_')
    )
    op.create_table('user',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=90), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.Column('is_subscriber', sa.Boolean(), nullable=False),
    sa.Column('trial_attempts', sa.Integer(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id_'),
    sa.UniqueConstraint('username')
    )
    op.create_table('matches',
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('match_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['match_id'], ['match.id_'], ),
    sa.ForeignKeyConstraint(['team_id'], ['team.id_'], ),
    sa.PrimaryKeyConstraint('team_id', 'match_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matches')
    op.drop_table('user')
    op.drop_table('team')
    op.drop_table('match')
    # ### end Alembic commands ###
