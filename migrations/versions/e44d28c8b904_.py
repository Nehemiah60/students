"""empty message

Revision ID: e44d28c8b904
Revises: 
Create Date: 2024-06-01 21:58:42.180078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e44d28c8b904'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('second_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('fee_paid', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_students_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_students_first_name'), ['first_name'], unique=True)
        batch_op.create_index(batch_op.f('ix_students_second_name'), ['second_name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_students_second_name'))
        batch_op.drop_index(batch_op.f('ix_students_first_name'))
        batch_op.drop_index(batch_op.f('ix_students_email'))

    op.drop_table('students')
    # ### end Alembic commands ###
