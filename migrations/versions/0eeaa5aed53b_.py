"""empty message

Revision ID: 0eeaa5aed53b
Revises: e36f1d0c4947
Create Date: 2019-06-26 17:31:17.238355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0eeaa5aed53b"
down_revision = "e36f1d0c4947"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "projects",
        sa.Column(
            "enforce_random_task_selection",
            sa.Boolean(),
            nullable=True,
            server_default=sa.false(),
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("projects", "enforce_random_task_selection")
    # ### end Alembic commands ###
