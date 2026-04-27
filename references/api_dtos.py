""" Options:
Date: 2026-04-27 20:17:54
Version: 10.06
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
class EmailAddress:
    address: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisplayName:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AggregateId:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UtcDateTime:
    pass


class TimeUnit(str, Enum):
    TICKS = 'Ticks'
    MILLISECONDS = 'Milliseconds'
    SECONDS = 'Seconds'
    MINUTES = 'Minutes'
    HOURS = 'Hours'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ExpirationToken:
    items: int = 0
    unit: Optional[TimeUnit] = None
    value: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashSubscriptionId(AggregateId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ExternalCustomerId:
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Quantity:
    value: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashManagedServiceSubscription:
    subscription_id: Optional[CodeMashSubscriptionId] = None
    ref_customer_id: Optional[ExternalCustomerId] = None
    ref_subscription_id: Optional[str] = None
    issued_on: Optional[UtcDateTime] = None
    will_expire_on: Optional[UtcDateTime] = None
    project_cap: Optional[Quantity] = None
    is_trial: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DomainUrl:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashLicense(CodeMashManagedServiceSubscription):
    domain: Optional[DomainUrl] = None
    account_id: Optional[AccountId] = None
    is_enterprise: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Tag:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagDescription:
    display_name: Optional[DisplayName] = None
    description: Optional[str] = None


TContent = TypeVar('TContent')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MessageTranslation(Generic[TContent]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagTranslation(MessageTranslation[TagDescription]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BaseTagDefinition:
    tag: Optional[Tag] = None
    translations: List[TagTranslation] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GroupDefinition(BaseTagDefinition):
    pass


class CommunicationChannel(str, Enum):
    TRANSACTIONAL = 'Transactional'
    MARKETING = 'Marketing'
    SYSTEM = 'System'


class DeliveryChannel(str, Enum):
    EMAIL = 'Email'
    PUSH = 'Push'
    SMS = 'Sms'
    WEB_PUSH = 'WebPush'
    IN_APP = 'InApp'
    CHAT_BOT = 'ChatBot'
    CHAT_PLATFORM = 'ChatPlatform'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagDefinition(BaseTagDefinition):
    default_delivery: Dict[str, bool] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectName:
    name: Optional[str] = None
    unique_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegrationId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectRegionId:
    value: Optional[str] = None


class Continent(str, Enum):
    AFRICA = 'Africa'
    ANTARCTICA = 'Antarctica'
    ASIA = 'Asia'
    EUROPE = 'Europe'
    NORTH_AMERICA = 'NorthAmerica'
    OCEANIA = 'Oceania'
    SOUTH_AMERICA = 'SouthAmerica'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectRegion:
    id: Optional[ProjectRegionId] = None
    name: Optional[str] = None
    continent: Optional[Continent] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Language:
    code: Optional[str] = None
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileResourceId:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileChecksum:
    algorithm: Optional[str] = None
    hash: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileResource:
    id: Optional[FileResourceId] = None
    original_file_name: Optional[str] = None
    extension: Optional[str] = None
    size_bytes: Optional[int] = None
    checksum: Optional[FileChecksum] = None
    stored_file_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectLogo:
    file_resource: Optional[FileResource] = None
    public_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectIcon:
    file_resource: Optional[FileResource] = None
    public_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BrandColor:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TimeZone:
    zone_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GroupTags:
    group: Optional[Tag] = None
    tags: List[Tag] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunicationChannel:
    channel: Optional[CommunicationChannel] = None
    groups: List[GroupTags] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunication:
    channels: List[ProjectCommunicationChannel] = field(default_factory=list)
    groups: List[GroupDefinition] = field(default_factory=list)
    tags: List[TagDefinition] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserId(IHasDomainEntityId):
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeviceId:
    id: Optional[str] = None


class DeviceType(str, Enum):
    UNKNOWN = 'Unknown'
    PHONE = 'Phone'
    TABLET = 'Tablet'
    DESKTOP = 'Desktop'
    TV = 'Tv'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushDeviceToken:
    token: Optional[str] = None


class PushDeviceDeliveryFamily(str, Enum):
    IOS = 'Ios'
    ANDROID = 'Android'
    CHROME = 'Chrome'
    SAFARI = 'Safari'
    EXPO = 'Expo'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushDeviceDeliveryToken:
    push_device_token: Optional[PushDeviceToken] = None
    delivery_family: Optional[PushDeviceDeliveryFamily] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushDevice:
    id: Optional[DeviceId] = None
    brand: Optional[str] = None
    manufacturer: Optional[str] = None
    model_name: Optional[str] = None
    device_name: Optional[str] = None
    device_type: Optional[DeviceType] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None
    platform_api_level: Optional[int] = None
    token: Optional[PushDeviceDeliveryToken] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashRequestBase(RequestBase, IHasProjectId):
    # @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as norbix-project-id.", IsRequired=true, Name="norbix-project-id", ParameterType="header")
    project_id: Optional[str] = None
    """
    ID of your project. Can be passed in a header as norbix-project-id.
    """


class IHasProjectId:
    project_id: Optional[str] = None


class Gender(str, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


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
    blocked_tags: Optional[Dict[str, IReadOnlySet[str]]] = None
    extra_metadata: Optional[str] = None
    notes: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveUser(CodeMashRequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Database integration id", IsRequired=true)
    database_integration_id: Optional[str] = None
    """
    Database integration id
    """


    # @ApiMember(DataType="object", Description="User Info", Name="UserGeneralInfo", ParameterType="body")
    user_general_info: Optional[UserGeneralInfoDto] = None
    """
    User Info
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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashListPaginationRequestBase(RequestBase, IHasProjectId):
    # @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as norbix-project-id.", IsRequired=true, Name="norbix-project-id", ParameterType="header")
    project_id: Optional[str] = None
    """
    ID of your project. Can be passed in a header as norbix-project-id.
    """


    # @ApiMember(DataType="object", Description="Paging", IsRequired=true, Name="paging", ParameterType="body")
    paging: Optional[PagingArgs] = None
    """
    Paging
    """


class CodeMashRelease(str, Enum):
    NOT_SET = 'NotSet'
    COMMUNITY = 'Community'
    MANAGED_SERVICE = 'ManagedService'
    ENTERPRISE = 'Enterprise'


class CodeMashRuntime(str, Enum):
    DEVELOPMENT = 'Development'
    CI = 'CI'
    PRODUCTION = 'Production'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashLicenseFromEndpointDto:
    domain_from_license: Optional[str] = None
    account_id_from_license: Optional[str] = None
    ref_customer_id: Optional[str] = None
    ref_subscription_id: Optional[str] = None
    issued: int = 0
    expire: int = 0
    projects_cap_from_license: int = 0
    is_trial: bool = False
    code_mash_release: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ErrorDto:
    message: Optional[str] = None
    error_code: Optional[str] = None
    context: Optional[Dict[str, str]] = None
    stack_trace: Optional[IReadOnlySet[ErrorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashResponseStatus:
    is_success: bool = False
    errors: Optional[List[ErrorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResponseBase:
    response_status: Optional[CodeMashResponseStatus] = None


class UserType(str, Enum):
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


class UserStatus(IntEnum):
    REGISTERED = 0
    PENDING_VALIDATION = 2
    ACTIVE = 8
    UNREGISTERED = 16
    SUSPENDED = 32
    IN_ACTIVE = 64
    BLOCKED = 128


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserDto(IBindableContract):
    id: Optional[str] = None
    type: Optional[UserType] = None
    email: Optional[str] = None
    user_name: Optional[str] = None
    registration: Optional[RegistrationDto] = None
    login: Optional[LoginDto] = None
    general_info: Optional[UserGeneralInfoDto] = None
    roles: Optional[IReadOnlySet[str]] = None
    push_devices: Optional[IReadOnlySet[str]] = None
    tags: Optional[IReadOnlySet[str]] = None
    status: Optional[UserStatus] = None
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
    blocked_tags: Optional[Dict[str, IReadOnlySet[str]]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TermMultiParentDto:
    taxonomy_id: Optional[str] = None
    parent_id: Optional[str] = None
    name: Optional[str] = None
    names: Optional[Dict[str, str]] = None


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


class TriggerType(str, Enum):
    MEMBERSHIP = 'Membership'
    SCHEMA = 'Schema'
    FILES = 'Files'
    PAYMENTS = 'Payments'


class TriggerActionType(str, Enum):
    CODE = 'Code'
    PUSH = 'Push'
    SMS = 'Sms'
    EMAIL = 'Email'
    WEBHOOK_CALL = 'WebhookCall'


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


class IHasDomainEntityId:
    view_id: Optional[str] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DecimalFieldDto(JsonSchemaFieldDto):
    minimum: Optional[Decimal] = None
    maximum: Optional[Decimal] = None
    multiple_of: Optional[Decimal] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CurrencyFieldDto(JsonSchemaFieldDto):
    allowed_currencies: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BooleanFieldDto(JsonSchemaFieldDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DateFieldDto(JsonSchemaFieldDto):
    minimum: Optional[int] = None
    maximum: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegerFieldDto(JsonSchemaFieldDto):
    minimum: Optional[int] = None
    maximum: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GeolocationFieldDto(JsonSchemaFieldDto):
    allowed_types: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagsFieldDto(JsonSchemaFieldDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileFieldDto(JsonSchemaFieldDto):
    storages: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomySelectionFieldDto(JsonSchemaFieldDto):
    taxonomy_id: Optional[str] = None
    multiple: bool = False


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleSelectionFieldDto(JsonSchemaFieldDto):
    multiple: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnumSelectionFieldDto(JsonSchemaFieldDto):
    values: Optional[IReadOnlyList[str]] = None
    multiple: bool = False


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
    license: Optional[CodeMashLicenseFromEndpointDto] = None
    ask_for_enterprise_license_email: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AskChatResponse(ResponseBase):
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserResponse(ResponseBase):
    user: Optional[UserDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUsersResponse(ResponseBase):
    list: Optional[PaginatedResponse[UserDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserPreferencesResponse(ResponseBase):
    preferences: Optional[UserMarketingPreferencesDto] = None


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


# @Route("/{version}/echo", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Echo(RequestBase, IReturn[EchoResponse]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountCreated:
    email: Optional[EmailAddress] = None
    display_name: Optional[DisplayName] = None
    account_id: Optional[AccountId] = None
    created_on: Optional[UtcDateTime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountVerified:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountSetAsActive:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountValidationTokenIssued:
    expiration: Optional[ExpirationToken] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountBlocked:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountProfileUpdated:
    display_name: Optional[DisplayName] = None
    billing_email: Optional[EmailAddress] = None
    operations_email: Optional[EmailAddress] = None
    security_email: Optional[EmailAddress] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountSetAsInactive:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountUnregistered:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LicenseCreated:
    license: Optional[CodeMashLicense] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CustomerCreated:
    customer_id: Optional[ExternalCustomerId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SubscriptionChanged:
    subscription: Optional[CodeMashManagedServiceSubscription] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SubscriptionCanceled:
    customer_id: Optional[ExternalCustomerId] = None
    subscription_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunicationGroupSaved:
    group: Optional[GroupDefinition] = None
    channel: Optional[CommunicationChannel] = None
    origin_channel: Optional[CommunicationChannel] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunicationTagFromGroupDeleted:
    group_tag: Optional[Tag] = None
    removed_tag: Optional[Tag] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunicationGroupDeleted:
    group_tag: Optional[Tag] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunicationTagSaved:
    tag: Optional[TagDefinition] = None
    group_tag: Optional[Tag] = None
    channel: Optional[CommunicationChannel] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunicationTagDeleted:
    tag: Optional[Tag] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCreated:
    id: Optional[ProjectId] = None
    name: Optional[ProjectName] = None
    database_integration_id: Optional[IntegrationId] = None
    regions: Optional[List[ProjectRegion]] = None
    description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectDeleted:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectActivated:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectDisabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectNameChanged:
    project_name: Optional[ProjectName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectDescriptionChanged:
    description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectMarketingUrlChanged:
    url: Optional[DomainUrl] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectAllowedOriginsChanged:
    origins: Optional[List[DomainUrl]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectDefaultLanguageChanged:
    language: Optional[Language] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectLanguagesChanged:
    languages: List[Language] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectLogoChanged:
    logo: Optional[ProjectLogo] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectIconChanged:
    icon: Optional[ProjectIcon] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectMainColorChanged:
    color: Optional[BrandColor] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectAccentColorChanged:
    color: Optional[BrandColor] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectRegionsChanged:
    regions: Optional[List[ProjectRegion]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectTimeZoneChanged:
    time_zone: Optional[TimeZone] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectPaymentZonesChanged:
    payment_zones: Optional[List[TimeZone]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunicationSet:
    project_communication: Optional[ProjectCommunication] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountUserPushDeviceCreated:
    user_id: Optional[UserId] = None
    push_device: Optional[PushDevice] = None


# @Route("/{version}/chat/complete", "POST")
# @Api(Description="AI")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AskChatRequest(CodeMashRequestBase, IReturn[AskChatResponse]):
    """
    AI
    """

    prompt: Optional[str] = None


# @Route("/{version}/membership/users/block", "PATCH")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BlockUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/membership/users/register/service", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveSystemUserWithPermissions(SaveUserWithRolesBase, IReturn[IdResponse]):
    """
    Membership
    """

    pass


# @Route("/{version}/membership/users/register/guest", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveGuestUser(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    pass


# @Route("/{version}/membership/users/register/user-name", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveUserNameUser(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    password: Optional[str] = None
    user_name: Optional[str] = None


# @Route("/{version}/membership/users/register/email", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailUser(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    password: Optional[str] = None
    email: Optional[str] = None


# @Route("/{version}/membership/users/register/phone", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePhoneUser(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    phone: Optional[str] = None


# @Route("/{version}/membership/users/register/phone-with-permissions", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePhoneUserNameWithPermissions(SaveUserWithRolesBase, IReturn[IdResponse]):
    """
    Membership
    """

    phone: Optional[str] = None


# @Route("/{version}/membership/users/register/email-with-permissions", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailUserNameWithPermissions(SaveUserWithRolesBase, IReturn[IdResponse]):
    """
    Membership
    """

    password: Optional[str] = None
    email: Optional[str] = None


# @Route("/{version}/membership/users/register/user-name-with-permissions", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveUserNameWithPermissions(SaveUserWithRolesBase, IReturn[IdResponse]):
    """
    Membership
    """

    password: Optional[str] = None
    user_name: Optional[str] = None


# @Route("/{version}/membership/users", "DELETE")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/membership/users/{id}", "GET")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserRequest(CodeMashRequestBase, IReturn[GetUserResponse]):
    """
    Membership
    """

    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/membership/users", "GET")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUsersRequest(CodeMashListPaginationRequestBase, IReturn[GetUsersResponse]):
    """
    Membership
    """

    database_integration_id: Optional[str] = None
    include_permissions: bool = False
    user_should_have_push_device: bool = False
    user_should_have_email: bool = False
    include_meta: bool = False
    role_names: Optional[List[str]] = None
    user_ids: Optional[List[str]] = None


# @Route("/{version}/membership/users/{id}/preferences", "GET")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserPreferencesRequest(CodeMashRequestBase, IReturn[GetUserPreferencesResponse]):
    """
    Membership
    """

    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/membership/users/invite", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InviteUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    email: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/membership/users/assign-roles", "PUT")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssignRolePermissionsRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    id: Optional[str] = None
    # @ApiMember(Description="Database integration id", IsRequired=true)
    database_integration_id: Optional[str] = None
    """
    Database integration id
    """


    roles: Optional[List[str]] = None


# @Route("/{version}/membership/users/unblock", "PATCH")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnblockUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/membership/users", "PUT")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateUserRequest(SaveUser, IReturn[IdResponse]):
    """
    Membership
    """

    id: Optional[str] = None


# @Route("/{version}/membership/users/{id}/preferences", "PUT")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateUserPreferencesRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    id: Optional[str] = None
    block_all_marketing_messages: bool = False
    blocked_tags: Optional[Dict[str, IReadOnlySet[str]]] = None
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
    update: Optional[str] = None


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

