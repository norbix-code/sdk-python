""" Options:
Date: 2026-09-04 14:55:41
Version: 10.08
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
class ProjectId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegrationId(AggregateId, IHasDomainEntityId):
    pass


class ResourceRefKind(str, Enum):
    CONTACT = 'Contact'
    DOCUMENT = 'Document'
    FILE = 'File'
    PAYMENT_CUSTOMER = 'PaymentCustomer'
    ORDER = 'Order'
    PAYMENT = 'Payment'
    PRODUCT = 'Product'
    INTEGRATION = 'Integration'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResourceRef:
    project_id: Optional[ProjectId] = None
    integration_id: Optional[IntegrationId] = None
    kind: Optional[ResourceRefKind] = None


class ResourceSource(str, Enum):
    NORBIX = 'Norbix'
    STRIPE = 'Stripe'
    SHOPIFY = 'Shopify'
    PAY_PAL = 'PayPal'
    ADYEN = 'Adyen'
    MOLLIE = 'Mollie'
    PADDLE = 'Paddle'
    LEMON_SQUEEZY = 'LemonSqueezy'
    APPLE_IN_APP = 'AppleInApp'
    GOOGLE_IN_APP = 'GoogleInApp'
    AUTHORIZE_NET = 'AuthorizeNet'
    BRAINTREE = 'Braintree'
    CHECK_OUT_COM = 'CheckOutCom'
    WOO_COMMERCE = 'WooCommerce'
    MAGENTO = 'Magento'
    WORLDPAY = 'Worldpay'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentCustomerRef(ResourceRef):
    kind: Optional[ResourceRefKind] = None
    source: Optional[ResourceSource] = None
    external_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Quantity:
    value: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashManagedServiceSubscription:
    subscription_id: Optional[CodeMashSubscriptionId] = None
    payment_customer_ref: Optional[PaymentCustomerRef] = None
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
class ProjectName:
    name: Optional[str] = None
    unique_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NorbixRegion:
    code: Optional[str] = None


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
    region: Optional[NorbixRegion] = None
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
class FileResourceRef:
    resource: Optional[FileResource] = None
    integration_id: Optional[IntegrationId] = None
    provider: Optional[FileProvider] = None
    path: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectLogo:
    file_resource: Optional[FileResourceRef] = None
    public_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectIcon:
    file_resource: Optional[FileResourceRef] = None
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
class AuthId(IHasDomainEntityId):
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
class Env:
    value: Optional[str] = None
    is_prod: bool = False


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


    resolved_env: Optional[Env] = None
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


    # @ApiMember(DataType="object", Description="Paging", Name="paging", ParameterType="body")
    paging: Optional[PagingArgs] = None
    """
    Paging
    """


class IPasskeyCeremonyRequest:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Integration(IIntegrationIdentification, IHasDomainEntityId):
    integration_id: Optional[IntegrationId] = None
    env: Optional[Env] = None
    capability: Optional[str] = None
    is_system_owned: bool = False
    integration_name: Optional[DisplayName] = None
    is_enabled: bool = False
    is_configured: bool = False
    last_integration_test_at_utc: Optional[datetime.datetime] = None
    last_integration_test_succeeded: Optional[bool] = None
    last_integration_test_error_messages: Optional[IReadOnlyList[str]] = None
    human_delivery_confirmed_at_utc: Optional[datetime.datetime] = None
    is_approved_that_it_works: bool = False


class PushProvider(str, Enum):
    APPLE_APNS = 'AppleApns'
    SAFARI_WEB = 'SafariWeb'
    SAFARI_PUSH = 'SafariPush'
    ANDROID_FIREBASE = 'AndroidFirebase'
    CHROME_WEB = 'ChromeWeb'
    FIREFOX_WEB = 'FirefoxWeb'
    EDGE_WEB = 'EdgeWeb'
    CHROME_PUSH = 'ChromePush'
    CODE_MASH_IOS_APP = 'CodeMashIosApp'
    CODE_MASH_ANDROID_APP = 'CodeMashAndroidApp'
    CODE_MASH_SAFARI_PLUGIN = 'CodeMashSafariPlugin'
    CODE_MASH_SAFARI_WEB = 'CodeMashSafariWeb'
    CODE_MASH_CHROME_PLUGIN = 'CodeMashChromePlugin'
    CODE_MASH_CHROME_WEB = 'CodeMashChromeWeb'
    EXPO = 'Expo'
    FAKE = 'Fake'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegration(Integration):
    provider: Optional[PushProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TemplateId:
    value: Optional[str] = None


TMessageContent = TypeVar('TMessageContent')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Template(Generic[TMessageContent], IBindableContract):
    template_id: Optional[TemplateId] = None
    template_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[TMessageContent]] = field(default_factory=list)
    communication_channel: Optional[CommunicationChannel] = None
    is_active: bool = False
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    file_integration_id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TemplateCode:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTitle:
    value: Optional[TemplateCode] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushBody:
    value: Optional[TemplateCode] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushMessageContent:
    title: Optional[PushTitle] = None
    sub_title: Optional[PushTitle] = None
    body: Optional[PushBody] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplate(Template[PushMessageContent]):
    pass


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
    description: Optional[str] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileResourceRefDto:
    resource: Optional[FileResourceDto] = None
    integration_id: Optional[str] = None
    provider: Optional[FileProvider] = None
    path: Optional[str] = None


class IHasDomainEntityId:
    view_id: Optional[str] = None


class IIntegrationIdentification:
    integration_id: Optional[IntegrationId] = None
    capability: Optional[str] = None
    is_system_owned: bool = False


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicProjectConfigDto:
    display_name: Optional[str] = None
    admin_portal_enabled: bool = False
    branding: Optional[PublicBrandDto] = None
    auth: Optional[PublicAuthDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublicLegalDocumentDto:
    kind: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    available: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AskChatResponse(ResponseBase):
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
class PasskeyOkResponse(ResponseBase):
    pass


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestUploadUrlResponse(ResponseBase):
    url: Optional[str] = None


# @Route("/{version}/echo", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Echo(RequestBase, IReturn[EchoResponse]):
    pass


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
    payment_customer_ref: Optional[PaymentCustomerRef] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SubscriptionChanged:
    subscription: Optional[CodeMashManagedServiceSubscription] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SubscriptionCanceled:
    payment_customer_ref: Optional[PaymentCustomerRef] = None
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
    primary_region: Optional[ProjectRegion] = None
    additional_regions: Optional[List[ProjectRegion]] = None
    description: Optional[str] = None
    is_provisioning: bool = False


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
    primary_region: Optional[ProjectRegion] = None
    additional_regions: Optional[List[ProjectRegion]] = None


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
    auth_id: Optional[AuthId] = None
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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationSaved:
    integration: Optional[PushIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationSetAsDefault:
    env: Optional[Env] = None
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushServiceEstablished:
    default_templates: Optional[List[PushTemplate]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushServiceEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushServiceDisabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateCreated:
    template_id: Optional[TemplateId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[PushMessageContent]] = field(default_factory=list)
    channel: Optional[CommunicationChannel] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateUpdated:
    template_id: Optional[TemplateId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[PushMessageContent]] = field(default_factory=list)
    channel: Optional[CommunicationChannel] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateDeleted:
    template_id: Optional[TemplateId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateArchived:
    template_id: Optional[TemplateId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateUnArchived:
    template_id: Optional[TemplateId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateMirrored:
    template: Optional[PushTemplate] = None

