from django.conf import settings
import random

class DatabaseRouter(object):
    def db_for_read(self, model, **hints):
        return random.choice(['default'])

    def db_for_write(self, model, **hints):
        # Always return the default database
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):

        db1 = settings.DATABASE_APPS_MAPPING.get(obj1._meta.app_label)
        db2 = settings.DATABASE_APPS_MAPPING.get(obj2._meta.app_label)
        if db1 and db2:
            return db1 == db2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if db in settings.DATABASE_APPS_MAPPING.values():
            return settings.DATABASE_APPS_MAPPING.get(app_label) == db
        elif app_label in settings.DATABASE_APPS_MAPPING:
            return False
    
    