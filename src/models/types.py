from datetime import datetime
from typing import Annotated

from sqlalchemy import DateTime, text
from sqlalchemy.orm import mapped_column


# ID
int_pk = Annotated[int, mapped_column(primary_key=True)]

# Date, time
created_at = Annotated[
    datetime,
    mapped_column(DateTime(timezone=False), server_default=text("CURRENT_TIMESTAMP")),
]
updated_at = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=False),
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=datetime.utcnow,
    ),
]
