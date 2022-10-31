"""empty message

Revision ID: 2b86f01c1b62
Revises: 62db00b61df7
Create Date: 2022-10-30 14:49:04.522213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b86f01c1b62'
down_revision = '62db00b61df7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('fk_id_item', table_name='favorite')
    op.drop_index('fk_id_item_2', table_name='favorite')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('fk_id_item_2', 'favorite', ['fk_id_item'], unique=False)
    op.create_index('fk_id_item', 'favorite', ['fk_id_item'], unique=False)
    # ### end Alembic commands ###