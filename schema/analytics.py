from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AnalyticsBase(BaseModel):
    url_id: int
    access_date: datetime
    ip_address: str
    referrer: Optional[str]
    browser: Optional[str]


class AnalyticsCreate(AnalyticsBase):
    pass


class AnalyticsResponse(AnalyticsBase):
    analytics_id: int

    class Config:
        orm_mode = True
