"""added runsuccess column to submission class

Revision ID: d04a7a244b51
Revises: def2c539e28e
Create Date: 2022-04-18 17:20:43.010155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd04a7a244b51'
down_revision = 'def2c539e28e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.add_column(sa.Column('run_success', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.drop_column('run_success')

    # ### end Alembic commands ###
