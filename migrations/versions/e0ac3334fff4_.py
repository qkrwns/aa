"""empty message

Revision ID: e0ac3334fff4
Revises: fbf45faedd94
Create Date: 2024-11-02 13:39:31.095051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0ac3334fff4'
down_revision = 'fbf45faedd94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lost', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lost', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###