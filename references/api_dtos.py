""" Options:
Date: 2026-10-07 10:03:25
Version: 10.20
Tip: To override a DTO option, remove "#" prefix before updating
BaseUrl: http://localhost:5002

#GlobalNamespace: 
#AddServiceStackTypes: True
#AddResponseStatus: False
#AddImplicitVersion: 
#AddDescriptionAsComments: True
#IncludeTypes: 
#ExcludeTypes: 
#DefaultImports: datetime,decimal,marshmallow.fields:*,servicestack:*,typing:*,dataclasses:dataclass/field,dataclasses_json:dataclass_json/LetterCase/Undefined/config,enum:Enum/IntEnum
#DataClass: 
#DataClassJson: 
"""

import datetime
import decimal
from marshmallow.fields import *
from servicestack import *
from typing import *
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase, Undefined, config
from enum import Enum, IntEnum
Object = TypeVar('Object')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestBase(ICultureBasedRequest, IVersionBasedRequest, IHasCorrelationIdRequest):
    # @ApiMember(DataType="string", Description="Specify culture code when your response from the API should be localised. E.g.: en", Name="CultureCode", ParameterType="header")
    culture_code: Optional[str] = None
    """
    Specify culture code when your response from the API should be localised. E.g.: en
    """


    # @ApiMember(DataType="string", Description="TimeZone", Name="TimeZoneId", ParameterType="header")
    time_zone_id: Optional[str] = None
    """
    TimeZone
    """


    # @ApiMember(DataType="string", Description="The CodeMash API version used to fetch data from the API. If not specified, the last version will be used.  E.g.: v3", IsRequired=true, Name="version", ParameterType="path")
    version: Optional[str] = None
    """
    The CodeMash API version used to fetch data from the API. If not specified, the last version will be used.  E.g.: v3
    """


    # @ApiMember(DataType="string", Description="CorrelationId for each request", Name="CorrelationId", ParameterType="header")
    correlation_id: Optional[str] = None
    """
    CorrelationId for each request
    """


class ICultureBasedRequest:
    culture_code: Optional[str] = None


class IVersionBasedRequest:
    version: Optional[str] = None


class IHasCorrelationIdRequest:
    correlation_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashRequestBase(RequestBase, IHasProjectId, IHasEnv):
    # @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as norbix-project-id.", IsRequired=true, Name="norbix-project-id", ParameterType="header")
    project_id: Optional[str] = None
    """
    ID of your project. Can be passed in a header as norbix-project-id.
    """


    # @ApiMember(DataType="string", Description="Target environment for this request (e.g. TEST, STAGING). Optional — when omitted the request runs against PROD. Can be passed in a header as norbix-env.", Name="norbix-env", ParameterType="header")
    env: Optional[str] = None
    """
    Target environment for this request (e.g. TEST, STAGING). Optional — when omitted the request runs against PROD. Can be passed in a header as norbix-env.
    """


class IHasProjectId:
    project_id: Optional[str] = None


class IHasEnv:
    env: Optional[str] = None


class Gender(str, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class MarketingBlockReason(str, Enum):
    UNSPECIFIED = 'Unspecified'
    UNSUBSCRIBED = 'Unsubscribed'
    COMPLAINT = 'Complaint'
    HARD_BOUNCE = 'HardBounce'
    INVALID_EMAIL = 'InvalidEmail'
    ADMIN_BLOCK = 'AdminBlock'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserGeneralInfoDto:
    phone: Optional[str] = None
    primary_email: Optional[str] = None
    display_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    company: Optional[str] = None
    gender: Optional[Gender] = None
    birth_date: Optional[int] = None
    time_zone: Optional[str] = None
    language: Optional[str] = None
    block_all_marketing_messages: bool = False
    blocked_tags: Optional[Dict[str, HashSet[str]]] = None
    block_reasons: Optional[List[MarketingBlockReason]] = None
    extra_metadata: Optional[str] = None
    notes: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveUser(CodeMashRequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


    # @ApiMember(DataType="object", Description="User Info", Name="UserGeneralInfo", ParameterType="body")
    user_general_info: Optional[UserGeneralInfoDto] = None
    """
    User Info
    """


    # @ApiMember(Description="Attach this login to an existing user id. Optional.")
    user_id: Optional[str] = None
    """
    Attach this login to an existing user id. Optional.
    """


    # @ApiMember(DataType="boolean", Description="Ignore UserRegistersAsRole from Membership Settings", Name="IgnoreUserRegistersAsRole", ParameterType="body")
    ignore_user_registers_as_role: bool = False
    """
    Ignore UserRegistersAsRole from Membership Settings
    """
    @staticmethod
    def response_type(): return IdResponse


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveUserWithRolesBase(SaveUser):
    roles: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashListPaginationRequestBase(RequestBase, IHasProjectId, IHasEnv):
    # @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as norbix-project-id.", IsRequired=true, Name="norbix-project-id", ParameterType="header")
    project_id: Optional[str] = None
    """
    ID of your project. Can be passed in a header as norbix-project-id.
    """


    # @ApiMember(DataType="string", Description="Target environment for this request (e.g. TEST, STAGING). Optional — when omitted the request runs against PROD. Can be passed in a header as norbix-env.", Name="norbix-env", ParameterType="header")
    env: Optional[str] = None
    """
    Target environment for this request (e.g. TEST, STAGING). Optional — when omitted the request runs against PROD. Can be passed in a header as norbix-env.
    """


    # @ApiMember(DataType="string", Description="Cursor token — fetch the page AFTER this item.", Name="startingAfter", ParameterType="query")
    starting_after: Optional[str] = None
    """
    Cursor token — fetch the page AFTER this item.
    """


    # @ApiMember(DataType="string", Description="Cursor token — fetch the page BEFORE this item.", Name="endingBefore", ParameterType="query")
    ending_before: Optional[str] = None
    """
    Cursor token — fetch the page BEFORE this item.
    """


    # @ApiMember(DataType="integer", Description="Amount of records to return.", Format="int32", Name="pageSize", ParameterType="query")
    page_size: Optional[int] = None
    """
    Amount of records to return.
    """


class IPasskeyCeremonyRequest:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CursorArgs(ICursorArgs):
    field: Optional[str] = None
    order: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PagingArgs:
    cursor_args: Optional[CursorArgs] = None
    page_size: Optional[int] = None
    starting_after: Optional[str] = None
    ending_before: Optional[str] = None


class CodeMashRelease(str, Enum):
    NOT_SET = 'NotSet'
    COMMUNITY = 'Community'
    MANAGED_SERVICE = 'ManagedService'
    ENTERPRISE = 'Enterprise'


class CodeMashRuntime(str, Enum):
    DEVELOPMENT = 'Development'
    CI = 'CI'
    STAGING = 'Staging'
    PRODUCTION = 'Production'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EchoLicenseDto:
    domain: Optional[str] = None
    account_id: Optional[str] = None
    email: Optional[str] = None
    release: Optional[str] = None
    expire: int = 0
    is_trial: bool = False
    projects_cap: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EchoRegionDto:
    code: Optional[str] = None
    display_name: Optional[str] = None
    api_url: Optional[str] = None
    hub_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EchoAgentDto:
    mcp_url: Optional[str] = None
    o_auth_metadata_url: Optional[str] = None
    installation_type: Optional[str] = None
    onboarding_docs_url: Optional[str] = None
    tools_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicBrandDto:
    display_name: Optional[str] = None
    main_color: Optional[str] = None
    accent_color: Optional[str] = None
    logo_url: Optional[str] = None
    icon_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicPasswordPolicyDto:
    min_length: int = 0
    max_length: Optional[int] = None
    min_numbers: Optional[int] = None
    min_upper: Optional[int] = None
    min_lower: Optional[int] = None
    min_special: Optional[int] = None
    allowed_special: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicAuthDto:
    social_providers: List[str] = field(default_factory=list)
    passkey: bool = False
    methods: Optional[List[str]] = None
    password_policy: Optional[PublicPasswordPolicyDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicAiAssistantDto:
    id: Optional[str] = None
    name: Optional[str] = None
    welcome: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicAiChatDto:
    enabled: bool = False
    assistants: List[PublicAiAssistantDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ErrorDto:
    message: Optional[str] = None
    error_code: Optional[str] = None
    context: Optional[Dict[str, str]] = None
    stack_trace: Optional[List[ErrorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashResponseStatus:
    is_success: bool = False
    errors: Optional[List[ErrorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResponseBase:
    response_status: Optional[CodeMashResponseStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EndUserChatAttachment:
    id: Optional[str] = None
    session_id: Optional[str] = None
    file_name: Optional[str] = None
    content_type: Optional[str] = None
    kind: Optional[str] = None
    size: int = 0
    summary: Optional[str] = None
    created_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EndUserChatMemoryNote:
    id: Optional[str] = None
    session_id: Optional[str] = None
    kind: Optional[str] = None
    text: Optional[str] = None
    created_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EndUserChatAssistant:
    id: Optional[str] = None
    name: Optional[str] = None
    welcome_message: Optional[str] = None
    is_default: bool = False
    memory_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EndUserChatPlan:
    id: Optional[str] = None
    name: Optional[str] = None
    quota_unit: Optional[str] = None
    monthly_quota: int = 0
    used: int = 0
    remaining: int = 0
    attachments: bool = False
    rag: bool = False
    memory: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EndUserChatSession:
    id: Optional[str] = None
    assistant_id: Optional[str] = None
    title: Optional[str] = None
    is_pinned: bool = False
    is_archived: bool = False
    last_seq: int = 0
    created_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    updated_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatEntryWireDto:
    kind: Optional[str] = None
    id: Optional[str] = None
    seq: int = 0
    at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    ref_entry_id: Optional[str] = None
    work_item_id: Optional[str] = None
    feedback: Optional[str] = None
    feedback_at_utc: Optional[datetime.datetime] = None
    feedback_by_user_auth_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EndUserAiToolParameter:
    name: Optional[str] = None
    type: Optional[str] = None
    required: bool = False
    description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EndUserAiTool:
    name: Optional[str] = None
    description: Optional[str] = None
    toolsets: List[str] = field(default_factory=list)
    requires_confirmation: bool = False
    parameters: List[EndUserAiToolParameter] = field(default_factory=list)


class AuthType(str, Enum):
    SERVICE = 'Service'
    EMAIL = 'Email'
    USER_NAME = 'UserName'
    PHONE = 'Phone'
    GUEST = 'Guest'
    SOCIAL = 'Social'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccessInformationDto:
    ip: Optional[str] = None
    date: Optional[datetime.datetime] = None
    time_zone: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RegistrationDto:
    registration_information: Optional[AccessInformationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoginDto:
    need_change_password_on_next_login: bool = False
    last_access_information: Optional[AccessInformationDto] = None


class AuthStatus(IntEnum):
    REGISTERED = 0
    PENDING_VALIDATION = 2
    ACTIVE = 8
    UNREGISTERED = 16
    SUSPENDED = 32
    IN_ACTIVE = 64
    BLOCKED = 128


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuthDto(IBindableContract):
    id: Optional[str] = None
    type: Optional[AuthType] = None
    email: Optional[str] = None
    user_name: Optional[str] = None
    registration: Optional[RegistrationDto] = None
    login: Optional[LoginDto] = None
    general_info: Optional[UserGeneralInfoDto] = None
    roles: Optional[List[str]] = None
    push_devices: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    status: Optional[AuthStatus] = None
    created_on: datetime.datetime = datetime.datetime(1, 1, 1)
    modified_on: datetime.datetime = datetime.datetime(1, 1, 1)


TViewModelProjection = TypeVar('TViewModelProjection')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaginatedResponse(Generic[TViewModelProjection]):
    items: Optional[IList[TViewModelProjection]] = None
    has_more: bool = False
    has_previous: bool = False
    starting_after: Optional[str] = None
    ending_before: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserMarketingPreferencesDto:
    block_all_marketing_messages: bool = False
    blocked_tags: Optional[Dict[str, HashSet[str]]] = None
    block_reasons: Optional[List[MarketingBlockReason]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyListItemDto:
    credential_id: Optional[str] = None
    friendly_name: Optional[str] = None
    registered_on_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    last_used_on_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    is_revoked: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TermMultiParentDto:
    taxonomy_id: Optional[str] = None
    parent_id: Optional[str] = None
    name: Optional[str] = None
    names: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TermTreeDto:
    id: Optional[str] = None
    taxonomy_id: Optional[str] = None
    taxonomy_name: Optional[str] = None
    parent_id: Optional[str] = None
    order: Optional[int] = None
    name: Optional[str] = None
    names: Optional[Dict[str, str]] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    descriptions: Optional[Dict[str, str]] = None
    multi_parents: Optional[List[TermMultiParentDto]] = None
    meta: Optional[Object] = None
    children: Optional[List[TermTreeDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomyTreeDto:
    view_id: Optional[str] = None
    taxonomy_name: Optional[str] = None
    taxonomy_slug: Optional[str] = None
    parent_id: Optional[str] = None
    children: Optional[List[TaxonomyTreeDto]] = None
    terms: Optional[List[TermTreeDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TermDto:
    id: Optional[str] = None
    taxonomy_id: Optional[str] = None
    taxonomy_name: Optional[str] = None
    parent_id: Optional[str] = None
    order: Optional[int] = None
    name: Optional[str] = None
    names: Optional[Dict[str, str]] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    descriptions: Optional[Dict[str, str]] = None
    multi_parents: Optional[List[TermMultiParentDto]] = None
    meta: Optional[Object] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class JsonSchemaFieldDto:
    field_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DataSchemaDto:
    json: Optional[str] = None
    fields: List[JsonSchemaFieldDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class VisualSchemaDto:
    json: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaSettingsDto:
    soft_delete: bool = False
    has_record_owner: bool = False
    description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaEmbedSettingsDto:
    enabled: bool = False
    fields: List[str] = field(default_factory=list)
    embedding_integration_id: Optional[str] = None
    per_user: bool = False


class TriggerType(str, Enum):
    MEMBERSHIP = 'Membership'
    SCHEMA = 'Schema'
    FILES = 'Files'
    PAYMENTS = 'Payments'
    AI = 'Ai'


class TriggerActionType(str, Enum):
    CODE = 'Code'
    PUSH = 'Push'
    SMS = 'Sms'
    EMAIL = 'Email'
    WEBHOOK_CALL = 'WebhookCall'
    SSE_CALL = 'SseCall'
    MARKETPLACE = 'Marketplace'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerActionDto:
    type: Optional[TriggerActionType] = None
    integration_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerDto(IHasViewId):
    type: Optional[TriggerType] = None
    view_id: Optional[str] = None
    name: Optional[str] = None
    then_action: Optional[TriggerActionDto] = None
    description: Optional[str] = None
    is_enabled: bool = False
    activation_code: Optional[str] = None
    saved_by_auth_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDto(IHasViewId):
    view_id: Optional[str] = None
    schema_name: Optional[str] = None
    schema_slug: Optional[str] = None
    version: int = 0
    meta_schema_version: int = 0
    data_schema: Optional[DataSchemaDto] = None
    visual_schema: Optional[VisualSchemaDto] = None
    published_at: datetime.datetime = datetime.datetime(1, 1, 1)
    settings: Optional[SchemaSettingsDto] = None
    embed: Optional[SchemaEmbedSettingsDto] = None
    triggers: Optional[List[TriggerDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaListProjection(IHasViewId):
    view_id: Optional[str] = None
    schema_name: Optional[str] = None
    schema_title: Optional[str] = None
    latest_version: Optional[int] = None
    has_draft: bool = False
    meta_schema_version: int = 0
    description: Optional[str] = None
    env: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileChecksumDto:
    algorithm: Optional[str] = None
    hash: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileResourceDto:
    id: Optional[str] = None
    original_file_name: Optional[str] = None
    extension: Optional[str] = None
    stored_file_name: Optional[str] = None
    size_bytes: Optional[int] = None
    checksum: Optional[FileChecksumDto] = None


class FileProvider(str, Enum):
    LOCAL = 'Local'
    AWS_S3 = 'AwsS3'
    AZURE_BLOB_STORAGE = 'AzureBlobStorage'
    GOOGLE_CLOUD_STORAGE = 'GoogleCloudStorage'
    FTP = 'Ftp'
    APPLE_I_CLOUD = 'AppleICloud'
    DROP_BOX = 'DropBox'
    GOOGLE_DRIVE = 'GoogleDrive'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileResourceRefDto:
    resource: Optional[FileResourceDto] = None
    integration_id: Optional[str] = None
    provider: Optional[FileProvider] = None
    path: Optional[str] = None
    public_url: Optional[str] = None
    is_public: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicFolderDto:
    path: Optional[str] = None
    public_id: Optional[str] = None
    public_url: Optional[str] = None
    inherited: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegrationTestResultItemDto:
    operation: Optional[str] = None
    result: Optional[str] = None
    errors: Optional[IReadOnlyList[str]] = None


class IBindableContract:
    pass


class IHasViewId:
    view_id: Optional[str] = None


class ICursorArgs:
    field: Optional[str] = None
    order: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StringFieldDto(JsonSchemaFieldDto):
    format: Optional[str] = None
    pattern: Optional[str] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    translate_options: Optional[IReadOnlyDictionary[str, str]] = None
    default: Optional[str] = None
    unique: Optional[bool] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DecimalFieldDto(JsonSchemaFieldDto):
    minimum: Optional[Decimal] = None
    maximum: Optional[Decimal] = None
    multiple_of: Optional[Decimal] = None
    default: Optional[Decimal] = None
    unique: Optional[bool] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CurrencyDefaultDto:
    value: Decimal = decimal.Decimal(0)
    currency: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CurrencyFieldDto(JsonSchemaFieldDto):
    allowed_currencies: Optional[IReadOnlyList[str]] = None
    multiple_of: Optional[Decimal] = None
    minimum: Optional[Decimal] = None
    maximum: Optional[Decimal] = None
    default: Optional[CurrencyDefaultDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BooleanFieldDto(JsonSchemaFieldDto):
    default: Optional[bool] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DateFieldDto(JsonSchemaFieldDto):
    minimum: Optional[int] = None
    maximum: Optional[int] = None
    default: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegerFieldDto(JsonSchemaFieldDto):
    minimum: Optional[int] = None
    maximum: Optional[int] = None
    default: Optional[int] = None
    unique: Optional[bool] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GeolocationFieldDto(JsonSchemaFieldDto):
    allowed_types: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagsFieldDto(JsonSchemaFieldDto):
    min_items: Optional[int] = None
    max_items: Optional[int] = None
    default: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileFieldDto(JsonSchemaFieldDto):
    storages: Optional[IReadOnlyList[str]] = None
    min_items: Optional[int] = None
    max_items: Optional[int] = None
    allowed_file_type: Optional[str] = None
    max_size_mb: Optional[Decimal] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomySelectionFieldDto(JsonSchemaFieldDto):
    taxonomy_id: Optional[str] = None
    multiple: bool = False
    display_field: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CollectionSelectionFieldDto(JsonSchemaFieldDto):
    collection_id: Optional[str] = None
    display_field: Optional[str] = None
    multiple: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserSelectionFieldDto(JsonSchemaFieldDto):
    multiple: bool = False
    display_field: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleSelectionFieldDto(JsonSchemaFieldDto):
    multiple: bool = False
    display_field: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnumSelectionFieldDto(JsonSchemaFieldDto):
    values: Optional[IReadOnlyList[str]] = None
    multiple: bool = False
    default: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ObjectFieldDto(JsonSchemaFieldDto):
    properties: Optional[IReadOnlyList[JsonSchemaFieldDto]] = None
    required: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ArrayFieldDto(JsonSchemaFieldDto):
    items: Optional[JsonSchemaFieldDto] = None
    min_items: Optional[int] = None
    max_items: Optional[int] = None
    unique_items: Optional[bool] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class JsonFieldDto(JsonSchemaFieldDto):
    max_bytes: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EchoResponse:
    container_name: Optional[str] = None
    ip: Optional[str] = None
    release: Optional[CodeMashRelease] = None
    runtime: Optional[CodeMashRuntime] = None
    managed_service_hub_url: Optional[str] = None
    managed_service_api_url: Optional[str] = None
    hub_url: Optional[str] = None
    api_url: Optional[str] = None
    api_version: Optional[str] = None
    hub_version: Optional[str] = None
    mjml_url: Optional[str] = None
    admin_url_template: Optional[str] = None
    license: Optional[EchoLicenseDto] = None
    ask_for_enterprise_license_email: Optional[str] = None
    email_service_configured: bool = False
    root_bootstrap_password_source: Optional[str] = None
    regions: Optional[List[EchoRegionDto]] = None
    is_production_installation: bool = False
    licensing_mode: Optional[str] = None
    grace_days_left: Optional[int] = None
    installation_domain: Optional[str] = None
    licensing_docs_url: Optional[str] = None
    agent: Optional[EchoAgentDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicProjectConfigDto:
    display_name: Optional[str] = None
    admin_portal_enabled: bool = False
    branding: Optional[PublicBrandDto] = None
    auth: Optional[PublicAuthDto] = None
    ai_chat: Optional[PublicAiChatDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicLegalDocumentDto:
    kind: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    available: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListEndUserChatAttachmentsResponse(ResponseBase):
    attachments: List[EndUserChatAttachment] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListEndUserChatMemoryResponse(ResponseBase):
    notes: List[EndUserChatMemoryNote] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEndUserChatAvailabilityResponse(ResponseBase):
    enabled: bool = False
    available: bool = False
    reason: Optional[str] = None
    default_assistant_id: Optional[str] = None
    assistants: List[EndUserChatAssistant] = field(default_factory=list)
    plan: Optional[EndUserChatPlan] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListEndUserChatSessionsResponse(ResponseBase):
    sessions: List[EndUserChatSession] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEndUserChatSessionResponse(ResponseBase):
    session: Optional[EndUserChatSession] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEndUserChatEntriesResponse(ResponseBase):
    session_id: Optional[str] = None
    entries: List[AiChatEntryWireDto] = field(default_factory=list)
    last_seq: int = 0
    has_more: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StartEndUserChatTurnResponse(ResponseBase):
    turn_id: Optional[str] = None
    session_id: Optional[str] = None
    channel: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEndUserAiToolsResponse(ResponseBase):
    tools: Optional[List[EndUserAiTool]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InvokeEndUserAiToolResponse(ResponseBase):
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserResponse(ResponseBase):
    user: Optional[AuthDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUsersResponse(ResponseBase):
    list: Optional[PaginatedResponse[AuthDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserPreferencesResponse(ResponseBase):
    preferences: Optional[UserMarketingPreferencesDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyOkResponse(ResponseBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyCeremonyOptionsResponse(ResponseBase):
    ceremony_id: Optional[str] = None
    options_json: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyAuthTokensResponse(ResponseBase):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_in_seconds: int = 0
    recovery_codes: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyListResponse(ResponseBase):
    passkeys: List[PasskeyListItemDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyRecoveryResponse(ResponseBase):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_in_seconds: int = 0
    remaining_codes: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyVerificationTokenResponse(ResponseBase):
    verification_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindMergedTermTreeResponse(ResponseBase):
    tree: Optional[List[TermTreeDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTaxonomyTreeResponse(ResponseBase):
    tree: Optional[List[TaxonomyTreeDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTermsResponse(ResponseBase):
    list: Optional[PaginatedResponse[TermDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTermsChildrenResponse(ResponseBase):
    list: Optional[PaginatedResponse[TermDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTermTreeResponse(ResponseBase):
    tree: Optional[List[TermTreeDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaResponse(ResponseBase):
    item: Optional[SchemaDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemasResponse(ResponseBase):
    list: Optional[PaginatedResponse[SchemaListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AggregateResponse(ResponseBase):
    result: Optional[List[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CountResponse(ResponseBase):
    count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DistinctResponse(ResponseBase):
    values: Optional[List[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ExecuteAggregateResponse(ResponseBase):
    result: Optional[List[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindResponse(ResponseBase):
    list: Optional[PaginatedResponse[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindOneResponse(ResponseBase):
    result: Optional[Object] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFileByIdResponse(ResponseBase):
    file: Optional[FileResourceRefDto] = None
    is_public: Optional[bool] = None
    public_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFileInfoResponse(ResponseBase):
    file: Optional[FileResourceRefDto] = None
    is_public: Optional[bool] = None
    public_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSignedUrlResponse(ResponseBase):
    url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListFilesResponse(ResponseBase):
    list: Optional[PaginatedResponse[FileResourceRefDto]] = None
    folders: Optional[IList[str]] = None
    public_folders: Optional[IList[PublicFolderDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestUploadUrlResponse(ResponseBase):
    url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestFilesIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


# @Route("/{version}/echo", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Echo(RequestBase, IReturn[EchoResponse]):
    pass


# @Route("/{version}/public/projects/{ProjectId}/brand/{Kind}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPublicProjectBrandAsset(RequestBase, IReturn[bytes]):
    project_id: Optional[str] = None
    kind: Optional[str] = None
    v: Optional[str] = None


# @Route("/{version}/public/projects/{ProjectId}/config", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPublicProjectConfig(RequestBase, IReturn[PublicProjectConfigDto]):
    project_id: Optional[str] = None


# @Route("/{version}/public/projects/{ProjectId}/legal/{Kind}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPublicProjectLegal(RequestBase, IReturn[PublicLegalDocumentDto]):
    project_id: Optional[str] = None
    kind: Optional[str] = None


# @Route("/{version}/ai/chat/sessions/{SessionId}/attachments", "POST")
# @Api(Description="Adds a file to one of the caller's own AI chats.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UploadEndUserChatAttachmentRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Adds a file to one of the caller's own AI chats.
    """

    session_id: Optional[str] = None
    file_name: Optional[str] = None
    content_type: Optional[str] = None
    base64_content: Optional[str] = None


# @Route("/{version}/ai/chat/sessions/{SessionId}/attachments", "GET")
# @Api(Description="Lists the files in one of the caller's own AI chats.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListEndUserChatAttachmentsRequest(CodeMashRequestBase, IReturn[ListEndUserChatAttachmentsResponse]):
    """
    Lists the files in one of the caller's own AI chats.
    """

    session_id: Optional[str] = None


# @Route("/{version}/ai/chat/attachments/{AttachmentId}", "DELETE")
# @Api(Description="Removes a file from one of the caller's own AI chats.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEndUserChatAttachmentRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Removes a file from one of the caller's own AI chats.
    """

    attachment_id: Optional[str] = None


# @Route("/{version}/ai/chat/sessions/{SessionId}/entries/{EntryId}/feedback", "PUT")
# @Api(Description="Likes, dislikes or clears one message of the caller's own AI chat.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetEndUserChatEntryFeedbackRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Likes, dislikes or clears one message of the caller's own AI chat.
    """

    session_id: Optional[str] = None
    entry_id: Optional[str] = None
    feedback: Optional[str] = None


# @Route("/{version}/ai/chat/memory", "GET")
# @Api(Description="Lists what the AI chat remembers about the caller.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListEndUserChatMemoryRequest(CodeMashRequestBase, IReturn[ListEndUserChatMemoryResponse]):
    """
    Lists what the AI chat remembers about the caller.
    """

    take: Optional[int] = None


# @Route("/{version}/ai/chat/memory/{NoteId}", "DELETE")
# @Api(Description="Forgets one thing the AI chat remembers about the caller.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ForgetEndUserChatMemoryRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Forgets one thing the AI chat remembers about the caller.
    """

    note_id: Optional[str] = None


# @Route("/{version}/ai/chat/availability", "GET")
# @Api(Description="Whether the AI chat can run for the caller, and which assistants it offers.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEndUserChatAvailabilityRequest(CodeMashRequestBase, IReturn[GetEndUserChatAvailabilityResponse]):
    """
    Whether the AI chat can run for the caller, and which assistants it offers.
    """

    pass


# @Route("/{version}/ai/chat/sessions", "GET")
# @Api(Description="Lists the caller's own AI chats.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListEndUserChatSessionsRequest(CodeMashRequestBase, IReturn[ListEndUserChatSessionsResponse]):
    """
    Lists the caller's own AI chats.
    """

    take: Optional[int] = None
    include_archived: bool = False


# @Route("/{version}/ai/chat/sessions", "POST")
# @Api(Description="Opens a new AI chat for the caller.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateEndUserChatSessionRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Opens a new AI chat for the caller.
    """

    assistant_id: Optional[str] = None
    title: Optional[str] = None


# @Route("/{version}/ai/chat/sessions/{SessionId}", "GET")
# @Api(Description="Returns one of the caller's own AI chats.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEndUserChatSessionRequest(CodeMashRequestBase, IReturn[GetEndUserChatSessionResponse]):
    """
    Returns one of the caller's own AI chats.
    """

    session_id: Optional[str] = None


# @Route("/{version}/ai/chat/sessions/{SessionId}", "PATCH")
# @Api(Description="Renames one of the caller's own AI chats.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RenameEndUserChatSessionRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Renames one of the caller's own AI chats.
    """

    session_id: Optional[str] = None
    title: Optional[str] = None


# @Route("/{version}/ai/chat/sessions/{SessionId}/pin", "PUT")
# @Api(Description="Pins or unpins one of the caller's own AI chats.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PinEndUserChatSessionRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Pins or unpins one of the caller's own AI chats.
    """

    session_id: Optional[str] = None
    pinned: bool = False


# @Route("/{version}/ai/chat/sessions/{SessionId}/archive", "PUT")
# @Api(Description="Archives or unarchives one of the caller's own AI chats.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ArchiveEndUserChatSessionRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Archives or unarchives one of the caller's own AI chats.
    """

    session_id: Optional[str] = None
    archived: bool = False


# @Route("/{version}/ai/chat/sessions/{SessionId}", "DELETE")
# @Api(Description="Deletes one of the caller's own AI chats.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEndUserChatSessionRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Deletes one of the caller's own AI chats.
    """

    session_id: Optional[str] = None


# @Route("/{version}/ai/chat/sessions/{SessionId}/entries", "GET")
# @Api(Description="Returns a page of one of the caller's own AI chat transcripts.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEndUserChatEntriesRequest(CodeMashRequestBase, IReturn[GetEndUserChatEntriesResponse]):
    """
    Returns a page of one of the caller's own AI chat transcripts.
    """

    session_id: Optional[str] = None
    after_seq: Optional[int] = None
    take: Optional[int] = None


# @Route("/{version}/ai/chat/turn", "POST")
# @Api(Description="Sends a message to the AI chat; the answer streams on the caller's channel.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StartEndUserChatTurnRequest(CodeMashRequestBase, IReturn[StartEndUserChatTurnResponse]):
    """
    Sends a message to the AI chat; the answer streams on the caller's channel.
    """

    session_id: Optional[str] = None
    assistant_id: Optional[str] = None
    message: Optional[str] = None


# @Route("/{version}/ai/tools", "GET")
# @Api(Description="Lists the AI tools a project user may use: only their own data (own:* toolsets).")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEndUserAiToolsRequest(RequestBase, IReturn[GetEndUserAiToolsResponse]):
    """
    Lists the AI tools a project user may use: only their own data (own:* toolsets).
    """

    pass


# @Route("/{version}/ai/tools/{ToolName}", "POST")
# @Api(Description="Invokes one own-scope AI tool as the calling project user.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InvokeEndUserAiToolRequest(RequestBase, IReturn[InvokeEndUserAiToolResponse]):
    """
    Invokes one own-scope AI tool as the calling project user.
    """

    tool_name: Optional[str] = None
    arguments_json: Optional[str] = None


# @Route("/{version}/membership/auth/block", "PATCH")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BlockUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Id of the user to block, from get_users.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the user to block, from get_users.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


# @Route("/{version}/membership/auth/register/service", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveSystemUserWithPermissions(SaveUserWithRolesBase, IReturn[IdResponse]):
    """
    Membership
    """

    pass


# @Route("/{version}/membership/auth/register/guest", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveGuestUser(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    pass


# @Route("/{version}/membership/auth/register/user-name", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveUserNameUser(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    password: Optional[str] = None
    user_name: Optional[str] = None


# @Route("/{version}/membership/auth/register/email", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailUser(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    password: Optional[str] = None
    email: Optional[str] = None


# @Route("/{version}/membership/auth/register/phone", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePhoneUser(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Phone number for the new user, in E.164 format.", IsRequired=true)
    phone: Optional[str] = None
    """
    Phone number for the new user, in E.164 format.
    """


# @Route("/{version}/membership/auth/register/phone-with-permissions", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePhoneUserNameWithPermissions(SaveUserWithRolesBase, IReturn[IdResponse]):
    """
    Membership
    """

    phone: Optional[str] = None


# @Route("/{version}/membership/auth/register/email-with-permissions", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailUserNameWithPermissions(SaveUserWithRolesBase, IReturn[IdResponse]):
    """
    Membership
    """

    password: Optional[str] = None
    email: Optional[str] = None


# @Route("/{version}/membership/auth/register/user-name-with-permissions", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveUserNameWithPermissions(SaveUserWithRolesBase, IReturn[IdResponse]):
    """
    Membership
    """

    password: Optional[str] = None
    user_name: Optional[str] = None


# @Route("/{version}/membership/auth", "DELETE")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Id of the user to delete, from get_users.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the user to delete, from get_users.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


# @Route("/{version}/membership/auth/{id}", "GET")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserRequest(CodeMashRequestBase, IReturn[GetUserResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Id of the user to fetch, from get_users.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the user to fetch, from get_users.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


# @Route("/{version}/membership/auth", "GET")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUsersRequest(CodeMashListPaginationRequestBase, IReturn[GetUsersResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


    # @ApiMember(Description="Include each user's effective permissions in the result.")
    include_permissions: bool = False
    """
    Include each user's effective permissions in the result.
    """


    # @ApiMember(Description="Only return users that have a registered push device.")
    user_should_have_push_device: bool = False
    """
    Only return users that have a registered push device.
    """


    # @ApiMember(Description="Only return users that have an email address.")
    user_should_have_email: bool = False
    """
    Only return users that have an email address.
    """


    # @ApiMember(Description="Include each user's metadata in the result.")
    include_meta: bool = False
    """
    Include each user's metadata in the result.
    """


    # @ApiMember(Description="Filter to users that have any of these role names.")
    role_names: Optional[List[str]] = None
    """
    Filter to users that have any of these role names.
    """


    # @ApiMember(Description="Filter to these specific user ids.")
    user_ids: Optional[List[str]] = None
    """
    Filter to these specific user ids.
    """


# @Route("/{version}/membership/auth/{id}/preferences", "GET")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserPreferencesRequest(CodeMashRequestBase, IReturn[GetUserPreferencesResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Id of the user whose preferences to fetch, from get_users.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the user whose preferences to fetch, from get_users.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the project's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the project's default integration.
    """


# @Route("/{version}/membership/users/{contactId}/marketing-state/{channel}/consent", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GrantContactConsentRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Id of the user (contact) to grant consent for.", IsRequired=true)
    contact_id: Optional[str] = None
    """
    Id of the user (contact) to grant consent for.
    """


    # @ApiMember(Description="Delivery channel to grant consent on: Email, Sms, or Push.", IsRequired=true)
    channel: Optional[str] = None
    """
    Delivery channel to grant consent on: Email, Sms, or Push.
    """


    # @ApiMember(Description="Lawful basis for the consent, e.g. Consent. Defaults to Consent.")
    lawful_basis: Optional[str] = None
    """
    Lawful basis for the consent, e.g. Consent. Defaults to Consent.
    """


    # @ApiMember(Description="Source of the consent, e.g. UserOptIn. Defaults to UserOptIn.")
    source: Optional[str] = None
    """
    Source of the consent, e.g. UserOptIn. Defaults to UserOptIn.
    """


    # @ApiMember(Description="Optional free-text reference to evidence of consent (e.g. a form submission id).")
    evidence_ref: Optional[str] = None
    """
    Optional free-text reference to evidence of consent (e.g. a form submission id).
    """


# @Route("/{version}/membership/auth/invite", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InviteUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Email address the invitation is sent to.", IsRequired=true)
    email: Optional[str] = None
    """
    Email address the invitation is sent to.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


# @Route("/{version}/membership/auth/{userId}/link-identity", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LinkIdentityRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    user_id: Optional[str] = None
    provider: Optional[str] = None
    provider_token: Optional[str] = None
    email_to_verify: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/membership/users/{userId}/map-auth", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MapAuthToUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    user_id: Optional[str] = None
    auth_id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/membership/auth/assign-roles", "PUT")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssignRolePermissionsRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Id of the user login to assign roles to, from get_users.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the user login to assign roles to, from get_users.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


    # @ApiMember(Description="The complete new list of role names (full replacement), from get_roles.")
    roles: Optional[List[str]] = None
    """
    The complete new list of role names (full replacement), from get_roles.
    """


# @Route("/{version}/membership/users/{userId}/roles", "PUT")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetContactRolesRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Id of the human user to assign roles to.", IsRequired=true)
    user_id: Optional[str] = None
    """
    Id of the human user to assign roles to.
    """


    # @ApiMember(Description="The complete new list of role ids (full replacement), from get_roles. Empty/omitted clears all roles.")
    roles: Optional[List[str]] = None
    """
    The complete new list of role ids (full replacement), from get_roles. Empty/omitted clears all roles.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


# @Route("/{version}/membership/users/{contactId}/marketing-state/{commChannel}/{channel}/tags/{tag}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetContactTagSubscriptionRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Id of the user (contact) to update.", IsRequired=true)
    contact_id: Optional[str] = None
    """
    Id of the user (contact) to update.
    """


    # @ApiMember(Description="Communication channel type: Marketing or Transactional.", IsRequired=true)
    comm_channel: Optional[str] = None
    """
    Communication channel type: Marketing or Transactional.
    """


    # @ApiMember(Description="Delivery channel: Email, Sms, or Push.", IsRequired=true)
    channel: Optional[str] = None
    """
    Delivery channel: Email, Sms, or Push.
    """


    # @ApiMember(Description="The tag name; must already exist for the communication channel.", IsRequired=true)
    tag: Optional[str] = None
    """
    The tag name; must already exist for the communication channel.
    """


    # @ApiMember(Description="True to subscribe (unblock) the tag, false to block it.")
    subscribed: bool = False
    """
    True to subscribe (unblock) the tag, false to block it.
    """


# @Route("/{version}/membership/auth/unblock", "PATCH")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnblockUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Id of the user to unblock, from get_users.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the user to unblock, from get_users.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


# @Route("/{version}/membership/users/{contactId}/marketing-state/{channel}/unsubscribe", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnsubscribeContactRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Id of the user (contact) to unsubscribe.", IsRequired=true)
    contact_id: Optional[str] = None
    """
    Id of the user (contact) to unsubscribe.
    """


    # @ApiMember(Description="Delivery channel to unsubscribe from: Email, Sms, or Push.", IsRequired=true)
    channel: Optional[str] = None
    """
    Delivery channel to unsubscribe from: Email, Sms, or Push.
    """


    # @ApiMember(Description="Optional suppression reason name explaining why consent was revoked.")
    reason: Optional[str] = None
    """
    Optional suppression reason name explaining why consent was revoked.
    """


# @Route("/{version}/membership/auth", "PUT")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateUserRequest(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Id of the user to update, from get_users.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the user to update, from get_users.
    """


# @Route("/{version}/membership/auth/{id}/preferences", "PUT")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateUserPreferencesRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    # @ApiMember(Description="Id of the user to update, from get_users.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the user to update, from get_users.
    """


    # @ApiMember(Description="When true, blocks all marketing messages to this user.")
    block_all_marketing_messages: bool = False
    """
    When true, blocks all marketing messages to this user.
    """


    # @ApiMember(Description="Per communication channel, the set of tags blocked for this user. Full replacement.")
    blocked_tags: Optional[Dict[str, HashSet[str]]] = None
    """
    Per communication channel, the set of tags blocked for this user. Full replacement.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the project's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the project's default integration.
    """


# @Route("/{version}/membership/userauth/password/change", "POST")
# @Api(Description="Membership · Password")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChangePasswordRequest(CodeMashRequestBase, IReturn[PasskeyOkResponse]):
    """
    Membership · Password
    """

    # @ApiMember(Description="The member's current password.", IsRequired=true)
    current_password: Optional[str] = None
    """
    The member's current password.
    """


    # @ApiMember(Description="The new password. Validated against the project's complexity policy.", IsRequired=true)
    new_password: Optional[str] = None
    """
    The new password. Validated against the project's complexity policy.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


# @Route("/{version}/membership/userauth/password/reset/request", "POST")
# @Api(Description="Membership · Password")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestPasswordResetRequest(CodeMashRequestBase, IReturn[PasskeyOkResponse]):
    """
    Membership · Password
    """

    # @ApiMember(Description="Email address to send the reset link to.", IsRequired=true)
    email: Optional[str] = None
    """
    Email address to send the reset link to.
    """


# @Route("/{version}/membership/userauth/password/reset/confirm", "POST")
# @Api(Description="Membership · Password")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmPasswordResetRequest(CodeMashRequestBase, IReturn[PasskeyOkResponse]):
    """
    Membership · Password
    """

    # @ApiMember(Description="One-time reset token from the email link.", IsRequired=true)
    token: Optional[str] = None
    """
    One-time reset token from the email link.
    """


    # @ApiMember(Description="The new password. Validated against the project's complexity policy.", IsRequired=true)
    new_password: Optional[str] = None
    """
    The new password. Validated against the project's complexity policy.
    """


    # @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
    database_integration_id: Optional[str] = None
    """
    Database integration id. Optional — defaults to the request environment's default integration.
    """


# @Route("/{version}/membership/userauth/passkey/authentication-options", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyAuthenticationOptionsRequest(CodeMashRequestBase, IReturn[PasskeyCeremonyOptionsResponse], IPasskeyCeremonyRequest):
    """
    Membership · Passkey
    """

    email: Optional[str] = None


# @Route("/{version}/membership/userauth/passkey/verify-authentication", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class VerifyPasskeyAuthenticationRequest(CodeMashRequestBase, IReturn[PasskeyAuthTokensResponse], IPasskeyCeremonyRequest):
    """
    Membership · Passkey
    """

    ceremony_id: Optional[str] = None
    assertion_response: Optional[str] = None


# @Route("/{version}/membership/userauth/passkeys", "GET")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListPasskeysRequest(CodeMashRequestBase, IReturn[PasskeyListResponse]):
    """
    Membership · Passkey
    """

    pass


# @Route("/{version}/membership/userauth/passkeys/{CredentialId}/rename", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RenamePasskeyRequest(CodeMashRequestBase, IReturn[PasskeyOkResponse]):
    """
    Membership · Passkey
    """

    # @ApiMember(Description="Base64 credential id of the passkey to rename, from list_passkeys.", IsRequired=true)
    credential_id: Optional[str] = None
    """
    Base64 credential id of the passkey to rename, from list_passkeys.
    """


    # @ApiMember(Description="The new friendly name for the passkey.", IsRequired=true)
    friendly_name: Optional[str] = None
    """
    The new friendly name for the passkey.
    """


# @Route("/{version}/membership/userauth/passkeys/{CredentialId}/revoke", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RevokePasskeyRequest(CodeMashRequestBase, IReturn[PasskeyOkResponse]):
    """
    Membership · Passkey
    """

    # @ApiMember(Description="Base64 credential id of the passkey to revoke, from list_passkeys.", IsRequired=true)
    credential_id: Optional[str] = None
    """
    Base64 credential id of the passkey to revoke, from list_passkeys.
    """


# @Route("/{version}/membership/userauth/recovery/use-code", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UseRecoveryCodeRequest(CodeMashRequestBase, IReturn[PasskeyRecoveryResponse]):
    """
    Membership · Passkey
    """

    email: Optional[str] = None
    recovery_code: Optional[str] = None


# @Route("/{version}/membership/userauth/recovery/magic-link/request", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestMagicLinkRequest(CodeMashRequestBase, IReturn[PasskeyOkResponse]):
    """
    Membership · Passkey
    """

    email: Optional[str] = None


# @Route("/{version}/membership/userauth/recovery/magic-link/consume", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConsumeMagicLinkRequest(CodeMashRequestBase, IReturn[PasskeyRecoveryResponse]):
    """
    Membership · Passkey
    """

    token: Optional[str] = None


# @Route("/{version}/membership/userauth/has-passkey", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HasPasskeyRequest(CodeMashRequestBase, IReturn[PasskeyOkResponse]):
    """
    Membership · Passkey
    """

    email: Optional[str] = None


# @Route("/{version}/membership/userauth/email/start-verification", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StartEmailVerificationRequest(CodeMashRequestBase, IReturn[PasskeyOkResponse]):
    """
    Membership · Passkey
    """

    email: Optional[str] = None


# @Route("/{version}/membership/userauth/email/confirm-verification", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmEmailVerificationRequest(CodeMashRequestBase, IReturn[PasskeyVerificationTokenResponse]):
    """
    Membership · Passkey
    """

    email: Optional[str] = None
    code: Optional[str] = None


# @Route("/{version}/membership/userauth/passkey/registration-options", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyRegistrationOptionsRequest(CodeMashRequestBase, IReturn[PasskeyCeremonyOptionsResponse], IPasskeyCeremonyRequest):
    """
    Membership · Passkey
    """

    verification_token: Optional[str] = None


# @Route("/{version}/membership/userauth/passkey/verify-registration", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class VerifyPasskeyRegistrationRequest(CodeMashRequestBase, IReturn[PasskeyAuthTokensResponse], IPasskeyCeremonyRequest):
    """
    Membership · Passkey
    """

    verification_token: Optional[str] = None
    ceremony_id: Optional[str] = None
    attestation_response: Optional[str] = None
    friendly_name: Optional[str] = None


# @Route("/{version}/membership/userauth/token/refresh", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RefreshPasskeyTokenRequest(CodeMashRequestBase, IReturn[PasskeyAuthTokensResponse]):
    """
    Membership · Passkey
    """

    refresh_token: Optional[str] = None


# @Route("/{version}/membership/userauth/logout", "POST")
# @Api(Description="Membership · Passkey")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasskeyLogoutRequest(CodeMashRequestBase, IReturn[PasskeyOkResponse]):
    """
    Membership · Passkey
    """

    refresh_token: Optional[str] = None


# @Route("/{version}/database/taxonomies/{taxonomyName}/merged-tree", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindMergedTermTreeRequest(CodeMashRequestBase, IReturn[FindMergedTermTreeResponse]):
    """
    Database
    """

    taxonomy_name: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/database/taxonomies/tree", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTaxonomyTreeRequest(CodeMashRequestBase, IReturn[FindTaxonomyTreeResponse]):
    """
    Database
    """

    include_terms: bool = False
    database_integration_id: Optional[str] = None


# @Route("/{version}/database/taxonomies/{taxonomyName}/terms", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTermsRequest(CodeMashListPaginationRequestBase, IReturn[FindTermsResponse]):
    """
    Database
    """

    taxonomy_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    filter: Optional[str] = None
    sort_descending: bool = False
    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTermsChildrenRequest(CodeMashListPaginationRequestBase, IReturn[FindTermsChildrenResponse]):
    """
    Database
    """

    taxonomy_name: Optional[str] = None
    parent_id: Optional[str] = None
    database_integration_id: Optional[str] = None
    filter: Optional[str] = None
    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/taxonomies/{taxonomyName}/terms/tree", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindTermTreeRequest(CodeMashRequestBase, IReturn[FindTermTreeResponse]):
    """
    Database
    """

    taxonomy_name: Optional[str] = None
    root_term_id: Optional[str] = None
    depth: Optional[int] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/database/schemas/{id}", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaRequest(CodeMashRequestBase, IReturn[GetDatabaseSchemaResponse]):
    """
    Database
    """

    id: Optional[str] = None


# @Route("/{version}/database/schemas", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemasRequest(CodeMashListPaginationRequestBase, IReturn[GetDatabaseSchemasResponse]):
    """
    Database
    """

    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/collections/{collectionName}/aggregate", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AggregateRequest(CodeMashRequestBase, IReturn[AggregateResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    pipeline: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}/{id}/responsibility", "PUT")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChangeResponsibilityRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    id: Optional[str] = None
    database_integration_id: Optional[str] = None
    new_responsible_user_id: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}/count", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CountRequest(CodeMashRequestBase, IReturn[CountResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    filter: Optional[str] = None
    schema_version: Optional[int] = None


# @Route("/{version}/database/collections/{collectionName}/many", "DELETE")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteManyRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    filter: Optional[str] = None
    all_records: Optional[bool] = None


# @Route("/{version}/database/collections/{collectionName}/{id}", "DELETE")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteOneRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}/distinct", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DistinctRequest(CodeMashRequestBase, IReturn[DistinctResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    field: Optional[str] = None
    filter: Optional[str] = None
    schema_version: Optional[int] = None


# @Route("/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ExecuteAggregateRequest(CodeMashRequestBase, IReturn[ExecuteAggregateResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    aggregate_id: Optional[str] = None
    database_integration_id: Optional[str] = None
    tokens: Optional[Dict[str, str]] = None


# @Route("/{version}/database/collections/{collectionName}", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindRequest(CodeMashListPaginationRequestBase, IReturn[FindResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    filter: Optional[str] = None
    schema_version: Optional[int] = None
    paging_args: Optional[PagingArgs] = None
    sort_by: Optional[str] = None
    sort_order: Optional[int] = None
    expand_references: bool = False


# @Route("/{version}/database/collections/{collectionName}/{id}", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindOneRequest(CodeMashRequestBase, IReturn[FindOneResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    id: Optional[str] = None
    database_integration_id: Optional[str] = None
    expand_references: bool = False


# @Route("/{version}/database/collections/{collectionName}/own", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindOwnRequest(CodeMashListPaginationRequestBase, IReturn[FindResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    filter: Optional[str] = None
    schema_version: Optional[int] = None
    paging_args: Optional[PagingArgs] = None
    # @ApiMember(Description="Set true to get every reference value as { id, display } (display = the target's displayField per the schema; null when the target is gone). Needs read permission on every source the schema links to (users, roles, taxonomy, collection, files) — otherwise the read is refused with CM-ERRORS-DATABASE-056 naming the source. Default false returns the stored ids.")
    expand_references: bool = False
    """
    Set true to get every reference value as { id, display } (display = the target's displayField per the schema; null when the target is gone). Needs read permission on every source the schema links to (users, roles, taxonomy, collection, files) — otherwise the read is refused with CM-ERRORS-DATABASE-056 naming the source. Default false returns the stored ids.
    """


# @Route("/{version}/database/collections/{collectionName}/many", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InsertManyRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    documents: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InsertOneRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    document: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}/{id}/replace", "PUT")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReplaceOneRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    id: Optional[str] = None
    database_integration_id: Optional[str] = None
    replacement: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}/many", "PUT")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateManyRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    database_integration_id: Optional[str] = None
    filter: Optional[str] = None
    all_records: Optional[bool] = None
    update: Optional[str] = None
    array_filters: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}/{id}", "PUT")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOneRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    collection_name: Optional[str] = None
    id: Optional[str] = None
    database_integration_id: Optional[str] = None
    update: Optional[str] = None
    array_filters: Optional[str] = None


# @Route("/{version}/files/{filesIntegrationId}/commit", "POST")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CommitUploadRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    path: Optional[str] = None
    content_type: Optional[str] = None
    size_bytes: Optional[int] = None
    file_name: Optional[str] = None


# @Route("/{version}/files/{filesIntegrationId}/content", "GET")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFileContentRequest(RequestBase, IReturn[bytes]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    path: Optional[str] = None
    token: Optional[str] = None


# @Route("/{version}/files/{filesIntegrationId}/content", "PUT")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PutFileContentRequest(RequestBase, IReturn[EmptyResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    path: Optional[str] = None
    token: Optional[str] = None


# @Route("/{version}/files/{filesIntegrationId}", "DELETE")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteFileApiRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    path: Optional[str] = None


# @Route("/{version}/files/{filesIntegrationId}/bulk", "DELETE")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteManyFilesApiRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    paths: List[str] = field(default_factory=list)


# @Route("/{version}/files/{filesIntegrationId}/download", "GET")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DownloadFileApiRequest(CodeMashRequestBase, IReturn[bytes]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    path: Optional[str] = None


# @Route("/{version}/files/{filesIntegrationId}/by-id/{id}", "GET")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFileByIdRequest(CodeMashRequestBase, IReturn[GetFileByIdResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    id: Optional[str] = None


# @Route("/{version}/files/{filesIntegrationId}/info", "GET")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFileInfoRequest(CodeMashRequestBase, IReturn[GetFileInfoResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    path: Optional[str] = None


# @Route("/{version}/files/{filesIntegrationId}/sign", "GET")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSignedUrlRequest(CodeMashRequestBase, IReturn[GetSignedUrlResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    path: Optional[str] = None
    expiration_seconds: Optional[int] = None


# @Route("/{version}/files/{filesIntegrationId}", "GET")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListFilesRequest(CodeMashListPaginationRequestBase, IReturn[ListFilesResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    path: Optional[str] = None


# @Route("/{version}/files/public/{PublicId}/{Name*}", "GET")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPublicFileRequest(RequestBase, IReturn[bytes]):
    """
    Files
    """

    public_id: Optional[str] = None
    name: Optional[str] = None


# @Route("/{version}/files/{filesIntegrationId}/upload-url", "POST")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestUploadUrlRequest(CodeMashRequestBase, IReturn[RequestUploadUrlResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None
    path: Optional[str] = None
    content_type: Optional[str] = None
    expiration_seconds: Optional[int] = None


# @Route("/{version}/files/{filesIntegrationId}/test", "POST")
# @Api(Description="Files")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestFilesIntegrationRequest(CodeMashRequestBase, IReturn[TestFilesIntegrationResponse]):
    """
    Files
    """

    files_integration_id: Optional[str] = None

