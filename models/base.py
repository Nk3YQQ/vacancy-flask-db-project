from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import ForeignKey, String
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
employer_id = Annotated[int, mapped_column(ForeignKey('employers.employer_id', ondelete="CASCADE"))]
str_80 = Annotated[str, 80]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_80: String(80)
    }
