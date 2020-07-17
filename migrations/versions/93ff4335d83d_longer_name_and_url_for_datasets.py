"""longer name and url for datasets

Revision ID: 93ff4335d83d
Revises: 96052cfeea9b
Create Date: 2020-07-17 00:36:42.235949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93ff4335d83d'
down_revision = '96052cfeea9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dataset', sa.Column('name', sa.String(length=160), nullable=True))
    op.add_column('dataset', sa.Column('path', sa.String(length=340), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dataset', 'path')
    op.drop_column('dataset', 'name')
    # ### end Alembic commands ###
