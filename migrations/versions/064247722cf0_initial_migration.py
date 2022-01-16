"""Initial migration.

Revision ID: 064247722cf0
Revises: 14838829462d
Create Date: 2021-12-28 11:38:53.444959

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '064247722cf0'
down_revision = '14838829462d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('match_ibfk_2', 'match', type_='foreignkey')
    op.drop_constraint('match_ibfk_1', 'match', type_='foreignkey')
    op.drop_column('match', 'away_id')
    op.drop_column('match', 'home_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('match', sa.Column('home_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('match', sa.Column('away_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('match_ibfk_1', 'match', 'team', ['away_id'], ['id_'])
    op.create_foreign_key('match_ibfk_2', 'match', 'team', ['home_id'], ['id_'])
    # ### end Alembic commands ###
