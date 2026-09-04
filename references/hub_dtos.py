""" Options:
Date: 2026-09-04 14:55:41
Version: 10.08
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
    FAKE = 'Fake'


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
    provider: Optional[EmailProvider] = None
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
    provider: Optional[EmailProvider] = None
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
    provider: Optional[EmailProvider] = None
    api_key: Optional[str] = None


class MailGunRegion(str, Enum):
    US = 'Us'
    EU = 'Eu'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MailGunEmailIntegrationRequest(EmailIntegrationRequest):
    provider: Optional[EmailProvider] = None
    domain: Optional[str] = None
    api_key: Optional[str] = None
    webhook_signing_key: Optional[str] = None
    region: Optional[MailGunRegion] = None


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
    validation_integration_id: Optional[str] = None
    language: Optional[str] = None
    initiator_id: Optional[str] = None
    notes: Optional[str] = None
    mapped_tokens: Optional[List[TokenMappingDto]] = None
    campaign_time: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToAllUsersDeliverySettingsRequest(EmailCampaignRequest):
    source: Optional[EmailCampaignRecipientsSourceTypes] = None
    roles_names: Optional[List[str]] = None
    user_tags: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToAccountUsersDeliverySettingsRequest(EmailCampaignRequest):
    source: Optional[EmailCampaignRecipientsSourceTypes] = None
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
    source: Optional[EmailCampaignRecipientsSourceTypes] = None
    fields: List[str] = field(default_factory=list)
    schema_name: Optional[str] = None
    field_type: Optional[CollectionEmailCampaignRecipientField] = None
    role_names: Optional[List[str]] = None
    languages: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToEmailsDeliverySettingsRequest(EmailCampaignRequest):
    source: Optional[EmailCampaignRecipientsSourceTypes] = None
    recipients: List[str] = field(default_factory=list)
    recipients_cc: Optional[List[str]] = None
    recipients_bcc: Optional[List[str]] = None
    single_email_strategy: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToUsersDeliverySettingsRequest(EmailCampaignRequest):
    source: Optional[EmailCampaignRecipientsSourceTypes] = None
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
    SSE_CALL = 'SseCall'
    MARKETPLACE = 'Marketplace'


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
    ON_USER_CREATED = 'OnUserCreated'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerRequest(SaveTriggerRequest):
    type: Optional[TriggerType] = None
    when: Optional[MembershipTriggerType] = None


class SchemaTriggerType(str, Enum):
    ON_INSERTED = 'OnInserted'
    ON_DELETED = 'OnDeleted'
    ON_UPDATED = 'OnUpdated'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerRequest(SaveTriggerRequest):
    type: Optional[TriggerType] = None
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
    type: Optional[TriggerType] = None
    when: Optional[FilesTriggerType] = None
    file_ref: Optional[FileResourceRefDto] = None


class PaymentTriggerType(str, Enum):
    ON_ORDER_CREATED = 'OnOrderCreated'
    ON_ORDER_PAID = 'OnOrderPaid'
    ON_WEBHOOK_CALL_RECEIVED = 'OnWebhookCallReceived'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentTriggerRequest(SaveTriggerRequest):
    type: Optional[TriggerType] = None
    when: Optional[PaymentTriggerType] = None
    integrations: Optional[List[str]] = None
    events: Optional[List[str]] = None


class DatabaseProvider(str, Enum):
    MONGO_DB_CONNECTION_STRING = 'MongoDbConnectionString'
    CODE_MASH_MONGO_DB_ATLAS_FLEX_MANAGED = 'CodeMashMongoDbAtlasFlexManaged'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[DatabaseProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbConnectionStringDatabaseIntegrationRequest(DatabaseIntegrationRequest):
    provider: Optional[DatabaseProvider] = None
    database_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAtlasFlexManagedDatabaseIntegrationRequest(DatabaseIntegrationRequest):
    provider: Optional[DatabaseProvider] = None
    norbix_region_code: Optional[str] = None


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
    provider: Optional[FileProvider] = None
    root_folder_id: Optional[str] = None
    service_account_json_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FtpFilesIntegrationRequest(FilesIntegrationRequest):
    provider: Optional[FileProvider] = None
    host: Optional[str] = None
    port: int = 0
    root_path: Optional[str] = None
    use_ssl: bool = False
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DropBoxFilesIntegrationRequest(FilesIntegrationRequest):
    provider: Optional[FileProvider] = None
    root_path: Optional[str] = None
    access_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleICloudFilesIntegrationRequest(FilesIntegrationRequest):
    provider: Optional[FileProvider] = None
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
    provider: Optional[FileProvider] = None
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
    provider: Optional[FileProvider] = None
    bucket_name: Optional[str] = None
    service_account_json_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AzureBlobFilesIntegrationRequest(FilesIntegrationRequest):
    provider: Optional[FileProvider] = None
    blob_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LocalFilesIntegrationRequest(FilesIntegrationRequest):
    provider: Optional[FileProvider] = None
    root_path: Optional[str] = None


class LoggingProvider(str, Enum):
    CONSOLE = 'Console'
    NORBIX_LOGGING = 'NorbixLogging'
    DATA_DOG = 'DataDog'
    NEW_RELIC = 'NewRelic'
    SENTRY = 'Sentry'
    GRAFANA_LOKI = 'GrafanaLoki'
    AXIOM = 'Axiom'
    ELASTIC_CLOUD = 'ElasticCloud'
    AWS_CLOUD_WATCH = 'AWSCloudWatch'
    GCP_CLOUD_LOGGING = 'GCPCloudLogging'
    AZURE_MONITOR_LOGS = 'AzureMonitorLogs'
    GENERIC_HTTP = 'GenericHttp'
    KAFKA = 'Kafka'
    AMQP = 'AMQP'
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
    provider: Optional[LoggingProvider] = None
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
    provider: Optional[LoggingProvider] = None
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
    provider: Optional[LoggingProvider] = None
    integration_type: Optional[AwsS3LoggingIntegrationType] = None
    bucket_name: Optional[str] = None
    region: Optional[str] = None
    role_arn: Optional[str] = None
    external_id: Optional[str] = None
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NewRelicLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    region: Optional[str] = None
    service_name: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    database_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class KafkaLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    bootstrap_servers: Optional[str] = None
    topic: Optional[str] = None
    security_protocol: Optional[str] = None
    sasl_username: Optional[str] = None
    sasl_password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PrometheusLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    endpoint_url: Optional[str] = None
    job_name: Optional[str] = None
    bearer_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DataDogLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    site: Optional[str] = None
    service_name: Optional[str] = None
    environment: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InternalKafkaLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    bootstrap_servers: Optional[str] = None
    topic: Optional[str] = None
    security_protocol: Optional[str] = None
    sasl_username: Optional[str] = None
    sasl_password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ElasticSearchLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    uri: Optional[str] = None
    index: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SplunkLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    hec_endpoint_url: Optional[str] = None
    index: Optional[str] = None
    hec_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AzureOtelLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    endpoint_url: Optional[str] = None
    resource_name: Optional[str] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class KibanaLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
    uri: Optional[str] = None
    space_id: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LocalFileLoggingIntegrationRequest(LoggingIntegrationRequest):
    provider: Optional[LoggingProvider] = None
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
    is_project_system_role: bool = False

    # @Ignore()
    is_account_system_role: bool = False

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
    provider: Optional[MembershipProvider] = None
    domain: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class XMembershipIntegrationRequest(MembershipIntegrationRequest):
    provider: Optional[MembershipProvider] = None
    api_key: Optional[str] = None
    api_secret_key: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleMembershipIntegrationRequest(MembershipIntegrationRequest):
    provider: Optional[MembershipProvider] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MicrosoftMembershipIntegrationRequest(MembershipIntegrationRequest):
    provider: Optional[MembershipProvider] = None
    tenant_id: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GitHubMembershipIntegrationRequest(MembershipIntegrationRequest):
    provider: Optional[MembershipProvider] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MetaMembershipIntegrationRequest(MembershipIntegrationRequest):
    provider: Optional[MembershipProvider] = None
    app_id: Optional[str] = None
    app_secret: Optional[str] = None
    o_auth_modes: Optional[List[OAuthModeConfig]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleMembershipIntegrationRequest(MembershipIntegrationRequest):
    provider: Optional[MembershipProvider] = None
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
    provider: Optional[PaymentGatewayPlatform] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LemonSqueezyPaymentIntegrationRequest(PaymentIntegrationRequest):
    provider: Optional[PaymentGatewayPlatform] = None
    store_id: Optional[str] = None
    api_key: Optional[str] = None
    webhook_signing_secret: Optional[str] = None
    is_test_mode: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AdyenPaymentIntegrationRequest(PaymentIntegrationRequest):
    provider: Optional[PaymentGatewayPlatform] = None
    merchant_account: Optional[str] = None
    api_key: Optional[str] = None
    environment: Optional[str] = None
    webhook_id: Optional[str] = None
    webhook_hmac_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MolliePaymentIntegrationRequest(PaymentIntegrationRequest):
    provider: Optional[PaymentGatewayPlatform] = None
    profile_id: Optional[str] = None
    api_key: Optional[str] = None
    is_test_mode: bool = False
    webhook_signing_secret: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaddlePaymentIntegrationRequest(PaymentIntegrationRequest):
    provider: Optional[PaymentGatewayPlatform] = None
    api_key: Optional[str] = None
    webhook_endpoint_secret_key: Optional[str] = None
    environment: Optional[str] = None
    client_side_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PayPalPaymentIntegrationRequest(PaymentIntegrationRequest):
    provider: Optional[PaymentGatewayPlatform] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    environment: Optional[str] = None
    brand_name: Optional[str] = None
    webhook_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StripePaymentIntegrationRequest(PaymentIntegrationRequest):
    provider: Optional[PaymentGatewayPlatform] = None
    publishable_key: Optional[str] = None
    secret_key: Optional[str] = None
    webhook_signing_secret: Optional[str] = None
    webhook_endpoint_id: Optional[str] = None
    default_currency: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleInAppPaymentIntegrationRequest(PaymentIntegrationRequest):
    provider: Optional[PaymentGatewayPlatform] = None
    merchant_identifier: Optional[str] = None
    merchant_domain: Optional[str] = None
    display_name: Optional[str] = None
    merchant_identity_certificate_p12_base64: Optional[str] = None
    merchant_identity_certificate_password: Optional[str] = None
    payment_processing_certificate_p12_base64: Optional[str] = None
    payment_processing_certificate_password: Optional[str] = None
    webhook_bundle_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleInAppPaymentIntegrationRequest(PaymentIntegrationRequest):
    provider: Optional[PaymentGatewayPlatform] = None
    merchant_id: Optional[str] = None
    merchant_name: Optional[str] = None
    gateway: Optional[str] = None
    private_key_or_token: Optional[str] = None
    gateway_merchant_id: Optional[str] = None
    webhook_package_name: Optional[str] = None


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
class PushIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[PushProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EdgeWebPushIntegrationRequest(PushIntegrationRequest):
    provider: Optional[PushProvider] = None
    vapid_public_key: Optional[str] = None
    vapid_private_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChromePluginPushIntegrationRequest(PushIntegrationRequest):
    provider: Optional[PushProvider] = None
    extension_id: Optional[str] = None
    vapid_public_key: Optional[str] = None
    vapid_private_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SafariPushIntegrationRequest(PushIntegrationRequest):
    provider: Optional[PushProvider] = None
    website_push_id: Optional[str] = None
    certificate_p12_base64: Optional[str] = None
    certificate_password: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChromeWebPushIntegrationRequest(PushIntegrationRequest):
    provider: Optional[PushProvider] = None
    vapid_public_key: Optional[str] = None
    vapid_private_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FirefoxWebPushIntegrationRequest(PushIntegrationRequest):
    provider: Optional[PushProvider] = None
    vapid_public_key: Optional[str] = None
    vapid_private_key: Optional[str] = None
    subject: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AndroidFirebasePushIntegrationRequest(PushIntegrationRequest):
    provider: Optional[PushProvider] = None
    project_id: Optional[str] = None
    client_email: Optional[str] = None
    service_account_json: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppleApnsPushIntegrationRequest(PushIntegrationRequest):
    provider: Optional[PushProvider] = None
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
    provider: Optional[CodeProvider] = None
    integration_type: Optional[AwsLambdaIntegrationType] = None
    region: Optional[str] = None
    role_arn: Optional[str] = None
    external_id: Optional[str] = None
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AzureFunctionsCodeIntegrationRequest(CodeIntegrationRequest):
    provider: Optional[CodeProvider] = None
    function_app_name: Optional[str] = None
    resource_group: Optional[str] = None
    connection_string_or_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleCloudFunctionsCodeIntegrationRequest(CodeIntegrationRequest):
    provider: Optional[CodeProvider] = None
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
    NORBIX_HOSTED = 'NorbixHosted'


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
    provider: Optional[LlmProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenRouterLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    provider: Optional[LlmProvider] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MistralLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    provider: Optional[LlmProvider] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GrokLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    provider: Optional[LlmProvider] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GroqLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    provider: Optional[LlmProvider] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GoogleLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    provider: Optional[LlmProvider] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AnthropicLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    provider: Optional[LlmProvider] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenAiLlmIntegrationRequest(LlmIntegrationRequest, ILlmApiKeyRequest):
    provider: Optional[LlmProvider] = None
    api_key: Optional[str] = None


class McpProvider(str, Enum):
    DOCKER = 'Docker'
    OBSIDIAN = 'Obsidian'
    GOOGLE_CALENDAR = 'GoogleCalendar'
    STRIPE = 'Stripe'
    GIT_HUB = 'GitHub'
    MONGO_DB = 'MongoDb'
    PLAYWRIGHT = 'Playwright'
    BRAVE_SEARCH = 'BraveSearch'


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
    provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    command: Optional[str] = None
    args: Optional[List[str]] = None
    headless: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbMcpIntegrationRequest(McpIntegrationRequest):
    provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    command: Optional[str] = None
    args: Optional[List[str]] = None
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GitHubMcpIntegrationRequest(McpIntegrationRequest):
    provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    server_url: Optional[str] = None
    access_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StripeMcpIntegrationRequest(McpIntegrationRequest):
    provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    server_url: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class BraveSearchMcpIntegrationRequest(McpIntegrationRequest):
    provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    server_url: Optional[str] = None
    api_key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ObsidianMcpIntegrationRequest(McpIntegrationRequest):
    provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    command: Optional[str] = None
    args: Optional[List[str]] = None
    environment_variables: Optional[Dict[str, str]] = None


class CommunicationChannel(str, Enum):
    TRANSACTIONAL = 'Transactional'
    MARKETING = 'Marketing'
    SYSTEM = 'System'


class NotificationMedium(str, Enum):
    EMAIL = 'Email'
    SMS = 'Sms'
    PUSH = 'Push'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TemplateDto(IHasViewId, IHasDatabaseId):
    id: Optional[str] = None
    view_id: Optional[str] = None
    template_name: Optional[str] = None
    description: Optional[str] = None
    communication_channel: Optional[CommunicationChannel] = None
    medium: Optional[NotificationMedium] = None
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
    static_attachments: Optional[List[FileResourceRefDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailMessageTranslationDto(IHasRazorTemplateCode):
    language: Optional[str] = None
    content: Optional[EmailMessageContentDto] = None
    static_attachments: Optional[List[FileResourceRefDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateDto(TemplateDto, IBindableContract):
    translations: List[EmailMessageTranslationDto] = field(default_factory=list)
    static_attachments: Optional[List[FileResourceRefDto]] = None


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
    translations: List[PushMessageTranslationDto] = field(default_factory=list)


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
    translations: List[SmsMessageTranslationDto] = field(default_factory=list)


class SystemEmailTemplateTheme(str, Enum):
    TEXT = 'Text'
    BRANDED = 'Branded'
    CREATIVE = 'Creative'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SystemEmailTemplateDto(EmailTemplateDto):
    image_preview: Optional[str] = None
    theme: Optional[SystemEmailTemplateTheme] = None
    system_group: Optional[str] = None
    system_tags: Optional[List[str]] = None
    for_trigger: Optional[TriggerType] = None
    hidden_system_email_template: bool = False


# @Flags()
class RespectTimeZoneSettings(IntEnum):
    RESPECT_TO_LAST_LOGIN_ZONE = 1
    RESPECT_TO_REGISTRATION_ZONE = 2
    RESPECT_TO_REGISTRATION_PROJECT_ZONE = 4


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignDeliverySettingsDto:
    recipients_source_type: Optional[EmailCampaignRecipientsSourceTypes] = None
    mapped_tokens: Optional[List[TokenMappingDto]] = None
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
    ACCOUNT_USERS = 'AccountUsers'


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
    destination_ids: Optional[List[str]] = None
    event_name: Optional[str] = None
    content_type: Optional[str] = None
    include_raw_payload: bool = False
    mapped_tokens: Optional[List[TokenMappingDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerActionWebhookDto(TriggerActionDto):
    delivery_settings: Optional[WebhookDeliverySettingsDto] = None


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
class TriggerActionSmsDto(TriggerActionDto):
    template_id: Optional[str] = None
    delivery_settings: Optional[SmsCampaignDeliverySettingsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SseDeliverySettingsDto:
    audience: Optional[str] = None
    user_auth_ids: Optional[List[str]] = None
    event_name: Optional[str] = None
    payload_type: Optional[str] = None
    payload_template: Optional[str] = None
    persist: bool = False
    mapped_tokens: Optional[List[TokenMappingDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerActionSseDto(TriggerActionDto):
    delivery_settings: Optional[SseDeliverySettingsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerActionMarketplaceDto(TriggerActionDto):
    function_id: Optional[str] = None
    payload: Optional[Dict[str, str]] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTriggers(CodeMashListPaginationRequestBase):
    schema_id: Optional[str] = None


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
class GetTriggersResponse(ResponseBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToAllUsersDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    roles_names: Optional[List[str]] = None
    user_tags: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToAccountUsersDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    user_recipients: List[str] = field(default_factory=list)
    user_cc: Optional[List[str]] = None
    user_bcc: Optional[List[str]] = None
    single_email_strategy: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToUsersDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    user_recipients: List[str] = field(default_factory=list)
    user_cc: Optional[List[str]] = None
    user_bcc: Optional[List[str]] = None
    single_email_strategy: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToEmailAddressesDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    recipients: List[str] = field(default_factory=list)
    recipients_cc: Optional[List[str]] = None
    recipients_bcc: Optional[List[str]] = None
    single_email_strategy: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailToCollectionRecordsDeliverySettingsDto(EmailCampaignDeliverySettingsDto):
    fields: List[str] = field(default_factory=list)
    schema_name: Optional[str] = None
    field_type: Optional[CollectionEmailCampaignRecipientField] = None
    role_names: Optional[List[str]] = None
    languages: Optional[List[str]] = None


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
class PushToAccountUsersDeliverySettingsDto(PushCampaignDeliverySettingsDto):
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
    env: Optional[str] = None
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
class MongoDbConnectionStringIntegrationDto(DatabaseIntegrationDto):
    database_name: Optional[str] = None


class IntegrationStatus(str, Enum):
    UNKNOWN = 'Unknown'
    PENDING = 'Pending'
    PROVISIONING = 'Provisioning'
    ACTIVE = 'Active'
    FAILED = 'Failed'
    DEPROVISIONING = 'Deprovisioning'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MongoDbAtlasFlexManagedIntegrationDto(DatabaseIntegrationDto):
    database_name: Optional[str] = None
    norbix_region_code: Optional[str] = None
    flex_tier_code: Optional[str] = None
    status: Optional[IntegrationStatus] = None
    atlas_project_id: Optional[str] = None
    atlas_cluster_name: Optional[str] = None
    failure_reason: Optional[str] = None


class SmsProvider(str, Enum):
    TWILIO = 'Twilio'
    VONAGE = 'Vonage'
    PLIVO = 'Plivo'
    TELNYX = 'Telnyx'
    BIRD = 'Bird'
    TELESIGN = 'Telesign'
    SINCH = 'Sinch'
    FAKE = 'Fake'


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
    region: Optional[MailGunRegion] = None


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
    is_configured: bool = False
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
    INTERNAL = 'Internal'
    SDK = 'Sdk'


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


class MarketplaceTokenResolverKind(str, Enum):
    STATIC = 'Static'
    REQUEST = 'Request'
    PROJECT = 'Project'
    INITIATOR = 'Initiator'
    CUSTOM = 'Custom'
    INTEGRATION_CONFIG = 'IntegrationConfig'
    INTEGRATION_SECRET = 'IntegrationSecret'


class MarketplaceSecretValueFormat(str, Enum):
    RAW = 'Raw'
    BEARER = 'Bearer'
    BASIC = 'Basic'
    PREFIXED = 'Prefixed'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceTokenMappingDto:
    token: Optional[str] = None
    resolver: Optional[MarketplaceTokenResolverKind] = None
    value: Optional[str] = None
    secret_keys: Optional[List[str]] = None
    format: Optional[MarketplaceSecretValueFormat] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionDto(IHasViewId):
    view_id: Optional[str] = None
    integration_view_id: Optional[str] = None
    function_key: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    is_enabled: bool = False
    request_template: Optional[str] = None
    mapped_tokens: List[MarketplaceTokenMappingDto] = field(default_factory=list)


class MarketplaceFieldType(str, Enum):
    STRING = 'String'
    NUMBER = 'Number'
    BOOLEAN = 'Boolean'
    URL = 'Url'
    EMAIL = 'Email'
    JSON = 'Json'
    MULTILINE_TEXT = 'MultilineText'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFieldDefinitionDto:
    key: Optional[str] = None
    label: Optional[str] = None
    description: Optional[str] = None
    documentation_url: Optional[str] = None
    type: Optional[MarketplaceFieldType] = None
    is_required: bool = False
    default_value: Optional[str] = None
    placeholder: Optional[str] = None
    validation_pattern: Optional[str] = None
    allowed_values: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionParameterDto:
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    is_required: bool = False
    default_value: Optional[str] = None


class MarketplaceParameterLocation(str, Enum):
    BODY = 'Body'
    HEADER = 'Header'
    QUERY = 'Query'
    PATH = 'Path'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceParameterSpecDto:
    name: Optional[str] = None
    location: Optional[MarketplaceParameterLocation] = None
    value_template: Optional[str] = None
    label: Optional[str] = None
    description: Optional[str] = None
    documentation_url: Optional[str] = None
    type: Optional[str] = None
    is_required: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceHttpRequestSpecDto:
    method: Optional[str] = None
    path_template: Optional[str] = None
    parameters: Optional[IReadOnlyList[MarketplaceParameterSpecDto]] = None
    content_type: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionDefinitionDto:
    definition_id: Optional[str] = None
    function_key: Optional[str] = None
    display_name: Optional[str] = None
    description: Optional[str] = None
    group: Optional[str] = None
    parameters: Optional[IReadOnlyList[MarketplaceFunctionParameterDto]] = None
    request_schema: Optional[str] = None
    request_template: Optional[str] = None
    request: Optional[MarketplaceHttpRequestSpecDto] = None
    default_token_mappings: List[MarketplaceTokenMappingDto] = field(default_factory=list)


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
    tags: Optional[IReadOnlyList[str]] = None
    spec_version: int = 0
    config_fields: Optional[IReadOnlyList[MarketplaceFieldDefinitionDto]] = None
    secret_fields: Optional[IReadOnlyList[MarketplaceFieldDefinitionDto]] = None
    functions: Optional[IReadOnlyList[MarketplaceFunctionDefinitionDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AdminPortalModuleDto:
    key: Optional[str] = None
    display_name: Optional[str] = None
    enabled: bool = False


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
class AiChatEntryAttachmentWireDto:
    id: Optional[str] = None
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserMessageEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    text: Optional[str] = None
    attachments: List[AiChatEntryAttachmentWireDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatEntrySourceWireDto:
    kind: Optional[str] = None
    requirement_id: Optional[str] = None
    session_id: Optional[str] = None
    entry_id: Optional[str] = None
    entry_seq: Optional[int] = None
    artifact_id: Optional[str] = None
    label: Optional[str] = None
    step: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssistantTextEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    text: Optional[str] = None
    is_streaming: bool = False
    sources: List[AiChatEntrySourceWireDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatQuestionOptionWireDto:
    value: Optional[str] = None
    label: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatQuestionWireDto:
    id: Optional[str] = None
    text: Optional[str] = None
    options: List[AiChatQuestionOptionWireDto] = field(default_factory=list)
    default: Optional[str] = None
    allow_free_text: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatGateResultWireDto:
    class_: Optional[str] = field(metadata=config(field_name='class'), default=None)
    reason: Optional[str] = None
    affected_requirement_ids: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssistantQuestionEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    questions: List[AiChatQuestionWireDto] = field(default_factory=list)
    status: Optional[str] = None
    scope: Optional[str] = None
    gate: Optional[AiChatGateResultWireDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserAnswerEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    answers: Dict[str, str] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatPlanStepInputsWireDto:
    artifacts: List[str] = field(default_factory=list)
    requirements: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatPlanStepDoneCheckWireDto:
    check: Optional[str] = None
    args_json: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatPlanStepLoopWireDto:
    max_iterations: Optional[int] = None
    max_tool_calls: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatPlanStepWireDto:
    n: int = 0
    tool: Optional[str] = None
    title: Optional[str] = None
    goal: Optional[str] = None
    inputs: Optional[AiChatPlanStepInputsWireDto] = None
    depends_on: List[int] = field(default_factory=list)
    replaces: Optional[int] = None
    done: List[AiChatPlanStepDoneCheckWireDto] = field(default_factory=list)
    loop: Optional[AiChatPlanStepLoopWireDto] = None
    difficulty: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PlanEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    goal: Optional[str] = None
    steps: List[AiChatPlanStepWireDto] = field(default_factory=list)
    status: Optional[str] = None
    gate: Optional[AiChatGateResultWireDto] = None
    difficulty: Optional[int] = None
    difficulty_reason: Optional[str] = None
    delta_of: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserDecisionEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    decision: Optional[str] = None
    comment: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiChatStepLogLineWireDto:
    seq: int = 0
    tool: Optional[str] = None
    agent: Optional[str] = None
    status: Optional[str] = None
    detail: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RunStepEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    n: int = 0
    tool: Optional[str] = None
    title: Optional[str] = None
    status: Optional[str] = None
    result_summary: Optional[str] = None
    error: Optional[str] = None
    log: List[AiChatStepLogLineWireDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ActionPendingEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    tool: Optional[str] = None
    arguments_json: Optional[str] = None
    status: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NoticeEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    text: Optional[str] = None
    level: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConversationSnapshotEntryWireDto(AiChatEntryWireDto):
    kind: Optional[str] = None
    snapshot_id: Optional[str] = None
    covers_up_to_seq: int = 0


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
class ProjectLegalDocuments:
    terms_markdown: Optional[str] = None
    privacy_markdown: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuthId(IHasDomainEntityId):
    value: Optional[str] = None


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
    PROJECT = 4096
    COMPLIANCE = 8192
    CONTACTS = 16384
    MARKETPLACE = 32768


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
class Permission:
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
    permissions: List[Permission] = field(default_factory=list)
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
class BillingPeriod:
    year: int = 0
    month: int = 0
    start_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    end_exclusive_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    last_instant_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AtlasClusterChargeRecord:
    atlas_project_id: Optional[str] = None
    atlas_cluster_name: Optional[str] = None
    cents: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AtlasUsageRecord:
    period: Optional[BillingPeriod] = None
    total_cents: int = 0
    per_cluster: Optional[IReadOnlyList[AtlasClusterChargeRecord]] = None
    recorded_at_utc: Optional[UtcDateTime] = None


class UsageIngestionFailureReason(IntEnum):
    UNKNOWN_CUSTOMER = 1
    METER_NOT_FOUND = 2
    VALIDATION_FAILED = 3
    IMPORT_SET_FAILED = 4


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UsageIngestionFailure:
    reason: Optional[UsageIngestionFailureReason] = None
    period: Optional[BillingPeriod] = None
    stripe_event_id: Optional[str] = None
    message: Optional[str] = None
    reported_at_utc: Optional[UtcDateTime] = None


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
    schema_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveTrigger(CodeMashRequestBase):
    trigger: Optional[SaveTriggerRequest] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CredentialsSettingsModeDto:
    name: Optional[str] = None
    logout_url: Optional[str] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegration(Integration):
    provider: Optional[MembershipProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerId(AggregateId, IHasDomainEntityId):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TriggerAction:
    type: Optional[TriggerActionType] = None
    integration_id: Optional[IntegrationId] = None


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
    env: Optional[Env] = None
    integration_id: Optional[IntegrationId] = None


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
    has_record_owner: bool = False
    description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaListColumnDto:
    field: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaListSortDto:
    field: Optional[str] = None
    order: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaListSettingsDto:
    columns: List[SchemaListColumnDto] = field(default_factory=list)
    default_sort: Optional[SchemaListSortDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImportColumnMappingDto:
    csv_column_index: int = 0
    csv_header: Optional[str] = None
    property_name: Optional[str] = None
    dont_import_on_error: bool = False


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
    status: Optional[IntegrationStatus] = None
    atlas_project_id: Optional[str] = None
    atlas_cluster_name: Optional[str] = None
    failure_reason: Optional[str] = None


class ProjectStatus(str, Enum):
    ACTIVE = 'Active'
    PROVISIONING = 'Provisioning'
    PROVISIONING_FAILED = 'ProvisioningFailed'
    NO_DATABASE = 'NoDatabase'
    DISABLED = 'Disabled'
    SUSPENDED = 'Suspended'
    REMOVED = 'Removed'


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
    has_record_owner: bool = False
    description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Schema(IHasDomainEntityId):
    schema_name: Optional[SchemaName] = None
    id: Optional[SchemaId] = None
    env: Optional[Env] = None
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


class IPasskeyMessage:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuthUserName:
    value: Optional[str] = None


class AuthType(str, Enum):
    SERVICE = 'Service'
    EMAIL = 'Email'
    USER_NAME = 'UserName'
    PHONE = 'Phone'
    GUEST = 'Guest'
    SOCIAL = 'Social'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IpAddress:
    ip: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccessInformation:
    ip: Optional[IpAddress] = None
    date: Optional[UtcDateTime] = None
    zone: Optional[TimeZone] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Registration:
    registration_information: Optional[AccessInformation] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Login:
    need_change_password_on_next_login: bool = False
    last_access_information: Optional[AccessInformation] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Phone:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FirstName:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LastName:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MidName:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FullName:
    first_name: Optional[FirstName] = None
    mid_name: Optional[MidName] = None
    last_name: Optional[LastName] = None
    title: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class City:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Country:
    code: Optional[str] = None
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AddressLine:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PostalCode:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CountryState:
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Address:
    city: Optional[City] = None
    country: Optional[Country] = None
    address_line1: Optional[AddressLine] = None
    address_line2: Optional[AddressLine] = None
    postal_code: Optional[PostalCode] = None
    state: Optional[CountryState] = None


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
class UserMarketingPreferences:
    block_all_marketing_messages: bool = False
    blocked_tags: Optional[Dict[str, HashSet[Tag]]] = None
    block_reasons: Optional[List[MarketingBlockReason]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserGeneralInfo(IBindableContract):
    phone: Optional[Phone] = None
    primary_email: Optional[EmailAddress] = None
    display_name: Optional[DisplayName] = None
    first_name: Optional[FirstName] = None
    last_name: Optional[LastName] = None
    full_name: Optional[FullName] = None
    address: Optional[Address] = None
    company: Optional[str] = None
    gender: Optional[Gender] = None
    birth_date: Optional[UtcDateTime] = None
    time_zone: Optional[TimeZone] = None
    language: Optional[Language] = None
    marketing_preferences: Optional[UserMarketingPreferences] = None
    notes: Optional[str] = None
    extra_metadata: Optional[str] = None


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
class PushDevices(List[PushDevice]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserId(IHasDomainEntityId):
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserRef(ResourceRef):
    kind: Optional[ResourceRefKind] = None
    user_id: Optional[UserId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class Auth(IBindableContract):
    id: Optional[AuthId] = None
    roles: Optional[List[RoleName]] = None
    email: Optional[EmailAddress] = None
    user_name: Optional[AuthUserName] = None
    type: Optional[AuthType] = None
    registration: Optional[Registration] = None
    login: Optional[Login] = None
    general_info: Optional[UserGeneralInfo] = None
    status: Optional[AuthStatus] = None
    created_on: Optional[UtcDateTime] = None
    modified_on: Optional[UtcDateTime] = None
    push_devices: Optional[PushDevices] = None
    tags: Optional[List[Tag]] = None
    user_ref: Optional[UserRef] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileIntegration(Integration):
    provider: Optional[FileProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileTrigger(Trigger):
    when: Optional[FilesTriggerType] = None
    file_resource_ref: Optional[FileResourceRef] = None


class EmailValidationProvider(IntEnum):
    ZERO_BOUNCE = 1
    NEVER_BOUNCE = 2
    BOUNCER = 3
    MAILGUN_VALIDATE = 4


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailValidationIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[EmailValidationProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailTemplate(CodeMashRequestBase):
    # @ApiMember(Description="The display name of the email template.", IsRequired=true)
    template_name: Optional[str] = None
    """
    The display name of the email template.
    """


    # @ApiMember(Description="Optional free-text description of what the template is used for.")
    description: Optional[str] = None
    """
    Optional free-text description of what the template is used for.
    """


    # @ApiMember(Description="The communication channel the template is intended for (e.g. Transactional, Marketing).")
    communication_channel: Optional[CommunicationChannel] = None
    """
    The communication channel the template is intended for (e.g. Transactional, Marketing).
    """


    # @ApiMember(Description="Optional tags to organize/filter the template by.")
    tags: Optional[List[str]] = None
    """
    Optional tags to organize/filter the template by.
    """


    # @ApiMember(Description="Optional static file attachments to send with every email using this template.")
    static_attachments: Optional[List[FileResourceRefDto]] = None
    """
    Optional static file attachments to send with every email using this template.
    """


    # @ApiMember(Description="The per-language content translations (subject/body) for this template.", IsRequired=true)
    translations: List[EmailMessageTranslationDto] = field(default_factory=list)
    """
    The per-language content translations (subject/body) for this template.
    """


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
class EmailFooter:
    id: Optional[EmailFooterId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[TemplateCode]] = field(default_factory=list)
    env: Optional[Env] = None


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
class EmailSignature:
    id: Optional[EmailSignatureId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[TemplateCode]] = field(default_factory=list)
    env: Optional[Env] = None


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
class EmailTemplate(Template[EmailMessageContent]):
    static_attachments: Optional[List[FileResourceRef]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailValidationIntegration(Integration):
    provider: Optional[EmailValidationProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CampaignId:
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CampaignBatchId:
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotificationId(AggregateId, IHasDomainEntityId):
    pass


class CampaignStopReason(str, Enum):
    USER_REQUESTED = 'UserRequested'
    MODULE_DISABLED = 'ModuleDisabled'


class EmailDeliveryEventType(str, Enum):
    UNKNOWN = 'Unknown'
    DELIVERED = 'Delivered'
    OPEN = 'Open'
    CLICK = 'Click'
    SOFT_BOUNCE = 'SoftBounce'
    HARD_BOUNCE = 'HardBounce'
    COMPLAINT = 'Complaint'
    UNSUBSCRIBED = 'Unsubscribed'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveSmsTemplate(CodeMashRequestBase):
    # @ApiMember(Description="Display name for the SMS template.", IsRequired=true)
    template_name: Optional[str] = None
    """
    Display name for the SMS template.
    """


    # @ApiMember(Description="Optional free-text description of the template's purpose.")
    description: Optional[str] = None
    """
    Optional free-text description of the template's purpose.
    """


    # @ApiMember(Description="Whether this template is Transactional or Marketing SMS.", IsRequired=true)
    communication_channel: Optional[CommunicationChannel] = None
    """
    Whether this template is Transactional or Marketing SMS.
    """


    # @ApiMember(Description="Optional tags to organize/filter templates.")
    tags: Optional[List[str]] = None
    """
    Optional tags to organize/filter templates.
    """


    # @ApiMember(Description="The template's per-language translations (each with its own SMS body).", IsRequired=true)
    translations: List[SmsMessageTranslationDto] = field(default_factory=list)
    """
    The template's per-language translations (each with its own SMS body).
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationRequest:
    integration_id: Optional[str] = None
    provider: Optional[SmsProvider] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegration(Integration):
    provider: Optional[SmsProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsTitle:
    value: Optional[TemplateCode] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsBody:
    value: Optional[TemplateCode] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsMessageContent:
    title: Optional[SmsTitle] = None
    body: Optional[SmsBody] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsTemplate(Template[SmsMessageContent]):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegration(Integration):
    provider: Optional[CodeProvider] = None


class MarketplaceIntegrationTransport(str, Enum):
    MCP = 'Mcp'
    REST = 'Rest'
    CODE = 'Code'
    INTERNAL = 'Internal'
    SDK = 'Sdk'


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


class MarketplaceTokenResolver(str, Enum):
    STATIC = 'Static'
    REQUEST = 'Request'
    PROJECT = 'Project'
    INITIATOR = 'Initiator'
    CUSTOM = 'Custom'
    INTEGRATION_CONFIG = 'IntegrationConfig'
    INTEGRATION_SECRET = 'IntegrationSecret'


class SecretValueFormat(str, Enum):
    RAW = 'Raw'
    BEARER = 'Bearer'
    BASIC = 'Basic'
    PREFIXED = 'Prefixed'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceTokenMapping:
    token: Optional[str] = None
    resolver: Optional[MarketplaceTokenResolver] = None
    value: Optional[str] = None
    secret_keys: Optional[IReadOnlyList[str]] = None
    format: Optional[SecretValueFormat] = None


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
    token_mappings: Optional[IReadOnlyList[MarketplaceTokenMapping]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionId(IHasDomainEntityId):
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunction(IHasDomainEntityId):
    function_id: Optional[MarketplaceFunctionId] = None
    integration_id: Optional[IntegrationId] = None
    env: Optional[Env] = None
    function_key: Optional[str] = None
    display_name: Optional[DisplayName] = None
    description: Optional[str] = None
    is_enabled: bool = False
    request_template: Optional[str] = None
    mapped_tokens: Optional[IReadOnlyList[MarketplaceTokenMapping]] = None
    view_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePushTemplate(CodeMashRequestBase):
    # @ApiMember(Description="The template's display name.", IsRequired=true)
    template_name: Optional[str] = None
    """
    The template's display name.
    """


    # @ApiMember(Description="Optional free-text description of the template's purpose.")
    description: Optional[str] = None
    """
    Optional free-text description of the template's purpose.
    """


    # @ApiMember(Description="Whether the template is Transactional or Marketing.")
    communication_channel: Optional[CommunicationChannel] = None
    """
    Whether the template is Transactional or Marketing.
    """


    # @ApiMember(Description="Optional tags for organizing/filtering templates.")
    tags: Optional[List[str]] = None
    """
    Optional tags for organizing/filtering templates.
    """


    # @ApiMember(Description="The per-locale translations (title/body/subtitle) that make up the template content.", IsRequired=true)
    translations: List[PushMessageTranslationDto] = field(default_factory=list)
    """
    The per-locale translations (title/body/subtitle) that make up the template content.
    """


class IHasAccountId:
    account_id: Optional[str] = None


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
class PushCampaignRequest:
    source: Optional[PushCampaignRecipientsSourceTypes] = None
    template_id: Optional[str] = None
    integration_id: Optional[str] = None
    language: Optional[str] = None
    initiator_id: Optional[str] = None
    notes: Optional[str] = None
    mapped_tokens: Optional[List[TokenMappingDto]] = None
    campaign_time: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegration(Integration):
    provider: Optional[PushProvider] = None


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
class PaymentIntegration(Integration):
    provider: Optional[PaymentGatewayPlatform] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentTrigger(Trigger):
    when: Optional[PaymentTriggerType] = None
    integrations: Optional[List[IntegrationId]] = None
    events: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegration(Integration):
    provider: Optional[LoggingProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatScreenContextDto:
    kind: Optional[str] = None
    view_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegration(Integration):
    provider: Optional[LlmProvider] = None
    default_model: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegration(Integration):
    provider: Optional[McpProvider] = None
    transport: Optional[McpTransport] = None
    metadata: Optional[McpMetadata] = None


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
    selected_events: List[TriggerEventName] = field(default_factory=list)
    extra_headers: Optional[IReadOnlyDictionary[str, str]] = None
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegration(Integration):
    capability: Optional[str] = None
    destinations: List[WebhookDestination] = field(default_factory=list)
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
class SchedulerTask(IHasDomainEntityId):
    id: Optional[TaskId] = None
    type: Optional[SchedulerTaskType] = None
    name: Optional[DisplayName] = None
    description: Optional[str] = None
    cron: Optional[CronExpression] = None
    payload_json: Optional[str] = None
    initiator_id: Optional[AuthId] = None
    is_enabled: bool = False
    stop_on_error: bool = False


class ResourceKindDto(str, Enum):
    CONTACT = 'contact'
    DOCUMENT = 'document'
    FILE = 'file'
    PAYMENT_CUSTOMER = 'paymentCustomer'
    ORDER = 'order'
    PAYMENT = 'payment'
    PRODUCT = 'product'
    INTEGRATION = 'integration'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResourceRefDto:
    project_id: Optional[str] = None
    integration_id: Optional[str] = None
    kind: Optional[ResourceKindDto] = None


class CaseResolutionFixKind(str, Enum):
    CODE_FIX = 'CodeFix'
    CONFIG_CHANGE = 'ConfigChange'
    CUSTOMER_INSTRUCTION = 'CustomerInstruction'
    KNOWN_LIMITATION = 'KnownLimitation'
    DUPLICATE = 'Duplicate'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CaseResolutionDto:
    problem: Optional[str] = None
    symptoms: List[str] = field(default_factory=list)
    root_cause: Optional[str] = None
    fix: Optional[CaseResolutionFixKind] = None
    fix_detail: Optional[str] = None
    affected_versions: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseId(AggregateId):
    view_id: Optional[str] = None


class SupportCaseKind(str, Enum):
    QUESTION = 'Question'
    BUG = 'Bug'
    INCIDENT = 'Incident'
    BILLING = 'Billing'
    SECURITY = 'Security'
    FEATURE_REQUEST = 'FeatureRequest'


class SupportCaseSeverity(IntEnum):
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4


class DeploymentMode(str, Enum):
    MANAGED = 'Managed'
    SELF_HOSTED = 'SelfHosted'
    ENTERPRISE = 'Enterprise'


class SupportMessageAuthorKind(str, Enum):
    CUSTOMER = 'Customer'
    STAFF = 'Staff'
    AI = 'Ai'
    SYSTEM = 'System'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportMessageRef:
    message_id: Optional[str] = None
    author_kind: Optional[SupportMessageAuthorKind] = None
    author_id: Optional[str] = None
    sent_on: Optional[UtcDateTime] = None


class SupportCaseStatus(str, Enum):
    OPEN = 'Open'
    TRIAGED = 'Triaged'
    IN_PROGRESS = 'InProgress'
    WAITING_ON_CUSTOMER = 'WaitingOnCustomer'
    RESOLVED = 'Resolved'
    CLOSED = 'Closed'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CaseResolution:
    problem: Optional[str] = None
    symptoms: Optional[IReadOnlyList[str]] = None
    root_cause: Optional[str] = None
    fix: Optional[CaseResolutionFixKind] = None
    fix_detail: Optional[str] = None
    module: Optional[str] = None
    kind: Optional[SupportCaseKind] = None
    severity: Optional[SupportCaseSeverity] = None
    affected_versions: Optional[IReadOnlyList[str]] = None
    resolved_by: Optional[str] = None


class SupportCaseCloseReason(str, Enum):
    MANUAL = 'Manual'
    AUTO_CLOSED_AFTER_RESOLVE = 'AutoClosedAfterResolve'


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
class AccountOwnerDto:
    email: Optional[str] = None
    display_name: Optional[str] = None
    billing_email: Optional[str] = None
    operations_email: Optional[str] = None
    security_email: Optional[str] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UsageBillingClusterChargeDto:
    atlas_project_id: Optional[str] = None
    atlas_cluster_name: Optional[str] = None
    cents: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UsageBillingPeriodDto:
    period: Optional[str] = None
    total_cents: int = 0
    per_cluster: List[UsageBillingClusterChargeDto] = field(default_factory=list)
    recorded_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UsageBillingIngestionFailureDto:
    reason: Optional[str] = None
    period: Optional[str] = None
    stripe_event_id: Optional[str] = None
    message: Optional[str] = None
    reported_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UsageBillingDto:
    account_id: Optional[str] = None
    atlas: Dict[str, UsageBillingPeriodDto] = field(default_factory=dict)
    ingestion_failures: List[UsageBillingIngestionFailureDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PromotionItemDto:
    type: Optional[str] = None
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PromotionBlockerDto:
    content_type: Optional[str] = None
    content_id: Optional[str] = None
    ref_kind: Optional[str] = None
    unresolved_ref: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PromotionResultDto:
    content_mirrored: List[PromotionItemDto] = field(default_factory=list)
    content_deleted: List[PromotionItemDto] = field(default_factory=list)
    integrations_seeded: List[PromotionItemDto] = field(default_factory=list)
    integrations_skipped: List[PromotionItemDto] = field(default_factory=list)
    blockers: List[PromotionBlockerDto] = field(default_factory=list)
    from_version: Optional[int] = None
    was_dry_run: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectEnvironmentsDto:
    environments: List[str] = field(default_factory=list)


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
class AuthenticationFlowPasswordPolicyDto:
    min_length: int = 0
    max_length: Optional[int] = None
    min_numbers: Optional[int] = None
    min_upper: Optional[int] = None
    min_lower: Optional[int] = None
    min_special: Optional[int] = None
    allowed_special: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AuthenticationFlowSummaryDto:
    type: Optional[str] = None
    provider: Optional[str] = None
    password_complexity: Optional[AuthenticationFlowPasswordPolicyDto] = None


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
    default_integration_view_ids: Dict[str, str] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailDto:
    is_enabled: bool = False
    default_integration_view_ids: Dict[str, str] = field(default_factory=dict)


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
class PermissionDto:
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
    permissions: Optional[List[PermissionDto]] = None


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
    require_email_validation: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingDto:
    is_enabled: bool = False
    is_established: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ServerEventsDto:
    is_enabled: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushDto:
    is_enabled: bool = False
    default_integration_view_ids: Dict[str, str] = field(default_factory=dict)
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
    default_integration_view_ids: Dict[str, str] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentTriggerDto(TriggerDto):
    when: Optional[PaymentTriggerType] = None
    integrations: Optional[List[str]] = None
    events: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsDto:
    is_enabled: bool = False
    triggers: Optional[List[PaymentTriggerDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsDto:
    is_enabled: bool = False
    default_integration_view_ids: Dict[str, str] = field(default_factory=dict)


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
    canonical_admin_url: Optional[str] = None
    admin_url: Optional[str] = None
    effective_admin_url: Optional[str] = None
    default_language: Optional[str] = None
    languages: List[str] = field(default_factory=list)
    primary_region: Optional[ProjectRegionDto] = None
    additional_regions: Optional[List[ProjectRegionDto]] = None
    is_multi_region_eligible: bool = False
    brand: Optional[ProjectBrandDto] = None
    notification_settings: Optional[NotificationSettingsDto] = None
    allowed_origins: Optional[List[str]] = None
    expose_brand_to_admin_portal: bool = False
    expose_auth_to_admin_portal: bool = False
    admin_portal_enabled: bool = False
    admin_portal_service_user_id: Optional[str] = None
    membership_authentication_flows: Optional[List[AuthenticationFlowSummaryDto]] = None
    expose_legal_to_admin_portal: bool = False
    legal_terms_markdown: Optional[str] = None
    legal_privacy_markdown: Optional[str] = None
    environments: List[str] = field(default_factory=list)
    environment_ranks: Dict[str, int] = field(default_factory=dict)
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
    default_llm_integration_view_id: Optional[str] = None
    connections: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectListItemDto:
    view_id: Optional[str] = None
    is_active: bool = False
    project_status: Optional[ProjectStatus] = None
    name: Optional[str] = None
    unique_name: Optional[str] = None
    primary_region: Optional[ProjectRegionDto] = None
    additional_regions: Optional[List[ProjectRegionDto]] = None


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasswordPolicyDto:
    min_length: int = 0
    max_length: Optional[int] = None
    min_numbers: Optional[int] = None
    max_numbers: Optional[int] = None
    min_upper: Optional[int] = None
    max_upper: Optional[int] = None
    min_lower: Optional[int] = None
    max_lower: Optional[int] = None
    min_special: Optional[int] = None
    max_special: Optional[int] = None
    allowed_special: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountTeamRoleDto:
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    is_system: bool = False
    policies: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyListItemDto:
    credential_id: Optional[str] = None
    friendly_name: Optional[str] = None
    registered_on_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    last_used_on_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    is_revoked: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LicenseDomainDnsRecordDto:
    host: Optional[str] = None
    record_type: Optional[str] = None
    resolved: bool = False
    required: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LicenseDomainDnsStatusDto:
    domain: Optional[str] = None
    all_required_resolved: bool = False
    records: List[LicenseDomainDnsRecordDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LicenseDomainVerificationChallengeDto:
    domain: Optional[str] = None
    txt_host: Optional[str] = None
    txt_value: Optional[str] = None
    expires_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    verified: bool = False
    verified_at_utc: Optional[datetime.datetime] = None
    skipped: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LicenseDomainVerificationStatusDto:
    domain: Optional[str] = None
    verified: bool = False
    skipped: bool = False
    txt_host: Optional[str] = None
    expected_txt_value: Optional[str] = None
    observed_txt_value: Optional[str] = None
    expires_at_utc: Optional[datetime.datetime] = None
    verified_at_utc: Optional[datetime.datetime] = None
    message: Optional[str] = None


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
class LicenseHeartbeatVerdictDto:
    status: Optional[str] = None
    proof_token: Optional[str] = None
    server_time_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    grace_until_utc: Optional[datetime.datetime] = None
    installation_id: Optional[str] = None
    license_account_id: Optional[str] = None
    domain: Optional[str] = None
    signature: Optional[str] = None
    message: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InstallationLicenseStatusDto:
    stored_mode: Optional[str] = None
    effective_mode: Optional[str] = None
    is_production: bool = False
    grace_days_left: Optional[int] = None
    grace_until_utc: Optional[datetime.datetime] = None
    last_proven_at_utc: Optional[datetime.datetime] = None
    last_heartbeat_at_utc: Optional[datetime.datetime] = None
    installation_domain: Optional[str] = None
    licensed_domain: Optional[str] = None
    host_kind: Optional[str] = None
    is_trial_license: bool = False
    license_expire_utc: Optional[datetime.datetime] = None
    message: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ServiceUserApiKeyDto:
    id: int = 0
    name: Optional[str] = None
    visible_key: Optional[str] = None
    scopes: List[str] = field(default_factory=list)
    created_date: datetime.datetime = datetime.datetime(1, 1, 1)
    expiry_date: Optional[datetime.datetime] = None
    cancelled_date: Optional[datetime.datetime] = None
    active: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetTriggerResponse(ResponseBase):
    pass


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
    destination_ids: Optional[List[str]] = None


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
class PasskeySettingsDto:
    enabled: bool = False
    code_ttl_minutes: int = 0
    max_credentials_per_user: int = 0
    recovery_code_count: int = 0
    generate_recovery_codes_at_signup: bool = False
    authenticator_attachment: Optional[str] = None
    allow_magic_link_recovery: bool = False
    refresh_token_ttl_days: int = 0
    rp_id: Optional[str] = None


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
class MembershipMessageTemplateDto:
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipEmailActionSettingsDto:
    send_email: bool = False
    template: Optional[MembershipMessageTemplateDto] = None
    callback: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipEmailPreferencesDto:
    registration_via_email: Optional[MembershipEmailActionSettingsDto] = None
    verification_via_email: Optional[MembershipEmailActionSettingsDto] = None
    password_reset_via_email: Optional[MembershipEmailActionSettingsDto] = None
    invitation_via_email: Optional[MembershipEmailActionSettingsDto] = None
    deactivation_via_email: Optional[MembershipEmailActionSettingsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasswordComplexityDto:
    min_length: int = 0
    max_length: Optional[int] = None
    min_numbers: Optional[int] = None
    max_numbers: Optional[int] = None
    min_upper: Optional[int] = None
    max_upper: Optional[int] = None
    min_lower: Optional[int] = None
    max_lower: Optional[int] = None
    min_special: Optional[int] = None
    max_special: Optional[int] = None
    allowed_special: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipAuthorizationViewDto:
    email_preferences: Optional[MembershipEmailPreferencesDto] = None
    user_registers_as_role: Optional[str] = None
    guest_registers_as_role: Optional[str] = None
    allowed_register_roles: Optional[List[str]] = None
    allowed_provider_register_roles: Optional[List[str]] = None
    reset_password_token_expiration: Optional[int] = None
    invitation_expiration: Optional[int] = None
    email_verification_expiration: Optional[int] = None
    deactivation_expiration: Optional[int] = None
    default_subscribe_to_news: bool = False
    password_complexity: Optional[PasswordComplexityDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipCredentialsSettingsModeDto:
    name: Optional[str] = None
    logout_url: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipCredentialsSettingsDto:
    logout_url: Optional[str] = None
    allow_usernames: bool = False
    modes: Optional[List[MembershipCredentialsSettingsModeDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipAuthenticationViewDto:
    credentials_settings: Optional[MembershipCredentialsSettingsDto] = None
    flows: List[str] = field(default_factory=list)


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
class AppliedTaxonomyDto:
    catalog_id: Optional[str] = None
    id: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    action: Optional[str] = None
    terms_created: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppliedCollectionDto:
    entity: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    action: Optional[str] = None
    published: bool = False
    linked_fields: List[str] = field(default_factory=list)


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
class CollectionIndexKeyDto:
    field: Optional[str] = None
    order: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CollectionIndexDto:
    name: Optional[str] = None
    keys: List[CollectionIndexKeyDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SeedCollectionReportItemDto:
    collection_name: Optional[str] = None
    requested: int = 0
    inserted: int = 0
    ids: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SeedCollectionRecordsResultDto:
    insert_order: List[str] = field(default_factory=list)
    report: List[SeedCollectionReportItemDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationListProjection(IntegrationListProjection):
    provider: Optional[DatabaseProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FlexTierDto:
    code: Optional[str] = None
    step: int = 0
    display_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IntegrationTestResultItemDto:
    operation: Optional[str] = None
    result: Optional[str] = None
    errors: Optional[IReadOnlyList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaRefDto:
    schema_id: Optional[str] = None
    schema_name: Optional[str] = None
    database_integration_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CollectionImportDto:
    id: Optional[str] = None
    schema: Optional[SchemaRefDto] = None
    file: Optional[FileResourceRefDto] = None
    error_file: Optional[FileResourceRefDto] = None
    delimiter: Optional[str] = None
    has_header: bool = False
    status: Optional[str] = None
    total_rows: int = 0
    total_imported: int = 0
    total_errors: int = 0
    failure_reason: Optional[str] = None
    mapping: Optional[List[ImportColumnMappingDto]] = None
    created_on: datetime.datetime = datetime.datetime(1, 1, 1)
    started_on: Optional[datetime.datetime] = None
    completed_on: Optional[datetime.datetime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImportUploadTargetDto:
    url: Optional[str] = None
    content_type: Optional[str] = None
    file: Optional[FileResourceRefDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImportFileColumnDto:
    index: int = 0
    header: Optional[str] = None
    samples: List[str] = field(default_factory=list)
    detected_type: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ImportFileAnalysisDto:
    file: Optional[FileResourceRefDto] = None
    columns: List[ImportFileColumnDto] = field(default_factory=list)
    sample_row_count: int = 0


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
class NotificationModuleDependencyItemDto:
    name: Optional[str] = None
    view_id: Optional[str] = None
    category: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotificationModuleDisableDependenciesDto:
    triggers: List[NotificationModuleDependencyItemDto] = field(default_factory=list)
    scheduler_tasks: List[NotificationModuleDependencyItemDto] = field(default_factory=list)
    in_flight_campaigns: List[NotificationModuleDependencyItemDto] = field(default_factory=list)
    membership_settings: List[NotificationModuleDependencyItemDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestEmailValidationItemDto:
    address: Optional[str] = None
    verdict: Optional[str] = None
    reason: Optional[str] = None
    score: Optional[Decimal] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TemplateListProjection(IHasViewId, IHasDatabaseId):
    id: Optional[str] = None
    view_id: Optional[str] = None
    template_name: Optional[str] = None
    is_active: bool = False
    type: Optional[CommunicationChannel] = None
    tags: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateListProjection(TemplateListProjection):
    has_attachments: bool = False
    languages: Optional[IReadOnlyList[str]] = None


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
class SystemEmailTemplateListProjection(EmailTemplateListProjection):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSignatureDto(IHasViewId):
    view_id: Optional[str] = None
    display_name: Optional[str] = None
    translations: List[TranslationDto] = field(default_factory=list)


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
class EmailFooterDto(IHasViewId):
    view_id: Optional[str] = None
    display_name: Optional[str] = None
    translations: List[TranslationDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSettings(IBindableContract):
    signatures: Optional[IList[EmailSignatureDto]] = None
    footers: Optional[IList[EmailFooterDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DomainHealthRecordItemDto:
    record: Optional[str] = None
    value: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationListProjection(IntegrationListProjection):
    email_provider: Optional[EmailProvider] = None
    sender_email_address: Optional[str] = None
    sender_display_name: Optional[str] = None


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
    errors: Optional[List[ErrorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CampaignDto(IHasResponsibleUserId, IHasDatabaseId):
    view_id: Optional[str] = None
    created_on: datetime.datetime = datetime.datetime(1, 1, 1)
    language: Optional[str] = None
    force_campaign_language: bool = False
    campaign_processing_integration_id: Optional[str] = None
    status_history: List[CampaignStatusChangeEntryDto] = field(default_factory=list)
    status: Optional[CampaignStatusChangeEntryDto] = None
    token_mapping_values: Optional[List[TokenMappingDto]] = None
    notes: Optional[str] = None
    user_id: Optional[str] = None
    id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignDto(CampaignDto):
    delivery_settings: Optional[EmailCampaignDeliverySettingsDto] = None
    template: Optional[EmailTemplateDto] = None
    validation_integration_id: Optional[str] = None
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
    errors: Optional[List[ErrorDto]] = None


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
    user_token_mappings: Optional[List[TokenMappingDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailRecipientsDto:
    to: Optional[List[EmailRecipientDto]] = None
    cc: Optional[List[EmailRecipientDto]] = None
    bcc: Optional[List[EmailRecipientDto]] = None
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
    BLOCKED_BY_VALIDATION = 'BlockedByValidation'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NotificationStatusChangeEntryDto:
    time: datetime.datetime = datetime.datetime(1, 1, 1)
    status: Optional[CampaignNotificationStatus] = None
    source_id: Optional[str] = None
    errors: Optional[List[ErrorDto]] = None
    tags: Optional[List[str]] = None


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
    status_history: List[NotificationStatusChangeEntryDto] = field(default_factory=list)
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
class SmsTemplateListProjection(TemplateListProjection):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsSettings(IBindableContract):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationListProjection(IntegrationListProjection):
    provider: Optional[SmsProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsCampaignDto(CampaignDto):
    recipients: Optional[SmsCampaignDeliverySettingsDto] = None
    template: Optional[SmsTemplateDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsRecipientDto:
    phone_number: Optional[str] = None
    user_id: Optional[str] = None
    language: Optional[str] = None
    user_token_mappings: Optional[List[TokenMappingDto]] = None
    time_zone_id: Optional[str] = None
    record: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsRecipientsDto:
    to: Optional[List[SmsRecipientDto]] = None
    starting_after: Optional[str] = None
    has_more: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsCampaignBatchDto(CampaignBatchDto):
    recipients: Optional[SmsRecipientsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsCampaignBatchNotificationDto(CampaignBatchNotificationDto):
    recipients: Optional[SmsRecipientsDto] = None
    content: Optional[SmsMessageContentDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceListingProjection(IHasViewId):
    view_id: Optional[str] = None
    slug: Optional[str] = None
    display_name: Optional[str] = None
    vendor: Optional[str] = None
    category: Optional[MarketplaceCategory] = None
    transport: Optional[MarketplaceTransport] = None
    icon_url: Optional[str] = None
    is_official: bool = False
    tags: Optional[IReadOnlyList[str]] = None
    function_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationListProjection(IHasViewId):
    view_id: Optional[str] = None
    integration_name: Optional[str] = None
    is_enabled: bool = False
    listing_view_id: Optional[str] = None
    vendor: Optional[str] = None
    category: Optional[MarketplaceCategory] = None
    transport: Optional[MarketplaceTransport] = None
    last_integration_test_at_utc: Optional[datetime.datetime] = None
    last_integration_test_succeeded: Optional[bool] = None
    last_integration_test_errors: Optional[IReadOnlyList[str]] = None
    human_delivery_confirmed_at_utc: Optional[datetime.datetime] = None
    requires_human_delivery_confirmation: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionProjection(IHasViewId):
    view_id: Optional[str] = None
    integration_view_id: Optional[str] = None
    function_key: Optional[str] = None
    display_name: Optional[str] = None
    is_enabled: bool = False
    mapping_count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationListProjection(IntegrationListProjection):
    provider: Optional[CodeProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushTemplateListProjection(TemplateListProjection):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushSettings:
    marketing_tags: Optional[List[TagDefinitionDto]] = None
    transactional_tags: Optional[List[TagDefinitionDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushIntegrationListProjection(IntegrationListProjection):
    provider: Optional[PushProvider] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushCampaignDto(CampaignDto):
    recipients: Optional[PushCampaignDeliverySettingsDto] = None
    template: Optional[PushTemplateDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushRecipientDto:
    device_tokens: List[PushDeviceDeliveryTokenDto] = field(default_factory=list)
    user_id: Optional[str] = None
    language: Optional[str] = None
    user_token_mappings: Optional[List[TokenMappingDto]] = None
    time_zone_id: Optional[str] = None
    record: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushRecipientsDto:
    to: Optional[List[PushRecipientDto]] = None
    starting_after: Optional[str] = None
    has_more: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushCampaignBatchDto(CampaignBatchDto):
    recipients: Optional[PushRecipientsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PushCampaignBatchNotificationDto(CampaignBatchNotificationDto):
    recipients: Optional[PushRecipientsDto] = None
    content: Optional[PushMessageContentDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsWebhookLogEntry:
    integration_id: Optional[str] = None
    source: Optional[str] = None
    event_name: Optional[str] = None
    provider_event_id: Optional[str] = None
    status_code: int = 0
    description: Optional[str] = None
    received_on: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentTriggerProjectionList(TriggerProjectionList):
    type: Optional[PaymentTriggerType] = None
    integrations: Optional[List[str]] = None
    events: Optional[List[str]] = None


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
class TenantLogEntryDto:
    id: Optional[str] = None
    timestamp: datetime.datetime = datetime.datetime(1, 1, 1)
    module: Optional[str] = None
    level: Optional[str] = None
    event_code: Optional[str] = None
    title: Optional[str] = None
    message: Optional[str] = None
    correlation_id: Optional[str] = None
    trace_id: Optional[str] = None
    span_id: Optional[str] = None
    meta: Optional[IReadOnlyDictionary[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiToolManifestParameter:
    name: Optional[str] = None
    type: Optional[str] = None
    required: bool = False
    description: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AiToolManifestItem:
    name: Optional[str] = None
    description: Optional[str] = None
    toolsets: List[str] = field(default_factory=list)
    requires_confirmation: bool = False
    parameters: List[AiToolManifestParameter] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatModelOption:
    llm_integration_id: Optional[str] = None
    kind: Optional[str] = None
    provider: Optional[str] = None
    model: Optional[str] = None
    label: Optional[str] = None
    is_default: bool = False
    is_auto: bool = False
    context_window: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatMemoryNote:
    id: Optional[str] = None
    kind: Optional[str] = None
    text: Optional[str] = None
    project_id: Optional[str] = None
    created_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatSessionListItem:
    session_id: Optional[str] = None
    profile: Optional[str] = None
    project_id: Optional[str] = None
    env: Optional[str] = None
    title: Optional[str] = None
    updated_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    is_archived: bool = False
    is_pinned: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectBriefSourceWireDto:
    kind: Optional[str] = None
    session_id: Optional[str] = None
    entry_id: Optional[str] = None
    entry_seq: Optional[int] = None
    event_id: Optional[str] = None
    user_auth_id: Optional[str] = None
    at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    surface: Optional[str] = None
    quote: Optional[str] = None
    work_item_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectBriefSatisfiedByWireDto:
    artifact_id: Optional[str] = None
    tool: Optional[str] = None
    orphaned: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectBriefRequirementWireDto:
    id: Optional[str] = None
    text: Optional[str] = None
    status: Optional[str] = None
    confidence: float = 0.0
    is_assumption: bool = False
    sources: List[ProjectBriefSourceWireDto] = field(default_factory=list)
    satisfied_by: List[ProjectBriefSatisfiedByWireDto] = field(default_factory=list)
    since_event_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectBriefDecisionWireDto:
    event_id: Optional[str] = None
    text: Optional[str] = None
    confidence: float = 0.0
    at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    sources: List[ProjectBriefSourceWireDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectBriefAssumptionWireDto:
    requirement_id: Optional[str] = None
    event_id: Optional[str] = None
    text: Optional[str] = None
    confidence: float = 0.0
    at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectBriefSnapshotWireDto:
    project_id: Optional[str] = None
    up_to_seq: int = 0
    at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    requirements: List[ProjectBriefRequirementWireDto] = field(default_factory=list)
    decisions: List[ProjectBriefDecisionWireDto] = field(default_factory=list)
    open_assumptions: List[ProjectBriefAssumptionWireDto] = field(default_factory=list)
    summary: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectBriefEventWireDto:
    id: Optional[str] = None
    project_id: Optional[str] = None
    seq: int = 0
    at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    kind: Optional[str] = None
    requirement_id: Optional[str] = None
    supersedes_event_id: Optional[str] = None
    text: Optional[str] = None
    confidence: float = 0.0
    sources: List[ProjectBriefSourceWireDto] = field(default_factory=list)
    origin: Optional[str] = None
    satisfied_by: List[ProjectBriefSatisfiedByWireDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WorkItemEntryRefWireDto:
    session_id: Optional[str] = None
    entry_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WorkItemRunRefWireDto:
    session_id: Optional[str] = None
    plan_entry_id: Optional[str] = None
    run_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WorkItemArtifactWireDto:
    artifact_id: Optional[str] = None
    what: Optional[str] = None
    step: int = 0
    plan_entry_id: Optional[str] = None
    kind: Optional[str] = None
    name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WorkItemMovedOutWireDto:
    text: Optional[str] = None
    reason: Optional[str] = None
    moved_to: Optional[str] = None
    source: Optional[str] = None
    entry_ref: Optional[WorkItemEntryRefWireDto] = None
    at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WorkItemNeedsYouWireDto:
    text: Optional[str] = None
    kind: Optional[str] = None
    entry_ref: Optional[WorkItemEntryRefWireDto] = None
    done: bool = False
    done_at_utc: Optional[datetime.datetime] = None
    done_by_user_auth_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WorkItemOpenQuestionWireDto:
    entry_ref: Optional[WorkItemEntryRefWireDto] = None
    blocking: bool = False
    text: Optional[str] = None
    at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WorkItemDoneConditionWireDto:
    condition: int = 0
    holds: bool = False
    reason: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WorkItemWireDto:
    id: Optional[str] = None
    project_id: Optional[str] = None
    status: Optional[str] = None
    goal: Optional[str] = None
    not_in_scope: List[str] = field(default_factory=list)
    scope_requirement_ids: List[str] = field(default_factory=list)
    difficulty: Optional[int] = None
    difficulty_reason: Optional[str] = None
    plan_entry_refs: List[WorkItemEntryRefWireDto] = field(default_factory=list)
    run_refs: List[WorkItemRunRefWireDto] = field(default_factory=list)
    artifacts: List[WorkItemArtifactWireDto] = field(default_factory=list)
    moved_out: List[WorkItemMovedOutWireDto] = field(default_factory=list)
    needs_you: List[WorkItemNeedsYouWireDto] = field(default_factory=list)
    open_questions: List[WorkItemOpenQuestionWireDto] = field(default_factory=list)
    session_ids: List[str] = field(default_factory=list)
    parent_id: Optional[str] = None
    children: List[str] = field(default_factory=list)
    summary_entry_ref: Optional[WorkItemEntryRefWireDto] = None
    created_by: Optional[str] = None
    created_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    updated_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    done_verdict: Optional[str] = None
    done_conditions: List[WorkItemDoneConditionWireDto] = field(default_factory=list)


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


class IVirtualDirectory:
    pass


class IVirtualPathProvider:
    root_directory: Optional[IVirtualDirectory] = None
    virtual_path_separator: Optional[str] = None
    real_path_separator: Optional[str] = None


class IVirtualFile:
    virtual_path_provider: Optional[IVirtualPathProvider] = None
    extension: Optional[str] = None
    length: int = 0


# @Flags()
class CacheControl(IntEnum):
    NONE = 0
    PUBLIC = 1
    PRIVATE = 2
    MUST_REVALIDATE = 4
    NO_CACHE = 8
    NO_STORE = 16
    NO_TRANSFORM = 32
    PROXY_REVALIDATE = 64


class IContentTypeWriter:
    pass


# @Flags()
class RequestAttributes(IntEnum):
    NONE = 0
    LOCALHOST = 1
    LOCAL_SUBNET = 2
    EXTERNAL = 4
    SECURE = 8
    IN_SECURE = 16
    ANY_SECURITY_MODE = 24
    HTTP_HEAD = 32
    HTTP_GET = 64
    HTTP_POST = 128
    HTTP_PUT = 256
    HTTP_DELETE = 512
    HTTP_PATCH = 1024
    HTTP_OPTIONS = 2048
    HTTP_OTHER = 4096
    ANY_HTTP_METHOD = 8160
    ONE_WAY = 8192
    REPLY = 16384
    ANY_CALL_STYLE = 24576
    SOAP11 = 32768
    SOAP12 = 65536
    XML = 131072
    JSON = 262144
    JSV = 524288
    PROTO_BUF = 1048576
    CSV = 2097152
    HTML = 4194304
    JSONL = 8388608
    MSG_PACK = 16777216
    FORMAT_OTHER = 33554432
    ANY_FORMAT = 67076096
    HTTP = 67108864
    MESSAGE_QUEUE = 134217728
    TCP = 268435456
    GRPC = 536870912
    ENDPOINT_OTHER = 1073741824
    ANY_ENDPOINT = 2080374784
    IN_PROCESS = -2147483648
    INTERNAL_NETWORK_ACCESS = -2147483645
    ANY_NETWORK_ACCESS_TYPE = -2147483641
    ANY = -1


class IRequestPreferences:
    accepts_brotli: bool = False
    accepts_deflate: bool = False
    accepts_gzip: bool = False


class IHttpFile:
    name: Optional[str] = None
    file_name: Optional[str] = None
    content_length: int = 0
    content_type: Optional[str] = None
    input_stream: Optional[bytes] = None


class IRequest:
    original_request: Optional[Object] = None
    response: Optional[IResponse] = None
    operation_name: Optional[str] = None
    verb: Optional[str] = None
    request_attributes: Optional[RequestAttributes] = None
    request_preferences: Optional[IRequestPreferences] = None
    dto: Optional[Object] = None
    content_type: Optional[str] = None
    is_local: bool = False
    user_agent: Optional[str] = None
    cookies: Optional[Dict[str, Cookie]] = None
    response_content_type: Optional[str] = None
    has_explicit_response_content_type: bool = False
    items: Optional[Dict[str, Object]] = None
    headers: Optional[NameValueCollection] = None
    query_string: Optional[NameValueCollection] = None
    form_data: Optional[NameValueCollection] = None
    use_buffered_stream: bool = False
    raw_url: Optional[str] = None
    absolute_uri: Optional[str] = None
    user_host_address: Optional[str] = None
    remote_ip: Optional[str] = None
    authorization: Optional[str] = None
    is_secure_connection: bool = False
    accept_types: Optional[List[str]] = None
    path_info: Optional[str] = None
    original_path_info: Optional[str] = None
    input_stream: Optional[bytes] = None
    content_length: int = 0
    files: Optional[List[IHttpFile]] = None
    url_referrer: Optional[str] = None
    request_aborted: Optional[CancellationToken] = None


class IResponse:
    original_response: Optional[Object] = None
    request: Optional[IRequest] = None
    status_code: int = 0
    status_description: Optional[str] = None
    content_type: Optional[str] = None
    output_stream: Optional[bytes] = None
    dto: Optional[Object] = None
    use_buffered_stream: bool = False
    is_closed: bool = False
    keep_alive: bool = False
    has_started: bool = False
    items: Optional[Dict[str, Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchedulerTaskListProjection(IHasViewId):
    task_id: Optional[str] = None
    name: Optional[str] = None
    cron: Optional[str] = None
    type: Optional[SchedulerTaskType] = None
    is_enabled: bool = False
    view_id: Optional[str] = None


class ResolvedRefStatus(str, Enum):
    OK = 'ok'
    NOT_FOUND = 'notFound'
    UNAUTHORIZED = 'unauthorized'
    SOURCE_ERROR = 'sourceError'
    ERASED = 'erased'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResolvedResourceEntry:
    ref: Optional[ResourceRefDto] = None
    status: Optional[ResolvedRefStatus] = None
    resolved: Optional[Object] = None
    diagnostic: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChannelSubscriptionStateDto:
    unsubscribed: bool = False
    blocked_tags: Dict[str, List[str]] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserDto:
    id: Optional[str] = None
    project_id: Optional[str] = None
    primary_email: Optional[str] = None
    primary_phone: Optional[str] = None
    display_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    company: Optional[str] = None
    locale: Optional[str] = None
    time_zone: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[int] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    tags: Optional[List[str]] = None
    roles: Optional[List[str]] = None
    lifecycle: Optional[str] = None
    source_of_creation: Optional[str] = None
    merged_into_contact_id: Optional[str] = None
    created_on: datetime.datetime = datetime.datetime(1, 1, 1)
    modified_on: datetime.datetime = datetime.datetime(1, 1, 1)
    auths: Optional[List[AuthDto]] = None
    marketing_preferences: Optional[Dict[str, ChannelSubscriptionStateDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConsentPurposeDto:
    key: Optional[str] = None
    name: Optional[str] = None
    channel: Optional[str] = None
    mapped_tags: List[str] = field(default_factory=list)
    regulatory_basis: List[str] = field(default_factory=list)
    description: Optional[str] = None
    is_deprecated: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RetentionWindowDto:
    data_kind: Optional[str] = None
    days: int = 0
    action: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectComplianceDto:
    regimes: List[str] = field(default_factory=list)
    consent_purposes: List[ConsentPurposeDto] = field(default_factory=list)
    retention_windows: List[RetentionWindowDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LegalHoldDto:
    id: Optional[str] = None
    subject_kind: Optional[str] = None
    subject_id: Optional[str] = None
    reason: Optional[str] = None
    placed_at: datetime.datetime = datetime.datetime(1, 1, 1)
    placed_by: Optional[str] = None
    released_at: Optional[datetime.datetime] = None
    released_by: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DsarRequestDto:
    id: Optional[str] = None
    subject_kind: Optional[str] = None
    subject_id: Optional[str] = None
    status: Optional[str] = None
    received_at: datetime.datetime = datetime.datetime(1, 1, 1)
    sla_deadline: datetime.datetime = datetime.datetime(1, 1, 1)
    auto_approve_at: Optional[datetime.datetime] = None
    decided_at: Optional[datetime.datetime] = None
    decided_by: Optional[str] = None
    rejection_reason: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ComplianceAuditEntryDto:
    id: Optional[str] = None
    timestamp: datetime.datetime = datetime.datetime(1, 1, 1)
    action: Optional[str] = None
    subject_kind: Optional[str] = None
    subject_id: Optional[str] = None
    reason: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountComplianceDto:
    dsar_mode: Optional[str] = None
    dsar_delay_days: int = 0
    auto_forward_advisories: bool = False
    security_contact: Optional[str] = None


class SupportCustomerStatus(str, Enum):
    PENDING = 'Pending'
    OPEN = 'Open'
    SOLVED = 'Solved'
    CLOSED = 'Closed'


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseDto(IHasViewId):
    view_id: Optional[str] = None
    account_id: Optional[str] = None
    project_id: Optional[str] = None
    reporter_id: Optional[str] = None
    kind: Optional[SupportCaseKind] = None
    severity: Optional[SupportCaseSeverity] = None
    status: Optional[SupportCaseStatus] = None
    customer_status: Optional[SupportCustomerStatus] = None
    subject: Optional[str] = None
    affected_module: Optional[str] = None
    deployment_mode: Optional[DeploymentMode] = None
    gateway_version: Optional[str] = None
    region: Optional[str] = None
    plan_tier: Optional[str] = None
    opened_on: int = 0
    first_response_on: Optional[int] = None
    resolved_on: Optional[int] = None
    closed_on: Optional[int] = None
    resolution: Optional[str] = None
    message_count: int = 0
    last_message_on: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseMessageDto:
    id: Optional[str] = None
    case_id: Optional[str] = None
    author_kind: Optional[SupportMessageAuthorKind] = None
    author_id: Optional[str] = None
    author_display_name: Optional[str] = None
    body: Optional[str] = None
    sent_on: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseDetailDto:
    case: Optional[SupportCaseDto] = None
    messages: List[SupportCaseMessageDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseListProjection(IHasViewId):
    view_id: Optional[str] = None
    project_id: Optional[str] = None
    kind: Optional[SupportCaseKind] = None
    severity: Optional[SupportCaseSeverity] = None
    status: Optional[SupportCaseStatus] = None
    customer_status: Optional[SupportCustomerStatus] = None
    subject: Optional[str] = None
    opened_on: int = 0
    message_count: int = 0
    last_message_on: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticPackStepDescriptorDto:
    step_id: Optional[str] = None
    kind: Optional[str] = None
    description: Optional[str] = None
    parameters: Dict[str, str] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticPackDescriptorDto:
    name: Optional[str] = None
    version: int = 0
    summary: Optional[str] = None
    steps: List[DiagnosticPackStepDescriptorDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticPackStepResultDto:
    step_id: Optional[str] = None
    kind: Optional[str] = None
    is_success: bool = False
    result: Optional[Object] = None
    error_message: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticPackRunResultDto:
    pack_name: Optional[str] = None
    pack_version: int = 0
    case_id: Optional[str] = None
    steps: List[DiagnosticPackStepResultDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticEchoRegionDto:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticEchoDto:
    container_name: Optional[str] = None
    is_managed_service: bool = False
    api_version: Optional[str] = None
    hub_version: Optional[str] = None
    release: Optional[str] = None
    runtime: Optional[str] = None
    hub_url: Optional[str] = None
    api_url: Optional[str] = None
    license_present: bool = False
    regions: Optional[List[DiagnosticEchoRegionDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticEventItemDto:
    position: int = 0
    event_type: Optional[str] = None
    payload: Optional[Dict[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticEventsPageDto:
    stream: Optional[str] = None
    from_: int = field(metadata=config(field_name='from'), default=0)
    count: int = 0
    has_more: bool = False
    next_from: int = 0
    items: List[DiagnosticEventItemDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticLogsResponse:
    list: Optional[PaginatedResponse[TenantLogEntryDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticRedisListItemDto:
    view_id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticRedisInspectDto:
    key_pattern: Optional[str] = None
    cache_key: Optional[str] = None
    is_list: bool = False
    item: Optional[Dict[str, Object]] = None
    list_items: Optional[List[DiagnosticRedisListItemDto]] = None
    has_more: bool = False
    starting_after: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiagnosticHealthCheckDto:
    check_id: Optional[str] = None
    is_healthy: bool = False
    status_code: int = 0
    detail: Optional[str] = None


class ILlmApiKeyRequest:
    api_key: Optional[str] = None


class IHasViewId:
    view_id: Optional[str] = None


class IHasDatabaseId:
    id: Optional[str] = None


class IBindableContract:
    pass


class IHasRazorTemplateCode:
    pass


class IHasDomainEntityId:
    view_id: Optional[str] = None


class IIntegrationIdentification:
    integration_id: Optional[IntegrationId] = None
    capability: Optional[str] = None
    is_system_owned: bool = False


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
class GetAccountUsageBillingResponse(ResponseBase):
    item: Optional[UsageBillingDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PromoteEnvironmentResponse(ResponseBase):
    item: Optional[PromotionResultDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjectEnvironmentsResponse(ResponseBase):
    item: Optional[ProjectEnvironmentsDto] = None


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
class WaitForProjectActiveResponse(ResponseBase):
    status: Optional[str] = None
    is_active: bool = False
    waited_seconds: int = 0
    message: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjectTokensResponse(ResponseBase):
    tokens: Optional[List[TokenMappingDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AdminPortalStructureDto:
    project_id: Optional[str] = None
    admin_portal_enabled: bool = False
    display_name: Optional[str] = None
    modules: List[AdminPortalModuleDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateAccountResponse(IdResponse):
    token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountCollaboratorsResponse(ResponseBase):
    list: Optional[PaginatedResponse[AuthDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountPasswordPolicyResponse(ResponseBase):
    policy: Optional[AccountPasswordPolicyDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountTeamPoliciesResponse(ResponseBase):
    policies: Optional[List[PolicyItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountTeamRolesResponse(ResponseBase):
    roles: Optional[List[AccountTeamRoleDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyOkResponse(ResponseBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyVerificationTokenResponse(ResponseBase):
    verification_token: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyCeremonyOptionsResponse(ResponseBase):
    ceremony_id: Optional[str] = None
    options_json: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyAuthTokensResponse(ResponseBase):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_in_seconds: int = 0
    recovery_codes: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyListResponse(ResponseBase):
    passkeys: List[AccountPasskeyListItemDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyEnrollmentResponse(ResponseBase):
    recovery_codes: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLicenseDomainDnsStatusResponse(ResponseBase):
    status: Optional[LicenseDomainDnsStatusDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StartLicenseDomainVerificationResponse(ResponseBase):
    challenge: Optional[LicenseDomainVerificationChallengeDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLicenseDomainVerificationStatusResponse(ResponseBase):
    status: Optional[LicenseDomainVerificationStatusDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLicensesResponse(ResponseBase):
    list: Optional[List[LicenseDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PostLicenseHeartbeatResponse(ResponseBase):
    verdict: Optional[LicenseHeartbeatVerdictDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetInstallationLicenseStatusResponse(ResponseBase):
    status: Optional[InstallationLicenseStatusDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IssueServiceUserApiKeyResponse:
    id: int = 0
    name: Optional[str] = None
    key: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListServiceUserApiKeysResponse:
    keys: List[ServiceUserApiKeyDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipTriggerResponse(GetTriggerResponse):
    trigger: Optional[MembershipTriggerDto] = None


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
class GetPasskeySettingsResponse(ResponseBase):
    result: Optional[PasskeySettingsDto] = None


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
class GetAuthorizationSettingsResponse(ResponseBase):
    result: Optional[MembershipAuthorizationViewDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdatePasswordComplexityResponse(ResponseBase):
    result: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAuthenticationSettingsResponse(ResponseBase):
    result: Optional[MembershipAuthenticationViewDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchemaTriggerResponse(GetTriggerResponse):
    trigger: Optional[SchemaTriggerDto] = None


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
class GetDatabaseTaxonomyTreeResponse(ResponseBase):
    tree: Optional[List[TaxonomyTreeDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomyTermResponse(ResponseBase):
    item: Optional[TermDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseMergedTermTreeResponse(ResponseBase):
    tree: Optional[List[TermTreeDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomyTermTreeResponse(ResponseBase):
    tree: Optional[List[TermTreeDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ApplyDatabaseSchemaBundleResponse(ResponseBase):
    tier: Optional[str] = None
    taxonomies: List[AppliedTaxonomyDto] = field(default_factory=list)
    collections: List[AppliedCollectionDto] = field(default_factory=list)
    decisions: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


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
class GetDatabaseSchemaListSettingsResponse(ResponseBase):
    settings: Optional[SchemaListSettingsDto] = None


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
class AggregateRecordsResponse(ResponseBase):
    result: Optional[List[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CountRecordsResponse(ResponseBase):
    count: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DistinctRecordValuesResponse(ResponseBase):
    values: Optional[List[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ExecuteRecordsAggregateResponse(ResponseBase):
    result: Optional[List[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindRecordsResponse(ResponseBase):
    list: Optional[PaginatedResponse[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindOneRecordResponse(ResponseBase):
    result: Optional[Object] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCollectionIndexesResponse(ResponseBase):
    indexes: Optional[List[CollectionIndexDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SeedCollectionRecordsResponse(ResponseBase):
    result: Optional[SeedCollectionRecordsResultDto] = None


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
class GetAllowedFlexTiersResponse(ResponseBase):
    tiers: Optional[List[FlexTierDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RevealManagedFlexConnectionStringResponse(ResponseBase):
    connection_string: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestDatabaseIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCollectionImportResponse(ResponseBase):
    result: Optional[CollectionImportDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCollectionImportsResponse(ResponseBase):
    result: Optional[PaginatedResponse[CollectionImportDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestImportUploadUrlResponse(ResponseBase):
    result: Optional[ImportUploadTargetDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AnalyzeImportFileResponse(ResponseBase):
    result: Optional[ImportFileAnalysisDto] = None


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
    trigger: Optional[FilesTriggerDto] = None


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
class TestFilesIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFolderFilesResponse(ResponseBase):
    list: Optional[PaginatedResponse[FileResourceRefDto]] = None
    folders: Optional[IList[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetNotificationModuleDisableDependenciesResponse(ResponseBase):
    dependencies: Optional[NotificationModuleDisableDependenciesDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestEmailValidationIntegrationResponse(ResponseBase):
    items: List[TestEmailValidationItemDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplateResponse(ResponseBase):
    item: Optional[EmailTemplateDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplatesResponse(ResponseBase):
    list: Optional[PaginatedResponse[EmailTemplateListProjection]] = None


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
class CheckEmailIntegrationDomainHealthResponse(ResponseBase):
    domain: Optional[str] = None
    items: Optional[IReadOnlyList[DomainHealthRecordItemDto]] = None


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
class GetSmsTemplateResponse(ResponseBase):
    item: Optional[SmsTemplateDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsTemplatesResponse(ResponseBase):
    list: Optional[PaginatedResponse[SmsTemplateListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsMessageContentTokensResponse(ResponseBase):
    tokens: Optional[Dict[str, List[str]]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RenderSmsTextResponse(ResponseBase):
    variables: Optional[List[str]] = None
    text: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsSettingsResponse(ResponseBase):
    settings: Optional[SmsSettings] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsIntegrationResponse(ResponseBase):
    item: Optional[SmsIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsIntegrationsResponse(ResponseBase):
    default_integration_id: Optional[str] = None
    list: Optional[PaginatedResponse[SmsIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestSmsIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignResponse(ResponseBase):
    sms_campaign: Optional[SmsCampaignDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignsResponse(ResponseBase):
    list: Optional[PaginatedResponse[SmsCampaignDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignBatchesResponse(ResponseBase):
    list: Optional[PaginatedResponse[SmsCampaignBatchDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignBatchNotificationResponse(ResponseBase):
    campaign_notification: Optional[SmsCampaignBatchNotificationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignBatchNotificationsResponse(ResponseBase):
    batch_status_history: Optional[List[BatchStatusChangeEntryDto]] = None
    list: Optional[PaginatedResponse[SmsCampaignBatchNotificationDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignStatisticsResponse(ResponseBase):
    stats: Optional[CampaignStatsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PreviewSmsNotificationResponse(ResponseBase):
    body: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignMessageResponse(ResponseBase):
    sms_message_entity: Optional[SmsCampaignBatchNotificationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignMessagesResponse(ResponseBase):
    list: Optional[PaginatedResponse[SmsCampaignBatchNotificationDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceListingResponse(ResponseBase):
    listing: Optional[MarketplaceListingDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceTokensResponse(ResponseBase):
    tokens: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceListingsResponse(ResponseBase):
    list: Optional[PaginatedResponse[MarketplaceListingProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceIntegrationResponse(ResponseBase):
    integration: Optional[MarketplaceIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceIntegrationsResponse(ResponseBase):
    list: Optional[PaginatedResponse[MarketplaceIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmptyMarketplaceSecretsResponse(ResponseBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RevealMarketplaceIntegrationSecretsResponse(ResponseBase):
    secrets: Optional[IReadOnlyDictionary[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestMarketplaceIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetMarketplaceIntegrationTokenMappingsResponse(ResponseBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceFunctionResponse(ResponseBase):
    function: Optional[MarketplaceFunctionDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceFunctionsResponse(ResponseBase):
    list: Optional[PaginatedResponse[MarketplaceFunctionProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceFunctionCatalogResponse(ResponseBase):
    functions: Optional[IReadOnlyList[MarketplaceFunctionDefinitionDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InvokeMarketplaceFunctionResponse(ResponseBase):
    is_success: bool = False
    output: Optional[Object] = None
    vendor_request_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCodeIntegrationResponse(ResponseBase):
    item: Optional[CodeIntegrationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCodeIntegrationsResponse(ResponseBase):
    list: Optional[PaginatedResponse[CodeIntegrationListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestCodeIntegrationResponse(ResponseBase):
    items: Optional[IReadOnlyList[IntegrationTestResultItemDto]] = None


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
class RenderPushResponse(ResponseBase):
    variables: Optional[List[str]] = None
    title: Optional[str] = None
    body: Optional[str] = None
    subtitle: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushSettingsResponse(ResponseBase):
    settings: Optional[PushSettings] = None


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
class GetPushCampaignResponse(ResponseBase):
    item: Optional[PushCampaignDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignsResponse(ResponseBase):
    list: Optional[PaginatedResponse[PushCampaignDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignBatchesResponse(ResponseBase):
    list: Optional[PaginatedResponse[PushCampaignBatchDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignBatchNotificationResponse(ResponseBase):
    campaign_notification: Optional[PushCampaignBatchNotificationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignBatchNotificationsResponse(ResponseBase):
    batch_status_history: Optional[List[BatchStatusChangeEntryDto]] = None
    list: Optional[PaginatedResponse[PushCampaignBatchNotificationDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignStatisticsResponse(ResponseBase):
    stats: Optional[CampaignStatsDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PreviewPushNotificationResponse(ResponseBase):
    title: Optional[str] = None
    body: Optional[str] = None
    subtitle: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignMessageResponse(ResponseBase):
    push_message_entity: Optional[PushCampaignBatchNotificationDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignMessagesResponse(ResponseBase):
    list: Optional[PaginatedResponse[PushCampaignBatchNotificationDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsWebhookLogResponse(ResponseBase):
    list: Optional[IReadOnlyList[PaymentsWebhookLogEntry]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsTriggerResponse(GetTriggerResponse):
    trigger: Optional[PaymentTriggerDto] = None


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
class CleanLogsResponse(ResponseBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLogsByCorrelationIdResponse(ResponseBase):
    items: Optional[IReadOnlyList[TenantLogEntryDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLogsResponse(ResponseBase):
    list: Optional[PaginatedResponse[TenantLogEntryDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLogSettingsResponse(ResponseBase):
    skip_cloud_dashboard_logs: bool = False
    skip_http_body_meta: bool = False
    ai_chat_logging_enabled: bool = False
    has_norbix_logging: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveLogSettingsResponse(ResponseBase):
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAiToolsResponse(ResponseBase):
    tools: Optional[List[AiToolManifestItem]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InvokeAiToolResponse(ResponseBase):
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AskChatResponse(ResponseBase):
    result: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UploadChatAttachmentResponse(ResponseBase):
    id: Optional[str] = None
    session_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatAvailabilityResponse(ResponseBase):
    available: bool = False
    reason: Optional[str] = None
    profiles: Optional[List[str]] = None
    models: Optional[List[ChatModelOption]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetChatMemoryResponse(ResponseBase):
    notes: Optional[List[ChatMemoryNote]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetChatSessionsResponse(ResponseBase):
    sessions: Optional[List[ChatSessionListItem]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetChatSessionEntriesResponse(ResponseBase):
    session_id: Optional[str] = None
    profile: Optional[str] = None
    project_id: Optional[str] = None
    env: Optional[str] = None
    entries: Optional[List[AiChatEntryWireDto]] = None
    last_seq: int = 0
    active_work_item_ids: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatTurnResponse(ResponseBase):
    session_id: Optional[str] = None
    reply: Optional[str] = None
    screen_patch: Optional[ChatScreenContextDto] = None
    tool_trace: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjectBriefResponse(ResponseBase):
    project_id: Optional[str] = None
    snapshot: Optional[ProjectBriefSnapshotWireDto] = None
    events: Optional[List[ProjectBriefEventWireDto]] = None
    last_seq: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetWorkItemsResponse(ResponseBase):
    project_id: Optional[str] = None
    work_items: Optional[List[WorkItemWireDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetWorkItemResponse(ResponseBase):
    work_item: Optional[WorkItemWireDto] = None
    plans: Optional[List[AiChatEntryWireDto]] = None
    steps: Optional[List[AiChatEntryWireDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ExportWorkItemResponse(ResponseBase):
    work_item_id: Optional[str] = None
    markdown: Optional[str] = None


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
class HttpResult:
    response_text: Optional[str] = None
    response_stream: Optional[bytes] = None
    file_info: Optional[FileInfo] = None
    virtual_file: Optional[IVirtualFile] = None
    content_type: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    cookies: Optional[List[Cookie]] = None
    e_tag: Optional[str] = None
    age: Optional[datetime.timedelta] = None
    max_age: Optional[datetime.timedelta] = None
    expires: Optional[datetime.datetime] = None
    last_modified: Optional[datetime.datetime] = None
    cache_control: Optional[CacheControl] = None
    result_scope: Optional[Func[IDisposable]] = None
    allows_partial_response: bool = False
    options: Optional[Dict[str, str]] = None
    status: int = 0
    status_code: Optional[HttpStatusCode] = None
    status_description: Optional[str] = None
    response: Optional[Object] = None
    response_filter: Optional[IContentTypeWriter] = None
    request_context: Optional[IRequest] = None
    view: Optional[str] = None
    template: Optional[str] = None
    padding_length: int = 0
    is_partial_request: bool = False


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


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResolveResourcesResponse(ResponseBase):
    resolved: Optional[IReadOnlyList[ResolvedResourceEntry]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetContactResponse(ResponseBase):
    item: Optional[UserDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAllContactsResponse(ResponseBase):
    items: Optional[IReadOnlyList[UserDto]] = None
    next_cursor: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetComplianceSettingsResponse(ResponseBase):
    settings: Optional[ProjectComplianceDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLegalHoldsResponse(ResponseBase):
    holds: List[LegalHoldDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDsarRequestsResponse(ResponseBase):
    requests: List[DsarRequestDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetComplianceAuditLogResponse(ResponseBase):
    entries: List[ComplianceAuditEntryDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountComplianceResponse(ResponseBase):
    settings: Optional[AccountComplianceDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSupportCaseResponse(ResponseBase):
    result: Optional[SupportCaseDetailDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSupportCasesResponse(ResponseBase):
    list: Optional[PaginatedResponse[SupportCaseListProjection]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDiagnosticPacksResponse(ResponseBase):
    packs: Optional[List[DiagnosticPackDescriptorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RunDiagnosticPackResponse(ResponseBase):
    result: Optional[DiagnosticPackRunResultDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDiagnosticEchoResponse(ResponseBase):
    result: Optional[DiagnosticEchoDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReadDiagnosticEventsResponse(ResponseBase):
    result: Optional[DiagnosticEventsPageDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryDiagnosticLogsResponse(ResponseBase):
    result: Optional[DiagnosticLogsResponse] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InspectDiagnosticRedisResponse(ResponseBase):
    result: Optional[DiagnosticRedisInspectDto] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RunDiagnosticHealthCheckResponse(ResponseBase):
    result: Optional[DiagnosticHealthCheckDto] = None


# @Route("/{version}/code/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableCode(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/code/disable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableCode(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/code/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCodeIntegrations(CodeMashListPaginationRequestBase, IReturn[GetCodeIntegrationsResponse]):
    pass


# @Route("/{version}/code/integrations/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCodeIntegration(CodeMashRequestBase, IReturn[GetCodeIntegrationResponse]):
    # @ApiMember(Description="Integration id, from get_code_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_code_integrations.
    """


# @Route("/{version}/code/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveCodeIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    integration: Optional[CodeIntegrationRequest] = None


# @Route("/{version}/code/integrations/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestCodeIntegration(CodeMashRequestBase, IReturn[TestCodeIntegrationResponse]):
    # @ApiMember(Description="Integration id, from get_code_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    Integration id, from get_code_integrations.
    """


# @Route("/{version}/code/integrations/confirm-human-delivery", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmCodeIntegrationHumanDeliveryRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Integration id, from get_code_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    Integration id, from get_code_integrations.
    """


# @Route("/{version}/code/integrations/{Id}/default", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetCodeIntegrationAsDefault(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Integration id, from get_code_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_code_integrations.
    """


# @Route("/{version}/code/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteCodeIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Integration id, from get_code_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_code_integrations.
    """


# @Route("/{version}/code/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableCodeIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Integration id, from get_code_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_code_integrations.
    """


# @Route("/{version}/code/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableCodeIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Integration id, from get_code_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_code_integrations.
    """


# @Route("/{version}/code/marketplace/listings", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceListings(CodeMashListPaginationRequestBase, IReturn[GetMarketplaceListingsResponse]):
    # @ApiMember(Description="Filter by one or more categories (Crm, Erp, Communication, etc.).")
    categories: Optional[List[MarketplaceCategory]] = None
    """
    Filter by one or more categories (Crm, Erp, Communication, etc.).
    """


    # @ApiMember(Description="Filter by transport (Mcp, Rest, Code).")
    transports: Optional[List[MarketplaceTransport]] = None
    """
    Filter by transport (Mcp, Rest, Code).
    """


    # @ApiMember(Description="Free-text search over the listing's display name, vendor, and description.")
    search: Optional[str] = None
    """
    Free-text search over the listing's display name, vendor, and description.
    """


    # @ApiMember(Description="If true, return only listings curated and verified by Norbix.")
    official_only: Optional[bool] = None
    """
    If true, return only listings curated and verified by Norbix.
    """


    # @ApiMember(Description="Filter by curated tag slugs (e.g. ai-llm, messaging, crm). Matches listings carrying any of the given tags.")
    tags: Optional[List[str]] = None
    """
    Filter by curated tag slugs (e.g. ai-llm, messaging, crm). Matches listings carrying any of the given tags.
    """


# @Route("/{version}/code/marketplace/listings/{ListingViewId}/functions/{FunctionKey}/tokens", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceListingFunctionTokens(CodeMashRequestBase, IReturn[GetMarketplaceTokensResponse]):
    # @ApiMember(Description="Marketplace listing view id, from get_marketplace_listings.", IsRequired=true)
    listing_view_id: Optional[str] = None
    """
    Marketplace listing view id, from get_marketplace_listings.
    """


    # @ApiMember(Description="Function key on the listing, from get_marketplace_listings.", IsRequired=true)
    function_key: Optional[str] = None
    """
    Function key on the listing, from get_marketplace_listings.
    """


# @Route("/{version}/code/marketplace/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceIntegrations(CodeMashListPaginationRequestBase, IReturn[GetMarketplaceIntegrationsResponse]):
    pass


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceIntegration(CodeMashRequestBase, IReturn[GetMarketplaceIntegrationResponse]):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


# @Route("/{version}/code/marketplace/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveMarketplaceIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="The marketplace integration to install, from a get_marketplace_listings entry.", IsRequired=true)
    integration: Optional[MarketplaceIntegrationDto] = None
    """
    The marketplace integration to install, from a get_marketplace_listings entry.
    """


    secrets: Dict[str, str] = field(default_factory=dict)


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteMarketplaceIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/enable", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableMarketplaceIntegration(CodeMashRequestBase):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/disable", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableMarketplaceIntegration(CodeMashRequestBase):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/functions", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceFunctions(CodeMashListPaginationRequestBase, IReturn[GetMarketplaceFunctionsResponse]):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceFunction(CodeMashRequestBase, IReturn[GetMarketplaceFunctionResponse]):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


    # @ApiMember(Description="Function view id, from get_marketplace_functions.", IsRequired=true)
    function_view_id: Optional[str] = None
    """
    Function view id, from get_marketplace_functions.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/functions", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveMarketplaceFunction(CodeMashRequestBase):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


    # @ApiMember(Description="The function to create: functionKey, displayName, description, and one mapping per vendor function parameter.", IsRequired=true)
    function: Optional[MarketplaceFunctionDto] = None
    """
    The function to create: functionKey, displayName, description, and one mapping per vendor function parameter.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteMarketplaceFunction(CodeMashRequestBase):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


    # @ApiMember(Description="Function view id, from get_marketplace_functions.", IsRequired=true)
    function_view_id: Optional[str] = None
    """
    Function view id, from get_marketplace_functions.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/enable", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableMarketplaceFunction(CodeMashRequestBase):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


    # @ApiMember(Description="Function view id, from get_marketplace_functions.", IsRequired=true)
    function_view_id: Optional[str] = None
    """
    Function view id, from get_marketplace_functions.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/disable", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableMarketplaceFunction(CodeMashRequestBase):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


    # @ApiMember(Description="Function view id, from get_marketplace_functions.", IsRequired=true)
    function_view_id: Optional[str] = None
    """
    Function view id, from get_marketplace_functions.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/functions/{FunctionViewId}/tokens", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceFunctionTokens(CodeMashRequestBase, IReturn[GetMarketplaceTokensResponse]):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


    # @ApiMember(Description="Function view id, from get_marketplace_functions.", IsRequired=true)
    function_view_id: Optional[str] = None
    """
    Function view id, from get_marketplace_functions.
    """


# @Route("/{version}/code/marketplace/functions/{FunctionViewId}/invoke", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InvokeMarketplaceFunction(CodeMashRequestBase, IReturn[InvokeMarketplaceFunctionResponse]):
    # @ApiMember(Description="Function view id (func_…), from get_marketplace_functions.", IsRequired=true)
    function_view_id: Optional[str] = None
    """
    Function view id (func_…), from get_marketplace_functions.
    """


    payload: Dict[str, Object] = field(default_factory=dict)


# @Route("/{version}/code/marketplace/listings/{ListingViewId}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceListing(CodeMashRequestBase, IReturn[GetMarketplaceListingResponse]):
    # @ApiMember(Description="Listing view id (ml_…), from get_marketplace_listings.", IsRequired=true)
    listing_view_id: Optional[str] = None
    """
    Listing view id (ml_…), from get_marketplace_listings.
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestMarketplaceIntegration(CodeMashRequestBase, IReturn[TestMarketplaceIntegrationResponse]):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


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
    typegen_15__mongo_db_connection_string_database_integration_request: Optional[MongoDbConnectionStringDatabaseIntegrationRequest] = None
    typegen_16__mongo_db_atlas_flex_managed_database_integration_request: Optional[MongoDbAtlasFlexManagedDatabaseIntegrationRequest] = None
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
    typegen_28__new_relic_logging_integration_request: Optional[NewRelicLoggingIntegrationRequest] = None
    typegen_30__mongo_db_logging_integration_request: Optional[MongoDbLoggingIntegrationRequest] = None
    typegen_31__kafka_logging_integration_request: Optional[KafkaLoggingIntegrationRequest] = None
    typegen_32__prometheus_logging_integration_request: Optional[PrometheusLoggingIntegrationRequest] = None
    typegen_33__data_dog_logging_integration_request: Optional[DataDogLoggingIntegrationRequest] = None
    typegen_34__internal_kafka_logging_integration_request: Optional[InternalKafkaLoggingIntegrationRequest] = None
    typegen_35__elastic_search_logging_integration_request: Optional[ElasticSearchLoggingIntegrationRequest] = None
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
    typegen_236__trigger_action_sms_dto: Optional[TriggerActionSmsDto] = None
    typegen_237__trigger_action_sse_dto: Optional[TriggerActionSseDto] = None
    typegen_238__trigger_action_marketplace_dto: Optional[TriggerActionMarketplaceDto] = None
    typegen_239__sse_delivery_settings_dto: Optional[SseDeliverySettingsDto] = None
    typegen_240__get_triggers: Optional[GetTriggers] = None
    typegen_241__get_triggers_response: Optional[GetTriggersResponse] = None
    typegen_90__email_to_all_users_delivery_settings_dto: Optional[EmailToAllUsersDeliverySettingsDto] = None
    typegen_91__email_to_account_users_delivery_settings_dto: Optional[EmailToAccountUsersDeliverySettingsDto] = None
    typegen_92__email_to_users_delivery_settings_dto: Optional[EmailToUsersDeliverySettingsDto] = None
    typegen_93__email_to_email_addresses_delivery_settings_dto: Optional[EmailToEmailAddressesDeliverySettingsDto] = None
    typegen_94__email_to_collection_records_delivery_settings_dto: Optional[EmailToCollectionRecordsDeliverySettingsDto] = None
    typegen_95__push_to_all_users_delivery_settings_dto: Optional[PushToAllUsersDeliverySettingsDto] = None
    typegen_96__push_to_users_delivery_settings_dto: Optional[PushToUsersDeliverySettingsDto] = None
    typegen_229__push_to_account_users_delivery_settings_dto: Optional[PushToAccountUsersDeliverySettingsDto] = None
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
    typegen_147__mongo_db_logging_integration_dto: Optional[MongoDbLoggingIntegrationDto] = None
    typegen_148__new_relic_logging_integration_dto: Optional[NewRelicLoggingIntegrationDto] = None
    typegen_149__prometheus_logging_integration_dto: Optional[PrometheusLoggingIntegrationDto] = None
    typegen_150__splunk_logging_integration_dto: Optional[SplunkLoggingIntegrationDto] = None
    typegen_153__apple_i_cloud_files_integration_dto: Optional[AppleICloudFilesIntegrationDto] = None
    typegen_154__aws_s3_cross_account_role_files_integration_dto: Optional[AwsS3CrossAccountRoleFilesIntegrationDto] = None
    typegen_155__aws_s3_iam_files_integration_dto: Optional[AwsS3IamFilesIntegrationDto] = None
    typegen_156__azure_blob_files_integration_dto: Optional[AzureBlobFilesIntegrationDto] = None
    typegen_157__drop_box_files_integration_dto: Optional[DropBoxFilesIntegrationDto] = None
    typegen_158__ftp_files_integration_dto: Optional[FtpFilesIntegrationDto] = None
    typegen_159__google_cloud_files_integration_dto: Optional[GoogleCloudFilesIntegrationDto] = None
    typegen_160__google_drive_files_integration_dto: Optional[GoogleDriveFilesIntegrationDto] = None
    typegen_161__local_files_integration_dto: Optional[LocalFilesIntegrationDto] = None
    typegen_164__mongo_db_connection_string_integration_dto: Optional[MongoDbConnectionStringIntegrationDto] = None
    typegen_165__mongo_db_atlas_flex_managed_integration_dto: Optional[MongoDbAtlasFlexManagedIntegrationDto] = None
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
    typegen_197__marketplace_function_dto: Optional[MarketplaceFunctionDto] = None
    typegen_198__marketplace_listing_dto: Optional[MarketplaceListingDto] = None
    typegen_199__marketplace_function_definition_dto: Optional[MarketplaceFunctionDefinitionDto] = None
    typegen_200__marketplace_function_parameter_dto: Optional[MarketplaceFunctionParameterDto] = None
    typegen_201__enable_code: Optional[EnableCode] = None
    typegen_202__disable_code: Optional[DisableCode] = None
    typegen_203__get_code_integrations: Optional[GetCodeIntegrations] = None
    typegen_204__get_code_integration: Optional[GetCodeIntegration] = None
    typegen_205__save_code_integration: Optional[SaveCodeIntegration] = None
    typegen_206__test_code_integration: Optional[TestCodeIntegration] = None
    typegen_207__confirm_code_integration_human_delivery_request: Optional[ConfirmCodeIntegrationHumanDeliveryRequest] = None
    typegen_208__set_code_integration_as_default: Optional[SetCodeIntegrationAsDefault] = None
    typegen_209__delete_code_integration_request: Optional[DeleteCodeIntegrationRequest] = None
    typegen_210__enable_code_integration_request: Optional[EnableCodeIntegrationRequest] = None
    typegen_211__disable_code_integration_request: Optional[DisableCodeIntegrationRequest] = None
    typegen_212__get_marketplace_listings: Optional[GetMarketplaceListings] = None
    typegen_213__get_marketplace_listing_function_tokens: Optional[GetMarketplaceListingFunctionTokens] = None
    typegen_214__get_marketplace_integrations: Optional[GetMarketplaceIntegrations] = None
    typegen_215__get_marketplace_integration: Optional[GetMarketplaceIntegration] = None
    typegen_216__save_marketplace_integration: Optional[SaveMarketplaceIntegration] = None
    typegen_217__delete_marketplace_integration: Optional[DeleteMarketplaceIntegration] = None
    typegen_218__enable_marketplace_integration: Optional[EnableMarketplaceIntegration] = None
    typegen_219__disable_marketplace_integration: Optional[DisableMarketplaceIntegration] = None
    typegen_221__get_marketplace_functions: Optional[GetMarketplaceFunctions] = None
    typegen_222__get_marketplace_function: Optional[GetMarketplaceFunction] = None
    typegen_223__save_marketplace_function: Optional[SaveMarketplaceFunction] = None
    typegen_224__delete_marketplace_function: Optional[DeleteMarketplaceFunction] = None
    typegen_225__enable_marketplace_function: Optional[EnableMarketplaceFunction] = None
    typegen_226__disable_marketplace_function: Optional[DisableMarketplaceFunction] = None
    typegen_227__get_marketplace_function_tokens: Optional[GetMarketplaceFunctionTokens] = None
    typegen_228__invoke_marketplace_function: Optional[InvokeMarketplaceFunction] = None
    typegen_232__get_marketplace_listing: Optional[GetMarketplaceListing] = None
    typegen_233__test_marketplace_integration: Optional[TestMarketplaceIntegration] = None
    typegen_234__test_marketplace_integration_response: Optional[TestMarketplaceIntegrationResponse] = None
    typegen_235__get_marketplace_listing_response: Optional[GetMarketplaceListingResponse] = None
    typegen_230__admin_portal_structure_dto: Optional[AdminPortalStructureDto] = None
    typegen_231__admin_portal_module_dto: Optional[AdminPortalModuleDto] = None
    typegen_236__user_message_entry_wire_dto: Optional[UserMessageEntryWireDto] = None
    typegen_237__assistant_text_entry_wire_dto: Optional[AssistantTextEntryWireDto] = None
    typegen_238__assistant_question_entry_wire_dto: Optional[AssistantQuestionEntryWireDto] = None
    typegen_239__user_answer_entry_wire_dto: Optional[UserAnswerEntryWireDto] = None
    typegen_240__plan_entry_wire_dto: Optional[PlanEntryWireDto] = None
    typegen_241__user_decision_entry_wire_dto: Optional[UserDecisionEntryWireDto] = None
    typegen_242__run_step_entry_wire_dto: Optional[RunStepEntryWireDto] = None
    typegen_243__action_pending_entry_wire_dto: Optional[ActionPendingEntryWireDto] = None
    typegen_244__notice_entry_wire_dto: Optional[NoticeEntryWireDto] = None
    typegen_245__conversation_snapshot_entry_wire_dto: Optional[ConversationSnapshotEntryWireDto] = None


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


# @Route("/{version}/account/profile", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountProfile(RequestBase, IReturn[GetAccountProfileResponse]):
    pass


# @Route("/{version}/account/profile", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAccountProfile(RequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Account owner's display name.", IsRequired=true)
    display_name: Optional[str] = None
    """
    Account owner's display name.
    """


    # @ApiMember(Description="Email address used for billing communications.")
    billing_email: Optional[str] = None
    """
    Email address used for billing communications.
    """


    # @ApiMember(Description="Email address used for operations communications.")
    operations_email: Optional[str] = None
    """
    Email address used for operations communications.
    """


    # @ApiMember(Description="Email address used for security-related communications.")
    security_email: Optional[str] = None
    """
    Email address used for security-related communications.
    """


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
    # @ApiMember(Description="Which subscription (e.g. main account plan) to open the billing portal for.")
    subscription_type: Optional[SubscriptionType] = None
    """
    Which subscription (e.g. main account plan) to open the billing portal for.
    """


    # @ApiMember(Description="URL to return to after the customer leaves the billing portal.")
    return_url: Optional[str] = None
    """
    URL to return to after the customer leaves the billing portal.
    """


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


# @Route("/{version}/account/usage-billing", "GET")
# @Api(Description="Get Account Usage Billing.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountUsageBilling(RequestBase, IReturn[GetAccountUsageBillingResponse]):
    """
    Get Account Usage Billing.
    """

    pass


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
    # @ApiMember(Description="Tag identifying the notification group to remove.", IsRequired=true)
    group_tag: Optional[str] = None
    """
    Tag identifying the notification group to remove.
    """


# @Route("/{version}/account/projects/{projectId}/notifications/settings/tag", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteNotificationsTag(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Tag identifying the notification tag to delete.", IsRequired=true)
    tag: Optional[str] = None
    """
    Tag identifying the notification tag to delete.
    """


# @Route("/{version}/account/projects/{projectId}/notifications/settings/group/tag", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveTagFromNotificationsGroup(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Tag identifying the notification group.", IsRequired=true)
    group_tag: Optional[str] = None
    """
    Tag identifying the notification group.
    """


    # @ApiMember(Description="Tag identifying the notification tag to remove from the group.", IsRequired=true)
    tag: Optional[str] = None
    """
    Tag identifying the notification tag to remove from the group.
    """


# @Route("/{version}/account/projects/{projectId}/notifications/settings/group", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveNotificationsGroup(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="The group's tag and translations to save. The tag identifies the group; translations provide its display name per locale.", IsRequired=true)
    group_definition: Optional[GroupDefinitionDto] = None
    """
    The group's tag and translations to save. The tag identifies the group; translations provide its display name per locale.
    """


    # @ApiMember(Description="Communication channel (e.g. Email, Push) this group belongs to.")
    channel: Optional[CommunicationChannel] = None
    """
    Communication channel (e.g. Email, Push) this group belongs to.
    """


    # @ApiMember(Description="If moving the group to a different channel, the channel it currently belongs to.")
    origin_channel: Optional[CommunicationChannel] = None
    """
    If moving the group to a different channel, the channel it currently belongs to.
    """


# @Route("/{version}/account/projects/{projectId}/notifications/settings/tag", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveNotificationsTag(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="The tag's identifier, translations, and default per-delivery-channel enabled/disabled settings.", IsRequired=true)
    tag_definition: Optional[TagDefinitionDto] = None
    """
    The tag's identifier, translations, and default per-delivery-channel enabled/disabled settings.
    """


    # @ApiMember(Description="Communication channel (e.g. Email, Push) this tag belongs to.")
    channel: Optional[CommunicationChannel] = None
    """
    Communication channel (e.g. Email, Push) this tag belongs to.
    """


    # @ApiMember(Description="Tag of the group this notification tag should be placed under, if any.")
    group_tag: Optional[str] = None
    """
    Tag of the group this notification tag should be placed under, if any.
    """


# @Route("/{version}/account/projects", "POST")
# @Api(Description="Create a new backend project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateProjectRequest(RequestBase, IReturn[IdResponse]):
    """
    Create a new backend project.
    """

    integration: Optional[DatabaseIntegrationRequest] = None
    # @ApiMember(Description="Project name, unique per account.")
    project_name: Optional[str] = None
    """
    Project name, unique per account.
    """


    # @ApiMember(Description="Region code for the primary region, e.g. 'nb-eu-germany'. Use a code from get_account_regions.")
    primary_region: Optional[str] = None
    """
    Region code for the primary region, e.g. 'nb-eu-germany'. Use a code from get_account_regions.
    """


    additional_regions: Optional[List[str]] = None
    description: Optional[str] = None


# @Route("/{version}/account/projects/{projectId}", "DELETE")
# @Api(Description="Deletes project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteProject(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Deletes project
    """

    pass


# @Route("/{version}/account/projects/environments", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateProjectEnvironmentRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Name for the new environment (e.g. 'TEST', 'STAGING'). A-Z/0-9/space, up to 15 chars, cannot be PROD.", IsRequired=true)
    environment_name: Optional[str] = None
    """
    Name for the new environment (e.g. 'TEST', 'STAGING'). A-Z/0-9/space, up to 15 chars, cannot be PROD.
    """


    integration: Optional[DatabaseIntegrationRequest] = None


# @Route("/{version}/account/projects/environments/{environmentName}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteProjectEnvironmentRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Name of the environment to delete (from get_project_environments), e.g. 'TEST'. PROD is rejected.", IsRequired=true)
    environment_name: Optional[str] = None
    """
    Name of the environment to delete (from get_project_environments), e.g. 'TEST'. PROD is rejected.
    """


# @Route("/{version}/account/projects/environments/{environmentName}/rank", "PATCH")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetEnvironmentRankRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Name of the environment to re-rank (from get_project_environments).", IsRequired=true)
    environment_name: Optional[str] = None
    """
    Name of the environment to re-rank (from get_project_environments).
    """


    # @ApiMember(Description="New promotion-ladder rank. Out-of-range values are clamped and ranks re-normalized.")
    rank: int = 0
    """
    New promotion-ladder rank. Out-of-range values are clamped and ranks re-normalized.
    """


# @Route("/{version}/account/projects/environments/promote", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PromoteEnvironmentRequest(CodeMashRequestBase, IReturn[PromoteEnvironmentResponse]):
    # @ApiMember(Description="Environment to promote FROM (source of truth for this promotion).", IsRequired=true)
    source_env: Optional[str] = None
    """
    Environment to promote FROM (source of truth for this promotion).
    """


    # @ApiMember(Description="Environment to promote INTO. Must be higher on the promotion ladder than SourceEnv.", IsRequired=true)
    target_env: Optional[str] = None
    """
    Environment to promote INTO. Must be higher on the promotion ladder than SourceEnv.
    """


    # @ApiMember(Description="When true, only returns the promotion plan (including deletions) without applying it or copying secrets. Use this to preview before a real run.")
    dry_run: bool = False
    """
    When true, only returns the promotion plan (including deletions) without applying it or copying secrets. Use this to preview before a real run.
    """


# @Route("/{version}/account/projects/environments/promote/rollback", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RollbackPromotionRequest(CodeMashRequestBase, IReturn[PromoteEnvironmentResponse]):
    # @ApiMember(Description="Environment whose content should be rolled back.", IsRequired=true)
    target_env: Optional[str] = None
    """
    Environment whose content should be rolled back.
    """


    # @ApiMember(Description="The fromVersion anchor returned by the promote_environment call being rolled back.", IsRequired=true)
    from_version: int = 0
    """
    The fromVersion anchor returned by the promote_environment call being rolled back.
    """


# @Route("/{version}/account/projects/environments", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjectEnvironments(CodeMashRequestBase, IReturn[GetProjectEnvironmentsResponse]):
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


# @Route("/{version}/account/projects/{projectId}/wait-active", "GET")
# @Api(Description="Waits (bounded, server-side) for a project to finish provisioning and become active.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WaitForProjectActiveRequest(CodeMashRequestBase, IReturn[WaitForProjectActiveResponse]):
    """
    Waits (bounded, server-side) for a project to finish provisioning and become active.
    """

    # @ApiMember(Description="Max seconds to wait before returning 'not active yet' (default 30, capped at 90).")
    timeout_seconds: Optional[int] = None
    """
    Max seconds to wait before returning 'not active yet' (default 30, capped at 90).
    """


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


# @Route("/{version}/account/projects/{projectId}/settings/admin-portal/service-user", "PUT")
# @Api(Description="Assigns the project's Admin Portal service user")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssignAdminPortalServiceUserRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Assigns the project's Admin Portal service user
    """

    # @ApiMember(Description="Id of the existing AuthType.Service user to assign as the project's Admin Portal service user.", IsRequired=true)
    service_user_id: Optional[str] = None
    """
    Id of the existing AuthType.Service user to assign as the project's Admin Portal service user.
    """


# @Route("/{version}/account/projects/{projectId}/admin-portal/structure", "GET")
# @Api(Description="Reads the Admin Portal layout/structure (service user only)")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAdminPortalStructure(CodeMashRequestBase, IReturn[AdminPortalStructureDto]):
    """
    Reads the Admin Portal layout/structure (service user only)
    """

    pass


# @Route("/{version}/account/projects/{projectId}/settings/admin-url", "PATCH")
# @Api(Description="Updates the project's admin-portal URL override")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectAdminUrl(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates the project's admin-portal URL override
    """

    # @ApiMember(Description="Custom admin-portal URL to use instead of the canonical address. Null/empty restores the canonical pr_{id}.admin.{host} address.")
    url: Optional[str] = None
    """
    Custom admin-portal URL to use instead of the canonical address. Null/empty restores the canonical pr_{id}.admin.{host} address.
    """


# @Route("/{version}/account/projects/{projectId}/settings/accent-color", "PATCH")
# @Api(Description="Updates project accent color")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectAccentColor(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project accent color
    """

    # @ApiMember(Description="Hex color code, e.g. '#FF6D00'.", IsRequired=true)
    color: Optional[str] = None
    """
    Hex color code, e.g. '#FF6D00'.
    """


# @Route("/{version}/account/projects/{projectId}/settings/icon", "PATCH")
# @Api(Description="Updates project icon")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectIcon(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project icon
    """

    file_resource: Optional[FileResourceRefDto] = None


# @Route("/{version}/account/projects/{projectId}/settings/logo", "PATCH")
# @Api(Description="Updates project logo")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectLogo(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project logo
    """

    file_resource: Optional[FileResourceRefDto] = None


# @Route("/{version}/account/projects/{projectId}/settings/main-color", "PATCH")
# @Api(Description="Updates project main color")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectMainColor(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project main color
    """

    # @ApiMember(Description="Hex color code, e.g. '#1A73E8'.", IsRequired=true)
    color: Optional[str] = None
    """
    Hex color code, e.g. '#1A73E8'.
    """


# @Route("/{version}/account/projects/{projectId}/settings/origins", "PATCH")
# @Api(Description="Updates project CORS settings")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectAllowedOrigins(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project CORS settings
    """

    # @ApiMember(Description="The complete new list of allowed origin URLs, e.g. [\"https://app.example.com\", \"https://example.com\"]. An entry with no scheme (e.g. \"example.com\") defaults to https. Whatever is not in this list stops being allowed.")
    origins: Optional[List[str]] = None
    """
    The complete new list of allowed origin URLs, e.g. ["https://app.example.com", "https://example.com"]. An entry with no scheme (e.g. "example.com") defaults to https. Whatever is not in this list stops being allowed.
    """


# @Route("/{version}/account/projects/{projectId}/settings/default-language", "PATCH")
# @Api(Description="Update project default language")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectDefaultLanguage(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Update project default language
    """

    # @ApiMember(Description="Language code, e.g. 'en' or 'de'.", IsRequired=true)
    default_language: Optional[str] = None
    """
    Language code, e.g. 'en' or 'de'.
    """


# @Route("/{version}/account/projects/{projectId}/settings/description", "PATCH")
# @Api(Description="Updates project description")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectDescription(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project description
    """

    # @ApiMember(Description="The new description text. Omit (null) to clear the description.")
    description: Optional[str] = None
    """
    The new description text. Omit (null) to clear the description.
    """


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

    # @ApiMember(Description="The complete new list of language codes, e.g. [\"en\", \"de\", \"lt\"].", IsRequired=true)
    languages: List[str] = field(default_factory=list)
    """
    The complete new list of language codes, e.g. ["en", "de", "lt"].
    """


# @Route("/{version}/account/projects/{projectId}/settings/legal", "PATCH")
# @Api(Description="Updates the project's public legal documents (Terms & Conditions, Privacy Policy)")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectLegalDocuments(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates the project's public legal documents (Terms & Conditions, Privacy Policy)
    """

    # @ApiMember(Description="Terms & Conditions document, Markdown. Null/empty clears it.")
    terms_markdown: Optional[str] = None
    """
    Terms & Conditions document, Markdown. Null/empty clears it.
    """


    # @ApiMember(Description="Privacy Policy document, Markdown. Null/empty clears it.")
    privacy_markdown: Optional[str] = None
    """
    Privacy Policy document, Markdown. Null/empty clears it.
    """


# @Route("/{version}/account/projects/{projectId}/settings/legal/expose", "PATCH")
# @Api(Description="Sets whether the project's legal documents are publicly readable via the Admin Portal")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectExposeLegal(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Sets whether the project's legal documents are publicly readable via the Admin Portal
    """

    # @ApiMember(Description="True to make the legal documents publicly readable via the Admin Portal, false to hide them.")
    exposed: bool = False
    """
    True to make the legal documents publicly readable via the Admin Portal, false to hide them.
    """


# @Route("/{version}/account/projects/{projectId}/settings/url", "PATCH")
# @Api(Description="Updates project marketing url")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectUrl(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project marketing url
    """

    # @ApiMember(Description="The marketing site URL, e.g. 'https://example.com'. Omit (null) to clear.")
    url: Optional[str] = None
    """
    The marketing site URL, e.g. 'https://example.com'. Omit (null) to clear.
    """


# @Route("/{version}/account/projects/{projectId}/settings/name", "PATCH")
# @Api(Description="Updates project name")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectName(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project name
    """

    # @ApiMember(Description="The new project name, unique per account.", IsRequired=true)
    name: Optional[str] = None
    """
    The new project name, unique per account.
    """


# @Route("/{version}/account/projects/{projectId}/settings/regions", "PATCH")
# @Api(Description="Updates project regions")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateProjectRegions(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates project regions
    """

    # @ApiMember(Description="Primary region code, e.g. 'nb-eu-germany'. Immutable once set — omit to keep the current one; only set it on a project that has none.")
    primary_region: Optional[str] = None
    """
    Primary region code, e.g. 'nb-eu-germany'. Immutable once set — omit to keep the current one; only set it on a project that has none.
    """


    # @ApiMember(Description="The complete new list of additional region codes (full replacement). A region that still hosts a provisioned database cluster cannot be removed.")
    additional_regions: Optional[List[str]] = None
    """
    The complete new list of additional region codes (full replacement). A region that still hosts a provisioned database cluster cannot be removed.
    """


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


# @Route("/{version}/account/team/member/password", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChangeTeamMemberPassword(RequestBase, IReturn[IdResponse]):
    email: Optional[str] = None
    current_password: Optional[str] = None
    new_password: Optional[str] = None


# @Route("/{version}/account/team/member/create", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateTeamMember(RequestBase, IReturn[IdResponse]):
    email: Optional[str] = None
    display_name: Optional[str] = None
    password: Optional[str] = None
    roles: Optional[List[str]] = None
    send_invitation: bool = False


# @Route("/{version}/account/team/policies", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateAccountPolicy(RequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Name for the new custom account policy.", IsRequired=true)
    policy_name: Optional[str] = None
    """
    Name for the new custom account policy.
    """


    # @ApiMember(Description="Optional human-readable description of the policy's purpose.")
    description: Optional[str] = None
    """
    Optional human-readable description of the policy's purpose.
    """


    # @ApiMember(Description="Raw JSON policy document, AWS-IAM style (Statement array of Effect/Action/Resource entries), matching PolicyDocument.schema.json. This defines which permissions the policy grants.")
    policy_document_json: Optional[str] = None
    """
    Raw JSON policy document, AWS-IAM style (Statement array of Effect/Action/Resource entries), matching PolicyDocument.schema.json. This defines which permissions the policy grants.
    """


# @Route("/{version}/account/team/roles", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateAccountRole(RequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Name for the new custom account team role.", IsRequired=true)
    role_name: Optional[str] = None
    """
    Name for the new custom account team role.
    """


    # @ApiMember(Description="Optional human-readable description of the role's purpose.")
    description: Optional[str] = None
    """
    Optional human-readable description of the role's purpose.
    """


    # @ApiMember(Description="Public policy ids (from get_account_team_policies) to attach to this role.")
    policies: Optional[List[str]] = None
    """
    Public policy ids (from get_account_team_policies) to attach to this role.
    """


# @Route("/{version}/account/team/policies/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteAccountPolicy(RequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Public policy id (from get_account_team_policies) to delete.", IsRequired=true)
    id: Optional[str] = None
    """
    Public policy id (from get_account_team_policies) to delete.
    """


# @Route("/{version}/account/team/roles/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteAccountRole(RequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Role template id (from get_account_team_roles) to delete.", IsRequired=true)
    id: Optional[str] = None
    """
    Role template id (from get_account_team_roles) to delete.
    """


# @Route("/{version}/account/collaborators", "GET")
# @Api(Description="Gets account team members (collaborators)")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountCollaborators(RequestBase, IReturn[GetAccountCollaboratorsResponse]):
    """
    Gets account team members (collaborators)
    """

    # @ApiMember(Description="Set true to also include the account owner in the list.")
    include_account_owner: bool = False
    """
    Set true to also include the account owner in the list.
    """


    # @ApiMember(Description="Set true to only return members that have a registered push device.")
    user_should_have_push_device: bool = False
    """
    Set true to only return members that have a registered push device.
    """


    # @ApiMember(Description="Optional project id — only members with access to that project.")
    project_id: Optional[str] = None
    """
    Optional project id — only members with access to that project.
    """


    # @ApiMember(Description="Optional filter: only these user ids.")
    user_ids: Optional[List[str]] = None
    """
    Optional filter: only these user ids.
    """


    # @ApiMember(Description="Optional filter: only members having one of these role names.")
    role_names: Optional[List[str]] = None
    """
    Optional filter: only members having one of these role names.
    """


    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/account/team/password-policy", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountPasswordPolicy(RequestBase, IReturn[GetAccountPasswordPolicyResponse]):
    pass


# @Route("/{version}/account/team/policies", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountTeamPolicies(RequestBase, IReturn[GetAccountTeamPoliciesResponse]):
    pass


# @Route("/{version}/account/team/roles", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountTeamRoles(RequestBase, IReturn[GetAccountTeamRolesResponse]):
    pass


# @Route("/{version}/account/team/member/invite", "POST")
# @Api(Description="Send invite to team member")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SendInviteToTeamMember(RequestBase, IReturn[EmptyResponse]):
    """
    Send invite to team member
    """

    # @ApiMember(Description="Email address the invitation is sent to.", IsRequired=true)
    email: Optional[str] = None
    """
    Email address the invitation is sent to.
    """


    # @ApiMember(Description="Account role ids (GUIDs from get_account_team_roles) the member gets on accepting. Omit for the default member role.")
    roles: Optional[List[str]] = None
    """
    Account role ids (GUIDs from get_account_team_roles) the member gets on accepting. Omit for the default member role.
    """


# @Route("/{version}/account/team/policies", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAccountPolicy(RequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Public policy id (from get_account_team_policies) to update.", IsRequired=true)
    id: Optional[str] = None
    """
    Public policy id (from get_account_team_policies) to update.
    """


    # @ApiMember(Description="New name for the policy.", IsRequired=true)
    policy_name: Optional[str] = None
    """
    New name for the policy.
    """


    # @ApiMember(Description="Optional human-readable description of the policy's purpose.")
    description: Optional[str] = None
    """
    Optional human-readable description of the policy's purpose.
    """


    # @ApiMember(Description="Raw JSON policy document, AWS-IAM style (Statement array of Effect/Action/Resource entries) — replaces the policy's current statement set.")
    policy_document_json: Optional[str] = None
    """
    Raw JSON policy document, AWS-IAM style (Statement array of Effect/Action/Resource entries) — replaces the policy's current statement set.
    """


# @Route("/{version}/account/team/roles", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAccountRole(RequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Role template id (from get_account_team_roles) to update.", IsRequired=true)
    id: Optional[str] = None
    """
    Role template id (from get_account_team_roles) to update.
    """


    # @ApiMember(Description="New name for the role.", IsRequired=true)
    role_name: Optional[str] = None
    """
    New name for the role.
    """


    # @ApiMember(Description="Optional human-readable description of the role's purpose.")
    description: Optional[str] = None
    """
    Optional human-readable description of the role's purpose.
    """


    # @ApiMember(Description="Public policy ids (from get_account_team_policies) to attach — replaces the current set.")
    policies: Optional[List[str]] = None
    """
    Public policy ids (from get_account_team_policies) to attach — replaces the current set.
    """


# @Route("/{version}/account/userauth/has-passkey", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountHasPasskeyRequest(RequestBase, IReturn[AccountPasskeyOkResponse]):
    email: Optional[str] = None


# @Route("/{version}/account/userauth/email/start-verification", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountStartEmailVerificationRequest(RequestBase, IReturn[AccountPasskeyOkResponse]):
    email: Optional[str] = None


# @Route("/{version}/account/userauth/email/confirm-verification", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountConfirmEmailVerificationRequest(RequestBase, IReturn[AccountPasskeyVerificationTokenResponse]):
    email: Optional[str] = None
    code: Optional[str] = None


# @Route("/{version}/account/userauth/passkey/registration-options", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyRegistrationOptionsRequest(RequestBase, IReturn[AccountPasskeyCeremonyOptionsResponse]):
    verification_token: Optional[str] = None


# @Route("/{version}/account/userauth/passkey/verify-registration", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountVerifyPasskeyRegistrationRequest(RequestBase, IReturn[AccountPasskeyAuthTokensResponse]):
    verification_token: Optional[str] = None
    ceremony_id: Optional[str] = None
    attestation_response: Optional[str] = None
    friendly_name: Optional[str] = None


# @Route("/{version}/account/userauth/passkey/authentication-options", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyAuthenticationOptionsRequest(RequestBase, IReturn[AccountPasskeyCeremonyOptionsResponse]):
    email: Optional[str] = None


# @Route("/{version}/account/userauth/passkey/verify-authentication", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountVerifyPasskeyAuthenticationRequest(RequestBase, IReturn[AccountPasskeyAuthTokensResponse]):
    ceremony_id: Optional[str] = None
    assertion_response: Optional[str] = None


# @Route("/{version}/account/userauth/passkeys", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListAccountPasskeysRequest(RequestBase, IReturn[AccountPasskeyListResponse]):
    pass


# @Route("/{version}/account/userauth/passkeys/{CredentialId}/rename", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RenameAccountPasskeyRequest(RequestBase, IReturn[AccountPasskeyOkResponse]):
    credential_id: Optional[str] = None
    friendly_name: Optional[str] = None


# @Route("/{version}/account/userauth/passkeys/{CredentialId}/revoke", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RevokeAccountPasskeyRequest(RequestBase, IReturn[AccountPasskeyOkResponse]):
    credential_id: Optional[str] = None


# @Route("/{version}/account/userauth/passkey/enrollment-options", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountPasskeyEnrollmentOptionsRequest(RequestBase, IReturn[AccountPasskeyCeremonyOptionsResponse]):
    pass


# @Route("/{version}/account/userauth/passkey/verify-enrollment", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountVerifyPasskeyEnrollmentRequest(RequestBase, IReturn[AccountPasskeyEnrollmentResponse]):
    ceremony_id: Optional[str] = None
    attestation_response: Optional[str] = None
    friendly_name: Optional[str] = None


# @Route("/{version}/account/licensing/dns-status", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLicenseDomainDnsStatus(RequestBase, IReturn[GetLicenseDomainDnsStatusResponse]):
    domain: Optional[str] = None


# @Route("/{version}/licensing/domain-verification/start", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StartLicenseDomainVerificationRequest(RequestBase, IReturn[StartLicenseDomainVerificationResponse]):
    domain: Optional[str] = None


# @Route("/{version}/licensing/domain-verification/status", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLicenseDomainVerificationStatus(RequestBase, IReturn[GetLicenseDomainVerificationStatusResponse]):
    domain: Optional[str] = None


# @Route("/{version}/account/licenses", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLicenses(RequestBase, IReturn[GetLicensesResponse]):
    pass


# @Route("/{version}/licensing/heartbeat", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PostLicenseHeartbeat(RequestBase, IReturn[PostLicenseHeartbeatResponse]):
    license: Optional[str] = None
    license_account_id: Optional[str] = None
    installation_id: Optional[str] = None
    domain: Optional[str] = None
    host_kind: Optional[str] = None
    release: Optional[str] = None
    instance_version: Optional[str] = None


# @Route("/{version}/account/licensing/status", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetInstallationLicenseStatus(RequestBase, IReturn[GetInstallationLicenseStatusResponse]):
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
    primary_region: Optional[ProjectRegion] = None
    additional_regions: Optional[List[ProjectRegion]] = None
    description: Optional[str] = None
    is_provisioning: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectActivated:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectSuspendedByLicense:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectResumedFromLicenseSuspension:
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
class ProjectAdminUrlChanged:
    url: Optional[DomainUrl] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectLegalDocumentsChanged:
    documents: Optional[ProjectLegalDocuments] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectExposeLegalToAdminPortalChanged:
    exposed: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectAdminPortalServiceUserAssigned:
    service_user_id: Optional[AuthId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectAllowedOriginsChanged:
    origins: Optional[List[DomainUrl]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectEnvironmentCreated:
    env: Optional[Env] = None
    ranks: Dict[str, int] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectEnvironmentDeleted:
    env: Optional[Env] = None
    ranks: Dict[str, int] = field(default_factory=dict)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectEnvironmentRanksChanged:
    ranks: Dict[str, int] = field(default_factory=dict)


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
class AccountTeamPolicyCreated:
    policy: Optional[MembershipPolicy] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountTeamPolicyUpdated:
    policy: Optional[MembershipPolicy] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountTeamPolicyDeleted:
    policy_id: Optional[PolicyId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountTeamRoleCreated:
    role: Optional[MembershipRole] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountTeamRoleUpdated:
    role: Optional[MembershipRole] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AccountTeamRoleDeleted:
    role_id: Optional[RoleId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AtlasUsageRecorded:
    record: Optional[AtlasUsageRecord] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UsageBillingIngestionFailed:
    failure: Optional[UsageIngestionFailure] = None


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


# @Route("/{version}/membership/users/{Id}/api-keys", "POST")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class IssueServiceUserApiKeyRequest(CodeMashRequestBase, IReturn[IssueServiceUserApiKeyResponse]):
    """
    Membership
    """

    id: Optional[str] = None
    database_integration_id: Optional[str] = None
    name: Optional[str] = None
    scopes: Optional[List[str]] = None
    expires_in_days: Optional[int] = None
    notes: Optional[str] = None


# @Route("/{version}/membership/users/{Id}/api-keys", "GET")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ListServiceUserApiKeysRequest(CodeMashRequestBase, IReturn[ListServiceUserApiKeysResponse]):
    """
    Membership
    """

    # @ApiMember(Description="The service user's auth id.", IsRequired=true)
    id: Optional[str] = None
    """
    The service user's auth id.
    """


# @Route("/{version}/membership/users/{Id}/api-keys/{KeyId}", "DELETE")
# @Api(Description="Membership")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteServiceUserApiKeyRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Membership
    """

    # @ApiMember(Description="The service user's auth id.", IsRequired=true)
    id: Optional[str] = None
    """
    The service user's auth id.
    """


    # @ApiMember(Description="The key id to delete, from list_service_user_api_keys.", IsRequired=true)
    key_id: int = 0
    """
    The key id to delete, from list_service_user_api_keys.
    """


# @Route("/{version}/membership/triggers/{triggerId}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteMembershipTrigger(DeleteTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/membership/triggers/{triggerId}/disable", "PATCH")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableMembershipTrigger(DisableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/membership/triggers/{triggerId}/enable", "PATCH")
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

    # @ApiMember(Description="Display name of the new role, unique within the project.", IsRequired=true)
    role_name: Optional[str] = None
    """
    Display name of the new role, unique within the project.
    """


    description: Optional[str] = None
    # @ApiMember(Description="Policy ids to attach. These are OPAQUE ids from get_policies (e.g. 'pol_3kJ9xJ2mQ0aBcDeFgHiJk') — NEVER invent them or guess from a policy name. Omit this to create a role with no policies and attach them later.")
    policies: Optional[List[str]] = None
    """
    Policy ids to attach. These are OPAQUE ids from get_policies (e.g. 'pol_3kJ9xJ2mQ0aBcDeFgHiJk') — NEVER invent them or guess from a policy name. Omit this to create a role with no policies and attach them later.
    """


# @Route("/{version}/membership/roles", "DELETE")
# @Api(Description="Deletes custom role from project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteRole(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Deletes custom role from project.
    """

    # @ApiMember(Description="Id of the role to delete, from get_roles.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the role to delete, from get_roles.
    """


# @Route("/{version}/membership/roles/{Id}", "GET")
# @Api(Description="Gets project role details.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetRole(CodeMashRequestBase, IReturn[GetRoleResponse]):
    """
    Gets project role details.
    """

    # @ApiMember(Description="Role id from get_roles.", IsRequired=true)
    id: Optional[str] = None
    """
    Role id from get_roles.
    """


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

    # @ApiMember(Description="Id of the role to update, from get_roles.", IsRequired=true)
    id: Optional[str] = None
    """
    Id of the role to update, from get_roles.
    """


    # @ApiMember(Description="The role's name — required; resend the current name to keep it.", IsRequired=true)
    role_name: Optional[str] = None
    """
    The role's name — required; resend the current name to keep it.
    """


    description: Optional[str] = None
    # @ApiMember(Description="The complete new list of attached policy ids (full replacement), opaque ids from get_policies (e.g. 'pol_3kJ9xJ2mQ0aBcDeFgHiJk') — never invent or guess them.")
    policies: Optional[List[str]] = None
    """
    The complete new list of attached policy ids (full replacement), opaque ids from get_policies (e.g. 'pol_3kJ9xJ2mQ0aBcDeFgHiJk') — never invent or guess them.
    """


# @Route("/{version}/membership/policies", "POST")
# @Api(Description="Create a new custom policy for project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreatePolicy(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Create a new custom policy for project.
    """

    # @ApiMember(Description="Display name of the new policy, unique within the project.", IsRequired=true)
    policy_name: Optional[str] = None
    """
    Display name of the new policy, unique within the project.
    """


    # @ApiMember(Description="Optional human-readable description of what the policy grants.")
    description: Optional[str] = None
    """
    Optional human-readable description of what the policy grants.
    """


    # @ApiMember(Description="AWS-IAM-style policy document as a raw JSON string (an object with a permission statement list) matching PolicyDocument.schema.json. Malformed or invalid documents are rejected before any change is made.")
    policy_document_json: Optional[str] = None
    """
    AWS-IAM-style policy document as a raw JSON string (an object with a permission statement list) matching PolicyDocument.schema.json. Malformed or invalid documents are rejected before any change is made.
    """


# @Route("/{version}/membership/policies", "DELETE")
# @Api(Description="Deletes custom policy from project.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePolicy(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Deletes custom policy from project.
    """

    # @ApiMember(Description="Public policy id, e.g. 'pol_database-read', from get_policies.", IsRequired=true)
    id: Optional[str] = None
    """
    Public policy id, e.g. 'pol_database-read', from get_policies.
    """


# @Route("/{version}/membership/policies/{Id}", "GET")
# @Api(Description="Gets project policy details.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPolicy(CodeMashRequestBase, IReturn[GetPolicyResponse]):
    """
    Gets project policy details.
    """

    # @ApiMember(Description="Public policy id, e.g. 'pol_database-read', from get_policies.", IsRequired=true)
    id: Optional[str] = None
    """
    Public policy id, e.g. 'pol_database-read', from get_policies.
    """


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

    # @ApiMember(Description="Public policy id, e.g. 'pol_database-read', from get_policies.", IsRequired=true)
    id: Optional[str] = None
    """
    Public policy id, e.g. 'pol_database-read', from get_policies.
    """


    # @ApiMember(Description="The policy's name — required; resend the current name to keep it.", IsRequired=true)
    policy_name: Optional[str] = None
    """
    The policy's name — required; resend the current name to keep it.
    """


    # @ApiMember(Description="Optional human-readable description of what the policy grants.")
    description: Optional[str] = None
    """
    Optional human-readable description of what the policy grants.
    """


    # @ApiMember(Description="AWS-IAM-style policy document as a raw JSON string (an object with a permission statement list) matching PolicyDocument.schema.json — this is a FULL replacement of the policy's current permissions.")
    policy_document_json: Optional[str] = None
    """
    AWS-IAM-style policy document as a raw JSON string (an object with a permission statement list) matching PolicyDocument.schema.json — this is a FULL replacement of the policy's current permissions.
    """


# @Route("/{version}/membership/passkey/settings", "GET")
# @Api(Description="Gets the project's passkey authentication settings.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPasskeySettings(CodeMashRequestBase, IReturn[GetPasskeySettingsResponse]):
    """
    Gets the project's passkey authentication settings.
    """

    pass


# @Route("/{version}/membership/passkey/settings", "POST")
# @Api(Description="Saves the project's passkey authentication settings.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePasskeySettings(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Saves the project's passkey authentication settings.
    """

    # @ApiMember(Description="Whether the email + passkey sign-in flow is enabled for the project.")
    enabled: bool = False
    """
    Whether the email + passkey sign-in flow is enabled for the project.
    """


    # @ApiMember(Description="Email verification code lifetime, in minutes. Allowed range: 3-15.")
    code_ttl_minutes: int = 0
    """
    Email verification code lifetime, in minutes. Allowed range: 3-15.
    """


    # @ApiMember(Description="Maximum passkeys a single user may register. Allowed range: 1-20.")
    max_credentials_per_user: int = 0
    """
    Maximum passkeys a single user may register. Allowed range: 1-20.
    """


    # @ApiMember(Description="Number of recovery codes generated at signup. Allowed range: 5-20.")
    recovery_code_count: int = 0
    """
    Number of recovery codes generated at signup. Allowed range: 5-20.
    """


    # @ApiMember(Description="Whether recovery codes are generated automatically at signup.")
    generate_recovery_codes_at_signup: bool = False
    """
    Whether recovery codes are generated automatically at signup.
    """


    # @ApiMember(Description="Accepted authenticator types: 'Any', 'Platform', or 'CrossPlatform'.")
    authenticator_attachment: Optional[str] = None
    """
    Accepted authenticator types: 'Any', 'Platform', or 'CrossPlatform'.
    """


    # @ApiMember(Description="Per-project opt-in for magic-link account recovery (off by default).")
    allow_magic_link_recovery: bool = False
    """
    Per-project opt-in for magic-link account recovery (off by default).
    """


    # @ApiMember(Description="Absolute refresh-token lifetime, in days. Allowed range: 7-90.")
    refresh_token_ttl_days: int = 0
    """
    Absolute refresh-token lifetime, in days. Allowed range: 7-90.
    """


    # @ApiMember(Description="Optional explicit WebAuthn RP-ID — a bare DNS host (e.g. 'app.example.com', no scheme/port/path). Leave null/empty to derive it from the project's CORS origins. WARNING: changing this value invalidates every existing passkey on the project — set it once before going live and avoid changing it afterward.")
    rp_id: Optional[str] = None
    """
    Optional explicit WebAuthn RP-ID — a bare DNS host (e.g. 'app.example.com', no scheme/port/path). Leave null/empty to derive it from the project's CORS origins. WARNING: changing this value invalidates every existing passkey on the project — set it once before going live and avoid changing it afterward.
    """


# @Route("/{version}/membership/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteMembershipIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Integration id, from get_membership_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_membership_integrations.
    """


# @Route("/{version}/membership/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableMembershipIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Integration id, from get_membership_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_membership_integrations.
    """


# @Route("/{version}/membership/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableMembershipIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Integration id, from get_membership_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_membership_integrations.
    """


# @Route("/{version}/membership/integrations/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipIntegration(CodeMashRequestBase, IReturn[GetMembershipIntegrationResponse]):
    # @ApiMember(Description="Integration id, from get_membership_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_membership_integrations.
    """


# @Route("/{version}/membership/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMembershipIntegrations(CodeMashListPaginationRequestBase, IReturn[GetMembershipIntegrationsResponse]):
    pass


# @Route("/{version}/membership/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveMembershipIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    integration: Optional[MembershipIntegrationRequest] = None


# @Route("/{version}/membership/integrations/{Id}/default", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetMembershipIntegrationAsDefaultRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Integration id, from get_membership_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Integration id, from get_membership_integrations.
    """


# @Route("/{version}/membership/authorization", "GET")
# @Api(Description="Gets the project's membership authorization (role-assignment) settings.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAuthorizationSettings(CodeMashRequestBase, IReturn[GetAuthorizationSettingsResponse]):
    """
    Gets the project's membership authorization (role-assignment) settings.
    """

    pass


# @Route("/{version}/membership/authorization", "PUT")
# @Api(Description="Updates the project's membership authorization settings.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAuthorizationSettings(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates the project's membership authorization settings.
    """

    setting: Optional[str] = None
    default_roles: Optional[List[str]] = None
    allowed_registration_roles: Optional[List[str]] = None
    allow_guest_users: bool = False
    guest_cleanup_period_days: Optional[int] = None
    user_registers_as_role: Optional[str] = None
    guest_registers_as_role: Optional[str] = None
    allowed_register_roles: Optional[List[str]] = None
    need_verification: bool = False
    verification_email_template: Optional[str] = None
    deactivation_email_template: Optional[str] = None
    allow_invite_users: bool = False
    allow_deactivate_users: bool = False
    invite_user_email_template: Optional[str] = None
    invitation_expiration: Optional[int] = None
    email_verification_expiration: Optional[int] = None
    deactivation_expiration: Optional[int] = None
    default_subscribe_to_news: bool = False
    min_length: int = 0
    max_length: Optional[int] = None
    min_numbers: Optional[int] = None
    max_numbers: Optional[int] = None
    min_upper: Optional[int] = None
    max_upper: Optional[int] = None
    min_lower: Optional[int] = None
    max_lower: Optional[int] = None
    min_special: Optional[int] = None
    max_special: Optional[int] = None
    allowed_special: Optional[str] = None


# @Route("/{version}/membership/authorization/password-complexity", "PUT")
# @Api(Description="Updates the project's membership password complexity policy.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdatePasswordComplexity(CodeMashRequestBase, IReturn[UpdatePasswordComplexityResponse]):
    """
    Updates the project's membership password complexity policy.
    """

    # @ApiMember(Description="Minimum password length.")
    min_length: int = 0
    """
    Minimum password length.
    """


    # @ApiMember(Description="Maximum password length, if capped.")
    max_length: Optional[int] = None
    """
    Maximum password length, if capped.
    """


    # @ApiMember(Description="Minimum number of numeric characters required.")
    min_numbers: Optional[int] = None
    """
    Minimum number of numeric characters required.
    """


    # @ApiMember(Description="Maximum number of numeric characters allowed.")
    max_numbers: Optional[int] = None
    """
    Maximum number of numeric characters allowed.
    """


    # @ApiMember(Description="Minimum number of uppercase characters required.")
    min_upper: Optional[int] = None
    """
    Minimum number of uppercase characters required.
    """


    # @ApiMember(Description="Maximum number of uppercase characters allowed.")
    max_upper: Optional[int] = None
    """
    Maximum number of uppercase characters allowed.
    """


    # @ApiMember(Description="Minimum number of lowercase characters required.")
    min_lower: Optional[int] = None
    """
    Minimum number of lowercase characters required.
    """


    # @ApiMember(Description="Maximum number of lowercase characters allowed.")
    max_lower: Optional[int] = None
    """
    Maximum number of lowercase characters allowed.
    """


    # @ApiMember(Description="Minimum number of special characters required.")
    min_special: Optional[int] = None
    """
    Minimum number of special characters required.
    """


    # @ApiMember(Description="Maximum number of special characters allowed.")
    max_special: Optional[int] = None
    """
    Maximum number of special characters allowed.
    """


    # @ApiMember(Description="The set of characters counted as 'special', if restricted.")
    allowed_special: Optional[str] = None
    """
    The set of characters counted as 'special', if restricted.
    """


# @Route("/{version}/membership/authentication", "GET")
# @Api(Description="Gets the project's configured membership authentication sign-in flows.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAuthenticationSettings(CodeMashRequestBase, IReturn[GetAuthenticationSettingsResponse]):
    """
    Gets the project's configured membership authentication sign-in flows.
    """

    pass


# @Route("/{version}/membership/authentication", "PUT")
# @Api(Description="Updates the project's membership authentication preferences.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateAuthenticationSettings(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates the project's membership authentication preferences.
    """

    # @ApiMember(Description="Default URL to redirect end users to after logout.")
    logout_url: Optional[str] = None
    """
    Default URL to redirect end users to after logout.
    """


    # @ApiMember(Description="Whether end users may sign in with a username in addition to email.")
    allow_usernames: bool = False
    """
    Whether end users may sign in with a username in addition to email.
    """


    # @ApiMember(Description="Per-authentication-mode logout URL overrides.")
    modes: Optional[List[CredentialsSettingsModeDto]] = None
    """
    Per-authentication-mode logout URL overrides.
    """


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
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationSetAsDefault:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


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
class MembershipTriggerMirrored:
    trigger: Optional[Trigger] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerEnabled(TriggerByIdEventBase):
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerDisabled(TriggerByIdEventBase):
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MembershipTriggerDeleted(TriggerByIdEventBase):
    env: Optional[Env] = None


# @Route("/{version}/database/disable", "GET")
# @Api(Description="Disable database service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableDatabase(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable database service
    """

    pass


# @Route("/{version}/database/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableDatabase(CodeMashRequestBase, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/database/schemas/triggers/{triggerId}", "DELETE")
# @Api(Description="Delete database trigger")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteSchemaTrigger(DeleteTrigger, IReturn[EmptyResponse]):
    """
    Delete database trigger
    """

    pass


# @Route("/{version}/database/schemas/triggers/{triggerId}/disable", "PATCH")
# @Api(Description="Disable database trigger")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableSchemaTrigger(DisableTrigger, IReturn[EmptyResponse]):
    """
    Disable database trigger
    """

    pass


# @Route("/{version}/database/schemas/triggers/{triggerId}/enable", "PATCH")
# @Api(Description="Enable database trigger")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableSchemaTrigger(EnableTrigger, IReturn[EmptyResponse]):
    """
    Enable database trigger
    """

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

    pass


# @Route("/{version}/database/schemas/triggers", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveSchemaTrigger(SaveTrigger, IReturn[IdResponse]):
    pass


# @Route("/{version}/database/taxonomies/{Id}", "DELETE")
# @Api(Description="Delete database taxonomy")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseTaxonomyRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete database taxonomy
    """

    # @ApiMember(Description="Taxonomy id to delete, from get_database_taxonomies.", IsRequired=true)
    id: Optional[str] = None
    """
    Taxonomy id to delete, from get_database_taxonomies.
    """


# @Route("/{version}/database/taxonomies/{id}", "GET")
# @Api(Description="Gets database taxonomy by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomy(CodeMashRequestBase, IReturn[GetDatabaseTaxonomyResponse]):
    """
    Gets database taxonomy by id
    """

    # @ApiMember(Description="Taxonomy id from get_database_taxonomies.", IsRequired=true)
    id: Optional[str] = None
    """
    Taxonomy id from get_database_taxonomies.
    """


# @Route("/{version}/database/taxonomies", "GET")
# @Api(Description="Gets database taxonomies")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomies(CodeMashListPaginationRequestBase, IReturn[GetDatabaseTaxonomiesResponse]):
    """
    Gets database taxonomies
    """

    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/taxonomies/tree", "GET")
# @Api(Description="Returns the single-parent taxonomy structure tree")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomyTreeRequest(CodeMashRequestBase, IReturn[GetDatabaseTaxonomyTreeResponse]):
    """
    Returns the single-parent taxonomy structure tree
    """

    # @ApiMember(Description="When true, each taxonomy node also carries its own term tree (heavier response).")
    include_terms: bool = False
    """
    When true, each taxonomy node also carries its own term tree (heavier response).
    """


    # @ApiMember(Description="Optional database integration id. When omitted, the project's default database integration is used.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id. When omitted, the project's default database integration is used.
    """


# @Route("/{version}/database/taxonomies", "POST")
# @Api(Description="Creates or updates a database taxonomy")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseTaxonomyRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Creates or updates a database taxonomy
    """

    # @ApiMember(Description="Empty to create a new taxonomy; set to an existing taxonomy id (from get_database_taxonomies) to update it.")
    view_id: Optional[str] = None
    """
    Empty to create a new taxonomy; set to an existing taxonomy id (from get_database_taxonomies) to update it.
    """


    # @ApiMember(Description="Human-entered taxonomy title (e.g. \"Countries\"); a slug is derived server-side.", IsRequired=true)
    taxonomy_name: Optional[str] = None
    """
    Human-entered taxonomy title (e.g. "Countries"); a slug is derived server-side.
    """


    # @ApiMember(Description="Optional free-text description of the taxonomy.")
    description: Optional[str] = None
    """
    Optional free-text description of the taxonomy.
    """


    # @ApiMember(Description="Optional raw JSON string (Norbix data meta-schema) describing custom meta fields for terms in this taxonomy. Omit to leave the taxonomy structural-only.")
    terms_meta_data_schema: Optional[str] = None
    """
    Optional raw JSON string (Norbix data meta-schema) describing custom meta fields for terms in this taxonomy. Omit to leave the taxonomy structural-only.
    """


    # @ApiMember(Description="Optional raw JSON string (Norbix UI/visual meta-schema) describing the term meta edit form.")
    terms_meta_visual_schema: Optional[str] = None
    """
    Optional raw JSON string (Norbix UI/visual meta-schema) describing the term meta edit form.
    """


    # @ApiMember(Description="Optional parent taxonomy id. The child taxonomy points to its parent — e.g. set the Countries taxonomy's parentId to the Regions taxonomy id so each country term can be parented by a region term. Omit for a root taxonomy.")
    parent_id: Optional[str] = None
    """
    Optional parent taxonomy id. The child taxonomy points to its parent — e.g. set the Countries taxonomy's parentId to the Regions taxonomy id so each country term can be parented by a region term. Omit for a root taxonomy.
    """


    # @ApiMember(Description="Optional list of other taxonomy ids this taxonomy depends on for multi-parent terms. Omit for a self-contained taxonomy.")
    dependencies: Optional[List[str]] = None
    """
    Optional list of other taxonomy ids this taxonomy depends on for multi-parent terms. Omit for a self-contained taxonomy.
    """


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}", "DELETE")
# @Api(Description="Delete a single term from a taxonomy by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseTaxonomyTermRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete a single term from a taxonomy by id
    """

    # @ApiMember(Description="Taxonomy id that owns the term, from get_database_taxonomies.", IsRequired=true)
    taxonomy_id: Optional[str] = None
    """
    Taxonomy id that owns the term, from get_database_taxonomies.
    """


    # @ApiMember(Description="Term id to delete, from get_database_taxonomy_term_tree.", IsRequired=true)
    id: Optional[str] = None
    """
    Term id to delete, from get_database_taxonomy_term_tree.
    """


    # @ApiMember(Description="Optional database integration id. When omitted, the project's default database integration is used.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id. When omitted, the project's default database integration is used.
    """


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/many", "DELETE")
# @Api(Description="Delete many terms in a taxonomy matching the given filter")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteManyDatabaseTaxonomyTermsRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete many terms in a taxonomy matching the given filter
    """

    # @ApiMember(Description="Taxonomy id whose terms to delete, from get_database_taxonomies.", IsRequired=true)
    taxonomy_id: Optional[str] = None
    """
    Taxonomy id whose terms to delete, from get_database_taxonomies.
    """


    # @ApiMember(Description="Optional database integration id. When omitted, the project's default database integration is used.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id. When omitted, the project's default database integration is used.
    """


    # @ApiMember(Description="MongoDB extended-JSON match filter (a raw JSON object, e.g. {\"active\":false}) selecting which terms to delete. Automatically ANDed server-side with the taxonomyId, so it cannot affect other taxonomies.", IsRequired=true)
    filter: Optional[str] = None
    """
    MongoDB extended-JSON match filter (a raw JSON object, e.g. {"active":false}) selecting which terms to delete. Automatically ANDed server-side with the taxonomyId, so it cannot affect other taxonomies.
    """


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}", "GET")
# @Api(Description="Get a single term from a taxonomy by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomyTermRequest(CodeMashRequestBase, IReturn[GetDatabaseTaxonomyTermResponse]):
    """
    Get a single term from a taxonomy by id
    """

    # @ApiMember(Description="Taxonomy id from get_database_taxonomies.", IsRequired=true)
    taxonomy_id: Optional[str] = None
    """
    Taxonomy id from get_database_taxonomies.
    """


    # @ApiMember(Description="Term id from get_database_taxonomy_term_tree.", IsRequired=true)
    id: Optional[str] = None
    """
    Term id from get_database_taxonomy_term_tree.
    """


    # @ApiMember(Description="Optional database integration id. When omitted, the project's default database integration is used.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id. When omitted, the project's default database integration is used.
    """


# @Route("/{version}/database/taxonomies/{TaxonomyName}/merged-tree", "GET")
# @Api(Description="Returns a merged term tree across a taxonomy and its child taxonomies")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseMergedTermTreeRequest(CodeMashRequestBase, IReturn[GetDatabaseMergedTermTreeResponse]):
    """
    Returns a merged term tree across a taxonomy and its child taxonomies
    """

    # @ApiMember(Description="Root taxonomy slug/name (from get_database_taxonomies). Its terms are the roots; child-taxonomy terms nest under them.", IsRequired=true)
    taxonomy_name: Optional[str] = None
    """
    Root taxonomy slug/name (from get_database_taxonomies). Its terms are the roots; child-taxonomy terms nest under them.
    """


    # @ApiMember(Description="Optional database integration id. When omitted, the project's default database integration is used.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id. When omitted, the project's default database integration is used.
    """


# @Route("/{version}/database/taxonomies/{TaxonomyName}/terms/tree", "GET")
# @Api(Description="Returns the whole term tree of a taxonomy (or a sub-tree) in one call")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseTaxonomyTermTreeRequest(CodeMashRequestBase, IReturn[GetDatabaseTaxonomyTermTreeResponse]):
    """
    Returns the whole term tree of a taxonomy (or a sub-tree) in one call
    """

    # @ApiMember(Description="Taxonomy slug/name to fetch the term tree for, from get_database_taxonomies.", IsRequired=true)
    taxonomy_name: Optional[str] = None
    """
    Taxonomy slug/name to fetch the term tree for, from get_database_taxonomies.
    """


    # @ApiMember(Description="Optional term id to root the returned tree at a sub-tree instead of the whole taxonomy.")
    root_term_id: Optional[str] = None
    """
    Optional term id to root the returned tree at a sub-tree instead of the whole taxonomy.
    """


    # @ApiMember(DataType="integer", Description="Optional maximum depth to return below the root.")
    depth: Optional[int] = None
    """
    Optional maximum depth to return below the root.
    """


    # @ApiMember(Description="Optional database integration id. When omitted, the project's default database integration is used.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id. When omitted, the project's default database integration is used.
    """


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms", "POST")
# @Api(Description="Insert a single term into a taxonomy")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseTaxonomyTermRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Insert a single term into a taxonomy
    """

    # @ApiMember(Description="Taxonomy id to insert the term into, from get_database_taxonomies.", IsRequired=true)
    taxonomy_id: Optional[str] = None
    """
    Taxonomy id to insert the term into, from get_database_taxonomies.
    """


    # @ApiMember(Description="Optional database integration id. When omitted, the project's default database integration is used.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id. When omitted, the project's default database integration is used.
    """


    # @ApiMember(Description="The term to insert, as a MongoDB extended-JSON document string (a raw JSON object). Supported term fields: name (string, or a {lang:value} map — required); description; order (integer sort position, lower shows first — omit for unordered); parentId (id of the single parent term); multiParents (\"additional categories\": array of {taxonomyId, parentId}). The server stamps taxonomyId/taxonomyName automatically — do not include them. Example: {\"name\":\"France\",\"order\":1}.", IsRequired=true)
    document: Optional[str] = None
    """
    The term to insert, as a MongoDB extended-JSON document string (a raw JSON object). Supported term fields: name (string, or a {lang:value} map — required); description; order (integer sort position, lower shows first — omit for unordered); parentId (id of the single parent term); multiParents ("additional categories": array of {taxonomyId, parentId}). The server stamps taxonomyId/taxonomyName automatically — do not include them. Example: {"name":"France","order":1}.
    """


# @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}", "PUT")
# @Api(Description="Update a single term in a taxonomy by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateDatabaseTaxonomyTermRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Update a single term in a taxonomy by id
    """

    # @ApiMember(Description="Taxonomy id that owns the term, from get_database_taxonomies.", IsRequired=true)
    taxonomy_id: Optional[str] = None
    """
    Taxonomy id that owns the term, from get_database_taxonomies.
    """


    # @ApiMember(Description="Term id to update, from get_database_taxonomy_term_tree.", IsRequired=true)
    id: Optional[str] = None
    """
    Term id to update, from get_database_taxonomy_term_tree.
    """


    # @ApiMember(Description="Optional database integration id. When omitted, the project's default database integration is used.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id. When omitted, the project's default database integration is used.
    """


    # @ApiMember(Description="Partial update document as MongoDB extended-JSON (a raw JSON object of fields to change), applied with $set — only the given fields change. Updatable term fields: name (string or {lang:value} map); description; order (integer sort position, lower shows first — use this to numerate/rank terms; set null to clear); parentId (single parent term id — a term from THIS taxonomy's parent taxonomy; e.g. link a country to its region by setting the country term's parentId to the region term id); multiParents (\"additional categories\": array of {taxonomyId, parentId}). Example to rank a term: {\"order\":1}.", IsRequired=true)
    update: Optional[str] = None
    """
    Partial update document as MongoDB extended-JSON (a raw JSON object of fields to change), applied with $set — only the given fields change. Updatable term fields: name (string or {lang:value} map); description; order (integer sort position, lower shows first — use this to numerate/rank terms; set null to clear); parentId (single parent term id — a term from THIS taxonomy's parent taxonomy; e.g. link a country to its region by setting the country term's parentId to the region term id); multiParents ("additional categories": array of {taxonomyId, parentId}). Example to rank a term: {"order":1}.
    """


# @Route("/{version}/database/schemas/apply-bundle", "POST")
# @Api(Description="Creates every collection and taxonomy of a compiled IF bundle, linked and published")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ApplyDatabaseSchemaBundleRequest(CodeMashRequestBase, IReturn[ApplyDatabaseSchemaBundleResponse]):
    """
    Creates every collection and taxonomy of a compiled IF bundle, linked and published
    """

    # @ApiMember(Description="Comma-separated catalog entity ids to create from the reviewed catalog (e.g. \"blog_posts,comments\"). The usual input.")
    entities: Optional[str] = None
    """
    Comma-separated catalog entity ids to create from the reviewed catalog (e.g. "blog_posts,comments"). The usual input.
    """


    # @ApiMember(Description="Only for entities the catalog lacks: one IF entity object or an array of IF objects (JSON string). May also hold catalog refs with add_fields / remove_fields.")
    bundle_json: Optional[str] = None
    """
    Only for entities the catalog lacks: one IF entity object or an array of IF objects (JSON string). May also hold catalog refs with add_fields / remove_fields.
    """


    # @ApiMember(Description="Field tier to compile: minimal | standard (default) | extended.")
    tier: Optional[str] = None
    """
    Field tier to compile: minimal | standard (default) | extended.
    """


    # @ApiMember(Description="true = mark free-text fields (title, body, excerpt …) translatable for multilingual content. Default false.")
    translatable: bool = False
    """
    true = mark free-text fields (title, body, excerpt …) translatable for multilingual content. Default false.
    """


    # @ApiMember(Description="false = leave every collection as a draft instead of publishing v1. Default true.")
    publish: bool = False
    """
    false = leave every collection as a draft instead of publishing v1. Default true.
    """


# @Route("/{version}/database/schemas/{Id}", "DELETE")
# @Api(Description="Delete database schema (collection)")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseSchemaRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete database schema (collection)
    """

    # @ApiMember(Description="Schema id to delete, from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id to delete, from get_database_schemas.
    """


# @Route("/{version}/database/schemas/{Id}/draft", "DELETE")
# @Api(Description="Discards the working-copy draft of a database schema without publishing")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DiscardDatabaseSchemaDraftRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Discards the working-copy draft of a database schema without publishing
    """

    # @ApiMember(Description="Schema id whose draft to discard, from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id whose draft to discard, from get_database_schemas.
    """


# @Route("/{version}/database/schemas/{id}", "GET")
# @Api(Description="Gets database schema by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchema(CodeMashRequestBase, IReturn[GetDatabaseSchemaResponse]):
    """
    Gets database schema by id
    """

    # @ApiMember(Description="Schema id from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id from get_database_schemas.
    """


    # @ApiMember(DataType="integer", Description="Optional published version number to pin; omit for the latest published version.", Name="version", ParameterType="query")
    schema_version: Optional[int] = None
    """
    Optional published version number to pin; omit for the latest published version.
    """


# @Route("/{version}/database/schemas", "GET")
# @Api(Description="Gets database schemas (collections)")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemas(CodeMashListPaginationRequestBase, IReturn[GetDatabaseSchemasResponse]):
    """
    Gets database schemas (collections)
    """

    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/schemas/{Id}/draft", "GET")
# @Api(Description="Gets the current draft of a database schema")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaDraft(CodeMashRequestBase, IReturn[GetDatabaseSchemaDraftResponse]):
    """
    Gets the current draft of a database schema
    """

    # @ApiMember(Description="Schema id from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id from get_database_schemas.
    """


# @Route("/{version}/database/schemas/{Id}/list-settings", "GET")
# @Api(Description="Gets database schema records-list display settings")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaListSettings(CodeMashRequestBase, IReturn[GetDatabaseSchemaListSettingsResponse]):
    """
    Gets database schema records-list display settings
    """

    # @ApiMember(Description="Schema id from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id from get_database_schemas.
    """


# @Route("/{version}/database/schemas/{Id}/versions/diff", "GET")
# @Api(Description="Structural diff between two published versions of a database schema")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaVersionDiff(CodeMashRequestBase, IReturn[GetDatabaseSchemaVersionDiffResponse]):
    """
    Structural diff between two published versions of a database schema
    """

    # @ApiMember(Description="Schema id from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id from get_database_schemas.
    """


    # @ApiMember(DataType="integer", Description="Earlier published version number to diff from. Get valid values from get_database_schema_versions.", IsRequired=true)
    from_version: int = 0
    """
    Earlier published version number to diff from. Get valid values from get_database_schema_versions.
    """


    # @ApiMember(DataType="integer", Description="Later published version number to diff to. Get valid values from get_database_schema_versions.", IsRequired=true)
    to_version: int = 0
    """
    Later published version number to diff to. Get valid values from get_database_schema_versions.
    """


# @Route("/{version}/database/schemas/{Id}/versions", "GET")
# @Api(Description="Lists published version summaries for a database schema")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseSchemaVersions(CodeMashRequestBase, IReturn[GetDatabaseSchemaVersionsResponse]):
    """
    Lists published version summaries for a database schema
    """

    # @ApiMember(Description="Schema id from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id from get_database_schemas.
    """


# @Route("/{version}/database/schemas/{Id}/publish", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PublishDatabaseSchemaRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    id: Optional[str] = None
    confirmed: bool = False


# @Route("/{version}/database/schemas/{Id}/rename", "PUT")
# @Api(Description="Renames a database schema (collection)")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RenameDatabaseSchemaRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Renames a database schema (collection)
    """

    # @ApiMember(Description="Schema id to rename, from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id to rename, from get_database_schemas.
    """


    # @ApiMember(Description="New human-entered title (e.g. \"Company Employees\"); the slug is derived server-side.", IsRequired=true)
    title: Optional[str] = None
    """
    New human-entered title (e.g. "Company Employees"); the slug is derived server-side.
    """


    # @ApiMember(Description="When true (default), rejects the rename if another schema already owns the derived slug. Leave true unless explicitly asked to bypass the uniqueness check.")
    rename_unique_name: bool = False
    """
    When true (default), rejects the rename if another schema already owns the derived slug. Leave true unless explicitly asked to bypass the uniqueness check.
    """


# @Route("/{version}/database/schemas", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseSchemaRequest(CodeMashRequestBase, IReturn[IdResponse]):
    # @ApiMember(Description="Empty to create a new schema; set to an existing schema id (from get_database_schemas) to update its draft.")
    view_id: Optional[str] = None
    """
    Empty to create a new schema; set to an existing schema id (from get_database_schemas) to update its draft.
    """


    # @ApiMember(Description="Human-entered schema title (e.g. \"Company Employees\"); a slug is derived server-side.", IsRequired=true)
    schema_name: Optional[str] = None
    """
    Human-entered schema title (e.g. "Company Employees"); a slug is derived server-side.
    """


    # @ApiMember(Description="Raw JSON string matching the Norbix data meta-schema (https://norbix.ai/schemas/meta/v1.json). When unsure of the shape, read an existing schema with get_database_schema first.")
    data_schema: Optional[str] = None
    """
    Raw JSON string matching the Norbix data meta-schema (https://norbix.ai/schemas/meta/v1.json). When unsure of the shape, read an existing schema with get_database_schema first.
    """


    # @ApiMember(Description="OPTIONAL raw JSON string matching the Norbix UI/visual meta-schema (https://norbix.ai/schemas/ui/v1.json), describing the record form layout. If omitted or invalid, the backend auto-generates a flat-list form from the data schema; provide it to control the layout.")
    visual_schema: Optional[str] = None
    """
    OPTIONAL raw JSON string matching the Norbix UI/visual meta-schema (https://norbix.ai/schemas/ui/v1.json), describing the record form layout. If omitted or invalid, the backend auto-generates a flat-list form from the data schema; provide it to control the layout.
    """


    # @ApiMember(Description="Optional schema-level settings (e.g. record validation behavior).")
    settings: Optional[SchemaSettingsDto] = None
    """
    Optional schema-level settings (e.g. record validation behavior).
    """


# @Route("/{version}/database/schemas/{Id}/draft", "PUT")
# @Api(Description="Saves the working-copy draft of a database schema")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateDatabaseSchemaDraftRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Saves the working-copy draft of a database schema
    """

    # @ApiMember(Description="Schema id whose draft to replace, from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id whose draft to replace, from get_database_schemas.
    """


    # @ApiMember(Description="Raw JSON string matching the Norbix data meta-schema (https://norbix.ai/schemas/meta/v1.json) for the draft's data schema.")
    data_schema: Optional[str] = None
    """
    Raw JSON string matching the Norbix data meta-schema (https://norbix.ai/schemas/meta/v1.json) for the draft's data schema.
    """


    # @ApiMember(Description="Raw JSON string matching the Norbix UI/visual meta-schema (https://norbix.ai/schemas/ui/v1.json) for the draft's record form.")
    visual_schema: Optional[str] = None
    """
    Raw JSON string matching the Norbix UI/visual meta-schema (https://norbix.ai/schemas/ui/v1.json) for the draft's record form.
    """


# @Route("/{version}/database/schemas/{Id}/list-settings", "PUT")
# @Api(Description="Updates database schema records-list display settings")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateDatabaseSchemaListSettingsRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates database schema records-list display settings
    """

    # @ApiMember(Description="Schema id whose list settings to update, from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id whose list settings to update, from get_database_schemas.
    """


    # @ApiMember(Description="The complete new list settings object (full replace).", IsRequired=true)
    settings: Optional[SchemaListSettingsDto] = None
    """
    The complete new list settings object (full replace).
    """


# @Route("/{version}/database/schemas/{Id}/settings", "PUT")
# @Api(Description="Updates database schema settings")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateDatabaseSchemaSettingsRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Updates database schema settings
    """

    # @ApiMember(Description="Schema id whose settings to update, from get_database_schemas.", IsRequired=true)
    id: Optional[str] = None
    """
    Schema id whose settings to update, from get_database_schemas.
    """


    # @ApiMember(Description="The new schema settings object.", IsRequired=true)
    settings: Optional[SchemaSettingsDto] = None
    """
    The new schema settings object.
    """


# @Route("/{version}/database/collections/{collectionName}/aggregate", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AggregateRecords(CodeMashRequestBase, IReturn[AggregateRecordsResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name to run the aggregation against.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name to run the aggregation against.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The aggregation pipeline as a MongoDB extended-JSON array of stages.", IsRequired=true)
    pipeline: Optional[str] = None
    """
    The aggregation pipeline as a MongoDB extended-JSON array of stages.
    """


# @Route("/{version}/database/collections/{collectionName}/{id}/responsibility", "PUT")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChangeRecordResponsibility(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name the record lives in.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name the record lives in.
    """


    # @ApiMember(Description="The id of the record whose responsibility changes.", IsRequired=true)
    id: Optional[str] = None
    """
    The id of the record whose responsibility changes.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The new responsible user (owner) id.", IsRequired=true)
    new_responsible_user_id: Optional[str] = None
    """
    The new responsible user (owner) id.
    """


# @Route("/{version}/database/collections/{collectionName}/count", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CountRecords(CodeMashRequestBase, IReturn[CountRecordsResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name to count records in.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name to count records in.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="Optional MongoDB extended-JSON filter. Empty means count all records.")
    filter: Optional[str] = None
    """
    Optional MongoDB extended-JSON filter. Empty means count all records.
    """


    schema_version: Optional[int] = None


# @Route("/{version}/database/collections/{collectionName}/many", "DELETE")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteManyRecords(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name the records live in.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name the records live in.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The match filter as a MongoDB extended-JSON document. Required.", IsRequired=true)
    filter: Optional[str] = None
    """
    The match filter as a MongoDB extended-JSON document. Required.
    """


# @Route("/{version}/database/collections/{collectionName}/{id}", "DELETE")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteRecord(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name the record lives in.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name the record lives in.
    """


    # @ApiMember(Description="The id of the record to delete.", IsRequired=true)
    id: Optional[str] = None
    """
    The id of the record to delete.
    """


    database_integration_id: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}/distinct", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DistinctRecordValues(CodeMashRequestBase, IReturn[DistinctRecordValuesResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name to read from.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name to read from.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The document field (dotted path allowed) to get distinct values for, e.g. 'status'.", IsRequired=true)
    field: Optional[str] = None
    """
    The document field (dotted path allowed) to get distinct values for, e.g. 'status'.
    """


    # @ApiMember(Description="Optional MongoDB extended-JSON filter. Empty means consider all records.")
    filter: Optional[str] = None
    """
    Optional MongoDB extended-JSON filter. Empty means consider all records.
    """


    schema_version: Optional[int] = None


# @Route("/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ExecuteRecordsAggregate(CodeMashRequestBase, IReturn[ExecuteRecordsAggregateResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name to run the saved aggregation against.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name to run the saved aggregation against.
    """


    # @ApiMember(Description="The saved aggregate id (maggr_…) to execute.", IsRequired=true)
    aggregate_id: Optional[str] = None
    """
    The saved aggregate id (maggr_…) to execute.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="Optional key/value substitutions for {TokenKey} placeholders in the saved pipeline.")
    tokens: Optional[Dict[str, str]] = None
    """
    Optional key/value substitutions for {TokenKey} placeholders in the saved pipeline.
    """


# @Route("/{version}/database/collections/{collectionName}", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindRecords(CodeMashListPaginationRequestBase, IReturn[FindRecordsResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name to read from.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name to read from.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="Optional MongoDB extended-JSON filter. Empty means match all records.")
    filter: Optional[str] = None
    """
    Optional MongoDB extended-JSON filter. Empty means match all records.
    """


    # @ApiMember(Description="Optional contact id (ct_…) — only that contact's records are returned.")
    contact_id: Optional[str] = None
    """
    Optional contact id (ct_…) — only that contact's records are returned.
    """


    schema_version: Optional[int] = None
    paging_args: Optional[PagingArgs] = None
    sort_by: Optional[str] = None
    sort_order: Optional[int] = None


# @Route("/{version}/database/collections/{collectionName}/{id}", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FindOneRecord(CodeMashRequestBase, IReturn[FindOneRecordResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name to read from.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name to read from.
    """


    # @ApiMember(Description="The id of the record to fetch.", IsRequired=true)
    id: Optional[str] = None
    """
    The id of the record to fetch.
    """


    database_integration_id: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}/indexes", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCollectionIndexes(CodeMashRequestBase, IReturn[GetCollectionIndexesResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name to inspect.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name to inspect.
    """


    database_integration_id: Optional[str] = None


# @Route("/{version}/database/collections/{collectionName}/many", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InsertManyRecords(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name to insert into.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name to insert into.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The records to insert as a MongoDB extended-JSON array of documents.", IsRequired=true)
    documents: Optional[str] = None
    """
    The records to insert as a MongoDB extended-JSON array of documents.
    """


# @Route("/{version}/database/collections/{collectionName}", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InsertRecord(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name to insert into.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name to insert into.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The record to insert, as a MongoDB extended-JSON document string.", IsRequired=true)
    document: Optional[str] = None
    """
    The record to insert, as a MongoDB extended-JSON document string.
    """


# @Route("/{version}/database/collections/{collectionName}/{id}/replace", "PUT")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReplaceRecord(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name the record lives in.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name the record lives in.
    """


    # @ApiMember(Description="The id of the record to replace.", IsRequired=true)
    id: Optional[str] = None
    """
    The id of the record to replace.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The replacement document as MongoDB extended-JSON.", IsRequired=true)
    replacement: Optional[str] = None
    """
    The replacement document as MongoDB extended-JSON.
    """


# @Route("/{version}/database/collections/seed", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SeedCollectionRecords(CodeMashRequestBase, IReturn[SeedCollectionRecordsResponse]):
    """
    Database
    """

    # @ApiMember(Description="Seeding mode: 'dummy' (server-generated sample data, default) or 'realistic' (caller-supplied documents).")
    mode: Optional[str] = None
    """
    Seeding mode: 'dummy' (server-generated sample data, default) or 'realistic' (caller-supplied documents).
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="JSON array of {collectionName, count?, documents?}. count applies to dummy mode (max 100 per collection); documents (extended-JSON objects, may contain $seedRef placeholders) apply to realistic mode.", IsRequired=true)
    collections: Optional[str] = None
    """
    JSON array of {collectionName, count?, documents?}. count applies to dummy mode (max 100 per collection); documents (extended-JSON objects, may contain $seedRef placeholders) apply to realistic mode.
    """


# @Route("/{version}/database/collections/{collectionName}/many", "PUT")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateManyRecords(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name the records live in.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name the records live in.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The match filter as a MongoDB extended-JSON document. Empty object means match all.", IsRequired=true)
    filter: Optional[str] = None
    """
    The match filter as a MongoDB extended-JSON document. Empty object means match all.
    """


    # @ApiMember(Description="The partial update document (applied with $set), as MongoDB extended-JSON.", IsRequired=true)
    update: Optional[str] = None
    """
    The partial update document (applied with $set), as MongoDB extended-JSON.
    """


# @Route("/{version}/database/collections/{collectionName}/{id}", "PUT")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateOneRecord(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    # @ApiMember(Description="The collection (schema) name the record lives in.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The collection (schema) name the record lives in.
    """


    # @ApiMember(Description="The id of the record to update.", IsRequired=true)
    id: Optional[str] = None
    """
    The id of the record to update.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The partial update document (applied with $set), as MongoDB extended-JSON.", IsRequired=true)
    update: Optional[str] = None
    """
    The partial update document (applied with $set), as MongoDB extended-JSON.
    """


# @Route("/{version}/database/integrations/{Id}", "DELETE")
# @Api(Description="Delete integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete integration for particular project
    """

    # @ApiMember(Description="Database integration id to delete, from get_database_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Database integration id to delete, from get_database_integrations.
    """


# @Route("/{version}/database/integrations/{Id}/disable", "PUT")
# @Api(Description="Disable integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableDatabaseIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable integration for particular project
    """

    # @ApiMember(Description="Database integration id to disable, from get_database_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Database integration id to disable, from get_database_integrations.
    """


# @Route("/{version}/database/integrations/{Id}/enable", "PUT")
# @Api(Description="Enable integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableDatabaseIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable integration for particular project
    """

    # @ApiMember(Description="Database integration id to enable, from get_database_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Database integration id to enable, from get_database_integrations.
    """


# @Route("/{version}/database/integrations/{id}", "GET")
# @Api(Description="Gets integration by specified Id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseIntegration(CodeMashRequestBase, IReturn[GetDatabaseIntegrationResponse]):
    """
    Gets integration by specified Id
    """

    # @ApiMember(Description="Database integration id from get_database_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Database integration id from get_database_integrations.
    """


# @Route("/{version}/database/integrations", "GET")
# @Api(Description="Gets database integrations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseIntegrations(CodeMashListPaginationRequestBase, IReturn[GetDatabaseIntegrationsResponse]):
    """
    Gets database integrations
    """

    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/integrations/flex-tiers", "GET")
# @Api(Description="Returns the Flex tiers this account is entitled to pick")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAllowedFlexTiers(CodeMashRequestBase, IReturn[GetAllowedFlexTiersResponse]):
    """
    Returns the Flex tiers this account is entitled to pick
    """

    pass


# @Route("/{version}/database/integrations/{Id}/connection-string", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RevealManagedFlexConnectionString(CodeMashRequestBase, IReturn[RevealManagedFlexConnectionStringResponse]):
    id: Optional[str] = None


# @Route("/{version}/database/integrations", "POST")
# @Api(Description="Saves database integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Saves database integration
    """

    integration: Optional[DatabaseIntegrationRequest] = None


# @Route("/{version}/database/integrations/{Id}/default", "PUT")
# @Api(Description="Sets integration as default")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetDatabaseIntegrationAsDefaultRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Sets integration as default
    """

    # @ApiMember(Description="Database integration id to set as default, from get_database_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Database integration id to set as default, from get_database_integrations.
    """


# @Route("/{version}/database/integrations/test", "POST")
# @Api(Description="Test database integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestDatabaseIntegration(CodeMashRequestBase, IReturn[TestDatabaseIntegrationResponse]):
    """
    Test database integration
    """

    # @ApiMember(Description="Database integration id to test, from get_database_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    Database integration id to test, from get_database_integrations.
    """


# @Route("/{version}/database/imports", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateCollectionImport(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Database
    """

    # @ApiMember(Description="The uploaded CSV's file ref, from the upload call.", IsRequired=true)
    file: Optional[FileResourceRefDto] = None
    """
    The uploaded CSV's file ref, from the upload call.
    """


    # @ApiMember(Description="The target schema id.", IsRequired=true)
    schema_id: Optional[str] = None
    """
    The target schema id.
    """


    # @ApiMember(Description="The target collection (schema) name.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    The target collection (schema) name.
    """


    database_integration_id: Optional[str] = None
    # @ApiMember(Description="The CSV delimiter used at upload time.", IsRequired=true)
    delimiter: Optional[str] = None
    """
    The CSV delimiter used at upload time.
    """


    has_header: bool = False
    # @ApiMember(Description="Column → property mapping, frozen for this import.", IsRequired=true)
    mapping: List[ImportColumnMappingDto] = field(default_factory=list)
    """
    Column → property mapping, frozen for this import.
    """


# @Route("/{version}/database/imports/{Id}", "DELETE")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteCollectionImportRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Database
    """

    # @ApiMember(Description="The import id (imp_…).", IsRequired=true)
    id: Optional[str] = None
    """
    The import id (imp_…).
    """


    database_integration_id: Optional[str] = None


# @Route("/{version}/database/imports/{Id}", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCollectionImport(CodeMashRequestBase, IReturn[GetCollectionImportResponse]):
    """
    Database
    """

    # @ApiMember(Description="The import id (imp_…).", IsRequired=true)
    id: Optional[str] = None
    """
    The import id (imp_…).
    """


    database_integration_id: Optional[str] = None


# @Route("/{version}/database/imports", "GET")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetCollectionImports(CodeMashListPaginationRequestBase, IReturn[GetCollectionImportsResponse]):
    """
    Database
    """

    database_integration_id: Optional[str] = None


# @Route("/{version}/database/imports/upload-url", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RequestImportUploadUrlRequest(CodeMashRequestBase, IReturn[RequestImportUploadUrlResponse]):
    """
    Database
    """

    file_account_id: Optional[str] = None
    # @ApiMember(Description="The original CSV file name, e.g. people.csv.", IsRequired=true)
    file_name: Optional[str] = None
    """
    The original CSV file name, e.g. people.csv.
    """


# @Route("/{version}/database/imports/analyze", "POST")
# @Api(Description="Database")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AnalyzeImportFileRequest(CodeMashRequestBase, IReturn[AnalyzeImportFileResponse]):
    """
    Database
    """

    # @ApiMember(Description="The uploaded CSV's file ref, from the upload-url call.", IsRequired=true)
    file: Optional[FileResourceRefDto] = None
    """
    The uploaded CSV's file ref, from the upload-url call.
    """


    # @ApiMember(Description="The CSV delimiter, e.g. \",\" or \";\".", IsRequired=true)
    delimiter: Optional[str] = None
    """
    The CSV delimiter, e.g. "," or ";".
    """


    # @ApiMember(Description="Whether the first row is a header row.")
    has_header: bool = False
    """
    Whether the first row is a header row.
    """


# @Route("/{version}/database/aggregates/{Id}", "DELETE")
# @Api(Description="Delete saved Mongo aggregation")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteDatabaseAggregateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete saved Mongo aggregation
    """

    # @ApiMember(Description="Aggregate id to delete, from get_database_aggregates.", IsRequired=true)
    id: Optional[str] = None
    """
    Aggregate id to delete, from get_database_aggregates.
    """


    # @ApiMember(Description="Schema id that owns this aggregate, from get_database_schemas.", IsRequired=true)
    schema_id: Optional[str] = None
    """
    Schema id that owns this aggregate, from get_database_schemas.
    """


# @Route("/{version}/database/aggregates/{Id}", "GET")
# @Api(Description="Get saved Mongo aggregation by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseAggregate(CodeMashRequestBase, IReturn[GetDatabaseAggregateResponse]):
    """
    Get saved Mongo aggregation by id
    """

    # @ApiMember(Description="Aggregate id from get_database_aggregates.", IsRequired=true)
    id: Optional[str] = None
    """
    Aggregate id from get_database_aggregates.
    """


    # @ApiMember(Description="Schema id that owns this aggregate, from get_database_schemas.", IsRequired=true)
    schema_id: Optional[str] = None
    """
    Schema id that owns this aggregate, from get_database_schemas.
    """


# @Route("/{version}/database/aggregates", "GET")
# @Api(Description="Lists saved Mongo aggregations for a schema")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDatabaseAggregates(CodeMashListPaginationRequestBase, IReturn[GetDatabaseAggregatesResponse]):
    """
    Lists saved Mongo aggregations for a schema
    """

    # @ApiMember(Description="Schema id whose saved aggregates to list, from get_database_schemas.", IsRequired=true)
    schema_id: Optional[str] = None
    """
    Schema id whose saved aggregates to list, from get_database_schemas.
    """


    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/database/aggregates", "POST")
# @Api(Description="Creates or updates a saved Mongo aggregation")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDatabaseAggregateRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Creates or updates a saved Mongo aggregation
    """

    # @ApiMember(Description="Empty to create a new saved aggregate; set to an existing aggregate id (from get_database_aggregates) to update it.")
    view_id: Optional[str] = None
    """
    Empty to create a new saved aggregate; set to an existing aggregate id (from get_database_aggregates) to update it.
    """


    # @ApiMember(Description="Schema id that owns this aggregate, from get_database_schemas.", IsRequired=true)
    schema_id: Optional[str] = None
    """
    Schema id that owns this aggregate, from get_database_schemas.
    """


    # @ApiMember(Description="Human-readable display name for the saved aggregate.", IsRequired=true)
    display_name: Optional[str] = None
    """
    Human-readable display name for the saved aggregate.
    """


    # @ApiMember(Description="Optional free-text description of what the aggregate does.")
    description: Optional[str] = None
    """
    Optional free-text description of what the aggregate does.
    """


    # @ApiMember(Description="MongoDB aggregation pipeline JSON, optionally containing {TokenKey} placeholders substituted at execute time.", IsRequired=true)
    pipeline: Optional[str] = None
    """
    MongoDB aggregation pipeline JSON, optionally containing {TokenKey} placeholders substituted at execute time.
    """


# @Route("/{version}/database/aggregates/test", "POST")
# @Api(Description="Test-run an aggregation pipeline with caller-supplied tokens")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestDatabaseAggregateRequest(CodeMashRequestBase, IReturn[TestDatabaseAggregateResponse]):
    """
    Test-run an aggregation pipeline with caller-supplied tokens
    """

    # @ApiMember(Description="Optional database integration id. When omitted, the project's default database integration is used.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id. When omitted, the project's default database integration is used.
    """


    # @ApiMember(Description="Name of the collection (schema) to run the aggregation against.", IsRequired=true)
    collection_name: Optional[str] = None
    """
    Name of the collection (schema) to run the aggregation against.
    """


    # @ApiMember(Description="MongoDB aggregation pipeline JSON, optionally containing {TokenKey} placeholders to be substituted from tokens.", IsRequired=true)
    pipeline: Optional[str] = None
    """
    MongoDB aggregation pipeline JSON, optionally containing {TokenKey} placeholders to be substituted from tokens.
    """


    # @ApiMember(Description="Optional key/value substitutions for {TokenKey} placeholders in the pipeline.")
    tokens: Optional[Dict[str, str]] = None
    """
    Optional key/value substitutions for {TokenKey} placeholders in the pipeline.
    """


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
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationSetAsDefault:
    env: Optional[Env] = None
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationProvisioningStarted:
    integration_id: Optional[IntegrationId] = None
    atlas_project_id: Optional[str] = None
    atlas_cluster_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationProvisioningCompleted:
    integration_id: Optional[IntegrationId] = None
    connection_string_template: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationProvisioningFailed:
    integration_id: Optional[IntegrationId] = None
    reason: Optional[str] = None
    retryable: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DatabaseIntegrationDeprovisioned:
    integration_id: Optional[IntegrationId] = None
    atlas_project_id: Optional[str] = None
    atlas_cluster_name: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectStatusChanged:
    status: Optional[ProjectStatus] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaCreated:
    schema: Optional[Schema] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaMirrored:
    schema: Optional[Schema] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDraftUpdated:
    id: Optional[SchemaId] = None
    draft: Optional[SchemaDraft] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDraftDiscarded:
    id: Optional[SchemaId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaVersionPublished:
    id: Optional[SchemaId] = None
    version: Optional[PublishedSchemaVersion] = None
    diff: Optional[SchemaDiff] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaSettingsUpdated:
    id: Optional[SchemaId] = None
    settings: Optional[SchemaSettings] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDeleted:
    id: Optional[SchemaId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaRenamed:
    schema_id: Optional[SchemaId] = None
    new_name: Optional[SchemaName] = None
    rename_unique_name: bool = False
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaDataCleared:
    id: Optional[SchemaId] = None
    integrations: List[IntegrationId] = field(default_factory=list)
    env: Optional[Env] = None


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
class DatabaseTriggerMirrored:
    trigger: Optional[Trigger] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerEnabled(TriggerByIdEventBase):
    schema_id: Optional[SchemaId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerDisabled(TriggerByIdEventBase):
    schema_id: Optional[SchemaId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SchemaTriggerDeleted(TriggerByIdEventBase):
    schema_id: Optional[SchemaId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProcessCollectionImport:
    import_id: Optional[str] = None
    project_id: Optional[str] = None
    account_id: Optional[str] = None
    database_integration_id: Optional[str] = None
    env: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RecordInserted:
    project_id: Optional[ProjectId] = None
    database_integration_id: Optional[IntegrationId] = None
    schema_name: Optional[SchemaName] = None
    id: Optional[str] = None
    document: Optional[Object] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RecordUpdated:
    project_id: Optional[ProjectId] = None
    database_integration_id: Optional[IntegrationId] = None
    schema_name: Optional[SchemaName] = None
    id: Optional[str] = None
    from_: Optional[Object] = field(metadata=config(field_name='from'), default=None)
    to: Optional[Object] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RecordDeleted:
    project_id: Optional[ProjectId] = None
    database_integration_id: Optional[IntegrationId] = None
    schema_name: Optional[SchemaName] = None
    id: Optional[str] = None
    document: Optional[Object] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RecordReplaced:
    project_id: Optional[ProjectId] = None
    database_integration_id: Optional[IntegrationId] = None
    schema_name: Optional[SchemaName] = None
    id: Optional[str] = None
    from_: Optional[Object] = field(metadata=config(field_name='from'), default=None)
    to: Optional[Object] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RecordResponsibilityChanged:
    project_id: Optional[ProjectId] = None
    database_integration_id: Optional[IntegrationId] = None
    schema_name: Optional[SchemaName] = None
    id: Optional[str] = None
    from_owner: Optional[AuthId] = None
    to_owner: Optional[AuthId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RecordsInserted:
    project_id: Optional[ProjectId] = None
    database_integration_id: Optional[IntegrationId] = None
    schema_name: Optional[SchemaName] = None
    ids: Optional[IReadOnlyList[str]] = None
    documents: Optional[IReadOnlyList[Object]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RecordsUpdated:
    project_id: Optional[ProjectId] = None
    database_integration_id: Optional[IntegrationId] = None
    schema_name: Optional[SchemaName] = None
    matched_count: int = 0
    modified_count: int = 0
    update: Optional[Object] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RecordsDeleted:
    project_id: Optional[ProjectId] = None
    database_integration_id: Optional[IntegrationId] = None
    schema_name: Optional[SchemaName] = None
    deleted_count: int = 0
    filter: Optional[Object] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailVerificationCodeRequested(IPasskeyMessage):
    email: Optional[str] = None
    project_id: Optional[str] = None
    code: Optional[str] = None
    expires_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MagicLinkRequested(IPasskeyMessage):
    email: Optional[str] = None
    project_id: Optional[str] = None
    token: Optional[str] = None
    expires_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasswordResetRequested(IPasskeyMessage):
    email: Optional[str] = None
    project_id: Optional[str] = None
    token: Optional[str] = None
    expires_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PasswordChanged(IPasskeyMessage):
    email: Optional[str] = None
    project_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SseCallTriggered:
    project_id: Optional[ProjectId] = None
    account_id: Optional[AccountId] = None
    trigger_id: Optional[TriggerId] = None
    trigger_type: Optional[TriggerType] = None
    source_event: Optional[str] = None
    target_user_auth_id: Optional[str] = None
    schema_id: Optional[str] = None
    token_mappings: Optional[IReadOnlyDictionary[str, str]] = None
    correlation_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserRegistered:
    auth: Optional[Auth] = None
    link_to_user: Optional[UserId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserCreated:
    user_id: Optional[UserId] = None
    project_id: Optional[ProjectId] = None
    auth_id: Optional[AuthId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserUpdated:
    auth_id: Optional[AuthId] = None
    from_: Optional[UserGeneralInfo] = field(metadata=config(field_name='from'), default=None)
    to: Optional[UserGeneralInfo] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserBlocked:
    user: Optional[UserGeneralInfo] = None
    auth_id: Optional[AuthId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserUnblocked:
    user: Optional[UserGeneralInfo] = None
    auth_id: Optional[AuthId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserInvited:
    email_address: Optional[EmailAddress] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserVerified:
    auth_id: Optional[AuthId] = None
    user: Optional[UserGeneralInfo] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UserDeleted:
    user: Optional[UserGeneralInfo] = None
    auth_id: Optional[AuthId] = None


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
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteFilesTrigger(DeleteTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/files/triggers/{triggerId}/disable", "PATCH")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableFilesTrigger(DisableTrigger, IReturn[EmptyResponse]):
    pass


# @Route("/{version}/files/triggers/{triggerId}/enable", "PATCH")
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
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveFilesTrigger(SaveTrigger, IReturn[IdResponse]):
    pass


# @Route("/{version}/files/integrations/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteFilesIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Files integration id to delete, from get_files_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Files integration id to delete, from get_files_integrations.
    """


# @Route("/{version}/files/integrations/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableFilesIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Files integration id to disable, from get_files_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Files integration id to disable, from get_files_integrations.
    """


# @Route("/{version}/files/integrations/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableFilesIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Files integration id to enable, from get_files_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Files integration id to enable, from get_files_integrations.
    """


# @Route("/{version}/files/integrations/{id}", "GET")
# @Api(Description="Gets integration by specified Id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesIntegration(CodeMashRequestBase, IReturn[GetFilesIntegrationResponse]):
    """
    Gets integration by specified Id
    """

    # @ApiMember(Description="Files integration id to fetch, from get_files_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Files integration id to fetch, from get_files_integrations.
    """


# @Route("/{version}/files/integrations", "GET")
# @Api(Description="Gets integrations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFilesIntegrations(CodeMashListPaginationRequestBase, IReturn[GetFilesIntegrationsResponse]):
    """
    Gets integrations
    """

    pass


# @Route("/{version}/files/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveFilesIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    integration: Optional[FilesIntegrationRequest] = None


# @Route("/{version}/files/integrations/{Id}/default", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetFilesIntegrationAsDefaultRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Files integration id to set as default, from get_files_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Files integration id to set as default, from get_files_integrations.
    """


# @Route("/{version}/files/integrations/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestFilesIntegration(CodeMashRequestBase, IReturn[TestFilesIntegrationResponse]):
    # @ApiMember(Description="Integration id, from get_files_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    Integration id, from get_files_integrations.
    """


# @Route("/{version}/files/folder", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetFolderFiles(CodeMashListPaginationRequestBase, IReturn[GetFolderFilesResponse]):
    # @ApiMember(Description="The files integration id to list from, from get_files_integrations.", IsRequired=true)
    files_integration_id: Optional[str] = None
    """
    The files integration id to list from, from get_files_integrations.
    """


    # @ApiMember(Description="Path prefix to list. Empty / null lists the root.")
    path: Optional[str] = None
    """
    Path prefix to list. Empty / null lists the root.
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesEstablished:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesDisabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationSaved:
    integration: Optional[FileIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesIntegrationSetAsDefault:
    env: Optional[Env] = None
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesTriggerSaved:
    trigger: Optional[FileTrigger] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesTriggerMirrored:
    trigger: Optional[Trigger] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesTriggerEnabled(TriggerByIdEventBase):
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesTriggerDisabled(TriggerByIdEventBase):
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FilesTriggerDeleted(TriggerByIdEventBase):
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileUploaded:
    project_id: Optional[ProjectId] = None
    integration_id: Optional[IntegrationId] = None
    file_ref: Optional[FileResourceRef] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class FileDeleted:
    project_id: Optional[ProjectId] = None
    integration_id: Optional[IntegrationId] = None
    path: Optional[str] = None


# @Route("/{version}/notifications/email/disable", "GET")
# @Api(Description="Disable email service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableEmail(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable email service
    """

    pass


# @Route("/{version}/notifications/email/disable-dependencies", "GET")
# @Api(Description="Get email disable dependencies")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailDisableDependencies(CodeMashRequestBase, IReturn[GetNotificationModuleDisableDependenciesResponse]):
    """
    Get email disable dependencies
    """

    pass


# @Route("/{version}/notifications/email/enable", "GET")
# @Api(Description="Enable email service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableEmail(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable email service
    """

    pass


# @Route("/{version}/notifications/email/validation/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailValidationIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    integration: Optional[EmailValidationIntegrationRequest] = None


# @Route("/{version}/notifications/email/validation/integrations/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestEmailValidationIntegration(CodeMashRequestBase, IReturn[TestEmailValidationIntegrationResponse]):
    integration_id: Optional[str] = None


# @Route("/{version}/notifications/email/templates/attachments", "POST")
# @Api(Description="Attach a file to an email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AttachFileToTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Attach a file to an email template
    """

    # @ApiMember(Description="Optional language code to scope the attachment to a single translation. Omit to attach at the template level.")
    language: Optional[str] = None
    """
    Optional language code to scope the attachment to a single translation. Omit to attach at the template level.
    """


    # @ApiMember(Description="The email template id to attach the file to. Get it from get_email_templates.", IsRequired=true)
    template_id: Optional[str] = None
    """
    The email template id to attach the file to. Get it from get_email_templates.
    """


    # @ApiMember(Description="The file resource reference to attach (from a prior file upload).", IsRequired=true)
    file_ref: Optional[FileResourceRefDto] = None
    """
    The file resource reference to attach (from a prior file upload).
    """


# @Route("/{version}/notifications/email/templates", "POST")
# @Api(Description="Create an email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateEmailTemplateRequest(SaveEmailTemplate, IReturn[IdResponse]):
    """
    Create an email template
    """

    pass


# @Route("/{version}/notifications/email/templates/{Id}", "DELETE")
# @Api(Description="Delete an email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEmailTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete an email template
    """

    # @ApiMember(Description="The email template id to delete. Get it from get_email_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The email template id to delete. Get it from get_email_templates.
    """


# @Route("/{version}/notifications/email/templates/{id}", "GET")
# @Api(Description="Get an email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplate(CodeMashRequestBase, IReturn[GetEmailTemplateResponse]):
    """
    Get an email template
    """

    # @ApiMember(Description="The email template id to fetch. Get it from get_email_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The email template id to fetch. Get it from get_email_templates.
    """


# @Route("/{version}/notifications/email/templates", "GET")
# @Api(Description="Gets email templates")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplates(CodeMashListPaginationRequestBase, IReturn[GetEmailTemplatesResponse]):
    """
    Gets email templates
    """

    # @ApiMember(Description="Set true to include archived templates.")
    show_archived: Optional[bool] = None
    """
    Set true to include archived templates.
    """


    # @ApiMember(Description="Optional: return only the template with this id.")
    template_id: Optional[str] = None
    """
    Optional: return only the template with this id.
    """


# @Route("/{version}/notifications/email/templates/mjml", "POST")
# @Api(Description="Render MJML email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMjml(CodeMashRequestBase, IReturn[GetHtmlFromMjmlResponse]):
    """
    Render MJML email template
    """

    # @ApiMember(Description="The MJML/Razor template source code to render.", IsRequired=true)
    code: Optional[str] = None
    """
    The MJML/Razor template source code to render.
    """


    # @ApiMember(Description="Optional token values to bind into the template while rendering.")
    tokens: Optional[List[TokenMappingDto]] = None
    """
    Optional token values to bind into the template while rendering.
    """


    # @ApiMember(Description="Set true when rendering for a preview (vs. a final save), to affect how missing tokens are handled.")
    is_for_preview: bool = False
    """
    Set true when rendering for a preview (vs. a final save), to affect how missing tokens are handled.
    """


# @Route("/{version}/notifications/email/system-templates/{id}", "GET")
# @Api(Description="Get a system email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSystemEmailTemplate(CodeMashRequestBase, IReturn[GetSystemEmailTemplateResponse]):
    """
    Get a system email template
    """

    # @ApiMember(Description="The system email template id to fetch. Get it from get_system_email_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The system email template id to fetch. Get it from get_system_email_templates.
    """


# @Route("/{version}/notifications/email/system-templates", "GET")
# @Api(Description="Get system email templates")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSystemEmailTemplates(CodeMashListPaginationRequestBase, IReturn[GetSystemEmailTemplatesResponse]):
    """
    Get system email templates
    """

    # @ApiMember(Description="Optional group tags to filter templates by (e.g. newsletter, onboarding).")
    group_tags: Optional[List[str]] = None
    """
    Optional group tags to filter templates by (e.g. newsletter, onboarding).
    """


    # @ApiMember(Description="Optional visual themes to filter templates by.")
    themes: Optional[List[str]] = None
    """
    Optional visual themes to filter templates by.
    """


    # @ApiMember(Description="Optional communication channel to filter templates by (e.g. Transactional, Marketing).")
    communication_channel: Optional[CommunicationChannel] = None
    """
    Optional communication channel to filter templates by (e.g. Transactional, Marketing).
    """


    # @ApiMember(Description="Optional trigger type to filter templates that are designed for a specific automated trigger.")
    for_trigger: Optional[TriggerType] = None
    """
    Optional trigger type to filter templates that are designed for a specific automated trigger.
    """


# @Route("/{version}/notifications/email/templates/{id}/tokens", "GET")
# @Api(Description="Gets the tokens used by an email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailTemplateAvailableTokens(CodeMashRequestBase, IReturn[GetEmailTemplateAvailableTokensResponse]):
    """
    Gets the tokens used by an email template
    """

    # @ApiMember(Description="Template id from get_email_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    Template id from get_email_templates.
    """


# @Route("/{version}/notifications/email/templates", "PUT")
# @Api(Description="Update an email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateEmailTemplateRequest(SaveEmailTemplate, IReturn[EmptyResponse]):
    """
    Update an email template
    """

    # @ApiMember(Description="The email template id to update. Get it from get_email_templates.", IsRequired=true)
    view_id: Optional[str] = None
    """
    The email template id to update. Get it from get_email_templates.
    """


# @Route("/{version}/notifications/email/signatures/{id}", "DELETE")
# @Api(Description="Delete an email signature")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEmailSignature(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete an email signature
    """

    # @ApiMember(Description="The email signature id to delete. Get it from get_email_signatures.", IsRequired=true)
    id: Optional[str] = None
    """
    The email signature id to delete. Get it from get_email_signatures.
    """


# @Route("/{version}/notifications/email/signatures/{id}", "GET")
# @Api(Description="Get an email signature")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailSignature(CodeMashRequestBase, IReturn[GetEmailSignatureResponse]):
    """
    Get an email signature
    """

    # @ApiMember(Description="The email signature id to fetch. Get it from get_email_signatures.", IsRequired=true)
    id: Optional[str] = None
    """
    The email signature id to fetch. Get it from get_email_signatures.
    """


# @Route("/{version}/notifications/email/signatures", "GET")
# @Api(Description="Get email signatures")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailSignatures(CodeMashListPaginationRequestBase, IReturn[GetEmailSignaturesResponse]):
    """
    Get email signatures
    """

    pass


# @Route("/{version}/notifications/email/signatures", "POST")
# @Api(Description="Save an email signature")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailSignatureRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Save an email signature
    """

    # @ApiMember(Description="The signature id to update. Omit to create a new signature. Get it from get_email_signatures.")
    view_id: Optional[str] = None
    """
    The signature id to update. Omit to create a new signature. Get it from get_email_signatures.
    """


    # @ApiMember(Description="The display name of the signature.", IsRequired=true)
    display_name: Optional[str] = None
    """
    The display name of the signature.
    """


    # @ApiMember(Description="The per-language content translations for this signature.", IsRequired=true)
    translations: List[TranslationDto] = field(default_factory=list)
    """
    The per-language content translations for this signature.
    """


# @Route("/{version}/notifications/email/settings", "GET")
# @Api(Description="Get email settings")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailSettings(CodeMashRequestBase, IReturn[GetEmailSettingsResponse]):
    """
    Get email settings
    """

    # @ApiMember(Description="Unused legacy field; leave empty.")
    id: Optional[str] = None
    """
    Unused legacy field; leave empty.
    """


# @Route("/{version}/notifications/email/integrations/confirm-human-delivery", "POST")
# @Api(Description="Confirm human delivery of a test email")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmEmailIntegrationHumanDeliveryRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Confirm human delivery of a test email
    """

    # @ApiMember(Description="The email integration id the test delivery was confirmed for. Get it from get_email_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    The email integration id the test delivery was confirmed for. Get it from get_email_integrations.
    """


# @Route("/{version}/notifications/email/integrations/{Id}", "DELETE")
# @Api(Description="Delete an email integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEmailIntegration(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete an email integration
    """

    # @ApiMember(Description="The email integration id to delete. Get it from get_email_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The email integration id to delete. Get it from get_email_integrations.
    """


# @Route("/{version}/notifications/email/integrations/{Id}/disable", "PUT")
# @Api(Description="Disable an email integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableEmailIntegration(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable an email integration
    """

    # @ApiMember(Description="The email integration id to disable. Get it from get_email_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The email integration id to disable. Get it from get_email_integrations.
    """


# @Route("/{version}/notifications/email/integrations/domain-health", "POST")
# @Api(Description="Check email integration domain health")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CheckEmailIntegrationDomainHealthRequest(CodeMashRequestBase, IReturn[CheckEmailIntegrationDomainHealthResponse]):
    """
    Check email integration domain health
    """

    # @ApiMember(Description="The email integration id to check DNS health for. Get it from get_email_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    The email integration id to check DNS health for. Get it from get_email_integrations.
    """


# @Route("/{version}/notifications/email/integrations/{Id}/enable", "PUT")
# @Api(Description="Enable an email integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableEmailIntegration(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable an email integration
    """

    # @ApiMember(Description="The email integration id to enable. Get it from get_email_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The email integration id to enable. Get it from get_email_integrations.
    """


# @Route("/{version}/notifications/email/integrations/{id}", "GET")
# @Api(Description="Get an email integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailIntegration(CodeMashRequestBase, IReturn[GetEmailIntegrationResponse]):
    """
    Get an email integration
    """

    # @ApiMember(Description="The email integration id to fetch. Get it from get_email_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The email integration id to fetch. Get it from get_email_integrations.
    """


# @Route("/{version}/notifications/email/integrations", "GET")
# @Api(Description="Gets email integrations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailIntegrations(CodeMashListPaginationRequestBase, IReturn[GetEmailIntegrationsResponse]):
    """
    Gets email integrations
    """

    pass


# @Route("/{version}/notifications/email/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    integration: Optional[EmailIntegrationRequest] = None


# @Route("/{version}/notifications/email/integrations/{Id}/default", "PUT")
# @Api(Description="Set an email integration as default")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetEmailsIntegrationAsDefault(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Set an email integration as default
    """

    # @ApiMember(Description="The email integration id to set as default. Get it from get_email_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The email integration id to set as default. Get it from get_email_integrations.
    """


# @Route("/{version}/notifications/email/integrations/test", "POST")
# @Api(Description="Test an email integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestEmailIntegration(CodeMashRequestBase, IReturn[TestEmailIntegrationResponse]):
    """
    Test an email integration
    """

    # @ApiMember(Description="The email integration id to test. Get it from get_email_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    The email integration id to test. Get it from get_email_integrations.
    """


    # @ApiMember(Description="The recipient email address to send the test email to.", IsRequired=true)
    to: Optional[str] = None
    """
    The recipient email address to send the test email to.
    """


# @Route("/{version}/notifications/email/templates/{Id}/archive", "PUT")
# @Api(Description="Archive an email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ArchiveEmailTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Archive an email template
    """

    # @ApiMember(Description="The email template id to archive. Get it from get_email_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The email template id to archive. Get it from get_email_templates.
    """


# @Route("/{version}/notifications/email/templates/{Id}/clone", "POST")
# @Api(Description="Clone an email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CloneEmailTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Clone an email template
    """

    # @ApiMember(Description="The email template id to clone. Get it from get_email_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The email template id to clone. Get it from get_email_templates.
    """


# @Route("/{version}/notifications/email/templates/{Id}/unarchive", "PUT")
# @Api(Description="Un-archive an email template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnArchiveEmailTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Un-archive an email template
    """

    # @ApiMember(Description="The email template id to unarchive. Get it from get_email_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The email template id to unarchive. Get it from get_email_templates.
    """


# @Route("/{version}/notifications/email/footers/{id}", "DELETE")
# @Api(Description="Delete an email footer")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteEmailFooter(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete an email footer
    """

    # @ApiMember(Description="The email footer id to delete. Get it from get_email_footers.", IsRequired=true)
    id: Optional[str] = None
    """
    The email footer id to delete. Get it from get_email_footers.
    """


# @Route("/{version}/notifications/email/footers/{id}", "GET")
# @Api(Description="Get an email footer")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailFooter(CodeMashRequestBase, IReturn[GetEmailFooterResponse]):
    """
    Get an email footer
    """

    # @ApiMember(Description="The email footer id to fetch. Get it from get_email_footers.", IsRequired=true)
    id: Optional[str] = None
    """
    The email footer id to fetch. Get it from get_email_footers.
    """


# @Route("/{version}/notifications/email/footers", "GET")
# @Api(Description="Get email footers")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailFooters(CodeMashListPaginationRequestBase, IReturn[GetEmailFootersResponse]):
    """
    Get email footers
    """

    pass


# @Route("/{version}/notifications/email/footers", "POST")
# @Api(Description="Save an email footer")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveEmailFooterRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Save an email footer
    """

    # @ApiMember(Description="The footer id to update. Omit to create a new footer. Get it from get_email_footers.")
    view_id: Optional[str] = None
    """
    The footer id to update. Omit to create a new footer. Get it from get_email_footers.
    """


    # @ApiMember(Description="The display name of the footer.", IsRequired=true)
    display_name: Optional[str] = None
    """
    The display name of the footer.
    """


    # @ApiMember(Description="The per-language content translations for this footer.", IsRequired=true)
    translations: List[TranslationDto] = field(default_factory=list)
    """
    The per-language content translations for this footer.
    """


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
# @Api(Description="Gets email campaign by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaign(CodeMashRequestBase, IReturn[GetEmailCampaignResponse]):
    """
    Gets email campaign by id
    """

    # @ApiMember(Description="The campaign id.")
    id: Optional[str] = None
    """
    The campaign id.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/email/campaigns", "GET")
# @Api(Description="Gets email campaigns")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaigns(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignsResponse]):
    """
    Gets email campaigns
    """

    # @ApiMember(Description="Optional. When omitted, the project's default database integration is used (resolved server-side from the project state).")
    database_integration_id: Optional[str] = None
    """
    Optional. When omitted, the project's default database integration is used (resolved server-side from the project state).
    """


    # @ApiMember(Description="Optional: return only the campaign with this id.")
    campaign_id: Optional[str] = None
    """
    Optional: return only the campaign with this id.
    """


    # @ApiMember(Description="Optional: only campaigns that targeted this email address.")
    email_address: Optional[str] = None
    """
    Optional: only campaigns that targeted this email address.
    """


    # @ApiMember(Description="Optional: only campaigns built on this email template id.")
    template_id: Optional[str] = None
    """
    Optional: only campaigns built on this email template id.
    """


    # @ApiMember(Description="Optional lower bound for the campaign time, unix timestamp in seconds (UTC).")
    from_: Optional[int] = field(metadata=config(field_name='from'), default=None)
    """
    Optional lower bound for the campaign time, unix timestamp in seconds (UTC).
    """


    # @ApiMember(Description="Optional upper bound for the campaign time, unix timestamp in seconds (UTC).")
    to: Optional[int] = None
    """
    Optional upper bound for the campaign time, unix timestamp in seconds (UTC).
    """


# @Route("/{version}/notifications/email/campaigns/{id}/batches", "GET")
# @Api(Description="Get email campaign batches")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignBatches(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignBatchesResponse]):
    """
    Get email campaign batches
    """

    # @ApiMember(Description="The email campaign id to list batches for. Get it from get_all_email_campaigns.", IsRequired=true)
    id: Optional[str] = None
    """
    The email campaign id to list batches for. Get it from get_all_email_campaigns.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


    # @ApiMember(Description="Optional batch id to filter to a single batch. Get it from a prior call to this tool.")
    batch_id: Optional[str] = None
    """
    Optional batch id to filter to a single batch. Get it from a prior call to this tool.
    """


    # @ApiMember(Description="Optional recipient email address to filter batches by.")
    email_address: Optional[str] = None
    """
    Optional recipient email address to filter batches by.
    """


# @Route("/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}", "GET")
# @Api(Description="Get an email campaign batch notification")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignBatchNotification(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignBatchNotificationResponse]):
    """
    Get an email campaign batch notification
    """

    # @ApiMember(Description="The email campaign id. Get it from get_all_email_campaigns.", IsRequired=true)
    id: Optional[str] = None
    """
    The email campaign id. Get it from get_all_email_campaigns.
    """


    # @ApiMember(Description="The campaign batch id. Get it from get_email_campaign_batches.", IsRequired=true)
    batch_id: Optional[str] = None
    """
    The campaign batch id. Get it from get_email_campaign_batches.
    """


    # @ApiMember(Description="The notification id within the batch. Get it from get_email_campaign_batch_notifications.", IsRequired=true)
    notification_id: Optional[str] = None
    """
    The notification id within the batch. Get it from get_email_campaign_batch_notifications.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/email/campaigns/{id}/batches/{batchId}", "GET")
# @Api(Description="Get email campaign batch notifications")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignBatchNotifications(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignBatchNotificationsResponse]):
    """
    Get email campaign batch notifications
    """

    # @ApiMember(Description="The email campaign id. Get it from get_all_email_campaigns.", IsRequired=true)
    id: Optional[str] = None
    """
    The email campaign id. Get it from get_all_email_campaigns.
    """


    # @ApiMember(Description="The campaign batch id to list notifications for. Get it from get_email_campaign_batches.", IsRequired=true)
    batch_id: Optional[str] = None
    """
    The campaign batch id to list notifications for. Get it from get_email_campaign_batches.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/email/campaigns/{id}/stats", "GET")
# @Api(Description="Get email campaign statistics")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignStatistics(CodeMashRequestBase, IReturn[GetEmailCampaignStatisticsResponse]):
    """
    Get email campaign statistics
    """

    # @ApiMember(Description="The email campaign id to get statistics for. Get it from get_all_email_campaigns.", IsRequired=true)
    id: Optional[str] = None
    """
    The email campaign id to get statistics for. Get it from get_all_email_campaigns.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/email/preview", "GET")
# @Api(Description="Preview an email notification")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PreviewEmailNotification(RequestBase, IReturn[PreviewEmailNotificationResponse]):
    """
    Preview an email notification
    """

    # @ApiMember(Description="The opaque, pre-signed preview hash identifying the project and notification to preview.", IsRequired=true)
    hash: Optional[str] = None
    """
    The opaque, pre-signed preview hash identifying the project and notification to preview.
    """


# @Route("/{version}/notifications/email/campaigns/{Id}/stop", "POST")
# @Api(Description="Stops a running email campaign")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StopEmailCampaignRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Stops a running email campaign
    """

    # @ApiMember(Description="The campaign id to stop.")
    id: Optional[str] = None
    """
    The campaign id to stop.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/emails/campaigns/{campaignId}/messages/{id}", "GET")
# @Api(Description="Get an email campaign message")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignMessage(CodeMashRequestBase, IReturn[GetEmailCampaignMessageResponse]):
    """
    Get an email campaign message
    """

    # @ApiMember(Description="The email campaign id. Get it from get_all_email_campaigns.", IsRequired=true)
    campaign_id: Optional[str] = None
    """
    The email campaign id. Get it from get_all_email_campaigns.
    """


    # @ApiMember(Description="The campaign batch id. Get it from get_email_campaign_batches.", IsRequired=true)
    campaign_batch_id: Optional[str] = None
    """
    The campaign batch id. Get it from get_email_campaign_batches.
    """


    # @ApiMember(Description="The notification (message) id to fetch. Get it from get_email_campaign_messages.", IsRequired=true)
    notification_id: Optional[str] = None
    """
    The notification (message) id to fetch. Get it from get_email_campaign_messages.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/emails/campaigns/{campaignId}/messages", "GET")
# @Api(Description="Get email campaign messages")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetEmailCampaignMessagesRequest(CodeMashListPaginationRequestBase, IReturn[GetEmailCampaignMessagesResponse]):
    """
    Get email campaign messages
    """

    # @ApiMember(Description="The email campaign id. Get it from get_all_email_campaigns.", IsRequired=true)
    campaign_id: Optional[str] = None
    """
    The email campaign id. Get it from get_all_email_campaigns.
    """


    # @ApiMember(Description="The campaign batch id to list messages for. Get it from get_email_campaign_batches.", IsRequired=true)
    campaign_batch_id: Optional[str] = None
    """
    The campaign batch id to list messages for. Get it from get_email_campaign_batches.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailServiceEstablished:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ProjectDatabaseConnected:
    env: Optional[Env] = None


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
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailFooterMirrored:
    footer: Optional[EmailFooter] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailFooterDeleted:
    id: Optional[EmailFooterId] = None
    env: Optional[Env] = None


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
    env: Optional[Env] = None


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
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationSetAsDefault:
    env: Optional[Env] = None
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSignatureSaved:
    id: Optional[EmailSignatureId] = None
    name: Optional[DisplayName] = None
    translations: List[MessageTranslation[TemplateCode]] = field(default_factory=list)
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSignatureMirrored:
    signature: Optional[EmailSignature] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailSignatureDeleted:
    id: Optional[EmailSignatureId] = None
    env: Optional[Env] = None


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
    env: Optional[Env] = None


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
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateMirrored:
    template: Optional[EmailTemplate] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateBackfilled:
    template: Optional[EmailTemplate] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateDeleted:
    template_id: Optional[TemplateId] = None
    files_to_be_deleted: Optional[List[FileResourceRef]] = None
    file_integration_id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateArchived:
    template_id: Optional[TemplateId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailTemplateUnArchived:
    template_id: Optional[TemplateId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailValidationIntegrationSaved:
    integration: Optional[EmailValidationIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailValidationIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailValidationIntegrationSecretsConfigured:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailValidationIntegrationSecretsConfigurationFailed:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailValidationIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailBatchRegistered:
    project_id: Optional[ProjectId] = None
    campaign_id: Optional[CampaignId] = None
    campaign_batch_id: Optional[CampaignBatchId] = None
    starting_after: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailNotificationRead:
    project_id: Optional[ProjectId] = None
    campaign_id: Optional[CampaignId] = None
    campaign_batch_id: Optional[CampaignBatchId] = None
    notification_id: Optional[NotificationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailNotificationClicked:
    project_id: Optional[ProjectId] = None
    campaign_id: Optional[CampaignId] = None
    campaign_batch_id: Optional[CampaignBatchId] = None
    notification_id: Optional[NotificationId] = None
    source_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignStarted:
    project_id: Optional[ProjectId] = None
    campaign_id: Optional[CampaignId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignStopped:
    project_id: Optional[ProjectId] = None
    campaign_id: Optional[CampaignId] = None
    reason: Optional[CampaignStopReason] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignCompleted:
    project_id: Optional[ProjectId] = None
    campaign_id: Optional[CampaignId] = None
    errors: Optional[List[ErrorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignFailed:
    project_id: Optional[ProjectId] = None
    campaign_id: Optional[CampaignId] = None
    errors: List[ErrorDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailCampaignTriggered:
    project_id: Optional[ProjectId] = None
    trigger_id: Optional[TriggerId] = None
    trigger_type: Optional[TriggerType] = None
    source_event: Optional[str] = None
    schema_id: Optional[str] = None
    token_mappings: Optional[IReadOnlyDictionary[str, str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EmailDeliveryEventReceived:
    project_id: Optional[ProjectId] = None
    integration_id: Optional[IntegrationId] = None
    recipient: Optional[EmailAddress] = None
    type: Optional[EmailDeliveryEventType] = None
    occurred_at: datetime.datetime = datetime.datetime(1, 1, 1)
    provider_message_id: Optional[str] = None
    reason: Optional[str] = None


# @Route("/{version}/notifications/sms/disable", "GET")
# @Api(Description="Disable SMS service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableSms(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable SMS service
    """

    pass


# @Route("/{version}/notifications/sms/disable-dependencies", "GET")
# @Api(Description="Lists SMS-module dependencies shown before disable")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsDisableDependencies(CodeMashRequestBase, IReturn[GetNotificationModuleDisableDependenciesResponse]):
    """
    Lists SMS-module dependencies shown before disable
    """

    pass


# @Route("/{version}/notifications/sms/enable", "GET")
# @Api(Description="Enable SMS service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableSms(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable SMS service
    """

    pass


# @Route("/{version}/notifications/sms/templates/{Id}/archive", "PUT")
# @Api(Description="Archives sms template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ArchiveSmsTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Archives sms template
    """

    # @ApiMember(Description="The SMS template id to archive. Get it from get_sms_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS template id to archive. Get it from get_sms_templates.
    """


# @Route("/{version}/notifications/sms/templates/{Id}/clone", "POST")
# @Api(Description="Clones sms template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CloneSmsTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Clones sms template
    """

    # @ApiMember(Description="The SMS template id to clone. Get it from get_sms_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS template id to clone. Get it from get_sms_templates.
    """


# @Route("/{version}/notifications/sms/templates", "POST")
# @Api(Description="Create SMS template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateSmsTemplateRequest(SaveSmsTemplate, IReturn[IdResponse]):
    """
    Create SMS template
    """

    pass


# @Route("/{version}/notifications/sms/templates/{Id}", "DELETE")
# @Api(Description="Delete Sms Template for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteSmsTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete Sms Template for particular project
    """

    # @ApiMember(Description="The SMS template id to delete. Get it from get_sms_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS template id to delete. Get it from get_sms_templates.
    """


# @Route("/{version}/notifications/sms/templates/{id}", "GET")
# @Api(Description="Gets sms template by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsTemplate(CodeMashRequestBase, IReturn[GetSmsTemplateResponse]):
    """
    Gets sms template by id
    """

    # @ApiMember(Description="The SMS template id to fetch. Get it from get_sms_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS template id to fetch. Get it from get_sms_templates.
    """


# @Route("/{version}/notifications/sms/templates", "GET")
# @Api(Description="Gets sms templates")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsTemplates(CodeMashListPaginationRequestBase, IReturn[GetSmsTemplatesResponse]):
    """
    Gets sms templates
    """

    # @ApiMember(Description="Set true to include archived templates.")
    show_archived: Optional[bool] = None
    """
    Set true to include archived templates.
    """


    # @ApiMember(Description="Optional: return only the template with this id.")
    template_id: Optional[str] = None
    """
    Optional: return only the template with this id.
    """


# @Route("/{version}/notifications/sms/templates/{id}/tokens", "GET")
# @Api(Description="Goes through the Sms template and returns all the tokens that are used in the template translations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsMessageContentTokens(CodeMashRequestBase, IReturn[GetSmsMessageContentTokensResponse]):
    """
    Goes through the Sms template and returns all the tokens that are used in the template translations
    """

    # @ApiMember(Description="The SMS template id. Get it from get_sms_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS template id. Get it from get_sms_templates.
    """


# @Route("/{version}/notifications/sms/templates/render", "POST")
# @Api(Description="Runs the SMS Razor template, returns the bound text or the list of unresolved tokens.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RenderSms(CodeMashRequestBase, IReturn[RenderSmsTextResponse]):
    """
    Runs the SMS Razor template, returns the bound text or the list of unresolved tokens.
    """

    # @ApiMember(Description="The Razor SMS template code to render.")
    code: Optional[str] = None
    """
    The Razor SMS template code to render.
    """


    # @ApiMember(Description="Token name/value pairs to bind into the template.")
    tokens: Optional[List[TokenMappingDto]] = None
    """
    Token name/value pairs to bind into the template.
    """


    # @ApiMember(Description="Set true when rendering for a preview (relaxes some validation).")
    is_for_preview: bool = False
    """
    Set true when rendering for a preview (relaxes some validation).
    """


# @Route("/{version}/notifications/sms/templates/{Id}/unarchive", "PUT")
# @Api(Description="Un-archives sms template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnArchiveSmsTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Un-archives sms template
    """

    # @ApiMember(Description="The SMS template id to unarchive.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS template id to unarchive.
    """


# @Route("/{version}/notifications/sms/templates", "PUT")
# @Api(Description="Edit sms template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateSmsTemplateRequest(SaveSmsTemplate, IReturn[EmptyResponse]):
    """
    Edit sms template
    """

    # @ApiMember(Description="The SMS template id to update. Get it from get_sms_templates.", IsRequired=true)
    view_id: Optional[str] = None
    """
    The SMS template id to update. Get it from get_sms_templates.
    """


# @Route("/{version}/notifications/sms/settings", "GET")
# @Api(Description="Gets SMS settings")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsSettings(CodeMashRequestBase, IReturn[GetSmsSettingsResponse]):
    """
    Gets SMS settings
    """

    # @ApiMember(Description="Unused legacy parameter; leave empty.")
    id: Optional[str] = None
    """
    Unused legacy parameter; leave empty.
    """


# @Route("/{version}/notifications/sms/integrations/confirm-human-delivery", "POST")
# @Api(Description="Confirm that you received the test SMS delivery.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmSmsIntegrationHumanDeliveryRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Confirm that you received the test SMS delivery.
    """

    # @ApiMember(Description="The SMS integration id being verified. Get it from get_sms_integrations.")
    integration_id: Optional[str] = None
    """
    The SMS integration id being verified. Get it from get_sms_integrations.
    """


# @Route("/{version}/notifications/sms/integrations/{Id}", "DELETE")
# @Api(Description="Delete integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteSmsIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete integration for particular project
    """

    # @ApiMember(Description="The SMS integration id to delete. Get it from get_sms_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS integration id to delete. Get it from get_sms_integrations.
    """


# @Route("/{version}/notifications/sms/integrations/{Id}/disable", "PUT")
# @Api(Description="Disable integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableSmsIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable integration for particular project
    """

    # @ApiMember(Description="The SMS integration id to disable. Get it from get_sms_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS integration id to disable. Get it from get_sms_integrations.
    """


# @Route("/{version}/notifications/sms/integrations/{Id}/enable", "PUT")
# @Api(Description="Enable integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableSmsIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable integration for particular project
    """

    # @ApiMember(Description="The SMS integration id to enable. Get it from get_sms_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS integration id to enable. Get it from get_sms_integrations.
    """


# @Route("/{version}/notifications/sms/integrations/{id}", "GET")
# @Api(Description="Gets integration by specified Id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsIntegration(CodeMashRequestBase, IReturn[GetSmsIntegrationResponse]):
    """
    Gets integration by specified Id
    """

    # @ApiMember(Description="The SMS integration id to fetch. Get it from get_sms_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS integration id to fetch. Get it from get_sms_integrations.
    """


# @Route("/{version}/notifications/sms/integrations", "GET")
# @Api(Description="Gets sms integrations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsIntegrations(CodeMashListPaginationRequestBase, IReturn[GetSmsIntegrationsResponse]):
    """
    Gets sms integrations
    """

    pass


# @Route("/{version}/notifications/sms/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveSmsIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    integration: Optional[SmsIntegrationRequest] = None


# @Route("/{version}/notifications/sms/integrations/{Id}/default", "PUT")
# @Api(Description="Sets integration as default")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetSmsIntegrationAsDefaultRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Sets integration as default
    """

    # @ApiMember(Description="The SMS integration id to set as default. Get it from get_sms_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The SMS integration id to set as default. Get it from get_sms_integrations.
    """


# @Route("/{version}/notifications/sms/integrations/test", "POST")
# @Api(Description="Test SMS integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestSmsIntegration(CodeMashRequestBase, IReturn[TestSmsIntegrationResponse]):
    """
    Test SMS integration
    """

    # @ApiMember(Description="The SMS integration id to test. Get it from get_sms_integrations.")
    integration_id: Optional[str] = None
    """
    The SMS integration id to test. Get it from get_sms_integrations.
    """


    # @ApiMember(Description="Optional phone number (international format) to send the test SMS to.")
    to: Optional[str] = None
    """
    Optional phone number (international format) to send the test SMS to.
    """


# @Route("/{version}/notifications/sms/campaigns", "POST")
# @Api(Description="Create SMS campaign")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateSmsCampaignRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Create SMS campaign
    """

    # @ApiMember(Description="SMS template id to send — pick one with get_sms_templates. Never invent it.")
    template_id: Optional[str] = None
    """
    SMS template id to send — pick one with get_sms_templates. Never invent it.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


    # @ApiMember(Description="Optional language code forcing one template translation for every recipient.")
    language: Optional[str] = None
    """
    Optional language code forcing one template translation for every recipient.
    """


    initiator_id: Optional[str] = None
    # @ApiMember(Description="Audience type: 'AllUsers' (every project member subscribed to the SMS channel — role-based delivery can address MILLIONS of contacts), 'SpecifiedUsers' (exact member ids), or 'PhoneNumbers' (raw phone numbers). Fill EXACTLY the settings object matching this value. 'Collection' delivery is not available from chat.")
    delivery_type: Optional[SmsCampaignRecipientsSourceTypes] = None
    """
    Audience type: 'AllUsers' (every project member subscribed to the SMS channel — role-based delivery can address MILLIONS of contacts), 'SpecifiedUsers' (exact member ids), or 'PhoneNumbers' (raw phone numbers). Fill EXACTLY the settings object matching this value. 'Collection' delivery is not available from chat.
    """


    # @ApiMember(Description="For deliveryType 'AllUsers'. JSON object: {\"recipientsSourceType\":\"AllUsers\",\"rolesNames\":[\"authenticated\"],\"userTags\":[],\"campaignTime\":<unix seconds UTC>}. rolesNames/userTags are optional narrowing filters — verify exact role names with get_roles.")
    all_users: Optional[SmsToAllUsersDeliverySettingsDto] = None
    """
    For deliveryType 'AllUsers'. JSON object: {"recipientsSourceType":"AllUsers","rolesNames":["authenticated"],"userTags":[],"campaignTime":<unix seconds UTC>}. rolesNames/userTags are optional narrowing filters — verify exact role names with get_roles.
    """


    # @ApiMember(Description="For deliveryType 'SpecifiedUsers'. JSON object: {\"recipientsSourceType\":\"SpecifiedUsers\",\"recipients\":[<member ids>],\"campaignTime\":<unix seconds UTC>}.")
    specified_users: Optional[SmsToUsersDeliverySettingsDto] = None
    """
    For deliveryType 'SpecifiedUsers'. JSON object: {"recipientsSourceType":"SpecifiedUsers","recipients":[<member ids>],"campaignTime":<unix seconds UTC>}.
    """


    collection: Optional[SmsToCollectionRecordsDeliverySettingsDto] = None
    # @ApiMember(Description="For deliveryType 'PhoneNumbers'. JSON object: {\"recipientsSourceType\":\"PhoneNumbers\",\"phoneNumbers\":[\"+37060000000\"],\"campaignTime\":<unix seconds UTC>}. Numbers in international format.")
    phone_numbers: Optional[SmsToPhoneNumbersDeliverySettingsDto] = None
    """
    For deliveryType 'PhoneNumbers'. JSON object: {"recipientsSourceType":"PhoneNumbers","phoneNumbers":["+37060000000"],"campaignTime":<unix seconds UTC>}. Numbers in international format.
    """


# @Route("/{version}/notifications/sms/campaigns/{id}", "DELETE")
# @Api(Description="Deletes sms campaign from queue")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteSmsCampaign(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Deletes sms campaign from queue
    """

    # @ApiMember(Description="The campaign id to delete. Get it from get_sms_campaigns.", IsRequired=true)
    id: Optional[str] = None
    """
    The campaign id to delete. Get it from get_sms_campaigns.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/sms/campaigns/{id}", "GET")
# @Api(Description="Get sms campaign by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaign(CodeMashRequestBase, IReturn[GetSmsCampaignResponse]):
    """
    Get sms campaign by id
    """

    # @ApiMember(Description="The campaign id.")
    id: Optional[str] = None
    """
    The campaign id.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/sms/campaigns", "GET")
# @Api(Description="Gets sms campaigns")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaigns(CodeMashListPaginationRequestBase, IReturn[GetSmsCampaignsResponse]):
    """
    Gets sms campaigns
    """

    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


    # @ApiMember(Description="Optional: only campaigns built on this SMS template id.")
    template_id: Optional[str] = None
    """
    Optional: only campaigns built on this SMS template id.
    """


    # @ApiMember(Description="Optional lower bound for the campaign time, unix timestamp in seconds (UTC).")
    from_: Optional[int] = field(metadata=config(field_name='from'), default=None)
    """
    Optional lower bound for the campaign time, unix timestamp in seconds (UTC).
    """


    # @ApiMember(Description="Optional upper bound for the campaign time, unix timestamp in seconds (UTC).")
    to: Optional[int] = None
    """
    Optional upper bound for the campaign time, unix timestamp in seconds (UTC).
    """


# @Route("/{version}/notifications/sms/campaigns/{id}/batches", "GET")
# @Api(Description="Gets sms campaign batches")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignBatches(CodeMashListPaginationRequestBase, IReturn[GetSmsCampaignBatchesResponse]):
    """
    Gets sms campaign batches
    """

    # @ApiMember(Description="The campaign id. Get it from get_sms_campaigns.")
    id: Optional[str] = None
    """
    The campaign id. Get it from get_sms_campaigns.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/sms/campaigns/{id}/batches/{batchId}/{notificationId}", "GET")
# @Api(Description="Gets sms campaign batch notification")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignBatchNotification(CodeMashListPaginationRequestBase, IReturn[GetSmsCampaignBatchNotificationResponse]):
    """
    Gets sms campaign batch notification
    """

    # @ApiMember(Description="The campaign id. Get it from get_sms_campaigns.", IsRequired=true)
    id: Optional[str] = None
    """
    The campaign id. Get it from get_sms_campaigns.
    """


    # @ApiMember(Description="The campaign batch id. Get it from get_sms_campaign_batches.", IsRequired=true)
    batch_id: Optional[str] = None
    """
    The campaign batch id. Get it from get_sms_campaign_batches.
    """


    # @ApiMember(Description="The notification id. Get it from get_sms_campaign_batch_notifications.", IsRequired=true)
    notification_id: Optional[str] = None
    """
    The notification id. Get it from get_sms_campaign_batch_notifications.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/sms/campaigns/{id}/batches/{batchId}", "GET")
# @Api(Description="Gets sms campaign batch notifications")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignBatchNotifications(CodeMashListPaginationRequestBase, IReturn[GetSmsCampaignBatchNotificationsResponse]):
    """
    Gets sms campaign batch notifications
    """

    # @ApiMember(Description="The campaign id. Get it from get_sms_campaigns.", IsRequired=true)
    id: Optional[str] = None
    """
    The campaign id. Get it from get_sms_campaigns.
    """


    # @ApiMember(Description="The campaign batch id. Get it from get_sms_campaign_batches.", IsRequired=true)
    batch_id: Optional[str] = None
    """
    The campaign batch id. Get it from get_sms_campaign_batches.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/sms/campaigns/{id}/stats", "GET")
# @Api(Description="Get sms campaign statistics")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignStatistics(CodeMashRequestBase, IReturn[GetSmsCampaignStatisticsResponse]):
    """
    Get sms campaign statistics
    """

    # @ApiMember(Description="The campaign id. Get it from get_sms_campaigns.", IsRequired=true)
    id: Optional[str] = None
    """
    The campaign id. Get it from get_sms_campaigns.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/sms/preview", "GET")
# @Api(Description="Returns SMS preview notification body")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PreviewSmsNotification(RequestBase, IReturn[PreviewSmsNotificationResponse]):
    """
    Returns SMS preview notification body
    """

    # @ApiMember(Description="Signed preview hash identifying the notification to render.")
    hash: Optional[str] = None
    """
    Signed preview hash identifying the notification to render.
    """


# @Route("/{version}/notifications/sms/campaigns/{Id}/stop", "POST")
# @Api(Description="Stops a running SMS campaign")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StopSmsCampaignRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Stops a running SMS campaign
    """

    # @ApiMember(Description="The campaign id to stop.")
    id: Optional[str] = None
    """
    The campaign id to stop.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/sms/campaigns/{campaignId}/messages/{id}", "GET")
# @Api(Description="Gets campaign sms message details")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignMessage(CodeMashRequestBase, IReturn[GetSmsCampaignMessageResponse]):
    """
    Gets campaign sms message details
    """

    # @ApiMember(Description="The campaign id. Get it from get_sms_campaigns.", IsRequired=true)
    campaign_id: Optional[str] = None
    """
    The campaign id. Get it from get_sms_campaigns.
    """


    # @ApiMember(Description="The campaign batch id. Get it from get_sms_campaign_batches.", IsRequired=true)
    campaign_batch_id: Optional[str] = None
    """
    The campaign batch id. Get it from get_sms_campaign_batches.
    """


    # @ApiMember(Description="The notification (message) id. Get it from get_sms_campaign_messages.", IsRequired=true)
    notification_id: Optional[str] = None
    """
    The notification (message) id. Get it from get_sms_campaign_messages.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


# @Route("/{version}/notifications/sms/campaigns/{campaignId}/messages", "GET")
# @Api(Description="Gets the sms notifications")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSmsCampaignMessagesRequest(CodeMashListPaginationRequestBase, IReturn[GetSmsCampaignMessagesResponse]):
    """
    Gets the sms notifications
    """

    # @ApiMember(Description="The campaign id. Get it from get_sms_campaigns.", IsRequired=true)
    campaign_id: Optional[str] = None
    """
    The campaign id. Get it from get_sms_campaigns.
    """


    # @ApiMember(Description="The campaign batch id. Get it from get_sms_campaign_batches.", IsRequired=true)
    campaign_batch_id: Optional[str] = None
    """
    The campaign batch id. Get it from get_sms_campaign_batches.
    """


    # @ApiMember(Description="Optional. Omit to use the project default database integration (resolved per environment).")
    database_integration_id: Optional[str] = None
    """
    Optional. Omit to use the project default database integration (resolved per environment).
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationSaved:
    integration: Optional[SmsIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationHumanDeliveryConfirmed:
    id: Optional[IntegrationId] = None
    confirmed_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationSetAsDefault:
    env: Optional[Env] = None
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsServiceEstablished:
    default_templates: Optional[List[SmsTemplate]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsServiceEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsServiceDisabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsTemplateCreated:
    template_id: Optional[TemplateId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[SmsMessageContent]] = field(default_factory=list)
    channel: Optional[CommunicationChannel] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsTemplateUpdated:
    template_id: Optional[TemplateId] = None
    display_name: Optional[DisplayName] = None
    translations: List[MessageTranslation[SmsMessageContent]] = field(default_factory=list)
    channel: Optional[CommunicationChannel] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsTemplateMirrored:
    template: Optional[SmsTemplate] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsTemplateDeleted:
    template_id: Optional[TemplateId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsTemplateArchived:
    template_id: Optional[TemplateId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsTemplateUnArchived:
    template_id: Optional[TemplateId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsBatchRegistered:
    campaign_id: Optional[CampaignId] = None
    campaign_batch_id: Optional[CampaignBatchId] = None
    starting_after: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsNotificationRead:
    campaign_id: Optional[CampaignId] = None
    campaign_batch_id: Optional[CampaignBatchId] = None
    notification_id: Optional[NotificationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsNotificationClicked:
    campaign_id: Optional[CampaignId] = None
    campaign_batch_id: Optional[CampaignBatchId] = None
    notification_id: Optional[NotificationId] = None
    source_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsCampaignStarted:
    campaign_id: Optional[CampaignId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsCampaignStopped:
    campaign_id: Optional[CampaignId] = None
    reason: Optional[CampaignStopReason] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsCampaignCompleted:
    campaign_id: Optional[CampaignId] = None
    errors: Optional[List[ErrorDto]] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsCampaignFailed:
    campaign_id: Optional[CampaignId] = None
    errors: List[ErrorDto] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SmsCampaignTriggered:
    project_id: Optional[ProjectId] = None
    trigger_id: Optional[TriggerId] = None
    trigger_type: Optional[TriggerType] = None
    source_event: Optional[str] = None
    schema_id: Optional[str] = None
    token_mappings: Optional[IReadOnlyDictionary[str, str]] = None


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/secrets", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReplaceMarketplaceIntegrationSecretsRequest(CodeMashRequestBase, IReturn[EmptyMarketplaceSecretsResponse]):
    # @ApiMember(Description="Integration view id (int_…).", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id (int_…).
    """


    secrets: Dict[str, str] = field(default_factory=dict)


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/secrets/reveal", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RevealMarketplaceIntegrationSecretsRequest(CodeMashRequestBase, IReturn[RevealMarketplaceIntegrationSecretsResponse]):
    # @ApiMember(Description="Integration view id (int_…).", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id (int_…).
    """


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/token-mappings", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetMarketplaceIntegrationTokenMappingsRequest(CodeMashRequestBase, IReturn[SetMarketplaceIntegrationTokenMappingsResponse]):
    # @ApiMember(Description="Integration view id (int_…).", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id (int_…).
    """


    token_mappings: List[MarketplaceTokenMappingDto] = field(default_factory=list)


# @Route("/{version}/code/marketplace/integrations/{IntegrationViewId}/catalog", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMarketplaceFunctionCatalog(CodeMashRequestBase, IReturn[GetMarketplaceFunctionCatalogResponse]):
    # @ApiMember(Description="Integration view id, from get_marketplace_integrations.", IsRequired=true)
    integration_view_id: Optional[str] = None
    """
    Integration view id, from get_marketplace_integrations.
    """


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
    env: Optional[Env] = None


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
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationSetAsDefault:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CodeIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationSaved:
    integration: Optional[MarketplaceIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationSecretsConfigured:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceIntegrationSecretsConfigurationFailed:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionSaved:
    function: Optional[MarketplaceFunction] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionDeleted:
    integration_id: Optional[IntegrationId] = None
    function_id: Optional[MarketplaceFunctionId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionEnabled:
    integration_id: Optional[IntegrationId] = None
    function_id: Optional[MarketplaceFunctionId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarketplaceFunctionDisabled:
    integration_id: Optional[IntegrationId] = None
    function_id: Optional[MarketplaceFunctionId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ServerlessEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ServerlessDisabled:
    pass


# @Route("/{version}/notifications/push/disable", "GET")
# @Api(Description="Disable push service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePush(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable push service
    """

    pass


# @Route("/{version}/notifications/push/disable-dependencies", "GET")
# @Api(Description="Lists push disable dependencies")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushDisableDependencies(CodeMashRequestBase, IReturn[GetNotificationModuleDisableDependenciesResponse]):
    """
    Lists push disable dependencies
    """

    pass


# @Route("/{version}/notifications/push/enable", "GET")
# @Api(Description="Enable push service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePush(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable push service
    """

    pass


# @Route("/{version}/notifications/push/templates/{Id}/archive", "PUT")
# @Api(Description="Archives push template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ArchivePushTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Archives push template
    """

    # @ApiMember(Description="The push template id to archive. Get it from get_push_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The push template id to archive. Get it from get_push_templates.
    """


# @Route("/{version}/notifications/push/templates/{Id}/clone", "POST")
# @Api(Description="Clones push template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ClonePushTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Clones push template
    """

    # @ApiMember(Description="The push template id to clone. Get it from get_push_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The push template id to clone. Get it from get_push_templates.
    """


# @Route("/{version}/notifications/push/templates", "POST")
# @Api(Description="Create push template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreatePushTemplateRequest(SavePushTemplate, IReturn[IdResponse]):
    """
    Create push template
    """

    pass


# @Route("/{version}/notifications/push/templates/{Id}", "DELETE")
# @Api(Description="Delete push template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePushTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete push template
    """

    # @ApiMember(Description="The push template id to delete. Get it from get_push_templates.", IsRequired=true)
    id: Optional[str] = None
    """
    The push template id to delete. Get it from get_push_templates.
    """


# @Route("/{version}/notifications/push/templates/{id}", "GET")
# @Api(Description="Gets a push template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushTemplate(CodeMashRequestBase, IReturn[GetPushTemplateResponse]):
    """
    Gets a push template
    """

    # @ApiMember(Description="The push template id to fetch. Get it from get_push_templates.")
    id: Optional[str] = None
    """
    The push template id to fetch. Get it from get_push_templates.
    """


# @Route("/{version}/notifications/push/templates", "GET")
# @Api(Description="Gets push templates")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushTemplates(CodeMashListPaginationRequestBase, IReturn[GetPushTemplatesResponse]):
    """
    Gets push templates
    """

    # @ApiMember(Description="Set true to include archived templates.")
    show_archived: Optional[bool] = None
    """
    Set true to include archived templates.
    """


    # @ApiMember(Description="Optional: return only the template with this id.")
    template_id: Optional[str] = None
    """
    Optional: return only the template with this id.
    """


# @Route("/{version}/notifications/push/templates/{id}/tokens", "GET")
# @Api(Description="Gets push template content tokens")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushMessageContentTokens(CodeMashRequestBase, IReturn[GetPushMessageContentTokensResponse]):
    """
    Gets push template content tokens
    """

    # @ApiMember(Description="The push template id to scan for tokens. Get it from get_push_templates.")
    id: Optional[str] = None
    """
    The push template id to scan for tokens. Get it from get_push_templates.
    """


# @Route("/{version}/notifications/push/templates/render", "POST")
# @Api(Description="Renders a push template field")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RenderPush(CodeMashRequestBase, IReturn[RenderPushResponse]):
    """
    Renders a push template field
    """

    # @ApiMember(Description="The Razor template source for the field being rendered (Title, Body, or Subtitle).", IsRequired=true)
    code: Optional[str] = None
    """
    The Razor template source for the field being rendered (Title, Body, or Subtitle).
    """


    # @ApiMember(Description="Optional token values already bound for this render pass.")
    tokens: Optional[List[TokenMappingDto]] = None
    """
    Optional token values already bound for this render pass.
    """


    # @ApiMember(Description="Set true when rendering for a preview (relaxes strict validation).")
    is_for_preview: bool = False
    """
    Set true when rendering for a preview (relaxes strict validation).
    """


# @Route("/{version}/notifications/push/templates/{Id}/unarchive", "PUT")
# @Api(Description="Un-archives push template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UnArchivePushTemplateRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Un-archives push template
    """

    # @ApiMember(Description="The push template id to unarchive.", IsRequired=true)
    id: Optional[str] = None
    """
    The push template id to unarchive.
    """


# @Route("/{version}/notifications/push/templates", "PUT")
# @Api(Description="Edit push template")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdatePushTemplateRequest(SavePushTemplate, IReturn[EmptyResponse]):
    """
    Edit push template
    """

    # @ApiMember(Description="The push template id to update. Get it from get_push_templates.", IsRequired=true)
    view_id: Optional[str] = None
    """
    The push template id to update. Get it from get_push_templates.
    """


# @Route("/{version}/notifications/push/settings", "GET")
# @Api(Description="Gets push settings")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushSettings(CodeMashRequestBase, IReturn[GetPushSettingsResponse]):
    """
    Gets push settings
    """

    # @ApiMember(Description="The push settings id to fetch.")
    id: Optional[str] = None
    """
    The push settings id to fetch.
    """


# @Route("/{version}/notifications/push/integrations/confirm-human-delivery", "POST")
# @Api(Description="Confirm human delivery of a test push")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmPushIntegrationHumanDeliveryRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Confirm human delivery of a test push
    """

    # @ApiMember(Description="The push integration id being verified. Get it from get_push_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    The push integration id being verified. Get it from get_push_integrations.
    """


# @Route("/{version}/notifications/push/integrations/{Id}", "DELETE")
# @Api(Description="Delete push integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePushIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete push integration
    """

    # @ApiMember(Description="The push integration id to delete. Get it from get_push_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The push integration id to delete. Get it from get_push_integrations.
    """


# @Route("/{version}/notifications/push/integrations/{Id}/disable", "PUT")
# @Api(Description="Disable push integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePushIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable push integration
    """

    # @ApiMember(Description="The push integration id to disable. Get it from get_push_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The push integration id to disable. Get it from get_push_integrations.
    """


# @Route("/{version}/notifications/push/integrations/{Id}/enable", "PUT")
# @Api(Description="Enable push integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePushIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable push integration
    """

    # @ApiMember(Description="The push integration id to enable. Get it from get_push_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The push integration id to enable. Get it from get_push_integrations.
    """


# @Route("/{version}/notifications/push/integrations/{id}", "GET")
# @Api(Description="Gets a push integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushIntegration(CodeMashRequestBase, IReturn[GetPushIntegrationResponse]):
    """
    Gets a push integration
    """

    # @ApiMember(Description="The push integration id to fetch. Get it from get_push_integrations.")
    id: Optional[str] = None
    """
    The push integration id to fetch. Get it from get_push_integrations.
    """


# @Route("/{version}/notifications/push/integrations", "GET")
# @Api(Description="Gets push integrations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushIntegrations(CodeMashListPaginationRequestBase, IReturn[GetPushIntegrationsResponse]):
    """
    Gets push integrations
    """

    pass


# @Route("/{version}/notifications/push/integrations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePushIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    integration: Optional[PushIntegrationRequest] = None


# @Route("/{version}/notifications/push/integrations/{Id}/default", "PUT")
# @Api(Description="Sets push integration as default")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetPushIntegrationAsDefaultRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Sets push integration as default
    """

    # @ApiMember(Description="The push integration id to set as default. Get it from get_push_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    The push integration id to set as default. Get it from get_push_integrations.
    """


# @Route("/{version}/notifications/push/integrations/test", "POST")
# @Api(Description="Test push integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestPushIntegration(CodeMashRequestBase, IReturn[TestEmailIntegrationResponse]):
    """
    Test push integration
    """

    # @ApiMember(Description="The push integration id to test. Get it from get_push_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    The push integration id to test. Get it from get_push_integrations.
    """


    # @ApiMember(Description="Optional device token to send the test notification to. Requires DeliveryFamily when set.")
    test_token: Optional[str] = None
    """
    Optional device token to send the test notification to. Requires DeliveryFamily when set.
    """


    # @ApiMember(Description="Optional delivery family for the test token (e.g. Ios, Android, Chrome, Safari, Expo). Requires TestToken when set.")
    delivery_family: Optional[str] = None
    """
    Optional delivery family for the test token (e.g. Ios, Android, Chrome, Safari, Expo). Requires TestToken when set.
    """


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
# @Api(Description="Registers a device for push notifications")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RegisterDevice(RequestBase, IReturn[IdResponse], IHasProjectId):
    """
    Registers a device for push notifications
    """

    # @ApiMember(Description="The device details: OS, token, model, and delivery family.", IsRequired=true)
    push_device_dto: Optional[PushDeviceDto] = None
    """
    The device details: OS, token, model, and delivery family.
    """


    # @ApiMember(Description="The id of the user this device belongs to.", IsRequired=true)
    user_id: Optional[str] = None
    """
    The id of the user this device belongs to.
    """


    project_id: Optional[str] = None
    # @ApiMember(Description="Optional account id to associate with the device.")
    account_id: Optional[str] = None
    """
    Optional account id to associate with the device.
    """


    # @ApiMember(Description="Optional database integration id; omit to use the project's default.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id; omit to use the project's default.
    """


# @Route("/{version}/notifications/push/campaigns", "POST")
# @Api(Description="Create push campaign")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreatePushCampaignRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Create push campaign
    """

    campaign: Optional[PushCampaignRequest] = None
    database_integration_id: Optional[str] = None


# @Route("/{version}/notifications/push/campaigns/{Id}", "DELETE")
# @Api(Description="Deletes push campaign from queue")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePushCampaignRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Deletes push campaign from queue
    """

    pass


# @Route("/{version}/notifications/push/campaigns/{id}", "GET")
# @Api(Description="Gets push campaign by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaign(CodeMashRequestBase, IReturn[GetPushCampaignResponse]):
    """
    Gets push campaign by id
    """

    # @ApiMember(Description="The campaign id.")
    id: Optional[str] = None
    """
    The campaign id.
    """


    # @ApiMember(Description="Optional database integration id; omit to use the project's default.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id; omit to use the project's default.
    """


# @Route("/{version}/notifications/push/campaigns", "GET")
# @Api(Description="Gets push campaigns")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaigns(CodeMashListPaginationRequestBase, IReturn[GetPushCampaignsResponse]):
    """
    Gets push campaigns
    """

    # @ApiMember(Description="Optional database integration id; omit to use the project's default.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id; omit to use the project's default.
    """


    # @ApiMember(Description="Optional: only campaigns built on this push template id.")
    template_id: Optional[str] = None
    """
    Optional: only campaigns built on this push template id.
    """


    # @ApiMember(Description="Optional lower bound for the campaign time, unix timestamp in seconds (UTC).")
    from_: Optional[int] = field(metadata=config(field_name='from'), default=None)
    """
    Optional lower bound for the campaign time, unix timestamp in seconds (UTC).
    """


    # @ApiMember(Description="Optional upper bound for the campaign time, unix timestamp in seconds (UTC).")
    to: Optional[int] = None
    """
    Optional upper bound for the campaign time, unix timestamp in seconds (UTC).
    """


# @Route("/{version}/notifications/push/campaigns/{id}/batches", "GET")
# @Api(Description="Gets push campaign batches")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignBatches(CodeMashListPaginationRequestBase, IReturn[GetPushCampaignBatchesResponse]):
    """
    Gets push campaign batches
    """

    # @ApiMember(Description="The push campaign id to list batches for. Get it from get_push_campaigns.")
    id: Optional[str] = None
    """
    The push campaign id to list batches for. Get it from get_push_campaigns.
    """


    # @ApiMember(Description="Optional database integration id; omit to use the project's default.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id; omit to use the project's default.
    """


    # @ApiMember(Description="Optional: only return the batch with this id.")
    batch_id: Optional[str] = None
    """
    Optional: only return the batch with this id.
    """


# @Route("/{version}/notifications/push/campaigns/{id}/batches/{batchId}/{notificationId}", "GET")
# @Api(Description="Gets a push campaign batch notification")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignBatchNotification(CodeMashListPaginationRequestBase, IReturn[GetPushCampaignBatchNotificationResponse]):
    """
    Gets a push campaign batch notification
    """

    # @ApiMember(Description="The push campaign id. Get it from get_push_campaigns.")
    id: Optional[str] = None
    """
    The push campaign id. Get it from get_push_campaigns.
    """


    # @ApiMember(Description="The batch id. Get it from get_push_campaign_batches.")
    batch_id: Optional[str] = None
    """
    The batch id. Get it from get_push_campaign_batches.
    """


    # @ApiMember(Description="The notification id within the batch.")
    notification_id: Optional[str] = None
    """
    The notification id within the batch.
    """


    # @ApiMember(Description="Optional database integration id; omit to use the project's default.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id; omit to use the project's default.
    """


# @Route("/{version}/notifications/push/campaigns/{id}/batches/{batchId}", "GET")
# @Api(Description="Gets push campaign batch notifications")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignBatchNotifications(CodeMashListPaginationRequestBase, IReturn[GetPushCampaignBatchNotificationsResponse]):
    """
    Gets push campaign batch notifications
    """

    # @ApiMember(Description="The push campaign id. Get it from get_push_campaigns.")
    id: Optional[str] = None
    """
    The push campaign id. Get it from get_push_campaigns.
    """


    # @ApiMember(Description="The batch id to list notifications for. Get it from get_push_campaign_batches.")
    batch_id: Optional[str] = None
    """
    The batch id to list notifications for. Get it from get_push_campaign_batches.
    """


    # @ApiMember(Description="Optional database integration id; omit to use the project's default.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id; omit to use the project's default.
    """


# @Route("/{version}/notifications/push/campaigns/{id}/stats", "GET")
# @Api(Description="Get push campaign statistics")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignStatistics(CodeMashRequestBase, IReturn[GetPushCampaignStatisticsResponse]):
    """
    Get push campaign statistics
    """

    # @ApiMember(Description="The push campaign id to get statistics for. Get it from get_push_campaigns.")
    id: Optional[str] = None
    """
    The push campaign id to get statistics for. Get it from get_push_campaigns.
    """


    # @ApiMember(Description="Optional database integration id; omit to use the project's default.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id; omit to use the project's default.
    """


# @Route("/{version}/notifications/push/preview", "GET")
# @Api(Description="Returns push preview notification")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PreviewPushNotification(RequestBase, IReturn[PreviewPushNotificationResponse]):
    """
    Returns push preview notification
    """

    # @ApiMember(Description="The encrypted preview hash identifying the project and notification.")
    hash: Optional[str] = None
    """
    The encrypted preview hash identifying the project and notification.
    """


# @Route("/{version}/notifications/push/campaigns/{Id}/stop", "POST")
# @Api(Description="Stops a running push campaign")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StopPushCampaignRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Stops a running push campaign
    """

    pass


# @Route("/{version}/notifications/push/campaigns/{campaignId}/messages/{id}", "GET")
# @Api(Description="Gets campaign push notification details")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignMessage(CodeMashRequestBase, IReturn[GetPushCampaignMessageResponse]):
    """
    Gets campaign push notification details
    """

    # @ApiMember(Description="The push campaign id. Get it from get_push_campaigns.")
    campaign_id: Optional[str] = None
    """
    The push campaign id. Get it from get_push_campaigns.
    """


    # @ApiMember(Description="The batch id. Get it from get_push_campaign_batches.")
    campaign_batch_id: Optional[str] = None
    """
    The batch id. Get it from get_push_campaign_batches.
    """


    # @ApiMember(Description="The notification id within the batch.")
    notification_id: Optional[str] = None
    """
    The notification id within the batch.
    """


    # @ApiMember(Description="Optional database integration id; omit to use the project's default.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id; omit to use the project's default.
    """


# @Route("/{version}/notifications/push/campaigns/{campaignId}/messages", "GET")
# @Api(Description="Gets push campaign messages")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPushCampaignMessagesRequest(CodeMashListPaginationRequestBase, IReturn[GetPushCampaignMessagesResponse]):
    """
    Gets push campaign messages
    """

    # @ApiMember(Description="The push campaign id. Get it from get_push_campaigns.")
    campaign_id: Optional[str] = None
    """
    The push campaign id. Get it from get_push_campaigns.
    """


    # @ApiMember(Description="Optional: restrict results to this batch id. Get it from get_push_campaign_batches.")
    campaign_batch_id: Optional[str] = None
    """
    Optional: restrict results to this batch id. Get it from get_push_campaign_batches.
    """


    # @ApiMember(Description="Optional database integration id; omit to use the project's default.")
    database_integration_id: Optional[str] = None
    """
    Optional database integration id; omit to use the project's default.
    """


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
    env: Optional[Env] = None


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
class PushTemplateMirrored:
    template: Optional[PushTemplate] = None


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


# @Route("/{version}/payments/disable", "GET")
# @Api(Description="Disable payments service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePayments(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable payments service
    """

    pass


# @Route("/{version}/payments/enable", "GET")
# @Api(Description="Enable payments service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePayments(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable payments service
    """

    pass


# @Route("/{version}/payments/webhooks/log", "GET")
# @Api(Description="Gets the received payment webhooks log")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsWebhookLog(CodeMashRequestBase, IReturn[GetPaymentsWebhookLogResponse]):
    """
    Gets the received payment webhooks log
    """

    # @ApiMember(DataType="string", Description="Only rows for this payments integration (view id). Omit for the whole project.")
    integration_id: Optional[str] = None
    """
    Only rows for this payments integration (view id). Omit for the whole project.
    """


    # @ApiMember(DataType="int", Description="Max rows to return, newest first. Default 50, ceiling 200.")
    limit: Optional[int] = None
    """
    Max rows to return, newest first. Default 50, ceiling 200.
    """


# @Route("/{version}/payments/triggers/{triggerId}", "DELETE")
# @Api(Description="Delete payments trigger")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePaymentsTrigger(DeleteTrigger, IReturn[EmptyResponse]):
    """
    Delete payments trigger
    """

    pass


# @Route("/{version}/payments/triggers/{triggerId}/disable", "PATCH")
# @Api(Description="Disable payments trigger")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePaymentsTrigger(DisableTrigger, IReturn[EmptyResponse]):
    """
    Disable payments trigger
    """

    pass


# @Route("/{version}/payments/triggers/{triggerId}/enable", "PATCH")
# @Api(Description="Enable payments trigger")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePaymentsTrigger(EnableTrigger, IReturn[EmptyResponse]):
    """
    Enable payments trigger
    """

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
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePaymentsTrigger(SaveTrigger, IReturn[IdResponse]):
    pass


# @Route("/{version}/payments/integrations/confirm-human-delivery", "POST")
# @Api(Description="Confirm that you received or verified the test payment integration outcome.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ConfirmPaymentsIntegrationHumanDeliveryRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Confirm that you received or verified the test payment integration outcome.
    """

    # @ApiMember(Description="The id of the payments integration whose test outcome is being confirmed.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    The id of the payments integration whose test outcome is being confirmed.
    """


# @Route("/{version}/payments/integrations/{Id}", "DELETE")
# @Api(Description="Delete integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeletePaymentsIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete integration for particular project
    """

    # @ApiMember(Description="Payments integration id to delete, from get_payments_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Payments integration id to delete, from get_payments_integrations.
    """


# @Route("/{version}/payments/integrations/{Id}/disable", "PUT")
# @Api(Description="Disable integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisablePaymentsIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable integration for particular project
    """

    # @ApiMember(Description="Payments integration id to disable, from get_payments_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Payments integration id to disable, from get_payments_integrations.
    """


# @Route("/{version}/payments/integrations/{Id}/enable", "PUT")
# @Api(Description="Enable integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnablePaymentsIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable integration for particular project
    """

    # @ApiMember(Description="Payments integration id to enable, from get_payments_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Payments integration id to enable, from get_payments_integrations.
    """


# @Route("/{version}/payments/integrations/{id}", "GET")
# @Api(Description="Gets integration by specified Id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsIntegration(CodeMashRequestBase, IReturn[GetPaymentsIntegrationResponse]):
    """
    Gets integration by specified Id
    """

    # @ApiMember(Description="Payments integration id to fetch, from get_payments_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Payments integration id to fetch, from get_payments_integrations.
    """


# @Route("/{version}/payments/integrations", "GET")
# @Api(Description="Gets integrations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetPaymentsIntegrations(CodeMashListPaginationRequestBase, IReturn[GetPaymentsIntegrationsResponse]):
    """
    Gets integrations
    """

    pass


# @Route("/{version}/payments/integrations", "POST")
# @Api(Description="Saves payments integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SavePaymentsIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Saves payments integration
    """

    integration: Optional[PaymentIntegrationRequest] = None


# @Route("/{version}/payments/integrations/test", "POST")
# @Api(Description="Test payments integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestPaymentsIntegration(CodeMashRequestBase, IReturn[TestPaymentsIntegrationResponse]):
    """
    Test payments integration
    """

    # @ApiMember(Description="The id of the payments integration to test.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    The id of the payments integration to test.
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsIntegrationSaved:
    integration: Optional[PaymentIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsIntegrationHumanDeliveryConfirmed:
    id: Optional[IntegrationId] = None
    confirmed_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsEstablished:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsEnabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsDisabled:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsTriggerSaved:
    trigger: Optional[PaymentTrigger] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentTriggerMirrored:
    trigger: Optional[Trigger] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsTriggerEnabled(TriggerByIdEventBase):
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsTriggerDisabled(TriggerByIdEventBase):
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PaymentsTriggerDeleted(TriggerByIdEventBase):
    env: Optional[Env] = None


# @Route("/{version}/logs/disable", "GET")
# @Api(Description="Disable logging service")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableLogging(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable logging service
    """

    pass


# @Route("/{version}/logs/enable", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableLogging(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(DataType="boolean", Description="When true, also create a Norbix Logging integration backed by the project's default database.", Name="createNorbixLogging", ParameterType="query")
    create_norbix_logging: bool = False
    """
    When true, also create a Norbix Logging integration backed by the project's default database.
    """


# @Route("/{version}/logs/integrations/{Id}", "DELETE")
# @Api(Description="Delete integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteLoggingIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Delete integration for particular project
    """

    # @ApiMember(Description="Logging integration id to delete, from get_logging_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Logging integration id to delete, from get_logging_integrations.
    """


    # @ApiMember(Description="When true and this is a Norbix Logging integration, also permanently wipes the stored log entries in its backing database. Ignored for other providers.")
    wipe_logs: bool = False
    """
    When true and this is a Norbix Logging integration, also permanently wipes the stored log entries in its backing database. Ignored for other providers.
    """


# @Route("/{version}/logs/integrations/{Id}/disable", "PUT")
# @Api(Description="Disable integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableLoggingIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Disable integration for particular project
    """

    # @ApiMember(Description="Logging integration id to disable, from get_logging_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Logging integration id to disable, from get_logging_integrations.
    """


# @Route("/{version}/logs/integrations/{Id}/enable", "PUT")
# @Api(Description="Enable integration for particular project")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableLoggingIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Enable integration for particular project
    """

    # @ApiMember(Description="Logging integration id to enable, from get_logging_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Logging integration id to enable, from get_logging_integrations.
    """


# @Route("/{version}/logs/integrations/{id}", "GET")
# @Api(Description="Gets integration by specified Id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLoggingIntegration(CodeMashRequestBase, IReturn[GetLoggingIntegrationResponse]):
    """
    Gets integration by specified Id
    """

    # @ApiMember(Description="Logging integration id to fetch, from get_logging_integrations.", IsRequired=true)
    id: Optional[str] = None
    """
    Logging integration id to fetch, from get_logging_integrations.
    """


# @Route("/{version}/logs/integrations", "GET")
# @Api(Description="Gets integrations")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLoggingIntegrations(CodeMashListPaginationRequestBase, IReturn[GetLoggingIntegrationsResponse]):
    """
    Gets integrations
    """

    pass


# @Route("/{version}/logs/integrations", "POST")
# @Api(Description="Saves logging integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveLoggingIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Saves logging integration
    """

    integration: Optional[LoggingIntegrationRequest] = None


# @Route("/{version}/logs/integrations/test", "POST")
# @Api(Description="Test logging integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestLoggingIntegration(CodeMashRequestBase, IReturn[TestLoggingIntegrationResponse]):
    """
    Test logging integration
    """

    # @ApiMember(Description="Logging integration id to test, from get_logging_integrations.", IsRequired=true)
    integration_id: Optional[str] = None
    """
    Logging integration id to test, from get_logging_integrations.
    """


# @Route("/{version}/logs/clean", "POST")
# @Api(Description="Delete every log entry stored in the project's Norbix Logging integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CleanLogs(CodeMashRequestBase, IReturn[CleanLogsResponse]):
    """
    Delete every log entry stored in the project's Norbix Logging integration
    """

    pass


# @Route("/{version}/logs/audit", "GET")
# @Api(Description="Fetch the audit trail for a correlation id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLogsByCorrelationId(CodeMashRequestBase, IReturn[GetLogsByCorrelationIdResponse]):
    """
    Fetch the audit trail for a correlation id
    """

    # @ApiMember(DataType="string", Description="The correlation id whose full request trail you want.", IsRequired=true, Name="correlationId", ParameterType="query")
    target_correlation_id: Optional[str] = None
    """
    The correlation id whose full request trail you want.
    """


# @Route("/{version}/logs", "GET")
# @Api(Description="Fetch a filtered, cursor-paged list of tenant log entries")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLogs(CodeMashListPaginationRequestBase, IReturn[GetLogsResponse]):
    """
    Fetch a filtered, cursor-paged list of tenant log entries
    """

    # @ApiMember(DataType="string", Description="Severity filter: Information, Warning or Error.", Name="level", ParameterType="query")
    level: Optional[str] = None
    """
    Severity filter: Information, Warning or Error.
    """


    # @ApiMember(DataType="string", Description="Module filter: Database, Email, Membership, etc.", Name="module", ParameterType="query")
    module: Optional[str] = None
    """
    Module filter: Database, Email, Membership, etc.
    """


    # @ApiMember(DataType="string", Description="Correlation id filter. Empty = no filter (show all).", Name="logCorrelationId", ParameterType="query")
    log_correlation_id: Optional[str] = None
    """
    Correlation id filter. Empty = no filter (show all).
    """


    # @ApiMember(DataType="string", Description="Exact event code filter (e.g. db:record:insert).", Name="eventCode", ParameterType="query")
    event_code: Optional[str] = None
    """
    Exact event code filter (e.g. db:record:insert).
    """


    # @ApiMember(DataType="string", Description="Free-text search over title and message.", Name="search", ParameterType="query")
    search: Optional[str] = None
    """
    Free-text search over title and message.
    """


    # @ApiMember(Description="Start of the timestamp range (inclusive, UTC). Optional.")
    from_utc: Optional[datetime.datetime] = None
    """
    Start of the timestamp range (inclusive, UTC). Optional.
    """


    # @ApiMember(Description="End of the timestamp range (inclusive, UTC). Optional.")
    to_utc: Optional[datetime.datetime] = None
    """
    End of the timestamp range (inclusive, UTC). Optional.
    """


# @Route("/{version}/logs/settings", "GET")
# @Api(Description="Fetch the per-project log settings (flags)")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLogSettings(CodeMashRequestBase, IReturn[GetLogSettingsResponse]):
    """
    Fetch the per-project log settings (flags)
    """

    pass


# @Route("/{version}/logs/settings", "POST")
# @Api(Description="Update the per-project log settings (flags)")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveLogSettings(CodeMashRequestBase, IReturn[SaveLogSettingsResponse]):
    """
    Update the per-project log settings (flags)
    """

    # @ApiMember(Description="Drop log entries from requests originating from the Norbix studio (cloud dashboard).")
    skip_cloud_dashboard_logs: bool = False
    """
    Drop log entries from requests originating from the Norbix studio (cloud dashboard).
    """


    # @ApiMember(Description="Strip request/response body meta off http:request / http:response log entries.")
    skip_http_body_meta: bool = False
    """
    Strip request/response body meta off http:request / http:response log entries.
    """


    # @ApiMember(Description="Turn on tenant-visible log entries for AI chat turns. Default false.")
    ai_chat_logging_enabled: bool = False
    """
    Turn on tenant-visible log entries for AI chat turns. Default false.
    """


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
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationRenamed:
    id: Optional[IntegrationId] = None
    name: Optional[DisplayName] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationSecretsConfigured:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationSecretsConfigurationFailed:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationSecretsCleared:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationSecretsClearingFailed:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LoggingIntegrationSetAsDefault:
    id: Optional[IntegrationId] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class NorbixLoggingLogsWipeRequested:
    deleted_integration_id: Optional[IntegrationId] = None
    database_integration_id: Optional[IntegrationId] = None


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


# @Route("/{version}/account/ai/tools", "GET")
# @Api(Description="Lists the AI tools this host exposes (external-agent bridge).")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAiToolsRequest(RequestBase, IReturn[GetAiToolsResponse]):
    """
    Lists the AI tools this host exposes (external-agent bridge).
    """

    toolset: Optional[str] = None


# @Route("/{version}/account/ai/tools/{ToolName}", "POST")
# @Api(Description="Invokes one AI tool directly (external-agent bridge).")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InvokeAiToolRequest(RequestBase, IReturn[InvokeAiToolResponse]):
    """
    Invokes one AI tool directly (external-agent bridge).
    """

    tool_name: Optional[str] = None
    arguments_json: Optional[str] = None


# @Route("/{version}/account/chat/complete", "POST")
# @Api(Description="Gets account info.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AskChatRequest(RequestBase, IReturn[AskChatResponse]):
    """
    Gets account info.
    """

    prompt: Optional[str] = None
    profile: Optional[str] = None


# @Route("/{version}/account/chat/attachments", "POST")
# @Api(Description="Uploads a file into an AI chat session.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UploadChatAttachmentRequest(RequestBase, IReturn[UploadChatAttachmentResponse]):
    """
    Uploads a file into an AI chat session.
    """

    session_id: Optional[str] = None
    file_name: Optional[str] = None
    content_type: Optional[str] = None
    base64_content: Optional[str] = None
    profile: Optional[str] = None
    topic: Optional[str] = None
    project_id: Optional[str] = None
    env: Optional[str] = None


# @Route("/{version}/account/chat/availability", "GET")
# @Api(Description="Reports AI chat availability and the model-picker menu.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatAvailabilityRequest(RequestBase, IReturn[ChatAvailabilityResponse]):
    """
    Reports AI chat availability and the model-picker menu.
    """

    project_id: Optional[str] = None
    env: Optional[str] = None


# @Route("/{version}/account/chat/memory", "GET")
# @Api(Description="Lists what the AI assistant remembers about this account.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetChatMemoryRequest(RequestBase, IReturn[GetChatMemoryResponse]):
    """
    Lists what the AI assistant remembers about this account.
    """

    project_id: Optional[str] = None


# @Route("/{version}/account/chat/memory/{NoteId}", "DELETE")
# @Api(Description="Deletes one AI memory note ('forget this').")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ForgetChatMemoryRequest(RequestBase, IReturn[EmptyResponse]):
    """
    Deletes one AI memory note ('forget this').
    """

    note_id: Optional[str] = None


# @Route("/{version}/account/chat/sessions/{SessionId}", "DELETE")
# @Api(Description="Deletes an AI chat session (soft delete).")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteChatSessionRequest(RequestBase, IReturn[IdResponse]):
    """
    Deletes an AI chat session (soft delete).
    """

    session_id: Optional[str] = None


# @Route("/{version}/account/chat/sessions/{SessionId}/archive", "PATCH")
# @Api(Description="Archives or unarchives an AI chat session.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetChatSessionArchivedRequest(RequestBase, IReturn[IdResponse]):
    """
    Archives or unarchives an AI chat session.
    """

    session_id: Optional[str] = None
    archived: bool = False


# @Route("/{version}/account/chat/sessions/{SessionId}/pin", "PATCH")
# @Api(Description="Pins or unpins an AI chat session.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetChatSessionPinnedRequest(RequestBase, IReturn[IdResponse]):
    """
    Pins or unpins an AI chat session.
    """

    session_id: Optional[str] = None
    pinned: bool = False


# @Route("/{version}/account/chat/sessions/{SessionId}/sharing", "PATCH")
# @Api(Description="Marks or unmarks an AI chat session as \"do not share\".")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetChatSessionSharingRequest(RequestBase, IReturn[IdResponse]):
    """
    Marks or unmarks an AI chat session as "do not share".
    """

    session_id: Optional[str] = None
    do_not_share: bool = False


# @Route("/{version}/account/chat/sessions", "GET")
# @Api(Description="Lists the account's recent AI chat sessions.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetChatSessionsRequest(RequestBase, IReturn[GetChatSessionsResponse]):
    """
    Lists the account's recent AI chat sessions.
    """

    take: Optional[int] = None
    include_archived: Optional[bool] = None


# @Route("/{version}/account/chat/sessions/{SessionId}/entries", "GET")
# @Api(Description="Returns one AI chat session's conversation entries — the transcript.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetChatSessionEntriesRequest(RequestBase, IReturn[GetChatSessionEntriesResponse]):
    """
    Returns one AI chat session's conversation entries — the transcript.
    """

    session_id: Optional[str] = None
    since_seq: Optional[int] = None


# @Route("/{version}/account/chat/sessions/{SessionId}/entries/{EntryId}/feedback", "POST")
# @Api(Description="Records like / dislike feedback on one AI chat entry, or clears it.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SetChatEntryFeedbackRequest(RequestBase, IReturn[IdResponse]):
    """
    Records like / dislike feedback on one AI chat entry, or clears it.
    """

    session_id: Optional[str] = None
    entry_id: Optional[str] = None
    feedback: Optional[str] = None


# @Route("/{version}/account/chat/sessions/{SessionId}/questions/{EntryId}/answer", "POST")
# @Api(Description="Answers one open AI chat question — or a prepared change's Apply / Skip — and continues the conversation.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AnswerChatQuestionRequest(RequestBase, IReturn[IdResponse]):
    """
    Answers one open AI chat question — or a prepared change's Apply / Skip — and continues the conversation.
    """

    session_id: Optional[str] = None
    entry_id: Optional[str] = None
    answers: Optional[Dict[str, str]] = None


# @Route("/{version}/account/chat/sessions/{SessionId}/plans/{EntryId}/decision", "POST")
# @Api(Description="Approves or rejects a proposed AI chat plan.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DecideChatPlanRequest(RequestBase, IReturn[IdResponse]):
    """
    Approves or rejects a proposed AI chat plan.
    """

    session_id: Optional[str] = None
    entry_id: Optional[str] = None
    decision: Optional[str] = None
    comment: Optional[str] = None


# @Route("/{version}/account/chat/sessions/{SessionId}/steps/{EntryId}/stop", "POST")
# @Api(Description="Stops one running step of an AI chat plan run.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class StopChatRunStepRequest(RequestBase, IReturn[IdResponse]):
    """
    Stops one running step of an AI chat plan run.
    """

    session_id: Optional[str] = None
    entry_id: Optional[str] = None


# @Route("/{version}/account/chat/turn", "POST")
# @Api(Description="Runs one AI chat conversation turn.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ChatTurnRequest(RequestBase, IReturn[ChatTurnResponse]):
    """
    Runs one AI chat conversation turn.
    """

    session_id: Optional[str] = None
    message: Optional[str] = None
    profile: Optional[str] = None
    topic: Optional[str] = None
    llm_integration_id: Optional[str] = None
    model: Optional[str] = None
    project_id: Optional[str] = None
    env: Optional[str] = None
    screen_context: Optional[ChatScreenContextDto] = None


# @Route("/{version}/account/mcp", "POST")
# @Api(Description="MCP server endpoint — JSON-RPC 2.0 over HTTP POST exposing the AI tool catalog.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpRequest(IReturn[str]):
    """
    MCP server endpoint — JSON-RPC 2.0 over HTTP POST exposing the AI tool catalog.
    """

    version: Optional[str] = None
    request_stream: Optional[bytes] = None


# @Route("/{version}/projects/{projectId}/ai/brief", "GET")
# @Api(Description="Reads a project's AI Brief: the requirements, decisions and assumptions the assistant recorded from conversations, each with the chat turn, user and time it came from.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetProjectBriefRequest(CodeMashRequestBase, IReturn[GetProjectBriefResponse]):
    """
    Reads a project's AI Brief: the requirements, decisions and assumptions the assistant recorded from conversations, each with the chat turn, user and time it came from.
    """

    # @ApiMember(Description="Return the Brief events after this sequence number as well (0 = all). Omit for the snapshot only.")
    since_seq: Optional[int] = None
    """
    Return the Brief events after this sequence number as well (0 = all). Omit for the snapshot only.
    """


# @Route("/{version}/projects/{projectId}/ai/work-items", "GET")
# @Api(Description="Lists a project's AI work items: one serious ask each, with its goal, plans, changes, moved-out items, needs-you list and open questions.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetWorkItemsRequest(CodeMashRequestBase, IReturn[GetWorkItemsResponse]):
    """
    Lists a project's AI work items: one serious ask each, with its goal, plans, changes, moved-out items, needs-you list and open questions.
    """

    # @ApiMember(Description="Filter by status: proposed, active, waiting, done, partly-done or dropped. Omit for all.")
    status: Optional[str] = None
    """
    Filter by status: proposed, active, waiting, done, partly-done or dropped. Omit for all.
    """


# @Route("/{version}/projects/{projectId}/ai/work-items/{WorkItemId}", "GET")
# @Api(Description="Reads one AI work item: the six long-task sections and the definition-of-done verdict.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetWorkItemRequest(CodeMashRequestBase, IReturn[GetWorkItemResponse]):
    """
    Reads one AI work item: the six long-task sections and the definition-of-done verdict.
    """

    work_item_id: Optional[str] = None


# @Route("/{version}/projects/{projectId}/ai/work-items/{WorkItemId}/export.md", "GET")
# @Api(Description="Exports one AI work item as markdown in the long-task shape: Goal, Plan, Changes, Rejected / moved out, Needs you, Open questions.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ExportWorkItemRequest(CodeMashRequestBase, IReturn[ExportWorkItemResponse]):
    """
    Exports one AI work item as markdown in the long-task shape: Goal, Plan, Changes, Rejected / moved out, Needs you, Open questions.
    """

    work_item_id: Optional[str] = None


# @Route("/{version}/projects/{projectId}/ai/work-items/{WorkItemId}/needs-you/{Index}/done", "POST")
# @Api(Description="Ticks one manual line of a work item's \"Needs you\" checklist — the one write a human makes to a work item directly.")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MarkNeedsYouDoneRequest(CodeMashRequestBase, IReturn[IdResponse]):
    """
    Ticks one manual line of a work item's "Needs you" checklist — the one write a human makes to a work item directly.
    """

    work_item_id: Optional[str] = None
    index: int = 0
    # @ApiMember(Description="Set false to un-tick the line. Default true.")
    done: Optional[bool] = None
    """
    Set false to un-tick the line. Default true.
    """


# @Route("/{version}/ai/integrations/llms/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteLlmIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Id of the LLM integration to delete.")
    id: Optional[str] = None
    """
    Id of the LLM integration to delete.
    """


# @Route("/{version}/ai/integrations/llms/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableLlmIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Id of the LLM integration to disable.")
    id: Optional[str] = None
    """
    Id of the LLM integration to disable.
    """


# @Route("/{version}/ai/integrations/llms/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableLlmIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Id of the LLM integration to enable.")
    id: Optional[str] = None
    """
    Id of the LLM integration to enable.
    """


# @Route("/{version}/ai/integrations/llms/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLlmIntegration(CodeMashRequestBase, IReturn[GetLlmIntegrationResponse]):
    # @ApiMember(Description="Id of the LLM integration to fetch.")
    id: Optional[str] = None
    """
    Id of the LLM integration to fetch.
    """


# @Route("/{version}/ai/integrations/llms/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLlmIntegrations(CodeMashListPaginationRequestBase, IReturn[GetLlmIntegrationsResponse]):
    pass


# @Route("/{version}/ai/integrations/llms/", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveLlmIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    integration: Optional[LlmIntegrationRequest] = None


# @Route("/{version}/ai/integrations/llms/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestLlmIntegration(CodeMashRequestBase, IReturn[TestLlmIntegrationResponse]):
    # @ApiMember(Description="Id of the LLM integration to test.")
    integration_id: Optional[str] = None
    """
    Id of the LLM integration to test.
    """


# @Route("/{version}/ai/integrations/mcp/{Id}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteMcpIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Id of the MCP integration to delete.")
    id: Optional[str] = None
    """
    Id of the MCP integration to delete.
    """


# @Route("/{version}/ai/integrations/mcp/{Id}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableMcpIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Id of the MCP integration to disable.")
    id: Optional[str] = None
    """
    Id of the MCP integration to disable.
    """


# @Route("/{version}/ai/integrations/mcp/{Id}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableMcpIntegrationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="Id of the MCP integration to enable.")
    id: Optional[str] = None
    """
    Id of the MCP integration to enable.
    """


# @Route("/{version}/ai/integrations/mcp/{id}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMcpIntegration(CodeMashRequestBase, IReturn[GetMcpIntegrationResponse]):
    # @ApiMember(Description="Id of the MCP integration to fetch.")
    id: Optional[str] = None
    """
    Id of the MCP integration to fetch.
    """


# @Route("/{version}/ai/integrations/mcp/integrations", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetMcpIntegrations(CodeMashListPaginationRequestBase, IReturn[GetMcpIntegrationsResponse]):
    pass


# @Route("/{version}/ai/integrations/mcp/", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveMcpIntegration(CodeMashRequestBase, IReturn[IdResponse]):
    integration: Optional[McpIntegrationRequest] = None


# @Route("/{version}/ai/integrations/mcp/test", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class TestMcpIntegration(CodeMashRequestBase, IReturn[TestLlmIntegrationResponse]):
    # @ApiMember(Description="Id of the MCP integration to test.")
    integration_id: Optional[str] = None
    """
    Id of the MCP integration to test.
    """


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationSaved:
    llm_integration: Optional[LlmIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationSecretsConfigured:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationSecretsConfigurationFailed:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class LlmIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationSaved:
    mcp_integration: Optional[McpIntegration] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationDeleted:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationEnabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationDisabled:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationSecretsConfigured:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationSecretsConfigurationFailed:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class McpIntegrationTested:
    id: Optional[IntegrationId] = None
    succeeded: bool = False
    error_messages: Optional[IReadOnlyList[str]] = None
    tested_at_utc: datetime.datetime = datetime.datetime(1, 1, 1)
    env: Optional[Env] = None


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
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegrationSecretsConfigurationFailed:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class WebhookIntegrationSecretsCleared:
    id: Optional[IntegrationId] = None
    env: Optional[Env] = None


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
# @Api(Description="Gets the project's webhook integration")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetWebhookIntegration(CodeMashRequestBase, IReturn[GetWebhookIntegrationResponse]):
    """
    Gets the project's webhook integration
    """

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
    # @ApiMember(Description="The integration-wide static headers to send with every delivery. Pass an empty dictionary to clear all extra headers.")
    extra_headers: Optional[Dict[str, str]] = None
    """
    The integration-wide static headers to send with every delivery. Pass an empty dictionary to clear all extra headers.
    """


# @Route("/{version}/webhooks/{source}/{integrationInstanceId}", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReceiveWebhook(IReturn[HttpResult]):
    source: Optional[str] = None
    integration_instance_id: Optional[str] = None
    request_stream: Optional[bytes] = None


# @Route("/{version}/webhooks/destinations/{DestinationId}/disable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DisableWebhookDestinationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="The webhook destination id to disable, from get_webhook_integration.", IsRequired=true)
    destination_id: Optional[str] = None
    """
    The webhook destination id to disable, from get_webhook_integration.
    """


# @Route("/{version}/webhooks/destinations/{DestinationId}/enable", "PUT")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class EnableWebhookDestinationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="The webhook destination id to enable, from get_webhook_integration.", IsRequired=true)
    destination_id: Optional[str] = None
    """
    The webhook destination id to enable, from get_webhook_integration.
    """


# @Route("/{version}/webhooks/destinations/{DestinationId}", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveWebhookDestinationRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    # @ApiMember(Description="The webhook destination id to remove, from get_webhook_integration.", IsRequired=true)
    destination_id: Optional[str] = None
    """
    The webhook destination id to remove, from get_webhook_integration.
    """


# @Route("/{version}/webhooks/destinations", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveWebhookDestinationRequest(CodeMashRequestBase, IReturn[SaveWebhookDestinationResponse]):
    # @ApiMember(Description="Existing destination id to overwrite, from get_webhook_integration. Omit to create a new destination.")
    destination_id: Optional[str] = None
    """
    Existing destination id to overwrite, from get_webhook_integration. Omit to create a new destination.
    """


    # @ApiMember(Description="Display name for the destination.", IsRequired=true)
    destination_name: Optional[str] = None
    """
    Display name for the destination.
    """


    # @ApiMember(Description="The HTTPS endpoint URL that will receive the webhook deliveries.", IsRequired=true)
    endpoint_url: Optional[str] = None
    """
    The HTTPS endpoint URL that will receive the webhook deliveries.
    """


    # @ApiMember(Description="The event names this destination subscribes to. Empty subscribes to none.")
    selected_events: List[str] = field(default_factory=list)
    """
    The event names this destination subscribes to. Empty subscribes to none.
    """


    # @ApiMember(Description="Destination-specific static headers sent with every delivery to this destination. These win over the integration-wide extra headers on duplicate keys.")
    extra_headers: Optional[Dict[str, str]] = None
    """
    Destination-specific static headers sent with every delivery to this destination. These win over the integration-wide extra headers on duplicate keys.
    """


    # @ApiMember(Description="Whether this destination is enabled for delivery. Defaults to true.")
    is_enabled: bool = False
    """
    Whether this destination is enabled for delivery. Defaults to true.
    """


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
# @Api(Description="Gets a scheduled task by id")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchedulerTask(CodeMashRequestBase, IReturn[GetSchedulerTaskResponse]):
    """
    Gets a scheduled task by id
    """

    id: Optional[str] = None


# @Route("/{version}/scheduler/tasks", "GET")
# @Api(Description="Gets scheduled tasks")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSchedulerTasks(CodeMashListPaginationRequestBase, IReturn[GetSchedulerTasksResponse]):
    """
    Gets scheduled tasks
    """

    # @ApiMember(Description="Optional filter — only return tasks of this type.")
    type: Optional[SchedulerTaskType] = None
    """
    Optional filter — only return tasks of this type.
    """


    # @ApiMember(Description="Optional filter — only return tasks whose enabled state matches this value.")
    enabled: Optional[bool] = None
    """
    Optional filter — only return tasks whose enabled state matches this value.
    """


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


# @Route("/{version}/resources/resolve", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResolveResources(CodeMashRequestBase, IReturn[ResolveResourcesResponse]):
    refs: Optional[IReadOnlyList[ResourceRefDto]] = None


# @Route("/{version}/membership/users", "POST")
# @Api(Description="Create a contact")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CreateContactRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Create a contact
    """

    # @ApiMember(Description="Primary email address of the contact (optional if a phone is given).")
    primary_email: Optional[str] = None
    """
    Primary email address of the contact (optional if a phone is given).
    """


    # @ApiMember(Description="Primary phone number in international format, e.g. +14155550123 (optional if an email is given).")
    primary_phone: Optional[str] = None
    """
    Primary phone number in international format, e.g. +14155550123 (optional if an email is given).
    """


    # @ApiMember(Description="Display name shown in the dashboard (optional).")
    display_name: Optional[str] = None
    """
    Display name shown in the dashboard (optional).
    """


    # @ApiMember(Description="Contact's first name (optional).")
    first_name: Optional[str] = None
    """
    Contact's first name (optional).
    """


    # @ApiMember(Description="Contact's last name (optional).")
    last_name: Optional[str] = None
    """
    Contact's last name (optional).
    """


# @Route("/{version}/membership/users/{contactId}", "DELETE")
# @Api(Description="Archive a contact")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeleteContact(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Archive a contact
    """

    # @ApiMember(Description="The contact id (ct_…) to archive. Get it from get_all_contacts.", IsRequired=true)
    contact_id: Optional[str] = None
    """
    The contact id (ct_…) to archive. Get it from get_all_contacts.
    """


# @Route("/{version}/membership/users/{contactId}", "GET")
# @Api(Description="Get a contact")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetContact(CodeMashRequestBase, IReturn[GetContactResponse]):
    """
    Get a contact
    """

    # @ApiMember(Description="The contact id (ct_…) to fetch. Get it from get_all_contacts.", IsRequired=true)
    contact_id: Optional[str] = None
    """
    The contact id (ct_…) to fetch. Get it from get_all_contacts.
    """


# @Route("/{version}/membership/users", "GET")
# @Api(Description="List contacts")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAllContacts(CodeMashRequestBase, IReturn[GetAllContactsResponse]):
    """
    List contacts
    """

    # @ApiMember(Description="Cursor for the next page: pass the nextCursor from the previous call. Omit for the first page.")
    starting_after: Optional[str] = None
    """
    Cursor for the next page: pass the nextCursor from the previous call. Omit for the first page.
    """


    # @ApiMember(Description="How many contacts to return per page (default 50).")
    page_size: Optional[int] = None
    """
    How many contacts to return per page (default 50).
    """


# @Route("/{version}/membership/users/merge", "POST")
# @Api(Description="Merge contacts")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class MergeContactsRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Merge contacts
    """

    # @ApiMember(Description="The contact id (ct_…) that will remain after the merge (the survivor).", IsRequired=true)
    survivor_id: Optional[str] = None
    """
    The contact id (ct_…) that will remain after the merge (the survivor).
    """


    # @ApiMember(Description="The contact ids (ct_…) to merge into the survivor and archive. At least one.", IsRequired=true)
    merged_ids: List[str] = field(default_factory=list)
    """
    The contact ids (ct_…) to merge into the survivor and archive. At least one.
    """


# @Route("/{version}/membership/users/{contactId}", "PATCH")
# @Api(Description="Update a contact")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class UpdateContactRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Update a contact
    """

    # @ApiMember(Description="The contact id (ct_…) to update. Get it from get_all_contacts.", IsRequired=true)
    contact_id: Optional[str] = None
    """
    The contact id (ct_…) to update. Get it from get_all_contacts.
    """


    # @ApiMember(Description="Display name shown in the dashboard.")
    display_name: Optional[str] = None
    """
    Display name shown in the dashboard.
    """


    # @ApiMember(Description="First name.")
    first_name: Optional[str] = None
    """
    First name.
    """


    # @ApiMember(Description="Last name.")
    last_name: Optional[str] = None
    """
    Last name.
    """


    # @ApiMember(Description="Full name (overrides first/last when set).")
    full_name: Optional[str] = None
    """
    Full name (overrides first/last when set).
    """


    # @ApiMember(Description="Company or organisation name.")
    company: Optional[str] = None
    """
    Company or organisation name.
    """


    # @ApiMember(Description="Free-text internal notes about the contact.")
    notes: Optional[str] = None
    """
    Free-text internal notes about the contact.
    """


    # @ApiMember(Description="Gender: Male, Female or Other.")
    gender: Optional[str] = None
    """
    Gender: Male, Female or Other.
    """


    # @ApiMember(Description="Birth date as a unix timestamp in MILLISECONDS (UTC).")
    birth_date: Optional[int] = None
    """
    Birth date as a unix timestamp in MILLISECONDS (UTC).
    """


    # @ApiMember(Description="IANA time zone id, e.g. Europe/Vilnius.")
    time_zone: Optional[str] = None
    """
    IANA time zone id, e.g. Europe/Vilnius.
    """


    # @ApiMember(Description="Preferred language/locale code, e.g. en or en-US.")
    language: Optional[str] = None
    """
    Preferred language/locale code, e.g. en or en-US.
    """


    # @ApiMember(Description="Address line 1 (street).")
    address_line1: Optional[str] = None
    """
    Address line 1 (street).
    """


    # @ApiMember(Description="Address line 2 (apartment, suite, etc.).")
    address_line2: Optional[str] = None
    """
    Address line 2 (apartment, suite, etc.).
    """


    # @ApiMember(Description="Country name or code.")
    country: Optional[str] = None
    """
    Country name or code.
    """


    # @ApiMember(Description="City.")
    city: Optional[str] = None
    """
    City.
    """


    # @ApiMember(Description="State, region or province.")
    state: Optional[str] = None
    """
    State, region or province.
    """


    # @ApiMember(Description="Postal or ZIP code.")
    postal_code: Optional[str] = None
    """
    Postal or ZIP code.
    """


# @Route("/{version}/membership/users/{contactId}/identities", "POST")
# @Api(Description="Link a login to a contact")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AddContactIdentityRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Link a login to a contact
    """

    # @ApiMember(Description="The contact id (ct_…) to link the login to.", IsRequired=true)
    contact_id: Optional[str] = None
    """
    The contact id (ct_…) to link the login to.
    """


    # @ApiMember(Description="The login (identity) id (usr_…) to link to the contact.", IsRequired=true)
    auth_id: Optional[str] = None
    """
    The login (identity) id (usr_…) to link to the contact.
    """


# @Route("/{version}/membership/users/{contactId}/identities/{authId}/promote", "POST")
# @Api(Description="Make a login the contact's primary")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PromoteContactIdentityRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Make a login the contact's primary
    """

    # @ApiMember(Description="The contact id (ct_…) whose login is being promoted.", IsRequired=true)
    contact_id: Optional[str] = None
    """
    The contact id (ct_…) whose login is being promoted.
    """


    # @ApiMember(Description="The linked login (identity) id (usr_…) to make primary.", IsRequired=true)
    auth_id: Optional[str] = None
    """
    The linked login (identity) id (usr_…) to make primary.
    """


# @Route("/{version}/membership/users/{contactId}/identities/{authId}", "DELETE")
# @Api(Description="Unlink a login from a contact")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveContactIdentityRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    """
    Unlink a login from a contact
    """

    # @ApiMember(Description="The contact id (ct_…) to unlink the login from.", IsRequired=true)
    contact_id: Optional[str] = None
    """
    The contact id (ct_…) to unlink the login from.
    """


    # @ApiMember(Description="The login (identity) id (usr_…) to unlink from the contact.", IsRequired=true)
    auth_id: Optional[str] = None
    """
    The login (identity) id (usr_…) to unlink from the contact.
    """


# @Route("/{version}/compliance/settings", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetComplianceSettings(CodeMashRequestBase, IReturn[GetComplianceSettingsResponse]):
    pass


# @Route("/{version}/compliance/retention", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RemoveRetentionWindowRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    data_kind: Optional[str] = None


# @Route("/{version}/compliance/retention", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveRetentionWindowRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    data_kind: Optional[str] = None
    days: int = 0
    action: Optional[str] = None


# @Route("/{version}/compliance/regimes", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AssignRegimeRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    regime: Optional[str] = None


# @Route("/{version}/compliance/regimes", "DELETE")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ClearRegimeRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    regime: Optional[str] = None


# @Route("/{version}/compliance/purposes", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DefineConsentPurposeRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    key: Optional[str] = None
    name: Optional[str] = None
    channel: Optional[str] = None
    mapped_tags: List[str] = field(default_factory=list)
    regulatory_basis: List[str] = field(default_factory=list)
    description: Optional[str] = None


# @Route("/{version}/compliance/purposes/deprecate", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class DeprecateConsentPurposeRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    key: Optional[str] = None


# @Route("/{version}/compliance/holds", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetLegalHolds(CodeMashRequestBase, IReturn[GetLegalHoldsResponse]):
    pass


# @Route("/{version}/compliance/holds", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class PlaceLegalHoldRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    subject_kind: Optional[str] = None
    subject_id: Optional[str] = None
    reason: Optional[str] = None


# @Route("/{version}/compliance/holds/release", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReleaseLegalHoldRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    hold_id: Optional[str] = None


# @Route("/{version}/compliance/dsar/approve", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ApproveDsarRequestRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    request_id: Optional[str] = None


# @Route("/{version}/compliance/dsar/reject", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RejectDsarRequestRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    request_id: Optional[str] = None
    reason: Optional[str] = None


# @Route("/{version}/compliance/dsar", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDsarRequests(CodeMashRequestBase, IReturn[GetDsarRequestsResponse]):
    pass


# @Route("/{version}/compliance/dsar", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenDsarRequestRequest(CodeMashRequestBase, IReturn[EmptyResponse]):
    subject_kind: Optional[str] = None
    subject_id: Optional[str] = None


# @Route("/{version}/compliance/audit", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetComplianceAuditLog(CodeMashRequestBase, IReturn[GetComplianceAuditLogResponse]):
    from_: Optional[datetime.datetime] = field(metadata=config(field_name='from'), default=None)
    to: Optional[datetime.datetime] = None
    subject_kind: Optional[str] = None
    subject_id: Optional[str] = None
    limit: int = 0


# @Route("/{version}/compliance/account", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetAccountCompliance(RequestBase, IReturn[GetAccountComplianceResponse]):
    pass


# @Route("/{version}/compliance/account/dsar-policy", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveDsarPolicyRequest(RequestBase, IReturn[EmptyResponse]):
    mode: Optional[str] = None
    delay_days: int = 0


# @Route("/{version}/compliance/account/incident-routing", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SaveIncidentRoutingRequest(RequestBase, IReturn[EmptyResponse]):
    auto_forward_advisories: bool = False
    security_contact: Optional[str] = None


# @Route("/{version}/support/cases/{CaseId}/close", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class CloseSupportCaseRequest(RequestBase, IReturn[EmptyResponse]):
    case_id: Optional[str] = None


# @Route("/{version}/support/cases/{CaseId}/reopen", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReopenSupportCaseRequest(RequestBase, IReturn[EmptyResponse]):
    case_id: Optional[str] = None
    reason: Optional[str] = None


# @Route("/{version}/support/cases/{CaseId}/resolve", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ResolveSupportCaseRequest(RequestBase, IReturn[EmptyResponse]):
    case_id: Optional[str] = None
    resolution: Optional[CaseResolutionDto] = None


# @Route("/{version}/support/cases/{CaseId}/messages", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class AppendSupportCaseMessageRequest(RequestBase, IReturn[IdResponse]):
    case_id: Optional[str] = None
    message: Optional[str] = None


# @Route("/{version}/support/cases/{CaseId}", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSupportCase(RequestBase, IReturn[GetSupportCaseResponse]):
    case_id: Optional[str] = None


# @Route("/{version}/support/cases", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetSupportCases(RequestBase, IReturn[GetSupportCasesResponse]):
    paging_args: Optional[PagingArgs] = None


# @Route("/{version}/support/cases", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class OpenSupportCaseRequest(RequestBase, IReturn[IdResponse]):
    kind: Optional[str] = None
    severity: Optional[str] = None
    subject: Optional[str] = None
    message: Optional[str] = None
    project_id: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseOpened:
    case_id: Optional[SupportCaseId] = None
    account_id: Optional[AccountId] = None
    project_id: Optional[ProjectId] = None
    reporter_id: Optional[str] = None
    kind: Optional[SupportCaseKind] = None
    severity: Optional[SupportCaseSeverity] = None
    subject: Optional[str] = None
    deployment_mode: Optional[DeploymentMode] = None
    gateway_version: Optional[str] = None
    region: Optional[str] = None
    plan_tier: Optional[str] = None
    opened_on: Optional[UtcDateTime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseTriaged:
    case_id: Optional[SupportCaseId] = None
    kind: Optional[SupportCaseKind] = None
    severity: Optional[SupportCaseSeverity] = None
    affected_module: Optional[str] = None
    triaged_by: Optional[str] = None
    triaged_on: Optional[UtcDateTime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseMessageAppended:
    case_id: Optional[SupportCaseId] = None
    message: Optional[SupportMessageRef] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseStatusChanged:
    case_id: Optional[SupportCaseId] = None
    from_: Optional[SupportCaseStatus] = field(metadata=config(field_name='from'), default=None)
    to: Optional[SupportCaseStatus] = None
    changed_on: Optional[UtcDateTime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseResolved:
    case_id: Optional[SupportCaseId] = None
    resolution: Optional[CaseResolution] = None
    resolved_on: Optional[UtcDateTime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseClosed:
    case_id: Optional[SupportCaseId] = None
    closed_by: Optional[str] = None
    closed_on: Optional[UtcDateTime] = None
    reason: Optional[SupportCaseCloseReason] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseReopened:
    case_id: Optional[SupportCaseId] = None
    reason: Optional[str] = None
    reopened_on: Optional[UtcDateTime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseWaitingReminderSent:
    case_id: Optional[SupportCaseId] = None
    tier_days: int = 0
    sent_on: Optional[UtcDateTime] = None


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class SupportCaseAttachmentLinked:
    case_id: Optional[SupportCaseId] = None
    attachment_ref: Optional[str] = None
    file_name: Optional[str] = None
    linked_on: Optional[UtcDateTime] = None


# @Route("/{version}/diagnostics/packs", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDiagnosticPacks(CodeMashRequestBase, IReturn[GetDiagnosticPacksResponse]):
    pass


# @Route("/{version}/diagnostics/packs/{PackName}/run", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RunDiagnosticPackRequest(CodeMashRequestBase, IReturn[RunDiagnosticPackResponse]):
    pack_name: Optional[str] = None
    pack_version: Optional[int] = None
    case_id: Optional[str] = None


# @Route("/{version}/diagnostics/echo", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class GetDiagnosticEcho(CodeMashRequestBase, IReturn[GetDiagnosticEchoResponse]):
    case_id: Optional[str] = None


# @Route("/{version}/diagnostics/events", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class ReadDiagnosticEventsRequest(CodeMashRequestBase, IReturn[ReadDiagnosticEventsResponse]):
    stream: Optional[str] = None
    from_: int = field(metadata=config(field_name='from'), default=0)
    count: int = 0
    case_id: Optional[str] = None


# @Route("/{version}/diagnostics/logs", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class QueryDiagnosticLogsRequest(CodeMashListPaginationRequestBase, IReturn[QueryDiagnosticLogsResponse]):
    level: Optional[str] = None
    module: Optional[str] = None
    log_correlation_id: Optional[str] = None
    event_code: Optional[str] = None
    search: Optional[str] = None
    from_utc: Optional[datetime.datetime] = None
    to_utc: Optional[datetime.datetime] = None
    case_id: Optional[str] = None


# @Route("/{version}/diagnostics/redis", "GET")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class InspectDiagnosticRedisRequest(CodeMashRequestBase, IReturn[InspectDiagnosticRedisResponse]):
    key_pattern: Optional[str] = None
    case_id: Optional[str] = None


# @Route("/{version}/diagnostics/health/{CheckId}", "POST")
@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
@dataclass
class RunDiagnosticHealthCheckRequest(CodeMashRequestBase, IReturn[RunDiagnosticHealthCheckResponse]):
    check_id: Optional[str] = None
    case_id: Optional[str] = None

