# 1
class TransactionalSaver:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        self.backup = self.obj.copy()
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.obj.clear()
            self.obj.update(self.backup)
            return True
        return False


# 2
class SuppressAndLog:
    def __init__(self, *errors):
        self.errors = errors

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.errors:
            print("Error suppressed:", exc_type.__name__)
            return True
        return False


# 3
class CacheManager:
    cache = {}

    def __init__(self, key):
        self.key = key

    def __enter__(self):
        return self

    def set(self, value):
        CacheManager.cache[self.key] = value

    def get(self):
        return CacheManager.cache.get(self.key)

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


# 4
class mock:
    def __init__(self, obj, **kwargs):
        self.obj = obj
        self.new_attrs = kwargs
        self.old_attrs = {}

    def __enter__(self):
        for k in self.new_attrs:
            if hasattr(self.obj, k):
                self.old_attrs[k] = getattr(self.obj, k)
            setattr(self.obj, k, self.new_attrs[k])
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        for k in self.new_attrs:
            if k in self.old_attrs:
                setattr(self.obj, k, self.old_attrs[k])
            else:
                delattr(self.obj, k)
        return False
