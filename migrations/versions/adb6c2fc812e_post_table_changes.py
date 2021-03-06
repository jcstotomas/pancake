"""post table changes

Revision ID: adb6c2fc812e
Revises: a125ddeedcbd
Create Date: 2020-05-10 22:15:31.087186

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'adb6c2fc812e'
down_revision = 'a125ddeedcbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('text_content', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('post_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('text_content', mysql.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('post_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('post')
    # ### end Alembic commands ###
