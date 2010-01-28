from django.utils.translation import ugettext as _


# Add-on and File statuses.
STATUS_NULL = 0
STATUS_SANDBOX = 1
STATUS_PENDING = 2
STATUS_NOMINATED = 3
STATUS_PUBLIC = 4
STATUS_DISABLED = 5
STATUS_LISTED = 6
STATUS_BETA = 7

STATUS_CHOICES = {
    STATUS_NULL: 'Null',
    STATUS_SANDBOX: 'In the sandbox',
    STATUS_PENDING: 'Pending approval',
    STATUS_NOMINATED: 'Nominated to be public',
    STATUS_PUBLIC: 'Public',
    STATUS_DISABLED: 'Disabled',
    STATUS_LISTED: 'Listed',
    STATUS_BETA: 'Beta',
}

# Add-on author roles.
AUTHOR_ROLE_NONE = 0
AUTHOR_ROLE_VIEWER = 1
AUTHOR_ROLE_DEV = 4
AUTHOR_ROLE_OWNER = 5
AUTHOR_ROLE_ADMIN = 6
AUTHOR_ROLE_ADMINOWNER = 7

AUTHOR_CHOICES = {
    AUTHOR_ROLE_NONE: 'None',
    AUTHOR_ROLE_VIEWER: 'Viewer',
    AUTHOR_ROLE_DEV: 'Developer',
    AUTHOR_ROLE_OWNER: 'Owner',
    AUTHOR_ROLE_ADMIN: 'Admin',
    AUTHOR_ROLE_ADMINOWNER: 'Admin & Owner',
}

# Collection author roles.
COLLECTION_ROLE_PUBLISHER = 0
COLLECTION_ROLE_ADMIN = 1

COLLECTION_AUTHOR_CHOICES = {
    COLLECTION_ROLE_PUBLISHER: 'Publisher',
    COLLECTION_ROLE_ADMIN: 'Admin',
}

# Addon types
ADDON_ANY = -1
ADDON_EXTENSION = 1
ADDON_THEME = 2
ADDON_DICT = 3
ADDON_SEARCH = 4
ADDON_LPAPP = 5
ADDON_LPADDON = 6
ADDON_PLUGIN = 7
ADDON_API = 8 # not actually a type but used to identify extensions + themes
ADDON_PERSONA = 9

# Applications
class FIREFOX:
    id = 1
    short = 'firefox'
    pretty = _('Firefox')
    browser = True

class THUNDERBIRD:
    id = 18
    short = 'thunderbird'
    pretty = _('Thunderbird')
    browser = True

class SEAMONKEY:
    id = 59
    short = 'seamonkey'
    pretty = _('SeaMonkey')
    browser = True

class SUNBIRD:
    id = 52
    short = 'sunbird'
    pretty = _('Sunbird')

class MOBILE:
    id = 60
    short = 'mobile'
    pretty = _('Mobile')
    browser = True

_apps = (FIREFOX, THUNDERBIRD, SEAMONKEY, SUNBIRD, MOBILE)
APPS = dict((app.short, app) for app in _apps)
APP_IDS = dict((app.id, app) for app in _apps)
