"""empty message

Revision ID: cecabb19c772
Revises: 3daea9358983
Create Date: 2019-08-06 20:28:07.438971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cecabb19c772'
down_revision = '3daea9358983'
branch_labels = None
depends_on = None


def upgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.create_table('schedule',
	sa.Column('id', sa.Integer(), nullable=False),
	sa.Column('description', sa.String(length=1000), nullable=True),
	sa.Column('start_date', sa.DateTime(), nullable=True),
	sa.Column('end_date', sa.DateTime(), nullable=True),
	sa.Column('activity_id', sa.Integer(), nullable=True),
	sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ),
	sa.PrimaryKeyConstraint('id')
	)
	# ### end Alembic commands ###


def downgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.drop_table('schedule')
	# ### end Alembic commands ###