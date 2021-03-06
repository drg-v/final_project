"""Initial migration.

Revision ID: 12d63d06710a
Revises: f723bdd65008
Create Date: 2021-12-28 11:24:39.067322

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '12d63d06710a'
down_revision = 'f723bdd65008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('match', sa.Column('home_id', sa.Integer(), nullable=False))
    op.add_column('match', sa.Column('away_id', sa.Integer(), nullable=False))
    op.drop_constraint('match_ibfk_2', 'match', type_='foreignkey')
    op.drop_constraint('match_ibfk_1', 'match', type_='foreignkey')
    op.create_foreign_key(None, 'match', 'team', ['away_id'], ['id_'])
    op.create_foreign_key(None, 'match', 'team', ['home_id'], ['id_'])
    op.drop_column('match', 'home')
    op.drop_column('match', 'away')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('match', sa.Column('away', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('match', sa.Column('home', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'match', type_='foreignkey')
    op.drop_constraint(None, 'match', type_='foreignkey')
    op.create_foreign_key('match_ibfk_1', 'match', 'team', ['away'], ['id_'])
    op.create_foreign_key('match_ibfk_2', 'match', 'team', ['home'], ['id_'])
    op.drop_column('match', 'away_id')
    op.drop_column('match', 'home_id')
    # ### end Alembic commands ###
