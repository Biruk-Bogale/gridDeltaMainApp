import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Text, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class IngestionDataset(str, enum.Enum):
    FUELHH = "FUELHH"
    WINDFOR = "WINDFOR"


class IngestionStatus(str, enum.Enum):
    running = "running"
    succeeded = "succeeded"
    failed = "failed"


def _values(e):
    return [m.value for m in e]


class IngestionRun(Base):
    __tablename__ = "ingestion_runs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    dataset: Mapped[IngestionDataset] = mapped_column(
        Enum(IngestionDataset, name="ingestion_dataset", values_callable=_values)
    )
    range_from: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    range_to: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    status: Mapped[IngestionStatus] = mapped_column(
        Enum(IngestionStatus, name="ingestion_status", values_callable=_values),
        server_default="running",
    )
    rows_fetched: Mapped[int | None] = mapped_column(Integer)
    rows_upserted: Mapped[int | None] = mapped_column(Integer)
    rows_skipped: Mapped[int | None] = mapped_column(Integer)
    error_message: Mapped[str | None] = mapped_column(Text)
    triggered_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id"))
    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
