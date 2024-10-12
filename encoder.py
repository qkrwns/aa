from sqlalchemy.ext.declarative import DeclarativeMeta
import json
import datetime

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        if isinstance(obj.__class__, DeclarativeMeta):
            # Convert SQLAlchemy model to dictionary
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and not x.startswith('query')]:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    else:
                        json.dumps(data)
                        fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields
        return json.JSONEncoder.default(self, obj)