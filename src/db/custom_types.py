import datetime

from sqlalchemy import DateTime as SADateTime
from sqlalchemy.types import TypeDecorator


class TZDateTime(TypeDecorator):
    """Timezone-aware timestamps stored as timezone-naive UTC timestamps.

    Converts incoming timestamps with timezone information to UTC and then strips out
    the timezone information before storing in the database. This implementation is
    preferred because it is compatible with all database backends.

    Note:
        This implementation is adapted from the following section of the SQLAlchemy
        documentation:
        https://docs.sqlalchemy.org/en/20/core/custom_types.html#store-timezone-aware-timestamps-as-timezone-naive-utc
    """

    impl = SADateTime
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return value

        if not value.tzinfo or value.tzinfo.utcoffset(value) is None:
            raise TypeError("tzinfo is required")

        value = value.astimezone(datetime.timezone.utc).replace(tzinfo=None)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = value.replace(tzinfo=datetime.timezone.utc)

        return value