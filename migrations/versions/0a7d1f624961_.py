"""empty message

Revision ID: 0a7d1f624961
Revises: 7f373951bb17
Create Date: 2019-08-06 20:01:45.175685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a7d1f624961'
down_revision = '7f373951bb17'
branch_labels = None
depends_on = None


def upgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.create_table('activity',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('title', sa.String(length=100), nullable=True),
	sa.Column('description', sa.String(length=1000), nullable=True),
	sa.Column('latitude', sa.Float(), nullable=True),
	sa.Column('longitude', sa.Float(), nullable=True),
	sa.PrimaryKeyConstraint('id'),
	sa.UniqueConstraint('title')
	)
	# ### end Alembic commands ###


def downgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.drop_table('activity')
	# ### end Alembic commands ###
