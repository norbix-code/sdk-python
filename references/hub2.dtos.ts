/* Options:
Date: 2026-04-27 18:40:11
Version: 10.06
Tip: To override a DTO option, remove "//" prefix before updating
BaseUrl: http://localhost:5001

GlobalNamespace: CodeMashHub2
//MakePropertiesOptional: False
//AddServiceStackTypes: True
//AddResponseStatus: False
//AddImplicitVersion: 
//AddDescriptionAsComments: True
//IncludeTypes: 
//ExcludeTypes: 
//DefaultImports: 
*/


export module CodeMashHub2
{
    // @ts-nocheck

    export interface IReturn<T>
    {
        createResponse(): T;
    }

    export interface IReturnVoid
    {
        createResponse(): void;
    }

    export interface IHasSessionId
    {
        sessionId?: string;
    }

    export interface IHasBearerToken
    {
        bearerToken?: string;
    }

    export interface IPost
    {
    }

    export interface IGet
    {
    }

    export type IReadOnlySet<T> = ReadonlyArray<T>;
    export type IReadOnlyList<T> = ReadonlyArray<T>;
    export type IList<T> = T[];
    export type HashSet<T> = T[];
    export type IReadOnlyDictionary<TKey extends string | number | symbol, TValue> = Record<TKey, TValue>;

    // @DataContract
    export enum EmailProvider
    {
        Smtp = 'Smtp',
        SendGrid = 'SendGrid',
        MailGun = 'MailGun',
        AwsSes = 'AwsSes',
    }

    export class EmailIntegrationRequest
    {
        public integrationId?: string;
        public provider: EmailProvider;
        public integrationName: string;
        public isEnabled: boolean;
        public emailAddress: string;
        public emailSenderName?: string;

        public constructor(init?: Partial<EmailIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export enum SmtpPorts
    {
        Default = 25,
        Ssl = 465,
        Tls = 587,
        Fallback = 2525,
    }

    export class SmtpEmailIntegrationRequest extends EmailIntegrationRequest
    {
        public domain: string;
        public port: SmtpPorts;
        public userName: string;
        public password: string;

        public constructor(init?: Partial<SmtpEmailIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum AwsIntegrationType
    {
        Iam = 'Iam',
        CrossAccountRole = 'CrossAccountRole',
    }

    export class AwsSesEmailIntegrationRequest extends EmailIntegrationRequest
    {
        public integrationType: AwsIntegrationType;
        public awsRegion: string;
        public emailIdentityArn: string;
        public configurationSet?: string;
        public roleArn?: string;
        public externalId?: string;
        public accessKey?: string;
        public secretKey?: string;

        public constructor(init?: Partial<AwsSesEmailIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class SendGridEmailIntegrationRequest extends EmailIntegrationRequest
    {
        public apiKey: string;

        public constructor(init?: Partial<SendGridEmailIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MailGunEmailIntegrationRequest extends EmailIntegrationRequest
    {
        public domain: string;
        public apiKey: string;
        public webhookSigningKey: string;

        public constructor(init?: Partial<MailGunEmailIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum EmailCampaignRecipientsSourceTypes
    {
        AllUsers = 'AllUsers',
        SpecifiedUsers = 'SpecifiedUsers',
        AccountUsers = 'AccountUsers',
        Email = 'Email',
        Collection = 'Collection',
    }

    export enum TokenMappingResolverType
    {
        NotSet = 'NotSet',
        Custom = 'Custom',
        Project = 'Project',
        ProjectSocials = 'ProjectSocials',
        Initiator = 'Initiator',
        Recipient = 'Recipient',
        SchemaRecord = 'SchemaRecord',
        TargetUser = 'TargetUser',
        TagDefinitions = 'TagDefinitions',
        EmailSignatures = 'EmailSignatures',
        Campaign = 'Campaign',
        Template = 'Template',
        EmailFooters = 'EmailFooters',
        Old = 'Old',
        New = 'New',
    }

    // @DataContract
    export class TokenMappingDto
    {
        // @DataMember
        public key: string;

        // @DataMember
        public value: string;

        // @DataMember
        public resolver: TokenMappingResolverType;

        public constructor(init?: Partial<TokenMappingDto>) { (Object as any).assign(this, init); }
    }

    export class EmailCampaignRequest
    {
        public source: EmailCampaignRecipientsSourceTypes;
        public templateId: string;
        public integrationId?: string;
        public language?: string;
        public initiatorId?: string;
        public notes?: string;
        // @DataMember
        public mappedTokens?: TokenMappingDto[];

        // @DataMember
        public campaignTime?: number;

        public constructor(init?: Partial<EmailCampaignRequest>) { (Object as any).assign(this, init); }
    }

    export class EmailToAllUsersDeliverySettingsRequest extends EmailCampaignRequest
    {
        public rolesNames?: string[];
        public userTags?: string[];

        public constructor(init?: Partial<EmailToAllUsersDeliverySettingsRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class EmailToAccountUsersDeliverySettingsRequest extends EmailCampaignRequest
    {
        public userRecipients: string[] = [];
        public userCc?: string[];
        public userBcc?: string[];
        public singleEmailStrategy: boolean;

        public constructor(init?: Partial<EmailToAccountUsersDeliverySettingsRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum CollectionEmailCampaignRecipientField
    {
        User = 'User',
        Email = 'Email',
    }

    export class EmailToCollectionRecordsDeliverySettingsRequest extends EmailCampaignRequest
    {
        public fields: string[] = [];
        public schemaName: string;
        public fieldType: CollectionEmailCampaignRecipientField;
        public roleNames?: string[];
        public languages?: string[];

        public constructor(init?: Partial<EmailToCollectionRecordsDeliverySettingsRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class EmailToEmailsDeliverySettingsRequest extends EmailCampaignRequest
    {
        public recipients: string[] = [];
        public recipientsCc?: string[];
        public recipientsBcc?: string[];
        public singleEmailStrategy: boolean;

        public constructor(init?: Partial<EmailToEmailsDeliverySettingsRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class EmailToUsersDeliverySettingsRequest extends EmailCampaignRequest
    {
        public userRecipients: string[] = [];
        public userCc?: string[];
        public userBcc?: string[];
        public singleEmailStrategy: boolean;

        public constructor(init?: Partial<EmailToUsersDeliverySettingsRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum TriggerType
    {
        Membership = 'Membership',
        Schema = 'Schema',
        Files = 'Files',
        Payments = 'Payments',
    }

    export enum TriggerActionType
    {
        Code = 'Code',
        Push = 'Push',
        Sms = 'Sms',
        Email = 'Email',
        WebhookCall = 'WebhookCall',
    }

    // @DataContract
    export class TriggerActionDto
    {
        // @DataMember
        public type: TriggerActionType;

        // @DataMember
        public integrationId?: string;

        public constructor(init?: Partial<TriggerActionDto>) { (Object as any).assign(this, init); }
    }

    export class SaveTriggerRequest
    {
        public type: TriggerType;
        public triggerId?: string;
        public name: string;
        public description?: string;
        public isEnabled: boolean;
        public preExecuteCode?: string;
        public action: TriggerActionDto;

        public constructor(init?: Partial<SaveTriggerRequest>) { (Object as any).assign(this, init); }
    }

    export enum MembershipTriggerType
    {
        OnRegistered = 'OnRegistered',
        OnInvited = 'OnInvited',
        OnVerified = 'OnVerified',
        OnUpdated = 'OnUpdated',
        OnDeleted = 'OnDeleted',
        OnBlocked = 'OnBlocked',
        OnReactivated = 'OnReactivated',
    }

    export class MembershipTriggerRequest extends SaveTriggerRequest
    {
        public when: MembershipTriggerType;

        public constructor(init?: Partial<MembershipTriggerRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum SchemaTriggerType
    {
        OnInserted = 'OnInserted',
        OnDeleted = 'OnDeleted',
        OnUpdated = 'OnUpdated',
    }

    export class SchemaTriggerRequest extends SaveTriggerRequest
    {
        public schemaId: string;
        public when: SchemaTriggerType;
        public configurationCode?: string;

        public constructor(init?: Partial<SchemaTriggerRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum FilesTriggerType
    {
        OnFileUploaded = 'OnFileUploaded',
        OnFileDeleted = 'OnFileDeleted',
    }

    // @DataContract
    export class FileChecksumDto
    {
        // @DataMember(Order=1)
        public algorithm: string;

        // @DataMember(Order=2)
        public hash: string;

        public constructor(init?: Partial<FileChecksumDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class FileResourceDto
    {
        // @DataMember(Order=1)
        public id: string;

        // @DataMember(Order=2)
        public originalFileName: string;

        // @DataMember(Order=3)
        public extension: string;

        // @DataMember(Order=4)
        public storedFileName: string;

        // @DataMember(Order=5)
        public sizeBytes?: number;

        // @DataMember(Order=6)
        public checksum?: FileChecksumDto;

        public constructor(init?: Partial<FileResourceDto>) { (Object as any).assign(this, init); }
    }

    export enum FileProvider
    {
        Local = 'Local',
        AwsS3 = 'AwsS3',
        AzureBlobStorage = 'AzureBlobStorage',
        GoogleCloudStorage = 'GoogleCloudStorage',
        Ftp = 'Ftp',
        AppleICloud = 'AppleICloud',
        DropBox = 'DropBox',
        GoogleDrive = 'GoogleDrive',
    }

    // @DataContract
    export class FileResourceRefDto
    {
        // @DataMember(Order=1)
        public resource: FileResourceDto;

        // @DataMember(Order=2)
        public integrationId: string;

        // @DataMember(Order=3)
        public provider: FileProvider;

        // @DataMember(Order=4)
        public path: string;

        public constructor(init?: Partial<FileResourceRefDto>) { (Object as any).assign(this, init); }
    }

    export class FilesTriggerRequest extends SaveTriggerRequest
    {
        public when: FilesTriggerType;
        public fileRef: FileResourceRefDto;

        public constructor(init?: Partial<FilesTriggerRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum PaymentTriggerType
    {
        OnOrderCreated = 'OnOrderCreated',
        OnOrderPaid = 'OnOrderPaid',
        OnWebhookCallReceived = 'OnWebhookCallReceived',
    }

    export class PaymentTriggerRequest extends SaveTriggerRequest
    {
        public when: PaymentTriggerType;

        public constructor(init?: Partial<PaymentTriggerRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum DatabaseProvider
    {
        CodeMashMongoDbAtlasCluster = 'CodeMashMongoDbAtlasCluster',
        CodeMashMongoDbAtlasServerless = 'CodeMashMongoDbAtlasServerless',
        MongoDbConnectionString = 'MongoDbConnectionString',
    }

    export class DatabaseIntegrationRequest
    {
        public integrationId?: string;
        public provider: DatabaseProvider;
        public integrationName: string;
        public isEnabled: boolean;

        public constructor(init?: Partial<DatabaseIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export class MongoDbAtlasServerlessDatabaseIntegrationRequest extends DatabaseIntegrationRequest
    {
        public databaseName?: string;
        public connectionString: string;

        public constructor(init?: Partial<MongoDbAtlasServerlessDatabaseIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbAtlasClusterDatabaseIntegrationRequest extends DatabaseIntegrationRequest
    {
        public databaseName?: string;
        public connectionString: string;

        public constructor(init?: Partial<MongoDbAtlasClusterDatabaseIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbConnectionStringDatabaseIntegrationRequest extends DatabaseIntegrationRequest
    {
        public databaseName?: string;
        public connectionString: string;

        public constructor(init?: Partial<MongoDbConnectionStringDatabaseIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class FilesIntegrationRequest
    {
        public integrationId?: string;
        public provider: FileProvider;
        public integrationName: string;
        public isEnabled: boolean;

        public constructor(init?: Partial<FilesIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export class GoogleDriveFilesIntegrationRequest extends FilesIntegrationRequest
    {
        public rootFolderId?: string;
        public serviceAccountJsonKey: string;

        public constructor(init?: Partial<GoogleDriveFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class FtpFilesIntegrationRequest extends FilesIntegrationRequest
    {
        public host: string;
        public port: number;
        public rootPath?: string;
        public useSsl: boolean;
        public username: string;
        public password: string;

        public constructor(init?: Partial<FtpFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class DropBoxFilesIntegrationRequest extends FilesIntegrationRequest
    {
        public rootPath?: string;
        public accessToken: string;

        public constructor(init?: Partial<DropBoxFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AppleICloudFilesIntegrationRequest extends FilesIntegrationRequest
    {
        public containerIdentifier: string;
        public relativePath?: string;
        public keyId: string;
        public teamId: string;
        public bundleId: string;
        public p8PrivateKey: string;

        public constructor(init?: Partial<AppleICloudFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum AwsS3IntegrationType
    {
        Iam = 'Iam',
        CrossAccountRole = 'CrossAccountRole',
    }

    export class AwsS3FilesIntegrationRequest extends FilesIntegrationRequest
    {
        public integrationType: AwsS3IntegrationType;
        public bucketName: string;
        public region: string;
        public roleArn?: string;
        public externalId?: string;
        public accessKey?: string;
        public secretKey?: string;

        public constructor(init?: Partial<AwsS3FilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleCloudFilesIntegrationRequest extends FilesIntegrationRequest
    {
        public bucketName: string;
        public serviceAccountJsonKey: string;

        public constructor(init?: Partial<GoogleCloudFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AzureBlobFilesIntegrationRequest extends FilesIntegrationRequest
    {
        public blobName: string;
        public connectionString: string;

        public constructor(init?: Partial<AzureBlobFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class LocalFilesIntegrationRequest extends FilesIntegrationRequest
    {
        public rootPath?: string;

        public constructor(init?: Partial<LocalFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum LoggingProvider
    {
        Console = 'Console',
        DataDog = 'DataDog',
        Kafka = 'Kafka',
        Zabbix = 'Zabbix',
        MicrosoftTeams = 'MicrosoftTeams',
        Slack = 'Slack',
        Telegram = 'Telegram',
        AMQP = 'AMQP',
        NewRelic = 'NewRelic',
        Prometheus = 'Prometheus',
        AzureOTel = 'AzureOTel',
        Splunk = 'Splunk',
        ElasticSearch = 'ElasticSearch',
        Kibana = 'Kibana',
        LocalFile = 'LocalFile',
        AWSS3 = 'AWSS3',
        AWSKinesis = 'AWSKinesis',
        MongoDB = 'MongoDB',
        InternalKafka = 'InternalKafka',
    }

    export class LoggingIntegrationRequest
    {
        public integrationId?: string;
        public provider: LoggingProvider;
        public integrationName: string;
        public isEnabled: boolean;

        public constructor(init?: Partial<LoggingIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export class AmqpLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public host: string;
        public port: number;
        public virtualHost: string;
        public exchange: string;
        public routingKey: string;
        public username: string;
        public password: string;

        public constructor(init?: Partial<AmqpLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsKinesisLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public streamName: string;
        public region: string;
        public accessKey: string;
        public secretKey: string;

        public constructor(init?: Partial<AwsKinesisLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum AwsS3LoggingIntegrationType
    {
        Iam = 'Iam',
        CrossAccountRole = 'CrossAccountRole',
    }

    export class AwsS3LoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public integrationType: AwsS3LoggingIntegrationType;
        public bucketName: string;
        public region: string;
        public roleArn?: string;
        public externalId?: string;
        public accessKey?: string;
        public secretKey?: string;

        public constructor(init?: Partial<AwsS3LoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class TelegramLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public chatId: string;
        public botToken: string;

        public constructor(init?: Partial<TelegramLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class NewRelicLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public region: string;
        public serviceName: string;
        public apiKey: string;

        public constructor(init?: Partial<NewRelicLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MicrosoftTeamsLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public channelName?: string;
        public webhookUrl: string;

        public constructor(init?: Partial<MicrosoftTeamsLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public databaseName?: string;
        public connectionString: string;

        public constructor(init?: Partial<MongoDbLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class KafkaLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public bootstrapServers: string;
        public topic: string;
        public securityProtocol?: string;
        public saslUsername?: string;
        public saslPassword?: string;

        public constructor(init?: Partial<KafkaLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class PrometheusLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public endpointUrl: string;
        public jobName?: string;
        public bearerToken?: string;

        public constructor(init?: Partial<PrometheusLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class DataDogLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public site: string;
        public serviceName: string;
        public environment: string;
        public apiKey: string;

        public constructor(init?: Partial<DataDogLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class InternalKafkaLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public bootstrapServers: string;
        public topic: string;
        public securityProtocol?: string;
        public saslUsername?: string;
        public saslPassword?: string;

        public constructor(init?: Partial<InternalKafkaLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class ElasticSearchLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public uri: string;
        public index: string;
        public username?: string;
        public password?: string;

        public constructor(init?: Partial<ElasticSearchLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class ZabbixLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public apiUrl: string;
        public hostName: string;
        public apiToken: string;

        public constructor(init?: Partial<ZabbixLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class SplunkLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public hecEndpointUrl: string;
        public index: string;
        public hecToken: string;

        public constructor(init?: Partial<SplunkLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AzureOtelLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public endpointUrl: string;
        public resourceName: string;
        public connectionString: string;

        public constructor(init?: Partial<AzureOtelLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class KibanaLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public uri: string;
        public spaceId?: string;
        public apiKey: string;

        public constructor(init?: Partial<KibanaLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class LocalFileLoggingIntegrationRequest extends LoggingIntegrationRequest
    {
        public rootPath?: string;

        public constructor(init?: Partial<LocalFileLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum MembershipProvider
    {
        AppleSignIn = 'AppleSignIn',
        GoogleSignIn = 'GoogleSignIn',
        Google = 'Google',
        Facebook = 'Facebook',
        X = 'X',
        GitHub = 'GitHub',
        LinkedIn = 'LinkedIn',
        Okta = 'Okta',
        Microsoft = 'Microsoft',
    }

    export class MembershipIntegrationRequest
    {
        public integrationId?: string;
        public provider: MembershipProvider;
        public integrationName: string;
        public isEnabled: boolean;

        public constructor(init?: Partial<MembershipIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export class DisplayName
    {
        public value: string;

        public constructor(init?: Partial<DisplayName>) { (Object as any).assign(this, init); }
    }

    export class RoleName
    {
        public name: string;
        public displayName: string;
        // @Ignore()
        public isAdministrator: boolean;

        // @Ignore()
        public isAuthenticated: boolean;

        // @Ignore()
        public isGuest: boolean;

        // @Ignore()
        public isRootRole: boolean;

        // @Ignore()
        public isCollaboratorRole: boolean;

        // @Ignore()
        public isSystemRole: boolean;

        public constructor(init?: Partial<RoleName>) { (Object as any).assign(this, init); }
    }

    export class OAuthModeConfig
    {
        public name: DisplayName;
        public callbackUrl: string;
        public logoutUrl?: string;
        public failureRedirectUrl?: string;
        public roleName?: RoleName;

        public constructor(init?: Partial<OAuthModeConfig>) { (Object as any).assign(this, init); }
    }

    export class OktaMembershipIntegrationRequest extends MembershipIntegrationRequest
    {
        public domain: string;
        public clientId: string;
        public clientSecret: string;
        public oAuthModes?: OAuthModeConfig[];

        public constructor(init?: Partial<OktaMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class XMembershipIntegrationRequest extends MembershipIntegrationRequest
    {
        public apiKey: string;
        public apiSecretKey: string;
        public oAuthModes?: OAuthModeConfig[];

        public constructor(init?: Partial<XMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleMembershipIntegrationRequest extends MembershipIntegrationRequest
    {
        public clientId: string;
        public clientSecret: string;
        public oAuthModes?: OAuthModeConfig[];

        public constructor(init?: Partial<GoogleMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MicrosoftMembershipIntegrationRequest extends MembershipIntegrationRequest
    {
        public tenantId: string;
        public clientId: string;
        public clientSecret: string;
        public oAuthModes?: OAuthModeConfig[];

        public constructor(init?: Partial<MicrosoftMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class GitHubMembershipIntegrationRequest extends MembershipIntegrationRequest
    {
        public clientId: string;
        public clientSecret: string;
        public oAuthModes?: OAuthModeConfig[];

        public constructor(init?: Partial<GitHubMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MetaMembershipIntegrationRequest extends MembershipIntegrationRequest
    {
        public appId: string;
        public appSecret: string;
        public oAuthModes?: OAuthModeConfig[];

        public constructor(init?: Partial<MetaMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AppleMembershipIntegrationRequest extends MembershipIntegrationRequest
    {
        public teamId: string;
        public appBundleId: string;
        public serviceId: string;
        public keyId: string;
        public privateKey: string;
        public isProduction: boolean;
        public oAuthModes?: OAuthModeConfig[];

        public constructor(init?: Partial<AppleMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum PaymentGatewayPlatform
    {
        Stripe = 'Stripe',
        Adyen = 'Adyen',
        Paddle = 'Paddle',
        LemonSqueezy = 'LemonSqueezy',
        AppleInApp = 'AppleInApp',
        GoogleInApp = 'GoogleInApp',
        Shopify = 'Shopify',
        WooCommerce = 'WooCommerce',
        Magento = 'Magento',
        PayPal = 'PayPal',
        Braintree = 'Braintree',
        AuthorizeNet = 'AuthorizeNet',
        CheckOutCom = 'CheckOutCom',
        Mollie = 'Mollie',
        Worldpay = 'Worldpay',
    }

    export class PaymentIntegrationRequest
    {
        public integrationId?: string;
        public gatewayPlatform: PaymentGatewayPlatform;
        public integrationName: string;
        public isEnabled: boolean;

        public constructor(init?: Partial<PaymentIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export class LemonSqueezyPaymentIntegrationRequest extends PaymentIntegrationRequest
    {
        public storeId: string;
        public apiKey: string;
        public webhookSigningSecret: string;
        public isTestMode: boolean;

        public constructor(init?: Partial<LemonSqueezyPaymentIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AdyenPaymentIntegrationRequest extends PaymentIntegrationRequest
    {
        public merchantAccount: string;
        public apiKey: string;
        public environment: string;
        public webhookId?: string;
        public webhookHmacKey?: string;

        public constructor(init?: Partial<AdyenPaymentIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MolliePaymentIntegrationRequest extends PaymentIntegrationRequest
    {
        public profileId: string;
        public apiKey: string;
        public isTestMode: boolean;

        public constructor(init?: Partial<MolliePaymentIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class PaddlePaymentIntegrationRequest extends PaymentIntegrationRequest
    {
        public apiKey: string;
        public webhookEndpointSecretKey: string;
        public environment: string;
        public clientSideToken?: string;

        public constructor(init?: Partial<PaddlePaymentIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class PayPalPaymentIntegrationRequest extends PaymentIntegrationRequest
    {
        public clientId: string;
        public clientSecret: string;
        public environment: string;
        public brandName?: string;

        public constructor(init?: Partial<PayPalPaymentIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class StripePaymentIntegrationRequest extends PaymentIntegrationRequest
    {
        public publishableKey: string;
        public secretKey: string;
        public webhookSigningSecret: string;
        public webhookEndpointId?: string;
        public defaultCurrency?: string;

        public constructor(init?: Partial<StripePaymentIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AppleInAppPaymentIntegrationRequest extends PaymentIntegrationRequest
    {
        public merchantIdentifier: string;
        public merchantDomain: string;
        public displayName: string;
        public merchantIdentityCertificateP12Base64: string;
        public merchantIdentityCertificatePassword: string;
        public paymentProcessingCertificateP12Base64: string;
        public paymentProcessingCertificatePassword: string;

        public constructor(init?: Partial<AppleInAppPaymentIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleInAppPaymentIntegrationRequest extends PaymentIntegrationRequest
    {
        public merchantId: string;
        public merchantName: string;
        public gateway: string;
        public privateKeyOrToken: string;
        public gatewayMerchantId?: string;

        public constructor(init?: Partial<GoogleInAppPaymentIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export enum PushProvider
    {
        AppleApns = 'AppleApns',
        SafariWeb = 'SafariWeb',
        SafariPush = 'SafariPush',
        AndroidFirebase = 'AndroidFirebase',
        ChromeWeb = 'ChromeWeb',
        FirefoxWeb = 'FirefoxWeb',
        EdgeWeb = 'EdgeWeb',
        ChromePush = 'ChromePush',
        CodeMashIosApp = 'CodeMashIosApp',
        CodeMashAndroidApp = 'CodeMashAndroidApp',
        CodeMashSafariPlugin = 'CodeMashSafariPlugin',
        CodeMashSafariWeb = 'CodeMashSafariWeb',
        CodeMashChromePlugin = 'CodeMashChromePlugin',
        CodeMashChromeWeb = 'CodeMashChromeWeb',
        Expo = 'Expo',
    }

    export class PushIntegrationRequest
    {
        public integrationId?: string;
        public provider: PushProvider;
        public integrationName: string;
        public isEnabled: boolean;

        public constructor(init?: Partial<PushIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export class EdgeWebPushIntegrationRequest extends PushIntegrationRequest
    {
        public vapidPublicKey: string;
        public vapidPrivateKey: string;
        public subject?: string;

        public constructor(init?: Partial<EdgeWebPushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class ChromePluginPushIntegrationRequest extends PushIntegrationRequest
    {
        public extensionId: string;
        public vapidPublicKey: string;
        public vapidPrivateKey: string;
        public subject?: string;

        public constructor(init?: Partial<ChromePluginPushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class SafariPushIntegrationRequest extends PushIntegrationRequest
    {
        public websitePushId: string;
        public certificateP12Base64: string;
        public certificatePassword: string;

        public constructor(init?: Partial<SafariPushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class ChromeWebPushIntegrationRequest extends PushIntegrationRequest
    {
        public vapidPublicKey: string;
        public vapidPrivateKey: string;
        public subject?: string;

        public constructor(init?: Partial<ChromeWebPushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class FirefoxWebPushIntegrationRequest extends PushIntegrationRequest
    {
        public vapidPublicKey: string;
        public vapidPrivateKey: string;
        public subject?: string;

        public constructor(init?: Partial<FirefoxWebPushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AndroidFirebasePushIntegrationRequest extends PushIntegrationRequest
    {
        public projectId: string;
        public clientEmail: string;
        public serviceAccountJson: string;

        public constructor(init?: Partial<AndroidFirebasePushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AppleApnsPushIntegrationRequest extends PushIntegrationRequest
    {
        public teamId: string;
        public appBundleId: string;
        public keyId: string;
        public privateKey: string;
        public isProduction: boolean;

        public constructor(init?: Partial<AppleApnsPushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum CodeProvider
    {
        AwsLambda = 'AwsLambda',
        AzureFunctions = 'AzureFunctions',
        GoogleCloudFunctions = 'GoogleCloudFunctions',
        Pipedream = 'Pipedream',
        Zapier = 'Zapier',
        CloudflareWorkers = 'CloudflareWorkers',
        Vercel = 'Vercel',
        Netlify = 'Netlify',
        SupabaseEdge = 'SupabaseEdge',
        Modal = 'Modal',
    }

    export class CodeIntegrationRequest
    {
        public integrationId?: string;
        public provider: CodeProvider;
        public integrationName: string;
        public isEnabled: boolean;

        public constructor(init?: Partial<CodeIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export enum AwsLambdaIntegrationType
    {
        Iam = 'Iam',
        CrossAccountRole = 'CrossAccountRole',
    }

    export class AwsLambdaCodeIntegrationRequest extends CodeIntegrationRequest
    {
        public integrationType: AwsLambdaIntegrationType;
        public region: string;
        public roleArn?: string;
        public externalId?: string;
        public accessKey?: string;
        public secretKey?: string;

        public constructor(init?: Partial<AwsLambdaCodeIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AzureFunctionsCodeIntegrationRequest extends CodeIntegrationRequest
    {
        public functionAppName: string;
        public resourceGroup?: string;
        public connectionStringOrKey: string;

        public constructor(init?: Partial<AzureFunctionsCodeIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleCloudFunctionsCodeIntegrationRequest extends CodeIntegrationRequest
    {
        public projectId: string;
        public region?: string;
        public serviceAccountJsonKey: string;

        public constructor(init?: Partial<GoogleCloudFunctionsCodeIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum LlmProvider
    {
        OpenAI = 'OpenAI',
        Anthropic = 'Anthropic',
        Ollama = 'Ollama',
        Groq = 'Groq',
        Google = 'Google',
        Mistral = 'Mistral',
        OpenRouter = 'OpenRouter',
        Grok = 'Grok',
    }

    export class LlmIntegrationRequest
    {
        public integrationId?: string;
        public provider: LlmProvider;
        public integrationName: string;
        public isEnabled: boolean;
        public endpoint?: string;
        public defaultModel?: string;

        public constructor(init?: Partial<LlmIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export class OllamaLlmIntegrationRequest extends LlmIntegrationRequest
    {

        public constructor(init?: Partial<OllamaLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class OpenRouterLlmIntegrationRequest extends LlmIntegrationRequest implements ILlmApiKeyRequest
    {
        public apiKey: string;

        public constructor(init?: Partial<OpenRouterLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MistralLlmIntegrationRequest extends LlmIntegrationRequest implements ILlmApiKeyRequest
    {
        public apiKey: string;

        public constructor(init?: Partial<MistralLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class GrokLlmIntegrationRequest extends LlmIntegrationRequest implements ILlmApiKeyRequest
    {
        public apiKey: string;

        public constructor(init?: Partial<GrokLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class GroqLlmIntegrationRequest extends LlmIntegrationRequest implements ILlmApiKeyRequest
    {
        public apiKey: string;

        public constructor(init?: Partial<GroqLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleLlmIntegrationRequest extends LlmIntegrationRequest implements ILlmApiKeyRequest
    {
        public apiKey: string;

        public constructor(init?: Partial<GoogleLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class AnthropicLlmIntegrationRequest extends LlmIntegrationRequest implements ILlmApiKeyRequest
    {
        public apiKey: string;

        public constructor(init?: Partial<AnthropicLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class OpenAiLlmIntegrationRequest extends LlmIntegrationRequest implements ILlmApiKeyRequest
    {
        public apiKey: string;

        public constructor(init?: Partial<OpenAiLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum McpProvider
    {
        Docker = 'Docker',
        Obsidian = 'Obsidian',
        GoogleCalendar = 'GoogleCalendar',
    }

    export enum McpTransport
    {
        Sse = 'Sse',
        HttpStream = 'HttpStream',
        Stdio = 'Stdio',
    }

    export class McpIntegrationRequest
    {
        public integrationId?: string;
        public provider: McpProvider;
        public transport: McpTransport;
        public integrationName: string;
        public isEnabled: boolean;
        public name: string;
        public category: string;
        public description: string;
        public icon: string;

        public constructor(init?: Partial<McpIntegrationRequest>) { (Object as any).assign(this, init); }
    }

    export class PlaywrightMcpIntegrationRequest extends McpIntegrationRequest
    {
        public command?: string;
        public args?: string[];
        public headless: string;

        public constructor(init?: Partial<PlaywrightMcpIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbMcpIntegrationRequest extends McpIntegrationRequest
    {
        public command?: string;
        public args?: string[];
        public connectionString: string;

        public constructor(init?: Partial<MongoDbMcpIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class GitHubMcpIntegrationRequest extends McpIntegrationRequest
    {
        public serverUrl: string;
        public accessToken: string;

        public constructor(init?: Partial<GitHubMcpIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class StripeMcpIntegrationRequest extends McpIntegrationRequest
    {
        public serverUrl: string;
        public apiKey: string;

        public constructor(init?: Partial<StripeMcpIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class BraveSearchMcpIntegrationRequest extends McpIntegrationRequest
    {
        public serverUrl: string;
        public apiKey: string;

        public constructor(init?: Partial<BraveSearchMcpIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export class ObsidianMcpIntegrationRequest extends McpIntegrationRequest
    {
        public command?: string;
        public args?: string[];
        public environmentVariables?: { [index:string]: string; };

        public constructor(init?: Partial<ObsidianMcpIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
    }

    export enum CommunicationChannel
    {
        Transactional = 'Transactional',
        Marketing = 'Marketing',
        System = 'System',
    }

    // @DataContract
    export class TemplateDto implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public templateName: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public communicationChannel: CommunicationChannel;

        // @DataMember
        public isActive: boolean;

        // @DataMember
        public tags?: string[];

        public constructor(init?: Partial<TemplateDto>) { (Object as any).assign(this, init); }
    }

    export enum EmailTemplateEngine
    {
        NotSet = 'NotSet',
        Handlebars = 'Handlebars',
        Mjml = 'Mjml',
        Liquid = 'Liquid',
        Razor = 'Razor',
        Mustache = 'Mustache',
    }

    // @DataContract
    export class EmailBodyDto implements IHasRazorTemplateCode
    {
        // @DataMember
        public structure?: string;

        // @DataMember
        public code: string;

        // @DataMember
        public templateEngine: EmailTemplateEngine;

        public constructor(init?: Partial<EmailBodyDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailMessageContentDto implements IHasRazorTemplateCode
    {
        // @DataMember
        public subject: string;

        // @DataMember
        public body: EmailBodyDto;

        // @DataMember
        public staticAttachments?: IReadOnlySet<FileResourceRefDto>;

        public constructor(init?: Partial<EmailMessageContentDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailMessageTranslationDto implements IHasRazorTemplateCode
    {
        // @DataMember
        public language: string;

        // @DataMember
        public content: EmailMessageContentDto;

        // @DataMember
        public staticAttachments?: IReadOnlySet<FileResourceRefDto>;

        public constructor(init?: Partial<EmailMessageTranslationDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailTemplateDto extends TemplateDto implements IBindableContract
    {
        // @DataMember
        public translations: IReadOnlySet<EmailMessageTranslationDto>;

        // @DataMember
        public staticAttachments?: IReadOnlySet<FileResourceRefDto>;

        public constructor(init?: Partial<EmailTemplateDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushMessageContentDto implements IHasRazorTemplateCode
    {
        // @DataMember
        public title: string;

        // @DataMember
        public body: string;

        public constructor(init?: Partial<PushMessageContentDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushMessageTranslationDto implements IHasRazorTemplateCode
    {
        // @DataMember
        public language: string;

        // @DataMember
        public content: PushMessageContentDto;

        public constructor(init?: Partial<PushMessageTranslationDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushTemplateDto extends TemplateDto implements IHasRazorTemplateCode, IBindableContract
    {
        // @DataMember
        public translations: IReadOnlySet<PushMessageTranslationDto>;

        public constructor(init?: Partial<PushTemplateDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SmsMessageContentDto implements IHasRazorTemplateCode
    {
        // @DataMember
        public subject: string;

        // @DataMember
        public body: string;

        public constructor(init?: Partial<SmsMessageContentDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SmsMessageTranslationDto implements IHasRazorTemplateCode
    {
        // @DataMember
        public language: string;

        // @DataMember
        public content: SmsMessageContentDto;

        public constructor(init?: Partial<SmsMessageTranslationDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SmsTemplateDto extends TemplateDto implements IHasRazorTemplateCode, IBindableContract
    {
        // @DataMember
        public translations: IReadOnlySet<SmsMessageTranslationDto>;

        public constructor(init?: Partial<SmsTemplateDto>) { super(init); (Object as any).assign(this, init); }
    }

    export enum SystemEmailTemplateTheme
    {
        Text = 'Text',
        Branded = 'Branded',
        Creative = 'Creative',
    }

    // @DataContract
    export class SystemEmailTemplateDto extends EmailTemplateDto implements IHasDatabaseId
    {
        // @DataMember
        public imagePreview: string;

        // @DataMember
        public theme: SystemEmailTemplateTheme;

        // @DataMember
        public systemGroup: string;

        // @DataMember
        public systemTags?: string[];

        // @DataMember
        public forTrigger?: TriggerType;

        // @DataMember
        public hiddenSystemEmailTemplate: boolean;

        // @DataMember
        public id?: string;

        public constructor(init?: Partial<SystemEmailTemplateDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @Flags()
    export enum RespectTimeZoneSettings
    {
        RespectToLastLoginZone = 1,
        RespectToRegistrationZone = 2,
        RespectToRegistrationProjectZone = 4,
    }

    export class EmailCampaignDeliverySettingsDto
    {
        // @DataMember
        public recipientsSourceType: EmailCampaignRecipientsSourceTypes;

        // @DataMember
        public mappedTokens?: IReadOnlySet<TokenMappingDto>;

        // @DataMember
        public campaignTime?: number;

        // @DataMember
        public respectTimeZoneSettings?: RespectTimeZoneSettings;

        public constructor(init?: Partial<EmailCampaignDeliverySettingsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TriggerActionEmailDto extends TriggerActionDto
    {
        // @DataMember
        public templateId: string;

        // @DataMember
        public deliverySettings: EmailCampaignDeliverySettingsDto;

        public constructor(init?: Partial<TriggerActionEmailDto>) { super(init); (Object as any).assign(this, init); }
    }

    export enum PushCampaignRecipientsSourceTypes
    {
        AllUsers = 'AllUsers',
        SpecifiedUsers = 'SpecifiedUsers',
        Collection = 'Collection',
        Devices = 'Devices',
    }

    // @DataContract
    export class PushCampaignDeliverySettingsDto
    {
        // @DataMember
        public recipientsSourceType: PushCampaignRecipientsSourceTypes;

        // @DataMember
        public mappedTokens?: TokenMappingDto[];

        // @DataMember
        public campaignTime?: number;

        // @DataMember
        public respectTimeZoneSettings?: RespectTimeZoneSettings;

        public constructor(init?: Partial<PushCampaignDeliverySettingsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TriggerActionPushDto extends TriggerActionDto
    {
        // @DataMember
        public templateId: string;

        // @DataMember
        public deliverySettings: PushCampaignDeliverySettingsDto;

        public constructor(init?: Partial<TriggerActionPushDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class CodeDeliverySettingsDto
    {
        // @DataMember
        public mappedTokens?: TokenMappingDto[];

        public constructor(init?: Partial<CodeDeliverySettingsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TriggerActionCodeDto extends TriggerActionDto
    {
        // @DataMember
        public functionId: string;

        // @DataMember
        public deliverySettings: CodeDeliverySettingsDto;

        public constructor(init?: Partial<TriggerActionCodeDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class WebhookDeliverySettingsDto
    {
        // @DataMember
        public eventName?: string;

        // @DataMember
        public contentType?: string;

        // @DataMember
        public includeRawPayload: boolean;

        // @DataMember
        public mappedTokens?: IReadOnlySet<TokenMappingDto>;

        public constructor(init?: Partial<WebhookDeliverySettingsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TriggerActionWebhookDto extends TriggerActionDto
    {
        // @DataMember
        public deliverySettings?: WebhookDeliverySettingsDto;

        public constructor(init?: Partial<TriggerActionWebhookDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailToAllUsersDeliverySettingsDto extends EmailCampaignDeliverySettingsDto
    {
        // @DataMember
        public rolesNames?: IReadOnlySet<string>;

        // @DataMember
        public userTags?: IReadOnlySet<string>;

        public constructor(init?: Partial<EmailToAllUsersDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailToAccountUsersDeliverySettingsDto extends EmailCampaignDeliverySettingsDto
    {
        // @DataMember
        public userRecipients: IReadOnlySet<string>;

        // @DataMember
        public userCc?: IReadOnlySet<string>;

        // @DataMember
        public userBcc?: IReadOnlySet<string>;

        // @DataMember
        public singleEmailStrategy: boolean;

        public constructor(init?: Partial<EmailToAccountUsersDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailToUsersDeliverySettingsDto extends EmailCampaignDeliverySettingsDto
    {
        // @DataMember
        public userRecipients: IReadOnlySet<string>;

        // @DataMember
        public userCc?: IReadOnlySet<string>;

        // @DataMember
        public userBcc?: IReadOnlySet<string>;

        // @DataMember
        public singleEmailStrategy: boolean;

        public constructor(init?: Partial<EmailToUsersDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailToEmailAddressesDeliverySettingsDto extends EmailCampaignDeliverySettingsDto
    {
        // @DataMember
        public recipients: IReadOnlySet<string>;

        // @DataMember
        public recipientsCc?: IReadOnlySet<string>;

        // @DataMember
        public recipientsBcc?: IReadOnlySet<string>;

        // @DataMember
        public singleEmailStrategy: boolean;

        public constructor(init?: Partial<EmailToEmailAddressesDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailToCollectionRecordsDeliverySettingsDto extends EmailCampaignDeliverySettingsDto
    {
        // @DataMember
        public fields: IReadOnlySet<string>;

        // @DataMember
        public schemaName: string;

        // @DataMember
        public fieldType: CollectionEmailCampaignRecipientField;

        // @DataMember
        public roleNames?: IReadOnlySet<string>;

        // @DataMember
        public languages?: IReadOnlySet<string>;

        public constructor(init?: Partial<EmailToCollectionRecordsDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushToAllUsersDeliverySettingsDto extends PushCampaignDeliverySettingsDto
    {
        // @DataMember
        public rolesNames?: string[];

        // @DataMember
        public userTags?: string[];

        public constructor(init?: Partial<PushToAllUsersDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushToUsersDeliverySettingsDto extends PushCampaignDeliverySettingsDto
    {
        // @DataMember
        public recipients: string[] = [];

        public constructor(init?: Partial<PushToUsersDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushToCollectionRecordsDeliverySettingsDto extends PushCampaignDeliverySettingsDto
    {
        // @DataMember
        public fields: string[] = [];

        // @DataMember
        public fieldType: CollectionEmailCampaignRecipientField;

        // @DataMember
        public schemaName: string;

        // @DataMember
        public roleNames?: string[];

        // @DataMember
        public languages?: string[];

        public constructor(init?: Partial<PushToCollectionRecordsDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushDeviceDeliveryTokenDto
    {

        public constructor(init?: Partial<PushDeviceDeliveryTokenDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushToDevicesDeliverySettingsDto extends PushCampaignDeliverySettingsDto
    {
        // @DataMember
        public devices: PushDeviceDeliveryTokenDto[] = [];

        public constructor(init?: Partial<PushToDevicesDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    export enum SmsCampaignRecipientsSourceTypes
    {
        AllUsers = 'AllUsers',
        SpecifiedUsers = 'SpecifiedUsers',
        AccountUsers = 'AccountUsers',
        PhoneNumbers = 'PhoneNumbers',
        Collection = 'Collection',
    }

    // @DataContract
    export class SmsCampaignDeliverySettingsDto
    {
        // @DataMember
        public recipientsSourceType: SmsCampaignRecipientsSourceTypes;

        // @DataMember
        public mappedTokens?: TokenMappingDto[];

        // @DataMember
        public campaignTime?: number;

        // @DataMember
        public respectTimeZoneSettings?: RespectTimeZoneSettings;

        public constructor(init?: Partial<SmsCampaignDeliverySettingsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SmsToAllUsersDeliverySettingsDto extends SmsCampaignDeliverySettingsDto
    {
        // @DataMember
        public rolesNames?: string[];

        // @DataMember
        public userTags?: string[];

        public constructor(init?: Partial<SmsToAllUsersDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SmsToUsersDeliverySettingsDto extends SmsCampaignDeliverySettingsDto
    {
        // @DataMember
        public recipients: string[] = [];

        public constructor(init?: Partial<SmsToUsersDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SmsToCollectionRecordsDeliverySettingsDto extends SmsCampaignDeliverySettingsDto
    {
        // @DataMember
        public fields: string[] = [];

        // @DataMember
        public fieldType: CollectionEmailCampaignRecipientField;

        // @DataMember
        public schemaName: string;

        // @DataMember
        public roleNames?: string[];

        // @DataMember
        public languages?: string[];

        public constructor(init?: Partial<SmsToCollectionRecordsDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SmsToPhoneNumbersDeliverySettingsDto extends SmsCampaignDeliverySettingsDto
    {
        // @DataMember
        public phoneNumbers: string[] = [];

        public constructor(init?: Partial<SmsToPhoneNumbersDeliverySettingsDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class IntegrationDto implements IHasViewId
    {
        public viewId: string;
        public integrationName: string;
        public isEnabled: boolean;
        public lastIntegrationTestAtUtc?: string;
        public lastIntegrationTestSucceeded?: boolean;
        public lastIntegrationTestErrors: IReadOnlyList<string>;
        public humanDeliveryConfirmedAtUtc?: string;
        public requiresHumanDeliveryConfirmation: boolean;

        public constructor(init?: Partial<IntegrationDto>) { (Object as any).assign(this, init); }
    }

    export class LlmIntegrationDto extends IntegrationDto
    {
        public provider: LlmProvider;
        public baseUrl?: string;
        public defaultModel?: string;
        public isConfigured: boolean;
        public isSystemOwned: boolean;

        public constructor(init?: Partial<LlmIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class OpenAiLlmIntegrationDto extends LlmIntegrationDto
    {

        public constructor(init?: Partial<OpenAiLlmIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AnthropicLlmIntegrationDto extends LlmIntegrationDto
    {

        public constructor(init?: Partial<AnthropicLlmIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class OllamaLlmIntegrationDto extends LlmIntegrationDto
    {

        public constructor(init?: Partial<OllamaLlmIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GroqLlmIntegrationDto extends LlmIntegrationDto
    {

        public constructor(init?: Partial<GroqLlmIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleLlmIntegrationDto extends LlmIntegrationDto
    {

        public constructor(init?: Partial<GoogleLlmIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MistralLlmIntegrationDto extends LlmIntegrationDto
    {

        public constructor(init?: Partial<MistralLlmIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class OpenRouterLlmIntegrationDto extends LlmIntegrationDto
    {

        public constructor(init?: Partial<OpenRouterLlmIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GrokLlmIntegrationDto extends LlmIntegrationDto
    {

        public constructor(init?: Partial<GrokLlmIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class McpMetadata
    {
        public name: string;
        public category: string;
        public description: string;
        public icon: string;

        public constructor(init?: Partial<McpMetadata>) { (Object as any).assign(this, init); }
    }

    export enum McpAuth
    {
        OAuth2 = 'OAuth2',
        ApiKey = 'ApiKey',
        None = 'None',
    }

    export class McpIntegrationDto extends IntegrationDto
    {
        public provider: McpProvider;
        public transport: McpTransport;
        public metadata: McpMetadata;
        public isConfigured: boolean;
        public isSystemOwned: boolean;
        public command?: string;
        public args?: string[];
        public serverUrl?: string;
        public auth?: McpAuth;

        public constructor(init?: Partial<McpIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class DockerMcpIntegrationDto extends McpIntegrationDto
    {

        public constructor(init?: Partial<DockerMcpIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleCalendarMcpIntegrationDto extends McpIntegrationDto
    {

        public constructor(init?: Partial<GoogleCalendarMcpIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class ObsidianMcpIntegrationDto extends McpIntegrationDto
    {

        public constructor(init?: Partial<ObsidianMcpIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class CodeIntegrationDto extends IntegrationDto
    {
        public provider: CodeProvider;

        public constructor(init?: Partial<CodeIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsLambdaCrossAccountRoleCodeIntegrationDto extends CodeIntegrationDto
    {
        public region: string;
        public roleArn: string;
        public externalId: string;

        public constructor(init?: Partial<AwsLambdaCrossAccountRoleCodeIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsLambdaIamCodeIntegrationDto extends CodeIntegrationDto
    {
        public region: string;

        public constructor(init?: Partial<AwsLambdaIamCodeIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AzureFunctionsCodeIntegrationDto extends CodeIntegrationDto
    {
        public functionAppName: string;
        public resourceGroup?: string;

        public constructor(init?: Partial<AzureFunctionsCodeIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleCloudFunctionsCodeIntegrationDto extends CodeIntegrationDto
    {
        public projectId: string;
        public region?: string;

        public constructor(init?: Partial<GoogleCloudFunctionsCodeIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class PaymentsIntegrationDto extends IntegrationDto
    {
        public gatewayPlatform: PaymentGatewayPlatform;

        public constructor(init?: Partial<PaymentsIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AdyenPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public merchantAccount: string;
        public environment: string;
        public webhookId?: string;

        public constructor(init?: Partial<AdyenPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AppleInAppPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public merchantIdentifier: string;
        public merchantDomain: string;
        public displayName: string;

        public constructor(init?: Partial<AppleInAppPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleInAppPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public merchantId: string;
        public merchantName: string;
        public gateway: string;
        public gatewayMerchantId?: string;

        public constructor(init?: Partial<GoogleInAppPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class LemonSqueezyPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public storeId: string;
        public isTestMode: boolean;

        public constructor(init?: Partial<LemonSqueezyPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MolliePaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public profileId: string;
        public isTestMode: boolean;

        public constructor(init?: Partial<MolliePaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class PaddlePaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public environment: string;
        public clientSideToken?: string;

        public constructor(init?: Partial<PaddlePaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class PayPalPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public clientId: string;
        public environment: string;
        public brandName?: string;

        public constructor(init?: Partial<PayPalPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class StripePaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public publishableKey: string;
        public webhookEndpointId?: string;
        public defaultCurrency?: string;

        public constructor(init?: Partial<StripePaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class ShopifyPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public shopDomain: string;
        public webhookSecret?: string;

        public constructor(init?: Partial<ShopifyPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class WooCommercePaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public storeUrl: string;
        public webhookSecret?: string;

        public constructor(init?: Partial<WooCommercePaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MagentoPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public storeUrl: string;
        public webhookSecret?: string;

        public constructor(init?: Partial<MagentoPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class BraintreePaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public merchantId: string;
        public environment: string;
        public webhookSecret?: string;

        public constructor(init?: Partial<BraintreePaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AuthorizeNetPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public merchantLoginId: string;
        public environment: string;
        public webhookSignatureKey?: string;

        public constructor(init?: Partial<AuthorizeNetPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class CheckOutComPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public merchantAccount: string;
        public environment: string;
        public webhookSecret?: string;

        public constructor(init?: Partial<CheckOutComPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class WorldpayPaymentIntegrationDto extends PaymentsIntegrationDto
    {
        public merchantCode: string;
        public environment: string;
        public webhookSecret?: string;

        public constructor(init?: Partial<WorldpayPaymentIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MembershipIntegrationDto extends IntegrationDto
    {
        public provider: MembershipProvider;

        public constructor(init?: Partial<MembershipIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AppleSignInMembershipIntegrationDto extends MembershipIntegrationDto
    {
        public teamId: string;
        public appBundleId: string;
        public serviceId: string;

        public constructor(init?: Partial<AppleSignInMembershipIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GitHubMembershipIntegrationDto extends MembershipIntegrationDto
    {
        public clientId: string;

        public constructor(init?: Partial<GitHubMembershipIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleMembershipIntegrationDto extends MembershipIntegrationDto
    {
        public clientId: string;

        public constructor(init?: Partial<GoogleMembershipIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MetaMembershipIntegrationDto extends MembershipIntegrationDto
    {
        public appId: string;

        public constructor(init?: Partial<MetaMembershipIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MicrosoftMembershipIntegrationDto extends MembershipIntegrationDto
    {
        public tenantId: string;
        public clientId: string;

        public constructor(init?: Partial<MicrosoftMembershipIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class OktaMembershipIntegrationDto extends MembershipIntegrationDto
    {
        public domain: string;
        public clientId: string;

        public constructor(init?: Partial<OktaMembershipIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class XMembershipIntegrationDto extends MembershipIntegrationDto
    {
        public apiKey: string;

        public constructor(init?: Partial<XMembershipIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class LoggingIntegrationDto extends IntegrationDto
    {
        public provider: LoggingProvider;

        public constructor(init?: Partial<LoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AmqpLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public host: string;
        public port: number;
        public virtualHost: string;
        public exchange: string;
        public routingKey: string;

        public constructor(init?: Partial<AmqpLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsKinesisLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public streamName: string;
        public region: string;

        public constructor(init?: Partial<AwsKinesisLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsS3CrossAccountRoleLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public bucketName: string;
        public region: string;
        public roleArn: string;
        public externalId: string;

        public constructor(init?: Partial<AwsS3CrossAccountRoleLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsS3IamLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public bucketName: string;
        public region: string;

        public constructor(init?: Partial<AwsS3IamLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AzureOtelLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public endpointUrl: string;
        public resourceName: string;

        public constructor(init?: Partial<AzureOtelLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class DataDogLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public site: string;
        public serviceName: string;
        public environment: string;

        public constructor(init?: Partial<DataDogLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class ElasticSearchLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public uri: string;
        public index: string;

        public constructor(init?: Partial<ElasticSearchLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class InternalKafkaLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public bootstrapServers: string;
        public topic: string;
        public securityProtocol?: string;

        public constructor(init?: Partial<InternalKafkaLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class KafkaLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public bootstrapServers: string;
        public topic: string;
        public securityProtocol?: string;

        public constructor(init?: Partial<KafkaLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class KibanaLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public uri: string;
        public spaceId?: string;

        public constructor(init?: Partial<KibanaLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class LocalFileLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public rootPath?: string;

        public constructor(init?: Partial<LocalFileLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MicrosoftTeamsLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public channelName?: string;

        public constructor(init?: Partial<MicrosoftTeamsLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public databaseName?: string;

        public constructor(init?: Partial<MongoDbLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class NewRelicLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public region: string;
        public serviceName: string;

        public constructor(init?: Partial<NewRelicLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class PrometheusLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public endpointUrl: string;
        public jobName?: string;

        public constructor(init?: Partial<PrometheusLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class SplunkLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public hecEndpointUrl: string;
        public index: string;

        public constructor(init?: Partial<SplunkLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class TelegramLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public chatId: string;

        public constructor(init?: Partial<TelegramLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class ZabbixLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public apiUrl: string;
        public hostName: string;

        public constructor(init?: Partial<ZabbixLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class SlackLoggingIntegrationDto extends LoggingIntegrationDto
    {
        public channelName?: string;

        public constructor(init?: Partial<SlackLoggingIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class FilesIntegrationDto extends IntegrationDto
    {
        public provider: FileProvider;

        public constructor(init?: Partial<FilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AppleICloudFilesIntegrationDto extends FilesIntegrationDto
    {
        public containerIdentifier: string;
        public relativePath?: string;

        public constructor(init?: Partial<AppleICloudFilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsS3CrossAccountRoleFilesIntegrationDto extends FilesIntegrationDto
    {
        public bucketName: string;
        public region: string;
        public roleArn: string;
        public externalId: string;

        public constructor(init?: Partial<AwsS3CrossAccountRoleFilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsS3IamFilesIntegrationDto extends FilesIntegrationDto
    {
        public bucketName: string;
        public region: string;

        public constructor(init?: Partial<AwsS3IamFilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AzureBlobFilesIntegrationDto extends FilesIntegrationDto
    {
        public blobName: string;

        public constructor(init?: Partial<AzureBlobFilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class DropBoxFilesIntegrationDto extends FilesIntegrationDto
    {
        public rootPath?: string;

        public constructor(init?: Partial<DropBoxFilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class FtpFilesIntegrationDto extends FilesIntegrationDto
    {
        public host: string;
        public port: number;
        public rootPath?: string;
        public useSsl: boolean;

        public constructor(init?: Partial<FtpFilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleCloudFilesIntegrationDto extends FilesIntegrationDto
    {
        public bucketName: string;

        public constructor(init?: Partial<GoogleCloudFilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GoogleDriveFilesIntegrationDto extends FilesIntegrationDto
    {
        public rootFolderId?: string;

        public constructor(init?: Partial<GoogleDriveFilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class LocalFilesIntegrationDto extends FilesIntegrationDto
    {
        public rootPath?: string;

        public constructor(init?: Partial<LocalFilesIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class DatabaseIntegrationDto extends IntegrationDto
    {
        public provider: DatabaseProvider;

        public constructor(init?: Partial<DatabaseIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbAtlasClusterIntegrationDto extends DatabaseIntegrationDto
    {
        public databaseName?: string;

        public constructor(init?: Partial<MongoDbAtlasClusterIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbAtlasServerlessIntegrationDto extends DatabaseIntegrationDto
    {
        public databaseName?: string;

        public constructor(init?: Partial<MongoDbAtlasServerlessIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbConnectionStringIntegrationDto extends DatabaseIntegrationDto
    {
        public databaseName?: string;

        public constructor(init?: Partial<MongoDbConnectionStringIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export enum SmsProvider
    {
        Twilio = 'Twilio',
        Vonage = 'Vonage',
        Plivo = 'Plivo',
        Telnyx = 'Telnyx',
        Bird = 'Bird',
        Telesign = 'Telesign',
        Sinch = 'Sinch',
    }

    export class SmsIntegrationDto extends IntegrationDto
    {
        public provider: SmsProvider;

        public constructor(init?: Partial<SmsIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class BirdSmsIntegrationDto extends SmsIntegrationDto
    {
        public originator: string;
        public region: string;

        public constructor(init?: Partial<BirdSmsIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class PlivoSmsIntegrationDto extends SmsIntegrationDto
    {
        public authId: string;
        public fromPhoneNumber: string;

        public constructor(init?: Partial<PlivoSmsIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class SinchSmsIntegrationDto extends SmsIntegrationDto
    {
        public servicePlanId: string;
        public fromPhoneNumber: string;

        public constructor(init?: Partial<SinchSmsIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class TelesignSmsIntegrationDto extends SmsIntegrationDto
    {
        public customerId: string;
        public fromSender: string;

        public constructor(init?: Partial<TelesignSmsIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class TelnyxSmsIntegrationDto extends SmsIntegrationDto
    {
        public messagingProfileId: string;
        public fromPhoneNumber: string;

        public constructor(init?: Partial<TelnyxSmsIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class TwilioSmsIntegrationDto extends SmsIntegrationDto
    {
        public accountSid: string;
        public fromPhoneNumber: string;

        public constructor(init?: Partial<TwilioSmsIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class VonageSmsIntegrationDto extends SmsIntegrationDto
    {
        public apiKey: string;
        public fromSender: string;

        public constructor(init?: Partial<VonageSmsIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class PushIntegrationDto extends IntegrationDto
    {
        public provider: PushProvider;

        public constructor(init?: Partial<PushIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AndroidFirebasePushIntegrationDto extends PushIntegrationDto
    {
        public projectId: string;
        public clientEmail: string;

        public constructor(init?: Partial<AndroidFirebasePushIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AppleApnsPushIntegrationDto extends PushIntegrationDto
    {
        public teamId: string;
        public appBundleId: string;

        public constructor(init?: Partial<AppleApnsPushIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class ChromePluginPushIntegrationDto extends PushIntegrationDto
    {
        public extensionId: string;
        public vapidPublicKey: string;
        public subject?: string;

        public constructor(init?: Partial<ChromePluginPushIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class ChromeWebPushIntegrationDto extends PushIntegrationDto
    {
        public vapidPublicKey: string;
        public subject?: string;

        public constructor(init?: Partial<ChromeWebPushIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class EdgeWebPushIntegrationDto extends PushIntegrationDto
    {
        public vapidPublicKey: string;
        public subject?: string;

        public constructor(init?: Partial<EdgeWebPushIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class FirefoxWebPushIntegrationDto extends PushIntegrationDto
    {
        public vapidPublicKey: string;
        public subject?: string;

        public constructor(init?: Partial<FirefoxWebPushIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class SafariPushIntegrationDto extends PushIntegrationDto
    {
        public websitePushId: string;

        public constructor(init?: Partial<SafariPushIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class EmailIntegrationDto extends IntegrationDto
    {
        public provider: EmailProvider;
        public emailAddress: string;
        public emailSenderName?: string;

        public constructor(init?: Partial<EmailIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsSesEmailIntegrationDto extends EmailIntegrationDto
    {
        public region: string;
        public identityArn: string;
        public configurationSetName?: string;

        public constructor(init?: Partial<AwsSesEmailIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsCrossAccountRoleEmailIntegrationDto extends AwsSesEmailIntegrationDto
    {
        public roleArn: string;
        public externalId: string;

        public constructor(init?: Partial<AwsCrossAccountRoleEmailIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class AwsIamEmailIntegrationDto extends AwsSesEmailIntegrationDto
    {

        public constructor(init?: Partial<AwsIamEmailIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class MailGunEmailIntegrationDto extends EmailIntegrationDto
    {
        public domain: string;

        public constructor(init?: Partial<MailGunEmailIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class SendGridEmailIntegrationDto extends EmailIntegrationDto
    {

        public constructor(init?: Partial<SendGridEmailIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class SmtpEmailIntegrationDto extends EmailIntegrationDto
    {
        public hostName: string;
        public port: number;

        public constructor(init?: Partial<SmtpEmailIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class WebhookDestinationDto
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public destinationName: string;

        // @DataMember
        public endpointUrl: string;

        // @DataMember
        public selectedEvents: IReadOnlyList<string>;

        // @DataMember
        public extraHeaders?: IReadOnlyDictionary<string, string>;

        // @DataMember
        public isEnabled: boolean;

        public constructor(init?: Partial<WebhookDestinationDto>) { (Object as any).assign(this, init); }
    }

    export class WebhookIntegrationDto extends IntegrationDto
    {
        public destinations: IReadOnlyList<WebhookDestinationDto>;
        public extraHeaders?: IReadOnlyDictionary<string, string>;

        public constructor(init?: Partial<WebhookIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export enum SchedulerTaskType
    {
        EmailCampaign = 'EmailCampaign',
        PushCampaign = 'PushCampaign',
        SmsCampaign = 'SmsCampaign',
        CodeFunctionalCall = 'CodeFunctionalCall',
        WebhookCall = 'WebhookCall',
    }

    // @DataContract
    export class SchedulerTaskDto
    {
        // @DataMember
        public projectId: string;

        // @DataMember
        public taskId: string;

        // @DataMember
        public name: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public cron: string;

        // @DataMember
        public type: SchedulerTaskType;

        // @DataMember
        public payloadJson: string;

        // @DataMember
        public initiatorId: string;

        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public stopOnError: boolean;

        // @DataMember
        public createdAtUnix?: number;

        // @DataMember
        public updatedAtUnix?: number;

        public constructor(init?: Partial<SchedulerTaskDto>) { (Object as any).assign(this, init); }
    }

    export class MongoDbAggregateDto implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public displayName: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public schemaViewId: string;

        // @DataMember
        public pipeline: string;

        public constructor(init?: Partial<MongoDbAggregateDto>) { (Object as any).assign(this, init); }
    }

    export enum MarketplaceTransport
    {
        Mcp = 'Mcp',
        Rest = 'Rest',
        Code = 'Code',
    }

    export enum MarketplaceCategory
    {
        Other = 'Other',
        Crm = 'Crm',
        Erp = 'Erp',
        Marketing = 'Marketing',
        Communication = 'Communication',
        Productivity = 'Productivity',
        Storage = 'Storage',
        Analytics = 'Analytics',
        Identity = 'Identity',
        Payments = 'Payments',
        DevTools = 'DevTools',
        Ai = 'Ai',
        Files = 'Files',
        Database = 'Database',
        Calendar = 'Calendar',
    }

    // @DataContract
    export class MarketplaceIntegrationDto extends IntegrationDto
    {
        // @DataMember
        public listingViewId: string;

        // @DataMember
        public transport: MarketplaceTransport;

        // @DataMember
        public vendor: string;

        // @DataMember
        public category: MarketplaceCategory;

        // @DataMember
        public description?: string;

        // @DataMember
        public config: IReadOnlyDictionary<string, string>;

        public constructor(init?: Partial<MarketplaceIntegrationDto>) { super(init); (Object as any).assign(this, init); }
    }

    export enum MarketplaceMappingSource
    {
        Default = 'Default',
        Resolver = 'Resolver',
        FromRequest = 'FromRequest',
    }

    // @DataContract
    export class MarketplaceMappingDto
    {
        // @DataMember
        public parameterName: string;

        // @DataMember
        public source: MarketplaceMappingSource;

        // @DataMember
        public defaultValue?: string;

        // @DataMember
        public resolver?: TokenMappingResolverType;

        // @DataMember
        public tokenKey?: string;

        // @DataMember
        public fromRequestPath?: string;

        // @DataMember
        public isRequired: boolean;

        public constructor(init?: Partial<MarketplaceMappingDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class MarketplaceFunctionBindingDto implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public integrationViewId: string;

        // @DataMember
        public functionKey: string;

        // @DataMember
        public displayName: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public mappings: IReadOnlyList<MarketplaceMappingDto>;

        public constructor(init?: Partial<MarketplaceFunctionBindingDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class MarketplaceFunctionParameterDto
    {
        // @DataMember
        public name: string;

        // @DataMember
        public type: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public isRequired: boolean;

        // @DataMember
        public defaultValue?: string;

        public constructor(init?: Partial<MarketplaceFunctionParameterDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class MarketplaceFunctionDefinitionDto
    {
        // @DataMember
        public functionKey: string;

        // @DataMember
        public displayName: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public group?: string;

        // @DataMember
        public parameters: IReadOnlyList<MarketplaceFunctionParameterDto>;

        public constructor(init?: Partial<MarketplaceFunctionDefinitionDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class MarketplaceListingDto implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public slug: string;

        // @DataMember
        public displayName: string;

        // @DataMember
        public vendor: string;

        // @DataMember
        public category: MarketplaceCategory;

        // @DataMember
        public transport: MarketplaceTransport;

        // @DataMember
        public description?: string;

        // @DataMember
        public iconUrl?: string;

        // @DataMember
        public documentationUrl?: string;

        // @DataMember
        public isOfficial: boolean;

        // @DataMember
        public functions: IReadOnlyList<MarketplaceFunctionDefinitionDto>;

        public constructor(init?: Partial<MarketplaceListingDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract(Namespace="http://codemash.io/types/")
    export class RequestBase implements ICultureBasedRequest, IVersionBasedRequest, IHasCorrelationIdRequest
    {
        /** @description Specify culture code when your response from the API should be localised. E.g.: en */
        // @DataMember
        // @ApiMember(DataType="string", Description="Specify culture code when your response from the API should be localised. E.g.: en", Name="CultureCode", ParameterType="header")
        public cultureCode?: string;

        /** @description TimeZone */
        // @DataMember
        // @ApiMember(DataType="string", Description="TimeZone", Name="TimeZoneId", ParameterType="header")
        public timeZoneId?: string;

        /** @description The CodeMash API version used to fetch data from the API. If not specified, the last version will be used.  E.g.: v3 */
        // @DataMember
        // @ApiMember(DataType="string", Description="The CodeMash API version used to fetch data from the API. If not specified, the last version will be used.  E.g.: v3", IsRequired=true, Name="version", ParameterType="path")
        public version: string;

        /** @description CorrelationId for each request */
        // @DataMember
        // @ApiMember(DataType="string", Description="CorrelationId for each request", Name="CorrelationId", ParameterType="header")
        public correlationId?: string;

        public constructor(init?: Partial<RequestBase>) { (Object as any).assign(this, init); }
    }

    export interface ICultureBasedRequest
    {
        cultureCode?: string;
    }

    export interface IVersionBasedRequest
    {
        version: string;
    }

    export interface IHasCorrelationIdRequest
    {
        correlationId?: string;
    }

    export enum SubscriptionType
    {
        ManagedService = 'ManagedService',
        License = 'License',
    }

    export interface IHasAccountId
    {
        accountId: string;
    }

    export class CodeMashRequestBase extends RequestBase implements IHasProjectId
    {
        /** @description ID of your project. Can be passed in a header as norbix-project-id. */
        // @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as norbix-project-id.", IsRequired=true, Name="norbix-project-id", ParameterType="header")
        public projectId: string;

        public constructor(init?: Partial<CodeMashRequestBase>) { super(init); (Object as any).assign(this, init); }
    }

    export interface IHasProjectId
    {
        projectId: string;
    }

    // @DataContract
    export class TagDescriptionDto
    {
        // @DataMember
        public title: string;

        // @DataMember
        public description?: string;

        public constructor(init?: Partial<TagDescriptionDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TagTranslationDto
    {
        // @DataMember
        public language: string;

        // @DataMember
        public content: TagDescriptionDto;

        public constructor(init?: Partial<TagTranslationDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TagDefinitionBaseDto
    {
        // @DataMember
        public tag: string;

        // @DataMember
        public translations: TagTranslationDto[] = [];

        public constructor(init?: Partial<TagDefinitionBaseDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class GroupDefinitionDto extends TagDefinitionBaseDto
    {

        public constructor(init?: Partial<GroupDefinitionDto>) { super(init); (Object as any).assign(this, init); }
    }

    export enum DeliveryChannel
    {
        Email = 'Email',
        Push = 'Push',
        Sms = 'Sms',
        WebPush = 'WebPush',
        InApp = 'InApp',
        ChatBot = 'ChatBot',
        ChatPlatform = 'ChatPlatform',
    }

    // @DataContract
    export class TagDefinitionDto extends TagDefinitionBaseDto
    {
        // @DataMember
        public defaultDelivery: { [index:string]: boolean; } = {};

        public constructor(init?: Partial<TagDefinitionDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class CursorArgs implements ICursorArgs
    {
        public field: string;
        public order: number;

        public constructor(init?: Partial<CursorArgs>) { (Object as any).assign(this, init); }
    }

    export class PagingArgs
    {
        public cursorArgs?: CursorArgs;
        public pageSize?: number;
        public startingAfter?: string;
        public endingBefore?: string;

        public constructor(init?: Partial<PagingArgs>) { (Object as any).assign(this, init); }
    }

    export class EmailAddress
    {
        public address: string;

        public constructor(init?: Partial<EmailAddress>) { (Object as any).assign(this, init); }
    }

    export class AggregateId
    {
        public value: string;

        public constructor(init?: Partial<AggregateId>) { (Object as any).assign(this, init); }
    }

    export class AccountId extends AggregateId implements IHasDomainEntityId
    {

        public constructor(init?: Partial<AccountId>) { super(init); (Object as any).assign(this, init); }
    }

    export class UtcDateTime
    {

        public constructor(init?: Partial<UtcDateTime>) { (Object as any).assign(this, init); }
    }

    export enum TimeUnit
    {
        Ticks = 'Ticks',
        Milliseconds = 'Milliseconds',
        Seconds = 'Seconds',
        Minutes = 'Minutes',
        Hours = 'Hours',
    }

    export class ExpirationToken
    {
        public items: number;
        public unit: TimeUnit;
        public value: number;

        public constructor(init?: Partial<ExpirationToken>) { (Object as any).assign(this, init); }
    }

    export class CodeMashSubscriptionId extends AggregateId
    {

        public constructor(init?: Partial<CodeMashSubscriptionId>) { super(init); (Object as any).assign(this, init); }
    }

    export class ExternalCustomerId
    {
        public id: string;

        public constructor(init?: Partial<ExternalCustomerId>) { (Object as any).assign(this, init); }
    }

    export class Quantity
    {
        public value: number;

        public constructor(init?: Partial<Quantity>) { (Object as any).assign(this, init); }
    }

    export class CodeMashManagedServiceSubscription
    {
        public subscriptionId: CodeMashSubscriptionId;
        public refCustomerId: ExternalCustomerId;
        public refSubscriptionId: string;
        public issuedOn: UtcDateTime;
        public willExpireOn: UtcDateTime;
        public projectCap: Quantity;
        public isTrial: boolean;

        public constructor(init?: Partial<CodeMashManagedServiceSubscription>) { (Object as any).assign(this, init); }
    }

    export class DomainUrl
    {
        public value: string;

        public constructor(init?: Partial<DomainUrl>) { (Object as any).assign(this, init); }
    }

    export class CodeMashLicense extends CodeMashManagedServiceSubscription
    {
        public domain: DomainUrl;
        public accountId: AccountId;
        public isEnterprise: boolean;

        public constructor(init?: Partial<CodeMashLicense>) { super(init); (Object as any).assign(this, init); }
    }

    export class ProjectId extends AggregateId implements IHasDomainEntityId
    {

        public constructor(init?: Partial<ProjectId>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ProjectName
    {
        // @DataMember
        public name: string;

        // @DataMember
        public uniqueName: string;

        public constructor(init?: Partial<ProjectName>) { (Object as any).assign(this, init); }
    }

    export class IntegrationId extends AggregateId implements IHasDomainEntityId
    {

        public constructor(init?: Partial<IntegrationId>) { super(init); (Object as any).assign(this, init); }
    }

    export class ProjectRegionId
    {
        public value: string;

        public constructor(init?: Partial<ProjectRegionId>) { (Object as any).assign(this, init); }
    }

    export enum Continent
    {
        Africa = 'Africa',
        Antarctica = 'Antarctica',
        Asia = 'Asia',
        Europe = 'Europe',
        NorthAmerica = 'NorthAmerica',
        Oceania = 'Oceania',
        SouthAmerica = 'SouthAmerica',
    }

    // @DataContract
    export class ProjectRegion
    {
        // @DataMember
        public id: ProjectRegionId;

        // @DataMember
        public name?: string;

        // @DataMember
        public continent?: Continent;

        public constructor(init?: Partial<ProjectRegion>) { (Object as any).assign(this, init); }
    }

    export class Language
    {
        public code: string;
        public name: string;

        public constructor(init?: Partial<Language>) { (Object as any).assign(this, init); }
    }

    export class FileResourceId
    {
        public value: string;

        public constructor(init?: Partial<FileResourceId>) { (Object as any).assign(this, init); }
    }

    export class FileChecksum
    {
        public algorithm: string;
        public hash: string;

        public constructor(init?: Partial<FileChecksum>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class FileResource
    {
        // @DataMember
        public id: FileResourceId;

        // @DataMember
        public originalFileName: string;

        // @DataMember
        public extension: string;

        // @DataMember
        public sizeBytes?: number;

        // @DataMember
        public checksum?: FileChecksum;

        // @DataMember
        public storedFileName: string;

        public constructor(init?: Partial<FileResource>) { (Object as any).assign(this, init); }
    }

    export class ProjectLogo
    {
        public fileResource: FileResource;
        public publicUrl?: string;

        public constructor(init?: Partial<ProjectLogo>) { (Object as any).assign(this, init); }
    }

    export class ProjectIcon
    {
        public fileResource: FileResource;
        public publicUrl?: string;

        public constructor(init?: Partial<ProjectIcon>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class BrandColor
    {
        // @DataMember
        public value: string;

        public constructor(init?: Partial<BrandColor>) { (Object as any).assign(this, init); }
    }

    export class Tag
    {

        public constructor(init?: Partial<Tag>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class GroupTags
    {
        // @DataMember
        public group: Tag;

        // @DataMember
        public tags: Tag[] = [];

        public constructor(init?: Partial<GroupTags>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ProjectCommunicationChannel
    {
        // @DataMember
        public channel: CommunicationChannel;

        // @DataMember
        public groups: GroupTags[] = [];

        public constructor(init?: Partial<ProjectCommunicationChannel>) { (Object as any).assign(this, init); }
    }

    export class TagDescription
    {
        public displayName: DisplayName;
        public description?: string;

        public constructor(init?: Partial<TagDescription>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class MessageTranslation<TContent>
    {

        public constructor(init?: Partial<MessageTranslation<TContent>>) { (Object as any).assign(this, init); }
    }

    export class TagTranslation extends MessageTranslation<TagDescription>
    {

        public constructor(init?: Partial<TagTranslation>) { super(init); (Object as any).assign(this, init); }
    }

    export class BaseTagDefinition
    {
        public tag: Tag;
        public translations: TagTranslation[] = [];

        public constructor(init?: Partial<BaseTagDefinition>) { (Object as any).assign(this, init); }
    }

    export class GroupDefinition extends BaseTagDefinition
    {

        public constructor(init?: Partial<GroupDefinition>) { super(init); (Object as any).assign(this, init); }
    }

    export class TagDefinition extends BaseTagDefinition
    {
        public defaultDelivery: { [index:string]: boolean; } = {};

        public constructor(init?: Partial<TagDefinition>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ProjectCommunication
    {
        // @DataMember
        public channels: ProjectCommunicationChannel[] = [];

        // @DataMember
        public groups: GroupDefinition[] = [];

        // @DataMember
        public tags: TagDefinition[] = [];

        public constructor(init?: Partial<ProjectCommunication>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TimeZone
    {
        // @DataMember
        public zoneId: string;

        public constructor(init?: Partial<TimeZone>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class DeleteTrigger extends CodeMashRequestBase
    {
        // @DataMember
        public triggerId: string;

        // @DataMember
        public triggerType: TriggerType;

        // @DataMember
        public schemaId?: string;

        public constructor(init?: Partial<DeleteTrigger>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class DisableTrigger extends CodeMashRequestBase
    {
        // @DataMember
        public triggerId: string;

        // @DataMember
        public triggerType: TriggerType;

        // @DataMember
        public schemaId?: string;

        public constructor(init?: Partial<DisableTrigger>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EnableTrigger extends CodeMashRequestBase
    {
        // @DataMember
        public triggerId: string;

        // @DataMember
        public triggerType: TriggerType;

        // @DataMember
        public schemaId?: string;

        public constructor(init?: Partial<EnableTrigger>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetTrigger extends CodeMashRequestBase
    {
        public id: string;

        public constructor(init?: Partial<GetTrigger>) { super(init); (Object as any).assign(this, init); }
    }

    export class CodeMashListPaginationRequestBase extends RequestBase implements IHasProjectId
    {
        /** @description ID of your project. Can be passed in a header as norbix-project-id. */
        // @DataMember
        // @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as norbix-project-id.", IsRequired=true, Name="norbix-project-id", ParameterType="header")
        public projectId: string;

        /** @description Paging */
        // @DataMember
        // @ApiMember(DataType="object", Description="Paging", IsRequired=true, Name="paging", ParameterType="body")
        public paging: PagingArgs;

        public constructor(init?: Partial<CodeMashListPaginationRequestBase>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class GetTriggers extends CodeMashListPaginationRequestBase
    {

        public constructor(init?: Partial<GetTriggers>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SaveTrigger extends CodeMashRequestBase
    {
        // @DataMember
        public trigger: SaveTriggerRequest;

        public constructor(init?: Partial<SaveTrigger>) { super(init); (Object as any).assign(this, init); }
    }

    export class Integration implements IIntegrationIdentification, IHasDomainEntityId
    {
        public integrationId: IntegrationId;
        declare public capability: string;
        public isSystemOwned: boolean;
        public integrationName: DisplayName;
        public isEnabled: boolean;
        public isConfigured: boolean;
        public lastIntegrationTestAtUtc?: string;
        public lastIntegrationTestSucceeded?: boolean;
        public lastIntegrationTestErrorMessages: IReadOnlyList<string>;
        public humanDeliveryConfirmedAtUtc?: string;
        public isApprovedThatItWorks: boolean;

        public constructor(init?: Partial<Integration>) { (Object as any).assign(this, init); }
    }

    export class MembershipIntegration extends Integration
    {
        public provider: MembershipProvider;

        public constructor(init?: Partial<MembershipIntegration>) { super(init); (Object as any).assign(this, init); }
    }

    export class PolicyId
    {
        public template: string;
        public tenancyScopeViewId: string;
        public viewId: string;
        public isSystem: boolean;

        public constructor(init?: Partial<PolicyId>) { (Object as any).assign(this, init); }
    }

    export enum PermissionEffect
    {
        Allow = 'Allow',
        Deny = 'Deny',
    }

    // @Flags()
    export enum ApplicationModule
    {
        Account = 0,
        Membership = 1,
        Database = 2,
        Files = 4,
        Code = 8,
        Email = 16,
        Push = 32,
        Payment = 64,
        Scheduler = 128,
        Logging = 256,
        ServerEvents = 512,
        Ai = 1024,
        Sms = 2048,
    }

    export class PermissionAction
    {
        public module?: ApplicationModule;
        public operation?: string;
        public isModuleWildcard: boolean;
        public isOperationWildcard: boolean;
        public isConcrete: boolean;
        public specificity: number;

        public constructor(init?: Partial<PermissionAction>) { (Object as any).assign(this, init); }
    }

    export class ResourceKind
    {
        public name: string;

        public constructor(init?: Partial<ResourceKind>) { (Object as any).assign(this, init); }
    }

    export class ResourceIdentifier
    {
        public value: string;

        public constructor(init?: Partial<ResourceIdentifier>) { (Object as any).assign(this, init); }
    }

    export class ResourcePattern
    {
        public account?: AccountId;
        public project?: ProjectId;
        public module?: ApplicationModule;
        public kind?: ResourceKind;
        public id?: ResourceIdentifier;
        public isAccountWildcard: boolean;
        public isProjectWildcard: boolean;
        public isModuleWildcard: boolean;
        public isKindWildcard: boolean;
        public isIdWildcard: boolean;
        public isConcrete: boolean;
        public isFullWildcard: boolean;
        public specificity: number;

        public constructor(init?: Partial<ResourcePattern>) { (Object as any).assign(this, init); }
    }

    export class PolicyStatement
    {
        public sid?: string;
        public effect: PermissionEffect;
        public actions: PermissionAction[] = [];
        public resources: ResourcePattern[] = [];

        public constructor(init?: Partial<PolicyStatement>) { (Object as any).assign(this, init); }
    }

    export class MembershipPolicy
    {
        public id: PolicyId;
        public name: DisplayName;
        public description?: string;
        public statements: PolicyStatement[] = [];
        public disabled: boolean;
        public isSystem: boolean;

        public constructor(init?: Partial<MembershipPolicy>) { (Object as any).assign(this, init); }
    }

    export class RoleId
    {
        public template: string;
        public tenancyScopeViewId: string;
        public viewId: string;
        public isSystem: boolean;

        public constructor(init?: Partial<RoleId>) { (Object as any).assign(this, init); }
    }

    export class MembershipRole
    {
        public id: RoleId;
        public name: DisplayName;
        public description?: string;
        public attachedPolicies: PolicyId[] = [];
        public disabled: boolean;
        public isSystem: boolean;

        public constructor(init?: Partial<MembershipRole>) { (Object as any).assign(this, init); }
    }

    export class TriggerId extends AggregateId implements IHasDomainEntityId
    {

        public constructor(init?: Partial<TriggerId>) { super(init); (Object as any).assign(this, init); }
    }

    export class TemplateId
    {
        public value: string;

        public constructor(init?: Partial<TemplateId>) { (Object as any).assign(this, init); }
    }

    export class TriggerAction
    {
        public type: TriggerActionType;
        public integrationId?: IntegrationId;
        public templateId: TemplateId;

        public constructor(init?: Partial<TriggerAction>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TemplateCode
    {

        public constructor(init?: Partial<TemplateCode>) { (Object as any).assign(this, init); }
    }

    export class Trigger implements IHasDomainEntityId
    {
        public triggerId: TriggerId;
        public name: DisplayName;
        public triggerAction: TriggerAction;
        public activationCode?: TemplateCode;
        public description?: string;
        public isEnabled: boolean;
        public integrationId?: IntegrationId;
        public type: TriggerType;

        public constructor(init?: Partial<Trigger>) { (Object as any).assign(this, init); }
    }

    export class MembershipTrigger extends Trigger
    {
        public when: MembershipTriggerType;

        public constructor(init?: Partial<MembershipTrigger>) { super(init); (Object as any).assign(this, init); }
    }

    export class TriggerByIdEventBase
    {
        public triggerId: TriggerId;

        public constructor(init?: Partial<TriggerByIdEventBase>) { (Object as any).assign(this, init); }
    }

    export class SchemaSettingsDto
    {
        // @DataMember
        public softDelete: boolean;

        public constructor(init?: Partial<SchemaSettingsDto>) { (Object as any).assign(this, init); }
    }

    export class MongoDbAggregateId extends AggregateId implements IHasDomainEntityId
    {

        public constructor(init?: Partial<MongoDbAggregateId>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbAggregateQuery
    {
        public value: string;

        public constructor(init?: Partial<MongoDbAggregateQuery>) { (Object as any).assign(this, init); }
    }

    export class SchemaId extends AggregateId implements IHasDomainEntityId
    {

        public constructor(init?: Partial<SchemaId>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbAggregate
    {
        public id: MongoDbAggregateId;
        public displayName: DisplayName;
        public description?: string;
        public query: MongoDbAggregateQuery;
        public schemaId: SchemaId;

        public constructor(init?: Partial<MongoDbAggregate>) { (Object as any).assign(this, init); }
    }

    export class DatabaseIntegration extends Integration
    {
        public provider: DatabaseProvider;

        public constructor(init?: Partial<DatabaseIntegration>) { super(init); (Object as any).assign(this, init); }
    }

    export class SchemaName
    {
        public value: string;
        public title: string;

        public constructor(init?: Partial<SchemaName>) { (Object as any).assign(this, init); }
    }

    export class JsonSchemaFieldName
    {
        public fieldName: string;

        public constructor(init?: Partial<JsonSchemaFieldName>) { (Object as any).assign(this, init); }
    }

    export class JsonSchemaField
    {
        public fieldName: JsonSchemaFieldName;

        public constructor(init?: Partial<JsonSchemaField>) { (Object as any).assign(this, init); }
    }

    export class DataSchema
    {
        public rawJson: string;
        public fields: JsonSchemaField[] = [];

        public constructor(init?: Partial<DataSchema>) { (Object as any).assign(this, init); }
    }

    export class VisualSchema
    {
        public rawJson: string;

        public constructor(init?: Partial<VisualSchema>) { (Object as any).assign(this, init); }
    }

    export class SchemaDraft
    {
        public dataSchema: DataSchema;
        public visualSchema: VisualSchema;
        public updatedAt: string;

        public constructor(init?: Partial<SchemaDraft>) { (Object as any).assign(this, init); }
    }

    export class SchemaVersion
    {
        public value: number;

        public constructor(init?: Partial<SchemaVersion>) { (Object as any).assign(this, init); }
    }

    export class MetaSchemaVersion
    {
        public value: number;

        public constructor(init?: Partial<MetaSchemaVersion>) { (Object as any).assign(this, init); }
    }

    export class PublishedSchemaVersion
    {
        public version: SchemaVersion;
        public dataSchema: DataSchema;
        public visualSchema: VisualSchema;
        public metaSchemaVersion: MetaSchemaVersion;
        public publishedAt: string;

        public constructor(init?: Partial<PublishedSchemaVersion>) { (Object as any).assign(this, init); }
    }

    export class SchemaSettings
    {
        public softDelete: boolean;

        public constructor(init?: Partial<SchemaSettings>) { (Object as any).assign(this, init); }
    }

    export class Schema implements IHasDomainEntityId
    {
        public schemaName: SchemaName;
        public id: SchemaId;
        public draft?: SchemaDraft;
        public publishedVersions: IReadOnlyList<PublishedSchemaVersion>;
        public triggers?: Trigger[];
        public settings?: SchemaSettings;

        public constructor(init?: Partial<Schema>) { (Object as any).assign(this, init); }
    }

    export class SchemaDiff
    {
        public addedFields: IReadOnlyList<string>;
        public removedFields: IReadOnlyList<string>;
        public typeChangedFields: IReadOnlyList<string>;
        public validatorTightenedFields: IReadOnlyList<string>;
        public isEmpty: boolean;

        public constructor(init?: Partial<SchemaDiff>) { (Object as any).assign(this, init); }
    }

    export class TaxonomyId extends AggregateId implements IHasDomainEntityId
    {

        public constructor(init?: Partial<TaxonomyId>) { super(init); (Object as any).assign(this, init); }
    }

    export class TaxonomyName
    {
        public value: string;
        public title: string;

        public constructor(init?: Partial<TaxonomyName>) { (Object as any).assign(this, init); }
    }

    export class RecordId
    {
        public id: string;

        public constructor(init?: Partial<RecordId>) { (Object as any).assign(this, init); }
    }

    export class Taxonomy implements IHasDomainEntityId
    {
        public parentId?: TaxonomyId;
        public id: TaxonomyId;
        public name: TaxonomyName;
        public description?: string;
        public termsMetaVisualSchema?: VisualSchema;
        public termsMetaDataSchema?: DataSchema;
        public dependencies?: TaxonomyId[];
        public recordId?: RecordId;

        public constructor(init?: Partial<Taxonomy>) { (Object as any).assign(this, init); }
    }

    export class SchemaTrigger extends Trigger
    {
        public schemaId: SchemaId;
        public when: SchemaTriggerType;
        public configuration?: TemplateCode;

        public constructor(init?: Partial<SchemaTrigger>) { super(init); (Object as any).assign(this, init); }
    }

    export class SaveEmailTemplate extends CodeMashRequestBase
    {
        public templateName: string;
        public description?: string;
        public communicationChannel: CommunicationChannel;
        public tags?: string[];
        // @DataMember
        public staticAttachments?: FileResourceRefDto[];

        public translations: EmailMessageTranslationDto[] = [];

        public constructor(init?: Partial<SaveEmailTemplate>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TranslationDto
    {
        // @DataMember
        public language: string;

        // @DataMember
        public content: string;

        public constructor(init?: Partial<TranslationDto>) { (Object as any).assign(this, init); }
    }

    export class EmailFooterId
    {
        public value: string;

        public constructor(init?: Partial<EmailFooterId>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailSenderName
    {

        public constructor(init?: Partial<EmailSenderName>) { (Object as any).assign(this, init); }
    }

    export class EmailIntegration extends Integration
    {
        public provider: EmailProvider;
        public emailAddress: EmailAddress;
        public emailSenderName?: EmailSenderName;

        public constructor(init?: Partial<EmailIntegration>) { super(init); (Object as any).assign(this, init); }
    }

    export class EmailSignatureId
    {
        public value: string;

        public constructor(init?: Partial<EmailSignatureId>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class FileResourceRef
    {
        // @DataMember(Order=1)
        public resource: FileResource;

        // @DataMember(Order=2)
        public integrationId: IntegrationId;

        // @DataMember(Order=3)
        public provider: FileProvider;

        // @DataMember(Order=4)
        public path: string;

        public constructor(init?: Partial<FileResourceRef>) { (Object as any).assign(this, init); }
    }

    export class CodeIntegration extends Integration
    {
        public provider: CodeProvider;

        public constructor(init?: Partial<CodeIntegration>) { super(init); (Object as any).assign(this, init); }
    }

    export enum MarketplaceIntegrationTransport
    {
        Mcp = 'Mcp',
        Rest = 'Rest',
        Code = 'Code',
    }

    export enum MarketplaceIntegrationCategory
    {
        Other = 'Other',
        Crm = 'Crm',
        Erp = 'Erp',
        Marketing = 'Marketing',
        Communication = 'Communication',
        Productivity = 'Productivity',
        Storage = 'Storage',
        Analytics = 'Analytics',
        Identity = 'Identity',
        Payments = 'Payments',
        DevTools = 'DevTools',
        Ai = 'Ai',
        Files = 'Files',
        Database = 'Database',
        Calendar = 'Calendar',
    }

    export class MarketplaceIntegration extends Integration
    {
        declare public capability: string;
        public listingViewId: string;
        public transport: MarketplaceIntegrationTransport;
        public vendor: string;
        public category: MarketplaceIntegrationCategory;
        public description?: string;
        public config: IReadOnlyDictionary<string, string>;

        public constructor(init?: Partial<MarketplaceIntegration>) { super(init); (Object as any).assign(this, init); }
    }

    export enum MarketplaceMappingSourceKind
    {
        Default = 'Default',
        Resolver = 'Resolver',
        FromRequest = 'FromRequest',
    }

    export class MarketplaceFunctionMapping
    {
        public parameterName: string;
        public source: MarketplaceMappingSourceKind;
        public defaultValue?: string;
        public resolver?: TokenMappingResolverType;
        public tokenKey?: string;
        public fromRequestPath?: string;
        public isRequired: boolean;

        public constructor(init?: Partial<MarketplaceFunctionMapping>) { (Object as any).assign(this, init); }
    }

    export class MarketplaceFunctionBinding implements IHasDomainEntityId
    {
        public bindingId: string;
        public integrationId: IntegrationId;
        public functionKey: string;
        public displayName: DisplayName;
        public description?: string;
        public isEnabled: boolean;
        public mappings: IReadOnlyList<MarketplaceFunctionMapping>;
        public viewId: string;

        public constructor(init?: Partial<MarketplaceFunctionBinding>) { (Object as any).assign(this, init); }
    }

    export class SavePushTemplate extends CodeMashRequestBase
    {
        public templateName: string;
        public description?: string;
        public communicationChannel: CommunicationChannel;
        public tags?: string[];
        public translations: PushMessageTranslationDto[] = [];

        public constructor(init?: Partial<SavePushTemplate>) { super(init); (Object as any).assign(this, init); }
    }

    export interface IHasAccountId
    {
        accountId: string;
    }

    export enum DeviceType
    {
        Unknown = 'Unknown',
        Phone = 'Phone',
        Tablet = 'Tablet',
        Desktop = 'Desktop',
        Tv = 'Tv',
    }

    // @DataContract
    export class PushDeviceDto
    {
        // @DataMember
        public deviceId?: string;

        // @DataMember
        public deviceOs: string;

        // @DataMember
        public token: string;

        // @DataMember
        public brand?: string;

        // @DataMember
        public manufacturer?: string;

        // @DataMember
        public modelName?: string;

        // @DataMember
        public deviceName?: string;

        // @DataMember
        public deviceType?: DeviceType;

        // @DataMember
        public osName?: string;

        // @DataMember
        public osVersion?: string;

        // @DataMember
        public platformApiLevel?: number;

        public constructor(init?: Partial<PushDeviceDto>) { (Object as any).assign(this, init); }
    }

    export class PushIntegration extends Integration
    {
        public provider: PushProvider;

        public constructor(init?: Partial<PushIntegration>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class Template<TMessageContent> implements IBindableContract
    {
        // @DataMember
        public templateId: TemplateId;

        // @DataMember
        public templateName: DisplayName;

        // @DataMember
        public translations: MessageTranslation<TMessageContent>[] = [];

        // @DataMember
        public communicationChannel: CommunicationChannel;

        // @DataMember
        public isActive: boolean;

        // @DataMember
        public description?: string;

        // @DataMember
        public tags?: Tag[];

        // @DataMember
        public fileIntegrationId?: IntegrationId;

        public constructor(init?: Partial<Template<TMessageContent>>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushTitle
    {
        // @DataMember
        public value: TemplateCode;

        public constructor(init?: Partial<PushTitle>) { (Object as any).assign(this, init); }
    }

    export class PushBody
    {
        public value: TemplateCode;

        public constructor(init?: Partial<PushBody>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushMessageContent
    {
        // @DataMember(Order=1)
        public title: PushTitle;

        // @DataMember(Order=1)
        public subTitle?: PushTitle;

        // @DataMember(Order=2)
        public body: PushBody;

        public constructor(init?: Partial<PushMessageContent>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushTemplate extends Template<PushMessageContent>
    {

        public constructor(init?: Partial<PushTemplate>) { super(init); (Object as any).assign(this, init); }
    }

    export class LoggingIntegration extends Integration
    {
        public provider: LoggingProvider;

        public constructor(init?: Partial<LoggingIntegration>) { super(init); (Object as any).assign(this, init); }
    }

    export class WebhookDestinationId extends AggregateId implements IHasDomainEntityId
    {

        public constructor(init?: Partial<WebhookDestinationId>) { super(init); (Object as any).assign(this, init); }
    }

    export class TriggerEventName
    {
        public value: string;

        public constructor(init?: Partial<TriggerEventName>) { (Object as any).assign(this, init); }
    }

    export class WebhookDestination
    {
        public destinationId: WebhookDestinationId;
        public destinationName: DisplayName;
        public endpointUrl: DomainUrl;
        public selectedEvents: IReadOnlySet<TriggerEventName>;
        public extraHeaders?: IReadOnlyDictionary<string, string>;
        public isEnabled: boolean;

        public constructor(init?: Partial<WebhookDestination>) { (Object as any).assign(this, init); }
    }

    export class WebhookIntegration extends Integration
    {
        declare public capability: string;
        public destinations: IReadOnlySet<WebhookDestination>;
        public extraHeaders?: IReadOnlyDictionary<string, string>;

        public constructor(init?: Partial<WebhookIntegration>) { super(init); (Object as any).assign(this, init); }
    }

    export class SchedulerTaskRequest
    {
        public type: SchedulerTaskType;

        public constructor(init?: Partial<SchedulerTaskRequest>) { (Object as any).assign(this, init); }
    }

    export class TaskId extends AggregateId
    {

        public constructor(init?: Partial<TaskId>) { super(init); (Object as any).assign(this, init); }
    }

    export class UserId implements IHasDomainEntityId
    {
        public value: string;

        public constructor(init?: Partial<UserId>) { (Object as any).assign(this, init); }
    }

    export class SchedulerTask implements IHasDomainEntityId
    {
        public id: TaskId;
        public type: SchedulerTaskType;
        public name: DisplayName;
        public description?: string;
        public cron: CronExpression;
        public payloadJson: string;
        public initiatorId: UserId;
        public isEnabled: boolean;
        public stopOnError: boolean;

        public constructor(init?: Partial<SchedulerTask>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export enum CodeMashRelease
    {
        NotSet = 'NotSet',
        Community = 'Community',
        ManagedService = 'ManagedService',
        Enterprise = 'Enterprise',
    }

    export enum CodeMashRuntime
    {
        Development = 'Development',
        CI = 'CI',
        Production = 'Production',
    }

    // @DataContract
    export class CodeMashLicenseFromEndpointDto
    {
        // @DataMember(Name="domain")
        public domain: string;

        // @DataMember(Name="accountId")
        public accountId: string;

        // @DataMember(Name="refCustomerId")
        public refCustomerId: string;

        // @DataMember(Name="refSubscriptionId")
        public refSubscriptionId: string;

        // @DataMember(Name="issued")
        public issued: number;

        // @DataMember(Name="expire")
        public expire: number;

        // @DataMember(Name="cap")
        public cap: number;

        // @DataMember(Name="isTrial")
        public isTrial: boolean;

        // @DataMember(Name="release")
        public release: string;

        public constructor(init?: Partial<CodeMashLicenseFromEndpointDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class AccountOwnerDto
    {
        // @DataMember
        public email: string;

        // @DataMember
        public displayName: string;

        // @DataMember
        public billingEmail?: string;

        // @DataMember
        public operationsEmail?: string;

        // @DataMember
        public securityEmail?: string;

        public constructor(init?: Partial<AccountOwnerDto>) { (Object as any).assign(this, init); }
    }

    export class ErrorDto
    {
        public message: string;
        public errorCode?: string;
        public context?: { [index:string]: string; };
        public stackTrace?: IReadOnlySet<ErrorDto>;

        public constructor(init?: Partial<ErrorDto>) { (Object as any).assign(this, init); }
    }

    export class CodeMashResponseStatus
    {
        public isSuccess: boolean;
        public errors?: ErrorDto[];

        public constructor(init?: Partial<CodeMashResponseStatus>) { (Object as any).assign(this, init); }
    }

    export class ResponseBase
    {
        public responseStatus: CodeMashResponseStatus;

        public constructor(init?: Partial<ResponseBase>) { (Object as any).assign(this, init); }
    }

    // @Flags()
    export enum AccountStatus
    {
        Registered = 1,
        PendingValidation = 2,
        Active = 8,
        InActive = 16,
        Blocked = 32,
        Unregistered = 64,
    }

    // @DataContract
    export class AccountStatusDto
    {
        // @DataMember
        public accountId: string;

        // @DataMember
        public accountIdAsGuid: string;

        // @DataMember
        public userId: string;

        // @DataMember
        public loggedInUserId: string;

        // @DataMember
        public loggedInUserEmail?: string;

        // @DataMember
        public status: AccountStatus;

        // @DataMember
        public projectCap: number;

        // @DataMember
        public permissions: string[] = [];

        // @DataMember
        public roles: string[] = [];

        // @DataMember
        public allowedProjects?: string[];

        // @DataMember
        public trialWasIssued: boolean;

        public constructor(init?: Partial<AccountStatusDto>) { (Object as any).assign(this, init); }
    }

    export enum ProjectStatus
    {
        Active = 'Active',
        Disabled = 'Disabled',
        Removed = 'Removed',
    }

    export class ProjectRegionDto
    {
        public id: string;
        public continent?: Continent;
        public name?: string;

        public constructor(init?: Partial<ProjectRegionDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ProjectBrandDto
    {
        // @DataMember
        public mainColor?: string;

        // @DataMember
        public accentColor?: string;

        // @DataMember
        public logo?: FileResourceRefDto;

        // @DataMember
        public icon?: FileResourceRefDto;

        public constructor(init?: Partial<ProjectBrandDto>) { (Object as any).assign(this, init); }
    }

    export class NotificationsSettingsGroupDto
    {
        public tag: string;
        public tags: string[] = [];

        public constructor(init?: Partial<NotificationsSettingsGroupDto>) { (Object as any).assign(this, init); }
    }

    export class NotificationSettingsChannelDto
    {
        public channel: CommunicationChannel;
        public groups: NotificationsSettingsGroupDto[] = [];

        public constructor(init?: Partial<NotificationSettingsChannelDto>) { (Object as any).assign(this, init); }
    }

    export class NotificationSettingsDto
    {
        public channels: NotificationSettingsChannelDto[] = [];
        public allGroups: GroupDefinitionDto[] = [];
        public allTags: TagDefinitionDto[] = [];

        public constructor(init?: Partial<NotificationSettingsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TriggerDto implements IHasViewId
    {
        // @DataMember
        public type: TriggerType;

        // @DataMember
        public viewId: string;

        // @DataMember
        public name: string;

        // @DataMember
        public thenAction: TriggerActionDto;

        // @DataMember
        public description?: string;

        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public activationCode?: string;

        public constructor(init?: Partial<TriggerDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SchemaTriggerDto extends TriggerDto
    {
        // @DataMember
        public schemaId: string;

        // @DataMember
        public when: SchemaTriggerType;

        // @DataMember
        public configurationCode?: string;

        public constructor(init?: Partial<SchemaTriggerDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class DatabaseDto
    {
        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public triggers?: SchemaTriggerDto[];

        // @DataMember
        public defaultIntegrationViewId?: string;

        public constructor(init?: Partial<DatabaseDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailSignatureDto implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public displayName?: string;

        // @DataMember
        public translations: TranslationDto[] = [];

        public constructor(init?: Partial<EmailSignatureDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailFooterDto implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public displayName?: string;

        // @DataMember
        public translations: TranslationDto[] = [];

        public constructor(init?: Partial<EmailFooterDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailDto
    {
        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public defaultIntegrationViewId?: string;

        // @DataMember
        public signatures?: EmailSignatureDto[];

        // @DataMember
        public footers?: EmailFooterDto[];

        public constructor(init?: Partial<EmailDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class AiDto
    {
        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public defaultIntegrationViewId?: string;

        public constructor(init?: Partial<AiDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class MembershipTriggerDto extends TriggerDto
    {
        // @DataMember
        public when: MembershipTriggerType;

        public constructor(init?: Partial<MembershipTriggerDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class RoleItemDto
    {
        public id: string;
        public name: string;
        public displayName?: string;
        public description?: string;
        public isSystem: boolean;
        public attachedPolicies?: string[];

        public constructor(init?: Partial<RoleItemDto>) { (Object as any).assign(this, init); }
    }

    export class PolicyStatementDto
    {
        public sid?: string;
        public effect: PermissionEffect;
        public actions: string[] = [];
        public resources: string[] = [];

        public constructor(init?: Partial<PolicyStatementDto>) { (Object as any).assign(this, init); }
    }

    export class PolicyItemDto
    {
        public id: string;
        public name: string;
        public description?: string;
        public isSystem: boolean;
        public statements?: PolicyStatementDto[];

        public constructor(init?: Partial<PolicyItemDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class AuthorizationDto
    {
        // @DataMember
        public userRegistersAsRole?: string;

        // @DataMember
        public allowedRegisterRoles?: string[];

        // @DataMember
        public allowedProviderRegisterRoles?: string[];

        public constructor(init?: Partial<AuthorizationDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class MembershipDto
    {
        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public triggers?: MembershipTriggerDto[];

        // @DataMember
        public customRoles?: RoleItemDto[];

        // @DataMember
        public customPolicies?: PolicyItemDto[];

        // @DataMember
        public authorization?: AuthorizationDto;

        public constructor(init?: Partial<MembershipDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class LoggingDto
    {
        // @DataMember
        public isEnabled: boolean;

        public constructor(init?: Partial<LoggingDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ServerEventsDto
    {
        // @DataMember
        public isEnabled: boolean;

        public constructor(init?: Partial<ServerEventsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushDto
    {
        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public defaultIntegrationViewId?: string;

        // @DataMember
        public marketingTags?: TagDefinitionDto[];

        // @DataMember
        public transactionalTags?: TagDefinitionDto[];

        public constructor(init?: Partial<PushDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SchedulerDto
    {
        // @DataMember
        public isEnabled: boolean;

        public constructor(init?: Partial<SchedulerDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class CodeDto
    {
        // @DataMember
        public isEnabled: boolean;

        public constructor(init?: Partial<CodeDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class FilesTriggerDto extends TriggerDto
    {
        // @DataMember
        public when: FilesTriggerType;

        public constructor(init?: Partial<FilesTriggerDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class FilesDto
    {
        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public triggers?: FilesTriggerDto[];

        // @DataMember
        public defaultIntegrationViewId?: string;

        public constructor(init?: Partial<FilesDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PaymentTriggerDto extends TriggerDto
    {
        // @DataMember
        public when: PaymentTriggerType;

        public constructor(init?: Partial<PaymentTriggerDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PaymentsDto
    {
        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public triggers?: PaymentTriggerDto[];

        public constructor(init?: Partial<PaymentsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SmsDto
    {
        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public defaultIntegrationViewId?: string;

        public constructor(init?: Partial<SmsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ProjectDto implements IHasViewId, IBindableContract
    {
        // @DataMember
        public accountViewId: string;

        // @DataMember
        public projectStatus: ProjectStatus;

        // @DataMember
        public isActive: boolean;

        // @DataMember
        public viewId: string;

        // @DataMember
        public name: string;

        // @DataMember
        public uniqueName: string;

        // @DataMember
        public hostLabel?: string;

        // @DataMember
        public apiHost?: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public marketingUrl?: string;

        // @DataMember
        public defaultLanguage: string;

        // @DataMember
        public languages: string[] = [];

        // @DataMember
        public regions?: ProjectRegionDto[];

        // @DataMember
        public brand?: ProjectBrandDto;

        // @DataMember
        public notificationSettings?: NotificationSettingsDto;

        // @DataMember
        public allowedOrigins?: string[];

        // @DataMember
        public database?: DatabaseDto;

        // @DataMember
        public email?: EmailDto;

        // @DataMember
        public ai?: AiDto;

        // @DataMember
        public membership?: MembershipDto;

        // @DataMember
        public logging?: LoggingDto;

        // @DataMember
        public serverEvents?: ServerEventsDto;

        // @DataMember
        public push?: PushDto;

        // @DataMember
        public scheduler?: SchedulerDto;

        // @DataMember
        public code?: CodeDto;

        // @DataMember
        public files?: FilesDto;

        // @DataMember
        public payments?: PaymentsDto;

        // @DataMember
        public sms?: SmsDto;

        // @DataMember
        public databaseEnabled: boolean;

        // @DataMember
        public emailEnabled: boolean;

        // @DataMember
        public membershipEnabled: boolean;

        // @DataMember
        public loggingEnabled: boolean;

        // @DataMember
        public serverEventsEnabled: boolean;

        // @DataMember
        public pushEnabled: boolean;

        // @DataMember
        public schedulerEnabled: boolean;

        // @DataMember
        public codeEnabled: boolean;

        // @DataMember
        public filesEnabled: boolean;

        // @DataMember
        public paymentsEnabled: boolean;

        // @DataMember
        public smsEnabled: boolean;

        // @DataMember
        public defaultFilesIntegrationViewId?: string;

        // @DataMember
        public defaultDatabaseIntegrationViewId?: string;

        // @DataMember
        public defaultEmailIntegrationViewId?: string;

        // @DataMember
        public defaultLlmIntegrationViewId?: string;

        // @DataMember
        public defaultPushIntegrationViewId?: string;

        // @DataMember
        public defaultSmsIntegrationViewId?: string;

        // @DataMember
        public connections: number;

        public constructor(init?: Partial<ProjectDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ProjectListItemDto
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public isActive: boolean;

        // @DataMember
        public name: string;

        // @DataMember
        public uniqueName: string;

        // @DataMember
        public regions?: ProjectRegionDto[];

        public constructor(init?: Partial<ProjectListItemDto>) { (Object as any).assign(this, init); }
    }

    export class PaginatedResponse<TViewModelProjection>
    {
        public items: IList<TViewModelProjection>;
        public hasMore: boolean;
        public hasPrevious: boolean;
        public startingAfter?: string;
        public endingBefore?: string;

        public constructor(init?: Partial<PaginatedResponse<TViewModelProjection>>) { (Object as any).assign(this, init); }
    }

    export enum UserType
    {
        Service = 'Service',
        Email = 'Email',
        UserName = 'UserName',
        Phone = 'Phone',
        Guest = 'Guest',
        Social = 'Social',
    }

    export class AccessInformationDto
    {
        public ip?: string;
        public date?: string;
        public timeZone?: string;

        public constructor(init?: Partial<AccessInformationDto>) { (Object as any).assign(this, init); }
    }

    export class RegistrationDto
    {
        public registrationInformation: AccessInformationDto;

        public constructor(init?: Partial<RegistrationDto>) { (Object as any).assign(this, init); }
    }

    export class LoginDto
    {
        public needChangePasswordOnNextLogin: boolean;
        public lastAccessInformation?: AccessInformationDto;

        public constructor(init?: Partial<LoginDto>) { (Object as any).assign(this, init); }
    }

    export enum Gender
    {
        Male = 'Male',
        Female = 'Female',
        Other = 'Other',
    }

    export class UserGeneralInfoDto
    {
        public phone?: string;
        public primaryEmail?: string;
        public displayName?: string;
        public firstName?: string;
        public lastName?: string;
        public fullName?: string;
        public addressLine1?: string;
        public addressLine2?: string;
        public country?: string;
        public city?: string;
        public state?: string;
        public postalCode?: string;
        public company?: string;
        public gender?: Gender;
        public birthDate?: number;
        public timeZone?: string;
        public language?: string;
        public blockAllMarketingMessages: boolean;
        public blockedTags?: { [index:string]: IReadOnlySet<string>; };
        public extraMetadata?: string;
        public notes?: string;

        public constructor(init?: Partial<UserGeneralInfoDto>) { (Object as any).assign(this, init); }
    }

    export enum UserStatus
    {
        Registered = 0,
        PendingValidation = 2,
        Active = 8,
        Unregistered = 16,
        Suspended = 32,
        InActive = 64,
        Blocked = 128,
    }

    export class UserDto implements IBindableContract
    {
        public id: string;
        public type: UserType;
        public email?: string;
        public userName?: string;
        public registration?: RegistrationDto;
        public login?: LoginDto;
        public generalInfo?: UserGeneralInfoDto;
        public roles?: IReadOnlySet<string>;
        public pushDevices?: IReadOnlySet<string>;
        public tags?: IReadOnlySet<string>;
        public status: UserStatus;
        public createdOn: string;
        public modifiedOn: string;

        public constructor(init?: Partial<UserDto>) { (Object as any).assign(this, init); }
    }

    export class CodeMashSubscriptionDto
    {
        public viewId: string;
        public domain: string;
        public willExpireOn: string;
        public issuedOn: string;
        public isTrial: boolean;
        public subscriptionRefId: string;

        public constructor(init?: Partial<CodeMashSubscriptionDto>) { (Object as any).assign(this, init); }
    }

    export class LicenseDto extends CodeMashSubscriptionDto
    {
        public isEnterprise: boolean;
        public projectCap: number;

        public constructor(init?: Partial<LicenseDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetTriggerResponse extends ResponseBase
    {
        public trigger?: TriggerDto;

        public constructor(init?: Partial<GetTriggerResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TriggerProjectionList implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public name: string;

        // @DataMember
        public actionType: TriggerActionType;

        // @DataMember
        public hasPreExecuteCode: boolean;

        // @DataMember
        public isEnabled: boolean;

        public constructor(init?: Partial<TriggerProjectionList>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class MembershipTriggerProjectionList extends TriggerProjectionList
    {
        // @DataMember
        public type: MembershipTriggerType;

        public constructor(init?: Partial<MembershipTriggerProjectionList>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class GetTriggersResponse extends ResponseBase
    {

        public constructor(init?: Partial<GetTriggersResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class RoleListProjectionDto
    {
        public viewId: string;
        public name: string;
        public displayName?: string;
        public isSystem: boolean;
        public policyCount: number;

        public constructor(init?: Partial<RoleListProjectionDto>) { (Object as any).assign(this, init); }
    }

    export class IntegrationListProjection implements IHasViewId
    {
        public viewId: string;
        public integrationName: string;
        public isEnabled: boolean;
        public lastIntegrationTestAtUtc?: string;
        public lastIntegrationTestSucceeded?: boolean;
        public lastIntegrationTestErrors: IReadOnlyList<string>;
        public humanDeliveryConfirmedAtUtc?: string;
        public requiresHumanDeliveryConfirmation: boolean;

        public constructor(init?: Partial<IntegrationListProjection>) { (Object as any).assign(this, init); }
    }

    export class MembershipIntegrationListProjection extends IntegrationListProjection
    {
        // @DataMember
        public provider: MembershipProvider;

        public constructor(init?: Partial<MembershipIntegrationListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SchemaTriggerProjectionList extends TriggerProjectionList
    {
        // @DataMember
        public type: SchemaTriggerType;

        public constructor(init?: Partial<SchemaTriggerProjectionList>) { super(init); (Object as any).assign(this, init); }
    }

    export class JsonSchemaFieldDto
    {
        // @DataMember
        public fieldName: string;

        public constructor(init?: Partial<JsonSchemaFieldDto>) { (Object as any).assign(this, init); }
    }

    export class DataSchemaDto
    {
        // @DataMember
        public json: string;

        // @DataMember
        public fields: JsonSchemaFieldDto[] = [];

        public constructor(init?: Partial<DataSchemaDto>) { (Object as any).assign(this, init); }
    }

    export class VisualSchemaDto
    {
        // @DataMember
        public json: string;

        public constructor(init?: Partial<VisualSchemaDto>) { (Object as any).assign(this, init); }
    }

    export class TaxonomyDto implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public name: string;

        // @DataMember
        public slug?: string;

        // @DataMember
        public parentId?: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public termsMetaDataSchema?: DataSchemaDto;

        // @DataMember
        public termsMetaVisualSchema?: VisualSchemaDto;

        // @DataMember
        public dependencies?: string[];

        public constructor(init?: Partial<TaxonomyDto>) { (Object as any).assign(this, init); }
    }

    export class TaxonomyListProjection implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public taxonomyName: string;

        // @DataMember
        public taxonomySlug: string;

        // @DataMember
        public parentId?: string;

        public constructor(init?: Partial<TaxonomyListProjection>) { (Object as any).assign(this, init); }
    }

    export class TermMultiParentDto
    {
        // @DataMember
        public taxonomyId: string;

        // @DataMember
        public parentId: string;

        // @DataMember
        public name?: string;

        // @DataMember
        public names?: { [index:string]: string; };

        public constructor(init?: Partial<TermMultiParentDto>) { (Object as any).assign(this, init); }
    }

    export class TermDto
    {
        // @DataMember
        public id: string;

        // @DataMember
        public taxonomyId?: string;

        // @DataMember
        public taxonomyName?: string;

        // @DataMember
        public parentId?: string;

        // @DataMember
        public order?: number;

        // @DataMember
        public name?: string;

        // @DataMember
        public names?: { [index:string]: string; };

        // @DataMember
        public description?: string;

        // @DataMember
        public descriptions?: { [index:string]: string; };

        // @DataMember
        public multiParents?: TermMultiParentDto[];

        // @DataMember
        public meta?: Object;

        public constructor(init?: Partial<TermDto>) { (Object as any).assign(this, init); }
    }

    export class SchemaDto implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public schemaName: string;

        // @DataMember
        public schemaSlug?: string;

        // @DataMember
        public version: number;

        // @DataMember
        public metaSchemaVersion: number;

        // @DataMember
        public dataSchema: DataSchemaDto;

        // @DataMember
        public visualSchema: VisualSchemaDto;

        // @DataMember
        public publishedAt: string;

        // @DataMember
        public settings?: SchemaSettingsDto;

        // @DataMember
        public triggers?: TriggerDto[];

        public constructor(init?: Partial<SchemaDto>) { (Object as any).assign(this, init); }
    }

    export class SchemaListProjection implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public schemaName: string;

        // @DataMember
        public schemaTitle: string;

        // @DataMember
        public latestVersion?: number;

        // @DataMember
        public hasDraft: boolean;

        // @DataMember
        public metaSchemaVersion: number;

        public constructor(init?: Partial<SchemaListProjection>) { (Object as any).assign(this, init); }
    }

    export class SchemaDraftDto
    {
        // @DataMember
        public dataSchema: DataSchemaDto;

        // @DataMember
        public visualSchema: VisualSchemaDto;

        // @DataMember
        public updatedAt: string;

        public constructor(init?: Partial<SchemaDraftDto>) { (Object as any).assign(this, init); }
    }

    export class SchemaDiffDto
    {
        // @DataMember
        public fromVersion: number;

        // @DataMember
        public toVersion: number;

        // @DataMember
        public added: string[] = [];

        // @DataMember
        public removed: string[] = [];

        // @DataMember
        public typeChanged: string[] = [];

        // @DataMember
        public validatorTightened: string[] = [];

        public constructor(init?: Partial<SchemaDiffDto>) { (Object as any).assign(this, init); }
    }

    export class SchemaVersionSummaryDto
    {
        // @DataMember
        public version: number;

        // @DataMember
        public metaSchemaVersion: number;

        // @DataMember
        public publishedAt: string;

        public constructor(init?: Partial<SchemaVersionSummaryDto>) { (Object as any).assign(this, init); }
    }

    export class DatabaseIntegrationListProjection extends IntegrationListProjection
    {
        // @DataMember
        public provider: DatabaseProvider;

        public constructor(init?: Partial<DatabaseIntegrationListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    export class MongoDbAggregateListProjection implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public displayName: string;

        // @DataMember
        public schemaViewId: string;

        public constructor(init?: Partial<MongoDbAggregateListProjection>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class FilesTriggerProjectionList extends TriggerProjectionList
    {
        // @DataMember
        public type: FilesTriggerType;

        public constructor(init?: Partial<FilesTriggerProjectionList>) { super(init); (Object as any).assign(this, init); }
    }

    export class FilesIntegrationListProjection extends IntegrationListProjection
    {
        // @DataMember
        public provider: FileProvider;

        public constructor(init?: Partial<FilesIntegrationListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TemplateListProjection implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public templateName: string;

        // @DataMember
        public isActive: boolean;

        // @DataMember
        public type: CommunicationChannel;

        // @DataMember
        public tags?: string[];

        public constructor(init?: Partial<TemplateListProjection>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class MjmlParseError
    {
        // @DataMember(Name="line")
        public line: number;

        // @DataMember(Name="message")
        public message?: string;

        // @DataMember(Name="tagName")
        public tagName?: string;

        // @DataMember(Name="formattedMessage")
        public formattedMessage?: string;

        public constructor(init?: Partial<MjmlParseError>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class HtmlFromMjmlResponse
    {
        // @DataMember(Name="html")
        public html: string;

        // @DataMember(Name="errors")
        public errors: MjmlParseError[] = [];

        public constructor(init?: Partial<HtmlFromMjmlResponse>) { (Object as any).assign(this, init); }
    }

    export class EmailTemplateListProjection extends TemplateListProjection
    {
        public hasAttachments: boolean;
        public languages: IReadOnlySet<string>;

        public constructor(init?: Partial<EmailTemplateListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    export class SystemEmailTemplateListProjection extends EmailTemplateListProjection
    {

        public constructor(init?: Partial<SystemEmailTemplateListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ListItemProjection implements IHasViewId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public displayName?: string;

        public constructor(init?: Partial<ListItemProjection>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ListItemWithTranslationsProjection extends ListItemProjection
    {
        // @DataMember
        public translations: string[] = [];

        public constructor(init?: Partial<ListItemWithTranslationsProjection>) { super(init); (Object as any).assign(this, init); }
    }

    export class EmailSettings implements IBindableContract
    {
        public signatures?: IList<ListItemWithTranslationsProjection>;
        public footers?: IList<ListItemWithTranslationsProjection>;

        public constructor(init?: Partial<EmailSettings>) { (Object as any).assign(this, init); }
    }

    export class EmailIntegrationListProjection extends IntegrationListProjection
    {
        public emailProvider: EmailProvider;
        public senderEmailAddress: string;
        public senderDisplayName?: string;

        public constructor(init?: Partial<EmailIntegrationListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class IntegrationTestResultItemDto
    {
        // @DataMember
        public operation: string;

        // @DataMember
        public result: string;

        // @DataMember
        public errors?: IReadOnlyList<string>;

        public constructor(init?: Partial<IntegrationTestResultItemDto>) { (Object as any).assign(this, init); }
    }

    export enum CampaignStatus
    {
        Pending = 'Pending',
        Registered = 'Registered',
        Scheduled = 'Scheduled',
        Started = 'Started',
        Stopped = 'Stopped',
        Processing = 'Processing',
        Completed = 'Completed',
        Failed = 'Failed',
    }

    export class CampaignStatusChangeEntryDto
    {
        public time: string;
        public status: CampaignStatus;
        public errors?: IReadOnlySet<ErrorDto>;

        public constructor(init?: Partial<CampaignStatusChangeEntryDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class CampaignDto implements IHasResponsibleUserId, IHasDatabaseId
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public createdOn: string;

        // @DataMember
        public language: string;

        // @DataMember
        public forceCampaignLanguage: boolean;

        // @DataMember
        public campaignProcessingIntegrationId?: string;

        // @DataMember
        public statusHistory: IReadOnlySet<CampaignStatusChangeEntryDto>;

        // @DataMember
        public status?: CampaignStatusChangeEntryDto;

        // @DataMember
        public tokenMappingValues?: IReadOnlySet<TokenMappingDto>;

        // @DataMember
        public notes?: string;

        // @DataMember
        public userId: string;

        // @DataMember
        public id?: string;

        public constructor(init?: Partial<CampaignDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailCampaignDto extends CampaignDto
    {
        // @DataMember
        public deliverySettings: EmailCampaignDeliverySettingsDto;

        // @DataMember
        public template: EmailTemplateDto;

        // @DataMember
        public templateIsSystem: boolean;

        public constructor(init?: Partial<EmailCampaignDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailCampaignListProjection
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public templateName: string;

        // @DataMember
        public templateId: string;

        // @DataMember
        public integrationId?: string;

        // @DataMember
        public language: string;

        // @DataMember
        public strategy: string;

        // @DataMember
        public latestStatus?: CampaignStatus;

        // @DataMember
        public createdOn: string;

        public constructor(init?: Partial<EmailCampaignListProjection>) { (Object as any).assign(this, init); }
    }

    export enum CampaignBatchStatus
    {
        Registered = 'Registered',
        Processing = 'Processing',
        Completed = 'Completed',
        Failed = 'Failed',
    }

    export class BatchStatusChangeEntryDto
    {
        public time: string;
        public status: CampaignBatchStatus;
        public errors?: IReadOnlySet<ErrorDto>;

        public constructor(init?: Partial<BatchStatusChangeEntryDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class CampaignBatchDto implements IHasDatabaseId
    {
        // @DataMember
        public campaignId: string;

        // @DataMember
        public batchId: string;

        // @DataMember
        public startAfter?: string;

        // @DataMember
        public statusHistory: BatchStatusChangeEntryDto[] = [];

        // @DataMember
        public id: string;

        public constructor(init?: Partial<CampaignBatchDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailRecipientDto
    {
        // @DataMember
        public emailAddress: string;

        // @DataMember
        public language?: string;

        // @DataMember
        public timeZoneId?: string;

        // @DataMember
        public userTokenMappings?: IReadOnlySet<TokenMappingDto>;

        public constructor(init?: Partial<EmailRecipientDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailRecipientsDto
    {
        // @DataMember
        public to?: IReadOnlySet<EmailRecipientDto>;

        // @DataMember
        public cc?: IReadOnlySet<EmailRecipientDto>;

        // @DataMember
        public bcc?: IReadOnlySet<EmailRecipientDto>;

        // @DataMember
        public startingAfter?: string;

        // @DataMember
        public hasMore: boolean;

        public constructor(init?: Partial<EmailRecipientsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailCampaignBatchDto extends CampaignBatchDto
    {
        // @DataMember
        public recipients?: EmailRecipientsDto;

        public constructor(init?: Partial<EmailCampaignBatchDto>) { super(init); (Object as any).assign(this, init); }
    }

    export enum CampaignNotificationStatus
    {
        Completed = 'Completed',
        BlockedByUserPreferenceBlockAll = 'BlockedByUserPreferenceBlockAll',
        BlockedByUserPreferenceBlockByTag = 'BlockedByUserPreferenceBlockByTag',
        Failed = 'Failed',
        Viewed = 'Viewed',
        Clicked = 'Clicked',
    }

    export class NotificationStatusChangeEntryDto
    {
        public time: string;
        public status: CampaignNotificationStatus;
        public sourceId?: string;
        public errors?: IReadOnlySet<ErrorDto>;
        public tags?: IReadOnlySet<string>;

        public constructor(init?: Partial<NotificationStatusChangeEntryDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class CampaignBatchNotificationDto implements IHasDatabaseId
    {
        // @DataMember
        public campaignId: string;

        // @DataMember
        public batchId: string;

        // @DataMember
        public notificationId: string;

        // @DataMember
        public refNotificationId?: string;

        // @DataMember
        public subject?: string;

        // @DataMember
        public body?: string;

        // @DataMember
        public model?: { [index:string]: string; };

        // @DataMember
        public statusHistory: IReadOnlySet<NotificationStatusChangeEntryDto>;

        // @DataMember
        public id: string;

        public constructor(init?: Partial<CampaignBatchNotificationDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailCampaignBatchNotificationDto extends CampaignBatchNotificationDto
    {
        // @DataMember
        public recipients: EmailRecipientsDto;

        // @DataMember
        public content?: EmailMessageContentDto;

        public constructor(init?: Partial<EmailCampaignBatchNotificationDto>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class CampaignStatsDto
    {
        // @DataMember
        public batches: number;

        // @DataMember
        public sent: number;

        // @DataMember
        public failed: number;

        // @DataMember
        public successRate: number;

        public constructor(init?: Partial<CampaignStatsDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PushTemplateListProjection extends TemplateListProjection
    {

        public constructor(init?: Partial<PushTemplateListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    export class PushIntegrationListProjection extends IntegrationListProjection
    {
        // @DataMember
        public provider: PushProvider;

        public constructor(init?: Partial<PushIntegrationListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PaymentTriggerProjectionList extends TriggerProjectionList
    {
        // @DataMember
        public type: PaymentTriggerType;

        public constructor(init?: Partial<PaymentTriggerProjectionList>) { super(init); (Object as any).assign(this, init); }
    }

    export class PaymentsIntegrationListProjection extends IntegrationListProjection
    {
        // @DataMember
        public gatewayPlatform: PaymentGatewayPlatform;

        public constructor(init?: Partial<PaymentsIntegrationListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    export class LoggingIntegrationListProjection extends IntegrationListProjection
    {
        // @DataMember
        public provider: LoggingProvider;

        public constructor(init?: Partial<LoggingIntegrationListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    export class LlmIntegrationListProjection extends IntegrationListProjection
    {
        public llmProvider: LlmProvider;
        public baseUrl?: string;
        public defaultModel?: string;

        public constructor(init?: Partial<LlmIntegrationListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    export class McpIntegrationListProjection extends IntegrationListProjection
    {
        public mcpProvider: McpProvider;
        public transport: McpTransport;
        public category?: string;
        public description?: string;
        public icon?: string;

        public constructor(init?: Partial<McpIntegrationListProjection>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SchedulerTaskListProjection implements IHasViewId
    {
        // @DataMember
        public taskId: string;

        // @DataMember
        public name: string;

        // @DataMember
        public cron: string;

        // @DataMember
        public type: SchedulerTaskType;

        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public viewId: string;

        public constructor(init?: Partial<SchedulerTaskListProjection>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ResponseError
    {
        // @DataMember(Order=1)
        public errorCode: string;

        // @DataMember(Order=2)
        public fieldName: string;

        // @DataMember(Order=3)
        public message: string;

        // @DataMember(Order=4)
        public meta?: { [index:string]: string; };

        public constructor(init?: Partial<ResponseError>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ResponseStatus
    {
        // @DataMember(Order=1)
        public errorCode: string;

        // @DataMember(Order=2)
        public message?: string;

        // @DataMember(Order=3)
        public stackTrace?: string;

        // @DataMember(Order=4)
        public errors?: ResponseError[];

        // @DataMember(Order=5)
        public meta?: { [index:string]: string; };

        public constructor(init?: Partial<ResponseStatus>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class UserApiKey
    {
        // @DataMember(Order=1)
        public key?: string;

        // @DataMember(Order=2)
        public keyType?: string;

        // @DataMember(Order=3)
        public expiryDate?: string;

        // @DataMember(Order=4)
        public meta?: { [index:string]: string; };

        public constructor(init?: Partial<UserApiKey>) { (Object as any).assign(this, init); }
    }

    export interface ILlmApiKeyRequest
    {
        apiKey: string;
    }

    export interface IHasViewId
    {
        viewId?: string;
    }

    export interface IBindableContract
    {
    }

    export interface IHasRazorTemplateCode
    {
    }

    export interface IHasDatabaseId
    {
        id?: string;
    }

    export interface IHasDomainEntityId
    {
    }

    export interface IIntegrationIdentification
    {
        integrationId: IntegrationId;
        capability: string;
        isSystemOwned: boolean;
    }

    // @DataContract
    export class EmailSubject
    {

        public constructor(init?: Partial<EmailSubject>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailBody
    {
        // @DataMember
        public code: TemplateCode;

        // @DataMember
        public structure?: string;

        // @DataMember
        public emailTemplateEngine: EmailTemplateEngine;

        public constructor(init?: Partial<EmailBody>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class EmailMessageContent
    {
        // @DataMember(Order=1)
        public subject: EmailSubject;

        // @DataMember(Order=2)
        public body: EmailBody;

        // @DataMember(Order=3)
        public staticAttachments?: FileResourceRef[];

        public constructor(init?: Partial<EmailMessageContent>) { (Object as any).assign(this, init); }
    }

    export class CronExpression
    {
        public value: string;
        public parsed: CronExpression;

        public constructor(init?: Partial<CronExpression>) { (Object as any).assign(this, init); }
    }

    export interface IHasResponsibleUserId
    {
        userId: string;
    }

    export interface ICursorArgs
    {
        field: string;
        order: number;
    }

    export class FileTrigger extends Trigger
    {
        public when: FilesTriggerType;
        public fileResourceRef?: FileResourceRef;

        public constructor(init?: Partial<FileTrigger>) { super(init); (Object as any).assign(this, init); }
    }

    export class PaymentTrigger extends Trigger
    {
        public when: PaymentTriggerType;

        public constructor(init?: Partial<PaymentTrigger>) { super(init); (Object as any).assign(this, init); }
    }

    export class StringField extends JsonSchemaField
    {
        public format?: string;
        public pattern?: string;
        public minLength?: number;
        public maxLength?: number;
        public translateOptions?: IReadOnlyDictionary<string, string>;

        public constructor(init?: Partial<StringField>) { super(init); (Object as any).assign(this, init); }
    }

    export class DecimalField extends JsonSchemaField
    {
        public minimum?: number;
        public maximum?: number;
        public multipleOf?: number;

        public constructor(init?: Partial<DecimalField>) { super(init); (Object as any).assign(this, init); }
    }

    export class CurrencyField extends JsonSchemaField
    {
        public allowedCurrencies?: IReadOnlyList<string>;

        public constructor(init?: Partial<CurrencyField>) { super(init); (Object as any).assign(this, init); }
    }

    export class BooleanField extends JsonSchemaField
    {

        public constructor(init?: Partial<BooleanField>) { super(init); (Object as any).assign(this, init); }
    }

    export class DateField extends JsonSchemaField
    {
        public minimum?: number;
        public maximum?: number;

        public constructor(init?: Partial<DateField>) { super(init); (Object as any).assign(this, init); }
    }

    export class IntegerField extends JsonSchemaField
    {
        public minimum?: number;
        public maximum?: number;

        public constructor(init?: Partial<IntegerField>) { super(init); (Object as any).assign(this, init); }
    }

    export class GeolocationField extends JsonSchemaField
    {
        public allowedTypes?: IReadOnlyList<string>;

        public constructor(init?: Partial<GeolocationField>) { super(init); (Object as any).assign(this, init); }
    }

    export class TagsField extends JsonSchemaField
    {

        public constructor(init?: Partial<TagsField>) { super(init); (Object as any).assign(this, init); }
    }

    export class FileField extends JsonSchemaField
    {
        public storages?: IReadOnlyList<string>;

        public constructor(init?: Partial<FileField>) { super(init); (Object as any).assign(this, init); }
    }

    export class TaxonomySelectionField extends JsonSchemaField
    {
        public taxonomyId?: string;
        public multiple: boolean;

        public constructor(init?: Partial<TaxonomySelectionField>) { super(init); (Object as any).assign(this, init); }
    }

    export class CollectionSelectionField extends JsonSchemaField
    {
        public collectionId?: string;
        public displayField?: string;
        public multiple: boolean;

        public constructor(init?: Partial<CollectionSelectionField>) { super(init); (Object as any).assign(this, init); }
    }

    export class UserSelectionField extends JsonSchemaField
    {
        public multiple: boolean;

        public constructor(init?: Partial<UserSelectionField>) { super(init); (Object as any).assign(this, init); }
    }

    export class RoleSelectionField extends JsonSchemaField
    {
        public multiple: boolean;

        public constructor(init?: Partial<RoleSelectionField>) { super(init); (Object as any).assign(this, init); }
    }

    export class EnumSelectionField extends JsonSchemaField
    {
        public values?: IReadOnlyList<string>;
        public multiple: boolean;

        public constructor(init?: Partial<EnumSelectionField>) { super(init); (Object as any).assign(this, init); }
    }

    export class StringFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public format?: string;

        // @DataMember
        public pattern?: string;

        // @DataMember
        public minLength?: number;

        // @DataMember
        public maxLength?: number;

        // @DataMember
        public translateOptions?: IReadOnlyDictionary<string, string>;

        public constructor(init?: Partial<StringFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class DecimalFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public minimum?: number;

        // @DataMember
        public maximum?: number;

        // @DataMember
        public multipleOf?: number;

        public constructor(init?: Partial<DecimalFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class CurrencyFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public allowedCurrencies?: IReadOnlyList<string>;

        public constructor(init?: Partial<CurrencyFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class BooleanFieldDto extends JsonSchemaFieldDto
    {

        public constructor(init?: Partial<BooleanFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class DateFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public minimum?: number;

        // @DataMember
        public maximum?: number;

        public constructor(init?: Partial<DateFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class IntegerFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public minimum?: number;

        // @DataMember
        public maximum?: number;

        public constructor(init?: Partial<IntegerFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class GeolocationFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public allowedTypes?: IReadOnlyList<string>;

        public constructor(init?: Partial<GeolocationFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class TagsFieldDto extends JsonSchemaFieldDto
    {

        public constructor(init?: Partial<TagsFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class FileFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public storages?: IReadOnlyList<string>;

        public constructor(init?: Partial<FileFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class TaxonomySelectionFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public taxonomyId?: string;

        // @DataMember
        public multiple: boolean;

        public constructor(init?: Partial<TaxonomySelectionFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class CollectionSelectionFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public collectionId?: string;

        // @DataMember
        public displayField?: string;

        // @DataMember
        public multiple: boolean;

        public constructor(init?: Partial<CollectionSelectionFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class UserSelectionFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public multiple: boolean;

        public constructor(init?: Partial<UserSelectionFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class RoleSelectionFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public multiple: boolean;

        public constructor(init?: Partial<RoleSelectionFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class EnumSelectionFieldDto extends JsonSchemaFieldDto
    {
        // @DataMember
        public values?: IReadOnlyList<string>;

        // @DataMember
        public multiple: boolean;

        public constructor(init?: Partial<EnumSelectionFieldDto>) { super(init); (Object as any).assign(this, init); }
    }

    export class EchoResponse
    {
        public containerName?: string;
        public ip: string;
        public release: CodeMashRelease;
        public runtime: CodeMashRuntime;
        public managedServiceHubUrl: string;
        public managedServiceApiUrl: string;
        public hubUrl: string;
        public apiUrl: string;
        public apiVersion: string;
        public hubVersion: string;
        public mjmlUrl: string;
        public license?: CodeMashLicenseFromEndpointDto;
        public askForEnterpriseLicenseEmail?: string;

        public constructor(init?: Partial<EchoResponse>) { (Object as any).assign(this, init); }
    }

    export class GetAccountProfileResponse extends ResponseBase
    {
        public item?: AccountOwnerDto;

        public constructor(init?: Partial<GetAccountProfileResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class EmptyResponse extends ResponseBase
    {

        public constructor(init?: Partial<EmptyResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetAccountStatusResponse extends ResponseBase
    {
        public item?: AccountStatusDto;

        public constructor(init?: Partial<GetAccountStatusResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class IdResponse extends ResponseBase
    {
        // @DataMember
        public id?: string;

        public constructor(init?: Partial<IdResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class CreateStripeCheckoutSessionResponse extends IdResponse
    {

        public constructor(init?: Partial<CreateStripeCheckoutSessionResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class GetStripeBillingPortalUrlResponse extends IdResponse
    {

        public constructor(init?: Partial<GetStripeBillingPortalUrlResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class CreateTeamMemberFromInvitationResponse extends IdResponse
    {
        // @DataMember
        public token?: string;

        public constructor(init?: Partial<CreateTeamMemberFromInvitationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetProjectResponse extends ResponseBase
    {
        public item?: ProjectDto;

        public constructor(init?: Partial<GetProjectResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetProjectsResponse extends ResponseBase
    {
        public list?: ProjectListItemDto[];

        public constructor(init?: Partial<GetProjectsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetAccountRegionsResponse extends ResponseBase
    {
        public items?: ProjectRegionDto[];

        public constructor(init?: Partial<GetAccountRegionsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetProjectTokensResponse extends ResponseBase
    {
        public tokens?: TokenMappingDto[];

        public constructor(init?: Partial<GetProjectTokensResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class CreateAccountResponse extends IdResponse
    {
        // @DataMember
        public token?: string;

        public constructor(init?: Partial<CreateAccountResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetAccountCollaboratorsResponse extends ResponseBase
    {
        public list?: PaginatedResponse<UserDto>;

        public constructor(init?: Partial<GetAccountCollaboratorsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetLicensesResponse extends ResponseBase
    {
        public list?: LicenseDto[];

        public constructor(init?: Partial<GetLicensesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetUserEmailPreferencesResponse extends ResponseBase
    {
        public defaultLanguage: string;
        public projectLanguages: string[] = [];
        public blockAllMarketingMessages: boolean;
        public subscribedTags?: { [index:string]: HashSet<string>; };

        public constructor(init?: Partial<GetUserEmailPreferencesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetMembershipTriggerResponse extends GetTriggerResponse
    {

        public constructor(init?: Partial<GetMembershipTriggerResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class GetMembershipTriggersResponse extends GetTriggersResponse
    {
        // @DataMember
        public list?: PaginatedResponse<MembershipTriggerProjectionList>;

        public constructor(init?: Partial<GetMembershipTriggersResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetRoleResponse extends ResponseBase
    {
        public role?: RoleItemDto;

        public constructor(init?: Partial<GetRoleResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetRolesResponse extends ResponseBase
    {
        public roles: RoleListProjectionDto[] = [];

        public constructor(init?: Partial<GetRolesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPolicyResponse extends ResponseBase
    {
        public policy?: PolicyItemDto;

        public constructor(init?: Partial<GetPolicyResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPoliciesResponse extends ResponseBase
    {
        public policies: PolicyItemDto[] = [];

        public constructor(init?: Partial<GetPoliciesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetMembershipIntegrationResponse extends ResponseBase
    {
        public item?: MembershipIntegrationDto;

        public constructor(init?: Partial<GetMembershipIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetMembershipIntegrationsResponse extends ResponseBase
    {
        public list?: PaginatedResponse<MembershipIntegrationListProjection>;

        public constructor(init?: Partial<GetMembershipIntegrationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetSchemaTriggerResponse extends GetTriggerResponse
    {

        public constructor(init?: Partial<GetSchemaTriggerResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetSchemaTriggersResponse extends GetTriggersResponse
    {
        public list?: PaginatedResponse<SchemaTriggerProjectionList>;

        public constructor(init?: Partial<GetSchemaTriggersResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseTaxonomyResponse extends ResponseBase
    {
        public item?: TaxonomyDto;

        public constructor(init?: Partial<GetDatabaseTaxonomyResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseTaxonomiesResponse extends ResponseBase
    {
        public list?: PaginatedResponse<TaxonomyListProjection>;

        public constructor(init?: Partial<GetDatabaseTaxonomiesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseTaxonomyTermResponse extends ResponseBase
    {
        public item?: TermDto;

        public constructor(init?: Partial<GetDatabaseTaxonomyTermResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseSchemaResponse extends ResponseBase
    {
        public item?: SchemaDto;

        public constructor(init?: Partial<GetDatabaseSchemaResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseSchemasResponse extends ResponseBase
    {
        public list?: PaginatedResponse<SchemaListProjection>;

        public constructor(init?: Partial<GetDatabaseSchemasResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseSchemaDraftResponse extends ResponseBase
    {
        public item?: SchemaDraftDto;

        public constructor(init?: Partial<GetDatabaseSchemaDraftResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseSchemaVersionDiffResponse extends ResponseBase
    {
        public item?: SchemaDiffDto;

        public constructor(init?: Partial<GetDatabaseSchemaVersionDiffResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseSchemaVersionsResponse extends ResponseBase
    {
        public items?: SchemaVersionSummaryDto[];

        public constructor(init?: Partial<GetDatabaseSchemaVersionsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseIntegrationResponse extends ResponseBase
    {
        public item?: DatabaseIntegrationDto;

        public constructor(init?: Partial<GetDatabaseIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseIntegrationsResponse extends ResponseBase
    {
        public defaultIntegrationId?: string;
        public list?: PaginatedResponse<DatabaseIntegrationListProjection>;

        public constructor(init?: Partial<GetDatabaseIntegrationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseAggregateResponse extends ResponseBase
    {
        public item?: MongoDbAggregateDto;

        public constructor(init?: Partial<GetDatabaseAggregateResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetDatabaseAggregatesResponse extends ResponseBase
    {
        public list?: PaginatedResponse<MongoDbAggregateListProjection>;

        public constructor(init?: Partial<GetDatabaseAggregatesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class TestDatabaseAggregateResponse extends ResponseBase
    {
        public result?: Object[];

        public constructor(init?: Partial<TestDatabaseAggregateResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetFilesTriggerResponse extends GetTriggerResponse
    {

        public constructor(init?: Partial<GetFilesTriggerResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetFilesTriggersResponse extends GetTriggersResponse
    {
        public list?: PaginatedResponse<FilesTriggerProjectionList>;

        public constructor(init?: Partial<GetFilesTriggersResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetFilesIntegrationResponse extends ResponseBase
    {
        public item?: FilesIntegrationDto;

        public constructor(init?: Partial<GetFilesIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetFilesIntegrationsResponse extends ResponseBase
    {
        public defaultIntegrationId?: string;
        public list?: PaginatedResponse<FilesIntegrationListProjection>;

        public constructor(init?: Partial<GetFilesIntegrationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailTemplateResponse extends ResponseBase
    {
        public item?: EmailTemplateDto;

        public constructor(init?: Partial<GetEmailTemplateResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailTemplatesResponse extends ResponseBase
    {
        public list?: PaginatedResponse<TemplateListProjection>;

        public constructor(init?: Partial<GetEmailTemplatesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetHtmlFromMjmlResponse extends ResponseBase
    {
        public variables?: string[];
        public htmlFromMjmlResponse?: HtmlFromMjmlResponse;

        public constructor(init?: Partial<GetHtmlFromMjmlResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetSystemEmailTemplateResponse extends ResponseBase
    {
        public item?: SystemEmailTemplateDto;

        public constructor(init?: Partial<GetSystemEmailTemplateResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetSystemEmailTemplatesResponse extends ResponseBase
    {
        public list?: PaginatedResponse<SystemEmailTemplateListProjection>;

        public constructor(init?: Partial<GetSystemEmailTemplatesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailTemplateAvailableTokensResponse extends ResponseBase
    {
        public tokens?: { [index:string]: string[]; };

        public constructor(init?: Partial<GetEmailTemplateAvailableTokensResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailSignatureResponse extends ResponseBase
    {
        public item?: EmailSignatureDto;

        public constructor(init?: Partial<GetEmailSignatureResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailSignaturesResponse extends ResponseBase
    {
        public list?: PaginatedResponse<ListItemWithTranslationsProjection>;

        public constructor(init?: Partial<GetEmailSignaturesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailSettingsResponse extends ResponseBase
    {
        public settings?: EmailSettings;
        public systemTags?: GroupDefinitionDto[];

        public constructor(init?: Partial<GetEmailSettingsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailIntegrationResponse extends ResponseBase
    {
        public item?: EmailIntegrationDto;

        public constructor(init?: Partial<GetEmailIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailIntegrationsResponse extends ResponseBase
    {
        public defaultIntegrationId?: string;
        public list?: PaginatedResponse<EmailIntegrationListProjection>;

        public constructor(init?: Partial<GetEmailIntegrationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TestEmailIntegrationResponse extends ResponseBase
    {
        // @DataMember
        public items?: IReadOnlyList<IntegrationTestResultItemDto>;

        public constructor(init?: Partial<TestEmailIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailFooterResponse extends ResponseBase
    {
        public item?: EmailFooterDto;

        public constructor(init?: Partial<GetEmailFooterResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailFootersResponse extends ResponseBase
    {
        public list?: PaginatedResponse<ListItemWithTranslationsProjection>;

        public constructor(init?: Partial<GetEmailFootersResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailCampaignResponse extends ResponseBase
    {
        public item?: EmailCampaignDto;

        public constructor(init?: Partial<GetEmailCampaignResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailCampaignsResponse extends ResponseBase
    {
        public list?: PaginatedResponse<EmailCampaignListProjection>;

        public constructor(init?: Partial<GetEmailCampaignsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailCampaignBatchesResponse extends ResponseBase
    {
        public list?: PaginatedResponse<EmailCampaignBatchDto>;

        public constructor(init?: Partial<GetEmailCampaignBatchesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailCampaignBatchNotificationResponse extends ResponseBase
    {
        public campaignNotification?: EmailCampaignBatchNotificationDto;

        public constructor(init?: Partial<GetEmailCampaignBatchNotificationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailCampaignBatchNotificationsResponse extends ResponseBase
    {
        public batchStatusHistory?: BatchStatusChangeEntryDto[];
        public list?: PaginatedResponse<EmailCampaignBatchNotificationDto>;

        public constructor(init?: Partial<GetEmailCampaignBatchNotificationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailCampaignStatisticsResponse extends ResponseBase
    {
        public stats?: CampaignStatsDto;

        public constructor(init?: Partial<GetEmailCampaignStatisticsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class PreviewEmailNotificationResponse extends ResponseBase
    {
        public subject?: string;
        public body?: string;

        public constructor(init?: Partial<PreviewEmailNotificationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailCampaignMessageResponse extends ResponseBase
    {
        public emailMessageEntity?: EmailCampaignBatchNotificationDto;

        public constructor(init?: Partial<GetEmailCampaignMessageResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEmailCampaignMessagesResponse extends ResponseBase
    {
        public list?: PaginatedResponse<EmailCampaignBatchNotificationDto>;

        public constructor(init?: Partial<GetEmailCampaignMessagesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPushTemplateResponse extends ResponseBase
    {
        public item?: PushTemplateDto;

        public constructor(init?: Partial<GetPushTemplateResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPushTemplatesResponse extends ResponseBase
    {
        public list?: PaginatedResponse<PushTemplateListProjection>;

        public constructor(init?: Partial<GetPushTemplatesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPushMessageContentTokensResponse extends ResponseBase
    {
        public tokens?: { [index:string]: string[]; };

        public constructor(init?: Partial<GetPushMessageContentTokensResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPushIntegrationResponse extends ResponseBase
    {
        public item?: PushIntegrationDto;

        public constructor(init?: Partial<GetPushIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPushIntegrationsResponse extends ResponseBase
    {
        public defaultIntegrationId?: string;
        public list?: PaginatedResponse<PushIntegrationListProjection>;

        public constructor(init?: Partial<GetPushIntegrationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPaymentsTriggerResponse extends GetTriggerResponse
    {

        public constructor(init?: Partial<GetPaymentsTriggerResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPaymentsTriggersResponse extends GetTriggersResponse
    {
        public list?: PaginatedResponse<PaymentTriggerProjectionList>;

        public constructor(init?: Partial<GetPaymentsTriggersResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPaymentsIntegrationResponse extends ResponseBase
    {
        public item?: PaymentsIntegrationDto;

        public constructor(init?: Partial<GetPaymentsIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetPaymentsIntegrationsResponse extends ResponseBase
    {
        public list?: PaginatedResponse<PaymentsIntegrationListProjection>;

        public constructor(init?: Partial<GetPaymentsIntegrationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TestPaymentsIntegrationResponse extends ResponseBase
    {
        // @DataMember
        public items?: IReadOnlyList<IntegrationTestResultItemDto>;

        public constructor(init?: Partial<TestPaymentsIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetLoggingIntegrationResponse extends ResponseBase
    {
        public item?: LoggingIntegrationDto;

        public constructor(init?: Partial<GetLoggingIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetLoggingIntegrationsResponse extends ResponseBase
    {
        public list?: PaginatedResponse<LoggingIntegrationListProjection>;

        public constructor(init?: Partial<GetLoggingIntegrationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TestLoggingIntegrationResponse extends ResponseBase
    {
        // @DataMember
        public items?: IReadOnlyList<IntegrationTestResultItemDto>;

        public constructor(init?: Partial<TestLoggingIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class AskChatResponse extends ResponseBase
    {
        public result?: string;

        public constructor(init?: Partial<AskChatResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetLlmIntegrationResponse extends ResponseBase
    {
        public item?: LlmIntegrationDto;

        public constructor(init?: Partial<GetLlmIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetLlmIntegrationsResponse extends ResponseBase
    {
        public defaultIntegrationId?: string;
        public list?: PaginatedResponse<LlmIntegrationListProjection>;

        public constructor(init?: Partial<GetLlmIntegrationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TestLlmIntegrationResponse extends ResponseBase
    {
        // @DataMember
        public items?: IReadOnlyList<IntegrationTestResultItemDto>;

        public constructor(init?: Partial<TestLlmIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetMcpIntegrationResponse extends ResponseBase
    {
        public item?: McpIntegrationDto;

        public constructor(init?: Partial<GetMcpIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetMcpIntegrationsResponse extends ResponseBase
    {
        public defaultIntegrationId?: string;
        public list?: PaginatedResponse<McpIntegrationListProjection>;

        public constructor(init?: Partial<GetMcpIntegrationsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetWebhookIntegrationResponse extends ResponseBase
    {
        public item?: WebhookIntegrationDto;

        public constructor(init?: Partial<GetWebhookIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class RevealWebhookIntegrationSecretResponse extends ResponseBase
    {
        public signingSecret?: string;

        public constructor(init?: Partial<RevealWebhookIntegrationSecretResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class RotateWebhookIntegrationSecretResponse extends ResponseBase
    {
        public signingSecret?: string;

        public constructor(init?: Partial<RotateWebhookIntegrationSecretResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class SaveWebhookDestinationResponse extends ResponseBase
    {
        public destinationId?: string;

        public constructor(init?: Partial<SaveWebhookDestinationResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetSchedulerTaskResponse extends ResponseBase
    {
        public item?: SchedulerTaskDto;

        public constructor(init?: Partial<GetSchedulerTaskResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetSchedulerTasksResponse extends ResponseBase
    {
        public list?: PaginatedResponse<SchedulerTaskListProjection>;

        public constructor(init?: Partial<GetSchedulerTasksResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class AuthenticateResponse implements IHasSessionId, IHasBearerToken
    {
        // @DataMember(Order=1)
        public userId?: string;

        // @DataMember(Order=2)
        public sessionId?: string;

        // @DataMember(Order=3)
        public userName?: string;

        // @DataMember(Order=4)
        public displayName?: string;

        // @DataMember(Order=5)
        public referrerUrl?: string;

        // @DataMember(Order=6)
        public bearerToken?: string;

        // @DataMember(Order=7)
        public refreshToken?: string;

        // @DataMember(Order=8)
        public refreshTokenExpiry?: string;

        // @DataMember(Order=9)
        public profileUrl?: string;

        // @DataMember(Order=10)
        public roles?: string[];

        // @DataMember(Order=11)
        public permissions?: string[];

        // @DataMember(Order=12)
        public authProvider?: string;

        // @DataMember(Order=13)
        public responseStatus?: ResponseStatus;

        // @DataMember(Order=14)
        public meta?: { [index:string]: string; };

        public constructor(init?: Partial<AuthenticateResponse>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class GetAccessTokenResponse
    {
        // @DataMember(Order=1)
        public accessToken?: string;

        // @DataMember(Order=2)
        public meta?: { [index:string]: string; };

        // @DataMember(Order=3)
        public responseStatus?: ResponseStatus;

        public constructor(init?: Partial<GetAccessTokenResponse>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class GetApiKeysResponse
    {
        // @DataMember(Order=1)
        public results?: UserApiKey[];

        // @DataMember(Order=2)
        public meta?: { [index:string]: string; };

        // @DataMember(Order=3)
        public responseStatus?: ResponseStatus;

        public constructor(init?: Partial<GetApiKeysResponse>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class RegenerateApiKeysResponse
    {
        // @DataMember(Order=1)
        public results?: UserApiKey[];

        // @DataMember(Order=2)
        public meta?: { [index:string]: string; };

        // @DataMember(Order=3)
        public responseStatus?: ResponseStatus;

        public constructor(init?: Partial<RegenerateApiKeysResponse>) { (Object as any).assign(this, init); }
    }

    // @Route("/internal/_typegen", "GET")
    export class InternalsTypeGen
    {
        public typegen_0_SmtpEmailIntegrationRequest?: SmtpEmailIntegrationRequest;
        public typegen_1_AwsSesEmailIntegrationRequest?: AwsSesEmailIntegrationRequest;
        public typegen_2_SendGridEmailIntegrationRequest?: SendGridEmailIntegrationRequest;
        public typegen_3_MailGunEmailIntegrationRequest?: MailGunEmailIntegrationRequest;
        public typegen_4_EmailToAllUsersDeliverySettingsRequest?: EmailToAllUsersDeliverySettingsRequest;
        public typegen_5_EmailToAccountUsersDeliverySettingsRequest?: EmailToAccountUsersDeliverySettingsRequest;
        public typegen_6_EmailToCollectionRecordsDeliverySettingsRequest?: EmailToCollectionRecordsDeliverySettingsRequest;
        public typegen_7_EmailToEmailsDeliverySettingsRequest?: EmailToEmailsDeliverySettingsRequest;
        public typegen_8_EmailToUsersDeliverySettingsRequest?: EmailToUsersDeliverySettingsRequest;
        public typegen_9_MembershipTriggerRequest?: MembershipTriggerRequest;
        public typegen_10_SchemaTriggerRequest?: SchemaTriggerRequest;
        public typegen_11_FilesTriggerRequest?: FilesTriggerRequest;
        public typegen_12_PaymentTriggerRequest?: PaymentTriggerRequest;
        public typegen_13_MongoDbAtlasServerlessDatabaseIntegrationRequest?: MongoDbAtlasServerlessDatabaseIntegrationRequest;
        public typegen_14_MongoDbAtlasClusterDatabaseIntegrationRequest?: MongoDbAtlasClusterDatabaseIntegrationRequest;
        public typegen_15_MongoDbConnectionStringDatabaseIntegrationRequest?: MongoDbConnectionStringDatabaseIntegrationRequest;
        public typegen_16_GoogleDriveFilesIntegrationRequest?: GoogleDriveFilesIntegrationRequest;
        public typegen_17_FtpFilesIntegrationRequest?: FtpFilesIntegrationRequest;
        public typegen_18_DropBoxFilesIntegrationRequest?: DropBoxFilesIntegrationRequest;
        public typegen_19_AppleICloudFilesIntegrationRequest?: AppleICloudFilesIntegrationRequest;
        public typegen_20_AwsS3FilesIntegrationRequest?: AwsS3FilesIntegrationRequest;
        public typegen_21_GoogleCloudFilesIntegrationRequest?: GoogleCloudFilesIntegrationRequest;
        public typegen_22_AzureBlobFilesIntegrationRequest?: AzureBlobFilesIntegrationRequest;
        public typegen_23_LocalFilesIntegrationRequest?: LocalFilesIntegrationRequest;
        public typegen_24_AmqpLoggingIntegrationRequest?: AmqpLoggingIntegrationRequest;
        public typegen_25_AwsKinesisLoggingIntegrationRequest?: AwsKinesisLoggingIntegrationRequest;
        public typegen_26_AwsS3LoggingIntegrationRequest?: AwsS3LoggingIntegrationRequest;
        public typegen_27_TelegramLoggingIntegrationRequest?: TelegramLoggingIntegrationRequest;
        public typegen_28_NewRelicLoggingIntegrationRequest?: NewRelicLoggingIntegrationRequest;
        public typegen_29_MicrosoftTeamsLoggingIntegrationRequest?: MicrosoftTeamsLoggingIntegrationRequest;
        public typegen_30_MongoDbLoggingIntegrationRequest?: MongoDbLoggingIntegrationRequest;
        public typegen_31_KafkaLoggingIntegrationRequest?: KafkaLoggingIntegrationRequest;
        public typegen_32_PrometheusLoggingIntegrationRequest?: PrometheusLoggingIntegrationRequest;
        public typegen_33_DataDogLoggingIntegrationRequest?: DataDogLoggingIntegrationRequest;
        public typegen_34_InternalKafkaLoggingIntegrationRequest?: InternalKafkaLoggingIntegrationRequest;
        public typegen_35_ElasticSearchLoggingIntegrationRequest?: ElasticSearchLoggingIntegrationRequest;
        public typegen_36_ZabbixLoggingIntegrationRequest?: ZabbixLoggingIntegrationRequest;
        public typegen_37_SplunkLoggingIntegrationRequest?: SplunkLoggingIntegrationRequest;
        public typegen_38_AzureOtelLoggingIntegrationRequest?: AzureOtelLoggingIntegrationRequest;
        public typegen_39_KibanaLoggingIntegrationRequest?: KibanaLoggingIntegrationRequest;
        public typegen_40_LocalFileLoggingIntegrationRequest?: LocalFileLoggingIntegrationRequest;
        public typegen_41_OktaMembershipIntegrationRequest?: OktaMembershipIntegrationRequest;
        public typegen_42_XMembershipIntegrationRequest?: XMembershipIntegrationRequest;
        public typegen_43_GoogleMembershipIntegrationRequest?: GoogleMembershipIntegrationRequest;
        public typegen_44_MicrosoftMembershipIntegrationRequest?: MicrosoftMembershipIntegrationRequest;
        public typegen_45_GitHubMembershipIntegrationRequest?: GitHubMembershipIntegrationRequest;
        public typegen_46_MetaMembershipIntegrationRequest?: MetaMembershipIntegrationRequest;
        public typegen_47_AppleMembershipIntegrationRequest?: AppleMembershipIntegrationRequest;
        public typegen_48_LemonSqueezyPaymentIntegrationRequest?: LemonSqueezyPaymentIntegrationRequest;
        public typegen_49_AdyenPaymentIntegrationRequest?: AdyenPaymentIntegrationRequest;
        public typegen_50_MolliePaymentIntegrationRequest?: MolliePaymentIntegrationRequest;
        public typegen_51_PaddlePaymentIntegrationRequest?: PaddlePaymentIntegrationRequest;
        public typegen_52_PayPalPaymentIntegrationRequest?: PayPalPaymentIntegrationRequest;
        public typegen_53_StripePaymentIntegrationRequest?: StripePaymentIntegrationRequest;
        public typegen_54_AppleInAppPaymentIntegrationRequest?: AppleInAppPaymentIntegrationRequest;
        public typegen_55_GoogleInAppPaymentIntegrationRequest?: GoogleInAppPaymentIntegrationRequest;
        public typegen_56_EdgeWebPushIntegrationRequest?: EdgeWebPushIntegrationRequest;
        public typegen_57_ChromePluginPushIntegrationRequest?: ChromePluginPushIntegrationRequest;
        public typegen_58_SafariPushIntegrationRequest?: SafariPushIntegrationRequest;
        public typegen_59_ChromeWebPushIntegrationRequest?: ChromeWebPushIntegrationRequest;
        public typegen_60_FirefoxWebPushIntegrationRequest?: FirefoxWebPushIntegrationRequest;
        public typegen_61_AndroidFirebasePushIntegrationRequest?: AndroidFirebasePushIntegrationRequest;
        public typegen_62_AppleApnsPushIntegrationRequest?: AppleApnsPushIntegrationRequest;
        public typegen_65_AwsLambdaCodeIntegrationRequest?: AwsLambdaCodeIntegrationRequest;
        public typegen_66_AzureFunctionsCodeIntegrationRequest?: AzureFunctionsCodeIntegrationRequest;
        public typegen_67_GoogleCloudFunctionsCodeIntegrationRequest?: GoogleCloudFunctionsCodeIntegrationRequest;
        public typegen_68_OllamaLlmIntegrationRequest?: OllamaLlmIntegrationRequest;
        public typegen_69_OpenRouterLlmIntegrationRequest?: OpenRouterLlmIntegrationRequest;
        public typegen_70_MistralLlmIntegrationRequest?: MistralLlmIntegrationRequest;
        public typegen_71_GrokLlmIntegrationRequest?: GrokLlmIntegrationRequest;
        public typegen_72_GroqLlmIntegrationRequest?: GroqLlmIntegrationRequest;
        public typegen_73_GoogleLlmIntegrationRequest?: GoogleLlmIntegrationRequest;
        public typegen_74_AnthropicLlmIntegrationRequest?: AnthropicLlmIntegrationRequest;
        public typegen_75_OpenAiLlmIntegrationRequest?: OpenAiLlmIntegrationRequest;
        public typegen_76_PlaywrightMcpIntegrationRequest?: PlaywrightMcpIntegrationRequest;
        public typegen_77_MongoDbMcpIntegrationRequest?: MongoDbMcpIntegrationRequest;
        public typegen_78_GitHubMcpIntegrationRequest?: GitHubMcpIntegrationRequest;
        public typegen_79_StripeMcpIntegrationRequest?: StripeMcpIntegrationRequest;
        public typegen_80_BraveSearchMcpIntegrationRequest?: BraveSearchMcpIntegrationRequest;
        public typegen_81_ObsidianMcpIntegrationRequest?: ObsidianMcpIntegrationRequest;
        public typegen_82_EmailTemplateDto?: EmailTemplateDto;
        public typegen_83_PushTemplateDto?: PushTemplateDto;
        public typegen_84_SmsTemplateDto?: SmsTemplateDto;
        public typegen_85_SystemEmailTemplateDto?: SystemEmailTemplateDto;
        public typegen_86_TriggerActionEmailDto?: TriggerActionEmailDto;
        public typegen_87_TriggerActionPushDto?: TriggerActionPushDto;
        public typegen_88_TriggerActionCodeDto?: TriggerActionCodeDto;
        public typegen_89_TriggerActionWebhookDto?: TriggerActionWebhookDto;
        public typegen_90_EmailToAllUsersDeliverySettingsDto?: EmailToAllUsersDeliverySettingsDto;
        public typegen_91_EmailToAccountUsersDeliverySettingsDto?: EmailToAccountUsersDeliverySettingsDto;
        public typegen_92_EmailToUsersDeliverySettingsDto?: EmailToUsersDeliverySettingsDto;
        public typegen_93_EmailToEmailAddressesDeliverySettingsDto?: EmailToEmailAddressesDeliverySettingsDto;
        public typegen_94_EmailToCollectionRecordsDeliverySettingsDto?: EmailToCollectionRecordsDeliverySettingsDto;
        public typegen_95_PushToAllUsersDeliverySettingsDto?: PushToAllUsersDeliverySettingsDto;
        public typegen_96_PushToUsersDeliverySettingsDto?: PushToUsersDeliverySettingsDto;
        public typegen_97_PushToCollectionRecordsDeliverySettingsDto?: PushToCollectionRecordsDeliverySettingsDto;
        public typegen_98_PushToDevicesDeliverySettingsDto?: PushToDevicesDeliverySettingsDto;
        public typegen_99_SmsToAllUsersDeliverySettingsDto?: SmsToAllUsersDeliverySettingsDto;
        public typegen_100_SmsToUsersDeliverySettingsDto?: SmsToUsersDeliverySettingsDto;
        public typegen_101_SmsToCollectionRecordsDeliverySettingsDto?: SmsToCollectionRecordsDeliverySettingsDto;
        public typegen_102_SmsToPhoneNumbersDeliverySettingsDto?: SmsToPhoneNumbersDeliverySettingsDto;
        public typegen_103_OpenAiLlmIntegrationDto?: OpenAiLlmIntegrationDto;
        public typegen_104_AnthropicLlmIntegrationDto?: AnthropicLlmIntegrationDto;
        public typegen_105_OllamaLlmIntegrationDto?: OllamaLlmIntegrationDto;
        public typegen_106_GroqLlmIntegrationDto?: GroqLlmIntegrationDto;
        public typegen_107_GoogleLlmIntegrationDto?: GoogleLlmIntegrationDto;
        public typegen_108_MistralLlmIntegrationDto?: MistralLlmIntegrationDto;
        public typegen_109_OpenRouterLlmIntegrationDto?: OpenRouterLlmIntegrationDto;
        public typegen_110_GrokLlmIntegrationDto?: GrokLlmIntegrationDto;
        public typegen_111_DockerMcpIntegrationDto?: DockerMcpIntegrationDto;
        public typegen_112_GoogleCalendarMcpIntegrationDto?: GoogleCalendarMcpIntegrationDto;
        public typegen_113_ObsidianMcpIntegrationDto?: ObsidianMcpIntegrationDto;
        public typegen_114_AwsLambdaCrossAccountRoleCodeIntegrationDto?: AwsLambdaCrossAccountRoleCodeIntegrationDto;
        public typegen_115_AwsLambdaIamCodeIntegrationDto?: AwsLambdaIamCodeIntegrationDto;
        public typegen_116_AzureFunctionsCodeIntegrationDto?: AzureFunctionsCodeIntegrationDto;
        public typegen_118_GoogleCloudFunctionsCodeIntegrationDto?: GoogleCloudFunctionsCodeIntegrationDto;
        public typegen_120_AdyenPaymentIntegrationDto?: AdyenPaymentIntegrationDto;
        public typegen_121_AppleInAppPaymentIntegrationDto?: AppleInAppPaymentIntegrationDto;
        public typegen_122_GoogleInAppPaymentIntegrationDto?: GoogleInAppPaymentIntegrationDto;
        public typegen_123_LemonSqueezyPaymentIntegrationDto?: LemonSqueezyPaymentIntegrationDto;
        public typegen_124_MolliePaymentIntegrationDto?: MolliePaymentIntegrationDto;
        public typegen_125_PaddlePaymentIntegrationDto?: PaddlePaymentIntegrationDto;
        public typegen_126_PayPalPaymentIntegrationDto?: PayPalPaymentIntegrationDto;
        public typegen_127_StripePaymentIntegrationDto?: StripePaymentIntegrationDto;
        public typegen_184_ShopifyPaymentIntegrationDto?: ShopifyPaymentIntegrationDto;
        public typegen_185_WooCommercePaymentIntegrationDto?: WooCommercePaymentIntegrationDto;
        public typegen_186_MagentoPaymentIntegrationDto?: MagentoPaymentIntegrationDto;
        public typegen_187_BraintreePaymentIntegrationDto?: BraintreePaymentIntegrationDto;
        public typegen_188_AuthorizeNetPaymentIntegrationDto?: AuthorizeNetPaymentIntegrationDto;
        public typegen_189_CheckOutComPaymentIntegrationDto?: CheckOutComPaymentIntegrationDto;
        public typegen_190_WorldpayPaymentIntegrationDto?: WorldpayPaymentIntegrationDto;
        public typegen_128_AppleSignInMembershipIntegrationDto?: AppleSignInMembershipIntegrationDto;
        public typegen_129_GitHubMembershipIntegrationDto?: GitHubMembershipIntegrationDto;
        public typegen_130_GoogleMembershipIntegrationDto?: GoogleMembershipIntegrationDto;
        public typegen_131_MetaMembershipIntegrationDto?: MetaMembershipIntegrationDto;
        public typegen_132_MicrosoftMembershipIntegrationDto?: MicrosoftMembershipIntegrationDto;
        public typegen_133_OktaMembershipIntegrationDto?: OktaMembershipIntegrationDto;
        public typegen_134_XMembershipIntegrationDto?: XMembershipIntegrationDto;
        public typegen_135_AmqpLoggingIntegrationDto?: AmqpLoggingIntegrationDto;
        public typegen_136_AwsKinesisLoggingIntegrationDto?: AwsKinesisLoggingIntegrationDto;
        public typegen_137_AwsS3CrossAccountRoleLoggingIntegrationDto?: AwsS3CrossAccountRoleLoggingIntegrationDto;
        public typegen_138_AwsS3IamLoggingIntegrationDto?: AwsS3IamLoggingIntegrationDto;
        public typegen_139_AzureOtelLoggingIntegrationDto?: AzureOtelLoggingIntegrationDto;
        public typegen_140_DataDogLoggingIntegrationDto?: DataDogLoggingIntegrationDto;
        public typegen_141_ElasticSearchLoggingIntegrationDto?: ElasticSearchLoggingIntegrationDto;
        public typegen_142_InternalKafkaLoggingIntegrationDto?: InternalKafkaLoggingIntegrationDto;
        public typegen_143_KafkaLoggingIntegrationDto?: KafkaLoggingIntegrationDto;
        public typegen_144_KibanaLoggingIntegrationDto?: KibanaLoggingIntegrationDto;
        public typegen_145_LocalFileLoggingIntegrationDto?: LocalFileLoggingIntegrationDto;
        public typegen_146_MicrosoftTeamsLoggingIntegrationDto?: MicrosoftTeamsLoggingIntegrationDto;
        public typegen_147_MongoDbLoggingIntegrationDto?: MongoDbLoggingIntegrationDto;
        public typegen_148_NewRelicLoggingIntegrationDto?: NewRelicLoggingIntegrationDto;
        public typegen_149_PrometheusLoggingIntegrationDto?: PrometheusLoggingIntegrationDto;
        public typegen_150_SplunkLoggingIntegrationDto?: SplunkLoggingIntegrationDto;
        public typegen_151_TelegramLoggingIntegrationDto?: TelegramLoggingIntegrationDto;
        public typegen_152_ZabbixLoggingIntegrationDto?: ZabbixLoggingIntegrationDto;
        public typegen_191_SlackLoggingIntegrationDto?: SlackLoggingIntegrationDto;
        public typegen_153_AppleICloudFilesIntegrationDto?: AppleICloudFilesIntegrationDto;
        public typegen_154_AwsS3CrossAccountRoleFilesIntegrationDto?: AwsS3CrossAccountRoleFilesIntegrationDto;
        public typegen_155_AwsS3IamFilesIntegrationDto?: AwsS3IamFilesIntegrationDto;
        public typegen_156_AzureBlobFilesIntegrationDto?: AzureBlobFilesIntegrationDto;
        public typegen_157_DropBoxFilesIntegrationDto?: DropBoxFilesIntegrationDto;
        public typegen_158_FtpFilesIntegrationDto?: FtpFilesIntegrationDto;
        public typegen_159_GoogleCloudFilesIntegrationDto?: GoogleCloudFilesIntegrationDto;
        public typegen_160_GoogleDriveFilesIntegrationDto?: GoogleDriveFilesIntegrationDto;
        public typegen_161_LocalFilesIntegrationDto?: LocalFilesIntegrationDto;
        public typegen_162_MongoDbAtlasClusterIntegrationDto?: MongoDbAtlasClusterIntegrationDto;
        public typegen_163_MongoDbAtlasServerlessIntegrationDto?: MongoDbAtlasServerlessIntegrationDto;
        public typegen_164_MongoDbConnectionStringIntegrationDto?: MongoDbConnectionStringIntegrationDto;
        public typegen_165_BirdSmsIntegrationDto?: BirdSmsIntegrationDto;
        public typegen_166_PlivoSmsIntegrationDto?: PlivoSmsIntegrationDto;
        public typegen_167_SinchSmsIntegrationDto?: SinchSmsIntegrationDto;
        public typegen_168_TelesignSmsIntegrationDto?: TelesignSmsIntegrationDto;
        public typegen_169_TelnyxSmsIntegrationDto?: TelnyxSmsIntegrationDto;
        public typegen_170_TwilioSmsIntegrationDto?: TwilioSmsIntegrationDto;
        public typegen_171_VonageSmsIntegrationDto?: VonageSmsIntegrationDto;
        public typegen_172_AndroidFirebasePushIntegrationDto?: AndroidFirebasePushIntegrationDto;
        public typegen_173_AppleApnsPushIntegrationDto?: AppleApnsPushIntegrationDto;
        public typegen_174_ChromePluginPushIntegrationDto?: ChromePluginPushIntegrationDto;
        public typegen_175_ChromeWebPushIntegrationDto?: ChromeWebPushIntegrationDto;
        public typegen_176_EdgeWebPushIntegrationDto?: EdgeWebPushIntegrationDto;
        public typegen_177_FirefoxWebPushIntegrationDto?: FirefoxWebPushIntegrationDto;
        public typegen_178_SafariPushIntegrationDto?: SafariPushIntegrationDto;
        public typegen_179_AwsCrossAccountRoleEmailIntegrationDto?: AwsCrossAccountRoleEmailIntegrationDto;
        public typegen_180_AwsIamEmailIntegrationDto?: AwsIamEmailIntegrationDto;
        public typegen_181_MailGunEmailIntegrationDto?: MailGunEmailIntegrationDto;
        public typegen_182_SendGridEmailIntegrationDto?: SendGridEmailIntegrationDto;
        public typegen_183_SmtpEmailIntegrationDto?: SmtpEmailIntegrationDto;
        public typegen_192_WebhookIntegrationDto?: WebhookIntegrationDto;
        public typegen_193_WebhookDestinationDto?: WebhookDestinationDto;
        public typegen_194_SchedulerTaskDto?: SchedulerTaskDto;
        public typegen_195_MongoDbAggregateDto?: MongoDbAggregateDto;
        public typegen_196_MarketplaceIntegrationDto?: MarketplaceIntegrationDto;
        public typegen_197_MarketplaceFunctionBindingDto?: MarketplaceFunctionBindingDto;
        public typegen_198_MarketplaceListingDto?: MarketplaceListingDto;
        public typegen_199_MarketplaceFunctionDefinitionDto?: MarketplaceFunctionDefinitionDto;
        public typegen_200_MarketplaceFunctionParameterDto?: MarketplaceFunctionParameterDto;
        public typegen_201_MarketplaceMappingDto?: MarketplaceMappingDto;

        public constructor(init?: Partial<InternalsTypeGen>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'InternalsTypeGen'; }
        public getMethod() { return 'GET'; }
        public createResponse() {}
    }

    // @Route("/{version}/echo", "GET")
    export class Echo extends RequestBase implements IReturn<EchoResponse>
    {

        public constructor(init?: Partial<Echo>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'Echo'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EchoResponse(); }
    }

    // @Route("/{version}/account/profile", "GET")
    export class GetAccountProfile extends RequestBase implements IReturn<GetAccountProfileResponse>
    {

        public constructor(init?: Partial<GetAccountProfile>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetAccountProfile'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetAccountProfileResponse(); }
    }

    // @Route("/{version}/account/profile", "PUT")
    // @DataContract
    export class UpdateAccountProfile extends RequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public displayName: string;

        // @DataMember
        public billingEmail?: string;

        // @DataMember
        public operationsEmail?: string;

        // @DataMember
        public securityEmail?: string;

        public constructor(init?: Partial<UpdateAccountProfile>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateAccountProfile'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/account/verify/resend", "GET")
    export class ResendAccountVerificationToken extends RequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<ResendAccountVerificationToken>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ResendAccountVerificationToken'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Get Account Status. */
    // @Route("/{version}/account/status", "GET")
    // @Api(Description="Get Account Status.")
    export class GetAccountStatus extends RequestBase implements IReturn<GetAccountStatusResponse>
    {

        public constructor(init?: Partial<GetAccountStatus>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetAccountStatus'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetAccountStatusResponse(); }
    }

    // @Route("/{version}/account/stripe/create-checkout-session", "POST")
    // @DataContract
    export class CreateStripeCheckoutSession extends RequestBase implements IReturn<CreateStripeCheckoutSessionResponse>
    {
        // @DataMember
        public subscriptionType: SubscriptionType;

        // @DataMember
        public domain?: string;

        // @DataMember
        public projectCap: number;

        // @DataMember
        public newProjectSessionId?: string;

        // @DataMember
        public returnUrl?: string;

        public constructor(init?: Partial<CreateStripeCheckoutSession>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreateStripeCheckoutSession'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new CreateStripeCheckoutSessionResponse(); }
    }

    // @Route("/{version}/account/stripe/get-portal-url", "POST")
    // @DataContract
    export class GetStripeBillingPortalUrl extends RequestBase implements IReturn<GetStripeBillingPortalUrlResponse>
    {
        // @DataMember
        public subscriptionType: SubscriptionType;

        // @DataMember
        public returnUrl?: string;

        public constructor(init?: Partial<GetStripeBillingPortalUrl>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetStripeBillingPortalUrl'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new GetStripeBillingPortalUrlResponse(); }
    }

    // @Route("/{version}/account/team/member", "POST")
    export class CreateTeamMemberFromInvitation extends RequestBase implements IReturn<CreateTeamMemberFromInvitationResponse>
    {
        /** @description Display name of the account holder */
        // @ApiMember(DataType="string", Description="Display name of the account holder", IsRequired=true, Name="DisplayName", ParameterType="form")
        public displayName: string;

        /** @description Token from invitation email */
        // @ApiMember(DataType="string", Description="Token from invitation email", IsRequired=true, Name="Token", ParameterType="form")
        public token: string;

        /** @description Set password for a new account */
        // @ApiMember(DataType="string", Description="Set password for a new account", Format="password", IsRequired=true, Name="Password", ParameterType="form")
        public password: string;

        public constructor(init?: Partial<CreateTeamMemberFromInvitation>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreateTeamMemberFromInvitation'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new CreateTeamMemberFromInvitationResponse(); }
    }

    // @Route("/{version}/account/verify", "GET")
    export class VerifyAccount extends RequestBase implements IReturn<EmptyResponse>, IHasAccountId
    {
        public token: string;
        public accountId: string;

        public constructor(init?: Partial<VerifyAccount>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'VerifyAccount'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/account/projects/{projectId}/notifications/settings/group", "DELETE")
    export class DeleteNotificationsGroup extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public groupTag: string;

        public constructor(init?: Partial<DeleteNotificationsGroup>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteNotificationsGroup'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/account/projects/{projectId}/notifications/settings/tag", "DELETE")
    export class DeleteNotificationsTag extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public tag: string;

        public constructor(init?: Partial<DeleteNotificationsTag>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteNotificationsTag'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/account/projects/{projectId}/notifications/settings/group/tag", "DELETE")
    export class RemoveTagFromNotificationsGroup extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public groupTag: string;
        public tag: string;

        public constructor(init?: Partial<RemoveTagFromNotificationsGroup>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RemoveTagFromNotificationsGroup'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/account/projects/{projectId}/notifications/settings/group", "POST")
    export class SaveNotificationsGroup extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public groupDefinition: GroupDefinitionDto;
        public channel: CommunicationChannel;
        public originChannel?: CommunicationChannel;

        public constructor(init?: Partial<SaveNotificationsGroup>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveNotificationsGroup'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/account/projects/{projectId}/notifications/settings/tag", "POST")
    export class SaveNotificationsTag extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public tagDefinition: TagDefinitionDto;
        public channel?: CommunicationChannel;
        public groupTag?: string;

        public constructor(init?: Partial<SaveNotificationsTag>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveNotificationsTag'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Create a new backend project. */
    // @Route("/{version}/account/projects", "POST")
    // @Api(Description="Create a new backend project.")
    // @DataContract
    export class CreateProjectRequest extends RequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: DatabaseIntegrationRequest;

        // @DataMember
        public projectName: string;

        // @DataMember
        public regions?: string[];

        // @DataMember
        public description?: string;

        public constructor(init?: Partial<CreateProjectRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreateProjectRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/account/projects/{projectId}", "DELETE")
    export class DeleteProject extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DeleteProject>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteProject'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Gets project info. */
    // @Route("/{version}/account/projects/{projectId}", "GET")
    // @Api(Description="Gets project info.")
    export class GetProject extends CodeMashRequestBase implements IReturn<GetProjectResponse>
    {

        public constructor(init?: Partial<GetProject>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetProject'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetProjectResponse(); }
    }

    /** @description Retrieve projects list. */
    // @Route("/{version}/account/projects", "GET")
    // @Api(Description="Retrieve projects list.")
    export class GetProjects extends RequestBase implements IReturn<GetProjectsResponse>
    {

        public constructor(init?: Partial<GetProjects>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetProjects'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetProjectsResponse(); }
    }

    /** @description Get available project regions. */
    // @Route("/{version}/account/regions", "GET")
    // @Api(Description="Get available project regions.")
    export class GetAccountRegions extends RequestBase implements IReturn<GetAccountRegionsResponse>
    {

        public constructor(init?: Partial<GetAccountRegions>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetAccountRegions'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetAccountRegionsResponse(); }
    }

    /** @description Gets project tokens. */
    // @Route("/{version}/account/projects/{projectId}/tokens", "GET")
    // @Api(Description="Gets project tokens.")
    export class GetProjectTokens extends CodeMashRequestBase implements IReturn<GetProjectTokensResponse>
    {
        public initiatorId?: string;
        public recipientId?: string;
        public targetUserId?: string;
        public membershipTriggerOldUserId?: string;
        public membershipTriggerNewUserId?: string;

        public constructor(init?: Partial<GetProjectTokens>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetProjectTokens'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetProjectTokensResponse(); }
    }

    /** @description Updates project accent color */
    // @Route("/{version}/account/projects/{projectId}/settings/accent-color", "PATCH")
    // @Api(Description="Updates project accent color")
    export class UpdateProjectAccentColor extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public color: string;

        public constructor(init?: Partial<UpdateProjectAccentColor>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectAccentColor'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Updates project icon */
    // @Route("/{version}/account/projects/{projectId}/settings/icon", "PATCH")
    // @Api(Description="Updates project icon")
    export class UpdateProjectIcon extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public fileResource?: FileResourceDto;

        public constructor(init?: Partial<UpdateProjectIcon>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectIcon'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Updates project logo */
    // @Route("/{version}/account/projects/{projectId}/settings/logo", "PATCH")
    // @Api(Description="Updates project logo")
    export class UpdateProjectLogo extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public fileResource?: FileResourceDto;

        public constructor(init?: Partial<UpdateProjectLogo>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectLogo'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Updates project main color */
    // @Route("/{version}/account/projects/{projectId}/settings/main-color", "PATCH")
    // @Api(Description="Updates project main color")
    export class UpdateProjectMainColor extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public color: string;

        public constructor(init?: Partial<UpdateProjectMainColor>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectMainColor'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Updates project CORS settings */
    // @Route("/{version}/account/projects/{projectId}/settings/origins", "PATCH")
    // @Api(Description="Updates project CORS settings")
    export class UpdateProjectAllowedOrigins extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public origins?: string[];

        public constructor(init?: Partial<UpdateProjectAllowedOrigins>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectAllowedOrigins'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Update project default language */
    // @Route("/{version}/account/projects/{projectId}/settings/default-language", "PATCH")
    // @Api(Description="Update project default language")
    export class UpdateProjectDefaultLanguage extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public defaultLanguage: string;

        public constructor(init?: Partial<UpdateProjectDefaultLanguage>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectDefaultLanguage'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Updates project description */
    // @Route("/{version}/account/projects/{projectId}/settings/description", "PATCH")
    // @Api(Description="Updates project description")
    export class UpdateProjectDescription extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public description?: string;

        public constructor(init?: Partial<UpdateProjectDescription>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectDescription'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Disables project */
    // @Route("/{version}/account/projects/{projectId}/disable", "PATCH")
    // @Api(Description="Disables project")
    export class DisableProject extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableProject>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableProject'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Enables project */
    // @Route("/{version}/account/projects/{projectId}/enable", "PATCH")
    // @Api(Description="Enables project")
    export class EnableProject extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableProject>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableProject'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Updates project languages */
    // @Route("/{version}/account/projects/{projectId}/settings/languages", "PATCH")
    // @Api(Description="Updates project languages")
    export class UpdateProjectLanguages extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public languages: string[] = [];

        public constructor(init?: Partial<UpdateProjectLanguages>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectLanguages'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Updates project marketing url */
    // @Route("/{version}/account/projects/{projectId}/settings/url", "PATCH")
    // @Api(Description="Updates project marketing url")
    export class UpdateProjectUrl extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public url?: string;

        public constructor(init?: Partial<UpdateProjectUrl>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectUrl'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Updates project name */
    // @Route("/{version}/account/projects/{projectId}/settings/name", "PATCH")
    // @Api(Description="Updates project name")
    export class UpdateProjectName extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public name: string;

        public constructor(init?: Partial<UpdateProjectName>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectName'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Updates project regions */
    // @Route("/{version}/account/projects/{projectId}/settings/regions", "PATCH")
    // @Api(Description="Updates project regions")
    export class UpdateProjectRegions extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public regions?: string[];

        public constructor(init?: Partial<UpdateProjectRegions>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateProjectRegions'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description This API endpoint allows users to create a new CodeMash account. */
    // @Route("/{version}/account", "POST")
    // @Api(Description="This API endpoint allows users to create a new CodeMash account.")
    export class CreateAccount extends RequestBase implements IReturn<CreateAccountResponse>
    {
        /** @description Display name of the account holder */
        // @ApiMember(DataType="string", Description="Display name of the account holder", IsRequired=true, Name="DisplayName", ParameterType="form")
        public displayName: string;

        /** @description Real email of account holder */
        // @ApiMember(DataType="string", Description="Real email of account holder", IsRequired=true, Name="Email", ParameterType="form")
        public email: string;

        /** @description Set password for a new account */
        // @ApiMember(DataType="string", Description="Set password for a new account", Format="password", IsRequired=true, Name="Password", ParameterType="form")
        public password: string;

        public constructor(init?: Partial<CreateAccount>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreateAccount'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new CreateAccountResponse(); }
    }

    // @Route("/{version}/account/collaborators", "GET")
    export class GetAccountCollaborators extends RequestBase implements IReturn<GetAccountCollaboratorsResponse>
    {
        public includeAccountOwner: boolean;
        public userShouldHavePushDevice: boolean;
        public projectId?: string;
        public userIds?: string[];
        public pagingArgs?: PagingArgs;

        public constructor(init?: Partial<GetAccountCollaborators>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetAccountCollaborators'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetAccountCollaboratorsResponse(); }
    }

    // @Route("/{version}/account/team/member/invite", "POST")
    export class SendInviteToTeamMember extends RequestBase implements IReturn<EmptyResponse>
    {
        public email: string;

        public constructor(init?: Partial<SendInviteToTeamMember>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SendInviteToTeamMember'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/account/licenses", "GET")
    export class GetLicenses extends RequestBase implements IReturn<GetLicensesResponse>
    {

        public constructor(init?: Partial<GetLicenses>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetLicenses'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetLicensesResponse(); }
    }

    export class AccountCreated
    {
        public email: EmailAddress;
        public displayName: DisplayName;
        public accountId: AccountId;
        public createdOn: UtcDateTime;

        public constructor(init?: Partial<AccountCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'AccountCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class AccountProfileUpdated
    {
        public displayName: DisplayName;
        public billingEmail?: EmailAddress;
        public operationsEmail?: EmailAddress;
        public securityEmail?: EmailAddress;

        public constructor(init?: Partial<AccountProfileUpdated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'AccountProfileUpdated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class AccountSetAsActive
    {

        public constructor(init?: Partial<AccountSetAsActive>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'AccountSetAsActive'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class AccountValidationTokenIssued
    {
        public expiration: ExpirationToken;

        public constructor(init?: Partial<AccountValidationTokenIssued>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'AccountValidationTokenIssued'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class AccountVerified
    {

        public constructor(init?: Partial<AccountVerified>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'AccountVerified'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class AccountBlocked
    {

        public constructor(init?: Partial<AccountBlocked>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'AccountBlocked'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class AccountSetAsInactive
    {

        public constructor(init?: Partial<AccountSetAsInactive>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'AccountSetAsInactive'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class AccountUnregistered
    {

        public constructor(init?: Partial<AccountUnregistered>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'AccountUnregistered'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class LicenseCreated
    {
        public license: CodeMashLicense;

        public constructor(init?: Partial<LicenseCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LicenseCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectCreated
    {
        public id: ProjectId;
        public name: ProjectName;
        public databaseIntegrationId: IntegrationId;
        public regions?: ProjectRegion[];
        public description?: string;

        public constructor(init?: Partial<ProjectCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectActivated
    {

        public constructor(init?: Partial<ProjectActivated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectActivated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectDisabled
    {

        public constructor(init?: Partial<ProjectDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectDeleted
    {

        public constructor(init?: Partial<ProjectDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectNameChanged
    {
        public projectName: ProjectName;

        public constructor(init?: Partial<ProjectNameChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectNameChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectDescriptionChanged
    {
        public description?: string;

        public constructor(init?: Partial<ProjectDescriptionChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectDescriptionChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectMarketingUrlChanged
    {
        public url?: DomainUrl;

        public constructor(init?: Partial<ProjectMarketingUrlChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectMarketingUrlChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectAllowedOriginsChanged
    {
        public origins?: DomainUrl[];

        public constructor(init?: Partial<ProjectAllowedOriginsChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectAllowedOriginsChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectDefaultLanguageChanged
    {
        public language: Language;

        public constructor(init?: Partial<ProjectDefaultLanguageChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectDefaultLanguageChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectLanguagesChanged
    {
        public languages: Language[] = [];

        public constructor(init?: Partial<ProjectLanguagesChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectLanguagesChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectLogoChanged
    {
        public logo?: ProjectLogo;

        public constructor(init?: Partial<ProjectLogoChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectLogoChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectIconChanged
    {
        public icon?: ProjectIcon;

        public constructor(init?: Partial<ProjectIconChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectIconChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectMainColorChanged
    {
        public color: BrandColor;

        public constructor(init?: Partial<ProjectMainColorChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectMainColorChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectAccentColorChanged
    {
        public color: BrandColor;

        public constructor(init?: Partial<ProjectAccentColorChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectAccentColorChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectRegionsChanged
    {
        public regions?: ProjectRegion[];

        public constructor(init?: Partial<ProjectRegionsChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectRegionsChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectEnabled
    {

        public constructor(init?: Partial<ProjectEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectCommunicationSet
    {
        public projectCommunication: ProjectCommunication;

        public constructor(init?: Partial<ProjectCommunicationSet>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectCommunicationSet'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectTimeZoneChanged
    {
        public timeZone?: TimeZone;

        public constructor(init?: Partial<ProjectTimeZoneChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectTimeZoneChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectPaymentZonesChanged
    {
        public paymentZones?: TimeZone[];

        public constructor(init?: Partial<ProjectPaymentZonesChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectPaymentZonesChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectCommunicationGroupSaved
    {
        public group: GroupDefinition;
        public channel: CommunicationChannel;
        public originChannel?: CommunicationChannel;

        public constructor(init?: Partial<ProjectCommunicationGroupSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectCommunicationGroupSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectCommunicationTagFromGroupDeleted
    {
        public groupTag: Tag;
        public removedTag: Tag;

        public constructor(init?: Partial<ProjectCommunicationTagFromGroupDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectCommunicationTagFromGroupDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectCommunicationGroupDeleted
    {
        public groupTag: Tag;

        public constructor(init?: Partial<ProjectCommunicationGroupDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectCommunicationGroupDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectCommunicationTagSaved
    {
        public tag: TagDefinition;
        public groupTag?: Tag;
        public channel?: CommunicationChannel;

        public constructor(init?: Partial<ProjectCommunicationTagSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectCommunicationTagSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class ProjectCommunicationTagDeleted
    {
        public tag: Tag;

        public constructor(init?: Partial<ProjectCommunicationTagDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'ProjectCommunicationTagDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class CustomerCreated
    {
        public customerId: ExternalCustomerId;

        public constructor(init?: Partial<CustomerCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'CustomerCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SubscriptionChanged
    {
        public subscription: CodeMashManagedServiceSubscription;

        public constructor(init?: Partial<SubscriptionChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SubscriptionChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SubscriptionCanceled
    {
        public customerId: ExternalCustomerId;
        public subscriptionId: string;

        public constructor(init?: Partial<SubscriptionCanceled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SubscriptionCanceled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    // @Route("/{version}/membership/disable", "GET")
    export class DisableMembership extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableMembership>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableMembership'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/membership/enable", "GET")
    export class EnableMembership extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableMembership>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableMembership'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/user/preferences", "GET")
    export class GetUserNotificationPreferences extends CodeMashRequestBase implements IReturn<GetUserEmailPreferencesResponse>
    {
        public userId: string;

        public constructor(init?: Partial<GetUserNotificationPreferences>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetUserNotificationPreferences'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetUserEmailPreferencesResponse(); }
    }

    // @Route("/{version}/notifications/user/preferences", "PUT")
    export class UpdateUserNotificationsPreferences extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public userId: string;
        public blockAllMarketingMessages: boolean;
        public subscribedToTags?: { [index:string]: HashSet<string>; };

        public constructor(init?: Partial<UpdateUserNotificationsPreferences>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateUserNotificationsPreferences'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/membership/triggers/{triggerId}", "DELETE")
    // @Route("/{version}/triggers", "DELETE")
    // @DataContract
    export class DeleteMembershipTrigger extends DeleteTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DeleteMembershipTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteMembershipTrigger'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/membership/triggers/{triggerId}/disable", "PATCH")
    // @Route("/{version}/triggers/disable", "PUT")
    // @DataContract
    export class DisableMembershipTrigger extends DisableTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableMembershipTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableMembershipTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/membership/triggers/{triggerId}/enable", "PATCH")
    // @Route("/{version}/triggers/enable", "PUT")
    // @DataContract
    export class EnableMembershipTrigger extends EnableTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableMembershipTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableMembershipTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Gets membership trigger by specified Id */
    // @Route("/{version}/membership/triggers/{id}", "GET")
    // @Api(Description="Gets membership trigger by specified Id")
    export class GetMembershipTrigger extends GetTrigger implements IReturn<GetMembershipTriggerResponse>
    {

        public constructor(init?: Partial<GetMembershipTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetMembershipTrigger'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetMembershipTriggerResponse(); }
    }

    /** @description Gets membership triggers */
    // @Route("/{version}/membership/triggers", "GET")
    // @Api(Description="Gets membership triggers")
    export class GetMembershipTriggers extends GetTriggers implements IReturn<GetMembershipTriggersResponse>
    {

        public constructor(init?: Partial<GetMembershipTriggers>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetMembershipTriggers'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetMembershipTriggersResponse(); }
    }

    // @Route("/{version}/membership/triggers", "POST")
    // @Route("/{version}/triggers", "POST")
    // @DataContract
    export class SaveMembershipTrigger extends SaveTrigger implements IReturn<IdResponse>
    {

        public constructor(init?: Partial<SaveMembershipTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveMembershipTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Create a new custom role for project. */
    // @Route("/{version}/membership/roles", "POST")
    // @Api(Description="Create a new custom role for project.")
    export class CreateRole extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        public roleName: string;
        public description?: string;
        public policies?: string[];

        public constructor(init?: Partial<CreateRole>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreateRole'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Deletes custom role from project. */
    // @Route("/{version}/membership/roles", "DELETE")
    // @Api(Description="Deletes custom role from project.")
    export class DeleteRole extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteRole>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteRole'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Gets project role details. */
    // @Route("/{version}/membership/roles/{Id}", "GET")
    // @Api(Description="Gets project role details.")
    export class GetRole extends CodeMashRequestBase implements IReturn<GetRoleResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetRole>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetRole'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetRoleResponse(); }
    }

    /** @description Gets project roles. */
    // @Route("/{version}/membership/roles", "GET")
    // @Api(Description="Gets project roles.")
    export class GetRoles extends CodeMashRequestBase implements IReturn<GetRolesResponse>
    {

        public constructor(init?: Partial<GetRoles>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetRoles'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetRolesResponse(); }
    }

    /** @description Updates role policies */
    // @Route("/{version}/membership/roles", "PATCH")
    // @Api(Description="Updates role policies")
    export class UpdateRolePolicies extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;
        public roleName: string;
        public description?: string;
        public policies?: string[];

        public constructor(init?: Partial<UpdateRolePolicies>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateRolePolicies'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Create a new custom policy for project. */
    // @Route("/{version}/membership/policies", "POST")
    // @Api(Description="Create a new custom policy for project.")
    export class CreatePolicy extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        public policyName: string;
        public description?: string;
        public policyDocumentJson?: string;

        public constructor(init?: Partial<CreatePolicy>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreatePolicy'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Deletes custom policy from project. */
    // @Route("/{version}/membership/policies", "DELETE")
    // @Api(Description="Deletes custom policy from project.")
    export class DeletePolicy extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeletePolicy>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeletePolicy'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Gets project policy details. */
    // @Route("/{version}/membership/policies/{Id}", "GET")
    // @Api(Description="Gets project policy details.")
    export class GetPolicy extends CodeMashRequestBase implements IReturn<GetPolicyResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetPolicy>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPolicy'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPolicyResponse(); }
    }

    /** @description Gets project policies. */
    // @Route("/{version}/membership/policies", "GET")
    // @Api(Description="Gets project policies.")
    export class GetPolicies extends CodeMashRequestBase implements IReturn<GetPoliciesResponse>
    {

        public constructor(init?: Partial<GetPolicies>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPolicies'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPoliciesResponse(); }
    }

    /** @description Updates a custom policy for project. */
    // @Route("/{version}/membership/policies", "PUT")
    // @Api(Description="Updates a custom policy for project.")
    export class UpdatePolicy extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        public id: string;
        public policyName: string;
        public description?: string;
        public policyDocumentJson?: string;

        public constructor(init?: Partial<UpdatePolicy>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdatePolicy'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/membership/integrations/{Id}", "DELETE")
    export class DeleteMembershipIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteMembershipIntegrationRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/membership/integrations/{Id}/disable", "PUT")
    export class DisableMembershipIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisableMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableMembershipIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/membership/integrations/{Id}/enable", "PUT")
    export class EnableMembershipIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnableMembershipIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableMembershipIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/membership/integrations/{id}", "GET")
    export class GetMembershipIntegration extends CodeMashRequestBase implements IReturn<GetMembershipIntegrationResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetMembershipIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetMembershipIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetMembershipIntegrationResponse(); }
    }

    // @Route("/{version}/membership/integrations", "GET")
    export class GetMembershipIntegrations extends CodeMashListPaginationRequestBase implements IReturn<GetMembershipIntegrationsResponse>
    {

        public constructor(init?: Partial<GetMembershipIntegrations>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetMembershipIntegrations'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetMembershipIntegrationsResponse(); }
    }

    // @Route("/{version}/membership/integrations", "POST")
    // @DataContract
    export class SaveMembershipIntegration extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: MembershipIntegrationRequest;

        public constructor(init?: Partial<SaveMembershipIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveMembershipIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/membership/integrations/{Id}/default", "PUT")
    export class SetMembershipIntegrationAsDefaultRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<SetMembershipIntegrationAsDefaultRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SetMembershipIntegrationAsDefaultRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    export class MembershipIntegrationSaved
    {
        public integration: MembershipIntegration;

        public constructor(init?: Partial<MembershipIntegrationSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipIntegrationSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipIntegrationTested
    {
        public id: IntegrationId;
        public succeeded: boolean;
        public errorMessages: IReadOnlyList<string>;
        public testedAtUtc: string;

        public constructor(init?: Partial<MembershipIntegrationTested>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipIntegrationTested'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipIntegrationRenamed
    {
        public id: IntegrationId;
        public name: DisplayName;

        public constructor(init?: Partial<MembershipIntegrationRenamed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipIntegrationRenamed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipIntegrationDeleted
    {
        public id: IntegrationId;

        public constructor(init?: Partial<MembershipIntegrationDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipIntegrationDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipIntegrationSetAsDefault
    {
        public id: IntegrationId;

        public constructor(init?: Partial<MembershipIntegrationSetAsDefault>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipIntegrationSetAsDefault'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipIntegrationEnabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<MembershipIntegrationEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipIntegrationEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipIntegrationDisabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<MembershipIntegrationDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipIntegrationDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipEstablished
    {

        public constructor(init?: Partial<MembershipEstablished>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipEstablished'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipEnabled
    {

        public constructor(init?: Partial<MembershipEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipDisabled
    {

        public constructor(init?: Partial<MembershipDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SetUserRegistersAsRole
    {
        public projectId?: ProjectId;
        public role: RoleName;

        public constructor(init?: Partial<SetUserRegistersAsRole>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SetUserRegistersAsRole'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PolicyCreated
    {
        public policy: MembershipPolicy;

        public constructor(init?: Partial<PolicyCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PolicyCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PolicyUpdated
    {
        public policy: MembershipPolicy;

        public constructor(init?: Partial<PolicyUpdated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PolicyUpdated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PolicyDeleted
    {
        public policyId: PolicyId;

        public constructor(init?: Partial<PolicyDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PolicyDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class RoleCreated
    {
        public role: MembershipRole;

        public constructor(init?: Partial<RoleCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'RoleCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class RoleUpdated
    {
        public role: MembershipRole;

        public constructor(init?: Partial<RoleUpdated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'RoleUpdated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class RoleDeleted
    {
        public roleId: RoleId;

        public constructor(init?: Partial<RoleDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'RoleDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipTriggerSaved
    {
        public trigger: MembershipTrigger;

        public constructor(init?: Partial<MembershipTriggerSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipTriggerSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipTriggerEnabled extends TriggerByIdEventBase
    {

        public constructor(init?: Partial<MembershipTriggerEnabled>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipTriggerEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipTriggerDisabled extends TriggerByIdEventBase
    {

        public constructor(init?: Partial<MembershipTriggerDisabled>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipTriggerDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MembershipTriggerDeleted extends TriggerByIdEventBase
    {

        public constructor(init?: Partial<MembershipTriggerDeleted>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'MembershipTriggerDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    // @Route("/{version}/database/disable", "GET")
    export class DisableDatabase extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableDatabase>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableDatabase'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/enable", "GET")
    export class EnableDatabase extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableDatabase>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableDatabase'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/schemas/triggers/{triggerId}", "DELETE")
    // @Route("/{version}/triggers", "DELETE")
    // @DataContract
    export class DeleteSchemaTrigger extends DeleteTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DeleteSchemaTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteSchemaTrigger'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/schemas/triggers/{triggerId}/disable", "PATCH")
    // @Route("/{version}/triggers/disable", "PUT")
    // @DataContract
    export class DisableSchemaTrigger extends DisableTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableSchemaTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableSchemaTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/schemas/triggers/{triggerId}/enable", "PATCH")
    // @Route("/{version}/triggers/enable", "PUT")
    // @DataContract
    export class EnableSchemaTrigger extends EnableTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableSchemaTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableSchemaTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Gets database trigger by specified Id */
    // @Route("/{version}/database/schemas/triggers/{id}", "GET")
    // @Api(Description="Gets database trigger by specified Id")
    export class GetSchemaTrigger extends GetTrigger implements IReturn<GetSchemaTriggerResponse>
    {

        public constructor(init?: Partial<GetSchemaTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetSchemaTrigger'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetSchemaTriggerResponse(); }
    }

    /** @description Gets database triggers */
    // @Route("/{version}/database/schemas/triggers", "GET")
    // @Api(Description="Gets database triggers")
    export class GetSchemaTriggers extends GetTriggers implements IReturn<GetSchemaTriggersResponse>
    {
        public schemaId: string;

        public constructor(init?: Partial<GetSchemaTriggers>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetSchemaTriggers'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetSchemaTriggersResponse(); }
    }

    // @Route("/{version}/database/schemas/triggers", "POST")
    // @Route("/{version}/triggers", "POST")
    // @DataContract
    export class SaveSchemaTrigger extends SaveTrigger implements IReturn<IdResponse>
    {

        public constructor(init?: Partial<SaveSchemaTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveSchemaTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/database/taxonomies/{Id}", "DELETE")
    export class DeleteDatabaseTaxonomyRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteDatabaseTaxonomyRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteDatabaseTaxonomyRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/taxonomies/{id}", "GET")
    export class GetDatabaseTaxonomy extends CodeMashRequestBase implements IReturn<GetDatabaseTaxonomyResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetDatabaseTaxonomy>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseTaxonomy'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseTaxonomyResponse(); }
    }

    // @Route("/{version}/database/taxonomies", "GET")
    export class GetDatabaseTaxonomies extends CodeMashListPaginationRequestBase implements IReturn<GetDatabaseTaxonomiesResponse>
    {
        public pagingArgs?: PagingArgs;

        public constructor(init?: Partial<GetDatabaseTaxonomies>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseTaxonomies'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseTaxonomiesResponse(); }
    }

    // @Route("/{version}/database/taxonomies", "POST")
    // @DataContract
    export class SaveDatabaseTaxonomyRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public viewId?: string;

        // @DataMember
        public taxonomyName: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public termsMetaDataSchema?: string;

        // @DataMember
        public termsMetaVisualSchema?: string;

        // @DataMember
        public parentId?: string;

        // @DataMember
        public dependencies?: string[];

        public constructor(init?: Partial<SaveDatabaseTaxonomyRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveDatabaseTaxonomyRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}", "DELETE")
    // @DataContract
    export class DeleteDatabaseTaxonomyTermRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public taxonomyId: string;

        // @DataMember
        public id: string;

        // @DataMember
        public databaseIntegrationId: string;

        public constructor(init?: Partial<DeleteDatabaseTaxonomyTermRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteDatabaseTaxonomyTermRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/many", "DELETE")
    // @DataContract
    export class DeleteManyDatabaseTaxonomyTermsRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public taxonomyId: string;

        // @DataMember
        public databaseIntegrationId: string;

        // @DataMember
        public filter: string;

        public constructor(init?: Partial<DeleteManyDatabaseTaxonomyTermsRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteManyDatabaseTaxonomyTermsRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}", "GET")
    // @DataContract
    export class GetDatabaseTaxonomyTermRequest extends CodeMashRequestBase implements IReturn<GetDatabaseTaxonomyTermResponse>
    {
        // @DataMember
        public taxonomyId: string;

        // @DataMember
        public id: string;

        // @DataMember
        public databaseIntegrationId: string;

        public constructor(init?: Partial<GetDatabaseTaxonomyTermRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseTaxonomyTermRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseTaxonomyTermResponse(); }
    }

    // @Route("/{version}/database/taxonomies/{TaxonomyId}/terms", "POST")
    // @DataContract
    export class SaveDatabaseTaxonomyTermRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public taxonomyId: string;

        // @DataMember
        public databaseIntegrationId: string;

        // @DataMember
        public document: string;

        public constructor(init?: Partial<SaveDatabaseTaxonomyTermRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveDatabaseTaxonomyTermRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/database/taxonomies/{TaxonomyId}/terms/{Id}", "PUT")
    // @DataContract
    export class UpdateDatabaseTaxonomyTermRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public taxonomyId: string;

        // @DataMember
        public id: string;

        // @DataMember
        public databaseIntegrationId: string;

        // @DataMember
        public update: string;

        public constructor(init?: Partial<UpdateDatabaseTaxonomyTermRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateDatabaseTaxonomyTermRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/schemas/{Id}", "DELETE")
    export class DeleteDatabaseSchemaRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteDatabaseSchemaRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteDatabaseSchemaRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/schemas/{Id}/draft", "DELETE")
    // @DataContract
    export class DiscardDatabaseSchemaDraftRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public id: string;

        public constructor(init?: Partial<DiscardDatabaseSchemaDraftRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DiscardDatabaseSchemaDraftRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/schemas/{id}", "GET")
    // @DataContract
    export class GetDatabaseSchema extends CodeMashRequestBase implements IReturn<GetDatabaseSchemaResponse>
    {
        // @DataMember
        public id: string;

        // @DataMember(Name="version")
        // @ApiMember(DataType="integer", Name="version", ParameterType="query")
        public schemaVersion?: number;

        public constructor(init?: Partial<GetDatabaseSchema>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseSchema'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseSchemaResponse(); }
    }

    // @Route("/{version}/database/schemas", "GET")
    export class GetDatabaseSchemas extends CodeMashListPaginationRequestBase implements IReturn<GetDatabaseSchemasResponse>
    {
        public pagingArgs?: PagingArgs;

        public constructor(init?: Partial<GetDatabaseSchemas>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseSchemas'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseSchemasResponse(); }
    }

    // @Route("/{version}/database/schemas/{Id}/draft", "GET")
    // @DataContract
    export class GetDatabaseSchemaDraft extends CodeMashRequestBase implements IReturn<GetDatabaseSchemaDraftResponse>
    {
        // @DataMember
        public id: string;

        public constructor(init?: Partial<GetDatabaseSchemaDraft>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseSchemaDraft'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseSchemaDraftResponse(); }
    }

    // @Route("/{version}/database/schemas/{Id}/versions/diff", "GET")
    // @DataContract
    export class GetDatabaseSchemaVersionDiff extends CodeMashRequestBase implements IReturn<GetDatabaseSchemaVersionDiffResponse>
    {
        // @DataMember
        public id: string;

        // @DataMember
        public fromVersion: number;

        // @DataMember
        public toVersion: number;

        public constructor(init?: Partial<GetDatabaseSchemaVersionDiff>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseSchemaVersionDiff'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseSchemaVersionDiffResponse(); }
    }

    // @Route("/{version}/database/schemas/{Id}/versions", "GET")
    // @DataContract
    export class GetDatabaseSchemaVersions extends CodeMashRequestBase implements IReturn<GetDatabaseSchemaVersionsResponse>
    {
        // @DataMember
        public id: string;

        public constructor(init?: Partial<GetDatabaseSchemaVersions>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseSchemaVersions'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseSchemaVersionsResponse(); }
    }

    // @Route("/{version}/database/schemas/{Id}/publish", "POST")
    // @DataContract
    export class PublishDatabaseSchemaRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public id: string;

        public constructor(init?: Partial<PublishDatabaseSchemaRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'PublishDatabaseSchemaRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/schemas/{Id}/rename", "PUT")
    // @DataContract
    export class RenameDatabaseSchemaRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public id: string;

        // @DataMember
        public title: string;

        // @DataMember
        public renameUniqueName: boolean;

        public constructor(init?: Partial<RenameDatabaseSchemaRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RenameDatabaseSchemaRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/schemas", "POST")
    // @DataContract
    export class SaveDatabaseSchemaRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public viewId?: string;

        // @DataMember
        public schemaName: string;

        // @DataMember
        public dataSchema?: string;

        // @DataMember
        public visualSchema?: string;

        // @DataMember
        public settings?: SchemaSettingsDto;

        public constructor(init?: Partial<SaveDatabaseSchemaRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveDatabaseSchemaRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/database/schemas/{Id}/draft", "PUT")
    // @DataContract
    export class UpdateDatabaseSchemaDraftRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public id: string;

        // @DataMember
        public dataSchema?: string;

        // @DataMember
        public visualSchema?: string;

        public constructor(init?: Partial<UpdateDatabaseSchemaDraftRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateDatabaseSchemaDraftRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/schemas/{Id}/settings", "PUT")
    // @DataContract
    export class UpdateDatabaseSchemaSettingsRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public settings: SchemaSettingsDto;

        public constructor(init?: Partial<UpdateDatabaseSchemaSettingsRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateDatabaseSchemaSettingsRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/integrations/{Id}", "DELETE")
    export class DeleteDatabaseIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteDatabaseIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteDatabaseIntegrationRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/integrations/{Id}/disable", "PUT")
    export class DisableDatabaseIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisableDatabaseIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableDatabaseIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/integrations/{Id}/enable", "PUT")
    export class EnableDatabaseIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnableDatabaseIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableDatabaseIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/integrations/{id}", "GET")
    export class GetDatabaseIntegration extends CodeMashRequestBase implements IReturn<GetDatabaseIntegrationResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetDatabaseIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseIntegrationResponse(); }
    }

    // @Route("/{version}/database/integrations", "GET")
    export class GetDatabaseIntegrations extends CodeMashListPaginationRequestBase implements IReturn<GetDatabaseIntegrationsResponse>
    {
        public pagingArgs?: PagingArgs;

        public constructor(init?: Partial<GetDatabaseIntegrations>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseIntegrations'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseIntegrationsResponse(); }
    }

    // @Route("/{version}/database/integrations", "POST")
    // @DataContract
    export class SaveDatabaseIntegration extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: DatabaseIntegrationRequest;

        public constructor(init?: Partial<SaveDatabaseIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveDatabaseIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/database/integrations/{Id}/default", "PUT")
    export class SetDatabaseIntegrationAsDefaultRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<SetDatabaseIntegrationAsDefaultRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SetDatabaseIntegrationAsDefaultRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/aggregates/{Id}", "DELETE")
    // @DataContract
    export class DeleteDatabaseAggregateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public id: string;

        // @DataMember
        public schemaId: string;

        public constructor(init?: Partial<DeleteDatabaseAggregateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteDatabaseAggregateRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/database/aggregates/{Id}", "GET")
    export class GetDatabaseAggregate extends CodeMashRequestBase implements IReturn<GetDatabaseAggregateResponse>
    {
        public id: string;
        public schemaId: string;

        public constructor(init?: Partial<GetDatabaseAggregate>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseAggregate'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseAggregateResponse(); }
    }

    // @Route("/{version}/database/aggregates", "GET")
    export class GetDatabaseAggregates extends CodeMashListPaginationRequestBase implements IReturn<GetDatabaseAggregatesResponse>
    {
        public schemaId: string;
        public pagingArgs?: PagingArgs;

        public constructor(init?: Partial<GetDatabaseAggregates>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseAggregates'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseAggregatesResponse(); }
    }

    // @Route("/{version}/database/aggregates", "POST")
    // @DataContract
    export class SaveDatabaseAggregateRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public viewId?: string;

        // @DataMember
        public schemaId: string;

        // @DataMember
        public displayName: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public pipeline: string;

        public constructor(init?: Partial<SaveDatabaseAggregateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveDatabaseAggregateRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/database/aggregates/test", "POST")
    // @DataContract
    export class TestDatabaseAggregateRequest extends CodeMashRequestBase implements IReturn<TestDatabaseAggregateResponse>
    {
        // @DataMember
        public databaseIntegrationId: string;

        // @DataMember
        public collectionName: string;

        // @DataMember
        public pipeline: string;

        // @DataMember
        public tokens?: { [index:string]: string; };

        public constructor(init?: Partial<TestDatabaseAggregateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'TestDatabaseAggregateRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new TestDatabaseAggregateResponse(); }
    }

    export class MongoDbAggregateCreated
    {
        public aggregate: MongoDbAggregate;

        public constructor(init?: Partial<MongoDbAggregateCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MongoDbAggregateCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MongoDbAggregateUpdated
    {
        public aggregate: MongoDbAggregate;

        public constructor(init?: Partial<MongoDbAggregateUpdated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MongoDbAggregateUpdated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MongoDbAggregateDeleted
    {
        public schemaId: SchemaId;
        public id: MongoDbAggregateId;

        public constructor(init?: Partial<MongoDbAggregateDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MongoDbAggregateDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseEstablished
    {

        public constructor(init?: Partial<DatabaseEstablished>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseEstablished'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseEnabled
    {

        public constructor(init?: Partial<DatabaseEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseDisabled
    {

        public constructor(init?: Partial<DatabaseDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseIntegrationSaved
    {
        public integration: DatabaseIntegration;

        public constructor(init?: Partial<DatabaseIntegrationSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseIntegrationSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseIntegrationTested
    {
        public id: IntegrationId;
        public succeeded: boolean;
        public errorMessages: IReadOnlyList<string>;
        public testedAtUtc: string;

        public constructor(init?: Partial<DatabaseIntegrationTested>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseIntegrationTested'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseIntegrationRenamed
    {
        public id: IntegrationId;
        public name: DisplayName;

        public constructor(init?: Partial<DatabaseIntegrationRenamed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseIntegrationRenamed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseIntegrationSetAsDefault
    {
        public id: IntegrationId;

        public constructor(init?: Partial<DatabaseIntegrationSetAsDefault>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseIntegrationSetAsDefault'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseIntegrationDeleted
    {
        public id: IntegrationId;

        public constructor(init?: Partial<DatabaseIntegrationDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseIntegrationDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseIntegrationEnabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<DatabaseIntegrationEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseIntegrationEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class DatabaseIntegrationDisabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<DatabaseIntegrationDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'DatabaseIntegrationDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaCreated
    {
        public schema: Schema;

        public constructor(init?: Partial<SchemaCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaDraftUpdated
    {
        public id: SchemaId;
        public draft: SchemaDraft;

        public constructor(init?: Partial<SchemaDraftUpdated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaDraftUpdated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaDraftDiscarded
    {
        public id: SchemaId;

        public constructor(init?: Partial<SchemaDraftDiscarded>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaDraftDiscarded'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaVersionPublished
    {
        public id: SchemaId;
        public version: PublishedSchemaVersion;
        public diff: SchemaDiff;

        public constructor(init?: Partial<SchemaVersionPublished>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaVersionPublished'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaSettingsUpdated
    {
        public id: SchemaId;
        public settings: SchemaSettings;

        public constructor(init?: Partial<SchemaSettingsUpdated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaSettingsUpdated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaDeleted
    {
        public id: SchemaId;

        public constructor(init?: Partial<SchemaDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaRenamed
    {
        public schemaId: SchemaId;
        public newName: SchemaName;
        public renameUniqueName: boolean;

        public constructor(init?: Partial<SchemaRenamed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaRenamed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaDataCleared
    {
        public id: SchemaId;
        public integrations: IntegrationId[] = [];

        public constructor(init?: Partial<SchemaDataCleared>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaDataCleared'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class TaxonomyCreated
    {
        public taxonomy: Taxonomy;

        public constructor(init?: Partial<TaxonomyCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'TaxonomyCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class TaxonomyUpdated
    {
        public taxonomy: Taxonomy;

        public constructor(init?: Partial<TaxonomyUpdated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'TaxonomyUpdated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class TaxonomyDeleted
    {
        public taxonomyId: TaxonomyId;

        public constructor(init?: Partial<TaxonomyDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'TaxonomyDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class TaxonomyDataCleared
    {
        public taxonomyId: TaxonomyId;
        public integrations: IntegrationId[] = [];

        public constructor(init?: Partial<TaxonomyDataCleared>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'TaxonomyDataCleared'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaTriggerSaved
    {
        public trigger: SchemaTrigger;

        public constructor(init?: Partial<SchemaTriggerSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaTriggerSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaTriggerEnabled extends TriggerByIdEventBase
    {
        public schemaId: SchemaId;

        public constructor(init?: Partial<SchemaTriggerEnabled>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaTriggerEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaTriggerDisabled extends TriggerByIdEventBase
    {
        public schemaId: SchemaId;

        public constructor(init?: Partial<SchemaTriggerDisabled>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaTriggerDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchemaTriggerDeleted extends TriggerByIdEventBase
    {
        public schemaId: SchemaId;

        public constructor(init?: Partial<SchemaTriggerDeleted>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SchemaTriggerDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    // @Route("/{version}/files/disable", "GET")
    export class DisableFiles extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableFiles>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableFiles'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/files/enable", "GET")
    export class EnableFiles extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableFiles>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableFiles'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/files/triggers/{triggerId}", "DELETE")
    // @Route("/{version}/triggers", "DELETE")
    // @DataContract
    export class DeleteFilesTrigger extends DeleteTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DeleteFilesTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteFilesTrigger'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/files/triggers/{triggerId}/disable", "PATCH")
    // @Route("/{version}/triggers/disable", "PUT")
    // @DataContract
    export class DisableFilesTrigger extends DisableTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableFilesTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableFilesTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/files/triggers/{triggerId}/enable", "PATCH")
    // @Route("/{version}/triggers/enable", "PUT")
    // @DataContract
    export class EnableFilesTrigger extends EnableTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableFilesTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableFilesTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Gets files trigger by specified Id */
    // @Route("/{version}/files/triggers/{id}", "GET")
    // @Api(Description="Gets files trigger by specified Id")
    export class GetFilesTrigger extends GetTrigger implements IReturn<GetFilesTriggerResponse>
    {

        public constructor(init?: Partial<GetFilesTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetFilesTrigger'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetFilesTriggerResponse(); }
    }

    /** @description Gets files triggers */
    // @Route("/{version}/files/triggers", "GET")
    // @Api(Description="Gets files triggers")
    export class GetFilesTriggers extends GetTriggers implements IReturn<GetFilesTriggersResponse>
    {

        public constructor(init?: Partial<GetFilesTriggers>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetFilesTriggers'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetFilesTriggersResponse(); }
    }

    // @Route("/{version}/files/triggers", "POST")
    // @Route("/{version}/triggers", "POST")
    // @DataContract
    export class SaveFilesTrigger extends SaveTrigger implements IReturn<IdResponse>
    {

        public constructor(init?: Partial<SaveFilesTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveFilesTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/files/integrations/{Id}", "DELETE")
    export class DeleteFilesIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteFilesIntegrationRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/files/integrations/{Id}/disable", "PUT")
    export class DisableFilesIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisableFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableFilesIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/files/integrations/{Id}/enable", "PUT")
    export class EnableFilesIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnableFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableFilesIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/files/integrations/{id}", "GET")
    export class GetFilesIntegration extends CodeMashRequestBase implements IReturn<GetFilesIntegrationResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetFilesIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetFilesIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetFilesIntegrationResponse(); }
    }

    // @Route("/{version}/files/integrations", "GET")
    export class GetFilesIntegrations extends CodeMashListPaginationRequestBase implements IReturn<GetFilesIntegrationsResponse>
    {

        public constructor(init?: Partial<GetFilesIntegrations>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetFilesIntegrations'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetFilesIntegrationsResponse(); }
    }

    // @Route("/{version}/files/integrations", "POST")
    // @DataContract
    export class SaveFilesIntegration extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: FilesIntegrationRequest;

        public constructor(init?: Partial<SaveFilesIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveFilesIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/files/integrations/{Id}/default", "PUT")
    export class SetFilesIntegrationAsDefaultRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<SetFilesIntegrationAsDefaultRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SetFilesIntegrationAsDefaultRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/disable", "GET")
    export class DisableEmail extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableEmail>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableEmail'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/enable", "GET")
    export class EnableEmail extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableEmail>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableEmail'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/templates/attachments", "POST")
    export class AttachFileToTemplateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public language?: string;
        public templateId: string;
        public fileRef: FileResourceRefDto;

        public constructor(init?: Partial<AttachFileToTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'AttachFileToTemplateRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/templates", "POST")
    export class CreateEmailTemplateRequest extends SaveEmailTemplate implements IReturn<IdResponse>
    {

        public constructor(init?: Partial<CreateEmailTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreateEmailTemplateRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/notifications/email/templates/{Id}", "DELETE")
    export class DeleteEmailTemplateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteEmailTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteEmailTemplateRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/templates/{id}", "GET")
    export class GetEmailTemplate extends CodeMashRequestBase implements IReturn<GetEmailTemplateResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetEmailTemplate>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailTemplate'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailTemplateResponse(); }
    }

    // @Route("/{version}/notifications/email/templates", "GET")
    export class GetEmailTemplates extends CodeMashListPaginationRequestBase implements IReturn<GetEmailTemplatesResponse>
    {
        public showArchived?: boolean;
        public templateId?: string;

        public constructor(init?: Partial<GetEmailTemplates>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailTemplates'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailTemplatesResponse(); }
    }

    // @Route("/{version}/notifications/email/templates/mjml", "POST")
    export class GetMjml extends CodeMashRequestBase implements IReturn<GetHtmlFromMjmlResponse>
    {
        public code: string;
        public tokens?: TokenMappingDto[];
        public isForPreview: boolean;

        public constructor(init?: Partial<GetMjml>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetMjml'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new GetHtmlFromMjmlResponse(); }
    }

    // @Route("/{version}/notifications/email/system-templates/{id}", "GET")
    export class GetSystemEmailTemplate extends CodeMashRequestBase implements IReturn<GetSystemEmailTemplateResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetSystemEmailTemplate>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetSystemEmailTemplate'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetSystemEmailTemplateResponse(); }
    }

    // @Route("/{version}/notifications/email/system-templates", "GET")
    export class GetSystemEmailTemplates extends CodeMashListPaginationRequestBase implements IReturn<GetSystemEmailTemplatesResponse>
    {
        public groupTags?: string[];
        public themes?: string[];
        public communicationChannel?: CommunicationChannel;
        public forTrigger?: TriggerType;

        public constructor(init?: Partial<GetSystemEmailTemplates>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetSystemEmailTemplates'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetSystemEmailTemplatesResponse(); }
    }

    // @Route("/{version}/notifications/email/templates/{id}/tokens", "GET")
    export class GetEmailTemplateAvailableTokens extends CodeMashRequestBase implements IReturn<GetEmailTemplateAvailableTokensResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetEmailTemplateAvailableTokens>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailTemplateAvailableTokens'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailTemplateAvailableTokensResponse(); }
    }

    // @Route("/{version}/notifications/email/templates", "PUT")
    export class UpdateEmailTemplateRequest extends SaveEmailTemplate implements IReturn<EmptyResponse>
    {
        public viewId: string;

        public constructor(init?: Partial<UpdateEmailTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateEmailTemplateRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/signatures/{id}", "DELETE")
    export class DeleteEmailSignature extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteEmailSignature>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteEmailSignature'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/signatures/{id}", "GET")
    export class GetEmailSignature extends CodeMashRequestBase implements IReturn<GetEmailSignatureResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetEmailSignature>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailSignature'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailSignatureResponse(); }
    }

    // @Route("/{version}/notifications/email/signatures", "GET")
    export class GetEmailSignatures extends CodeMashListPaginationRequestBase implements IReturn<GetEmailSignaturesResponse>
    {

        public constructor(init?: Partial<GetEmailSignatures>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailSignatures'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailSignaturesResponse(); }
    }

    // @Route("/{version}/notifications/email/signatures", "POST")
    export class SaveEmailSignatureRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        public viewId?: string;
        public displayName: string;
        public translations: TranslationDto[] = [];

        public constructor(init?: Partial<SaveEmailSignatureRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveEmailSignatureRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/notifications/email/settings", "GET")
    export class GetEmailSettings extends CodeMashRequestBase implements IReturn<GetEmailSettingsResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetEmailSettings>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailSettings'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailSettingsResponse(); }
    }

    // @Route("/{version}/notifications/email/integrations/confirm-human-delivery", "POST")
    // @DataContract
    export class ConfirmEmailIntegrationHumanDeliveryRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public integrationId: string;

        public constructor(init?: Partial<ConfirmEmailIntegrationHumanDeliveryRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ConfirmEmailIntegrationHumanDeliveryRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/integrations/{Id}", "DELETE")
    export class DeleteEmailIntegration extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteEmailIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteEmailIntegration'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/integrations/{Id}/disable", "PUT")
    export class DisableEmailIntegration extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisableEmailIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableEmailIntegration'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/integrations/{Id}/enable", "PUT")
    export class EnableEmailIntegration extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnableEmailIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableEmailIntegration'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/integrations/{id}", "GET")
    export class GetEmailIntegration extends CodeMashRequestBase implements IReturn<GetEmailIntegrationResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetEmailIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailIntegrationResponse(); }
    }

    // @Route("/{version}/notifications/email/integrations", "GET")
    export class GetEmailIntegrations extends CodeMashListPaginationRequestBase implements IReturn<GetEmailIntegrationsResponse>
    {

        public constructor(init?: Partial<GetEmailIntegrations>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailIntegrations'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailIntegrationsResponse(); }
    }

    // @Route("/{version}/notifications/email/integrations", "POST")
    // @DataContract
    export class SaveEmailIntegration extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: EmailIntegrationRequest;

        public constructor(init?: Partial<SaveEmailIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveEmailIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/notifications/email/integrations/{Id}/default", "PUT")
    export class SetEmailsIntegrationAsDefault extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<SetEmailsIntegrationAsDefault>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SetEmailsIntegrationAsDefault'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/integrations/test", "POST")
    export class TestEmailIntegration extends CodeMashRequestBase implements IReturn<TestEmailIntegrationResponse>
    {
        public integrationId: string;
        public to?: string;

        public constructor(init?: Partial<TestEmailIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'TestEmailIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new TestEmailIntegrationResponse(); }
    }

    // @Route("/{version}/notifications/email/templates/{Id}/archive", "PUT")
    export class ArchiveEmailTemplateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<ArchiveEmailTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ArchiveEmailTemplateRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/templates/{Id}/clone", "POST")
    export class CloneEmailTemplateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<CloneEmailTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CloneEmailTemplateRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/templates/{Id}/unarchive", "PUT")
    export class UnArchiveEmailTemplateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<UnArchiveEmailTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UnArchiveEmailTemplateRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/footers/{id}", "DELETE")
    export class DeleteEmailFooter extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteEmailFooter>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteEmailFooter'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/footers/{id}", "GET")
    export class GetEmailFooter extends CodeMashRequestBase implements IReturn<GetEmailFooterResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetEmailFooter>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailFooter'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailFooterResponse(); }
    }

    // @Route("/{version}/notifications/email/footers", "GET")
    export class GetEmailFooters extends CodeMashListPaginationRequestBase implements IReturn<GetEmailFootersResponse>
    {

        public constructor(init?: Partial<GetEmailFooters>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailFooters'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailFootersResponse(); }
    }

    // @Route("/{version}/notifications/email/footers", "POST")
    export class SaveEmailFooterRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        public viewId?: string;
        public displayName: string;
        public translations: TranslationDto[] = [];

        public constructor(init?: Partial<SaveEmailFooterRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveEmailFooterRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description This endpoint implements the RFC 8058 one-click unsubscribe flow used by mailbox providers. */
    // @Route("/{version}/email/one-click-unsubscribe", "POST")
    // @Api(Description="This endpoint implements the RFC 8058 one-click unsubscribe flow used by mailbox providers.")
    // @DataContract
    export class OneClickUnsubscribeRequest extends RequestBase implements IReturn<EmptyResponse>
    {
        /** @description Encrypted unsubscribe token. The campaign batcher embedded this value in the List-Unsubscribe header. */
        // @DataMember
        // @ApiMember(Description="Encrypted unsubscribe token. The campaign batcher embedded this value in the List-Unsubscribe header.", IsRequired=true, Name="token", ParameterType="query")
        public token: string;

        public constructor(init?: Partial<OneClickUnsubscribeRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'OneClickUnsubscribeRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Create email campaign */
    // @Route("/{version}/notifications/email/campaigns", "POST")
    // @Api(Description="Create email campaign")
    // @DataContract
    export class CreateEmailCampaignRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public campaign: EmailCampaignRequest;

        // @DataMember
        public databaseIntegrationId: string;

        public constructor(init?: Partial<CreateEmailCampaignRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreateEmailCampaignRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Deletes emails campaign from queue */
    // @Route("/{version}/notifications/email/campaigns/{Id}", "DELETE")
    // @Api(Description="Deletes emails campaign from queue")
    // @DataContract
    export class DeleteEmailCampaignRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DeleteEmailCampaignRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteEmailCampaignRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/email/campaigns/{id}", "GET")
    export class GetEmailCampaign extends CodeMashRequestBase implements IReturn<GetEmailCampaignResponse>
    {
        public id: string;
        public databaseIntegrationId: string;

        public constructor(init?: Partial<GetEmailCampaign>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailCampaign'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailCampaignResponse(); }
    }

    // @Route("/{version}/notifications/email/campaigns", "GET")
    export class GetEmailCampaigns extends CodeMashListPaginationRequestBase implements IReturn<GetEmailCampaignsResponse>
    {
        public databaseIntegrationId: string;
        public campaignId?: string;
        public emailAddress?: string;
        public templateId?: string;
        public from?: number;
        public to?: number;

        public constructor(init?: Partial<GetEmailCampaigns>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailCampaigns'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailCampaignsResponse(); }
    }

    // @Route("/{version}/notifications/email/campaigns/{id}/batches", "GET")
    export class GetEmailCampaignBatches extends CodeMashListPaginationRequestBase implements IReturn<GetEmailCampaignBatchesResponse>
    {
        public id: string;
        public databaseIntegrationId: string;
        public batchId?: string;
        public emailAddress?: string;

        public constructor(init?: Partial<GetEmailCampaignBatches>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailCampaignBatches'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailCampaignBatchesResponse(); }
    }

    // @Route("/{version}/notifications/email/campaigns/{id}/batches/{batchId}/{notificationId}", "GET")
    export class GetEmailCampaignBatchNotification extends CodeMashListPaginationRequestBase implements IReturn<GetEmailCampaignBatchNotificationResponse>
    {
        public id: string;
        public batchId: string;
        public notificationId: string;
        public databaseIntegrationId: string;

        public constructor(init?: Partial<GetEmailCampaignBatchNotification>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailCampaignBatchNotification'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailCampaignBatchNotificationResponse(); }
    }

    // @Route("/{version}/notifications/email/campaigns/{id}/batches/{batchId}", "GET")
    export class GetEmailCampaignBatchNotifications extends CodeMashListPaginationRequestBase implements IReturn<GetEmailCampaignBatchNotificationsResponse>
    {
        public id: string;
        public batchId: string;
        public databaseIntegrationId: string;

        public constructor(init?: Partial<GetEmailCampaignBatchNotifications>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailCampaignBatchNotifications'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailCampaignBatchNotificationsResponse(); }
    }

    // @Route("/{version}/notifications/email/campaigns/{id}/stats", "GET")
    export class GetEmailCampaignStatistics extends CodeMashRequestBase implements IReturn<GetEmailCampaignStatisticsResponse>
    {
        public id: string;
        public databaseIntegrationId: string;

        public constructor(init?: Partial<GetEmailCampaignStatistics>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailCampaignStatistics'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailCampaignStatisticsResponse(); }
    }

    // @Route("/{version}/notifications/email/preview", "GET")
    export class PreviewEmailNotification extends RequestBase implements IReturn<PreviewEmailNotificationResponse>
    {
        public hash: string;

        public constructor(init?: Partial<PreviewEmailNotification>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'PreviewEmailNotification'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new PreviewEmailNotificationResponse(); }
    }

    // @Route("/{version}/notifications/emails/campaigns/{campaignId}/messages/{id}", "GET")
    export class GetEmailCampaignMessage extends CodeMashRequestBase implements IReturn<GetEmailCampaignMessageResponse>
    {
        public campaignId: string;
        public campaignBatchId: string;
        public notificationId: string;
        public databaseIntegrationId: string;

        public constructor(init?: Partial<GetEmailCampaignMessage>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailCampaignMessage'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailCampaignMessageResponse(); }
    }

    // @Route("/{version}/notifications/emails/campaigns/{campaignId}/messages", "GET")
    export class GetEmailCampaignMessagesRequest extends CodeMashListPaginationRequestBase implements IReturn<GetEmailCampaignMessagesResponse>
    {
        public campaignId: string;
        public campaignBatchId: string;
        public databaseIntegrationId: string;

        public constructor(init?: Partial<GetEmailCampaignMessagesRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEmailCampaignMessagesRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEmailCampaignMessagesResponse(); }
    }

    export class EmailServiceEstablished
    {

        public constructor(init?: Partial<EmailServiceEstablished>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailServiceEstablished'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailServiceEnabled
    {

        public constructor(init?: Partial<EmailServiceEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailServiceEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailServiceDisabled
    {

        public constructor(init?: Partial<EmailServiceDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailServiceDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailFooterSaved
    {
        public id: EmailFooterId;
        public name: DisplayName;
        public translations: MessageTranslation<TemplateCode>[] = [];

        public constructor(init?: Partial<EmailFooterSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailFooterSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailFooterDeleted
    {
        public id: EmailFooterId;

        public constructor(init?: Partial<EmailFooterDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailFooterDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailIntegrationSaved
    {
        public integration: EmailIntegration;

        public constructor(init?: Partial<EmailIntegrationSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailIntegrationSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailIntegrationTested
    {
        public id: IntegrationId;
        public succeeded: boolean;
        public errorMessages: IReadOnlyList<string>;
        public testedAtUtc: string;

        public constructor(init?: Partial<EmailIntegrationTested>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailIntegrationTested'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailIntegrationHumanDeliveryConfirmed
    {
        public id: IntegrationId;
        public confirmedAtUtc: string;

        public constructor(init?: Partial<EmailIntegrationHumanDeliveryConfirmed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailIntegrationHumanDeliveryConfirmed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailIntegrationRenamed
    {
        public id: IntegrationId;
        public name: DisplayName;

        public constructor(init?: Partial<EmailIntegrationRenamed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailIntegrationRenamed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailIntegrationSetAsDefault
    {
        public id: IntegrationId;

        public constructor(init?: Partial<EmailIntegrationSetAsDefault>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailIntegrationSetAsDefault'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailIntegrationDeleted
    {
        public id: IntegrationId;

        public constructor(init?: Partial<EmailIntegrationDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailIntegrationDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailIntegrationEnabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<EmailIntegrationEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailIntegrationEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailIntegrationDisabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<EmailIntegrationDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailIntegrationDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailSignatureSaved
    {
        public id: EmailSignatureId;
        public name: DisplayName;
        public translations: MessageTranslation<TemplateCode>[] = [];

        public constructor(init?: Partial<EmailSignatureSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailSignatureSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailSignatureDeleted
    {
        public id: EmailSignatureId;

        public constructor(init?: Partial<EmailSignatureDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailSignatureDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailTemplateCreated
    {
        public templateId: TemplateId;
        public displayName: DisplayName;
        public translations: MessageTranslation<EmailMessageContent>[] = [];
        public channel: CommunicationChannel;
        public description?: string;
        public tags?: Tag[];
        public languageAgnosticAttachments?: FileResourceRef[];

        public constructor(init?: Partial<EmailTemplateCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailTemplateCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailTemplateUpdated
    {
        public templateId: TemplateId;
        public displayName: DisplayName;
        public translations: MessageTranslation<EmailMessageContent>[] = [];
        public channel: CommunicationChannel;
        public description?: string;
        public tags?: Tag[];
        public languageAgnosticAttachments?: FileResourceRef[];
        public attachmentsToBeDeleted?: FileResourceRef[];

        public constructor(init?: Partial<EmailTemplateUpdated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailTemplateUpdated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailTemplateDeleted
    {
        public templateId: TemplateId;
        public filesToBeDeleted?: FileResourceRef[];
        public fileIntegrationId?: IntegrationId;

        public constructor(init?: Partial<EmailTemplateDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailTemplateDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailTemplateArchived
    {
        public templateId: TemplateId;

        public constructor(init?: Partial<EmailTemplateArchived>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailTemplateArchived'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class EmailTemplateUnArchived
    {
        public templateId: TemplateId;

        public constructor(init?: Partial<EmailTemplateUnArchived>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'EmailTemplateUnArchived'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class CodeIntegrationSaved
    {
        public integration: CodeIntegration;

        public constructor(init?: Partial<CodeIntegrationSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'CodeIntegrationSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class CodeIntegrationTested
    {
        public id: IntegrationId;
        public succeeded: boolean;
        public errorMessages: IReadOnlyList<string>;
        public testedAtUtc: string;

        public constructor(init?: Partial<CodeIntegrationTested>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'CodeIntegrationTested'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class CodeIntegrationHumanDeliveryConfirmed
    {
        public id: IntegrationId;
        public confirmedAtUtc: string;

        public constructor(init?: Partial<CodeIntegrationHumanDeliveryConfirmed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'CodeIntegrationHumanDeliveryConfirmed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class CodeIntegrationRenamed
    {
        public id: IntegrationId;
        public name: DisplayName;

        public constructor(init?: Partial<CodeIntegrationRenamed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'CodeIntegrationRenamed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class CodeIntegrationSetAsDefault
    {
        public id: IntegrationId;

        public constructor(init?: Partial<CodeIntegrationSetAsDefault>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'CodeIntegrationSetAsDefault'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class CodeIntegrationDeleted
    {
        public id: IntegrationId;

        public constructor(init?: Partial<CodeIntegrationDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'CodeIntegrationDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class CodeIntegrationEnabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<CodeIntegrationEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'CodeIntegrationEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class CodeIntegrationDisabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<CodeIntegrationDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'CodeIntegrationDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceIntegrationSaved
    {
        public integration: MarketplaceIntegration;

        public constructor(init?: Partial<MarketplaceIntegrationSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceIntegrationSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceIntegrationDeleted
    {
        public id: IntegrationId;

        public constructor(init?: Partial<MarketplaceIntegrationDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceIntegrationDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceIntegrationEnabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<MarketplaceIntegrationEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceIntegrationEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceIntegrationDisabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<MarketplaceIntegrationDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceIntegrationDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceIntegrationSecretsConfigured
    {
        public id: IntegrationId;

        public constructor(init?: Partial<MarketplaceIntegrationSecretsConfigured>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceIntegrationSecretsConfigured'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceIntegrationSecretsConfigurationFailed
    {
        public id: IntegrationId;

        public constructor(init?: Partial<MarketplaceIntegrationSecretsConfigurationFailed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceIntegrationSecretsConfigurationFailed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceFunctionBindingSaved
    {
        public binding: MarketplaceFunctionBinding;

        public constructor(init?: Partial<MarketplaceFunctionBindingSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceFunctionBindingSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceFunctionBindingDeleted
    {
        public integrationId: IntegrationId;
        public bindingId: string;

        public constructor(init?: Partial<MarketplaceFunctionBindingDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceFunctionBindingDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceFunctionBindingEnabled
    {
        public integrationId: IntegrationId;
        public bindingId: string;

        public constructor(init?: Partial<MarketplaceFunctionBindingEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceFunctionBindingEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class MarketplaceFunctionBindingDisabled
    {
        public integrationId: IntegrationId;
        public bindingId: string;

        public constructor(init?: Partial<MarketplaceFunctionBindingDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'MarketplaceFunctionBindingDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    // @Route("/{version}/notifications/push/disable", "GET")
    export class DisablePush extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisablePush>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisablePush'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/enable", "GET")
    export class EnablePush extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnablePush>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnablePush'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/templates/{Id}/archive", "PUT")
    export class ArchivePushTemplateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<ArchivePushTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ArchivePushTemplateRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/templates/{Id}/clone", "POST")
    export class ClonePushTemplateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<ClonePushTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ClonePushTemplateRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/templates", "POST")
    export class CreatePushTemplateRequest extends SavePushTemplate implements IReturn<IdResponse>
    {

        public constructor(init?: Partial<CreatePushTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreatePushTemplateRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/notifications/push/templates/{Id}", "DELETE")
    export class DeletePushTemplateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeletePushTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeletePushTemplateRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/templates/{id}", "GET")
    export class GetPushTemplate extends CodeMashRequestBase implements IReturn<GetPushTemplateResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetPushTemplate>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPushTemplate'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPushTemplateResponse(); }
    }

    // @Route("/{version}/notifications/push/templates", "GET")
    export class GetPushTemplates extends CodeMashListPaginationRequestBase implements IReturn<GetPushTemplatesResponse>
    {
        public showArchived?: boolean;
        public templateId?: string;

        public constructor(init?: Partial<GetPushTemplates>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPushTemplates'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPushTemplatesResponse(); }
    }

    // @Route("/{version}/notifications/push/templates/{id}/tokens", "GET")
    export class GetPushMessageContentTokens extends CodeMashRequestBase implements IReturn<GetPushMessageContentTokensResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetPushMessageContentTokens>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPushMessageContentTokens'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPushMessageContentTokensResponse(); }
    }

    // @Route("/{version}/notifications/push/templates/{Id}/unarchive", "PUT")
    export class UnArchivePushTemplateRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<UnArchivePushTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UnArchivePushTemplateRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/templates", "PUT")
    export class UpdatePushTemplateRequest extends SavePushTemplate implements IReturn<EmptyResponse>
    {
        public viewId: string;

        public constructor(init?: Partial<UpdatePushTemplateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdatePushTemplateRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations/confirm-human-delivery", "POST")
    // @DataContract
    export class ConfirmPushIntegrationHumanDeliveryRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public integrationId: string;

        public constructor(init?: Partial<ConfirmPushIntegrationHumanDeliveryRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ConfirmPushIntegrationHumanDeliveryRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations/{Id}", "DELETE")
    export class DeletePushIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeletePushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeletePushIntegrationRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations/{Id}/disable", "PUT")
    export class DisablePushIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisablePushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisablePushIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations/{Id}/enable", "PUT")
    export class EnablePushIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnablePushIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnablePushIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations/{id}", "GET")
    export class GetPushIntegration extends CodeMashRequestBase implements IReturn<GetPushIntegrationResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetPushIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPushIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPushIntegrationResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations", "GET")
    export class GetPushIntegrations extends CodeMashListPaginationRequestBase implements IReturn<GetPushIntegrationsResponse>
    {

        public constructor(init?: Partial<GetPushIntegrations>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPushIntegrations'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPushIntegrationsResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations", "POST")
    // @DataContract
    export class SavePushIntegration extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: PushIntegrationRequest;

        public constructor(init?: Partial<SavePushIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SavePushIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations/{Id}/default", "PUT")
    export class SetPushIntegrationAsDefaultRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<SetPushIntegrationAsDefaultRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SetPushIntegrationAsDefaultRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations/test", "POST")
    export class TestPushIntegration extends CodeMashRequestBase implements IReturn<TestEmailIntegrationResponse>
    {
        // @DataMember
        public integrationId: string;

        // @DataMember
        public testToken?: string;

        // @DataMember
        public deliveryFamily?: string;

        public constructor(init?: Partial<TestPushIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'TestPushIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new TestEmailIntegrationResponse(); }
    }

    // @Route("/{version}/notifications/push/integrations/app/request", "POST")
    export class RegisterCodeMashAppPushIntegration extends CodeMashRequestBase implements IReturn<EmptyResponse>, IHasAccountId
    {
        public accountId: string;
        public userId: string;
        public requestId: string;
        public pin: number;
        public validTill: string;
        public publicKey: string;

        public constructor(init?: Partial<RegisterCodeMashAppPushIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RegisterCodeMashAppPushIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/notifications/push/devices", "POST")
    // @DataContract
    export class RegisterDevice extends RequestBase implements IReturn<IdResponse>, IHasProjectId
    {
        // @DataMember
        public pushDeviceDto: PushDeviceDto;

        // @DataMember
        public userId: string;

        // @DataMember
        public projectId: string;

        // @DataMember
        public accountId?: string;

        public constructor(init?: Partial<RegisterDevice>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RegisterDevice'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    export class PushIntegrationSaved
    {
        public integration: PushIntegration;

        public constructor(init?: Partial<PushIntegrationSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushIntegrationSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushIntegrationTested
    {
        public id: IntegrationId;
        public succeeded: boolean;
        public errorMessages: IReadOnlyList<string>;
        public testedAtUtc: string;

        public constructor(init?: Partial<PushIntegrationTested>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushIntegrationTested'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushIntegrationHumanDeliveryConfirmed
    {
        public id: IntegrationId;
        public confirmedAtUtc: string;

        public constructor(init?: Partial<PushIntegrationHumanDeliveryConfirmed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushIntegrationHumanDeliveryConfirmed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushIntegrationRenamed
    {
        public id: IntegrationId;
        public name: DisplayName;

        public constructor(init?: Partial<PushIntegrationRenamed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushIntegrationRenamed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushIntegrationSetAsDefault
    {
        public id: IntegrationId;

        public constructor(init?: Partial<PushIntegrationSetAsDefault>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushIntegrationSetAsDefault'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushIntegrationDeleted
    {
        public id: IntegrationId;

        public constructor(init?: Partial<PushIntegrationDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushIntegrationDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushIntegrationEnabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<PushIntegrationEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushIntegrationEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushIntegrationDisabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<PushIntegrationDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushIntegrationDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushServiceEstablished
    {
        public defaultTemplates?: PushTemplate[];

        public constructor(init?: Partial<PushServiceEstablished>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushServiceEstablished'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushServiceEnabled
    {

        public constructor(init?: Partial<PushServiceEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushServiceEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushServiceDisabled
    {

        public constructor(init?: Partial<PushServiceDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushServiceDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushModuleTagSaved
    {
        public tag: TagDefinition;
        public communicationChannel: CommunicationChannel;

        public constructor(init?: Partial<PushModuleTagSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushModuleTagSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushModuleTagDeleted
    {
        public tag: Tag;
        public communicationChannel: CommunicationChannel;

        public constructor(init?: Partial<PushModuleTagDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushModuleTagDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushTemplateCreated
    {
        public templateId: TemplateId;
        public displayName: DisplayName;
        public translations: MessageTranslation<PushMessageContent>[] = [];
        public channel: CommunicationChannel;
        public description?: string;
        public tags?: Tag[];

        public constructor(init?: Partial<PushTemplateCreated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushTemplateCreated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushTemplateUpdated
    {
        public templateId: TemplateId;
        public displayName: DisplayName;
        public translations: MessageTranslation<PushMessageContent>[] = [];
        public channel: CommunicationChannel;
        public description?: string;
        public tags?: Tag[];

        public constructor(init?: Partial<PushTemplateUpdated>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushTemplateUpdated'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushTemplateDeleted
    {
        public templateId: TemplateId;

        public constructor(init?: Partial<PushTemplateDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushTemplateDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushTemplateArchived
    {
        public templateId: TemplateId;

        public constructor(init?: Partial<PushTemplateArchived>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushTemplateArchived'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class PushTemplateUnArchived
    {
        public templateId: TemplateId;

        public constructor(init?: Partial<PushTemplateUnArchived>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'PushTemplateUnArchived'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    // @Route("/{version}/payments/disable", "GET")
    export class DisablePayments extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisablePayments>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisablePayments'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/payments/enable", "GET")
    export class EnablePayments extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnablePayments>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnablePayments'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/payments/triggers/{triggerId}", "DELETE")
    // @Route("/{version}/triggers", "DELETE")
    // @DataContract
    export class DeletePaymentsTrigger extends DeleteTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DeletePaymentsTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeletePaymentsTrigger'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/payments/triggers/{triggerId}/disable", "PATCH")
    // @Route("/{version}/triggers/disable", "PUT")
    // @DataContract
    export class DisablePaymentsTrigger extends DisableTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisablePaymentsTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisablePaymentsTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/payments/triggers/{triggerId}/enable", "PATCH")
    // @Route("/{version}/triggers/enable", "PUT")
    // @DataContract
    export class EnablePaymentsTrigger extends EnableTrigger implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnablePaymentsTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnablePaymentsTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Gets payments trigger by specified Id */
    // @Route("/{version}/payments/triggers/{id}", "GET")
    // @Api(Description="Gets payments trigger by specified Id")
    export class GetPaymentsTrigger extends GetTrigger implements IReturn<GetPaymentsTriggerResponse>
    {

        public constructor(init?: Partial<GetPaymentsTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPaymentsTrigger'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPaymentsTriggerResponse(); }
    }

    /** @description Gets payments triggers */
    // @Route("/{version}/payments/triggers", "GET")
    // @Api(Description="Gets payments triggers")
    export class GetPaymentsTriggers extends GetTriggers implements IReturn<GetPaymentsTriggersResponse>
    {

        public constructor(init?: Partial<GetPaymentsTriggers>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPaymentsTriggers'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPaymentsTriggersResponse(); }
    }

    // @Route("/{version}/payments/triggers", "POST")
    // @Route("/{version}/triggers", "POST")
    // @DataContract
    export class SavePaymentsTrigger extends SaveTrigger implements IReturn<IdResponse>
    {

        public constructor(init?: Partial<SavePaymentsTrigger>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SavePaymentsTrigger'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/payments/integrations/confirm-human-delivery", "POST")
    // @DataContract
    export class ConfirmPaymentsIntegrationHumanDeliveryRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public integrationId: string;

        public constructor(init?: Partial<ConfirmPaymentsIntegrationHumanDeliveryRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ConfirmPaymentsIntegrationHumanDeliveryRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/payments/integrations/{Id}", "DELETE")
    export class DeletePaymentsIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeletePaymentsIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeletePaymentsIntegrationRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/payments/integrations/{Id}/disable", "PUT")
    export class DisablePaymentsIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisablePaymentsIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisablePaymentsIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/payments/integrations/{Id}/enable", "PUT")
    export class EnablePaymentsIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnablePaymentsIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnablePaymentsIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/payments/integrations/{id}", "GET")
    export class GetPaymentsIntegration extends CodeMashRequestBase implements IReturn<GetPaymentsIntegrationResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetPaymentsIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPaymentsIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPaymentsIntegrationResponse(); }
    }

    // @Route("/{version}/payments/integrations", "GET")
    export class GetPaymentsIntegrations extends CodeMashListPaginationRequestBase implements IReturn<GetPaymentsIntegrationsResponse>
    {

        public constructor(init?: Partial<GetPaymentsIntegrations>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPaymentsIntegrations'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetPaymentsIntegrationsResponse(); }
    }

    // @Route("/{version}/payments/integrations", "POST")
    // @DataContract
    export class SavePaymentsIntegration extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: PaymentIntegrationRequest;

        public constructor(init?: Partial<SavePaymentsIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SavePaymentsIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/payments/integrations/test", "POST")
    export class TestPaymentsIntegration extends CodeMashRequestBase implements IReturn<TestPaymentsIntegrationResponse>
    {
        public integrationId: string;

        public constructor(init?: Partial<TestPaymentsIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'TestPaymentsIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new TestPaymentsIntegrationResponse(); }
    }

    // @Route("/{version}/logs/disable", "GET")
    export class DisableLogging extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableLogging>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableLogging'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/logs/enable", "GET")
    export class EnableLogging extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableLogging>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableLogging'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/logs/integrations/{Id}", "DELETE")
    export class DeleteLoggingIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteLoggingIntegrationRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/logs/integrations/{Id}/disable", "PUT")
    export class DisableLoggingIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisableLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableLoggingIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/logs/integrations/{Id}/enable", "PUT")
    export class EnableLoggingIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnableLoggingIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableLoggingIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/logs/integrations/{id}", "GET")
    export class GetLoggingIntegration extends CodeMashRequestBase implements IReturn<GetLoggingIntegrationResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetLoggingIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetLoggingIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetLoggingIntegrationResponse(); }
    }

    // @Route("/{version}/logs/integrations", "GET")
    export class GetLoggingIntegrations extends CodeMashListPaginationRequestBase implements IReturn<GetLoggingIntegrationsResponse>
    {

        public constructor(init?: Partial<GetLoggingIntegrations>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetLoggingIntegrations'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetLoggingIntegrationsResponse(); }
    }

    // @Route("/{version}/logs/integrations", "POST")
    // @DataContract
    export class SaveLoggingIntegration extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: LoggingIntegrationRequest;

        public constructor(init?: Partial<SaveLoggingIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveLoggingIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/logs/integrations/test", "POST")
    export class TestLoggingIntegration extends CodeMashRequestBase implements IReturn<TestLoggingIntegrationResponse>
    {
        public integrationId: string;

        public constructor(init?: Partial<TestLoggingIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'TestLoggingIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new TestLoggingIntegrationResponse(); }
    }

    export class LoggingIntegrationSaved
    {
        public integration: LoggingIntegration;

        public constructor(init?: Partial<LoggingIntegrationSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LoggingIntegrationSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class LoggingIntegrationTested
    {
        public id: IntegrationId;
        public succeeded: boolean;
        public errorMessages: IReadOnlyList<string>;
        public testedAtUtc: string;

        public constructor(init?: Partial<LoggingIntegrationTested>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LoggingIntegrationTested'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class LoggingIntegrationRenamed
    {
        public id: IntegrationId;
        public name: DisplayName;

        public constructor(init?: Partial<LoggingIntegrationRenamed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LoggingIntegrationRenamed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class LoggingIntegrationDeleted
    {
        public id: IntegrationId;

        public constructor(init?: Partial<LoggingIntegrationDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LoggingIntegrationDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class LoggingIntegrationEnabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<LoggingIntegrationEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LoggingIntegrationEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class LoggingIntegrationDisabled
    {
        public id: IntegrationId;

        public constructor(init?: Partial<LoggingIntegrationDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LoggingIntegrationDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class LoggingEstablished
    {

        public constructor(init?: Partial<LoggingEstablished>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LoggingEstablished'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class LoggingEnabled
    {

        public constructor(init?: Partial<LoggingEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LoggingEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class LoggingDisabled
    {

        public constructor(init?: Partial<LoggingDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'LoggingDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    /** @description Gets account info. */
    // @Route("/{version}/account/chat/complete", "POST")
    // @Api(Description="Gets account info.")
    export class AskChatRequest extends RequestBase implements IReturn<AskChatResponse>
    {
        public prompt: string;

        public constructor(init?: Partial<AskChatRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'AskChatRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new AskChatResponse(); }
    }

    // @Route("/{version}/ai/integrations/llms/{Id}", "DELETE")
    export class DeleteLlmIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteLlmIntegrationRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/ai/integrations/llms/{Id}/disable", "PUT")
    export class DisableLlmIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisableLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableLlmIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/ai/integrations/llms/{Id}/enable", "PUT")
    export class EnableLlmIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnableLlmIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableLlmIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/ai/integrations/llms/{id}", "GET")
    export class GetLlmIntegration extends CodeMashRequestBase implements IReturn<GetLlmIntegrationResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetLlmIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetLlmIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetLlmIntegrationResponse(); }
    }

    // @Route("/{version}/ai/integrations/llms/integrations", "GET")
    export class GetLlmIntegrations extends CodeMashListPaginationRequestBase implements IReturn<GetLlmIntegrationsResponse>
    {

        public constructor(init?: Partial<GetLlmIntegrations>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetLlmIntegrations'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetLlmIntegrationsResponse(); }
    }

    // @Route("/{version}/ai/integrations/llms/", "POST")
    // @DataContract
    export class SaveLlmIntegration extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: LlmIntegrationRequest;

        public constructor(init?: Partial<SaveLlmIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveLlmIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/ai/integrations/llms/test", "POST")
    export class TestLlmIntegration extends CodeMashRequestBase implements IReturn<TestLlmIntegrationResponse>
    {
        public integrationId: string;

        public constructor(init?: Partial<TestLlmIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'TestLlmIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new TestLlmIntegrationResponse(); }
    }

    // @Route("/{version}/ai/integrations/mcp/{Id}", "DELETE")
    export class DeleteMcpIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteMcpIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteMcpIntegrationRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/ai/integrations/mcp/{Id}/disable", "PUT")
    export class DisableMcpIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisableMcpIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableMcpIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/ai/integrations/mcp/{Id}/enable", "PUT")
    export class EnableMcpIntegrationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnableMcpIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableMcpIntegrationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/ai/integrations/mcp/{id}", "GET")
    export class GetMcpIntegration extends CodeMashRequestBase implements IReturn<GetMcpIntegrationResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetMcpIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetMcpIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetMcpIntegrationResponse(); }
    }

    // @Route("/{version}/ai/integrations/mcp/integrations", "GET")
    export class GetMcpIntegrations extends CodeMashListPaginationRequestBase implements IReturn<GetMcpIntegrationsResponse>
    {

        public constructor(init?: Partial<GetMcpIntegrations>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetMcpIntegrations'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetMcpIntegrationsResponse(); }
    }

    // @Route("/{version}/ai/integrations/mcp/", "POST")
    // @DataContract
    export class SaveMcpIntegration extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public integration: McpIntegrationRequest;

        public constructor(init?: Partial<SaveMcpIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveMcpIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    // @Route("/{version}/ai/integrations/mcp/test", "POST")
    export class TestMcpIntegration extends CodeMashRequestBase implements IReturn<TestLlmIntegrationResponse>
    {
        public integrationId: string;

        public constructor(init?: Partial<TestMcpIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'TestMcpIntegration'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new TestLlmIntegrationResponse(); }
    }

    export class WebhookIntegrationSaved
    {
        public integration: WebhookIntegration;

        public constructor(init?: Partial<WebhookIntegrationSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'WebhookIntegrationSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class WebhookIntegrationExtraHeadersChanged
    {
        public id: IntegrationId;
        public extraHeaders?: IReadOnlyDictionary<string, string>;

        public constructor(init?: Partial<WebhookIntegrationExtraHeadersChanged>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'WebhookIntegrationExtraHeadersChanged'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class WebhookIntegrationSecretsConfigured
    {
        public id: IntegrationId;

        public constructor(init?: Partial<WebhookIntegrationSecretsConfigured>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'WebhookIntegrationSecretsConfigured'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class WebhookIntegrationSecretsConfigurationFailed
    {
        public id: IntegrationId;

        public constructor(init?: Partial<WebhookIntegrationSecretsConfigurationFailed>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'WebhookIntegrationSecretsConfigurationFailed'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class WebhookIntegrationSecretsCleared
    {
        public id: IntegrationId;

        public constructor(init?: Partial<WebhookIntegrationSecretsCleared>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'WebhookIntegrationSecretsCleared'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class WebhookDestinationSaved
    {
        public integrationId: IntegrationId;
        public destination: WebhookDestination;

        public constructor(init?: Partial<WebhookDestinationSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'WebhookDestinationSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class WebhookDestinationRemoved
    {
        public integrationId: IntegrationId;
        public destinationId: WebhookDestinationId;

        public constructor(init?: Partial<WebhookDestinationRemoved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'WebhookDestinationRemoved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class WebhookDestinationEnabled
    {
        public integrationId: IntegrationId;
        public destinationId: WebhookDestinationId;

        public constructor(init?: Partial<WebhookDestinationEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'WebhookDestinationEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class WebhookDestinationDisabled
    {
        public integrationId: IntegrationId;
        public destinationId: WebhookDestinationId;

        public constructor(init?: Partial<WebhookDestinationDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'WebhookDestinationDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    // @Route("/{version}/webhooks/integration", "GET")
    export class GetWebhookIntegration extends CodeMashRequestBase implements IReturn<GetWebhookIntegrationResponse>
    {

        public constructor(init?: Partial<GetWebhookIntegration>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetWebhookIntegration'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetWebhookIntegrationResponse(); }
    }

    // @Route("/{version}/webhooks/integration/secret", "GET")
    export class RevealWebhookIntegrationSecretRequest extends CodeMashRequestBase implements IReturn<RevealWebhookIntegrationSecretResponse>
    {

        public constructor(init?: Partial<RevealWebhookIntegrationSecretRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RevealWebhookIntegrationSecretRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new RevealWebhookIntegrationSecretResponse(); }
    }

    // @Route("/{version}/webhooks/integration/secret/rotate", "POST")
    export class RotateWebhookIntegrationSecretRequest extends CodeMashRequestBase implements IReturn<RotateWebhookIntegrationSecretResponse>
    {

        public constructor(init?: Partial<RotateWebhookIntegrationSecretRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RotateWebhookIntegrationSecretRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new RotateWebhookIntegrationSecretResponse(); }
    }

    // @Route("/{version}/webhooks/integration/extra-headers", "PUT")
    export class UpdateWebhookIntegrationExtraHeadersRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public extraHeaders?: { [index:string]: string; };

        public constructor(init?: Partial<UpdateWebhookIntegrationExtraHeadersRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateWebhookIntegrationExtraHeadersRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/webhooks/destinations/{DestinationId}/disable", "PUT")
    export class DisableWebhookDestinationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public destinationId: string;

        public constructor(init?: Partial<DisableWebhookDestinationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableWebhookDestinationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/webhooks/destinations/{DestinationId}/enable", "PUT")
    export class EnableWebhookDestinationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public destinationId: string;

        public constructor(init?: Partial<EnableWebhookDestinationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableWebhookDestinationRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/webhooks/destinations/{DestinationId}", "DELETE")
    export class RemoveWebhookDestinationRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public destinationId: string;

        public constructor(init?: Partial<RemoveWebhookDestinationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RemoveWebhookDestinationRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/webhooks/destinations", "POST")
    export class SaveWebhookDestinationRequest extends CodeMashRequestBase implements IReturn<SaveWebhookDestinationResponse>
    {
        public destinationId?: string;
        public destinationName: string;
        public endpointUrl: string;
        public selectedEvents: string[] = [];
        public extraHeaders?: { [index:string]: string; };
        public isEnabled: boolean;

        public constructor(init?: Partial<SaveWebhookDestinationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveWebhookDestinationRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new SaveWebhookDestinationResponse(); }
    }

    // @Route("/{version}/scheduler/disable", "GET")
    export class DisableScheduler extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<DisableScheduler>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableScheduler'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/scheduler/enable", "GET")
    export class EnableScheduler extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {

        public constructor(init?: Partial<EnableScheduler>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableScheduler'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/scheduler/tasks/{Id}", "DELETE")
    export class DeleteSchedulerTask extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DeleteSchedulerTask>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteSchedulerTask'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/scheduler/tasks/{Id}/disable", "PUT")
    export class DisableSchedulerTask extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<DisableSchedulerTask>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DisableSchedulerTask'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/scheduler/tasks/{Id}/enable", "PUT")
    export class EnableSchedulerTask extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public id: string;

        public constructor(init?: Partial<EnableSchedulerTask>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'EnableSchedulerTask'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/scheduler/tasks/{id}", "GET")
    export class GetSchedulerTask extends CodeMashRequestBase implements IReturn<GetSchedulerTaskResponse>
    {
        public id: string;

        public constructor(init?: Partial<GetSchedulerTask>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetSchedulerTask'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetSchedulerTaskResponse(); }
    }

    // @Route("/{version}/scheduler/tasks", "GET")
    export class GetSchedulerTasks extends CodeMashListPaginationRequestBase implements IReturn<GetSchedulerTasksResponse>
    {
        public type?: SchedulerTaskType;
        public enabled?: boolean;

        public constructor(init?: Partial<GetSchedulerTasks>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetSchedulerTasks'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetSchedulerTasksResponse(); }
    }

    /** @description Save scheduled task */
    // @Route("/{version}/scheduler/tasks", "POST")
    // @Api(Description="Save scheduled task")
    // @DataContract
    export class SaveSchedulerTaskRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public taskId?: string;

        // @DataMember
        public name: string;

        // @DataMember
        public description?: string;

        // @DataMember
        public cron: string;

        // @DataMember
        public initiatorUserId: string;

        // @DataMember
        public isEnabled: boolean;

        // @DataMember
        public stopOnError: boolean;

        // @DataMember
        public task: SchedulerTaskRequest;

        public constructor(init?: Partial<SaveSchedulerTaskRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveSchedulerTaskRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    export class SchedulerEnabled
    {

        public constructor(init?: Partial<SchedulerEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchedulerEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchedulerDisabled
    {

        public constructor(init?: Partial<SchedulerDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchedulerDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchedulerTaskSaved
    {
        public task: SchedulerTask;

        public constructor(init?: Partial<SchedulerTaskSaved>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchedulerTaskSaved'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchedulerTaskEnabled
    {
        public taskId: TaskId;

        public constructor(init?: Partial<SchedulerTaskEnabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchedulerTaskEnabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchedulerTaskDisabled
    {
        public taskId: TaskId;

        public constructor(init?: Partial<SchedulerTaskDisabled>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchedulerTaskDisabled'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    export class SchedulerTaskDeleted
    {
        public taskId: TaskId;

        public constructor(init?: Partial<SchedulerTaskDeleted>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'SchedulerTaskDeleted'; }
        public getMethod() { return 'POST'; }
        public createResponse() {}
    }

    /** @description Sign In */
    // @Route("/auth", "GET,POST")
    // @Route("/auth/{provider}", "GET,POST")
    // @Route("/v3/auth", "POST,GET,OPTIONS")
    // @Route("/v3/auth/{provider}", "POST,GET,OPTIONS")
    // @Api(Description="Sign In")
    // @DataContract
    export class Authenticate implements IReturn<AuthenticateResponse>, IPost
    {
        /** @description AuthProvider, e.g. credentials */
        // @DataMember(Order=1)
        public provider?: string;

        // @DataMember(Order=2)
        public userName?: string;

        // @DataMember(Order=3)
        public password?: string;

        // @DataMember(Order=4)
        public rememberMe?: boolean;

        // @DataMember(Order=5)
        public accessToken?: string;

        // @DataMember(Order=6)
        public accessTokenSecret?: string;

        // @DataMember(Order=7)
        public returnUrl?: string;

        // @DataMember(Order=8)
        public errorView?: string;

        // @DataMember(Order=9)
        public meta?: { [index:string]: string; };

        public constructor(init?: Partial<Authenticate>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'Authenticate'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new AuthenticateResponse(); }
    }

    // @Route("/access-token")
    // @DataContract
    export class GetAccessToken implements IReturn<GetAccessTokenResponse>, IPost
    {
        // @DataMember(Order=1)
        public refreshToken?: string;

        // @DataMember(Order=2)
        public meta?: { [index:string]: string; };

        public constructor(init?: Partial<GetAccessToken>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'GetAccessToken'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new GetAccessTokenResponse(); }
    }

    // @Route("/apikeys")
    // @Route("/apikeys/{Environment}")
    // @DataContract
    export class GetApiKeys implements IReturn<GetApiKeysResponse>, IGet
    {
        // @DataMember(Order=1)
        public environment?: string;

        // @DataMember(Order=2)
        public meta?: { [index:string]: string; };

        public constructor(init?: Partial<GetApiKeys>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'GetApiKeys'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetApiKeysResponse(); }
    }

    // @Route("/apikeys/regenerate")
    // @Route("/apikeys/regenerate/{Environment}")
    // @DataContract
    export class RegenerateApiKeys implements IReturn<RegenerateApiKeysResponse>, IPost
    {
        // @DataMember(Order=1)
        public environment?: string;

        // @DataMember(Order=2)
        public meta?: { [index:string]: string; };

        public constructor(init?: Partial<RegenerateApiKeys>) { (Object as any).assign(this, init); }
        public getTypeName() { return 'RegenerateApiKeys'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new RegenerateApiKeysResponse(); }
    }

}

