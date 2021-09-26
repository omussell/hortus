"""
Initial models

Revision ID: f3992d2c49a0
Revises: 
Create Date: 2020-12-16 20:31:37.593598

"""
# 3rd-party
import sqlalchemy as sa
from alembic import op

revision = "f3992d2c49a0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "classification",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_classification_id"), "classification", ["id"], unique=False
    )
    op.create_table(
        "flora",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("classification", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.ForeignKeyConstraint(
            ["classification"],
            ["classification.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_flora_id"), "flora", ["id"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_flora_id"), table_name="flora")
    op.drop_table("flora")
    op.drop_index(op.f("ix_classification_id"), table_name="classification")
    op.drop_table("classification")
