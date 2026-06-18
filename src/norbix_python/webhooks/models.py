from __future__ import annotations

import warnings
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class _Model(BaseModel):
    """Base for webhook DTOs — permissive and camelCase-aware, matching the SDK."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)


class UserDto(_Model):
    """A membership user. Email / username are optional (username-only signup)."""

    id: str | None = None
    type: str | None = None
    email: str | None = None
    user_name: str | None = Field(default=None, alias="userName")
    roles: list[str] | None = None
    tags: list[str] | None = None
    status: str | None = None
    created_on: str | None = Field(default=None, alias="createdOn")
    modified_on: str | None = Field(default=None, alias="modifiedOn")


class FileResourceRef(_Model):
    """A file reference carried by files.* events."""

    path: str | None = None
    name: str | None = None
    size: int | None = None
    content_type: str | None = Field(default=None, alias="contentType")


class UserInvited(_Model):
    """membership.user.invited payload (no full entity yet)."""

    email: str | None = None


class FileDeleted(_Model):
    """files.file.deleted payload."""

    path: str | None = None


class Mutation(_Model, Generic[T]):
    """A before/after pair for a mutation event (user.updated, record.updated)."""

    from_: T = Field(alias="from")
    to: T


class UserMutation(Mutation[UserDto]):
    """membership.user.updated payload — `from`/`to` are full users."""


class WebhookSchemaInfo(_Model):
    """Schema identifiers for database.* events."""

    id: str | None = None
    name: str = ""


class WebhookEntityRef(_Model):
    """A single entity id reference."""

    id: str


class WebhookRecordIds(_Model):
    """Batch record ids."""

    ids: list[str] = Field(default_factory=list)


# ``schema`` intentionally shadows the deprecated BaseModel.schema() helper so
# handler code can read ``event.metadata.schema`` (matching the TS SDK). The
# field is built by the SDK, never a JSON-schema call — silence the one warning.
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", message='Field name "schema" .* shadows')

    class WebhookEventMetadata(_Model):
        """Identifiers lifted off the wire payload onto ``event.metadata``."""

        user: WebhookEntityRef | None = None
        schema: WebhookSchemaInfo | None = None  # type: ignore[assignment]
        record: WebhookEntityRef | None = None
        records: WebhookRecordIds | None = None
        integration_id: str | None = Field(default=None, alias="integrationId")


class WebhookEnvelope(_Model):
    """The raw JSON envelope POSTed to a destination."""

    id: str
    event: str
    created_on: str | None = Field(default=None, alias="createdOn")
    account_id: str | None = Field(default=None, alias="accountId")
    project_id: str | None = Field(default=None, alias="projectId")
    trigger_id: str | None = Field(default=None, alias="triggerId")
    data: Any = None


class WebhookEvent(_Model):
    """Metadata object passed as the 2nd argument to a typed handler.

    Carries the delivery facts plus identifiers under ``metadata``.
    """

    name: str
    delivery_id: str = Field(alias="deliveryId")
    created_on: str | None = Field(default=None, alias="createdOn")
    trigger_id: str | None = Field(default=None, alias="triggerId")
    correlation_id: str | None = Field(default=None, alias="correlationId")
    account_id: str | None = Field(default=None, alias="accountId")
    project_id: str | None = Field(default=None, alias="projectId")
    integration_id: str | None = Field(default=None, alias="integrationId")
    destination_id: str | None = Field(default=None, alias="destinationId")
    verified: bool | None = None
    metadata: WebhookEventMetadata = Field(default_factory=WebhookEventMetadata)
    raw: WebhookEnvelope


class WebhookContext(_Model):
    """Context passed to ``on_all`` handlers alongside the envelope."""

    path: str | None = None
    verified: bool | None = None
    account_id: str | None = Field(default=None, alias="accountId")
    project_id: str | None = Field(default=None, alias="projectId")
    integration_id: str | None = Field(default=None, alias="integrationId")
    destination_id: str | None = Field(default=None, alias="destinationId")


class WebhookHandleResult(_Model):
    """Result of handling a delivery (return 200 to the caller)."""

    received: bool = True
    event: str
    delivery_id: str = Field(alias="deliveryId")
    verified: bool | None = None
    handled: bool = False
    trigger_id: str | None = Field(default=None, alias="triggerId")
