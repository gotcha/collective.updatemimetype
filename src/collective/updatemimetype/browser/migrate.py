from Products.Five import BrowserView
from collective.updatemimetype.migration import migrate


class MigrateView(BrowserView):

    def __call__(self):
        migrate(self.context)
        return 'migrated'
