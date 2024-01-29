from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from data.init import Base

from datetime import datetime
from datetime import timedelta


class Analytics(Base):
    __tablename__ = "Analytics"
    analytics_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )
    url_id = Column(Integer, ForeignKey("URLs.id"), index=True, nullable=False)
    access_date = Column(DateTime)
    ip_address = Column(String(255))
    referrer = Column(String(2048))
    browser = Column(String(255))

    # url = relationship("URL", back_populates="Analytics")

    def __repr__(self):
        return f"<Analytics(url_id={self.url_id}, access_date={self.access_date}, ip_address={self.ip_address}, referrer={self.referrer}, browser={self.browser})>"
