"""Added Student model

Revision ID: f8f1c8f4c3b5
Revises: e30cd56fce9c
Create Date: 2023-09-01 12:53:07.524880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8f1c8f4c3b5'
down_revision = 'e30cd56fce9c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=55), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('enrolled_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_students_name'), 'students', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_name'), table_name='students')
    op.drop_table('students')
    # ### end Alembic commands ###
