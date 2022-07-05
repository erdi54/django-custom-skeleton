import shortuuid
from django_extensions.db.fields import ShortUUIDField, UUIDVersionError


class _ShortUUIDField(ShortUUIDField):
    def __init__(self, *args, **kwargs):
        super(_ShortUUIDField, self).__init__(*args, **kwargs)
        kwargs['max_length'] = 22

    def create_uuid(self):
        if not self.version or self.version == 4:
            return shortuuid.uuid()
        elif self.version == 1:
            return shortuuid.uuid()
        elif self.version == 2:
            raise UUIDVersionError("UUID version 2 is not supported.")
        elif self.version == 3:
            raise UUIDVersionError("UUID version 3 is not supported.")
        elif self.version == 5:
            return shortuuid.uuid(name=self.namespace)
        else:
            raise UUIDVersionError("UUID version %s is not valid." % self.version)
