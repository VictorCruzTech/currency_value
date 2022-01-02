from datetime import datetime

from sqlalchemy import Column, DateTime


def return_now():
    ''' Ok, that's weird. However, it makes freeze_time to work properly '''
    return datetime.utcnow()


class BaseMixin(object):
    def __json__(self):
        return {}

    def json(self):
        return self.__json__()


class CreatedUpdatedMixin(BaseMixin):
    """Provides created and updated attributes"""
    created = Column(DateTime, default=return_now, index=True)
    updated = Column(DateTime, default=return_now, onupdate=return_now, index=True)
