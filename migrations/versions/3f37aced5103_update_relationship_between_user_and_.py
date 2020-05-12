"""update relationship between user and post

Revision ID: 3f37aced5103
Revises: 989796f3d6ef
Create Date: 2020-05-12 11:53:11.793070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f37aced5103'
down_revision = '989796f3d6ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'post', ['user_id'])
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='unique')
    # ### end Alembic commands ###
