/* Options:
Date: 2025-10-22 10:51:05
Version: 8.30
Tip: To override a DTO option, remove "//" prefix before updating
BaseUrl: http://localhost:5002

GlobalNamespace: CodeMashApi2
//MakePropertiesOptional: False
AddServiceStackTypes: True
AddResponseStatus: False
//AddImplicitVersion: 
AddDescriptionAsComments: True
//IncludeTypes: 
//ExcludeTypes: 
//DefaultImports: 
*/


export module CodeMashApi2
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

    // @DataContract(Namespace="http://codemash.io/types/")
    export class CodeMashRequestBase extends RequestBase implements IHasProjectId, IHasEnv
    {
        /** @description ID of your project. Can be passed in a header as norbix-project-id. */
        // @DataMember
        // @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as norbix-project-id.", IsRequired=true, Name="norbix-project-id", ParameterType="header")
        public projectId: string;

        /** @description Target environment for this request (e.g. TEST, STAGING). Optional — when omitted the request runs against PROD. Can be passed in a header as norbix-env. */
        // @DataMember
        // @ApiMember(DataType="string", Description="Target environment for this request (e.g. TEST, STAGING). Optional — when omitted the request runs against PROD. Can be passed in a header as norbix-env.", Name="norbix-env", ParameterType="header")
        public env?: string;

        public constructor(init?: Partial<CodeMashRequestBase>) { super(init); (Object as any).assign(this, init); }
    }

    export interface IHasProjectId
    {
        projectId: string;
    }

    export interface IHasEnv
    {
        env?: string;
    }

    export enum Gender
    {
        Male = 'Male',
        Female = 'Female',
        Other = 'Other',
    }

    export enum MarketingBlockReason
    {
        Unspecified = 'Unspecified',
        Unsubscribed = 'Unsubscribed',
        Complaint = 'Complaint',
        HardBounce = 'HardBounce',
        InvalidEmail = 'InvalidEmail',
        AdminBlock = 'AdminBlock',
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
        public blockedTags?: { [index:string]: HashSet<string>; };
        public blockReasons?: MarketingBlockReason[];
        public extraMetadata?: string;
        public notes?: string;

        public constructor(init?: Partial<UserGeneralInfoDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SaveUser extends CodeMashRequestBase
    {
        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        /** @description User Info */
        // @DataMember
        // @ApiMember(DataType="object", Description="User Info", Name="UserGeneralInfo", ParameterType="body")
        public userGeneralInfo?: UserGeneralInfoDto;

        /** @description Attach this login to an existing user id. Optional. */
        // @DataMember
        // @ApiMember(Description="Attach this login to an existing user id. Optional.")
        public userId?: string;

        /** @description Ignore UserRegistersAsRole from Membership Settings */
        // @DataMember
        // @ApiMember(DataType="boolean", Description="Ignore UserRegistersAsRole from Membership Settings", Name="IgnoreUserRegistersAsRole", ParameterType="body")
        public ignoreUserRegistersAsRole: boolean;

        public constructor(init?: Partial<SaveUser>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class SaveUserWithRolesBase extends SaveUser
    {
        // @DataMember
        public roles: string[] = [];

        public constructor(init?: Partial<SaveUserWithRolesBase>) { super(init); (Object as any).assign(this, init); }
    }

    export class CodeMashListPaginationRequestBase extends RequestBase implements IHasProjectId, IHasEnv
    {
        /** @description ID of your project. Can be passed in a header as norbix-project-id. */
        // @DataMember
        // @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as norbix-project-id.", IsRequired=true, Name="norbix-project-id", ParameterType="header")
        public projectId: string;

        /** @description Target environment for this request (e.g. TEST, STAGING). Optional — when omitted the request runs against PROD. Can be passed in a header as norbix-env. */
        // @DataMember
        // @ApiMember(DataType="string", Description="Target environment for this request (e.g. TEST, STAGING). Optional — when omitted the request runs against PROD. Can be passed in a header as norbix-env.", Name="norbix-env", ParameterType="header")
        public env?: string;

        /** @description Cursor token — fetch the page AFTER this item. */
        // @DataMember
        // @ApiMember(DataType="string", Description="Cursor token — fetch the page AFTER this item.", Name="startingAfter", ParameterType="query")
        public startingAfter?: string;

        /** @description Cursor token — fetch the page BEFORE this item. */
        // @DataMember
        // @ApiMember(DataType="string", Description="Cursor token — fetch the page BEFORE this item.", Name="endingBefore", ParameterType="query")
        public endingBefore?: string;

        /** @description Amount of records to return. */
        // @DataMember
        // @ApiMember(DataType="integer", Description="Amount of records to return.", Format="int32", Name="pageSize", ParameterType="query")
        public pageSize?: number;

        public constructor(init?: Partial<CodeMashListPaginationRequestBase>) { super(init); (Object as any).assign(this, init); }
    }

    export interface IPasskeyCeremonyRequest
    {
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
        Staging = 'Staging',
        Production = 'Production',
    }

    // @DataContract
    export class EchoLicenseDto
    {
        // @DataMember(Name="domain")
        public domain?: string;

        // @DataMember(Name="accountId")
        public accountId?: string;

        // @DataMember(Name="email")
        public email?: string;

        // @DataMember(Name="release")
        public release?: string;

        // @DataMember(Name="expire")
        public expire: number;

        // @DataMember(Name="isTrial")
        public isTrial: boolean;

        // @DataMember(Name="cap")
        public cap: number;

        public constructor(init?: Partial<EchoLicenseDto>) { (Object as any).assign(this, init); }
    }

    export class EchoRegionDto
    {
        public code: string;
        public displayName: string;
        public apiUrl: string;
        public hubUrl: string;

        public constructor(init?: Partial<EchoRegionDto>) { (Object as any).assign(this, init); }
    }

    export class EchoAgentDto
    {
        public mcpUrl: string;
        public oAuthMetadataUrl?: string;
        public installationType: string;
        public onboardingDocsUrl: string;
        public toolsUrl: string;

        public constructor(init?: Partial<EchoAgentDto>) { (Object as any).assign(this, init); }
    }

    export class PublicBrandDto
    {
        public displayName: string;
        public mainColor?: string;
        public accentColor?: string;
        public logoUrl?: string;
        public iconUrl?: string;

        public constructor(init?: Partial<PublicBrandDto>) { (Object as any).assign(this, init); }
    }

    export class PublicPasswordPolicyDto
    {
        public minLength: number;
        public maxLength?: number;
        public minNumbers?: number;
        public minUpper?: number;
        public minLower?: number;
        public minSpecial?: number;
        public allowedSpecial?: string;

        public constructor(init?: Partial<PublicPasswordPolicyDto>) { (Object as any).assign(this, init); }
    }

    export class PublicAuthDto
    {
        public socialProviders: string[] = [];
        public passkey: boolean;
        public methods?: string[];
        public passwordPolicy?: PublicPasswordPolicyDto;

        public constructor(init?: Partial<PublicAuthDto>) { (Object as any).assign(this, init); }
    }

    export class PublicAiAssistantDto
    {
        public id: string;
        public name: string;
        public welcome?: string;

        public constructor(init?: Partial<PublicAiAssistantDto>) { (Object as any).assign(this, init); }
    }

    export class PublicAiChatDto
    {
        public enabled: boolean;
        public assistants: PublicAiAssistantDto[] = [];

        public constructor(init?: Partial<PublicAiChatDto>) { (Object as any).assign(this, init); }
    }

    export class ErrorDto
    {
        public message: string;
        public errorCode?: string;
        public context?: { [index:string]: string; };
        public stackTrace?: ErrorDto[];

        public constructor(init?: Partial<ErrorDto>) { (Object as any).assign(this, init); }
    }

    export class CodeMashResponseStatus
    {
        public isSuccess: boolean;
        public errors?: ErrorDto[];

        public constructor(init?: Partial<CodeMashResponseStatus>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class ResponseBase
    {
        // @DataMember
        public responseStatus: CodeMashResponseStatus;

        public constructor(init?: Partial<ResponseBase>) { (Object as any).assign(this, init); }
    }

    export class EndUserChatAttachment
    {
        public id: string;
        public sessionId: string;
        public fileName: string;
        public contentType: string;
        public kind: string;
        public size: number;
        public summary?: string;
        public createdAtUtc: string;

        public constructor(init?: Partial<EndUserChatAttachment>) { (Object as any).assign(this, init); }
    }

    export class EndUserChatMemoryNote
    {
        public id: string;
        public sessionId: string;
        public kind: string;
        public text: string;
        public createdAtUtc: string;

        public constructor(init?: Partial<EndUserChatMemoryNote>) { (Object as any).assign(this, init); }
    }

    export class EndUserChatAssistant
    {
        public id: string;
        public name: string;
        public welcomeMessage?: string;
        public isDefault: boolean;
        public memoryEnabled: boolean;

        public constructor(init?: Partial<EndUserChatAssistant>) { (Object as any).assign(this, init); }
    }

    export class EndUserChatPlan
    {
        public id: string;
        public name: string;
        public quotaUnit: string;
        public monthlyQuota: number;
        public used: number;
        public remaining: number;
        public attachments: boolean;
        public rag: boolean;
        public memory: boolean;

        public constructor(init?: Partial<EndUserChatPlan>) { (Object as any).assign(this, init); }
    }

    export class EndUserChatSession
    {
        public id: string;
        public assistantId?: string;
        public title?: string;
        public isPinned: boolean;
        public isArchived: boolean;
        public lastSeq: number;
        public createdAtUtc: string;
        public updatedAtUtc: string;

        public constructor(init?: Partial<EndUserChatSession>) { (Object as any).assign(this, init); }
    }

    export class AiChatEntryWireDto
    {
        public kind: string;
        public id: string;
        public seq: number;
        public atUtc: string;
        public refEntryId?: string;
        public workItemId?: string;
        public feedback?: string;
        public feedbackAtUtc?: string;
        public feedbackByUserAuthId?: string;

        public constructor(init?: Partial<AiChatEntryWireDto>) { (Object as any).assign(this, init); }
    }

    export class EndUserAiToolParameter
    {
        public name: string;
        public type: string;
        public required: boolean;
        public description?: string;

        public constructor(init?: Partial<EndUserAiToolParameter>) { (Object as any).assign(this, init); }
    }

    export class EndUserAiTool
    {
        public name: string;
        public description: string;
        public toolsets: string[] = [];
        public requiresConfirmation: boolean;
        public parameters: EndUserAiToolParameter[] = [];

        public constructor(init?: Partial<EndUserAiTool>) { (Object as any).assign(this, init); }
    }

    export enum AuthType
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

    export enum AuthStatus
    {
        Registered = 0,
        PendingValidation = 2,
        Active = 8,
        Unregistered = 16,
        Suspended = 32,
        InActive = 64,
        Blocked = 128,
    }

    export class AuthDto implements IBindableContract
    {
        public id: string;
        public type: AuthType;
        public email?: string;
        public userName?: string;
        public registration?: RegistrationDto;
        public login?: LoginDto;
        public generalInfo?: UserGeneralInfoDto;
        public roles?: string[];
        public pushDevices?: string[];
        public tags?: string[];
        public status: AuthStatus;
        public createdOn: string;
        public modifiedOn: string;

        public constructor(init?: Partial<AuthDto>) { (Object as any).assign(this, init); }
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

    export class UserMarketingPreferencesDto
    {
        public blockAllMarketingMessages: boolean;
        public blockedTags?: { [index:string]: HashSet<string>; };
        public blockReasons?: MarketingBlockReason[];

        public constructor(init?: Partial<UserMarketingPreferencesDto>) { (Object as any).assign(this, init); }
    }

    export class PasskeyListItemDto
    {
        public credentialId: string;
        public friendlyName: string;
        public registeredOnUtc: string;
        public lastUsedOnUtc: string;
        public isRevoked: boolean;

        public constructor(init?: Partial<PasskeyListItemDto>) { (Object as any).assign(this, init); }
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

    export class TermTreeDto
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

        // @DataMember
        public children?: TermTreeDto[];

        public constructor(init?: Partial<TermTreeDto>) { (Object as any).assign(this, init); }
    }

    export class TaxonomyTreeDto
    {
        // @DataMember
        public viewId: string;

        // @DataMember
        public taxonomyName: string;

        // @DataMember
        public taxonomySlug: string;

        // @DataMember
        public parentId?: string;

        // @DataMember
        public children?: TaxonomyTreeDto[];

        // @DataMember
        public terms?: TermTreeDto[];

        public constructor(init?: Partial<TaxonomyTreeDto>) { (Object as any).assign(this, init); }
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

    export class SchemaSettingsDto
    {
        // @DataMember
        public softDelete: boolean;

        // @DataMember
        public hasRecordOwner: boolean;

        // @DataMember
        public description?: string;

        public constructor(init?: Partial<SchemaSettingsDto>) { (Object as any).assign(this, init); }
    }

    export class SchemaEmbedSettingsDto
    {
        // @DataMember
        public enabled: boolean;

        // @DataMember
        public fields: string[] = [];

        // @DataMember
        public embeddingIntegrationId?: string;

        // @DataMember
        public perUser: boolean;

        public constructor(init?: Partial<SchemaEmbedSettingsDto>) { (Object as any).assign(this, init); }
    }

    export enum TriggerType
    {
        Membership = 'Membership',
        Schema = 'Schema',
        Files = 'Files',
        Payments = 'Payments',
        Ai = 'Ai',
    }

    export enum TriggerActionType
    {
        Code = 'Code',
        Push = 'Push',
        Sms = 'Sms',
        Email = 'Email',
        WebhookCall = 'WebhookCall',
        SseCall = 'SseCall',
        Marketplace = 'Marketplace',
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

        // @DataMember
        public savedByAuthId?: string;

        public constructor(init?: Partial<TriggerDto>) { (Object as any).assign(this, init); }
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
        public embed?: SchemaEmbedSettingsDto;

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

        // @DataMember
        public description?: string;

        // @DataMember
        public env?: string;

        public constructor(init?: Partial<SchemaListProjection>) { (Object as any).assign(this, init); }
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

        // @DataMember(Order=5)
        public publicUrl?: string;

        // @DataMember(Order=6)
        public isPublic: boolean;

        public constructor(init?: Partial<FileResourceRefDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class PublicFolderDto
    {
        // @DataMember(Order=1)
        public path: string;

        // @DataMember(Order=2)
        public publicId: string;

        // @DataMember(Order=3)
        public publicUrl?: string;

        // @DataMember(Order=4)
        public inherited: boolean;

        public constructor(init?: Partial<PublicFolderDto>) { (Object as any).assign(this, init); }
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

    export interface IBindableContract
    {
    }

    export interface IHasViewId
    {
        viewId: string;
    }

    export interface ICursorArgs
    {
        field: string;
        order: number;
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
        public adminUrlTemplate?: string;
        public license?: EchoLicenseDto;
        public askForEnterpriseLicenseEmail?: string;
        public emailServiceConfigured: boolean;
        public rootBootstrapPasswordSource?: string;
        public regions?: EchoRegionDto[];
        public isProductionInstallation: boolean;
        public licensingMode: string;
        public graceDaysLeft?: number;
        public installationDomain?: string;
        public licensingDocsUrl?: string;
        public agent?: EchoAgentDto;

        public constructor(init?: Partial<EchoResponse>) { (Object as any).assign(this, init); }
    }

    export class PublicProjectConfigDto
    {
        public displayName: string;
        public adminPortalEnabled: boolean;
        public branding?: PublicBrandDto;
        public auth: PublicAuthDto;
        public aiChat: PublicAiChatDto;

        public constructor(init?: Partial<PublicProjectConfigDto>) { (Object as any).assign(this, init); }
    }

    export class PublicLegalDocumentDto
    {
        public kind: string;
        public title?: string;
        public body: string;
        public available: boolean;

        public constructor(init?: Partial<PublicLegalDocumentDto>) { (Object as any).assign(this, init); }
    }

    // @DataContract
    export class IdResponse extends ResponseBase
    {
        // @DataMember
        public id?: string;

        // @DataMember
        public status?: string;

        public constructor(init?: Partial<IdResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class ListEndUserChatAttachmentsResponse extends ResponseBase
    {
        public attachments: EndUserChatAttachment[] = [];

        public constructor(init?: Partial<ListEndUserChatAttachmentsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class EmptyResponse extends ResponseBase
    {

        public constructor(init?: Partial<EmptyResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class ListEndUserChatMemoryResponse extends ResponseBase
    {
        public notes: EndUserChatMemoryNote[] = [];

        public constructor(init?: Partial<ListEndUserChatMemoryResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEndUserChatAvailabilityResponse extends ResponseBase
    {
        public enabled: boolean;
        public available: boolean;
        public reason?: string;
        public defaultAssistantId?: string;
        public assistants: EndUserChatAssistant[] = [];
        public plan?: EndUserChatPlan;

        public constructor(init?: Partial<GetEndUserChatAvailabilityResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class ListEndUserChatSessionsResponse extends ResponseBase
    {
        public sessions: EndUserChatSession[] = [];

        public constructor(init?: Partial<ListEndUserChatSessionsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEndUserChatSessionResponse extends ResponseBase
    {
        public session?: EndUserChatSession;

        public constructor(init?: Partial<GetEndUserChatSessionResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEndUserChatEntriesResponse extends ResponseBase
    {
        public sessionId?: string;
        public entries: AiChatEntryWireDto[] = [];
        public lastSeq: number;
        public hasMore: boolean;

        public constructor(init?: Partial<GetEndUserChatEntriesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class StartEndUserChatTurnResponse extends ResponseBase
    {
        public turnId?: string;
        public sessionId?: string;
        public channel?: string;

        public constructor(init?: Partial<StartEndUserChatTurnResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetEndUserAiToolsResponse extends ResponseBase
    {
        public tools?: EndUserAiTool[];

        public constructor(init?: Partial<GetEndUserAiToolsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class InvokeEndUserAiToolResponse extends ResponseBase
    {
        public result?: string;

        public constructor(init?: Partial<InvokeEndUserAiToolResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetUserResponse extends ResponseBase
    {
        public user?: AuthDto;

        public constructor(init?: Partial<GetUserResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetUsersResponse extends ResponseBase
    {
        public list?: PaginatedResponse<AuthDto>;

        public constructor(init?: Partial<GetUsersResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetUserPreferencesResponse extends ResponseBase
    {
        public preferences?: UserMarketingPreferencesDto;

        public constructor(init?: Partial<GetUserPreferencesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class PasskeyOkResponse extends ResponseBase
    {

        public constructor(init?: Partial<PasskeyOkResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class PasskeyCeremonyOptionsResponse extends ResponseBase
    {
        public ceremonyId: string;
        public optionsJson: string;

        public constructor(init?: Partial<PasskeyCeremonyOptionsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class PasskeyAuthTokensResponse extends ResponseBase
    {
        public accessToken: string;
        public refreshToken: string;
        public expiresInSeconds: number;
        public recoveryCodes?: string[];

        public constructor(init?: Partial<PasskeyAuthTokensResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class PasskeyListResponse extends ResponseBase
    {
        public passkeys: PasskeyListItemDto[] = [];

        public constructor(init?: Partial<PasskeyListResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class PasskeyRecoveryResponse extends ResponseBase
    {
        public accessToken: string;
        public refreshToken: string;
        public expiresInSeconds: number;
        public remainingCodes: number;

        public constructor(init?: Partial<PasskeyRecoveryResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class PasskeyVerificationTokenResponse extends ResponseBase
    {
        public verificationToken: string;

        public constructor(init?: Partial<PasskeyVerificationTokenResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class FindMergedTermTreeResponse extends ResponseBase
    {
        public tree?: TermTreeDto[];

        public constructor(init?: Partial<FindMergedTermTreeResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class FindTaxonomyTreeResponse extends ResponseBase
    {
        public tree?: TaxonomyTreeDto[];

        public constructor(init?: Partial<FindTaxonomyTreeResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class FindTermsResponse extends ResponseBase
    {
        public list?: PaginatedResponse<TermDto>;

        public constructor(init?: Partial<FindTermsResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class FindTermsChildrenResponse extends ResponseBase
    {
        public list?: PaginatedResponse<TermDto>;

        public constructor(init?: Partial<FindTermsChildrenResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class FindTermTreeResponse extends ResponseBase
    {
        public tree?: TermTreeDto[];

        public constructor(init?: Partial<FindTermTreeResponse>) { super(init); (Object as any).assign(this, init); }
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

    export class AggregateResponse extends ResponseBase
    {
        public result?: Object[];

        public constructor(init?: Partial<AggregateResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class CountResponse extends ResponseBase
    {
        public count: number;

        public constructor(init?: Partial<CountResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class DistinctResponse extends ResponseBase
    {
        public values?: Object[];

        public constructor(init?: Partial<DistinctResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class ExecuteAggregateResponse extends ResponseBase
    {
        public result?: Object[];

        public constructor(init?: Partial<ExecuteAggregateResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class FindResponse extends ResponseBase
    {
        public list?: PaginatedResponse<Object>;

        public constructor(init?: Partial<FindResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class FindOneResponse extends ResponseBase
    {
        public result?: Object;

        public constructor(init?: Partial<FindOneResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetFileInfoResponse extends ResponseBase
    {
        public file?: FileResourceRefDto;
        public isPublic?: boolean;
        public publicUrl?: string;

        public constructor(init?: Partial<GetFileInfoResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class GetSignedUrlResponse extends ResponseBase
    {
        public url?: string;

        public constructor(init?: Partial<GetSignedUrlResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class ListFilesResponse extends ResponseBase
    {
        public list?: PaginatedResponse<FileResourceRefDto>;
        public folders?: IList<string>;
        public publicFolders?: IList<PublicFolderDto>;

        public constructor(init?: Partial<ListFilesResponse>) { super(init); (Object as any).assign(this, init); }
    }

    export class RequestUploadUrlResponse extends ResponseBase
    {
        public url?: string;

        public constructor(init?: Partial<RequestUploadUrlResponse>) { super(init); (Object as any).assign(this, init); }
    }

    // @DataContract
    export class TestFilesIntegrationResponse extends ResponseBase
    {
        // @DataMember
        public items?: IReadOnlyList<IntegrationTestResultItemDto>;

        public constructor(init?: Partial<TestFilesIntegrationResponse>) { super(init); (Object as any).assign(this, init); }
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

    // @Route("/{version}/echo", "GET")
    export class Echo extends RequestBase implements IReturn<EchoResponse>
    {

        public constructor(init?: Partial<Echo>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'Echo'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new EchoResponse(); }
    }

    // @Route("/{version}/public/projects/{ProjectId}/brand/{Kind}", "GET")
    export class GetPublicProjectBrandAsset extends RequestBase implements IReturn<Blob>
    {
        public projectId?: string;
        public kind?: string;
        public v?: string;

        public constructor(init?: Partial<GetPublicProjectBrandAsset>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPublicProjectBrandAsset'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new Blob(); }
    }

    // @Route("/{version}/public/projects/{ProjectId}/config", "GET")
    export class GetPublicProjectConfig extends RequestBase implements IReturn<PublicProjectConfigDto>
    {
        public projectId?: string;

        public constructor(init?: Partial<GetPublicProjectConfig>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPublicProjectConfig'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new PublicProjectConfigDto(); }
    }

    // @Route("/{version}/public/projects/{ProjectId}/legal/{Kind}", "GET")
    export class GetPublicProjectLegal extends RequestBase implements IReturn<PublicLegalDocumentDto>
    {
        public projectId?: string;
        public kind?: string;

        public constructor(init?: Partial<GetPublicProjectLegal>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPublicProjectLegal'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new PublicLegalDocumentDto(); }
    }

    /** @description Adds a file to one of the caller's own AI chats. */
    // @Route("/{version}/ai/chat/sessions/{SessionId}/attachments", "POST")
    // @Api(Description="Adds a file to one of the caller's own AI chats.")
    export class UploadEndUserChatAttachmentRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        public sessionId: string;
        public fileName: string;
        public contentType: string;
        public base64Content: string;

        public constructor(init?: Partial<UploadEndUserChatAttachmentRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UploadEndUserChatAttachmentRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Lists the files in one of the caller's own AI chats. */
    // @Route("/{version}/ai/chat/sessions/{SessionId}/attachments", "GET")
    // @Api(Description="Lists the files in one of the caller's own AI chats.")
    export class ListEndUserChatAttachmentsRequest extends CodeMashRequestBase implements IReturn<ListEndUserChatAttachmentsResponse>
    {
        public sessionId: string;

        public constructor(init?: Partial<ListEndUserChatAttachmentsRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ListEndUserChatAttachmentsRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new ListEndUserChatAttachmentsResponse(); }
    }

    /** @description Removes a file from one of the caller's own AI chats. */
    // @Route("/{version}/ai/chat/attachments/{AttachmentId}", "DELETE")
    // @Api(Description="Removes a file from one of the caller's own AI chats.")
    export class DeleteEndUserChatAttachmentRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public attachmentId: string;

        public constructor(init?: Partial<DeleteEndUserChatAttachmentRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteEndUserChatAttachmentRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Likes, dislikes or clears one message of the caller's own AI chat. */
    // @Route("/{version}/ai/chat/sessions/{SessionId}/entries/{EntryId}/feedback", "PUT")
    // @Api(Description="Likes, dislikes or clears one message of the caller's own AI chat.")
    export class SetEndUserChatEntryFeedbackRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public sessionId: string;
        public entryId: string;
        public feedback?: string;

        public constructor(init?: Partial<SetEndUserChatEntryFeedbackRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SetEndUserChatEntryFeedbackRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Lists what the AI chat remembers about the caller. */
    // @Route("/{version}/ai/chat/memory", "GET")
    // @Api(Description="Lists what the AI chat remembers about the caller.")
    export class ListEndUserChatMemoryRequest extends CodeMashRequestBase implements IReturn<ListEndUserChatMemoryResponse>
    {
        public take?: number;

        public constructor(init?: Partial<ListEndUserChatMemoryRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ListEndUserChatMemoryRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new ListEndUserChatMemoryResponse(); }
    }

    /** @description Forgets one thing the AI chat remembers about the caller. */
    // @Route("/{version}/ai/chat/memory/{NoteId}", "DELETE")
    // @Api(Description="Forgets one thing the AI chat remembers about the caller.")
    export class ForgetEndUserChatMemoryRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public noteId: string;

        public constructor(init?: Partial<ForgetEndUserChatMemoryRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ForgetEndUserChatMemoryRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Whether the AI chat can run for the caller, and which assistants it offers. */
    // @Route("/{version}/ai/chat/availability", "GET")
    // @Api(Description="Whether the AI chat can run for the caller, and which assistants it offers.")
    export class GetEndUserChatAvailabilityRequest extends CodeMashRequestBase implements IReturn<GetEndUserChatAvailabilityResponse>
    {

        public constructor(init?: Partial<GetEndUserChatAvailabilityRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEndUserChatAvailabilityRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEndUserChatAvailabilityResponse(); }
    }

    /** @description Lists the caller's own AI chats. */
    // @Route("/{version}/ai/chat/sessions", "GET")
    // @Api(Description="Lists the caller's own AI chats.")
    export class ListEndUserChatSessionsRequest extends CodeMashRequestBase implements IReturn<ListEndUserChatSessionsResponse>
    {
        public take?: number;
        public includeArchived: boolean;

        public constructor(init?: Partial<ListEndUserChatSessionsRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ListEndUserChatSessionsRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new ListEndUserChatSessionsResponse(); }
    }

    /** @description Opens a new AI chat for the caller. */
    // @Route("/{version}/ai/chat/sessions", "POST")
    // @Api(Description="Opens a new AI chat for the caller.")
    export class CreateEndUserChatSessionRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        public assistantId?: string;
        public title?: string;

        public constructor(init?: Partial<CreateEndUserChatSessionRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CreateEndUserChatSessionRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Returns one of the caller's own AI chats. */
    // @Route("/{version}/ai/chat/sessions/{SessionId}", "GET")
    // @Api(Description="Returns one of the caller's own AI chats.")
    export class GetEndUserChatSessionRequest extends CodeMashRequestBase implements IReturn<GetEndUserChatSessionResponse>
    {
        public sessionId: string;

        public constructor(init?: Partial<GetEndUserChatSessionRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEndUserChatSessionRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEndUserChatSessionResponse(); }
    }

    /** @description Renames one of the caller's own AI chats. */
    // @Route("/{version}/ai/chat/sessions/{SessionId}", "PATCH")
    // @Api(Description="Renames one of the caller's own AI chats.")
    export class RenameEndUserChatSessionRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public sessionId: string;
        public title?: string;

        public constructor(init?: Partial<RenameEndUserChatSessionRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RenameEndUserChatSessionRequest'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Pins or unpins one of the caller's own AI chats. */
    // @Route("/{version}/ai/chat/sessions/{SessionId}/pin", "PUT")
    // @Api(Description="Pins or unpins one of the caller's own AI chats.")
    export class PinEndUserChatSessionRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public sessionId: string;
        public pinned: boolean;

        public constructor(init?: Partial<PinEndUserChatSessionRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'PinEndUserChatSessionRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Archives or unarchives one of the caller's own AI chats. */
    // @Route("/{version}/ai/chat/sessions/{SessionId}/archive", "PUT")
    // @Api(Description="Archives or unarchives one of the caller's own AI chats.")
    export class ArchiveEndUserChatSessionRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public sessionId: string;
        public archived: boolean;

        public constructor(init?: Partial<ArchiveEndUserChatSessionRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ArchiveEndUserChatSessionRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Deletes one of the caller's own AI chats. */
    // @Route("/{version}/ai/chat/sessions/{SessionId}", "DELETE")
    // @Api(Description="Deletes one of the caller's own AI chats.")
    export class DeleteEndUserChatSessionRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public sessionId: string;

        public constructor(init?: Partial<DeleteEndUserChatSessionRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteEndUserChatSessionRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Returns a page of one of the caller's own AI chat transcripts. */
    // @Route("/{version}/ai/chat/sessions/{SessionId}/entries", "GET")
    // @Api(Description="Returns a page of one of the caller's own AI chat transcripts.")
    export class GetEndUserChatEntriesRequest extends CodeMashRequestBase implements IReturn<GetEndUserChatEntriesResponse>
    {
        public sessionId: string;
        public afterSeq?: number;
        public take?: number;

        public constructor(init?: Partial<GetEndUserChatEntriesRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEndUserChatEntriesRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEndUserChatEntriesResponse(); }
    }

    /** @description Sends a message to the AI chat; the answer streams on the caller's channel. */
    // @Route("/{version}/ai/chat/turn", "POST")
    // @Api(Description="Sends a message to the AI chat; the answer streams on the caller's channel.")
    export class StartEndUserChatTurnRequest extends CodeMashRequestBase implements IReturn<StartEndUserChatTurnResponse>
    {
        public sessionId?: string;
        public assistantId?: string;
        public message: string;

        public constructor(init?: Partial<StartEndUserChatTurnRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'StartEndUserChatTurnRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new StartEndUserChatTurnResponse(); }
    }

    /** @description Lists the AI tools a project user may use: only their own data (own:* toolsets). */
    // @Route("/{version}/ai/tools", "GET")
    // @Api(Description="Lists the AI tools a project user may use: only their own data (own:* toolsets).")
    export class GetEndUserAiToolsRequest extends RequestBase implements IReturn<GetEndUserAiToolsResponse>
    {

        public constructor(init?: Partial<GetEndUserAiToolsRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetEndUserAiToolsRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetEndUserAiToolsResponse(); }
    }

    /** @description Invokes one own-scope AI tool as the calling project user. */
    // @Route("/{version}/ai/tools/{ToolName}", "POST")
    // @Api(Description="Invokes one own-scope AI tool as the calling project user.")
    export class InvokeEndUserAiToolRequest extends RequestBase implements IReturn<InvokeEndUserAiToolResponse>
    {
        public toolName: string;
        public argumentsJson?: string;

        public constructor(init?: Partial<InvokeEndUserAiToolRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'InvokeEndUserAiToolRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new InvokeEndUserAiToolResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/block", "PATCH")
    // @Api(Description="Membership")
    // @DataContract
    export class BlockUserRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Id of the user to block, from get_users. */
        // @DataMember
        // @ApiMember(Description="Id of the user to block, from get_users.", IsRequired=true)
        public id: string;

        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<BlockUserRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'BlockUserRequest'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/register/service", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class SaveSystemUserWithPermissions extends SaveUserWithRolesBase implements IReturn<IdResponse>
    {

        public constructor(init?: Partial<SaveSystemUserWithPermissions>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveSystemUserWithPermissions'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/register/guest", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class SaveGuestUser extends SaveUser implements IReturn<IdResponse>
    {

        public constructor(init?: Partial<SaveGuestUser>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveGuestUser'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/register/user-name", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class SaveUserNameUser extends SaveUser implements IReturn<IdResponse>
    {
        // @DataMember
        public password: string;

        // @DataMember
        public userName: string;

        public constructor(init?: Partial<SaveUserNameUser>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveUserNameUser'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/register/email", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class SaveEmailUser extends SaveUser implements IReturn<IdResponse>
    {
        // @DataMember
        public password: string;

        // @DataMember
        public email: string;

        public constructor(init?: Partial<SaveEmailUser>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveEmailUser'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/register/phone", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class SavePhoneUser extends SaveUser implements IReturn<IdResponse>
    {
        /** @description Phone number for the new user, in E.164 format. */
        // @DataMember
        // @ApiMember(Description="Phone number for the new user, in E.164 format.", IsRequired=true)
        public phone: string;

        public constructor(init?: Partial<SavePhoneUser>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SavePhoneUser'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/register/phone-with-permissions", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class SavePhoneUserNameWithPermissions extends SaveUserWithRolesBase implements IReturn<IdResponse>
    {
        // @DataMember
        public phone: string;

        public constructor(init?: Partial<SavePhoneUserNameWithPermissions>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SavePhoneUserNameWithPermissions'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/register/email-with-permissions", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class SaveEmailUserNameWithPermissions extends SaveUserWithRolesBase implements IReturn<IdResponse>
    {
        // @DataMember
        public password: string;

        // @DataMember
        public email: string;

        public constructor(init?: Partial<SaveEmailUserNameWithPermissions>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveEmailUserNameWithPermissions'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/register/user-name-with-permissions", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class SaveUserNameWithPermissions extends SaveUserWithRolesBase implements IReturn<IdResponse>
    {
        // @DataMember
        public password: string;

        // @DataMember
        public userName: string;

        public constructor(init?: Partial<SaveUserNameWithPermissions>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SaveUserNameWithPermissions'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth", "DELETE")
    // @Api(Description="Membership")
    // @DataContract
    export class DeleteUserRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Id of the user to delete, from get_users. */
        // @DataMember
        // @ApiMember(Description="Id of the user to delete, from get_users.", IsRequired=true)
        public id: string;

        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<DeleteUserRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteUserRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/{id}", "GET")
    // @Api(Description="Membership")
    // @DataContract
    export class GetUserRequest extends CodeMashRequestBase implements IReturn<GetUserResponse>
    {
        /** @description Id of the user to fetch, from get_users. */
        // @DataMember
        // @ApiMember(Description="Id of the user to fetch, from get_users.", IsRequired=true)
        public id: string;

        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<GetUserRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetUserRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetUserResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth", "GET")
    // @Api(Description="Membership")
    // @DataContract
    export class GetUsersRequest extends CodeMashListPaginationRequestBase implements IReturn<GetUsersResponse>
    {
        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        /** @description Include each user's effective permissions in the result. */
        // @DataMember
        // @ApiMember(Description="Include each user's effective permissions in the result.")
        public includePermissions: boolean;

        /** @description Only return users that have a registered push device. */
        // @DataMember
        // @ApiMember(Description="Only return users that have a registered push device.")
        public userShouldHavePushDevice: boolean;

        /** @description Only return users that have an email address. */
        // @DataMember
        // @ApiMember(Description="Only return users that have an email address.")
        public userShouldHaveEmail: boolean;

        /** @description Include each user's metadata in the result. */
        // @DataMember
        // @ApiMember(Description="Include each user's metadata in the result.")
        public includeMeta: boolean;

        /** @description Filter to users that have any of these role names. */
        // @DataMember
        // @ApiMember(Description="Filter to users that have any of these role names.")
        public roleNames?: string[];

        /** @description Filter to these specific user ids. */
        // @DataMember
        // @ApiMember(Description="Filter to these specific user ids.")
        public userIds?: string[];

        public constructor(init?: Partial<GetUsersRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetUsersRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetUsersResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/{id}/preferences", "GET")
    // @Api(Description="Membership")
    // @DataContract
    export class GetUserPreferencesRequest extends CodeMashRequestBase implements IReturn<GetUserPreferencesResponse>
    {
        /** @description Id of the user whose preferences to fetch, from get_users. */
        // @DataMember
        // @ApiMember(Description="Id of the user whose preferences to fetch, from get_users.", IsRequired=true)
        public id: string;

        /** @description Database integration id. Optional — defaults to the project's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the project's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<GetUserPreferencesRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetUserPreferencesRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetUserPreferencesResponse(); }
    }

    // @Route("/{version}/membership/users/{contactId}/marketing-state/{channel}/consent", "POST")
    export class GrantContactConsentRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Id of the user (contact) to grant consent for. */
        // @ApiMember(Description="Id of the user (contact) to grant consent for.", IsRequired=true)
        public contactId: string;

        /** @description Delivery channel to grant consent on: Email, Sms, or Push. */
        // @ApiMember(Description="Delivery channel to grant consent on: Email, Sms, or Push.", IsRequired=true)
        public channel: string;

        /** @description Lawful basis for the consent, e.g. Consent. Defaults to Consent. */
        // @ApiMember(Description="Lawful basis for the consent, e.g. Consent. Defaults to Consent.")
        public lawfulBasis: string;

        /** @description Source of the consent, e.g. UserOptIn. Defaults to UserOptIn. */
        // @ApiMember(Description="Source of the consent, e.g. UserOptIn. Defaults to UserOptIn.")
        public source: string;

        /** @description Optional free-text reference to evidence of consent (e.g. a form submission id). */
        // @ApiMember(Description="Optional free-text reference to evidence of consent (e.g. a form submission id).")
        public evidenceRef?: string;

        public constructor(init?: Partial<GrantContactConsentRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GrantContactConsentRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/invite", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class InviteUserRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Email address the invitation is sent to. */
        // @DataMember
        // @ApiMember(Description="Email address the invitation is sent to.", IsRequired=true)
        public email: string;

        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<InviteUserRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'InviteUserRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/{userId}/link-identity", "POST")
    // @Api(Description="Membership")
    // @DataContract
    export class LinkIdentityRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public userId: string;

        // @DataMember
        public provider: string;

        // @DataMember
        public providerToken: string;

        // @DataMember
        public emailToVerify?: string;

        // @DataMember
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<LinkIdentityRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'LinkIdentityRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/users/{userId}/map-auth", "POST")
    // @Api(Description="Membership")
    export class MapAuthToUserRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        public userId: string;
        public authId: string;
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<MapAuthToUserRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'MapAuthToUserRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/assign-roles", "PUT")
    // @Api(Description="Membership")
    // @DataContract
    export class AssignRolePermissionsRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Id of the user login to assign roles to, from get_users. */
        // @DataMember
        // @ApiMember(Description="Id of the user login to assign roles to, from get_users.", IsRequired=true)
        public id: string;

        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        /** @description The complete new list of role names (full replacement), from get_roles. */
        // @DataMember
        // @ApiMember(Description="The complete new list of role names (full replacement), from get_roles.")
        public roles?: string[];

        public constructor(init?: Partial<AssignRolePermissionsRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'AssignRolePermissionsRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/users/{userId}/roles", "PUT")
    // @Api(Description="Membership")
    // @DataContract
    export class SetContactRolesRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Id of the human user to assign roles to. */
        // @DataMember
        // @ApiMember(Description="Id of the human user to assign roles to.", IsRequired=true)
        public userId: string;

        /** @description The complete new list of role ids (full replacement), from get_roles. Empty/omitted clears all roles. */
        // @DataMember
        // @ApiMember(Description="The complete new list of role ids (full replacement), from get_roles. Empty/omitted clears all roles.")
        public roles?: string[];

        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<SetContactRolesRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SetContactRolesRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/membership/users/{contactId}/marketing-state/{commChannel}/{channel}/tags/{tag}", "PUT")
    export class SetContactTagSubscriptionRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Id of the user (contact) to update. */
        // @ApiMember(Description="Id of the user (contact) to update.", IsRequired=true)
        public contactId: string;

        /** @description Communication channel type: Marketing or Transactional. */
        // @ApiMember(Description="Communication channel type: Marketing or Transactional.", IsRequired=true)
        public commChannel: string;

        /** @description Delivery channel: Email, Sms, or Push. */
        // @ApiMember(Description="Delivery channel: Email, Sms, or Push.", IsRequired=true)
        public channel: string;

        /** @description The tag name; must already exist for the communication channel. */
        // @ApiMember(Description="The tag name; must already exist for the communication channel.", IsRequired=true)
        public tag: string;

        /** @description True to subscribe (unblock) the tag, false to block it. */
        // @ApiMember(Description="True to subscribe (unblock) the tag, false to block it.")
        public subscribed: boolean;

        public constructor(init?: Partial<SetContactTagSubscriptionRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'SetContactTagSubscriptionRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/unblock", "PATCH")
    // @Api(Description="Membership")
    // @DataContract
    export class UnblockUserRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Id of the user to unblock, from get_users. */
        // @DataMember
        // @ApiMember(Description="Id of the user to unblock, from get_users.", IsRequired=true)
        public id: string;

        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<UnblockUserRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UnblockUserRequest'; }
        public getMethod() { return 'PATCH'; }
        public createResponse() { return new EmptyResponse(); }
    }

    // @Route("/{version}/membership/users/{contactId}/marketing-state/{channel}/unsubscribe", "POST")
    export class UnsubscribeContactRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Id of the user (contact) to unsubscribe. */
        // @ApiMember(Description="Id of the user (contact) to unsubscribe.", IsRequired=true)
        public contactId: string;

        /** @description Delivery channel to unsubscribe from: Email, Sms, or Push. */
        // @ApiMember(Description="Delivery channel to unsubscribe from: Email, Sms, or Push.", IsRequired=true)
        public channel: string;

        /** @description Optional suppression reason name explaining why consent was revoked. */
        // @ApiMember(Description="Optional suppression reason name explaining why consent was revoked.")
        public reason?: string;

        public constructor(init?: Partial<UnsubscribeContactRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UnsubscribeContactRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth", "PUT")
    // @Api(Description="Membership")
    // @DataContract
    export class UpdateUserRequest extends SaveUser implements IReturn<IdResponse>
    {
        /** @description Id of the user to update, from get_users. */
        // @DataMember
        // @ApiMember(Description="Id of the user to update, from get_users.", IsRequired=true)
        public id: string;

        public constructor(init?: Partial<UpdateUserRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateUserRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Membership */
    // @Route("/{version}/membership/auth/{id}/preferences", "PUT")
    // @Api(Description="Membership")
    // @DataContract
    export class UpdateUserPreferencesRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        /** @description Id of the user to update, from get_users. */
        // @DataMember
        // @ApiMember(Description="Id of the user to update, from get_users.", IsRequired=true)
        public id: string;

        /** @description When true, blocks all marketing messages to this user. */
        // @DataMember
        // @ApiMember(Description="When true, blocks all marketing messages to this user.")
        public blockAllMarketingMessages: boolean;

        /** @description Per communication channel, the set of tags blocked for this user. Full replacement. */
        // @DataMember
        // @ApiMember(Description="Per communication channel, the set of tags blocked for this user. Full replacement.")
        public blockedTags?: { [index:string]: HashSet<string>; };

        /** @description Database integration id. Optional — defaults to the project's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the project's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<UpdateUserPreferencesRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateUserPreferencesRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Membership · Password */
    // @Route("/{version}/membership/userauth/password/change", "POST")
    // @Api(Description="Membership · Password")
    // @DataContract
    export class ChangePasswordRequest extends CodeMashRequestBase implements IReturn<PasskeyOkResponse>
    {
        /** @description The member's current password. */
        // @DataMember
        // @ApiMember(Description="The member's current password.", IsRequired=true)
        public currentPassword: string;

        /** @description The new password. Validated against the project's complexity policy. */
        // @DataMember
        // @ApiMember(Description="The new password. Validated against the project's complexity policy.", IsRequired=true)
        public newPassword: string;

        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<ChangePasswordRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ChangePasswordRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyOkResponse(); }
    }

    /** @description Membership · Password */
    // @Route("/{version}/membership/userauth/password/reset/request", "POST")
    // @Api(Description="Membership · Password")
    // @DataContract
    export class RequestPasswordResetRequest extends CodeMashRequestBase implements IReturn<PasskeyOkResponse>
    {
        /** @description Email address to send the reset link to. */
        // @DataMember
        // @ApiMember(Description="Email address to send the reset link to.", IsRequired=true)
        public email: string;

        public constructor(init?: Partial<RequestPasswordResetRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RequestPasswordResetRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyOkResponse(); }
    }

    /** @description Membership · Password */
    // @Route("/{version}/membership/userauth/password/reset/confirm", "POST")
    // @Api(Description="Membership · Password")
    // @DataContract
    export class ConfirmPasswordResetRequest extends CodeMashRequestBase implements IReturn<PasskeyOkResponse>
    {
        /** @description One-time reset token from the email link. */
        // @DataMember
        // @ApiMember(Description="One-time reset token from the email link.", IsRequired=true)
        public token: string;

        /** @description The new password. Validated against the project's complexity policy. */
        // @DataMember
        // @ApiMember(Description="The new password. Validated against the project's complexity policy.", IsRequired=true)
        public newPassword: string;

        /** @description Database integration id. Optional — defaults to the request environment's default integration. */
        // @DataMember
        // @ApiMember(Description="Database integration id. Optional — defaults to the request environment's default integration.")
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<ConfirmPasswordResetRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ConfirmPasswordResetRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyOkResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/passkey/authentication-options", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class PasskeyAuthenticationOptionsRequest extends CodeMashRequestBase implements IReturn<PasskeyCeremonyOptionsResponse>, IPasskeyCeremonyRequest
    {
        // @DataMember
        public email: string;

        public constructor(init?: Partial<PasskeyAuthenticationOptionsRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'PasskeyAuthenticationOptionsRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyCeremonyOptionsResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/passkey/verify-authentication", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class VerifyPasskeyAuthenticationRequest extends CodeMashRequestBase implements IReturn<PasskeyAuthTokensResponse>, IPasskeyCeremonyRequest
    {
        // @DataMember
        public ceremonyId: string;

        // @DataMember
        public assertionResponse: string;

        public constructor(init?: Partial<VerifyPasskeyAuthenticationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'VerifyPasskeyAuthenticationRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyAuthTokensResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/passkeys", "GET")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class ListPasskeysRequest extends CodeMashRequestBase implements IReturn<PasskeyListResponse>
    {

        public constructor(init?: Partial<ListPasskeysRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ListPasskeysRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new PasskeyListResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/passkeys/{CredentialId}/rename", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class RenamePasskeyRequest extends CodeMashRequestBase implements IReturn<PasskeyOkResponse>
    {
        /** @description Base64 credential id of the passkey to rename, from list_passkeys. */
        // @DataMember
        // @ApiMember(Description="Base64 credential id of the passkey to rename, from list_passkeys.", IsRequired=true)
        public credentialId: string;

        /** @description The new friendly name for the passkey. */
        // @DataMember
        // @ApiMember(Description="The new friendly name for the passkey.", IsRequired=true)
        public friendlyName: string;

        public constructor(init?: Partial<RenamePasskeyRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RenamePasskeyRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyOkResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/passkeys/{CredentialId}/revoke", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class RevokePasskeyRequest extends CodeMashRequestBase implements IReturn<PasskeyOkResponse>
    {
        /** @description Base64 credential id of the passkey to revoke, from list_passkeys. */
        // @DataMember
        // @ApiMember(Description="Base64 credential id of the passkey to revoke, from list_passkeys.", IsRequired=true)
        public credentialId: string;

        public constructor(init?: Partial<RevokePasskeyRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RevokePasskeyRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyOkResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/recovery/use-code", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class UseRecoveryCodeRequest extends CodeMashRequestBase implements IReturn<PasskeyRecoveryResponse>
    {
        // @DataMember
        public email: string;

        // @DataMember
        public recoveryCode: string;

        public constructor(init?: Partial<UseRecoveryCodeRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UseRecoveryCodeRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyRecoveryResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/recovery/magic-link/request", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class RequestMagicLinkRequest extends CodeMashRequestBase implements IReturn<PasskeyOkResponse>
    {
        // @DataMember
        public email: string;

        public constructor(init?: Partial<RequestMagicLinkRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RequestMagicLinkRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyOkResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/recovery/magic-link/consume", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class ConsumeMagicLinkRequest extends CodeMashRequestBase implements IReturn<PasskeyRecoveryResponse>
    {
        // @DataMember
        public token: string;

        public constructor(init?: Partial<ConsumeMagicLinkRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ConsumeMagicLinkRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyRecoveryResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/has-passkey", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class HasPasskeyRequest extends CodeMashRequestBase implements IReturn<PasskeyOkResponse>
    {
        // @DataMember
        public email: string;

        public constructor(init?: Partial<HasPasskeyRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'HasPasskeyRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyOkResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/email/start-verification", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class StartEmailVerificationRequest extends CodeMashRequestBase implements IReturn<PasskeyOkResponse>
    {
        // @DataMember
        public email: string;

        public constructor(init?: Partial<StartEmailVerificationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'StartEmailVerificationRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyOkResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/email/confirm-verification", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class ConfirmEmailVerificationRequest extends CodeMashRequestBase implements IReturn<PasskeyVerificationTokenResponse>
    {
        // @DataMember
        public email: string;

        // @DataMember
        public code: string;

        public constructor(init?: Partial<ConfirmEmailVerificationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ConfirmEmailVerificationRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyVerificationTokenResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/passkey/registration-options", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class PasskeyRegistrationOptionsRequest extends CodeMashRequestBase implements IReturn<PasskeyCeremonyOptionsResponse>, IPasskeyCeremonyRequest
    {
        // @DataMember
        public verificationToken: string;

        public constructor(init?: Partial<PasskeyRegistrationOptionsRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'PasskeyRegistrationOptionsRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyCeremonyOptionsResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/passkey/verify-registration", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class VerifyPasskeyRegistrationRequest extends CodeMashRequestBase implements IReturn<PasskeyAuthTokensResponse>, IPasskeyCeremonyRequest
    {
        // @DataMember
        public verificationToken: string;

        // @DataMember
        public ceremonyId: string;

        // @DataMember
        public attestationResponse: string;

        // @DataMember
        public friendlyName?: string;

        public constructor(init?: Partial<VerifyPasskeyRegistrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'VerifyPasskeyRegistrationRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyAuthTokensResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/token/refresh", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class RefreshPasskeyTokenRequest extends CodeMashRequestBase implements IReturn<PasskeyAuthTokensResponse>
    {
        // @DataMember
        public refreshToken?: string;

        public constructor(init?: Partial<RefreshPasskeyTokenRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RefreshPasskeyTokenRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyAuthTokensResponse(); }
    }

    /** @description Membership · Passkey */
    // @Route("/{version}/membership/userauth/logout", "POST")
    // @Api(Description="Membership · Passkey")
    // @DataContract
    export class PasskeyLogoutRequest extends CodeMashRequestBase implements IReturn<PasskeyOkResponse>
    {
        // @DataMember
        public refreshToken?: string;

        public constructor(init?: Partial<PasskeyLogoutRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'PasskeyLogoutRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new PasskeyOkResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/taxonomies/{taxonomyName}/merged-tree", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class FindMergedTermTreeRequest extends CodeMashRequestBase implements IReturn<FindMergedTermTreeResponse>
    {
        // @DataMember
        public taxonomyName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<FindMergedTermTreeRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'FindMergedTermTreeRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new FindMergedTermTreeResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/taxonomies/tree", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class FindTaxonomyTreeRequest extends CodeMashRequestBase implements IReturn<FindTaxonomyTreeResponse>
    {
        // @DataMember
        public includeTerms: boolean;

        // @DataMember
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<FindTaxonomyTreeRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'FindTaxonomyTreeRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new FindTaxonomyTreeResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/taxonomies/{taxonomyName}/terms", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class FindTermsRequest extends CodeMashListPaginationRequestBase implements IReturn<FindTermsResponse>
    {
        // @DataMember
        public taxonomyName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public filter?: string;

        // @DataMember
        public sortDescending: boolean;

        // @DataMember
        public pagingArgs?: PagingArgs;

        public constructor(init?: Partial<FindTermsRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'FindTermsRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new FindTermsResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/taxonomies/{taxonomyName}/terms/{parentId}/children", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class FindTermsChildrenRequest extends CodeMashListPaginationRequestBase implements IReturn<FindTermsChildrenResponse>
    {
        // @DataMember
        public taxonomyName: string;

        // @DataMember
        public parentId: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public filter?: string;

        // @DataMember
        public pagingArgs?: PagingArgs;

        public constructor(init?: Partial<FindTermsChildrenRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'FindTermsChildrenRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new FindTermsChildrenResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/taxonomies/{taxonomyName}/terms/tree", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class FindTermTreeRequest extends CodeMashRequestBase implements IReturn<FindTermTreeResponse>
    {
        // @DataMember
        public taxonomyName: string;

        // @DataMember
        public rootTermId?: string;

        // @DataMember
        public depth?: number;

        // @DataMember
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<FindTermTreeRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'FindTermTreeRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new FindTermTreeResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/schemas/{id}", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class GetDatabaseSchemaRequest extends CodeMashRequestBase implements IReturn<GetDatabaseSchemaResponse>
    {
        // @DataMember
        public id: string;

        public constructor(init?: Partial<GetDatabaseSchemaRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseSchemaRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseSchemaResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/schemas", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class GetDatabaseSchemasRequest extends CodeMashListPaginationRequestBase implements IReturn<GetDatabaseSchemasResponse>
    {
        // @DataMember
        public pagingArgs?: PagingArgs;

        public constructor(init?: Partial<GetDatabaseSchemasRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetDatabaseSchemasRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetDatabaseSchemasResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/aggregate", "POST")
    // @Api(Description="Database")
    // @DataContract
    export class AggregateRequest extends CodeMashRequestBase implements IReturn<AggregateResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public pipeline: string;

        public constructor(init?: Partial<AggregateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'AggregateRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new AggregateResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/{id}/responsibility", "PUT")
    // @Api(Description="Database")
    // @DataContract
    export class ChangeResponsibilityRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public id: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public newResponsibleUserId: string;

        public constructor(init?: Partial<ChangeResponsibilityRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ChangeResponsibilityRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/count", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class CountRequest extends CodeMashRequestBase implements IReturn<CountResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public filter?: string;

        // @DataMember
        public schemaVersion?: number;

        public constructor(init?: Partial<CountRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CountRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new CountResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/many", "DELETE")
    // @Api(Description="Database")
    // @DataContract
    export class DeleteManyRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public filter: string;

        // @DataMember
        public allRecords?: boolean;

        public constructor(init?: Partial<DeleteManyRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteManyRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/{id}", "DELETE")
    // @Api(Description="Database")
    // @DataContract
    export class DeleteOneRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public id: string;

        // @DataMember
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<DeleteOneRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteOneRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/distinct", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class DistinctRequest extends CodeMashRequestBase implements IReturn<DistinctResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public field: string;

        // @DataMember
        public filter?: string;

        // @DataMember
        public schemaVersion?: number;

        public constructor(init?: Partial<DistinctRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DistinctRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new DistinctResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/aggregates/{aggregateId}/execute", "POST")
    // @Api(Description="Database")
    // @DataContract
    export class ExecuteAggregateRequest extends CodeMashRequestBase implements IReturn<ExecuteAggregateResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public aggregateId: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public tokens?: { [index:string]: string; };

        public constructor(init?: Partial<ExecuteAggregateRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ExecuteAggregateRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new ExecuteAggregateResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class FindRequest extends CodeMashListPaginationRequestBase implements IReturn<FindResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public filter?: string;

        // @DataMember
        public schemaVersion?: number;

        // @DataMember
        public pagingArgs?: PagingArgs;

        // @DataMember
        public sortBy?: string;

        // @DataMember
        public sortOrder?: number;

        public constructor(init?: Partial<FindRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'FindRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new FindResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/{id}", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class FindOneRequest extends CodeMashRequestBase implements IReturn<FindOneResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public id: string;

        // @DataMember
        public databaseIntegrationId?: string;

        public constructor(init?: Partial<FindOneRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'FindOneRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new FindOneResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/own", "GET")
    // @Api(Description="Database")
    // @DataContract
    export class FindOwnRequest extends CodeMashListPaginationRequestBase implements IReturn<FindResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public filter?: string;

        // @DataMember
        public schemaVersion?: number;

        // @DataMember
        public pagingArgs?: PagingArgs;

        public constructor(init?: Partial<FindOwnRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'FindOwnRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new FindResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/many", "POST")
    // @Api(Description="Database")
    // @DataContract
    export class InsertManyRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public documents: string;

        public constructor(init?: Partial<InsertManyRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'InsertManyRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}", "POST")
    // @Api(Description="Database")
    // @DataContract
    export class InsertOneRequest extends CodeMashRequestBase implements IReturn<IdResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public document: string;

        public constructor(init?: Partial<InsertOneRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'InsertOneRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new IdResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/{id}/replace", "PUT")
    // @Api(Description="Database")
    // @DataContract
    export class ReplaceOneRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public id: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public replacement: string;

        public constructor(init?: Partial<ReplaceOneRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ReplaceOneRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/many", "PUT")
    // @Api(Description="Database")
    // @DataContract
    export class UpdateManyRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public filter: string;

        // @DataMember
        public allRecords?: boolean;

        // @DataMember
        public update: string;

        public constructor(init?: Partial<UpdateManyRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateManyRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Database */
    // @Route("/{version}/database/collections/{collectionName}/{id}", "PUT")
    // @Api(Description="Database")
    // @DataContract
    export class UpdateOneRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public collectionName: string;

        // @DataMember
        public id: string;

        // @DataMember
        public databaseIntegrationId?: string;

        // @DataMember
        public update: string;

        public constructor(init?: Partial<UpdateOneRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'UpdateOneRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}/commit", "POST")
    // @Api(Description="Files")
    // @DataContract
    export class CommitUploadRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember
        public path: string;

        // @DataMember
        public contentType?: string;

        // @DataMember
        public sizeBytes?: number;

        // @DataMember
        public fileName?: string;

        public constructor(init?: Partial<CommitUploadRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'CommitUploadRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}/content", "GET")
    // @Api(Description="Files")
    // @DataContract
    export class GetFileContentRequest extends RequestBase implements IReturn<Blob>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember
        public path: string;

        // @DataMember
        public token?: string;

        public constructor(init?: Partial<GetFileContentRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetFileContentRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new Blob(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}/content", "PUT")
    // @Api(Description="Files")
    // @DataContract
    export class PutFileContentRequest extends RequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember
        public path: string;

        // @DataMember
        public token?: string;

        public constructor(init?: Partial<PutFileContentRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'PutFileContentRequest'; }
        public getMethod() { return 'PUT'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}", "DELETE")
    // @Api(Description="Files")
    // @DataContract
    export class DeleteFileApiRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember
        public path: string;

        public constructor(init?: Partial<DeleteFileApiRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteFileApiRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}/bulk", "DELETE")
    // @Api(Description="Files")
    // @DataContract
    export class DeleteManyFilesApiRequest extends CodeMashRequestBase implements IReturn<EmptyResponse>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember(Name="paths[]")
        public paths__: string[] = [];

        public constructor(init?: Partial<DeleteManyFilesApiRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DeleteManyFilesApiRequest'; }
        public getMethod() { return 'DELETE'; }
        public createResponse() { return new EmptyResponse(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}/download", "GET")
    // @Api(Description="Files")
    // @DataContract
    export class DownloadFileApiRequest extends CodeMashRequestBase implements IReturn<Blob>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember
        public path: string;

        public constructor(init?: Partial<DownloadFileApiRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'DownloadFileApiRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new Blob(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}/info", "GET")
    // @Api(Description="Files")
    // @DataContract
    export class GetFileInfoRequest extends CodeMashRequestBase implements IReturn<GetFileInfoResponse>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember
        public path: string;

        public constructor(init?: Partial<GetFileInfoRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetFileInfoRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetFileInfoResponse(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}/sign", "GET")
    // @Api(Description="Files")
    // @DataContract
    export class GetSignedUrlRequest extends CodeMashRequestBase implements IReturn<GetSignedUrlResponse>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember
        public path: string;

        // @DataMember
        public expirationSeconds?: number;

        public constructor(init?: Partial<GetSignedUrlRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetSignedUrlRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new GetSignedUrlResponse(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}", "GET")
    // @Api(Description="Files")
    // @DataContract
    export class ListFilesRequest extends CodeMashListPaginationRequestBase implements IReturn<ListFilesResponse>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember
        public path?: string;

        public constructor(init?: Partial<ListFilesRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'ListFilesRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new ListFilesResponse(); }
    }

    /** @description Files */
    // @Route("/{version}/files/public/{PublicId}/{Name*}", "GET")
    // @Api(Description="Files")
    // @DataContract
    export class GetPublicFileRequest extends RequestBase implements IReturn<Blob>
    {
        // @DataMember
        public publicId?: string;

        // @DataMember
        public name?: string;

        public constructor(init?: Partial<GetPublicFileRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'GetPublicFileRequest'; }
        public getMethod() { return 'GET'; }
        public createResponse() { return new Blob(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}/upload-url", "POST")
    // @Api(Description="Files")
    // @DataContract
    export class RequestUploadUrlRequest extends CodeMashRequestBase implements IReturn<RequestUploadUrlResponse>
    {
        // @DataMember
        public filesIntegrationId: string;

        // @DataMember
        public path: string;

        // @DataMember
        public contentType: string;

        // @DataMember
        public expirationSeconds?: number;

        public constructor(init?: Partial<RequestUploadUrlRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'RequestUploadUrlRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new RequestUploadUrlResponse(); }
    }

    /** @description Files */
    // @Route("/{version}/files/{filesIntegrationId}/test", "POST")
    // @Api(Description="Files")
    // @DataContract
    export class TestFilesIntegrationRequest extends CodeMashRequestBase implements IReturn<TestFilesIntegrationResponse>
    {
        // @DataMember
        public filesIntegrationId: string;

        public constructor(init?: Partial<TestFilesIntegrationRequest>) { super(init); (Object as any).assign(this, init); }
        public getTypeName() { return 'TestFilesIntegrationRequest'; }
        public getMethod() { return 'POST'; }
        public createResponse() { return new TestFilesIntegrationResponse(); }
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

}

