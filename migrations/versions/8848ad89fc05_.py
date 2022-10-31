"""empty message

Revision ID: 8848ad89fc05
Revises: 67ac6c61ea52
Create Date: 2022-10-30 12:13:57.650599

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8848ad89fc05'
down_revision = '67ac6c61ea52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fk_user', sa.Integer(), nullable=True),
    sa.Column('fk_character', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_character'], ['character.id'], ),
    sa.ForeignKeyConstraint(['fk_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fk_user', sa.Integer(), nullable=True),
    sa.Column('fk_planet', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_planet'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['fk_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('email', table_name='pet_caregiver')
    op.drop_index('email_2', table_name='pet_caregiver')
    op.drop_index('username', table_name='pet_caregiver')
    op.drop_index('username_2', table_name='pet_caregiver')
    op.drop_table('pet_caregiver')
    op.drop_index('rol', table_name='rol')
    op.drop_index('rol_2', table_name='rol')
    op.drop_table('rol')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rol',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('rol', mysql.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('rol_2', 'rol', ['rol'], unique=False)
    op.create_index('rol', 'rol', ['rol'], unique=False)
    op.create_table('pet_caregiver',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=12), nullable=False),
    sa.Column('fk_rol', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['fk_rol'], ['rol.id'], name='pet_caregiver_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('username_2', 'pet_caregiver', ['username'], unique=False)
    op.create_index('username', 'pet_caregiver', ['username'], unique=False)
    op.create_index('email_2', 'pet_caregiver', ['email'], unique=False)
    op.create_index('email', 'pet_caregiver', ['email'], unique=False)
    op.drop_table('favorite_planet')
    op.drop_table('favorite_character')
    # ### end Alembic commands ###