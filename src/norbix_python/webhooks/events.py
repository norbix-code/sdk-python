from __future__ import annotations

from typing import Final

#: Closed catalog of event names a destination may subscribe to.
#: Source: gateway Domain trigger event-name value objects.
NORBIX_WEBHOOK_EVENT_NAMES: Final[tuple[str, ...]] = (
    "database.record.inserted",
    "database.record.updated",
    "database.record.deleted",
    "database.record.replaced",
    "database.record.responsibilityChanged",
    "database.records.inserted",
    "database.records.updated",
    "database.records.deleted",
    "membership.user.registered",
    "membership.user.invited",
    "membership.user.verified",
    "membership.user.updated",
    "membership.user.deleted",
    "membership.user.blocked",
    "membership.user.reactivated",
    "files.file.uploaded",
    "files.file.deleted",
)


class NorbixWebhookEvents:
    """Named event constants — use these instead of raw strings.

    Example:
        receiver.on(NorbixWebhookEvents.Membership.USER_REGISTERED, handler)
    """

    class Database:
        RECORD_INSERTED: Final = "database.record.inserted"
        RECORD_UPDATED: Final = "database.record.updated"
        RECORD_DELETED: Final = "database.record.deleted"
        RECORD_REPLACED: Final = "database.record.replaced"
        RECORD_RESPONSIBILITY_CHANGED: Final = "database.record.responsibilityChanged"
        RECORDS_INSERTED: Final = "database.records.inserted"
        RECORDS_UPDATED: Final = "database.records.updated"
        RECORDS_DELETED: Final = "database.records.deleted"

    class Membership:
        USER_REGISTERED: Final = "membership.user.registered"
        USER_INVITED: Final = "membership.user.invited"
        USER_VERIFIED: Final = "membership.user.verified"
        USER_UPDATED: Final = "membership.user.updated"
        USER_DELETED: Final = "membership.user.deleted"
        USER_BLOCKED: Final = "membership.user.blocked"
        USER_REACTIVATED: Final = "membership.user.reactivated"

    class Files:
        FILE_UPLOADED: Final = "files.file.uploaded"
        FILE_DELETED: Final = "files.file.deleted"
