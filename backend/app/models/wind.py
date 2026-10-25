import uuid
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Index, Numeric, SmallInteger, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class WindActual(Base):
    __tablename__ = "wind_actuals"
    __table_args__ = (Index("idx_wind_actuals_settlement_date", "settlement_date"),)

    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), primary_key=True
    )
    generation_mw: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    settlement_date: Mapped[date] = mapped_column(Date)
    settlement_period: Mapped[int] = mapped_column(SmallInteger)
    source_publish_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    ingestion_run_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("ingestion_runs.id")
    )
    ingested_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class WindForecast(Base):
    __tablename__ = "wind_forecasts"
    __table_args__ = (Index("idx_wind_forecasts_publish_time", "publish_time"),)

    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), primary_key=True
    )
    publish_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), primary_key=True
    )
    generation_mw: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    ingestion_run_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("ingestion_runs.id")
    )
    ingested_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
