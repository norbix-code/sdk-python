""" Options:
Date: 2026-04-27 20:17:55
Version: 10.06
Tip: To override a DTO option, remove "#" prefix before updating
BaseUrl: http://localhost:5001

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


class EmailProvider(str, Enum):
    SMTP = 'Smtp'
    SEND_GRID = 'SendGrid'
    MAIL_GUN = 'MailGun'
    AWS_SES = 'AwsSes'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[EmailProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False
    email_address: Optional[str] = None
    email_sender_name: Optional[str] = None


class SmtpPorts(IntEnum):
    DEFAULT = 25
    SSL = 465
    TLS = 587
    FALLBACK = 2525


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmtpEmailIntegrationRequest(EmailIntegrationRequest):
    domain: Optional[str] = None
    port: Optional[SmtpPorts] = None
    user_name: Optional[str] = None
    password: Optional[str] = None


class AwsIntegrationType(str, Enum):
    IAM = 'Iam'
    CROSS_ACCOUNT_ROLE = 'CrossAccountRole'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsSesEmailIntegrationRequest(EmailIntegrationRequest):
    integration_type: Optional[AwsIntegrationType] = None
    aws_region: Optional[str] = None
    email_identity_arn: Optional[str] = None
    configuration_set: Optional[str] = None
    role_arn: Optional[str] = None
    external_id: Optional[str] = None
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendGridEmailIntegrationRequest(EmailIntegrationRequest):
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MailGunEmailIntegrationRequest(EmailIntegrationRequest):
    domain: Optional[str] = None
    api_key: Optional[str] = None
    webhook_signing_key: Optional[str] = None


class EmailCampaignRecipientsSourceTypes(str, Enum):
    ALL_USERS = 'AllUsers'
    SPECIFIED_USERS = 'SpecifiedUsers'
    ACCOUNT_USERS = 'AccountUsers'
    EMAIL = 'Email'
    COLLECTION = 'Collection'


class TokenMappingResolverType(str, Enum):
    NOT_SET = 'NotSet'
    CUSTOM = 'Custom'
    PROJECT = 'Project'
    PROJECT_SOCIALS = 'ProjectSocials'
    INITIATOR = 'Initiator'
    RECIPIENT = 'Recipient'
    SCHEMA_RECORD = 'SchemaRecord'
    TARGET_USER = 'TargetUser'
    TAG_DEFINITIONS = 'TagDefinitions'
    EMAIL_SIGNATURES = 'EmailSignatures'
    CAMPAIGN = 'Campaign'
    TEMPLATE = 'Template'
    EMAIL_FOOTERS = 'EmailFooters'
    OLD = 'Old'
    NEW = 'New'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TokenMappingDto:
    key: Optional[str] = None
    value: Optional[str] = None
    resolver: Optional[TokenMappingResolverType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignRequest:
    source: Optional[EmailCampaignRecipientsSourceTypes] = None
    template_id: Optional[str] = None
    integration_id: Optional[str] = None
    language: Optional[str] = None
    initiator_id: Optional[str] = None
    notes: Optional[str] = None
    mapped_tokens: Optional[List[TokenMappingDto]] = None
    campaign_time: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToAllUsersDeliverySettingsRequest(EmailCampaignRequest):
    roles_names: Optional[List[str]] = None
    user_tags: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToAccountUsersDeliverySettingsRequest(EmailCampaignRequest):
    user_recipients: List[str] = field(default_factory=list)
    user_cc: Optional[List[str]] = None
    user_bcc: Optional[List[str]] = None
    single_email_strategy: bool = False


class CollectionEmailCampaignRecipientField(str, Enum):
    USER = 'User'
    EMAIL = 'Email'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToCollectionRecordsDeliverySettingsRequest(EmailCampaignRequest):
    fields: List[str] = field(default_factory=list)
    schema_name: Optional[str] = None
    field_type: Optional[CollectionEmailCampaignRecipientField] = None
    role_names: Optional[List[str]] = None
    languages: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToEmailsDeliverySettingsRequest(EmailCampaignRequest):
    recipients: List[str] = field(default_factory=list)
    recipients_cc: Optional[List[str]] = None
    recipients_bcc: Optional[List[str]] = None
    single_email_strategy: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToUsersDeliverySettingsRequest(EmailCampaignRequest):
    user_recipients: List[str] = field(default_factory=list)
    user_cc: Optional[List[str]] = None
    user_bcc: Optional[List[str]] = None
    single_email_strategy: bool = False


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
class SaveTriggerRequest:
    type: Optional[TriggerType] = None
    trigger_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    is_enabled: bool = False
    pre_execute_code: Optional[str] = None
    action: Optional[TriggerActionDto] = None


class MembershipTriggerType(str, Enum):
    ON_REGISTERED = 'OnRegistered'
    ON_INVITED = 'OnInvited'
    ON_VERIFIED = 'OnVerified'
    ON_UPDATED = 'OnUpdated'
    ON_DELETED = 'OnDeleted'
    ON_BLOCKED = 'OnBlocked'
    ON_REACTIVATED = 'OnReactivated'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerRequest(SaveTriggerRequest):
    when: Optional[MembershipTriggerType] = None


class SchemaTriggerType(str, Enum):
    ON_INSERTED = 'OnInserted'
    ON_DELETED = 'OnDeleted'
    ON_UPDATED = 'OnUpdated'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerRequest(SaveTriggerRequest):
    schema_id: Optional[str] = None
    when: Optional[SchemaTriggerType] = None
    configuration_code: Optional[str] = None


class FilesTriggerType(str, Enum):
    ON_FILE_UPLOADED = 'OnFileUploaded'
    ON_FILE_DELETED = 'OnFileDeleted'


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesTriggerRequest(SaveTriggerRequest):
    when: Optional[FilesTriggerType] = None
    file_ref: Optional[FileResourceRefDto] = None


class PaymentTriggerType(str, Enum):
    ON_ORDER_CREATED = 'OnOrderCreated'
    ON_ORDER_PAID = 'OnOrderPaid'
    ON_WEBHOOK_CALL_RECEIVED = 'OnWebhookCallReceived'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentTriggerRequest(SaveTriggerRequest):
    when: Optional[PaymentTriggerType] = None


class DatabaseProvider(str, Enum):
    CODE_MASH_MONGO_DB_ATLAS_CLUSTER = 'CodeMashMongoDbAtlasCluster'
    CODE_MASH_MONGO_DB_ATLAS_SERVERLESS = 'CodeMashMongoDbAtlasServerless'
    MONGO_DB_CONNECTION_STRING = 'MongoDbConnectionString'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[DatabaseProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAtlasServerlessDatabaseIntegrationRequest(DatabaseIntegrationRequest):
    database_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAtlasClusterDatabaseIntegrationRequest(DatabaseIntegrationRequest):
    database_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbConnectionStringDatabaseIntegrationRequest(DatabaseIntegrationRequest):
    database_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[FileProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleDriveFilesIntegrationRequest(FilesIntegrationRequest):
    root_folder_id: Optional[str] = None
    service_account_json_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FtpFilesIntegrationRequest(FilesIntegrationRequest):
    host: Optional[str] = None
    port: int = 0
    root_path: Optional[str] = None
    use_ssl: bool = False
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DropBoxFilesIntegrationRequest(FilesIntegrationRequest):
    root_path: Optional[str] = None
    access_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleICloudFilesIntegrationRequest(FilesIntegrationRequest):
    container_identifier: Optional[str] = None
    relative_path: Optional[str] = None
    key_id: Optional[str] = None
    team_id: Optional[str] = None
    bundle_id: Optional[str] = None
    p8_private_key: Optional[str] = None


class AwsS3IntegrationType(str, Enum):
    IAM = 'Iam'
    CROSS_ACCOUNT_ROLE = 'CrossAccountRole'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsS3FilesIntegrationRequest(FilesIntegrationRequest):
    integration_type: Optional[AwsS3IntegrationType] = None
    bucket_name: Optional[str] = None
    region: Optional[str] = None
    role_arn: Optional[str] = None
    external_id: Optional[str] = None
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleCloudFilesIntegrationRequest(FilesIntegrationRequest):
    bucket_name: Optional[str] = None
    service_account_json_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AzureBlobFilesIntegrationRequest(FilesIntegrationRequest):
    blob_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LocalFilesIntegrationRequest(FilesIntegrationRequest):
    root_path: Optional[str] = None


class LoggingProvider(str, Enum):
    CONSOLE = 'Console'
    DATA_DOG = 'DataDog'
    KAFKA = 'Kafka'
    ZABBIX = 'Zabbix'
    MICROSOFT_TEAMS = 'MicrosoftTeams'
    SLACK = 'Slack'
    TELEGRAM = 'Telegram'
    AMQP = 'AMQP'
    NEW_RELIC = 'NewRelic'
    PROMETHEUS = 'Prometheus'
    AZURE_O_TEL = 'AzureOTel'
    SPLUNK = 'Splunk'
    ELASTIC_SEARCH = 'ElasticSearch'
    KIBANA = 'Kibana'
    LOCAL_FILE = 'LocalFile'
    AWSS3 = 'AWSS3'
    AWS_KINESIS = 'AWSKinesis'
    MONGO_D_B = 'MongoDB'
    INTERNAL_KAFKA = 'InternalKafka'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[LoggingProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AmqpLoggingIntegrationRequest(LoggingIntegrationRequest):
    host: Optional[str] = None
    port: int = 0
    virtual_host: Optional[str] = None
    exchange: Optional[str] = None
    routing_key: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsKinesisLoggingIntegrationRequest(LoggingIntegrationRequest):
    stream_name: Optional[str] = None
    region: Optional[str] = None
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


class AwsS3LoggingIntegrationType(str, Enum):
    IAM = 'Iam'
    CROSS_ACCOUNT_ROLE = 'CrossAccountRole'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsS3LoggingIntegrationRequest(LoggingIntegrationRequest):
    integration_type: Optional[AwsS3LoggingIntegrationType] = None
    bucket_name: Optional[str] = None
    region: Optional[str] = None
    role_arn: Optional[str] = None
    external_id: Optional[str] = None
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TelegramLoggingIntegrationRequest(LoggingIntegrationRequest):
    chat_id: Optional[str] = None
    bot_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NewRelicLoggingIntegrationRequest(LoggingIntegrationRequest):
    region: Optional[str] = None
    service_name: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MicrosoftTeamsLoggingIntegrationRequest(LoggingIntegrationRequest):
    channel_name: Optional[str] = None
    webhook_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbLoggingIntegrationRequest(LoggingIntegrationRequest):
    database_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class KafkaLoggingIntegrationRequest(LoggingIntegrationRequest):
    bootstrap_servers: Optional[str] = None
    topic: Optional[str] = None
    security_protocol: Optional[str] = None
    sasl_username: Optional[str] = None
    sasl_password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PrometheusLoggingIntegrationRequest(LoggingIntegrationRequest):
    endpoint_url: Optional[str] = None
    job_name: Optional[str] = None
    bearer_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DataDogLoggingIntegrationRequest(LoggingIntegrationRequest):
    site: Optional[str] = None
    service_name: Optional[str] = None
    environment: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InternalKafkaLoggingIntegrationRequest(LoggingIntegrationRequest):
    bootstrap_servers: Optional[str] = None
    topic: Optional[str] = None
    security_protocol: Optional[str] = None
    sasl_username: Optional[str] = None
    sasl_password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ElasticSearchLoggingIntegrationRequest(LoggingIntegrationRequest):
    uri: Optional[str] = None
    index: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ZabbixLoggingIntegrationRequest(LoggingIntegrationRequest):
    api_url: Optional[str] = None
    host_name: Optional[str] = None
    api_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SplunkLoggingIntegrationRequest(LoggingIntegrationRequest):
    hec_endpoint_url: Optional[str] = None
    index: Optional[str] = None
    hec_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AzureOtelLoggingIntegrationRequest(LoggingIntegrationRequest):
    endpoint_url: Optional[str] = None
    resource_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class KibanaLoggingIntegrationRequest(LoggingIntegrationRequest):
    uri: Optional[str] = None
    space_id: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LocalFileLoggingIntegrationRequest(LoggingIntegrationRequest):
    root_path: Optional[str] = None


class MembershipProvider(str, Enum):
    APPLE_SIGN_IN = 'AppleSignIn'
    GOOGLE_SIGN_IN = 'GoogleSignIn'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    X = 'X'
    GIT_HUB = 'GitHub'
    LINKED_IN = 'LinkedIn'
    OKTA = 'Okta'
    MICROSOFT = 'Microsoft'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[MembershipProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisplayName:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleName:
    name: Optional[str] = None
    display_name: Optional[str] = None
    # @Ignore()
    is_administrator: bool = False

    # @Ignore()
    is_authenticated: bool = False

    # @Ignore()
    is_guest: bool = False

    # @Ignore()
    is_root_role: bool = False

    # @Ignore()
    is_collaborator_role: bool = False

    # @Ignore()
    is_system_role: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OAuthModeConfig:
    name: Optional[DisplayName] = None
    callback_url: Optional[str] = None
    logout_url: Optional[str] = None
    failure_redirect_url: Optional[str] = None
    role_name: Optional[RoleName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OktaMembershipIntegrationRequest(MembershipIntegrationRequest):
    domain: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class XMembershipIntegrationRequest(MembershipIntegrationRequest):
    api_key: Optional[str] = None
    api_secret_key: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleMembershipIntegrationRequest(MembershipIntegrationRequest):
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MicrosoftMembershipIntegrationRequest(MembershipIntegrationRequest):
    tenant_id: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GitHubMembershipIntegrationRequest(MembershipIntegrationRequest):
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MetaMembershipIntegrationRequest(MembershipIntegrationRequest):
    app_id: Optional[str] = None
    app_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleMembershipIntegrationRequest(MembershipIntegrationRequest):
    team_id: Optional[str] = None
    app_bundle_id: Optional[str] = None
    service_id: Optional[str] = None
    key_id: Optional[str] = None
    private_key: Optional[str] = None
    is_production: bool = False
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


class PaymentGatewayPlatform(str, Enum):
    STRIPE = 'Stripe'
    ADYEN = 'Adyen'
    PADDLE = 'Paddle'
    LEMON_SQUEEZY = 'LemonSqueezy'
    APPLE_IN_APP = 'AppleInApp'
    GOOGLE_IN_APP = 'GoogleInApp'
    SHOPIFY = 'Shopify'
    WOO_COMMERCE = 'WooCommerce'
    MAGENTO = 'Magento'
    PAY_PAL = 'PayPal'
    BRAINTREE = 'Braintree'
    AUTHORIZE_NET = 'AuthorizeNet'
    CHECK_OUT_COM = 'CheckOutCom'
    MOLLIE = 'Mollie'
    WORLDPAY = 'Worldpay'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentIntegrationRequest:
    integration_id: Optional[str] = None
    gateway_platform: Optional[PaymentGatewayPlatform] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LemonSqueezyPaymentIntegrationRequest(PaymentIntegrationRequest):
    store_id: Optional[str] = None
    api_key: Optional[str] = None
    webhook_signing_secret: Optional[str] = None
    is_test_mode: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AdyenPaymentIntegrationRequest(PaymentIntegrationRequest):
    merchant_account: Optional[str] = None
    api_key: Optional[str] = None
    environment: Optional[str] = None
    webhook_id: Optional[str] = None
    webhook_hmac_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MolliePaymentIntegrationRequest(PaymentIntegrationRequest):
    profile_id: Optional[str] = None
    api_key: Optional[str] = None
    is_test_mode: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaddlePaymentIntegrationRequest(PaymentIntegrationRequest):
    api_key: Optional[str] = None
    webhook_endpoint_secret_key: Optional[str] = None
    environment: Optional[str] = None
    client_side_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PayPalPaymentIntegrationRequest(PaymentIntegrationRequest):
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    environment: Optional[str] = None
    brand_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StripePaymentIntegrationRequest(PaymentIntegrationRequest):
    publishable_key: Optional[str] = None
    secret_key: Optional[str] = None
    webhook_signing_secret: Optional[str] = None
    webhook_endpoint_id: Optional[str] = None
    default_currency: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleInAppPaymentIntegrationRequest(PaymentIntegrationRequest):
    merchant_identifier: Optional[str] = None
    merchant_domain: Optional[str] = None
    display_name: Optional[str] = None
    merchant_identity_certificate_p12_base64: Optional[str] = None
    merchant_identity_certificate_password: Optional[str] = None
    payment_processing_certificate_p12_base64: Optional[str] = None
    payment_processing_certificate_password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleInAppPaymentIntegrationRequest(PaymentIntegrationRequest):
    merchant_id: Optional[str] = None
    merchant_name: Optional[str] = None
    gateway: Optional[str] = None
    private_key_or_token: Optional[str] = None
    gateway_merchant_id: Optional[str] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[PushProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EdgeWebPushIntegrationRequest(PushIntegrationRequest):
    vapid_public_key: Optional[str] = None
    vapid_private_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChromePluginPushIntegrationRequest(PushIntegrationRequest):
    extension_id: Optional[str] = None
    vapid_public_key: Optional[str] = None
    vapid_private_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SafariPushIntegrationRequest(PushIntegrationRequest):
    website_push_id: Optional[str] = None
    certificate_p12_base64: Optional[str] = None
    certificate_password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChromeWebPushIntegrationRequest(PushIntegrationRequest):
    vapid_public_key: Optional[str] = None
    vapid_private_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FirefoxWebPushIntegrationRequest(PushIntegrationRequest):
    vapid_public_key: Optional[str] = None
    vapid_private_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AndroidFirebasePushIntegrationRequest(PushIntegrationRequest):
    project_id: Optional[str] = None
    client_email: Optional[str] = None
    service_account_json: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleApnsPushIntegrationRequest(PushIntegrationRequest):
    team_id: Optional[str] = None
    app_bundle_id: Optional[str] = None
    key_id: Optional[str] = None
    private_key: Optional[str] = None
    is_production: bool = False


class CodeProvider(str, Enum):
    AWS_LAMBDA = 'AwsLambda'
    AZURE_FUNCTIONS = 'AzureFunctions'
    GOOGLE_CLOUD_FUNCTIONS = 'GoogleCloudFunctions'
    PIPEDREAM = 'Pipedream'
    ZAPIER = 'Zapier'
    CLOUDFLARE_WORKERS = 'CloudflareWorkers'
    VERCEL = 'Vercel'
    NETLIFY = 'Netlify'
    SUPABASE_EDGE = 'SupabaseEdge'
    MODAL = 'Modal'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[CodeProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


class AwsLambdaIntegrationType(str, Enum):
    IAM = 'Iam'
    CROSS_ACCOUNT_ROLE = 'CrossAccountRole'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsLambdaCodeIntegrationRequest(CodeIntegrationRequest):
    integration_type: Optional[AwsLambdaIntegrationType] = None
    region: Optional[str] = None
    role_arn: Optional[str] = None
    external_id: Optional[str] = None
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AzureFunctionsCodeIntegrationRequest(CodeIntegrationRequest):
    function_app_name: Optional[str] = None
    resource_group: Optional[str] = None
    connection_string_or_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleCloudFunctionsCodeIntegrationRequest(CodeIntegrationRequest):
    project_id: Optional[str] = None
    region: Optional[str] = None
    service_account_json_key: Optional[str] = None


class LlmProvider(str, Enum):
    OPEN_A_I = 'OpenAI'
    ANTHROPIC = 'Anthropic'
    OLLAMA = 'Ollama'
    GROQ = 'Groq'
    GOOGLE = 'Google'
    MISTRAL = 'Mistral'
    OPEN_ROUTER = 'OpenRouter'
    GROK = 'Grok'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[LlmProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False
    endpoint: Optional[str] = None
    default_model: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OllamaLlmIntegrationRequest(LlmIntegrationRequest):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenRouterLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MistralLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GrokLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GroqLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AnthropicLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    api_key: Optional[str] = None


class McpProvider(str, Enum):
    DOCKER = 'Docker'
    OBSIDIAN = 'Obsidian'
    GOOGLE_CALENDAR = 'GoogleCalendar'


class McpTransport(str, Enum):
    SSE = 'Sse'
    HTTP_STREAM = 'HttpStream'
    STDIO = 'Stdio'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PlaywrightMcpIntegrationRequest(McpIntegrationRequest):
    command: Optional[str] = None
    args: Optional[List[str]] = None
    headless: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbMcpIntegrationRequest(McpIntegrationRequest):
    command: Optional[str] = None
    args: Optional[List[str]] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GitHubMcpIntegrationRequest(McpIntegrationRequest):
    server_url: Optional[str] = None
    access_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StripeMcpIntegrationRequest(McpIntegrationRequest):
    server_url: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BraveSearchMcpIntegrationRequest(McpIntegrationRequest):
    server_url: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ObsidianMcpIntegrationRequest(McpIntegrationRequest):
    command: Optional[str] = None
    args: Optional[List[str]] = None
    environment_variables: Optional[Dict[str, str]] = None


class CommunicationChannel(str, Enum):
    TRANSACTIONAL = 'Transactional'
    MARKETING = 'Marketing'
    SYSTEM = 'System'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TemplateDto(IHasViewId):
    view_id: Optional[str] = None
    template_name: Optional[str] = None
    description: Optional[str] = None
    communication_channel: Optional[CommunicationChannel] = None
    is_active: bool = False
    tags: Optional[List[str]] = None


class EmailTemplateEngine(str, Enum):
    NOT_SET = 'NotSet'
    HANDLEBARS = 'Handlebars'
    MJML = 'Mjml'
    LIQUID = 'Liquid'
    RAZOR = 'Razor'
    MUSTACHE = 'Mustache'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailBodyDto(IHasRazorTemplateCode):
    structure: Optional[str] = None
    code: Optional[str] = None
    template_engine: Optional[EmailTemplateEngine] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailMessageContentDto(IHasRazorTemplateCode):
    subject: Optional[str] = None
    body: Optional[EmailBodyDto] = None
    static_attachments: Optional[IReadOnlySet[FileResourceRefDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailMessageTranslationDto(IHasRazorTemplateCode):
    language: Optional[str] = None
    content: Optional[EmailMessageContentDto] = None
    static_attachments: Optional[IReadOnlySet[FileResourceRefDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateDto(TemplateDto, IBindableContract):
    translations: Optional[IReadOnlySet[EmailMessageTranslationDto]] = None
    static_attachments: Optional[IReadOnlySet[FileResourceRefDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushMessageContentDto(IHasRazorTemplateCode):
    title: Optional[str] = None
    body: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushMessageTranslationDto(IHasRazorTemplateCode):
    language: Optional[str] = None
    content: Optional[PushMessageContentDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateDto(TemplateDto, IHasRazorTemplateCode, IBindableContract):
    translations: Optional[IReadOnlySet[PushMessageTranslationDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsMessageContentDto(IHasRazorTemplateCode):
    subject: Optional[str] = None
    body: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsMessageTranslationDto(IHasRazorTemplateCode):
    language: Optional[str] = None
    content: Optional[SmsMessageContentDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsTemplateDto(TemplateDto, IHasRazorTemplateCode, IBindableContract):
    translations: Optional[IReadOnlySet[SmsMessageTranslationDto]] = None


class SystemEmailTemplateTheme(str, Enum):
    TEXT = 'Text'
    BRANDED = 'Branded'
    CREATIVE = 'Creative'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SystemEmailTemplateDto(EmailTemplateDto, IHasDatabaseId):
    image_preview: Optional[str] = None
    theme: Optional[SystemEmailTemplateTheme] = None
    system_group: Optional[str] = None
    system_tags: Optional[List[str]] = None
    for_trigger: Optional[TriggerType] = None
    hidden_system_email_template: bool = False
    id: Optional[str] = None


# @Flags()
class RespectTimeZoneSettings(IntEnum):
    RESPECT_TO_LAST_LOGIN_ZONE = 1
    RESPECT_TO_REGISTRATION_ZONE = 2
    RESPECT_TO_REGISTRATION_PROJECT_ZONE = 4


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignDeliverySettingsDto:
    recipients_source_type: Optional[EmailCampaignRecipientsSourceTypes] = None
    mapped_tokens: Optional[IReadOnlySet[TokenMappingDto]] = None
    campaign_time: Optional[int] = None
    respect_time_zone_settings: Optional[RespectTimeZoneSettings] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerActionEmailDto(TriggerActionDto):
    template_id: Optional[str] = None
    delivery_settings: Optional[EmailCampaignDeliverySettingsDto] = None


class PushCampaignRecipientsSourceTypes(str, Enum):
    ALL_USERS = 'AllUsers'
    SPECIFIED_USERS = 'SpecifiedUsers'
    COLLECTION = 'Collection'
    DEVICES = 'Devices'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushCampaignDeliverySettingsDto:
    recipients_source_type: Optional[PushCampaignRecipientsSourceTypes] = None
    mapped_tokens: Optional[List[TokenMappingDto]] = None
    campaign_time: Optional[int] = None
    respect_time_zone_settings: Optional[RespectTimeZoneSettings] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerActionPushDto(TriggerActionDto):
    template_id: Optional[str] = None
    delivery_settings: Optional[PushCampaignDeliverySettingsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeDeliverySettingsDto:
    mapped_tokens: Optional[List[TokenMappingDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerActionCodeDto(TriggerActionDto):
    function_id: Optional[str] = None
    delivery_settings: Optional[CodeDeliverySettingsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookDeliverySettingsDto:
    event_name: Optional[str] = None
    content_type: Optional[str] = None
    include_raw_payload: bool = False
    mapped_tokens: Optional[IReadOnlySet[TokenMappingDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerActionWebhookDto(TriggerActionDto):
    delivery_settings: Optional[WebhookDeliverySettingsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToAllUsersDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    roles_names: Optional[IReadOnlySet[str]] = None
    user_tags: Optional[IReadOnlySet[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToAccountUsersDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    user_recipients: Optional[IReadOnlySet[str]] = None
    user_cc: Optional[IReadOnlySet[str]] = None
    user_bcc: Optional[IReadOnlySet[str]] = None
    single_email_strategy: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToUsersDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    user_recipients: Optional[IReadOnlySet[str]] = None
    user_cc: Optional[IReadOnlySet[str]] = None
    user_bcc: Optional[IReadOnlySet[str]] = None
    single_email_strategy: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToEmailAddressesDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    recipients: Optional[IReadOnlySet[str]] = None
    recipients_cc: Optional[IReadOnlySet[str]] = None
    recipients_bcc: Optional[IReadOnlySet[str]] = None
    single_email_strategy: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToCollectionRecordsDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    fields: Optional[IReadOnlySet[str]] = None
    schema_name: Optional[str] = None
    field_type: Optional[CollectionEmailCampaignRecipientField] = None
    role_names: Optional[IReadOnlySet[str]] = None
    languages: Optional[IReadOnlySet[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushToAllUsersDeliverySettingsDto(PushCampaignDeliverySettingsDto):
    roles_names: Optional[List[str]] = None
    user_tags: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushToUsersDeliverySettingsDto(PushCampaignDeliverySettingsDto):
    recipients: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushToCollectionRecordsDeliverySettingsDto(PushCampaignDeliverySettingsDto):
    fields: List[str] = field(default_factory=list)
    field_type: Optional[CollectionEmailCampaignRecipientField] = None
    schema_name: Optional[str] = None
    role_names: Optional[List[str]] = None
    languages: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushDeviceDeliveryTokenDto:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushToDevicesDeliverySettingsDto(PushCampaignDeliverySettingsDto):
    devices: List[PushDeviceDeliveryTokenDto] = field(default_factory=list)


class SmsCampaignRecipientsSourceTypes(str, Enum):
    ALL_USERS = 'AllUsers'
    SPECIFIED_USERS = 'SpecifiedUsers'
    ACCOUNT_USERS = 'AccountUsers'
    PHONE_NUMBERS = 'PhoneNumbers'
    COLLECTION = 'Collection'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsCampaignDeliverySettingsDto:
    recipients_source_type: Optional[SmsCampaignRecipientsSourceTypes] = None
    mapped_tokens: Optional[List[TokenMappingDto]] = None
    campaign_time: Optional[int] = None
    respect_time_zone_settings: Optional[RespectTimeZoneSettings] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsToAllUsersDeliverySettingsDto(SmsCampaignDeliverySettingsDto):
    roles_names: Optional[List[str]] = None
    user_tags: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsToUsersDeliverySettingsDto(SmsCampaignDeliverySettingsDto):
    recipients: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsToCollectionRecordsDeliverySettingsDto(SmsCampaignDeliverySettingsDto):
    fields: List[str] = field(default_factory=list)
    field_type: Optional[CollectionEmailCampaignRecipientField] = None
    schema_name: Optional[str] = None
    role_names: Optional[List[str]] = None
    languages: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsToPhoneNumbersDeliverySettingsDto(SmsCampaignDeliverySettingsDto):
    phone_numbers: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegrationDto(IHasViewId):
    view_id: Optional[str] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False
    last_integration_test_at_utc: Optional[datetime.datetime] = None
    last_integration_test_succeeded: Optional[bool] = None
    last_integration_test_errors: Optional[IReadOnlyList[str]] = None
    human_delivery_confirmed_at_utc: Optional[datetime.datetime] = None
    requires_human_delivery_confirmation: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationDto(IntegrationDto):
    provider: Optional[LlmProvider] = None
    base_url: Optional[str] = None
    default_model: Optional[str] = None
    is_configured: bool = False
    is_system_owned: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiLlmIntegrationDto(LlmIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AnthropicLlmIntegrationDto(LlmIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OllamaLlmIntegrationDto(LlmIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GroqLlmIntegrationDto(LlmIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleLlmIntegrationDto(LlmIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MistralLlmIntegrationDto(LlmIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenRouterLlmIntegrationDto(LlmIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GrokLlmIntegrationDto(LlmIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpMetadata:
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None


class McpAuth(str, Enum):
    O_AUTH2 = 'OAuth2'
    API_KEY = 'ApiKey'
    NONE = 'None'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationDto(IntegrationDto):
    provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    metadata: Optional[McpMetadata] = None
    is_configured: bool = False
    is_system_owned: bool = False
    command: Optional[str] = None
    args: Optional[List[str]] = None
    server_url: Optional[str] = None
    auth: Optional[McpAuth] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DockerMcpIntegrationDto(McpIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleCalendarMcpIntegrationDto(McpIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ObsidianMcpIntegrationDto(McpIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationDto(IntegrationDto):
    provider: Optional[CodeProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsLambdaCrossAccountRoleCodeIntegrationDto(CodeIntegrationDto):
    region: Optional[str] = None
    role_arn: Optional[str] = None
    external_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsLambdaIamCodeIntegrationDto(CodeIntegrationDto):
    region: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AzureFunctionsCodeIntegrationDto(CodeIntegrationDto):
    function_app_name: Optional[str] = None
    resource_group: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleCloudFunctionsCodeIntegrationDto(CodeIntegrationDto):
    project_id: Optional[str] = None
    region: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsIntegrationDto(IntegrationDto):
    gateway_platform: Optional[PaymentGatewayPlatform] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AdyenPaymentIntegrationDto(PaymentsIntegrationDto):
    merchant_account: Optional[str] = None
    environment: Optional[str] = None
    webhook_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleInAppPaymentIntegrationDto(PaymentsIntegrationDto):
    merchant_identifier: Optional[str] = None
    merchant_domain: Optional[str] = None
    display_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleInAppPaymentIntegrationDto(PaymentsIntegrationDto):
    merchant_id: Optional[str] = None
    merchant_name: Optional[str] = None
    gateway: Optional[str] = None
    gateway_merchant_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LemonSqueezyPaymentIntegrationDto(PaymentsIntegrationDto):
    store_id: Optional[str] = None
    is_test_mode: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MolliePaymentIntegrationDto(PaymentsIntegrationDto):
    profile_id: Optional[str] = None
    is_test_mode: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaddlePaymentIntegrationDto(PaymentsIntegrationDto):
    environment: Optional[str] = None
    client_side_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PayPalPaymentIntegrationDto(PaymentsIntegrationDto):
    client_id: Optional[str] = None
    environment: Optional[str] = None
    brand_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StripePaymentIntegrationDto(PaymentsIntegrationDto):
    publishable_key: Optional[str] = None
    webhook_endpoint_id: Optional[str] = None
    default_currency: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ShopifyPaymentIntegrationDto(PaymentsIntegrationDto):
    shop_domain: Optional[str] = None
    webhook_secret: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WooCommercePaymentIntegrationDto(PaymentsIntegrationDto):
    store_url: Optional[str] = None
    webhook_secret: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MagentoPaymentIntegrationDto(PaymentsIntegrationDto):
    store_url: Optional[str] = None
    webhook_secret: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BraintreePaymentIntegrationDto(PaymentsIntegrationDto):
    merchant_id: Optional[str] = None
    environment: Optional[str] = None
    webhook_secret: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuthorizeNetPaymentIntegrationDto(PaymentsIntegrationDto):
    merchant_login_id: Optional[str] = None
    environment: Optional[str] = None
    webhook_signature_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CheckOutComPaymentIntegrationDto(PaymentsIntegrationDto):
    merchant_account: Optional[str] = None
    environment: Optional[str] = None
    webhook_secret: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WorldpayPaymentIntegrationDto(PaymentsIntegrationDto):
    merchant_code: Optional[str] = None
    environment: Optional[str] = None
    webhook_secret: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationDto(IntegrationDto):
    provider: Optional[MembershipProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleSignInMembershipIntegrationDto(MembershipIntegrationDto):
    team_id: Optional[str] = None
    app_bundle_id: Optional[str] = None
    service_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GitHubMembershipIntegrationDto(MembershipIntegrationDto):
    client_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleMembershipIntegrationDto(MembershipIntegrationDto):
    client_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MetaMembershipIntegrationDto(MembershipIntegrationDto):
    app_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MicrosoftMembershipIntegrationDto(MembershipIntegrationDto):
    tenant_id: Optional[str] = None
    client_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OktaMembershipIntegrationDto(MembershipIntegrationDto):
    domain: Optional[str] = None
    client_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class XMembershipIntegrationDto(MembershipIntegrationDto):
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationDto(IntegrationDto):
    provider: Optional[LoggingProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AmqpLoggingIntegrationDto(LoggingIntegrationDto):
    host: Optional[str] = None
    port: int = 0
    virtual_host: Optional[str] = None
    exchange: Optional[str] = None
    routing_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsKinesisLoggingIntegrationDto(LoggingIntegrationDto):
    stream_name: Optional[str] = None
    region: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsS3CrossAccountRoleLoggingIntegrationDto(LoggingIntegrationDto):
    bucket_name: Optional[str] = None
    region: Optional[str] = None
    role_arn: Optional[str] = None
    external_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsS3IamLoggingIntegrationDto(LoggingIntegrationDto):
    bucket_name: Optional[str] = None
    region: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AzureOtelLoggingIntegrationDto(LoggingIntegrationDto):
    endpoint_url: Optional[str] = None
    resource_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DataDogLoggingIntegrationDto(LoggingIntegrationDto):
    site: Optional[str] = None
    service_name: Optional[str] = None
    environment: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ElasticSearchLoggingIntegrationDto(LoggingIntegrationDto):
    uri: Optional[str] = None
    index: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InternalKafkaLoggingIntegrationDto(LoggingIntegrationDto):
    bootstrap_servers: Optional[str] = None
    topic: Optional[str] = None
    security_protocol: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class KafkaLoggingIntegrationDto(LoggingIntegrationDto):
    bootstrap_servers: Optional[str] = None
    topic: Optional[str] = None
    security_protocol: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class KibanaLoggingIntegrationDto(LoggingIntegrationDto):
    uri: Optional[str] = None
    space_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LocalFileLoggingIntegrationDto(LoggingIntegrationDto):
    root_path: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MicrosoftTeamsLoggingIntegrationDto(LoggingIntegrationDto):
    channel_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbLoggingIntegrationDto(LoggingIntegrationDto):
    database_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NewRelicLoggingIntegrationDto(LoggingIntegrationDto):
    region: Optional[str] = None
    service_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PrometheusLoggingIntegrationDto(LoggingIntegrationDto):
    endpoint_url: Optional[str] = None
    job_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SplunkLoggingIntegrationDto(LoggingIntegrationDto):
    hec_endpoint_url: Optional[str] = None
    index: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TelegramLoggingIntegrationDto(LoggingIntegrationDto):
    chat_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ZabbixLoggingIntegrationDto(LoggingIntegrationDto):
    api_url: Optional[str] = None
    host_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SlackLoggingIntegrationDto(LoggingIntegrationDto):
    channel_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationDto(IntegrationDto):
    provider: Optional[FileProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleICloudFilesIntegrationDto(FilesIntegrationDto):
    container_identifier: Optional[str] = None
    relative_path: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsS3CrossAccountRoleFilesIntegrationDto(FilesIntegrationDto):
    bucket_name: Optional[str] = None
    region: Optional[str] = None
    role_arn: Optional[str] = None
    external_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsS3IamFilesIntegrationDto(FilesIntegrationDto):
    bucket_name: Optional[str] = None
    region: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AzureBlobFilesIntegrationDto(FilesIntegrationDto):
    blob_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DropBoxFilesIntegrationDto(FilesIntegrationDto):
    root_path: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FtpFilesIntegrationDto(FilesIntegrationDto):
    host: Optional[str] = None
    port: int = 0
    root_path: Optional[str] = None
    use_ssl: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleCloudFilesIntegrationDto(FilesIntegrationDto):
    bucket_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleDriveFilesIntegrationDto(FilesIntegrationDto):
    root_folder_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LocalFilesIntegrationDto(FilesIntegrationDto):
    root_path: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationDto(IntegrationDto):
    provider: Optional[DatabaseProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAtlasClusterIntegrationDto(DatabaseIntegrationDto):
    database_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAtlasServerlessIntegrationDto(DatabaseIntegrationDto):
    database_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbConnectionStringIntegrationDto(DatabaseIntegrationDto):
    database_name: Optional[str] = None


class SmsProvider(str, Enum):
    TWILIO = 'Twilio'
    VONAGE = 'Vonage'
    PLIVO = 'Plivo'
    TELNYX = 'Telnyx'
    BIRD = 'Bird'
    TELESIGN = 'Telesign'
    SINCH = 'Sinch'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationDto(IntegrationDto):
    provider: Optional[SmsProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BirdSmsIntegrationDto(SmsIntegrationDto):
    originator: Optional[str] = None
    region: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PlivoSmsIntegrationDto(SmsIntegrationDto):
    auth_id: Optional[str] = None
    from_phone_number: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SinchSmsIntegrationDto(SmsIntegrationDto):
    service_plan_id: Optional[str] = None
    from_phone_number: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TelesignSmsIntegrationDto(SmsIntegrationDto):
    customer_id: Optional[str] = None
    from_sender: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TelnyxSmsIntegrationDto(SmsIntegrationDto):
    messaging_profile_id: Optional[str] = None
    from_phone_number: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TwilioSmsIntegrationDto(SmsIntegrationDto):
    account_sid: Optional[str] = None
    from_phone_number: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class VonageSmsIntegrationDto(SmsIntegrationDto):
    api_key: Optional[str] = None
    from_sender: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationDto(IntegrationDto):
    provider: Optional[PushProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AndroidFirebasePushIntegrationDto(PushIntegrationDto):
    project_id: Optional[str] = None
    client_email: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleApnsPushIntegrationDto(PushIntegrationDto):
    team_id: Optional[str] = None
    app_bundle_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChromePluginPushIntegrationDto(PushIntegrationDto):
    extension_id: Optional[str] = None
    vapid_public_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChromeWebPushIntegrationDto(PushIntegrationDto):
    vapid_public_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EdgeWebPushIntegrationDto(PushIntegrationDto):
    vapid_public_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FirefoxWebPushIntegrationDto(PushIntegrationDto):
    vapid_public_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SafariPushIntegrationDto(PushIntegrationDto):
    website_push_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationDto(IntegrationDto):
    provider: Optional[EmailProvider] = None
    email_address: Optional[str] = None
    email_sender_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsSesEmailIntegrationDto(EmailIntegrationDto):
    region: Optional[str] = None
    identity_arn: Optional[str] = None
    configuration_set_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsCrossAccountRoleEmailIntegrationDto(AwsSesEmailIntegrationDto):
    role_arn: Optional[str] = None
    external_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AwsIamEmailIntegrationDto(AwsSesEmailIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MailGunEmailIntegrationDto(EmailIntegrationDto):
    domain: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendGridEmailIntegrationDto(EmailIntegrationDto):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmtpEmailIntegrationDto(EmailIntegrationDto):
    host_name: Optional[str] = None
    port: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookDestinationDto:
    view_id: Optional[str] = None
    destination_name: Optional[str] = None
    endpoint_url: Optional[str] = None
    selected_events: Optional[IReadOnlyList[str]] = None
    extra_headers: Optional[IReadOnlyDictionary[str, str]] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegrationDto(IntegrationDto):
    destinations: Optional[IReadOnlyList[WebhookDestinationDto]] = None
    extra_headers: Optional[IReadOnlyDictionary[str, str]] = None


class SchedulerTaskType(str, Enum):
    EMAIL_CAMPAIGN = 'EmailCampaign'
    PUSH_CAMPAIGN = 'PushCampaign'
    SMS_CAMPAIGN = 'SmsCampaign'
    CODE_FUNCTIONAL_CALL = 'CodeFunctionalCall'
    WEBHOOK_CALL = 'WebhookCall'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerTaskDto:
    project_id: Optional[str] = None
    task_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    cron: Optional[str] = None
    type: Optional[SchedulerTaskType] = None
    payload_json: Optional[str] = None
    initiator_id: Optional[str] = None
    is_enabled: bool = False
    stop_on_error: bool = False
    created_at_unix: Optional[int] = None
    updated_at_unix: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAggregateDto(IHasViewId):
    view_id: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    schema_view_id: Optional[str] = None
    pipeline: Optional[str] = None


class MarketplaceTransport(str, Enum):
    MCP = 'Mcp'
    REST = 'Rest'
    CODE = 'Code'


class MarketplaceCategory(str, Enum):
    OTHER = 'Other'
    CRM = 'Crm'
    ERP = 'Erp'
    MARKETING = 'Marketing'
    COMMUNICATION = 'Communication'
    PRODUCTIVITY = 'Productivity'
    STORAGE = 'Storage'
    ANALYTICS = 'Analytics'
    IDENTITY = 'Identity'
    PAYMENTS = 'Payments'
    DEV_TOOLS = 'DevTools'
    AI = 'Ai'
    FILES = 'Files'
    DATABASE = 'Database'
    CALENDAR = 'Calendar'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationDto(IntegrationDto):
    listing_view_id: Optional[str] = None
    transport: Optional[MarketplaceTransport] = None
    vendor: Optional[str] = None
    category: Optional[MarketplaceCategory] = None
    description: Optional[str] = None
    config: Optional[IReadOnlyDictionary[str, str]] = None


class MarketplaceMappingSource(str, Enum):
    DEFAULT = 'Default'
    RESOLVER = 'Resolver'
    FROM_REQUEST = 'FromRequest'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceMappingDto:
    parameter_name: Optional[str] = None
    source: Optional[MarketplaceMappingSource] = None
    default_value: Optional[str] = None
    resolver: Optional[TokenMappingResolverType] = None
    token_key: Optional[str] = None
    from_request_path: Optional[str] = None
    is_required: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionBindingDto(IHasViewId):
    view_id: Optional[str] = None
    integration_view_id: Optional[str] = None
    function_key: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    is_enabled: bool = False
    mappings: Optional[IReadOnlyList[MarketplaceMappingDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionParameterDto:
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    is_required: bool = False
    default_value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionDefinitionDto:
    function_key: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    group: Optional[str] = None
    parameters: Optional[IReadOnlyList[MarketplaceFunctionParameterDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceListingDto(IHasViewId):
    view_id: Optional[str] = None
    slug: Optional[str] = None
    display_name: Optional[str] = None
    vendor: Optional[str] = None
    category: Optional[MarketplaceCategory] = None
    transport: Optional[MarketplaceTransport] = None
    description: Optional[str] = None
    icon_url: Optional[str] = None
    documentation_url: Optional[str] = None
    is_official: bool = False
    functions: Optional[IReadOnlyList[MarketplaceFunctionDefinitionDto]] = None


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


class SubscriptionType(str, Enum):
    MANAGED_SERVICE = 'ManagedService'
    LICENSE = 'License'


class IHasAccountId:
    account_id: Optional[str] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagDescriptionDto:
    title: Optional[str] = None
    description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagTranslationDto:
    language: Optional[str] = None
    content: Optional[TagDescriptionDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagDefinitionBaseDto:
    tag: Optional[str] = None
    translations: List[TagTranslationDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GroupDefinitionDto(TagDefinitionBaseDto):
    pass


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
class TagDefinitionDto(TagDefinitionBaseDto):
    default_delivery: Dict[str, bool] = field(default_factory=dict)


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
class EmailAddress:
    address: Optional[str] = None


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
class Tag:
    pass


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagDefinition(BaseTagDefinition):
    default_delivery: Dict[str, bool] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunication:
    channels: List[ProjectCommunicationChannel] = field(default_factory=list)
    groups: List[GroupDefinition] = field(default_factory=list)
    tags: List[TagDefinition] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TimeZone:
    zone_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteTrigger(CodeMashRequestBase):
    trigger_id: Optional[str] = None
    trigger_type: Optional[TriggerType] = None
    schema_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableTrigger(CodeMashRequestBase):
    trigger_id: Optional[str] = None
    trigger_type: Optional[TriggerType] = None
    schema_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableTrigger(CodeMashRequestBase):
    trigger_id: Optional[str] = None
    trigger_type: Optional[TriggerType] = None
    schema_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTrigger(CodeMashRequestBase):
    id: Optional[str] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTriggers(CodeMashListPaginationRequestBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveTrigger(CodeMashRequestBase):
    trigger: Optional[SaveTriggerRequest] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Integration(IIntegrationIdentification, IHasDomainEntityId):
    integration_id: Optional[IntegrationId] = None
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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegration(Integration):
    provider: Optional[MembershipProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PolicyId:
    template: Optional[str] = None
    tenancy_scope_view_id: Optional[str] = None
    view_id: Optional[str] = None
    is_system: bool = False


class PermissionEffect(str, Enum):
    ALLOW = 'Allow'
    DENY = 'Deny'


# @Flags()
class ApplicationModule(IntEnum):
    ACCOUNT = 0
    MEMBERSHIP = 1
    DATABASE = 2
    FILES = 4
    CODE = 8
    EMAIL = 16
    PUSH = 32
    PAYMENT = 64
    SCHEDULER = 128
    LOGGING = 256
    SERVER_EVENTS = 512
    AI = 1024
    SMS = 2048


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PermissionAction:
    module: Optional[ApplicationModule] = None
    operation: Optional[str] = None
    is_module_wildcard: bool = False
    is_operation_wildcard: bool = False
    is_concrete: bool = False
    specificity: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResourceKind:
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResourceIdentifier:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResourcePattern:
    account: Optional[AccountId] = None
    project: Optional[ProjectId] = None
    module: Optional[ApplicationModule] = None
    kind: Optional[ResourceKind] = None
    id: Optional[ResourceIdentifier] = None
    is_account_wildcard: bool = False
    is_project_wildcard: bool = False
    is_module_wildcard: bool = False
    is_kind_wildcard: bool = False
    is_id_wildcard: bool = False
    is_concrete: bool = False
    is_full_wildcard: bool = False
    specificity: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PolicyStatement:
    sid: Optional[str] = None
    effect: Optional[PermissionEffect] = None
    actions: List[PermissionAction] = field(default_factory=list)
    resources: List[ResourcePattern] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipPolicy:
    id: Optional[PolicyId] = None
    name: Optional[DisplayName] = None
    description: Optional[str] = None
    statements: List[PolicyStatement] = field(default_factory=list)
    disabled: bool = False
    is_system: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleId:
    template: Optional[str] = None
    tenancy_scope_view_id: Optional[str] = None
    view_id: Optional[str] = None
    is_system: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipRole:
    id: Optional[RoleId] = None
    name: Optional[DisplayName] = None
    description: Optional[str] = None
    attached_policies: List[PolicyId] = field(default_factory=list)
    disabled: bool = False
    is_system: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TemplateId:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerAction:
    type: Optional[TriggerActionType] = None
    integration_id: Optional[IntegrationId] = None
    template_id: Optional[TemplateId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TemplateCode:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Trigger(IHasDomainEntityId):
    trigger_id: Optional[TriggerId] = None
    name: Optional[DisplayName] = None
    trigger_action: Optional[TriggerAction] = None
    activation_code: Optional[TemplateCode] = None
    description: Optional[str] = None
    is_enabled: bool = False
    integration_id: Optional[IntegrationId] = None
    type: Optional[TriggerType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTrigger(Trigger):
    when: Optional[MembershipTriggerType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerByIdEventBase:
    trigger_id: Optional[TriggerId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaSettingsDto:
    soft_delete: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAggregateId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAggregateQuery:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAggregate:
    id: Optional[MongoDbAggregateId] = None
    display_name: Optional[DisplayName] = None
    description: Optional[str] = None
    query: Optional[MongoDbAggregateQuery] = None
    schema_id: Optional[SchemaId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegration(Integration):
    provider: Optional[DatabaseProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaName:
    value: Optional[str] = None
    title: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class JsonSchemaFieldName:
    field_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class JsonSchemaField:
    field_name: Optional[JsonSchemaFieldName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DataSchema:
    raw_json: Optional[str] = None
    fields: List[JsonSchemaField] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class VisualSchema:
    raw_json: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDraft:
    data_schema: Optional[DataSchema] = None
    visual_schema: Optional[VisualSchema] = None
    updated_at: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaVersion:
    value: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MetaSchemaVersion:
    value: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublishedSchemaVersion:
    version: Optional[SchemaVersion] = None
    data_schema: Optional[DataSchema] = None
    visual_schema: Optional[VisualSchema] = None
    meta_schema_version: Optional[MetaSchemaVersion] = None
    published_at: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaSettings:
    soft_delete: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Schema(IHasDomainEntityId):
    schema_name: Optional[SchemaName] = None
    id: Optional[SchemaId] = None
    draft: Optional[SchemaDraft] = None
    published_versions: Optional[IReadOnlyList[PublishedSchemaVersion]] = None
    triggers: Optional[List[Trigger]] = None
    settings: Optional[SchemaSettings] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDiff:
    added_fields: Optional[IReadOnlyList[str]] = None
    removed_fields: Optional[IReadOnlyList[str]] = None
    type_changed_fields: Optional[IReadOnlyList[str]] = None
    validator_tightened_fields: Optional[IReadOnlyList[str]] = None
    is_empty: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomyId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomyName:
    value: Optional[str] = None
    title: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RecordId:
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Taxonomy(IHasDomainEntityId):
    parent_id: Optional[TaxonomyId] = None
    id: Optional[TaxonomyId] = None
    name: Optional[TaxonomyName] = None
    description: Optional[str] = None
    terms_meta_visual_schema: Optional[VisualSchema] = None
    terms_meta_data_schema: Optional[DataSchema] = None
    dependencies: Optional[List[TaxonomyId]] = None
    record_id: Optional[RecordId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTrigger(Trigger):
    schema_id: Optional[SchemaId] = None
    when: Optional[SchemaTriggerType] = None
    configuration: Optional[TemplateCode] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailTemplate(CodeMashRequestBase):
    template_name: Optional[str] = None
    description: Optional[str] = None
    communication_channel: Optional[CommunicationChannel] = None
    tags: Optional[List[str]] = None
    static_attachments: Optional[List[FileResourceRefDto]] = None
    translations: List[EmailMessageTranslationDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TranslationDto:
    language: Optional[str] = None
    content: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailFooterId:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSenderName:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegration(Integration):
    provider: Optional[EmailProvider] = None
    email_address: Optional[EmailAddress] = None
    email_sender_name: Optional[EmailSenderName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSignatureId:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileResourceRef:
    resource: Optional[FileResource] = None
    integration_id: Optional[IntegrationId] = None
    provider: Optional[FileProvider] = None
    path: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegration(Integration):
    provider: Optional[CodeProvider] = None


class MarketplaceIntegrationTransport(str, Enum):
    MCP = 'Mcp'
    REST = 'Rest'
    CODE = 'Code'


class MarketplaceIntegrationCategory(str, Enum):
    OTHER = 'Other'
    CRM = 'Crm'
    ERP = 'Erp'
    MARKETING = 'Marketing'
    COMMUNICATION = 'Communication'
    PRODUCTIVITY = 'Productivity'
    STORAGE = 'Storage'
    ANALYTICS = 'Analytics'
    IDENTITY = 'Identity'
    PAYMENTS = 'Payments'
    DEV_TOOLS = 'DevTools'
    AI = 'Ai'
    FILES = 'Files'
    DATABASE = 'Database'
    CALENDAR = 'Calendar'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegration(Integration):
    capability: Optional[str] = None
    listing_view_id: Optional[str] = None
    transport: Optional[MarketplaceIntegrationTransport] = None
    vendor: Optional[str] = None
    category: Optional[MarketplaceIntegrationCategory] = None
    description: Optional[str] = None
    config: Optional[IReadOnlyDictionary[str, str]] = None


class MarketplaceMappingSourceKind(str, Enum):
    DEFAULT = 'Default'
    RESOLVER = 'Resolver'
    FROM_REQUEST = 'FromRequest'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionMapping:
    parameter_name: Optional[str] = None
    source: Optional[MarketplaceMappingSourceKind] = None
    default_value: Optional[str] = None
    resolver: Optional[TokenMappingResolverType] = None
    token_key: Optional[str] = None
    from_request_path: Optional[str] = None
    is_required: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionBinding(IHasDomainEntityId):
    binding_id: Optional[str] = None
    integration_id: Optional[IntegrationId] = None
    function_key: Optional[str] = None
    display_name: Optional[DisplayName] = None
    description: Optional[str] = None
    is_enabled: bool = False
    mappings: Optional[IReadOnlyList[MarketplaceFunctionMapping]] = None
    view_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePushTemplate(CodeMashRequestBase):
    template_name: Optional[str] = None
    description: Optional[str] = None
    communication_channel: Optional[CommunicationChannel] = None
    tags: Optional[List[str]] = None
    translations: List[PushMessageTranslationDto] = field(default_factory=list)


class IHasAccountId:
    account_id: Optional[str] = None


class DeviceType(str, Enum):
    UNKNOWN = 'Unknown'
    PHONE = 'Phone'
    TABLET = 'Tablet'
    DESKTOP = 'Desktop'
    TV = 'Tv'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushDeviceDto:
    device_id: Optional[str] = None
    device_os: Optional[str] = None
    token: Optional[str] = None
    brand: Optional[str] = None
    manufacturer: Optional[str] = None
    model_name: Optional[str] = None
    device_name: Optional[str] = None
    device_type: Optional[DeviceType] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None
    platform_api_level: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegration(Integration):
    provider: Optional[PushProvider] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegration(Integration):
    provider: Optional[LoggingProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookDestinationId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerEventName:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookDestination:
    destination_id: Optional[WebhookDestinationId] = None
    destination_name: Optional[DisplayName] = None
    endpoint_url: Optional[DomainUrl] = None
    selected_events: Optional[IReadOnlySet[TriggerEventName]] = None
    extra_headers: Optional[IReadOnlyDictionary[str, str]] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegration(Integration):
    capability: Optional[str] = None
    destinations: Optional[IReadOnlySet[WebhookDestination]] = None
    extra_headers: Optional[IReadOnlyDictionary[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerTaskRequest:
    type: Optional[SchedulerTaskType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaskId(AggregateId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CronExpression:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserId(IHasDomainEntityId):
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerTask(IHasDomainEntityId):
    id: Optional[TaskId] = None
    type: Optional[SchedulerTaskType] = None
    name: Optional[DisplayName] = None
    description: Optional[str] = None
    cron: Optional[CronExpression] = None
    payload_json: Optional[str] = None
    initiator_id: Optional[UserId] = None
    is_enabled: bool = False
    stop_on_error: bool = False


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
class AccountOwnerDto:
    email: Optional[str] = None
    display_name: Optional[str] = None
    billing_email: Optional[str] = None
    operations_email: Optional[str] = None
    security_email: Optional[str] = None


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


# @Flags()
class AccountStatus(IntEnum):
    REGISTERED = 1
    PENDING_VALIDATION = 2
    ACTIVE = 8
    IN_ACTIVE = 16
    BLOCKED = 32
    UNREGISTERED = 64


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountStatusDto:
    account_id: Optional[str] = None
    account_id_as_guid: Optional[str] = None
    user_id: Optional[str] = None
    logged_in_user_id: Optional[str] = None
    logged_in_user_email: Optional[str] = None
    status: Optional[AccountStatus] = None
    project_cap: int = 0
    permissions: List[str] = field(default_factory=list)
    roles: List[str] = field(default_factory=list)
    allowed_projects: Optional[List[str]] = None
    trial_was_issued: bool = False


class ProjectStatus(str, Enum):
    ACTIVE = 'Active'
    DISABLED = 'Disabled'
    REMOVED = 'Removed'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectRegionDto:
    id: Optional[str] = None
    continent: Optional[Continent] = None
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectBrandDto:
    main_color: Optional[str] = None
    accent_color: Optional[str] = None
    logo: Optional[FileResourceRefDto] = None
    icon: Optional[FileResourceRefDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotificationsSettingsGroupDto:
    tag: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotificationSettingsChannelDto:
    channel: Optional[CommunicationChannel] = None
    groups: List[NotificationsSettingsGroupDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotificationSettingsDto:
    channels: List[NotificationSettingsChannelDto] = field(default_factory=list)
    all_groups: List[GroupDefinitionDto] = field(default_factory=list)
    all_tags: List[TagDefinitionDto] = field(default_factory=list)


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
class SchemaTriggerDto(TriggerDto):
    schema_id: Optional[str] = None
    when: Optional[SchemaTriggerType] = None
    configuration_code: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseDto:
    is_enabled: bool = False
    triggers: Optional[List[SchemaTriggerDto]] = None
    default_integration_view_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSignatureDto(IHasViewId):
    view_id: Optional[str] = None
    display_name: Optional[str] = None
    translations: List[TranslationDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailFooterDto(IHasViewId):
    view_id: Optional[str] = None
    display_name: Optional[str] = None
    translations: List[TranslationDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailDto:
    is_enabled: bool = False
    default_integration_view_id: Optional[str] = None
    signatures: Optional[List[EmailSignatureDto]] = None
    footers: Optional[List[EmailFooterDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiDto:
    is_enabled: bool = False
    default_integration_view_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerDto(TriggerDto):
    when: Optional[MembershipTriggerType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleItemDto:
    id: Optional[str] = None
    name: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    is_system: bool = False
    attached_policies: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PolicyStatementDto:
    sid: Optional[str] = None
    effect: Optional[PermissionEffect] = None
    actions: List[str] = field(default_factory=list)
    resources: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PolicyItemDto:
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    is_system: bool = False
    statements: Optional[List[PolicyStatementDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuthorizationDto:
    user_registers_as_role: Optional[str] = None
    allowed_register_roles: Optional[List[str]] = None
    allowed_provider_register_roles: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipDto:
    is_enabled: bool = False
    triggers: Optional[List[MembershipTriggerDto]] = None
    custom_roles: Optional[List[RoleItemDto]] = None
    custom_policies: Optional[List[PolicyItemDto]] = None
    authorization: Optional[AuthorizationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingDto:
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ServerEventsDto:
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushDto:
    is_enabled: bool = False
    default_integration_view_id: Optional[str] = None
    marketing_tags: Optional[List[TagDefinitionDto]] = None
    transactional_tags: Optional[List[TagDefinitionDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerDto:
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeDto:
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesTriggerDto(TriggerDto):
    when: Optional[FilesTriggerType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesDto:
    is_enabled: bool = False
    triggers: Optional[List[FilesTriggerDto]] = None
    default_integration_view_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentTriggerDto(TriggerDto):
    when: Optional[PaymentTriggerType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsDto:
    is_enabled: bool = False
    triggers: Optional[List[PaymentTriggerDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsDto:
    is_enabled: bool = False
    default_integration_view_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectDto(IHasViewId, IBindableContract):
    account_view_id: Optional[str] = None
    project_status: Optional[ProjectStatus] = None
    is_active: bool = False
    view_id: Optional[str] = None
    name: Optional[str] = None
    unique_name: Optional[str] = None
    host_label: Optional[str] = None
    api_host: Optional[str] = None
    description: Optional[str] = None
    marketing_url: Optional[str] = None
    default_language: Optional[str] = None
    languages: List[str] = field(default_factory=list)
    regions: Optional[List[ProjectRegionDto]] = None
    brand: Optional[ProjectBrandDto] = None
    notification_settings: Optional[NotificationSettingsDto] = None
    allowed_origins: Optional[List[str]] = None
    database: Optional[DatabaseDto] = None
    email: Optional[EmailDto] = None
    ai: Optional[AiDto] = None
    membership: Optional[MembershipDto] = None
    logging: Optional[LoggingDto] = None
    server_events: Optional[ServerEventsDto] = None
    push: Optional[PushDto] = None
    scheduler: Optional[SchedulerDto] = None
    code: Optional[CodeDto] = None
    files: Optional[FilesDto] = None
    payments: Optional[PaymentsDto] = None
    sms: Optional[SmsDto] = None
    database_enabled: bool = False
    email_enabled: bool = False
    membership_enabled: bool = False
    logging_enabled: bool = False
    server_events_enabled: bool = False
    push_enabled: bool = False
    scheduler_enabled: bool = False
    code_enabled: bool = False
    files_enabled: bool = False
    payments_enabled: bool = False
    sms_enabled: bool = False
    default_files_integration_view_id: Optional[str] = None
    default_database_integration_view_id: Optional[str] = None
    default_email_integration_view_id: Optional[str] = None
    default_llm_integration_view_id: Optional[str] = None
    default_push_integration_view_id: Optional[str] = None
    default_sms_integration_view_id: Optional[str] = None
    connections: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectListItemDto:
    view_id: Optional[str] = None
    is_active: bool = False
    name: Optional[str] = None
    unique_name: Optional[str] = None
    regions: Optional[List[ProjectRegionDto]] = None


TViewModelProjection = TypeVar('TViewModelProjection')


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaginatedResponse(Generic[TViewModelProjection]):
    items: Optional[IList[TViewModelProjection]] = None
    has_more: bool = False
    has_previous: bool = False
    starting_after: Optional[str] = None
    ending_before: Optional[str] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeMashSubscriptionDto:
    view_id: Optional[str] = None
    domain: Optional[str] = None
    will_expire_on: datetime.datetime = datetime.datetime(1, 1, 1)
    issued_on: datetime.datetime = datetime.datetime(1, 1, 1)
    is_trial: bool = False
    subscription_ref_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LicenseDto(CodeMashSubscriptionDto):
    is_enterprise: bool = False
    project_cap: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTriggerResponse(ResponseBase):
    trigger: Optional[TriggerDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerProjectionList(IHasViewId):
    view_id: Optional[str] = None
    name: Optional[str] = None
    action_type: Optional[TriggerActionType] = None
    has_pre_execute_code: bool = False
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerProjectionList(TriggerProjectionList):
    type: Optional[MembershipTriggerType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTriggersResponse(ResponseBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleListProjectionDto:
    view_id: Optional[str] = None
    name: Optional[str] = None
    display_name: Optional[str] = None
    is_system: bool = False
    policy_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegrationListProjection(IHasViewId):
    view_id: Optional[str] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False
    last_integration_test_at_utc: Optional[datetime.datetime] = None
    last_integration_test_succeeded: Optional[bool] = None
    last_integration_test_errors: Optional[IReadOnlyList[str]] = None
    human_delivery_confirmed_at_utc: Optional[datetime.datetime] = None
    requires_human_delivery_confirmation: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationListProjection(IntegrationListProjection):
    provider: Optional[MembershipProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerProjectionList(TriggerProjectionList):
    type: Optional[SchemaTriggerType] = None


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
class TaxonomyDto(IHasViewId):
    view_id: Optional[str] = None
    name: Optional[str] = None
    slug: Optional[str] = None
    parent_id: Optional[str] = None
    description: Optional[str] = None
    terms_meta_data_schema: Optional[DataSchemaDto] = None
    terms_meta_visual_schema: Optional[VisualSchemaDto] = None
    dependencies: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomyListProjection(IHasViewId):
    view_id: Optional[str] = None
    taxonomy_name: Optional[str] = None
    taxonomy_slug: Optional[str] = None
    parent_id: Optional[str] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDraftDto:
    data_schema: Optional[DataSchemaDto] = None
    visual_schema: Optional[VisualSchemaDto] = None
    updated_at: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDiffDto:
    from_version: int = 0
    to_version: int = 0
    added: List[str] = field(default_factory=list)
    removed: List[str] = field(default_factory=list)
    type_changed: List[str] = field(default_factory=list)
    validator_tightened: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaVersionSummaryDto:
    version: int = 0
    meta_schema_version: int = 0
    published_at: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationListProjection(IntegrationListProjection):
    provider: Optional[DatabaseProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAggregateListProjection(IHasViewId):
    view_id: Optional[str] = None
    display_name: Optional[str] = None
    schema_view_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesTriggerProjectionList(TriggerProjectionList):
    type: Optional[FilesTriggerType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationListProjection(IntegrationListProjection):
    provider: Optional[FileProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TemplateListProjection(IHasViewId):
    view_id: Optional[str] = None
    template_name: Optional[str] = None
    is_active: bool = False
    type: Optional[CommunicationChannel] = None
    tags: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MjmlParseError:
    line: int = 0
    message: Optional[str] = None
    tag_name: Optional[str] = None
    formatted_message: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class HtmlFromMjmlResponse:
    html: Optional[str] = None
    errors: List[MjmlParseError] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateListProjection(TemplateListProjection):
    has_attachments: bool = False
    languages: Optional[IReadOnlySet[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SystemEmailTemplateListProjection(EmailTemplateListProjection):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListItemProjection(IHasViewId):
    view_id: Optional[str] = None
    display_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListItemWithTranslationsProjection(ListItemProjection):
    translations: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSettings(IBindableContract):
    signatures: Optional[IList[ListItemWithTranslationsProjection]] = None
    footers: Optional[IList[ListItemWithTranslationsProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationListProjection(IntegrationListProjection):
    email_provider: Optional[EmailProvider] = None
    sender_email_address: Optional[str] = None
    sender_display_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegrationTestResultItemDto:
    operation: Optional[str] = None
    result: Optional[str] = None
    errors: Optional[IReadOnlyList[str]] = None


class CampaignStatus(str, Enum):
    PENDING = 'Pending'
    REGISTERED = 'Registered'
    SCHEDULED = 'Scheduled'
    STARTED = 'Started'
    STOPPED = 'Stopped'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    FAILED = 'Failed'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CampaignStatusChangeEntryDto:
    time: datetime.datetime = datetime.datetime(1, 1, 1)
    status: Optional[CampaignStatus] = None
    errors: Optional[IReadOnlySet[ErrorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CampaignDto(IHasResponsibleUserId, IHasDatabaseId):
    view_id: Optional[str] = None
    created_on: datetime.datetime = datetime.datetime(1, 1, 1)
    language: Optional[str] = None
    force_campaign_language: bool = False
    campaign_processing_integration_id: Optional[str] = None
    status_history: Optional[IReadOnlySet[CampaignStatusChangeEntryDto]] = None
    status: Optional[CampaignStatusChangeEntryDto] = None
    token_mapping_values: Optional[IReadOnlySet[TokenMappingDto]] = None
    notes: Optional[str] = None
    user_id: Optional[str] = None
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignDto(CampaignDto):
    delivery_settings: Optional[EmailCampaignDeliverySettingsDto] = None
    template: Optional[EmailTemplateDto] = None
    template_is_system: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignListProjection:
    view_id: Optional[str] = None
    template_name: Optional[str] = None
    template_id: Optional[str] = None
    integration_id: Optional[str] = None
    language: Optional[str] = None
    strategy: Optional[str] = None
    latest_status: Optional[CampaignStatus] = None
    created_on: datetime.datetime = datetime.datetime(1, 1, 1)


class CampaignBatchStatus(str, Enum):
    REGISTERED = 'Registered'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    FAILED = 'Failed'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BatchStatusChangeEntryDto:
    time: datetime.datetime = datetime.datetime(1, 1, 1)
    status: Optional[CampaignBatchStatus] = None
    errors: Optional[IReadOnlySet[ErrorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CampaignBatchDto(IHasDatabaseId):
    campaign_id: Optional[str] = None
    batch_id: Optional[str] = None
    start_after: Optional[str] = None
    status_history: List[BatchStatusChangeEntryDto] = field(default_factory=list)
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailRecipientDto:
    email_address: Optional[str] = None
    language: Optional[str] = None
    time_zone_id: Optional[str] = None
    user_token_mappings: Optional[IReadOnlySet[TokenMappingDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailRecipientsDto:
    to: Optional[IReadOnlySet[EmailRecipientDto]] = None
    cc: Optional[IReadOnlySet[EmailRecipientDto]] = None
    bcc: Optional[IReadOnlySet[EmailRecipientDto]] = None
    starting_after: Optional[str] = None
    has_more: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignBatchDto(CampaignBatchDto):
    recipients: Optional[EmailRecipientsDto] = None


class CampaignNotificationStatus(str, Enum):
    COMPLETED = 'Completed'
    BLOCKED_BY_USER_PREFERENCE_BLOCK_ALL = 'BlockedByUserPreferenceBlockAll'
    BLOCKED_BY_USER_PREFERENCE_BLOCK_BY_TAG = 'BlockedByUserPreferenceBlockByTag'
    FAILED = 'Failed'
    VIEWED = 'Viewed'
    CLICKED = 'Clicked'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotificationStatusChangeEntryDto:
    time: datetime.datetime = datetime.datetime(1, 1, 1)
    status: Optional[CampaignNotificationStatus] = None
    source_id: Optional[str] = None
    errors: Optional[IReadOnlySet[ErrorDto]] = None
    tags: Optional[IReadOnlySet[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CampaignBatchNotificationDto(IHasDatabaseId):
    campaign_id: Optional[str] = None
    batch_id: Optional[str] = None
    notification_id: Optional[str] = None
    ref_notification_id: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    model: Optional[Dict[str, str]] = None
    status_history: Optional[IReadOnlySet[NotificationStatusChangeEntryDto]] = None
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignBatchNotificationDto(CampaignBatchNotificationDto):
    recipients: Optional[EmailRecipientsDto] = None
    content: Optional[EmailMessageContentDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CampaignStatsDto:
    batches: int = 0
    sent: int = 0
    failed: int = 0
    success_rate: Decimal = decimal.Decimal(0)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateListProjection(TemplateListProjection):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationListProjection(IntegrationListProjection):
    provider: Optional[PushProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentTriggerProjectionList(TriggerProjectionList):
    type: Optional[PaymentTriggerType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsIntegrationListProjection(IntegrationListProjection):
    gateway_platform: Optional[PaymentGatewayPlatform] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationListProjection(IntegrationListProjection):
    provider: Optional[LoggingProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationListProjection(IntegrationListProjection):
    llm_provider: Optional[LlmProvider] = None
    base_url: Optional[str] = None
    default_model: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationListProjection(IntegrationListProjection):
    mcp_provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    category: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerTaskListProjection(IHasViewId):
    task_id: Optional[str] = None
    name: Optional[str] = None
    cron: Optional[str] = None
    type: Optional[SchedulerTaskType] = None
    is_enabled: bool = False
    view_id: Optional[str] = None


class ILlmApiKeyRequest:
    api_key: Optional[str] = None


class IHasViewId:
    view_id: Optional[str] = None


class IBindableContract:
    pass


class IHasRazorTemplateCode:
    pass


class IHasDatabaseId:
    id: Optional[str] = None


class IHasDomainEntityId:
    view_id: Optional[str] = None


class IIntegrationIdentification:
    integration_id: Optional[IntegrationId] = None
    capability: Optional[str] = None
    is_system_owned: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSubject:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailBody:
    code: Optional[TemplateCode] = None
    structure: Optional[str] = None
    email_template_engine: Optional[EmailTemplateEngine] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailMessageContent:
    subject: Optional[EmailSubject] = None
    body: Optional[EmailBody] = None
    static_attachments: Optional[List[FileResourceRef]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CronExpression:
    value: Optional[str] = None
    parsed: Optional[CronExpression] = None


class IHasResponsibleUserId:
    user_id: Optional[str] = None


class ICursorArgs:
    field: Optional[str] = None
    order: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileTrigger(Trigger):
    when: Optional[FilesTriggerType] = None
    file_resource_ref: Optional[FileResourceRef] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentTrigger(Trigger):
    when: Optional[PaymentTriggerType] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StringField(JsonSchemaField):
    format: Optional[str] = None
    pattern: Optional[str] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    translate_options: Optional[IReadOnlyDictionary[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DecimalField(JsonSchemaField):
    minimum: Optional[Decimal] = None
    maximum: Optional[Decimal] = None
    multiple_of: Optional[Decimal] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CurrencyField(JsonSchemaField):
    allowed_currencies: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BooleanField(JsonSchemaField):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DateField(JsonSchemaField):
    minimum: Optional[int] = None
    maximum: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegerField(JsonSchemaField):
    minimum: Optional[int] = None
    maximum: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GeolocationField(JsonSchemaField):
    allowed_types: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TagsField(JsonSchemaField):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileField(JsonSchemaField):
    storages: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomySelectionField(JsonSchemaField):
    taxonomy_id: Optional[str] = None
    multiple: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CollectionSelectionField(JsonSchemaField):
    collection_id: Optional[str] = None
    display_field: Optional[str] = None
    multiple: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserSelectionField(JsonSchemaField):
    multiple: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleSelectionField(JsonSchemaField):
    multiple: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnumSelectionField(JsonSchemaField):
    values: Optional[IReadOnlyList[str]] = None
    multiple: bool = False


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
class GetAccountProfileResponse(ResponseBase):
    item: Optional[AccountOwnerDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountStatusResponse(ResponseBase):
    item: Optional[AccountStatusDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateStripeCheckoutSessionResponse(IdResponse):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetStripeBillingPortalUrlResponse(IdResponse):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateTeamMemberFromInvitationResponse(IdResponse):
    token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjectResponse(ResponseBase):
    item: Optional[ProjectDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjectsResponse(ResponseBase):
    list: Optional[List[ProjectListItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountRegionsResponse(ResponseBase):
    items: Optional[List[ProjectRegionDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjectTokensResponse(ResponseBase):
    tokens: Optional[List[TokenMappingDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateAccountResponse(IdResponse):
    token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountCollaboratorsResponse(ResponseBase):
    list: Optional[PaginatedResponse[UserDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLicensesResponse(ResponseBase):
    list: Optional[List[LicenseDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserEmailPreferencesResponse(ResponseBase):
    default_language: Optional[str] = None
    project_languages: List[str] = field(default_factory=list)
    block_all_marketing_messages: bool = False
    subscribed_tags: Optional[Dict[str, HashSet[str]]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipTriggerResponse(GetTriggerResponse):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipTriggersResponse(GetTriggersResponse):
    list: Optional[PaginatedResponse[MembershipTriggerProjectionList]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetRoleResponse(ResponseBase):
    role: Optional[RoleItemDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetRolesResponse(ResponseBase):
    roles: List[RoleListProjectionDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPolicyResponse(ResponseBase):
    policy: Optional[PolicyItemDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPoliciesResponse(ResponseBase):
    policies: List[PolicyItemDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipIntegrationResponse(ResponseBase):
    item: Optional[MembershipIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipIntegrationsResponse(ResponseBase):
    list: Optional[PaginatedResponse[MembershipIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchemaTriggerResponse(GetTriggerResponse):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchemaTriggersResponse(GetTriggersResponse):
    list: Optional[PaginatedResponse[SchemaTriggerProjectionList]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomyResponse(ResponseBase):
    item: Optional[TaxonomyDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomiesResponse(ResponseBase):
    list: Optional[PaginatedResponse[TaxonomyListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomyTermResponse(ResponseBase):
    item: Optional[TermDto] = None


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
class GetDatabaseSchemaDraftResponse(ResponseBase):
    item: Optional[SchemaDraftDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaVersionDiffResponse(ResponseBase):
    item: Optional[SchemaDiffDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaVersionsResponse(ResponseBase):
    items: Optional[List[SchemaVersionSummaryDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseIntegrationResponse(ResponseBase):
    item: Optional[DatabaseIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseIntegrationsResponse(ResponseBase):
    default_integration_id: Optional[str] = None
    list: Optional[PaginatedResponse[DatabaseIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseAggregateResponse(ResponseBase):
    item: Optional[MongoDbAggregateDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseAggregatesResponse(ResponseBase):
    list: Optional[PaginatedResponse[MongoDbAggregateListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestDatabaseAggregateResponse(ResponseBase):
    result: Optional[List[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesTriggerResponse(GetTriggerResponse):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesTriggersResponse(GetTriggersResponse):
    list: Optional[PaginatedResponse[FilesTriggerProjectionList]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesIntegrationResponse(ResponseBase):
    item: Optional[FilesIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesIntegrationsResponse(ResponseBase):
    default_integration_id: Optional[str] = None
    list: Optional[PaginatedResponse[FilesIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplateResponse(ResponseBase):
    item: Optional[EmailTemplateDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplatesResponse(ResponseBase):
    list: Optional[PaginatedResponse[TemplateListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetHtmlFromMjmlResponse(ResponseBase):
    variables: Optional[List[str]] = None
    html_from_mjml_response: Optional[HtmlFromMjmlResponse] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSystemEmailTemplateResponse(ResponseBase):
    item: Optional[SystemEmailTemplateDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSystemEmailTemplatesResponse(ResponseBase):
    list: Optional[PaginatedResponse[SystemEmailTemplateListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplateAvailableTokensResponse(ResponseBase):
    tokens: Optional[Dict[str, List[str]]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailSignatureResponse(ResponseBase):
    item: Optional[EmailSignatureDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailSignaturesResponse(ResponseBase):
    list: Optional[PaginatedResponse[ListItemWithTranslationsProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailSettingsResponse(ResponseBase):
    settings: Optional[EmailSettings] = None
    system_tags: Optional[List[GroupDefinitionDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailIntegrationResponse(ResponseBase):
    item: Optional[EmailIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailIntegrationsResponse(ResponseBase):
    default_integration_id: Optional[str] = None
    list: Optional[PaginatedResponse[EmailIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestEmailIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailFooterResponse(ResponseBase):
    item: Optional[EmailFooterDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailFootersResponse(ResponseBase):
    list: Optional[PaginatedResponse[ListItemWithTranslationsProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignResponse(ResponseBase):
    item: Optional[EmailCampaignDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignsResponse(ResponseBase):
    list: Optional[PaginatedResponse[EmailCampaignListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignBatchesResponse(ResponseBase):
    list: Optional[PaginatedResponse[EmailCampaignBatchDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignBatchNotificationResponse(ResponseBase):
    campaign_notification: Optional[EmailCampaignBatchNotificationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignBatchNotificationsResponse(ResponseBase):
    batch_status_history: Optional[List[BatchStatusChangeEntryDto]] = None
    list: Optional[PaginatedResponse[EmailCampaignBatchNotificationDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignStatisticsResponse(ResponseBase):
    stats: Optional[CampaignStatsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PreviewEmailNotificationResponse(ResponseBase):
    subject: Optional[str] = None
    body: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignMessageResponse(ResponseBase):
    email_message_entity: Optional[EmailCampaignBatchNotificationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignMessagesResponse(ResponseBase):
    list: Optional[PaginatedResponse[EmailCampaignBatchNotificationDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushTemplateResponse(ResponseBase):
    item: Optional[PushTemplateDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushTemplatesResponse(ResponseBase):
    list: Optional[PaginatedResponse[PushTemplateListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushMessageContentTokensResponse(ResponseBase):
    tokens: Optional[Dict[str, List[str]]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushIntegrationResponse(ResponseBase):
    item: Optional[PushIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushIntegrationsResponse(ResponseBase):
    default_integration_id: Optional[str] = None
    list: Optional[PaginatedResponse[PushIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsTriggerResponse(GetTriggerResponse):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsTriggersResponse(GetTriggersResponse):
    list: Optional[PaginatedResponse[PaymentTriggerProjectionList]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsIntegrationResponse(ResponseBase):
    item: Optional[PaymentsIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsIntegrationsResponse(ResponseBase):
    list: Optional[PaginatedResponse[PaymentsIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestPaymentsIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLoggingIntegrationResponse(ResponseBase):
    item: Optional[LoggingIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLoggingIntegrationsResponse(ResponseBase):
    list: Optional[PaginatedResponse[LoggingIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestLoggingIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AskChatResponse(ResponseBase):
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLlmIntegrationResponse(ResponseBase):
    item: Optional[LlmIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLlmIntegrationsResponse(ResponseBase):
    default_integration_id: Optional[str] = None
    list: Optional[PaginatedResponse[LlmIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestLlmIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMcpIntegrationResponse(ResponseBase):
    item: Optional[McpIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMcpIntegrationsResponse(ResponseBase):
    default_integration_id: Optional[str] = None
    list: Optional[PaginatedResponse[McpIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetWebhookIntegrationResponse(ResponseBase):
    item: Optional[WebhookIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RevealWebhookIntegrationSecretResponse(ResponseBase):
    signing_secret: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RotateWebhookIntegrationSecretResponse(ResponseBase):
    signing_secret: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveWebhookDestinationResponse(ResponseBase):
    destination_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchedulerTaskResponse(ResponseBase):
    item: Optional[SchedulerTaskDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchedulerTasksResponse(ResponseBase):
    list: Optional[PaginatedResponse[SchedulerTaskListProjection]] = None


# @Route("/internal/_typegen", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InternalsTypeGen:
    typegen_0__smtp_email_integration_request: Optional[SmtpEmailIntegrationRequest] = None
    typegen_1__aws_ses_email_integration_request: Optional[AwsSesEmailIntegrationRequest] = None
    typegen_2__send_grid_email_integration_request: Optional[SendGridEmailIntegrationRequest] = None
    typegen_3__mail_gun_email_integration_request: Optional[MailGunEmailIntegrationRequest] = None
    typegen_4__email_to_all_users_delivery_settings_request: Optional[EmailToAllUsersDeliverySettingsRequest] = None
    typegen_5__email_to_account_users_delivery_settings_request: Optional[EmailToAccountUsersDeliverySettingsRequest] = None
    typegen_6__email_to_collection_records_delivery_settings_request: Optional[EmailToCollectionRecordsDeliverySettingsRequest] = None
    typegen_7__email_to_emails_delivery_settings_request: Optional[EmailToEmailsDeliverySettingsRequest] = None
    typegen_8__email_to_users_delivery_settings_request: Optional[EmailToUsersDeliverySettingsRequest] = None
    typegen_9__membership_trigger_request: Optional[MembershipTriggerRequest] = None
    typegen_10__schema_trigger_request: Optional[SchemaTriggerRequest] = None
    typegen_11__files_trigger_request: Optional[FilesTriggerRequest] = None
    typegen_12__payment_trigger_request: Optional[PaymentTriggerRequest] = None
    typegen_13__mongo_db_atlas_serverless_database_integration_request: Optional[MongoDbAtlasServerlessDatabaseIntegrationRequest] = None
    typegen_14__mongo_db_atlas_cluster_database_integration_request: Optional[MongoDbAtlasClusterDatabaseIntegrationRequest] = None
    typegen_15__mongo_db_connection_string_database_integration_request: Optional[MongoDbConnectionStringDatabaseIntegrationRequest] = None
    typegen_16__google_drive_files_integration_request: Optional[GoogleDriveFilesIntegrationRequest] = None
    typegen_17__ftp_files_integration_request: Optional[FtpFilesIntegrationRequest] = None
    typegen_18__drop_box_files_integration_request: Optional[DropBoxFilesIntegrationRequest] = None
    typegen_19__apple_i_cloud_files_integration_request: Optional[AppleICloudFilesIntegrationRequest] = None
    typegen_20__aws_s3_files_integration_request: Optional[AwsS3FilesIntegrationRequest] = None
    typegen_21__google_cloud_files_integration_request: Optional[GoogleCloudFilesIntegrationRequest] = None
    typegen_22__azure_blob_files_integration_request: Optional[AzureBlobFilesIntegrationRequest] = None
    typegen_23__local_files_integration_request: Optional[LocalFilesIntegrationRequest] = None
    typegen_24__amqp_logging_integration_request: Optional[AmqpLoggingIntegrationRequest] = None
    typegen_25__aws_kinesis_logging_integration_request: Optional[AwsKinesisLoggingIntegrationRequest] = None
    typegen_26__aws_s3_logging_integration_request: Optional[AwsS3LoggingIntegrationRequest] = None
    typegen_27__telegram_logging_integration_request: Optional[TelegramLoggingIntegrationRequest] = None
    typegen_28__new_relic_logging_integration_request: Optional[NewRelicLoggingIntegrationRequest] = None
    typegen_29__microsoft_teams_logging_integration_request: Optional[MicrosoftTeamsLoggingIntegrationRequest] = None
    typegen_30__mongo_db_logging_integration_request: Optional[MongoDbLoggingIntegrationRequest] = None
    typegen_31__kafka_logging_integration_request: Optional[KafkaLoggingIntegrationRequest] = None
    typegen_32__prometheus_logging_integration_request: Optional[PrometheusLoggingIntegrationRequest] = None
    typegen_33__data_dog_logging_integration_request: Optional[DataDogLoggingIntegrationRequest] = None
    typegen_34__internal_kafka_logging_integration_request: Optional[InternalKafkaLoggingIntegrationRequest] = None
    typegen_35__elastic_search_logging_integration_request: Optional[ElasticSearchLoggingIntegrationRequest] = None
    typegen_36__zabbix_logging_integration_request: Optional[ZabbixLoggingIntegrationRequest] = None
    typegen_37__splunk_logging_integration_request: Optional[SplunkLoggingIntegrationRequest] = None
    typegen_38__azure_otel_logging_integration_request: Optional[AzureOtelLoggingIntegrationRequest] = None
    typegen_39__kibana_logging_integration_request: Optional[KibanaLoggingIntegrationRequest] = None
    typegen_40__local_file_logging_integration_request: Optional[LocalFileLoggingIntegrationRequest] = None
    typegen_41__okta_membership_integration_request: Optional[OktaMembershipIntegrationRequest] = None
    typegen_42__x_membership_integration_request: Optional[XMembershipIntegrationRequest] = None
    typegen_43__google_membership_integration_request: Optional[GoogleMembershipIntegrationRequest] = None
    typegen_44__microsoft_membership_integration_request: Optional[MicrosoftMembershipIntegrationRequest] = None
    typegen_45__git_hub_membership_integration_request: Optional[GitHubMembershipIntegrationRequest] = None
    typegen_46__meta_membership_integration_request: Optional[MetaMembershipIntegrationRequest] = None
    typegen_47__apple_membership_integration_request: Optional[AppleMembershipIntegrationRequest] = None
    typegen_48__lemon_squeezy_payment_integration_request: Optional[LemonSqueezyPaymentIntegrationRequest] = None
    typegen_49__adyen_payment_integration_request: Optional[AdyenPaymentIntegrationRequest] = None
    typegen_50__mollie_payment_integration_request: Optional[MolliePaymentIntegrationRequest] = None
    typegen_51__paddle_payment_integration_request: Optional[PaddlePaymentIntegrationRequest] = None
    typegen_52__pay_pal_payment_integration_request: Optional[PayPalPaymentIntegrationRequest] = None
    typegen_53__stripe_payment_integration_request: Optional[StripePaymentIntegrationRequest] = None
    typegen_54__apple_in_app_payment_integration_request: Optional[AppleInAppPaymentIntegrationRequest] = None
    typegen_55__google_in_app_payment_integration_request: Optional[GoogleInAppPaymentIntegrationRequest] = None
    typegen_56__edge_web_push_integration_request: Optional[EdgeWebPushIntegrationRequest] = None
    typegen_57__chrome_plugin_push_integration_request: Optional[ChromePluginPushIntegrationRequest] = None
    typegen_58__safari_push_integration_request: Optional[SafariPushIntegrationRequest] = None
    typegen_59__chrome_web_push_integration_request: Optional[ChromeWebPushIntegrationRequest] = None
    typegen_60__firefox_web_push_integration_request: Optional[FirefoxWebPushIntegrationRequest] = None
    typegen_61__android_firebase_push_integration_request: Optional[AndroidFirebasePushIntegrationRequest] = None
    typegen_62__apple_apns_push_integration_request: Optional[AppleApnsPushIntegrationRequest] = None
    typegen_65__aws_lambda_code_integration_request: Optional[AwsLambdaCodeIntegrationRequest] = None
    typegen_66__azure_functions_code_integration_request: Optional[AzureFunctionsCodeIntegrationRequest] = None
    typegen_67__google_cloud_functions_code_integration_request: Optional[GoogleCloudFunctionsCodeIntegrationRequest] = None
    typegen_68__ollama_llm_integration_request: Optional[OllamaLlmIntegrationRequest] = None
    typegen_69__open_router_llm_integration_request: Optional[OpenRouterLlmIntegrationRequest] = None
    typegen_70__mistral_llm_integration_request: Optional[MistralLlmIntegrationRequest] = None
    typegen_71__grok_llm_integration_request: Optional[GrokLlmIntegrationRequest] = None
    typegen_72__groq_llm_integration_request: Optional[GroqLlmIntegrationRequest] = None
    typegen_73__google_llm_integration_request: Optional[GoogleLlmIntegrationRequest] = None
    typegen_74__anthropic_llm_integration_request: Optional[AnthropicLlmIntegrationRequest] = None
    typegen_75__open_ai_llm_integration_request: Optional[OpenAiLlmIntegrationRequest] = None
    typegen_76__playwright_mcp_integration_request: Optional[PlaywrightMcpIntegrationRequest] = None
    typegen_77__mongo_db_mcp_integration_request: Optional[MongoDbMcpIntegrationRequest] = None
    typegen_78__git_hub_mcp_integration_request: Optional[GitHubMcpIntegrationRequest] = None
    typegen_79__stripe_mcp_integration_request: Optional[StripeMcpIntegrationRequest] = None
    typegen_80__brave_search_mcp_integration_request: Optional[BraveSearchMcpIntegrationRequest] = None
    typegen_81__obsidian_mcp_integration_request: Optional[ObsidianMcpIntegrationRequest] = None
    typegen_82__email_template_dto: Optional[EmailTemplateDto] = None
    typegen_83__push_template_dto: Optional[PushTemplateDto] = None
    typegen_84__sms_template_dto: Optional[SmsTemplateDto] = None
    typegen_85__system_email_template_dto: Optional[SystemEmailTemplateDto] = None
    typegen_86__trigger_action_email_dto: Optional[TriggerActionEmailDto] = None
    typegen_87__trigger_action_push_dto: Optional[TriggerActionPushDto] = None
    typegen_88__trigger_action_code_dto: Optional[TriggerActionCodeDto] = None
    typegen_89__trigger_action_webhook_dto: Optional[TriggerActionWebhookDto] = None
    typegen_90__email_to_all_users_delivery_settings_dto: Optional[EmailToAllUsersDeliverySettingsDto] = None
    typegen_91__email_to_account_users_delivery_settings_dto: Optional[EmailToAccountUsersDeliverySettingsDto] = None
    typegen_92__email_to_users_delivery_settings_dto: Optional[EmailToUsersDeliverySettingsDto] = None
    typegen_93__email_to_email_addresses_delivery_settings_dto: Optional[EmailToEmailAddressesDeliverySettingsDto] = None
    typegen_94__email_to_collection_records_delivery_settings_dto: Optional[EmailToCollectionRecordsDeliverySettingsDto] = None
    typegen_95__push_to_all_users_delivery_settings_dto: Optional[PushToAllUsersDeliverySettingsDto] = None
    typegen_96__push_to_users_delivery_settings_dto: Optional[PushToUsersDeliverySettingsDto] = None
    typegen_97__push_to_collection_records_delivery_settings_dto: Optional[PushToCollectionRecordsDeliverySettingsDto] = None
    typegen_98__push_to_devices_delivery_settings_dto: Optional[PushToDevicesDeliverySettingsDto] = None
    typegen_99__sms_to_all_users_delivery_settings_dto: Optional[SmsToAllUsersDeliverySettingsDto] = None
    typegen_100__sms_to_users_delivery_settings_dto: Optional[SmsToUsersDeliverySettingsDto] = None
    typegen_101__sms_to_collection_records_delivery_settings_dto: Optional[SmsToCollectionRecordsDeliverySettingsDto] = None
    typegen_102__sms_to_phone_numbers_delivery_settings_dto: Optional[SmsToPhoneNumbersDeliverySettingsDto] = None
    typegen_103__open_ai_llm_integration_dto: Optional[OpenAiLlmIntegrationDto] = None
    typegen_104__anthropic_llm_integration_dto: Optional[AnthropicLlmIntegrationDto] = None
    typegen_105__ollama_llm_integration_dto: Optional[OllamaLlmIntegrationDto] = None
    typegen_106__groq_llm_integration_dto: Optional[GroqLlmIntegrationDto] = None
    typegen_107__google_llm_integration_dto: Optional[GoogleLlmIntegrationDto] = None
    typegen_108__mistral_llm_integration_dto: Optional[MistralLlmIntegrationDto] = None
    typegen_109__open_router_llm_integration_dto: Optional[OpenRouterLlmIntegrationDto] = None
    typegen_110__grok_llm_integration_dto: Optional[GrokLlmIntegrationDto] = None
    typegen_111__docker_mcp_integration_dto: Optional[DockerMcpIntegrationDto] = None
    typegen_112__google_calendar_mcp_integration_dto: Optional[GoogleCalendarMcpIntegrationDto] = None
    typegen_113__obsidian_mcp_integration_dto: Optional[ObsidianMcpIntegrationDto] = None
    typegen_114__aws_lambda_cross_account_role_code_integration_dto: Optional[AwsLambdaCrossAccountRoleCodeIntegrationDto] = None
    typegen_115__aws_lambda_iam_code_integration_dto: Optional[AwsLambdaIamCodeIntegrationDto] = None
    typegen_116__azure_functions_code_integration_dto: Optional[AzureFunctionsCodeIntegrationDto] = None
    typegen_118__google_cloud_functions_code_integration_dto: Optional[GoogleCloudFunctionsCodeIntegrationDto] = None
    typegen_120__adyen_payment_integration_dto: Optional[AdyenPaymentIntegrationDto] = None
    typegen_121__apple_in_app_payment_integration_dto: Optional[AppleInAppPaymentIntegrationDto] = None
    typegen_122__google_in_app_payment_integration_dto: Optional[GoogleInAppPaymentIntegrationDto] = None
    typegen_123__lemon_squeezy_payment_integration_dto: Optional[LemonSqueezyPaymentIntegrationDto] = None
    typegen_124__mollie_payment_integration_dto: Optional[MolliePaymentIntegrationDto] = None
    typegen_125__paddle_payment_integration_dto: Optional[PaddlePaymentIntegrationDto] = None
    typegen_126__pay_pal_payment_integration_dto: Optional[PayPalPaymentIntegrationDto] = None
    typegen_127__stripe_payment_integration_dto: Optional[StripePaymentIntegrationDto] = None
    typegen_184__shopify_payment_integration_dto: Optional[ShopifyPaymentIntegrationDto] = None
    typegen_185__woo_commerce_payment_integration_dto: Optional[WooCommercePaymentIntegrationDto] = None
    typegen_186__magento_payment_integration_dto: Optional[MagentoPaymentIntegrationDto] = None
    typegen_187__braintree_payment_integration_dto: Optional[BraintreePaymentIntegrationDto] = None
    typegen_188__authorize_net_payment_integration_dto: Optional[AuthorizeNetPaymentIntegrationDto] = None
    typegen_189__check_out_com_payment_integration_dto: Optional[CheckOutComPaymentIntegrationDto] = None
    typegen_190__worldpay_payment_integration_dto: Optional[WorldpayPaymentIntegrationDto] = None
    typegen_128__apple_sign_in_membership_integration_dto: Optional[AppleSignInMembershipIntegrationDto] = None
    typegen_129__git_hub_membership_integration_dto: Optional[GitHubMembershipIntegrationDto] = None
    typegen_130__google_membership_integration_dto: Optional[GoogleMembershipIntegrationDto] = None
    typegen_131__meta_membership_integration_dto: Optional[MetaMembershipIntegrationDto] = None
    typegen_132__microsoft_membership_integration_dto: Optional[MicrosoftMembershipIntegrationDto] = None
    typegen_133__okta_membership_integration_dto: Optional[OktaMembershipIntegrationDto] = None
    typegen_134__x_membership_integration_dto: Optional[XMembershipIntegrationDto] = None
    typegen_135__amqp_logging_integration_dto: Optional[AmqpLoggingIntegrationDto] = None
    typegen_136__aws_kinesis_logging_integration_dto: Optional[AwsKinesisLoggingIntegrationDto] = None
    typegen_137__aws_s3_cross_account_role_logging_integration_dto: Optional[AwsS3CrossAccountRoleLoggingIntegrationDto] = None
    typegen_138__aws_s3_iam_logging_integration_dto: Optional[AwsS3IamLoggingIntegrationDto] = None
    typegen_139__azure_otel_logging_integration_dto: Optional[AzureOtelLoggingIntegrationDto] = None
    typegen_140__data_dog_logging_integration_dto: Optional[DataDogLoggingIntegrationDto] = None
    typegen_141__elastic_search_logging_integration_dto: Optional[ElasticSearchLoggingIntegrationDto] = None
    typegen_142__internal_kafka_logging_integration_dto: Optional[InternalKafkaLoggingIntegrationDto] = None
    typegen_143__kafka_logging_integration_dto: Optional[KafkaLoggingIntegrationDto] = None
    typegen_144__kibana_logging_integration_dto: Optional[KibanaLoggingIntegrationDto] = None
    typegen_145__local_file_logging_integration_dto: Optional[LocalFileLoggingIntegrationDto] = None
    typegen_146__microsoft_teams_logging_integration_dto: Optional[MicrosoftTeamsLoggingIntegrationDto] = None
    typegen_147__mongo_db_logging_integration_dto: Optional[MongoDbLoggingIntegrationDto] = None
    typegen_148__new_relic_logging_integration_dto: Optional[NewRelicLoggingIntegrationDto] = None
    typegen_149__prometheus_logging_integration_dto: Optional[PrometheusLoggingIntegrationDto] = None
    typegen_150__splunk_logging_integration_dto: Optional[SplunkLoggingIntegrationDto] = None
    typegen_151__telegram_logging_integration_dto: Optional[TelegramLoggingIntegrationDto] = None
    typegen_152__zabbix_logging_integration_dto: Optional[ZabbixLoggingIntegrationDto] = None
    typegen_191__slack_logging_integration_dto: Optional[SlackLoggingIntegrationDto] = None
    typegen_153__apple_i_cloud_files_integration_dto: Optional[AppleICloudFilesIntegrationDto] = None
    typegen_154__aws_s3_cross_account_role_files_integration_dto: Optional[AwsS3CrossAccountRoleFilesIntegrationDto] = None
    typegen_155__aws_s3_iam_files_integration_dto: Optional[AwsS3IamFilesIntegrationDto] = None
    typegen_156__azure_blob_files_integration_dto: Optional[AzureBlobFilesIntegrationDto] = None
    typegen_157__drop_box_files_integration_dto: Optional[DropBoxFilesIntegrationDto] = None
    typegen_158__ftp_files_integration_dto: Optional[FtpFilesIntegrationDto] = None
    typegen_159__google_cloud_files_integration_dto: Optional[GoogleCloudFilesIntegrationDto] = None
    typegen_160__google_drive_files_integration_dto: Optional[GoogleDriveFilesIntegrationDto] = None
    typegen_161__local_files_integration_dto: Optional[LocalFilesIntegrationDto] = None
    typegen_162__mongo_db_atlas_cluster_integration_dto: Optional[MongoDbAtlasClusterIntegrationDto] = None
    typegen_163__mongo_db_atlas_serverless_integration_dto: Optional[MongoDbAtlasServerlessIntegrationDto] = None
    typegen_164__mongo_db_connection_string_integration_dto: Optional[MongoDbConnectionStringIntegrationDto] = None
    typegen_165__bird_sms_integration_dto: Optional[BirdSmsIntegrationDto] = None
    typegen_166__plivo_sms_integration_dto: Optional[PlivoSmsIntegrationDto] = None
    typegen_167__sinch_sms_integration_dto: Optional[SinchSmsIntegrationDto] = None
    typegen_168__telesign_sms_integration_dto: Optional[TelesignSmsIntegrationDto] = None
    typegen_169__telnyx_sms_integration_dto: Optional[TelnyxSmsIntegrationDto] = None
    typegen_170__twilio_sms_integration_dto: Optional[TwilioSmsIntegrationDto] = None
    typegen_171__vonage_sms_integration_dto: Optional[VonageSmsIntegrationDto] = None
    typegen_172__android_firebase_push_integration_dto: Optional[AndroidFirebasePushIntegrationDto] = None
    typegen_173__apple_apns_push_integration_dto: Optional[AppleApnsPushIntegrationDto] = None
    typegen_174__chrome_plugin_push_integration_dto: Optional[ChromePluginPushIntegrationDto] = None
    typegen_175__chrome_web_push_integration_dto: Optional[ChromeWebPushIntegrationDto] = None
    typegen_176__edge_web_push_integration_dto: Optional[EdgeWebPushIntegrationDto] = None
    typegen_177__firefox_web_push_integration_dto: Optional[FirefoxWebPushIntegrationDto] = None
    typegen_178__safari_push_integration_dto: Optional[SafariPushIntegrationDto] = None
    typegen_179__aws_cross_account_role_email_integration_dto: Optional[AwsCrossAccountRoleEmailIntegrationDto] = None
    typegen_180__aws_iam_email_integration_dto: Optional[AwsIamEmailIntegrationDto] = None
    typegen_181__mail_gun_email_integration_dto: Optional[MailGunEmailIntegrationDto] = None
    typegen_182__send_grid_email_integration_dto: Optional[SendGridEmailIntegrationDto] = None
    typegen_183__smtp_email_integration_dto: Optional[SmtpEmailIntegrationDto] = None
    typegen_192__webhook_integration_dto: Optional[WebhookIntegrationDto] = None
    typegen_193__webhook_destination_dto: Optional[WebhookDestinationDto] = None
    typegen_194__scheduler_task_dto: Optional[SchedulerTaskDto] = None
    typegen_195__mongo_db_aggregate_dto: Optional[MongoDbAggregateDto] = None
    typegen_196__marketplace_integration_dto: Optional[MarketplaceIntegrationDto] = None
    typegen_197__marketplace_function_binding_dto: Optional[MarketplaceFunctionBindingDto] = None
    typegen_198__marketplace_listing_dto: Optional[MarketplaceListingDto] = None
    typegen_199__marketplace_function_definition_dto: Optional[MarketplaceFunctionDefinitionDto] = None
    typegen_200__marketplace_function_parameter_dto: Optional[MarketplaceFunctionParameterDto] = None
    typegen_201__marketplace_mapping_dto: Optional[MarketplaceMappingDto] = None


# @Route("/{version}/echo", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Echo(RequestBase, IReturn[EchoResponse]):
    pass


# @Route("/{version}/account/profile", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountProfile(RequestBase, IReturn[GetAccountProfileResponse]):
    pass


# @Route("/{version}/account/profile", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAccountProfile(RequestBase, IReturn[EmptyResponse]):
    display_name: Optional[str] = None
    billing_email: Optional[str] = None
    operations_email: Optional[str] = None
    security_email: Optional[str] = None


# @Route("/{version}/account/verify/resend", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResendAccountVerificationToken(RequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/account/status", "GET")
# @Api(Description="Get Account Status.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountStatus(RequestBase, IReturn[GetAccountStatusResponse]):
    """
    Get Account Status.
    """

    pass


# @Route("/{version}/account/stripe/create-checkout-session", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateStripeCheckoutSession(RequestBase, IReturn[CreateStripeCheckoutSessionResponse]):
    subscription_type: Optional[SubscriptionType] = None
    domain: Optional[str] = None
    project_cap: int = 0
    new_project_session_id: Optional[str] = None
    return_url: Optional[str] = None


# @Route("/{version}/account/stripe/get-portal-url", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetStripeBillingPortalUrl(RequestBase, IReturn[GetStripeBillingPortalUrlResponse]):
    subscription_type: Optional[SubscriptionType] = None
    return_url: Optional[str] = None


# @Route("/{version}/account/team/member", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateTeamMemberFromInvitation(RequestBase, IReturn[CreateTeamMemberFromInvitationResponse]):
    # @ApiMember(DataType="string", Description="Display name of the account holder", IsRequired=true, Name="DisplayName", ParameterType="form")
    display_name: Optional[str] = None
    """
    Display name of the account holder
    """


    # @ApiMember(DataType="string", Description="Token from invitation email", IsRequired=true, Name="Token", ParameterType="form")
    token: Optional[str] = None
    """
    Token from invitation email
    """


    # @ApiMember(DataType="string", Description="Set password for a new account", Format="password", IsRequired=true, Name="Password", ParameterType="form")
    password: Optional[str] = None
    """
    Set password for a new account
    """


# @Route("/{version}/account/verify", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class VerifyAccount(RequestBase, IReturn[EmptyResponse], IHasAccountId):
    token: Optional[str] = None
    account_id: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/notifications/settings/group", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteNotificationsGroup(CodeMashRequestBase, IReturn[EmptyResponse]):
    group_tag: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/notifications/settings/tag", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteNotificationsTag(CodeMashRequestBase, IReturn[EmptyResponse]):
    tag: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/notifications/settings/group/tag", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveTagFromNotificationsGroup(CodeMashRequestBase, IReturn[EmptyResponse]):
    group_tag: Optional[str] = None
    tag: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/notifications/settings/group", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveNotificationsGroup(CodeMashRequestBase, IReturn[EmptyResponse]):
    group_definition: Optional[GroupDefinitionDto] = None
    channel: Optional[CommunicationChannel] = None
    origin_channel: Optional[CommunicationChannel] = None


# @Route("/{version}/account/projects/{projectId}/notifications/settings/tag", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveNotificationsTag(CodeMashRequestBase, IReturn[EmptyResponse]):
    tag_definition: Optional[TagDefinitionDto] = None
    channel: Optional[CommunicationChannel] = None
    group_tag: Optional[str] = None


# @Route("/{version}/account/projects", "POST")
# @Api(Description="Create a new backend project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateProjectRequest(RequestBase, IReturn[IdResponse]):
    """
    Create a new backend project.
    """

    integration: Optional[DatabaseIntegrationRequest] = None
    project_name: Optional[str] = None
    regions: Optional[List[str]] = None
    description: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteProject(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/account/projects/{projectId}", "GET")
# @Api(Description="Gets project info.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProject(CodeMashRequestBase, IReturn[GetProjectResponse]):
    """
    Gets project info.
    """

    pass


# @Route("/{version}/account/projects", "GET")
# @Api(Description="Retrieve projects list.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjects(RequestBase, IReturn[GetProjectsResponse]):
    """
    Retrieve projects list.
    """

    pass


# @Route("/{version}/account/regions", "GET")
# @Api(Description="Get available project regions.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountRegions(RequestBase, IReturn[GetAccountRegionsResponse]):
    """
    Get available project regions.
    """

    pass


# @Route("/{version}/account/projects/{projectId}/tokens", "GET")
# @Api(Description="Gets project tokens.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjectTokens(CodeMashRequestBase, IReturn[GetProjectTokensResponse]):
    """
    Gets project tokens.
    """

    initiator_id: Optional[str] = None
    recipient_id: Optional[str] = None
    target_user_id: Optional[str] = None
    membership_trigger_old_user_id: Optional[str] = None
    membership_trigger_new_user_id: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/settings/accent-color", "PATCH")
# @Api(Description="Updates project accent color")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectAccentColor(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project accent color
    """

    color: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/settings/icon", "PATCH")
# @Api(Description="Updates project icon")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectIcon(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project icon
    """

    file_resource: Optional[FileResourceDto] = None


# @Route("/{version}/account/projects/{projectId}/settings/logo", "PATCH")
# @Api(Description="Updates project logo")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectLogo(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project logo
    """

    file_resource: Optional[FileResourceDto] = None


# @Route("/{version}/account/projects/{projectId}/settings/main-color", "PATCH")
# @Api(Description="Updates project main color")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectMainColor(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project main color
    """

    color: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/settings/origins", "PATCH")
# @Api(Description="Updates project CORS settings")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectAllowedOrigins(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project CORS settings
    """

    origins: Optional[List[str]] = None


# @Route("/{version}/account/projects/{projectId}/settings/default-language", "PATCH")
# @Api(Description="Update project default language")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectDefaultLanguage(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Update project default language
    """

    default_language: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/settings/description", "PATCH")
# @Api(Description="Updates project description")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectDescription(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project description
    """

    description: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/disable", "PATCH")
# @Api(Description="Disables project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableProject(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disables project
    """

    pass


# @Route("/{version}/account/projects/{projectId}/enable", "PATCH")
# @Api(Description="Enables project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableProject(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enables project
    """

    pass


# @Route("/{version}/account/projects/{projectId}/settings/languages", "PATCH")
# @Api(Description="Updates project languages")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectLanguages(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project languages
    """

    languages: List[str] = field(default_factory=list)


# @Route("/{version}/account/projects/{projectId}/settings/url", "PATCH")
# @Api(Description="Updates project marketing url")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectUrl(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project marketing url
    """

    url: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/settings/name", "PATCH")
# @Api(Description="Updates project name")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectName(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project name
    """

    name: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}/settings/regions", "PATCH")
# @Api(Description="Updates project regions")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectRegions(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project regions
    """

    regions: Optional[List[str]] = None


# @Route("/{version}/account", "POST")
# @Api(Description="This API endpoint allows users to create a new CodeMash account.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateAccount(RequestBase, IReturn[CreateAccountResponse]):
    """
    This API endpoint allows users to create a new CodeMash account.
    """

    # @ApiMember(DataType="string", Description="Display name of the account holder", IsRequired=true, Name="DisplayName", ParameterType="form")
    display_name: Optional[str] = None
    """
    Display name of the account holder
    """


    # @ApiMember(DataType="string", Description="Real email of account holder", IsRequired=true, Name="Email", ParameterType="form")
    email: Optional[str] = None
    """
    Real email of account holder
    """


    # @ApiMember(DataType="string", Description="Set password for a new account", Format="password", IsRequired=true, Name="Password", ParameterType="form")
    password: Optional[str] = None
    """
    Set password for a new account
    """


# @Route("/{version}/account/collaborators", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountCollaborators(RequestBase, IReturn[GetAccountCollaboratorsResponse]):
    include_account_owner: bool = False
    user_should_have_push_device: bool = False
    project_id: Optional[str] = None
    user_ids: Optional[List[str]] = None
    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/account/team/member/invite", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendInviteToTeamMember(RequestBase, IReturn[EmptyResponse]):
    email: Optional[str] = None


# @Route("/{version}/account/licenses", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLicenses(RequestBase, IReturn[GetLicensesResponse]):
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
class AccountProfileUpdated:
    display_name: Optional[DisplayName] = None
    billing_email: Optional[EmailAddress] = None
    operations_email: Optional[EmailAddress] = None
    security_email: Optional[EmailAddress] = None


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
class AccountVerified:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountBlocked:
    pass


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
class ProjectCreated:
    id: Optional[ProjectId] = None
    name: Optional[ProjectName] = None
    database_integration_id: Optional[IntegrationId] = None
    regions: Optional[List[ProjectRegion]] = None
    description: Optional[str] = None


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
class ProjectDeleted:
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
class ProjectEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectCommunicationSet:
    project_communication: Optional[ProjectCommunication] = None


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


# @Route("/{version}/membership/disable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableMembership(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/membership/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableMembership(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/notifications/user/preferences", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetUserNotificationPreferences(CodeMashRequestBase, IReturn[GetUserEmailPreferencesResponse]):
    user_id: Optional[str] = None


# @Route("/{version}/notifications/user/preferences", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateUserNotificationsPreferences(CodeMashRequestBase, IReturn[EmptyResponse]):
    user_id: Optional[str] = None
    block_all_marketing_messages: bool = False
    subscribed_to_tags: Optional[Dict[str, HashSet[str]]] = None


# @Route("/{version}/membership/triggers/{triggerId}", "DELETE")
# @Route("/{version}/triggers", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteMembershipTrigger(DeleteTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/membership/triggers/{triggerId}/disable", "PATCH")
# @Route("/{version}/triggers/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableMembershipTrigger(DisableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/membership/triggers/{triggerId}/enable", "PATCH")
# @Route("/{version}/triggers/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableMembershipTrigger(EnableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/membership/triggers/{id}", "GET")
# @Api(Description="Gets membership trigger by specified Id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipTrigger(GetTrigger, IReturn[GetMembershipTriggerResponse]):
    """
    Gets membership trigger by specified Id
    """

    pass


# @Route("/{version}/membership/triggers", "GET")
# @Api(Description="Gets membership triggers")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipTriggers(GetTriggers, IReturn[GetMembershipTriggersResponse]):
    """
    Gets membership triggers
    """

    pass


# @Route("/{version}/membership/triggers", "POST")
# @Route("/{version}/triggers", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveMembershipTrigger(SaveTrigger, IReturn[IdResponse]):
    pass


# @Route("/{version}/membership/roles", "POST")
# @Api(Description="Create a new custom role for project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateRole(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Create a new custom role for project.
    """

    role_name: Optional[str] = None
    description: Optional[str] = None
    policies: Optional[List[str]] = None


# @Route("/{version}/membership/roles", "DELETE")
# @Api(Description="Deletes custom role from project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteRole(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Deletes custom role from project.
    """

    id: Optional[str] = None


# @Route("/{version}/membership/roles/{Id}", "GET")
# @Api(Description="Gets project role details.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetRole(CodeMashRequestBase, IReturn[GetRoleResponse]):
    """
    Gets project role details.
    """

    id: Optional[str] = None


# @Route("/{version}/membership/roles", "GET")
# @Api(Description="Gets project roles.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetRoles(CodeMashRequestBase, IReturn[GetRolesResponse]):
    """
    Gets project roles.
    """

    pass


# @Route("/{version}/membership/roles", "PATCH")
# @Api(Description="Updates role policies")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateRolePolicies(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates role policies
    """

    id: Optional[str] = None
    role_name: Optional[str] = None
    description: Optional[str] = None
    policies: Optional[List[str]] = None


# @Route("/{version}/membership/policies", "POST")
# @Api(Description="Create a new custom policy for project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreatePolicy(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Create a new custom policy for project.
    """

    policy_name: Optional[str] = None
    description: Optional[str] = None
    policy_document_json: Optional[str] = None


# @Route("/{version}/membership/policies", "DELETE")
# @Api(Description="Deletes custom policy from project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePolicy(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Deletes custom policy from project.
    """

    id: Optional[str] = None


# @Route("/{version}/membership/policies/{Id}", "GET")
# @Api(Description="Gets project policy details.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPolicy(CodeMashRequestBase, IReturn[GetPolicyResponse]):
    """
    Gets project policy details.
    """

    id: Optional[str] = None


# @Route("/{version}/membership/policies", "GET")
# @Api(Description="Gets project policies.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPolicies(CodeMashRequestBase, IReturn[GetPoliciesResponse]):
    """
    Gets project policies.
    """

    pass


# @Route("/{version}/membership/policies", "PUT")
# @Api(Description="Updates a custom policy for project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdatePolicy(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Updates a custom policy for project.
    """

    id: Optional[str] = None
    policy_name: Optional[str] = None
    description: Optional[str] = None
    policy_document_json: Optional[str] = None


# @Route("/{version}/membership/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteMembershipIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/membership/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableMembershipIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/membership/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableMembershipIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/membership/integrations/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipIntegration(CodeMashRequestBase, IReturn[GetMembershipIntegrationResponse]):
    id: Optional[str] = None


# @Route("/{version}/membership/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipIntegrations(CodeMashListPaginationRequestBase, IReturn[GetMembershipIntegrationsResponse]):
    pass


# @Route("/{version}/membership/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveMembershipIntegration(CodeMashRequestBase):
    integration: Optional[MembershipIntegrationRequest] = None


# @Route("/{version}/membership/integrations/{Id}/default", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetMembershipIntegrationAsDefaultRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationSaved:
    integration: Optional[MembershipIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationDeleted:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationSetAsDefault:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationEnabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationDisabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipEstablished:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipDisabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetUserRegistersAsRole:
    project_id: Optional[ProjectId] = None
    role: Optional[RoleName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PolicyCreated:
    policy: Optional[MembershipPolicy] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PolicyUpdated:
    policy: Optional[MembershipPolicy] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PolicyDeleted:
    policy_id: Optional[PolicyId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleCreated:
    role: Optional[MembershipRole] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleUpdated:
    role: Optional[MembershipRole] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RoleDeleted:
    role_id: Optional[RoleId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerSaved:
    trigger: Optional[MembershipTrigger] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerEnabled(TriggerByIdEventBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerDisabled(TriggerByIdEventBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerDeleted(TriggerByIdEventBase):
    pass


# @Route("/{version}/database/disable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableDatabase(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/database/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableDatabase(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/database/schemas/triggers/{triggerId}", "DELETE")
# @Route("/{version}/triggers", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteSchemaTrigger(DeleteTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/database/schemas/triggers/{triggerId}/disable", "PATCH")
# @Route("/{version}/triggers/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableSchemaTrigger(DisableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/database/schemas/triggers/{triggerId}/enable", "PATCH")
# @Route("/{version}/triggers/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableSchemaTrigger(EnableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/database/schemas/triggers/{id}", "GET")
# @Api(Description="Gets database trigger by specified Id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchemaTrigger(GetTrigger, IReturn[GetSchemaTriggerResponse]):
    """
    Gets database trigger by specified Id
    """

    pass


# @Route("/{version}/database/schemas/triggers", "GET")
# @Api(Description="Gets database triggers")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchemaTriggers(GetTriggers, IReturn[GetSchemaTriggersResponse]):
    """
    Gets database triggers
    """

    schema_id: Optional[str] = None


# @Route("/{version}/database/schemas/triggers", "POST")
# @Route("/{version}/triggers", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveSchemaTrigger(SaveTrigger, IReturn[IdResponse]):
    pass


# @Route("/{version}/database/taxonomies/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseTaxonomyRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/taxonomies/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomy(CodeMashRequestBase, IReturn[GetDatabaseTaxonomyResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/taxonomies", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomies(CodeMashListPaginationRequestBase, IReturn[GetDatabaseTaxonomiesResponse]):
    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/taxonomies", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseTaxonomyRequest(CodeMashRequestBase, IReturn[IdResponse]):
    view_id: Optional[str] = None
    taxonomy_name: Optional[str] = None
    description: Optional[str] = None
    terms_meta_data_schema: Optional[str] = None
    terms_meta_visual_schema: Optional[str] = None
    parent_id: Optional[str] = None
    dependencies: Optional[List[str]] = None


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseTaxonomyTermRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    taxonomy_id: Optional[str] = None
    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/many", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteManyDatabaseTaxonomyTermsRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    taxonomy_id: Optional[str] = None
    database_integration_id: Optional[str] = None
    filter: Optional[str] = None


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomyTermRequest(CodeMashRequestBase, IReturn[GetDatabaseTaxonomyTermResponse]):
    taxonomy_id: Optional[str] = None
    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseTaxonomyTermRequest(CodeMashRequestBase, IReturn[IdResponse]):
    taxonomy_id: Optional[str] = None
    database_integration_id: Optional[str] = None
    document: Optional[str] = None


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateDatabaseTaxonomyTermRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    taxonomy_id: Optional[str] = None
    id: Optional[str] = None
    database_integration_id: Optional[str] = None
    update: Optional[str] = None


# @Route("/{version}/database/schemas/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseSchemaRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/schemas/{Id}/draft", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiscardDatabaseSchemaDraftRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/schemas/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchema(CodeMashRequestBase, IReturn[GetDatabaseSchemaResponse]):
    id: Optional[str] = None
    # @ApiMember(DataType="integer", Name="version", ParameterType="query")
    schema_version: Optional[int] = None


# @Route("/{version}/database/schemas", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemas(CodeMashListPaginationRequestBase, IReturn[GetDatabaseSchemasResponse]):
    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/schemas/{Id}/draft", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaDraft(CodeMashRequestBase, IReturn[GetDatabaseSchemaDraftResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/schemas/{Id}/versions/diff", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaVersionDiff(CodeMashRequestBase, IReturn[GetDatabaseSchemaVersionDiffResponse]):
    id: Optional[str] = None
    from_version: int = 0
    to_version: int = 0


# @Route("/{version}/database/schemas/{Id}/versions", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaVersions(CodeMashRequestBase, IReturn[GetDatabaseSchemaVersionsResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/schemas/{Id}/publish", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublishDatabaseSchemaRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/schemas/{Id}/rename", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RenameDatabaseSchemaRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None
    title: Optional[str] = None
    rename_unique_name: bool = False


# @Route("/{version}/database/schemas", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseSchemaRequest(CodeMashRequestBase, IReturn[IdResponse]):
    view_id: Optional[str] = None
    schema_name: Optional[str] = None
    data_schema: Optional[str] = None
    visual_schema: Optional[str] = None
    settings: Optional[SchemaSettingsDto] = None


# @Route("/{version}/database/schemas/{Id}/draft", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateDatabaseSchemaDraftRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None
    data_schema: Optional[str] = None
    visual_schema: Optional[str] = None


# @Route("/{version}/database/schemas/{Id}/settings", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateDatabaseSchemaSettingsRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    settings: Optional[SchemaSettingsDto] = None


# @Route("/{version}/database/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableDatabaseIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableDatabaseIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/integrations/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseIntegration(CodeMashRequestBase, IReturn[GetDatabaseIntegrationResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseIntegrations(CodeMashListPaginationRequestBase, IReturn[GetDatabaseIntegrationsResponse]):
    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseIntegration(CodeMashRequestBase):
    integration: Optional[DatabaseIntegrationRequest] = None


# @Route("/{version}/database/integrations/{Id}/default", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetDatabaseIntegrationAsDefaultRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/aggregates/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseAggregateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None
    schema_id: Optional[str] = None


# @Route("/{version}/database/aggregates/{Id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseAggregate(CodeMashRequestBase, IReturn[GetDatabaseAggregateResponse]):
    id: Optional[str] = None
    schema_id: Optional[str] = None


# @Route("/{version}/database/aggregates", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseAggregates(CodeMashListPaginationRequestBase, IReturn[GetDatabaseAggregatesResponse]):
    schema_id: Optional[str] = None
    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/aggregates", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseAggregateRequest(CodeMashRequestBase, IReturn[IdResponse]):
    view_id: Optional[str] = None
    schema_id: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    pipeline: Optional[str] = None


# @Route("/{version}/database/aggregates/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestDatabaseAggregateRequest(CodeMashRequestBase, IReturn[TestDatabaseAggregateResponse]):
    database_integration_id: Optional[str] = None
    collection_name: Optional[str] = None
    pipeline: Optional[str] = None
    tokens: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAggregateCreated:
    aggregate: Optional[MongoDbAggregate] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAggregateUpdated:
    aggregate: Optional[MongoDbAggregate] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAggregateDeleted:
    schema_id: Optional[SchemaId] = None
    id: Optional[MongoDbAggregateId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseEstablished:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseDisabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationSaved:
    integration: Optional[DatabaseIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationSetAsDefault:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationDeleted:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationEnabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationDisabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaCreated:
    schema: Optional[Schema] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDraftUpdated:
    id: Optional[SchemaId] = None
    draft: Optional[SchemaDraft] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDraftDiscarded:
    id: Optional[SchemaId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaVersionPublished:
    id: Optional[SchemaId] = None
    version: Optional[PublishedSchemaVersion] = None
    diff: Optional[SchemaDiff] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaSettingsUpdated:
    id: Optional[SchemaId] = None
    settings: Optional[SchemaSettings] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDeleted:
    id: Optional[SchemaId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaRenamed:
    schema_id: Optional[SchemaId] = None
    new_name: Optional[SchemaName] = None
    rename_unique_name: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDataCleared:
    id: Optional[SchemaId] = None
    integrations: List[IntegrationId] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomyCreated:
    taxonomy: Optional[Taxonomy] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomyUpdated:
    taxonomy: Optional[Taxonomy] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomyDeleted:
    taxonomy_id: Optional[TaxonomyId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TaxonomyDataCleared:
    taxonomy_id: Optional[TaxonomyId] = None
    integrations: List[IntegrationId] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerSaved:
    trigger: Optional[SchemaTrigger] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerEnabled(TriggerByIdEventBase):
    schema_id: Optional[SchemaId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerDisabled(TriggerByIdEventBase):
    schema_id: Optional[SchemaId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerDeleted(TriggerByIdEventBase):
    schema_id: Optional[SchemaId] = None


# @Route("/{version}/files/disable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableFiles(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/files/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableFiles(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/files/triggers/{triggerId}", "DELETE")
# @Route("/{version}/triggers", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteFilesTrigger(DeleteTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/files/triggers/{triggerId}/disable", "PATCH")
# @Route("/{version}/triggers/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableFilesTrigger(DisableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/files/triggers/{triggerId}/enable", "PATCH")
# @Route("/{version}/triggers/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableFilesTrigger(EnableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/files/triggers/{id}", "GET")
# @Api(Description="Gets files trigger by specified Id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesTrigger(GetTrigger, IReturn[GetFilesTriggerResponse]):
    """
    Gets files trigger by specified Id
    """

    pass


# @Route("/{version}/files/triggers", "GET")
# @Api(Description="Gets files triggers")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesTriggers(GetTriggers, IReturn[GetFilesTriggersResponse]):
    """
    Gets files triggers
    """

    pass


# @Route("/{version}/files/triggers", "POST")
# @Route("/{version}/triggers", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveFilesTrigger(SaveTrigger, IReturn[IdResponse]):
    pass


# @Route("/{version}/files/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteFilesIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/files/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableFilesIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/files/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableFilesIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/files/integrations/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesIntegration(CodeMashRequestBase, IReturn[GetFilesIntegrationResponse]):
    id: Optional[str] = None


# @Route("/{version}/files/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesIntegrations(CodeMashListPaginationRequestBase, IReturn[GetFilesIntegrationsResponse]):
    pass


# @Route("/{version}/files/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveFilesIntegration(CodeMashRequestBase):
    integration: Optional[FilesIntegrationRequest] = None


# @Route("/{version}/files/integrations/{Id}/default", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetFilesIntegrationAsDefaultRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/disable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableEmail(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/notifications/email/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableEmail(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/notifications/email/templates/attachments", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AttachFileToTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    language: Optional[str] = None
    template_id: Optional[str] = None
    file_ref: Optional[FileResourceRefDto] = None


# @Route("/{version}/notifications/email/templates", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateEmailTemplateRequest(SaveEmailTemplate, IReturn[IdResponse]):
    pass


# @Route("/{version}/notifications/email/templates/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEmailTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/templates/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplate(CodeMashRequestBase, IReturn[GetEmailTemplateResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/templates", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplates(CodeMashListPaginationRequestBase, IReturn[GetEmailTemplatesResponse]):
    show_archived: Optional[bool] = None
    template_id: Optional[str] = None


# @Route("/{version}/notifications/email/templates/mjml", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMjml(CodeMashRequestBase, IReturn[GetHtmlFromMjmlResponse]):
    code: Optional[str] = None
    tokens: Optional[List[TokenMappingDto]] = None
    is_for_preview: bool = False


# @Route("/{version}/notifications/email/system-templates/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSystemEmailTemplate(CodeMashRequestBase, IReturn[GetSystemEmailTemplateResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/system-templates", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSystemEmailTemplates(CodeMashListPaginationRequestBase, IReturn[GetSystemEmailTemplatesResponse]):
    group_tags: Optional[List[str]] = None
    themes: Optional[List[str]] = None
    communication_channel: Optional[CommunicationChannel] = None
    for_trigger: Optional[TriggerType] = None


# @Route("/{version}/notifications/email/templates/{id}/tokens", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplateAvailableTokens(CodeMashRequestBase, IReturn[GetEmailTemplateAvailableTokensResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/templates", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateEmailTemplateRequest(SaveEmailTemplate, IReturn[EmptyResponse]):
    view_id: Optional[str] = None


# @Route("/{version}/notifications/email/signatures/{id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEmailSignature(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/signatures/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailSignature(CodeMashRequestBase, IReturn[GetEmailSignatureResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/signatures", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailSignatures(CodeMashListPaginationRequestBase, IReturn[GetEmailSignaturesResponse]):
    pass


# @Route("/{version}/notifications/email/signatures", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailSignatureRequest(CodeMashRequestBase, IReturn[IdResponse]):
    view_id: Optional[str] = None
    display_name: Optional[str] = None
    translations: List[TranslationDto] = field(default_factory=list)


# @Route("/{version}/notifications/email/settings", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailSettings(CodeMashRequestBase, IReturn[GetEmailSettingsResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/integrations/confirm-human-delivery", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmEmailIntegrationHumanDeliveryRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    integration_id: Optional[str] = None


# @Route("/{version}/notifications/email/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEmailIntegration(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableEmailIntegration(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableEmailIntegration(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/integrations/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailIntegration(CodeMashRequestBase, IReturn[GetEmailIntegrationResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailIntegrations(CodeMashListPaginationRequestBase, IReturn[GetEmailIntegrationsResponse]):
    pass


# @Route("/{version}/notifications/email/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailIntegration(CodeMashRequestBase):
    integration: Optional[EmailIntegrationRequest] = None


# @Route("/{version}/notifications/email/integrations/{Id}/default", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetEmailsIntegrationAsDefault(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/integrations/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestEmailIntegration(CodeMashRequestBase, IReturn[TestEmailIntegrationResponse]):
    integration_id: Optional[str] = None
    to: Optional[str] = None


# @Route("/{version}/notifications/email/templates/{Id}/archive", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ArchiveEmailTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/templates/{Id}/clone", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CloneEmailTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/templates/{Id}/unarchive", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnArchiveEmailTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/footers/{id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEmailFooter(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/footers/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailFooter(CodeMashRequestBase, IReturn[GetEmailFooterResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/email/footers", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailFooters(CodeMashListPaginationRequestBase, IReturn[GetEmailFootersResponse]):
    pass


# @Route("/{version}/notifications/email/footers", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailFooterRequest(CodeMashRequestBase, IReturn[IdResponse]):
    view_id: Optional[str] = None
    display_name: Optional[str] = None
    translations: List[TranslationDto] = field(default_factory=list)


# @Route("/{version}/email/one-click-unsubscribe", "POST")
# @Api(Description="This endpoint implements the RFC 8058 one-click unsubscribe flow used by mailbox providers.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OneClickUnsubscribeRequest(RequestBase, IReturn[EmptyResponse]):
    """
    This endpoint implements the RFC 8058 one-click unsubscribe flow used by mailbox providers.
    """

    # @ApiMember(Description="Encrypted unsubscribe token. The campaign batcher embedded this value in the List-Unsubscribe header.", IsRequired=true, Name="token", ParameterType="query")
    token: Optional[str] = None
    """
    Encrypted unsubscribe token. The campaign batcher embedded this value in the List-Unsubscribe header.
    """


# @Route("/{version}/notifications/email/campaigns", "POST")
# @Api(Description="Create email campaign")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateEmailCampaignRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Create email campaign
    """

    campaign: Optional[EmailCampaignRequest] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/notifications/email/campaigns/{Id}", "DELETE")
# @Api(Description="Deletes emails campaign from queue")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEmailCampaignRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Deletes emails campaign from queue
    """

    pass


# @Route("/{version}/notifications/email/campaigns/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaign(CodeMashRequestBase, IReturn[GetEmailCampaignResponse]):
    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/notifications/email/campaigns", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaigns(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignsResponse]):
    database_integration_id: Optional[str] = None
    campaign_id: Optional[str] = None
    email_address: Optional[str] = None
    template_id: Optional[str] = None
    from_: Optional[int] = field(metadata=config(field_name='from'), default=None)
    to: Optional[int] = None


# @Route("/{version}/notifications/email/campaigns/{id}/batches", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignBatches(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignBatchesResponse]):
    id: Optional[str] = None
    database_integration_id: Optional[str] = None
    batch_id: Optional[str] = None
    email_address: Optional[str] = None


# @Route("/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignBatchNotification(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignBatchNotificationResponse]):
    id: Optional[str] = None
    batch_id: Optional[str] = None
    notification_id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/notifications/email/campaigns/{id}/batches/{batchId}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignBatchNotifications(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignBatchNotificationsResponse]):
    id: Optional[str] = None
    batch_id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/notifications/email/campaigns/{id}/stats", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignStatistics(CodeMashRequestBase, IReturn[GetEmailCampaignStatisticsResponse]):
    id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/notifications/email/preview", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PreviewEmailNotification(RequestBase, IReturn[PreviewEmailNotificationResponse]):
    hash: Optional[str] = None


# @Route("/{version}/notifications/emails/campaigns/{campaignId}/messages/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignMessage(CodeMashRequestBase, IReturn[GetEmailCampaignMessageResponse]):
    campaign_id: Optional[str] = None
    campaign_batch_id: Optional[str] = None
    notification_id: Optional[str] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/notifications/emails/campaigns/{campaignId}/messages", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignMessagesRequest(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignMessagesResponse]):
    campaign_id: Optional[str] = None
    campaign_batch_id: Optional[str] = None
    database_integration_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailServiceEstablished:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailServiceEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailServiceDisabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailFooterSaved:
    id: Optional[EmailFooterId] = None
    name: Optional[DisplayName] = None
    translations: List[MessageTranslation[TemplateCode]] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailFooterDeleted:
    id: Optional[EmailFooterId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationSaved:
    integration: Optional[EmailIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationHumanDeliveryConfirmed:
    id: Optional[IntegrationId] = None
    confirmed_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationSetAsDefault:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationDeleted:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationEnabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationDisabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSignatureSaved:
    id: Optional[EmailSignatureId] = None
    name: Optional[DisplayName] = None
    translations: List[MessageTranslation[TemplateCode]] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSignatureDeleted:
    id: Optional[EmailSignatureId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateCreated:
    template_id: Optional[TemplateId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[EmailMessageContent]] = field(default_factory=list)
    channel: Optional[CommunicationChannel] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    language_agnostic_attachments: Optional[List[FileResourceRef]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateUpdated:
    template_id: Optional[TemplateId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[EmailMessageContent]] = field(default_factory=list)
    channel: Optional[CommunicationChannel] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    language_agnostic_attachments: Optional[List[FileResourceRef]] = None
    attachments_to_be_deleted: Optional[List[FileResourceRef]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateDeleted:
    template_id: Optional[TemplateId] = None
    files_to_be_deleted: Optional[List[FileResourceRef]] = None
    file_integration_id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateArchived:
    template_id: Optional[TemplateId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateUnArchived:
    template_id: Optional[TemplateId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationSaved:
    integration: Optional[CodeIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationHumanDeliveryConfirmed:
    id: Optional[IntegrationId] = None
    confirmed_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationSetAsDefault:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationDeleted:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationEnabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationDisabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationSaved:
    integration: Optional[MarketplaceIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationDeleted:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationEnabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationDisabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationSecretsConfigured:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationSecretsConfigurationFailed:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionBindingSaved:
    binding: Optional[MarketplaceFunctionBinding] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionBindingDeleted:
    integration_id: Optional[IntegrationId] = None
    binding_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionBindingEnabled:
    integration_id: Optional[IntegrationId] = None
    binding_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionBindingDisabled:
    integration_id: Optional[IntegrationId] = None
    binding_id: Optional[str] = None


# @Route("/{version}/notifications/push/disable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePush(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/notifications/push/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePush(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/notifications/push/templates/{Id}/archive", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ArchivePushTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/templates/{Id}/clone", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ClonePushTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/templates", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreatePushTemplateRequest(SavePushTemplate, IReturn[IdResponse]):
    pass


# @Route("/{version}/notifications/push/templates/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePushTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/templates/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushTemplate(CodeMashRequestBase, IReturn[GetPushTemplateResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/templates", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushTemplates(CodeMashListPaginationRequestBase, IReturn[GetPushTemplatesResponse]):
    show_archived: Optional[bool] = None
    template_id: Optional[str] = None


# @Route("/{version}/notifications/push/templates/{id}/tokens", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushMessageContentTokens(CodeMashRequestBase, IReturn[GetPushMessageContentTokensResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/templates/{Id}/unarchive", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnArchivePushTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/templates", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdatePushTemplateRequest(SavePushTemplate, IReturn[EmptyResponse]):
    view_id: Optional[str] = None


# @Route("/{version}/notifications/push/integrations/confirm-human-delivery", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmPushIntegrationHumanDeliveryRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    integration_id: Optional[str] = None


# @Route("/{version}/notifications/push/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePushIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePushIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePushIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/integrations/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushIntegration(CodeMashRequestBase, IReturn[GetPushIntegrationResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushIntegrations(CodeMashListPaginationRequestBase, IReturn[GetPushIntegrationsResponse]):
    pass


# @Route("/{version}/notifications/push/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePushIntegration(CodeMashRequestBase):
    integration: Optional[PushIntegrationRequest] = None


# @Route("/{version}/notifications/push/integrations/{Id}/default", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetPushIntegrationAsDefaultRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/notifications/push/integrations/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestPushIntegration(CodeMashRequestBase, IReturn[TestEmailIntegrationResponse]):
    integration_id: Optional[str] = None
    test_token: Optional[str] = None
    delivery_family: Optional[str] = None


# @Route("/{version}/notifications/push/integrations/app/request", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RegisterCodeMashAppPushIntegration(CodeMashRequestBase, IReturn[EmptyResponse], IHasAccountId):
    account_id: Optional[str] = None
    user_id: Optional[str] = None
    request_id: Optional[str] = None
    pin: int = 0
    valid_till: datetime.datetime = datetime.datetime(1, 1, 1)
    public_key: Optional[str] = None


# @Route("/{version}/notifications/push/devices", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RegisterDevice(RequestBase, IReturn[IdResponse], IHasProjectId):
    push_device_dto: Optional[PushDeviceDto] = None
    user_id: Optional[str] = None
    project_id: Optional[str] = None
    account_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationSaved:
    integration: Optional[PushIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationHumanDeliveryConfirmed:
    id: Optional[IntegrationId] = None
    confirmed_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationSetAsDefault:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationDeleted:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationEnabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationDisabled:
    id: Optional[IntegrationId] = None


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
class PushModuleTagSaved:
    tag: Optional[TagDefinition] = None
    communication_channel: Optional[CommunicationChannel] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushModuleTagDeleted:
    tag: Optional[Tag] = None
    communication_channel: Optional[CommunicationChannel] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateCreated:
    template_id: Optional[TemplateId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[PushMessageContent]] = field(default_factory=list)
    channel: Optional[CommunicationChannel] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateUpdated:
    template_id: Optional[TemplateId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[PushMessageContent]] = field(default_factory=list)
    channel: Optional[CommunicationChannel] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateDeleted:
    template_id: Optional[TemplateId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateArchived:
    template_id: Optional[TemplateId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateUnArchived:
    template_id: Optional[TemplateId] = None


# @Route("/{version}/payments/disable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePayments(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/payments/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePayments(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/payments/triggers/{triggerId}", "DELETE")
# @Route("/{version}/triggers", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePaymentsTrigger(DeleteTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/payments/triggers/{triggerId}/disable", "PATCH")
# @Route("/{version}/triggers/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePaymentsTrigger(DisableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/payments/triggers/{triggerId}/enable", "PATCH")
# @Route("/{version}/triggers/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePaymentsTrigger(EnableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/payments/triggers/{id}", "GET")
# @Api(Description="Gets payments trigger by specified Id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsTrigger(GetTrigger, IReturn[GetPaymentsTriggerResponse]):
    """
    Gets payments trigger by specified Id
    """

    pass


# @Route("/{version}/payments/triggers", "GET")
# @Api(Description="Gets payments triggers")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsTriggers(GetTriggers, IReturn[GetPaymentsTriggersResponse]):
    """
    Gets payments triggers
    """

    pass


# @Route("/{version}/payments/triggers", "POST")
# @Route("/{version}/triggers", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePaymentsTrigger(SaveTrigger, IReturn[IdResponse]):
    pass


# @Route("/{version}/payments/integrations/confirm-human-delivery", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmPaymentsIntegrationHumanDeliveryRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    integration_id: Optional[str] = None


# @Route("/{version}/payments/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePaymentsIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/payments/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePaymentsIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/payments/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePaymentsIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/payments/integrations/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsIntegration(CodeMashRequestBase, IReturn[GetPaymentsIntegrationResponse]):
    id: Optional[str] = None


# @Route("/{version}/payments/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsIntegrations(CodeMashListPaginationRequestBase, IReturn[GetPaymentsIntegrationsResponse]):
    pass


# @Route("/{version}/payments/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePaymentsIntegration(CodeMashRequestBase):
    integration: Optional[PaymentIntegrationRequest] = None


# @Route("/{version}/payments/integrations/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestPaymentsIntegration(CodeMashRequestBase, IReturn[TestPaymentsIntegrationResponse]):
    integration_id: Optional[str] = None


# @Route("/{version}/logs/disable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableLogging(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/logs/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableLogging(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/logs/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteLoggingIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/logs/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableLoggingIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/logs/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableLoggingIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/logs/integrations/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLoggingIntegration(CodeMashRequestBase, IReturn[GetLoggingIntegrationResponse]):
    id: Optional[str] = None


# @Route("/{version}/logs/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLoggingIntegrations(CodeMashListPaginationRequestBase, IReturn[GetLoggingIntegrationsResponse]):
    pass


# @Route("/{version}/logs/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveLoggingIntegration(CodeMashRequestBase):
    integration: Optional[LoggingIntegrationRequest] = None


# @Route("/{version}/logs/integrations/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestLoggingIntegration(CodeMashRequestBase, IReturn[TestLoggingIntegrationResponse]):
    integration_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationSaved:
    integration: Optional[LoggingIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationDeleted:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationEnabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationDisabled:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingEstablished:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingDisabled:
    pass


# @Route("/{version}/account/chat/complete", "POST")
# @Api(Description="Gets account info.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AskChatRequest(RequestBase, IReturn[AskChatResponse]):
    """
    Gets account info.
    """

    prompt: Optional[str] = None


# @Route("/{version}/ai/integrations/llms/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteLlmIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/ai/integrations/llms/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableLlmIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/ai/integrations/llms/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableLlmIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/ai/integrations/llms/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLlmIntegration(CodeMashRequestBase, IReturn[GetLlmIntegrationResponse]):
    id: Optional[str] = None


# @Route("/{version}/ai/integrations/llms/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLlmIntegrations(CodeMashListPaginationRequestBase, IReturn[GetLlmIntegrationsResponse]):
    pass


# @Route("/{version}/ai/integrations/llms/", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveLlmIntegration(CodeMashRequestBase):
    integration: Optional[LlmIntegrationRequest] = None


# @Route("/{version}/ai/integrations/llms/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestLlmIntegration(CodeMashRequestBase, IReturn[TestLlmIntegrationResponse]):
    integration_id: Optional[str] = None


# @Route("/{version}/ai/integrations/mcp/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteMcpIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/ai/integrations/mcp/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableMcpIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/ai/integrations/mcp/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableMcpIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/ai/integrations/mcp/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMcpIntegration(CodeMashRequestBase, IReturn[GetMcpIntegrationResponse]):
    id: Optional[str] = None


# @Route("/{version}/ai/integrations/mcp/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMcpIntegrations(CodeMashListPaginationRequestBase, IReturn[GetMcpIntegrationsResponse]):
    pass


# @Route("/{version}/ai/integrations/mcp/", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveMcpIntegration(CodeMashRequestBase):
    integration: Optional[McpIntegrationRequest] = None


# @Route("/{version}/ai/integrations/mcp/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestMcpIntegration(CodeMashRequestBase, IReturn[TestLlmIntegrationResponse]):
    integration_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegrationSaved:
    integration: Optional[WebhookIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegrationExtraHeadersChanged:
    id: Optional[IntegrationId] = None
    extra_headers: Optional[IReadOnlyDictionary[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegrationSecretsConfigured:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegrationSecretsConfigurationFailed:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegrationSecretsCleared:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookDestinationSaved:
    integration_id: Optional[IntegrationId] = None
    destination: Optional[WebhookDestination] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookDestinationRemoved:
    integration_id: Optional[IntegrationId] = None
    destination_id: Optional[WebhookDestinationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookDestinationEnabled:
    integration_id: Optional[IntegrationId] = None
    destination_id: Optional[WebhookDestinationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookDestinationDisabled:
    integration_id: Optional[IntegrationId] = None
    destination_id: Optional[WebhookDestinationId] = None


# @Route("/{version}/webhooks/integration", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetWebhookIntegration(CodeMashRequestBase, IReturn[GetWebhookIntegrationResponse]):
    pass


# @Route("/{version}/webhooks/integration/secret", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RevealWebhookIntegrationSecretRequest(CodeMashRequestBase, IReturn[RevealWebhookIntegrationSecretResponse]):
    pass


# @Route("/{version}/webhooks/integration/secret/rotate", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RotateWebhookIntegrationSecretRequest(CodeMashRequestBase, IReturn[RotateWebhookIntegrationSecretResponse]):
    pass


# @Route("/{version}/webhooks/integration/extra-headers", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateWebhookIntegrationExtraHeadersRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    extra_headers: Optional[Dict[str, str]] = None


# @Route("/{version}/webhooks/destinations/{DestinationId}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableWebhookDestinationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    destination_id: Optional[str] = None


# @Route("/{version}/webhooks/destinations/{DestinationId}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableWebhookDestinationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    destination_id: Optional[str] = None


# @Route("/{version}/webhooks/destinations/{DestinationId}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveWebhookDestinationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    destination_id: Optional[str] = None


# @Route("/{version}/webhooks/destinations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveWebhookDestinationRequest(CodeMashRequestBase, IReturn[SaveWebhookDestinationResponse]):
    destination_id: Optional[str] = None
    destination_name: Optional[str] = None
    endpoint_url: Optional[str] = None
    selected_events: List[str] = field(default_factory=list)
    extra_headers: Optional[Dict[str, str]] = None
    is_enabled: bool = False


# @Route("/{version}/scheduler/disable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableScheduler(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/scheduler/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableScheduler(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/scheduler/tasks/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteSchedulerTask(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/scheduler/tasks/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableSchedulerTask(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/scheduler/tasks/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableSchedulerTask(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None


# @Route("/{version}/scheduler/tasks/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchedulerTask(CodeMashRequestBase, IReturn[GetSchedulerTaskResponse]):
    id: Optional[str] = None


# @Route("/{version}/scheduler/tasks", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchedulerTasks(CodeMashListPaginationRequestBase, IReturn[GetSchedulerTasksResponse]):
    type: Optional[SchedulerTaskType] = None
    enabled: Optional[bool] = None


# @Route("/{version}/scheduler/tasks", "POST")
# @Api(Description="Save scheduled task")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveSchedulerTaskRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Save scheduled task
    """

    task_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    cron: Optional[str] = None
    initiator_user_id: Optional[str] = None
    is_enabled: bool = False
    stop_on_error: bool = False
    task: Optional[SchedulerTaskRequest] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerDisabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerTaskSaved:
    task: Optional[SchedulerTask] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerTaskEnabled:
    task_id: Optional[TaskId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerTaskDisabled:
    task_id: Optional[TaskId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerTaskDeleted:
    task_id: Optional[TaskId] = None

