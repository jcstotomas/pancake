"""posts table

Revision ID: a125ddeedcbd
Revises: b078d627de30
Create Date: 2020-05-10 20:29:41.318065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a125ddeedcbd'
down_revision = 'b078d627de30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True, foreign_key=True),
    sa.Column('text_content', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
