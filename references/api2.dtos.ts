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

export module CodeMashApi2 {
  export interface IReturn<T> {
    createResponse(): T;
  }

  export interface IReturnVoid {
    createResponse(): void;
  }

  export interface IHasSessionId {
    sessionId?: string;
  }

  export interface IHasBearerToken {
    bearerToken?: string;
  }

  export interface IPost {}

  export interface IGet {}

  export class ValueObject {
    public constructor(init?: Partial<ValueObject>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class BindableTemplate<T> extends ValueObject {
    // @DataMember
    public code: RazorTemplateCode;

    public constructor(init?: Partial<BindableTemplate<T>>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class MessageTranslation<TContent> extends ValueObject {
    // @DataMember
    public language: Language;

    // @DataMember
    public content: TContent;

    public constructor(init?: Partial<MessageTranslation<TContent>>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailAddress extends ValueObject {
    // @DataMember
    public address: string;

    public constructor(init?: Partial<EmailAddress>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class DisplayName extends ValueObject {
    // @DataMember
    public value: string;

    public constructor(init?: Partial<DisplayName>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class ProjectName extends ValueObject {
    // @DataMember
    public name: string;

    // @DataMember
    public uniqueName: string;

    public constructor(init?: Partial<ProjectName>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class AccountOwner extends ValueObject {
    // @DataMember
    public email: EmailAddress;

    // @DataMember
    public displayName?: DisplayName;

    // @DataMember
    public billingEmail?: EmailAddress;

    // @DataMember
    public operationsEmail?: EmailAddress;

    // @DataMember
    public securityEmail?: EmailAddress;

    // @DataMember
    public permissions?: string[];

    // @DataMember
    public allowedProjects?: ProjectName[];

    public constructor(init?: Partial<AccountOwner>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class AggregateId extends ValueObject {
    // @DataMember
    public id: string;

    public constructor(init?: Partial<AggregateId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class AccountId extends AggregateId {
    public constructor(init?: Partial<AccountId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class HashedToken extends ValueObject {
    public constructor(init?: Partial<HashedToken>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum ValidationType {
    AccountAdmin = 'AccountAdmin',
    AccountUser = 'AccountUser',
    ProjectUser = 'ProjectUser',
  }

  export class ProjectId extends AggregateId {
    public constructor(init?: Partial<ProjectId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class UserId extends ValueObject {
    // @DataMember
    public id: string;

    public constructor(init?: Partial<UserId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class ValidationToken extends HashedToken {
    public token: string;
    public createDate: string;
    public validUntil?: string;
    public type: ValidationType;
    public projectId: ProjectId;
    public accountId: AccountId;
    public accountOwner: AccountOwner;
    public userId: UserId;

    public constructor(init?: Partial<ValidationToken>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CodeMashSubscriptionId extends AggregateId {
    public constructor(init?: Partial<CodeMashSubscriptionId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class UtcDateTime extends ValueObject {
    public constructor(init?: Partial<UtcDateTime>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class Quantity extends ValueObject {
    public value: number;

    public constructor(init?: Partial<Quantity>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CodeMashManagedServiceSubscription extends ValueObject {
    public subscriptionId: CodeMashSubscriptionId;
    public willExpireOn: UtcDateTime;
    public issuedOn: UtcDateTime;
    public projectCap: Quantity;
    public isTrial: boolean;

    public constructor(init?: Partial<CodeMashManagedServiceSubscription>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class SecretVersion extends ValueObject {
    // @DataMember
    public value: string;

    public constructor(init?: Partial<SecretVersion>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class Secret extends ValueObject implements IDecryptable {
    // @DataMember
    public value: string;

    // @DataMember
    public version: SecretVersion;

    public constructor(init?: Partial<Secret>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CodeMashLicense extends CodeMashManagedServiceSubscription {
    public domain: string;
    public accountId: AccountId;
    public isEnterprise: boolean;
    public key: Secret;

    public constructor(init?: Partial<CodeMashLicense>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class ExternalCustomerId extends ValueObject {
    public id: string;

    public constructor(init?: Partial<ExternalCustomerId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class Tag extends ValueObject {
    public value: string;

    public constructor(init?: Partial<Tag>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class TagDescription extends ValueObject {
    public displayName: DisplayName;
    public description?: string;

    public constructor(init?: Partial<TagDescription>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class TagTranslation extends MessageTranslation<TagDescription> {
    public constructor(init?: Partial<TagTranslation>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class BaseTagDefinition extends ValueObject {
    // @DataMember
    public tag: Tag;

    // @DataMember
    public translations: TagTranslation[];

    public constructor(init?: Partial<BaseTagDefinition>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class GroupDefinition extends BaseTagDefinition {
    public constructor(init?: Partial<GroupDefinition>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum CommunicationChannel {
    Transactional = 'Transactional',
    Marketing = 'Marketing',
    System = 'System',
  }

  export enum DeliveryChannel {
    Email = 'Email',
    Push = 'Push',
    Sms = 'Sms',
    WebPush = 'WebPush',
    InApp = 'InApp',
    ChatBot = 'ChatBot',
    ChatPlatform = 'ChatPlatform',
  }

  // @DataContract
  export class TagDefinition extends BaseTagDefinition {
    // @DataMember
    public defaultDelivery: { [index: string]: boolean };

    public constructor(init?: Partial<TagDefinition>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class IntegrationId extends AggregateId {
    public constructor(init?: Partial<IntegrationId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum ProjectStatus {
    Active = 'Active',
    Locked = 'Locked',
    Disabled = 'Disabled',
  }

  export class ProjectRegionId extends ValueObject {
    // @DataMember
    public value: string;

    public constructor(init?: Partial<ProjectRegionId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum Continent {
    Africa = 'Africa',
    Antarctica = 'Antarctica',
    Asia = 'Asia',
    Europe = 'Europe',
    NorthAmerica = 'NorthAmerica',
    Oceania = 'Oceania',
    SouthAmerica = 'SouthAmerica',
  }

  // @DataContract
  export class ProjectRegion extends ValueObject {
    // @DataMember
    public id: ProjectRegionId;

    // @DataMember
    public name?: string;

    // @DataMember
    public continent?: Continent;

    public constructor(init?: Partial<ProjectRegion>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class GroupTags extends ValueObject {
    // @DataMember
    public group: Tag;

    // @DataMember
    public tags: Tag[];

    public constructor(init?: Partial<GroupTags>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class ProjectCommunicationChannel extends ValueObject {
    // @DataMember
    public channel: CommunicationChannel;

    // @DataMember
    public groups: GroupTags[];

    public constructor(init?: Partial<ProjectCommunicationChannel>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class ProjectCommunication {
    // @DataMember
    public channels: ProjectCommunicationChannel[];

    // @DataMember
    public groups: GroupDefinition[];

    // @DataMember
    public tags: TagDefinition[];

    public constructor(init?: Partial<ProjectCommunication>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class Language extends ValueObject {
    // @DataMember
    public code: string;

    // @DataMember
    public name: string;

    public constructor(init?: Partial<Language>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class BrandColor extends ValueObject {
    // @DataMember
    public color: string;

    public constructor(init?: Partial<BrandColor>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class FilePath extends ValueObject {
    public path: string;

    public constructor(init?: Partial<FilePath>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class FileResource extends ValueObject {
    public path: FilePath;
    public integrationId: IntegrationId;

    public constructor(init?: Partial<FileResource>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class ProjectLogo extends ValueObject {
    public fileResource: FileResource;
    public publicUrl?: string;

    public constructor(init?: Partial<ProjectLogo>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class ProjectIcon extends ValueObject {
    public fileResource: FileResource;
    public publicUrl?: string;

    public constructor(init?: Partial<ProjectIcon>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class ProjectBrand extends ValueObject {
    // @DataMember
    public mainColor?: BrandColor;

    // @DataMember
    public accentColor?: BrandColor;

    // @DataMember
    public logo?: ProjectLogo;

    // @DataMember
    public icon?: ProjectIcon;

    public constructor(init?: Partial<ProjectBrand>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class TimeZone extends ValueObject {
    // @DataMember
    public zoneId: string;

    public constructor(init?: Partial<TimeZone>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class DomainUrl extends ValueObject {
    public value: string;

    public constructor(init?: Partial<DomainUrl>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum ModuleWidgetTypes {
    Days7Count = 'Days7Count',
    WeeklyCount = 'WeeklyCount',
    Days30Count = 'Days30Count',
    MonthlyCount = 'MonthlyCount',
    YearlyCount = 'YearlyCount',
    LifetimeCount = 'LifetimeCount',
  }

  // @Flags()
  export enum ApplicationModule {
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
  }

  export class ProjectWidget extends ValueObject {
    public widgetType: ModuleWidgetTypes;
    public applicationModule: ApplicationModule;

    public constructor(init?: Partial<ProjectWidget>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class Project extends ValueObject implements IBindableToSystemTokens {
    // @DataMember
    public id: ProjectId;

    // @DataMember
    public defaultDatabaseIntegrationId: IntegrationId;

    // @DataMember
    public status: ProjectStatus;

    // @DataMember
    public name: ProjectName;

    // @DataMember
    public regions?: ProjectRegion[];

    // @DataMember
    public projectCommunication?: ProjectCommunication;

    // @DataMember
    public languages: Language[];

    // @DataMember
    public defaultLanguage: Language;

    // @DataMember
    public description?: string;

    // @DataMember
    public brand?: ProjectBrand;

    // @DataMember
    public timeZone?: TimeZone;

    // @DataMember
    public paymentZones?: TimeZone[];

    // @DataMember
    public marketingUrl?: DomainUrl;

    // @DataMember
    public socials?: { [index: string]: string };

    // @DataMember
    public allowedOrigins?: DomainUrl[];

    // @DataMember
    public widgets?: ProjectWidget[];

    public constructor(init?: Partial<Project>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class Integration extends ValueObject implements IHasDomainId {
    // @DataMember
    public id: IntegrationId;

    // @DataMember
    public name: DisplayName;

    // @DataMember
    public isEnabled: boolean;

    // @DataMember
    public viewId: string;

    public constructor(init?: Partial<Integration>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export enum DatabaseProvider {
    CodeMashMongoDbAtlasCluster = 'CodeMashMongoDbAtlasCluster',
    CodeMashMongoDbAtlasServerless = 'CodeMashMongoDbAtlasServerless',
    MongoDbConnectionString = 'MongoDbConnectionString',
  }

  // @DataContract
  export class DatabaseIntegration extends Integration {
    // @DataMember
    public provider: DatabaseProvider;

    public constructor(init?: Partial<DatabaseIntegration>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class DeviceId extends ValueObject {
    public id: string;

    public constructor(init?: Partial<DeviceId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum DeviceType {
    Unknown = 'Unknown',
    Phone = 'Phone',
    Tablet = 'Tablet',
    Desktop = 'Desktop',
    Tv = 'Tv',
  }

  export class PushDeviceToken extends ValueObject {
    public token: string;

    public constructor(init?: Partial<PushDeviceToken>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum PushDeviceDeliveryFamily {
    Ios = 'Ios',
    Android = 'Android',
    Chrome = 'Chrome',
    Safari = 'Safari',
    Expo = 'Expo',
  }

  // @DataContract
  export class PushDeviceDeliveryToken {
    // @DataMember
    public pushDeviceToken: PushDeviceToken;

    // @DataMember
    public deliveryFamily: PushDeviceDeliveryFamily;

    public constructor(init?: Partial<PushDeviceDeliveryToken>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class PushDevice extends ValueObject {
    // @DataMember
    public id: DeviceId;

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

    // @DataMember
    public token: PushDeviceDeliveryToken;

    public constructor(init?: Partial<PushDevice>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract(Namespace="http://codemash.io/types/")
  export class RequestBase
    implements ICultureBasedRequest, IVersionBasedRequest
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

    public constructor(init?: Partial<RequestBase>) {
      (Object as any).assign(this, init);
    }
  }

  export class CodeMashRequestBase
    extends RequestBase
    implements IHasProjectId
  {
    /** @description ID of your project. Can be passed in a header as X-CM-ProjectId. */
    // @DataMember
    // @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as X-CM-ProjectId.", IsRequired=true, Name="X-CM-ProjectId", ParameterType="header")
    public projectId: string;

    public constructor(init?: Partial<CodeMashRequestBase>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export interface ICultureBasedRequest {
    cultureCode?: string;
  }

  export interface IVersionBasedRequest {
    version: string;
  }

  export interface IHasProjectId {
    projectId: string;
  }

  export enum Gender {
    Male = 'Male',
    Female = 'Female',
    Other = 'Other',
  }

  export class UserGeneralInfoDto {
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
    public blockedTags?: { [index: string]: string[] };
    public extraMetadata?: string;
    public notes?: string;

    public constructor(init?: Partial<UserGeneralInfoDto>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class SaveUser extends CodeMashRequestBase {
    /** @description User Info */
    // @DataMember
    // @ApiMember(DataType="object", Description="User Info", Name="UserGeneralInfo", ParameterType="body")
    public userGeneralInfo?: UserGeneralInfoDto;

    /** @description Ignore UserRegistersAsRole from Membership Settings */
    // @DataMember
    // @ApiMember(DataType="boolean", Description="Ignore UserRegistersAsRole from Membership Settings", Name="IgnoreUserRegistersAsRole", ParameterType="body")
    public ignoreUserRegistersAsRole: boolean;

    public constructor(init?: Partial<SaveUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class SaveUserWithRolesBase extends SaveUser {
    // @DataMember
    public roles: string[];

    public constructor(init?: Partial<SaveUserWithRolesBase>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class ListPaginationRequestBase
    extends RequestBase
    implements IRequestWithPaging, IRequestWithSorting
  {
    /** @description Amount of records to return */
    // @DataMember
    // @ApiMember(DataType="integer", Description="Amount of records to return", Format="int32", Name="PageSize", ParameterType="form")
    public pageSize?: number;

    // @DataMember
    public startingAfter?: string;

    // @DataMember
    public endingBefore?: string;

    /** @description A query that specifies how to sort filtered records */
    // @DataMember
    // @ApiMember(DataType="string", Description="A query that specifies how to sort filtered records", Name="Sort", ParameterType="body")
    public sort?: string;

    public constructor(init?: Partial<ListPaginationRequestBase>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CodeMashListPaginationRequestBase
    extends ListPaginationRequestBase
    implements IHasProjectId
  {
    /** @description ID of your project. Can be passed in a header as X-CM-ProjectId. */
    // @DataMember
    // @ApiMember(DataType="string", Description="ID of your project. Can be passed in a header as X-CM-ProjectId.", IsRequired=true, Name="X-CM-ProjectId", ParameterType="header")
    public projectId: string;

    public constructor(init?: Partial<CodeMashListPaginationRequestBase>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export interface IRequestWithPaging {
    pageSize?: number;
    startingAfter?: string;
    endingBefore?: string;
  }

  export interface IRequestWithSorting {
    sort?: string;
  }

  export class RoleName extends ValueObject {
    public displayName?: string;
    public name: string;

    public constructor(init?: Partial<RoleName>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class IamResourcePermission extends ValueObject {
    public permissionNamespace: string;
    public permissionName: string;
    public permissionDisplayName: string;
    public permissionDescription?: string;
    public selected?: boolean;

    public constructor(init?: Partial<IamResourcePermission>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum PermissionsAccessSet {
    OwnRecord = 'OwnRecord',
    Full = 'Full',
    ReadOnly = 'ReadOnly',
    SameRole = 'SameRole',
    Executable = 'Executable',
    SharedWithMe = 'SharedWithMe',
    Custom = 'Custom',
  }

  export class IamResourcePermissionsSet extends ValueObject {
    public setName: PermissionsAccessSet;
    public resourcePermissions: IamResourcePermission[];

    public constructor(init?: Partial<IamResourcePermissionsSet>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class IamModuleGroupResource extends ValueObject {
    public namespaceId: string;
    public resourceDisplayName: string;
    public resourcePermissions: IamResourcePermission[];
    public resourcePermissionSets: IamResourcePermissionsSet[];

    public constructor(init?: Partial<IamModuleGroupResource>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class IamModuleGroup extends ValueObject {
    public displayName: string;
    public name: string;
    public resources: IamModuleGroupResource[];

    public constructor(init?: Partial<IamModuleGroup>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class IamModule extends ValueObject {
    public displayName: string;
    public name: string;
    public groups: IamModuleGroup[];

    public constructor(init?: Partial<IamModule>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CustomPolicyId extends AggregateId {
    public constructor(init?: Partial<CustomPolicyId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CustomPolicy extends ValueObject {
    public name: DisplayName;
    public permissions: IamModule[];
    public description?: string;
    public id: CustomPolicyId;
    public isReadonly: boolean;

    public constructor(init?: Partial<CustomPolicy>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CustomPolicyPermissions extends ValueObject {
    public policy: CustomPolicy;
    public permissions: string[];

    public constructor(init?: Partial<CustomPolicyPermissions>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class Phone extends ValueObject {
    public value: string;

    public constructor(init?: Partial<Phone>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class FirstName extends ValueObject {
    // @DataMember
    public value: string;

    public constructor(init?: Partial<FirstName>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class LastName extends ValueObject {
    // @DataMember
    public value: string;

    public constructor(init?: Partial<LastName>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class MidName extends ValueObject {
    public value: string;

    public constructor(init?: Partial<MidName>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class FullName extends ValueObject {
    public firstName?: FirstName;
    public midName?: MidName;
    public lastName?: LastName;
    public title?: string;

    public constructor(init?: Partial<FullName>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class City extends ValueObject {
    public value: string;

    public constructor(init?: Partial<City>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class Country extends ValueObject {
    public code: string;
    public name: string;

    public constructor(init?: Partial<Country>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class AddressLine extends ValueObject {
    public value: string;

    public constructor(init?: Partial<AddressLine>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class PostalCode extends ValueObject {
    public value: string;

    public constructor(init?: Partial<PostalCode>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CountryState extends ValueObject {
    public value: string;

    public constructor(init?: Partial<CountryState>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class Address extends ValueObject {
    public city?: City;
    public country?: Country;
    public addressLine1?: AddressLine;
    public addressLine2?: AddressLine;
    public postalCode?: PostalCode;
    public state?: CountryState;

    public constructor(init?: Partial<Address>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class UserMarketingPreferences {
    public blockAllMarketingMessages: boolean;
    public blockedTags?: { [index: string]: Tag[] };

    public constructor(init?: Partial<UserMarketingPreferences>) {
      (Object as any).assign(this, init);
    }
  }

  export class UserGeneralInfo implements IBindableToSystemTokens {
    public phone?: Phone;
    public primaryEmail?: EmailAddress;
    public displayName?: DisplayName;
    public firstName?: FirstName;
    public lastName?: LastName;
    public fullName?: FullName;
    public address?: Address;
    public company?: string;
    public gender?: Gender;
    public birthDate?: UtcDateTime;
    public timeZone?: TimeZone;
    public language?: Language;
    public marketingPreferences?: UserMarketingPreferences;
    public notes?: string;
    public extraMetadata?: string;

    public constructor(init?: Partial<UserGeneralInfo>) {
      (Object as any).assign(this, init);
    }
  }

  export enum TriggerType {
    Membership = 'Membership',
    Schema = 'Schema',
    Files = 'Files',
    Payments = 'Payments',
  }

  export class TriggerId extends ValueObject {
    public id: string;

    public constructor(init?: Partial<TriggerId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class RazorTemplateCode extends ValueObject {
    public value: string;

    public constructor(init?: Partial<RazorTemplateCode>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum TriggerActionType {
    Code = 'Code',
    Push = 'Push',
    Email = 'Email',
    WebhookCall = 'WebhookCall',
  }

  // @DataContract
  export class TriggerAction extends ValueObject {
    // @DataMember
    public type: TriggerActionType;

    // @DataMember
    public integrationId?: IntegrationId;

    public constructor(init?: Partial<TriggerAction>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class Trigger extends ValueObject {
    // @DataMember
    public type: TriggerType;

    // @DataMember
    public id: TriggerId;

    // @DataMember
    public name: DisplayName;

    // @DataMember
    public description?: string;

    // @DataMember
    public preExecuteCode?: RazorTemplateCode;

    // @DataMember
    public thenAction: TriggerAction;

    // @DataMember
    public executeOnBehalfOfUser?: UserId;

    // @DataMember
    public isEnabled: boolean;

    // @DataMember
    public order: number;

    // @DataMember
    public breakOnError: boolean;

    public constructor(init?: Partial<Trigger>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum MembershipTriggerType {
    OnRegistered = 'OnRegistered',
    OnInvited = 'OnInvited',
    OnVerified = 'OnVerified',
    OnUpdated = 'OnUpdated',
    OnDeleted = 'OnDeleted',
    OnBlocked = 'OnBlocked',
    OnReactivated = 'OnReactivated',
  }

  export class MembershipTrigger extends Trigger {
    public when: MembershipTriggerType;

    public constructor(init?: Partial<MembershipTrigger>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class TriggersProcessingStarted {
    // @DataMember
    public correlationId: string;

    // @DataMember
    public createdOn: UtcDateTime;

    public constructor(init?: Partial<TriggersProcessingStarted>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class TriggerStarted {
    // @DataMember
    public triggerId: TriggerId;

    // @DataMember
    public correlationId: string;

    // @DataMember
    public moduleName: string;

    // @DataMember
    public createdOn: UtcDateTime;

    public constructor(init?: Partial<TriggerStarted>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class ErrorDto {
    // @DataMember
    public message: string;

    // @DataMember
    public errorCode?: string;

    // @DataMember
    public context?: { [index: string]: string };

    // @DataMember
    public stackTrace?: ErrorDto[];

    public constructor(init?: Partial<ErrorDto>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class TriggerFailed {
    // @DataMember
    public triggerId: TriggerId;

    // @DataMember
    public correlationId: string;

    // @DataMember
    public moduleName: string;

    // @DataMember
    public breakOnError: boolean;

    // @DataMember
    public preExecutionCode?: string;

    // @DataMember
    public preExecutionBoundedCode?: string;

    // @DataMember
    public errors?: ErrorDto[];

    // @DataMember
    public createdOn: UtcDateTime;

    public constructor(init?: Partial<TriggerFailed>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class TriggerFinished {
    // @DataMember
    public triggerId: TriggerId;

    // @DataMember
    public correlationId: string;

    // @DataMember
    public moduleName: string;

    // @DataMember
    public createdOn: UtcDateTime;

    // @DataMember
    public skipped: boolean;

    public constructor(init?: Partial<TriggerFinished>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class TriggersProcessingStopped {
    // @DataMember
    public correlationId: string;

    // @DataMember
    public createdOn: UtcDateTime;

    public constructor(init?: Partial<TriggersProcessingStopped>) {
      (Object as any).assign(this, init);
    }
  }

  export class UserName extends ValueObject {
    public value: string;

    public constructor(init?: Partial<UserName>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum UserType {
    Service = 'Service',
    Email = 'Email',
    UserName = 'UserName',
    Phone = 'Phone',
    Guest = 'Guest',
    Social = 'Social',
  }

  export class IpAddress {
    public ip: string;

    public constructor(init?: Partial<IpAddress>) {
      (Object as any).assign(this, init);
    }
  }

  export class AccessInformation {
    public ip?: IpAddress;
    public date?: UtcDateTime;
    public zone?: TimeZone;

    public constructor(init?: Partial<AccessInformation>) {
      (Object as any).assign(this, init);
    }
  }

  export class Registration {
    public registrationInformation: AccessInformation;

    public constructor(init?: Partial<Registration>) {
      (Object as any).assign(this, init);
    }
  }

  export class Login {
    public needChangePasswordOnNextLogin: boolean;
    public lastAccessInformation?: AccessInformation;

    public constructor(init?: Partial<Login>) {
      (Object as any).assign(this, init);
    }
  }

  export enum UserStatus {
    Registered = 0,
    PendingValidation = 2,
    Active = 8,
    Unregistered = 16,
    Suspended = 32,
    InActive = 64,
    Blocked = 128,
  }

  export class PushDevices extends Array<PushDevice> {
    public constructor(init?: Partial<PushDevices>) {
      super();
      (Object as any).assign(this, init);
    }
  }

  export class User extends ValueObject implements IBindableToSystemTokens {
    public id: UserId;
    public roles?: RoleName[];
    public email?: EmailAddress;
    public userName?: UserName;
    public type: UserType;
    public registration: Registration;
    public login?: Login;
    public generalInfo?: UserGeneralInfo;
    public status: UserStatus;
    public createdOn: UtcDateTime;
    public modifiedOn: UtcDateTime;
    public pushDevices?: PushDevices;
    public tags?: Tag[];

    public constructor(init?: Partial<User>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CampaignId extends ValueObject {
    public id: string;

    public constructor(init?: Partial<CampaignId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class CampaignBatchId extends ValueObject {
    public id: string;

    public constructor(init?: Partial<CampaignBatchId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class Recipient implements IRecipient {
    public constructor(init?: Partial<Recipient>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailRecipient extends Recipient {
    // @DataMember
    public emailAddress: EmailAddress;

    // @DataMember
    public user?: User;

    // @DataMember
    public record?: Object;

    public constructor(init?: Partial<EmailRecipient>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class EmailRecipients {
    public to: EmailRecipient[];
    public cc?: EmailRecipient[];
    public bcc?: EmailRecipient[];
    public startingAfter?: string;
    public hasMore: boolean;

    public constructor(init?: Partial<EmailRecipients>) {
      (Object as any).assign(this, init);
    }
  }

  export class NotificationId extends ValueObject {
    public id: string;

    public constructor(init?: Partial<NotificationId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class SendNotificationResult {
    public id: NotificationId;
    public subject: string;
    public body: string;
    public refId?: string;
    public model?: any;

    public constructor(init?: Partial<SendNotificationResult>) {
      (Object as any).assign(this, init);
    }
  }

  export class TemplateId extends ValueObject {
    public id: string;

    public constructor(init?: Partial<TemplateId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum CampaignStatus {
    Pending = 'Pending',
    Registered = 'Registered',
    Scheduled = 'Scheduled',
    Started = 'Started',
    Stopped = 'Stopped',
    Processing = 'Processing',
    Completed = 'Completed',
    Failed = 'Failed',
  }

  export class TokenKey extends ValueObject {
    public value: string;

    public constructor(init?: Partial<TokenKey>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum TokenMappingResolverType {
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

  export class TokenValue extends ValueObject {
    public value: string;
    public tokenMappingResolverType: TokenMappingResolverType;

    public constructor(init?: Partial<TokenValue>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class TokenMapping extends ValueObject {
    public key: TokenKey;
    public value: TokenValue;

    public constructor(init?: Partial<TokenMapping>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @Flags()
  export enum RespectTimeZoneSettings {
    RespectToLastLoginZone = 1,
    RespectToRegistrationZone = 2,
    RespectToRegistrationProjectZone = 4,
  }

  // @DataContract
  export class CampaignDeliverySettings implements ICampaignDeliverySettings {
    // @DataMember
    public deliveryChannel: DeliveryChannel;

    // @DataMember
    public campaignTime?: UtcDateTime;

    // @DataMember
    public mappedTokens?: TokenMapping[];

    // @DataMember
    public respectTimeZoneSettings?: RespectTimeZoneSettings;

    public constructor(init?: Partial<CampaignDeliverySettings>) {
      (Object as any).assign(this, init);
    }
  }

  export class Campaign
    extends ValueObject
    implements ICampaign, IBindableToSystemTokens
  {
    public campaignId: CampaignId;
    public createdOn: UtcDateTime;
    public forceCampaignLanguage: boolean;
    public language?: Language;
    public timeZone?: TimeZone;
    public templateId: TemplateId;
    public integrationId?: IntegrationId;
    public forceToSendWhenHasBindErrors: boolean;
    public status: CampaignStatus;
    public deliverySettings: CampaignDeliverySettings;
    public tokenMappingValues?: TokenMapping[];
    public notes?: string;

    public constructor(init?: Partial<Campaign>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class EmailCampaign extends Campaign {
    public constructor(init?: Partial<EmailCampaign>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class Template<TMessageContent>
    extends ValueObject
    implements IBindableToSystemTokens
  {
    // @DataMember
    public templateId: TemplateId;

    // @DataMember
    public templateName: DisplayName;

    // @DataMember
    public description?: string;

    // @DataMember
    public translations: MessageTranslation<TMessageContent>[];

    // @DataMember
    public isActive: boolean;

    // @DataMember
    public communicationChannel: CommunicationChannel;

    // @DataMember
    public tags?: Tag[];

    // @DataMember
    public fileIntegrationId?: IntegrationId;

    public constructor(init?: Partial<Template<TMessageContent>>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailSubject extends BindableTemplate<EmailSubject> {
    public constructor(init?: Partial<EmailSubject>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export enum EmailTemplateEngine {
    NotSet = 'NotSet',
    Handlebars = 'Handlebars',
    Mjml = 'Mjml',
    Liquid = 'Liquid',
    Razor = 'Razor',
    Mustache = 'Mustache',
  }

  // @DataContract
  export class EmailBody extends BindableTemplate<EmailBody> {
    // @DataMember
    public structure?: string;

    // @DataMember
    public templateEngine: EmailTemplateEngine;

    public constructor(init?: Partial<EmailBody>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailMessageContent extends ValueObject {
    // @DataMember
    public subject: EmailSubject;

    // @DataMember
    public body: EmailBody;

    // @DataMember
    public staticAttachments?: string[];

    public constructor(init?: Partial<EmailMessageContent>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailTemplate extends Template<EmailMessageContent> {
    public constructor(init?: Partial<EmailTemplate>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class EventBase {
    public constructor(init?: Partial<EventBase>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailSenderName extends ValueObject {
    // @DataMember
    public value: string;

    public constructor(init?: Partial<EmailSenderName>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export enum EmailProvider {
    Smtp = 'Smtp',
    SendGrid = 'SendGrid',
    MailGun = 'MailGun',
    AwsSes = 'AwsSes',
  }

  // @DataContract
  export class EmailIntegration extends Integration {
    // @DataMember
    public emailAddress: EmailAddress;

    // @DataMember
    public senderDisplayName?: EmailSenderName;

    // @DataMember
    public provider: EmailProvider;

    public constructor(init?: Partial<EmailIntegration>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class EmailSignatureId extends AggregateId {
    public constructor(init?: Partial<EmailSignatureId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailSignatureContent extends BindableTemplate<EmailSignatureContent> {
    public constructor(init?: Partial<EmailSignatureContent>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailSignatureTranslation extends MessageTranslation<EmailSignatureContent> {
    public constructor(init?: Partial<EmailSignatureTranslation>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class EmailSignature extends ValueObject {
    public id: EmailSignatureId;
    public displayName?: DisplayName;
    public translations: EmailSignatureTranslation[];

    public constructor(init?: Partial<EmailSignature>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class EmailFooterId extends AggregateId {
    public constructor(init?: Partial<EmailFooterId>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailFooterContent extends BindableTemplate<EmailFooterContent> {
    public constructor(init?: Partial<EmailFooterContent>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class EmailFooterTranslation extends MessageTranslation<EmailFooterContent> {
    public constructor(init?: Partial<EmailFooterTranslation>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class EmailFooter extends ValueObject {
    public id: EmailFooterId;
    public displayName?: DisplayName;
    public translations: EmailFooterTranslation[];

    public constructor(init?: Partial<EmailFooter>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class PushRecipient extends Recipient {
    // @DataMember
    public user: User;

    // @DataMember
    public record?: Object;

    public constructor(init?: Partial<PushRecipient>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class PushRecipients {
    public to: PushRecipient[];
    public startingAfter?: string;
    public hasMore: boolean;

    public constructor(init?: Partial<PushRecipients>) {
      (Object as any).assign(this, init);
    }
  }

  export class PushCampaign extends Campaign {
    public constructor(init?: Partial<PushCampaign>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class PushTitle extends BindableTemplate<PushTitle> {
    public constructor(init?: Partial<PushTitle>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class PushBody extends BindableTemplate<PushBody> {
    public constructor(init?: Partial<PushBody>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class PushMessageContent extends ValueObject {
    // @DataMember
    public title: PushTitle;

    // @DataMember
    public body: PushBody;

    public constructor(init?: Partial<PushMessageContent>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class PushTemplate extends Template<PushMessageContent> {
    public constructor(init?: Partial<PushTemplate>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export enum PushProvider {
    AppleDevices = 'AppleDevices',
    SafariWebPush = 'SafariWebPush',
    CodeMashSafariExtension = 'CodeMashSafariExtension',
    AndroidDevices = 'AndroidDevices',
    CodeMashChromeExtension = 'CodeMashChromeExtension',
    ChromeWebPush = 'ChromeWebPush',
    CodeMashApp = 'CodeMashApp',
    Expo = 'Expo',
  }

  export class PushIntegration extends Integration {
    // @DataMember
    public provider: PushProvider;

    public constructor(init?: Partial<PushIntegration>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class CodeMashResponseStatus {
    // @DataMember
    public isSuccess: boolean;

    // @DataMember
    public errors?: ErrorDto[];

    public constructor(init?: Partial<CodeMashResponseStatus>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class ResponseBase {
    // @DataMember
    public responseStatus: CodeMashResponseStatus;

    public constructor(init?: Partial<ResponseBase>) {
      (Object as any).assign(this, init);
    }
  }

  export class AccessInformationDto {
    public ip?: string;
    public date?: string;
    public timeZone?: string;

    public constructor(init?: Partial<AccessInformationDto>) {
      (Object as any).assign(this, init);
    }
  }

  export class RegistrationDto {
    public registrationInformation: AccessInformationDto;

    public constructor(init?: Partial<RegistrationDto>) {
      (Object as any).assign(this, init);
    }
  }

  export class LoginDto {
    public needChangePasswordOnNextLogin: boolean;
    public lastAccessInformation?: AccessInformationDto;

    public constructor(init?: Partial<LoginDto>) {
      (Object as any).assign(this, init);
    }
  }

  export class UserDto {
    public id?: string;
    public type: UserType;
    public email?: string;
    public userName?: string;
    public registration?: RegistrationDto;
    public login?: LoginDto;
    public userGeneralInfo?: UserGeneralInfoDto;
    public roles?: string[];
    public pushDevices?: string[];
    public tags?: string[];
    public status: UserStatus;
    public createdOn: string;
    public modifiedOn: string;

    public constructor(init?: Partial<UserDto>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class ResponseError {
    // @DataMember(Order=1)
    public errorCode: string;

    // @DataMember(Order=2)
    public fieldName: string;

    // @DataMember(Order=3)
    public message: string;

    // @DataMember(Order=4)
    public meta: { [index: string]: string };

    public constructor(init?: Partial<ResponseError>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class ResponseStatus {
    // @DataMember(Order=1)
    public errorCode: string;

    // @DataMember(Order=2)
    public message: string;

    // @DataMember(Order=3)
    public stackTrace: string;

    // @DataMember(Order=4)
    public errors: ResponseError[];

    // @DataMember(Order=5)
    public meta: { [index: string]: string };

    public constructor(init?: Partial<ResponseStatus>) {
      (Object as any).assign(this, init);
    }
  }

  export class ResponseBase_1<T> {
    // @DataMember
    public responseStatus?: ResponseStatus;

    // @DataMember(Name="result")
    public result: T;

    public constructor(init?: Partial<ResponseBase_1<T>>) {
      (Object as any).assign(this, init);
    }
  }

  export class ListResponseBase<T> extends ResponseBase_1<T> {
    public hasMore: boolean;
    public startingAfter?: string;
    public endingBefore?: string;

    public constructor(init?: Partial<ListResponseBase<T>>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class UserApiKey {
    // @DataMember(Order=1)
    public key: string;

    // @DataMember(Order=2)
    public keyType: string;

    // @DataMember(Order=3)
    public expiryDate?: string;

    // @DataMember(Order=4)
    public meta: { [index: string]: string };

    public constructor(init?: Partial<UserApiKey>) {
      (Object as any).assign(this, init);
    }
  }

  export interface IHasDomainId {
    viewId: string;
  }

  export interface IBindableToSystemTokens {}

  export interface ICampaign {
    campaignId: CampaignId;
    language?: Language;
  }

  export interface IDecryptable {}

  export interface IRecipient {
    language?: Language;
    timeZone?: TimeZone;
    userNotificationPreferences?: UserMarketingPreferences;
  }

  export interface ICampaignDeliverySettings
    extends IDeliverySettings,
      IPostponedCampaign {
    deliveryChannel: DeliveryChannel;
    respectTimeZoneSettings?: RespectTimeZoneSettings;
  }

  export interface IDeliverySettings {
    mappedTokens?: TokenMapping[];
  }

  export interface IPostponedCampaign {
    campaignTime?: UtcDateTime;
  }

  // @DataContract
  export class EmptyResponse extends ResponseBase {
    public constructor(init?: Partial<EmptyResponse>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class IdResponse extends ResponseBase {
    // @DataMember
    public id?: string;

    public constructor(init?: Partial<IdResponse>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class GetUserResponse extends ResponseBase {
    public user?: UserDto;

    public constructor(init?: Partial<GetUserResponse>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  export class GetUsersResponse extends ResponseBase {
    public list?: ListResponseBase<UserDto[]>;

    public constructor(init?: Partial<GetUsersResponse>) {
      super(init);
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class AuthenticateResponse implements IHasSessionId, IHasBearerToken {
    // @DataMember(Order=1)
    public userId: string;

    // @DataMember(Order=2)
    public sessionId: string;

    // @DataMember(Order=3)
    public userName: string;

    // @DataMember(Order=4)
    public displayName: string;

    // @DataMember(Order=5)
    public referrerUrl: string;

    // @DataMember(Order=6)
    public bearerToken: string;

    // @DataMember(Order=7)
    public refreshToken: string;

    // @DataMember(Order=8)
    public refreshTokenExpiry?: string;

    // @DataMember(Order=9)
    public profileUrl: string;

    // @DataMember(Order=10)
    public roles: string[];

    // @DataMember(Order=11)
    public permissions: string[];

    // @DataMember(Order=12)
    public responseStatus: ResponseStatus;

    // @DataMember(Order=13)
    public meta: { [index: string]: string };

    public constructor(init?: Partial<AuthenticateResponse>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class GetAccessTokenResponse {
    // @DataMember(Order=1)
    public accessToken: string;

    // @DataMember(Order=2)
    public meta: { [index: string]: string };

    // @DataMember(Order=3)
    public responseStatus: ResponseStatus;

    public constructor(init?: Partial<GetAccessTokenResponse>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class GetApiKeysResponse {
    // @DataMember(Order=1)
    public results: UserApiKey[];

    // @DataMember(Order=2)
    public meta: { [index: string]: string };

    // @DataMember(Order=3)
    public responseStatus: ResponseStatus;

    public constructor(init?: Partial<GetApiKeysResponse>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class RegenerateApiKeysResponse {
    // @DataMember(Order=1)
    public results: UserApiKey[];

    // @DataMember(Order=2)
    public meta: { [index: string]: string };

    // @DataMember(Order=3)
    public responseStatus: ResponseStatus;

    public constructor(init?: Partial<RegenerateApiKeysResponse>) {
      (Object as any).assign(this, init);
    }
  }

  // @DataContract
  export class AccountCreated {
    // @DataMember
    public owner: AccountOwner;

    // @DataMember
    public accountId: AccountId;

    public constructor(init?: Partial<AccountCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'AccountCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class AccountVerified {
    public constructor(init?: Partial<AccountVerified>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'AccountVerified';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class AccountSetAsActive {
    public constructor(init?: Partial<AccountSetAsActive>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'AccountSetAsActive';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class AccountValidationTokenIssued {
    public token: ValidationToken;

    public constructor(init?: Partial<AccountValidationTokenIssued>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'AccountValidationTokenIssued';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class LicenseCreated {
    public license: CodeMashLicense;
    public refId?: string;

    public constructor(init?: Partial<LicenseCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'LicenseCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class LicenseRenewed {
    public license: CodeMashLicense;
    public refId?: string;

    public constructor(init?: Partial<LicenseRenewed>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'LicenseRenewed';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class CustomerCreated {
    public customerId: ExternalCustomerId;

    public constructor(init?: Partial<CustomerCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'CustomerCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class SubscriptionCreated {
    public subscription: CodeMashManagedServiceSubscription;

    public constructor(init?: Partial<SubscriptionCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'SubscriptionCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectCommunicationGroupSaved {
    public projectId: ProjectId;
    public group: GroupDefinition;
    public channel: CommunicationChannel;
    public originChannel?: CommunicationChannel;

    public constructor(init?: Partial<ProjectCommunicationGroupSaved>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectCommunicationGroupSaved';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectCommunicationTagFromGroupRemoved {
    public projectId: ProjectId;
    public groupTag: Tag;
    public removedTag: Tag;

    public constructor(
      init?: Partial<ProjectCommunicationTagFromGroupRemoved>,
    ) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectCommunicationTagFromGroupRemoved';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectCommunicationGroupDeleted {
    public projectId: ProjectId;
    public groupTag: Tag;

    public constructor(init?: Partial<ProjectCommunicationGroupDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectCommunicationGroupDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectCommunicationTagSaved {
    public projectId: ProjectId;
    public channel?: CommunicationChannel;
    public groupTag?: Tag;
    public tag: TagDefinition;

    public constructor(init?: Partial<ProjectCommunicationTagSaved>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectCommunicationTagSaved';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectCommunicationTagDeleted {
    public projectId: ProjectId;
    public tag: Tag;

    public constructor(init?: Partial<ProjectCommunicationTagDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectCommunicationTagDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class ProjectCreated {
    // @DataMember
    public project: Project;

    // @DataMember
    public databaseIntegration: DatabaseIntegration;

    public constructor(init?: Partial<ProjectCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectDeleted {
    public projectId: ProjectId;

    public constructor(init?: Partial<ProjectDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectNameUpdated {
    public projectId: ProjectId;
    public name: ProjectName;

    public constructor(init?: Partial<ProjectNameUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectNameUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectDescriptionUpdated {
    public projectId: ProjectId;
    public description?: string;

    public constructor(init?: Partial<ProjectDescriptionUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectDescriptionUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectUrlUpdated {
    public projectId: ProjectId;
    public url?: DomainUrl;

    public constructor(init?: Partial<ProjectUrlUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectUrlUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectAllowedOriginsUpdated {
    public origins?: DomainUrl[];
    public projectId: ProjectId;

    public constructor(init?: Partial<ProjectAllowedOriginsUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectAllowedOriginsUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectDefaultLanguageUpdated {
    public language: Language;
    public projectId: ProjectId;

    public constructor(init?: Partial<ProjectDefaultLanguageUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectDefaultLanguageUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectLanguagesUpdated {
    public projectId: ProjectId;
    public languages: Language[];

    public constructor(init?: Partial<ProjectLanguagesUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectLanguagesUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectLogoUpdated {
    public projectId: ProjectId;
    public logo?: ProjectLogo;

    public constructor(init?: Partial<ProjectLogoUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectLogoUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectIconUpdated {
    public projectId: ProjectId;
    public icon?: ProjectIcon;

    public constructor(init?: Partial<ProjectIconUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectIconUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectMainColorUpdated {
    public projectId: ProjectId;
    public color?: BrandColor;

    public constructor(init?: Partial<ProjectMainColorUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectMainColorUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectAccentColorUpdated {
    public projectId: ProjectId;
    public color?: BrandColor;

    public constructor(init?: Partial<ProjectAccentColorUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectAccentColorUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class ProjectRegionsUpdated {
    public projectId: ProjectId;
    public regions?: ProjectRegion[];

    public constructor(init?: Partial<ProjectRegionsUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'ProjectRegionsUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class AccountUserPushDeviceCreated {
    // @DataMember
    public userId: UserId;

    // @DataMember
    public pushDevice: PushDevice;

    public constructor(init?: Partial<AccountUserPushDeviceCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'AccountUserPushDeviceCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/block", "PATCH")
  // @Api(Description="Membership")
  // @DataContract
  export class BlockUser
    extends CodeMashRequestBase
    implements IReturn<EmptyResponse>
  {
    // @DataMember
    public id: string;

    public constructor(init?: Partial<BlockUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'BlockUser';
    }
    public getMethod() {
      return 'PATCH';
    }
    public createResponse() {
      return new EmptyResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/register/service", "POST")
  // @Api(Description="Membership")
  // @DataContract
  export class SaveSystemUserWithPermissions
    extends SaveUserWithRolesBase
    implements IReturn<IdResponse>
  {
    public constructor(init?: Partial<SaveSystemUserWithPermissions>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'SaveSystemUserWithPermissions';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new IdResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/register/guest", "POST")
  // @Api(Description="Membership")
  // @DataContract
  export class SaveGuestUser extends SaveUser implements IReturn<IdResponse> {
    public constructor(init?: Partial<SaveGuestUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'SaveGuestUser';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new IdResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/register/user-name", "POST")
  // @Api(Description="Membership")
  // @DataContract
  export class SaveUserNameUser
    extends SaveUser
    implements IReturn<IdResponse>
  {
    // @DataMember
    public password: string;

    // @DataMember
    public userName: string;

    public constructor(init?: Partial<SaveUserNameUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'SaveUserNameUser';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new IdResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/register/email", "POST")
  // @Api(Description="Membership")
  // @DataContract
  export class SaveEmailUser extends SaveUser implements IReturn<IdResponse> {
    // @DataMember
    public password: string;

    // @DataMember
    public email: string;

    public constructor(init?: Partial<SaveEmailUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'SaveEmailUser';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new IdResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/register/phone", "POST")
  // @Api(Description="Membership")
  // @DataContract
  export class SavePhoneUser extends SaveUser implements IReturn<IdResponse> {
    // @DataMember
    public phone: string;

    public constructor(init?: Partial<SavePhoneUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'SavePhoneUser';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new IdResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/register/phone-with-permissions", "POST")
  // @Api(Description="Membership")
  // @DataContract
  export class SavePhoneUserNameWithPermissions
    extends SaveUserWithRolesBase
    implements IReturn<IdResponse>
  {
    // @DataMember
    public phone: string;

    public constructor(init?: Partial<SavePhoneUserNameWithPermissions>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'SavePhoneUserNameWithPermissions';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new IdResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/register/email-with-permissions", "POST")
  // @Api(Description="Membership")
  // @DataContract
  export class SaveEmailUserNameWithPermissions
    extends SaveUserWithRolesBase
    implements IReturn<IdResponse>
  {
    // @DataMember
    public password: string;

    // @DataMember
    public email: string;

    public constructor(init?: Partial<SaveEmailUserNameWithPermissions>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'SaveEmailUserNameWithPermissions';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new IdResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/register/user-name-with-permissions", "POST")
  // @Api(Description="Membership")
  // @DataContract
  export class SaveUserNameWithPermissions
    extends SaveUserWithRolesBase
    implements IReturn<IdResponse>
  {
    // @DataMember
    public password: string;

    // @DataMember
    public userName: string;

    public constructor(init?: Partial<SaveUserNameWithPermissions>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'SaveUserNameWithPermissions';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new IdResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users", "DELETE")
  // @Api(Description="Membership")
  // @DataContract
  export class DeleteUser
    extends CodeMashRequestBase
    implements IReturn<EmptyResponse>
  {
    // @DataMember
    public id: string;

    public constructor(init?: Partial<DeleteUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DeleteUser';
    }
    public getMethod() {
      return 'DELETE';
    }
    public createResponse() {
      return new EmptyResponse();
    }
  }

  // @Route("/{version}/membership/users/{id}", "GET")
  export class GetUser
    extends CodeMashRequestBase
    implements IReturn<GetUserResponse>
  {
    public id: string;

    public constructor(init?: Partial<GetUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'GetUser';
    }
    public getMethod() {
      return 'GET';
    }
    public createResponse() {
      return new GetUserResponse();
    }
  }

  // @Route("/{version}/membership/users", "GET")
  export class GetUsers
    extends CodeMashListPaginationRequestBase
    implements IReturn<GetUsersResponse>
  {
    public includePermissions: boolean;
    public userShouldHavePushDevice: boolean;
    public userShouldHaveEmail: boolean;
    public includeMeta: boolean;
    public roleNames?: string[];
    public userIds?: string[];

    public constructor(init?: Partial<GetUsers>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'GetUsers';
    }
    public getMethod() {
      return 'GET';
    }
    public createResponse() {
      return new GetUsersResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/invite", "POST")
  // @Api(Description="Membership")
  // @DataContract
  export class InviteUser
    extends CodeMashRequestBase
    implements IReturn<EmptyResponse>
  {
    // @DataMember
    public email: string;

    public constructor(init?: Partial<InviteUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'InviteUser';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new EmptyResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/assign-roles", "PUT")
  // @Api(Description="Membership")
  // @DataContract
  export class AssignRolePermissions
    extends CodeMashRequestBase
    implements IReturn<EmptyResponse>
  {
    // @DataMember
    public id: string;

    // @DataMember
    public roles?: RoleName[];

    public constructor(init?: Partial<AssignRolePermissions>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'AssignRolePermissions';
    }
    public getMethod() {
      return 'PUT';
    }
    public createResponse() {
      return new EmptyResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users/unblock", "PATCH")
  // @Api(Description="Membership")
  // @DataContract
  export class UnblockUser
    extends CodeMashRequestBase
    implements IReturn<EmptyResponse>
  {
    // @DataMember
    public id: string;

    public constructor(init?: Partial<UnblockUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UnblockUser';
    }
    public getMethod() {
      return 'PATCH';
    }
    public createResponse() {
      return new EmptyResponse();
    }
  }

  /** @description Membership */
  // @Route("/{version}/membership/users", "PUT")
  // @Api(Description="Membership")
  // @DataContract
  export class UpdateUser extends SaveUser implements IReturn<IdResponse> {
    // @DataMember
    public id: string;

    public constructor(init?: Partial<UpdateUser>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UpdateUser';
    }
    public getMethod() {
      return 'PUT';
    }
    public createResponse() {
      return new IdResponse();
    }
  }

  export class MembershipEstablished {
    public constructor(init?: Partial<MembershipEstablished>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipEstablished';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class MembershipEnabled {
    public constructor(init?: Partial<MembershipEnabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipEnabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class MembershipDisabled {
    public constructor(init?: Partial<MembershipDisabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipDisabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PolicyCreated {
    public policyPermissions: CustomPolicyPermissions;

    public constructor(init?: Partial<PolicyCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PolicyCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PolicyUpdated {
    public policyName: DisplayName;
    public description?: string;
    public policyPermissions: CustomPolicyPermissions;

    public constructor(init?: Partial<PolicyUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PolicyUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PolicyDeleted {
    public policyId: CustomPolicyId;

    public constructor(init?: Partial<PolicyDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PolicyDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class RoleCreated {
    public roleName: RoleName;
    public description?: string;
    public policyIds?: CustomPolicyId[];

    public constructor(init?: Partial<RoleCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'RoleCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class RoleUpdated {
    public roleName: RoleName;
    public description?: string;
    public policyIds?: CustomPolicyId[];

    public constructor(init?: Partial<RoleUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'RoleUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class RoleDeleted {
    public roleName: RoleName;

    public constructor(init?: Partial<RoleDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'RoleDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggerCalled {
    // @DataMember
    public userId: UserId;

    // @DataMember
    public from?: UserGeneralInfo;

    // @DataMember
    public to?: UserGeneralInfo;

    // @DataMember
    public emailAddress?: EmailAddress;

    // @DataMember
    public correlationId: string;

    // @DataMember
    public trigger: MembershipTrigger;

    // @DataMember
    public createdOn: UtcDateTime;

    public constructor(init?: Partial<MembershipTriggerCalled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggerCalled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggerCreated {
    public constructor(init?: Partial<MembershipTriggerCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggerCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggerChanged {
    public constructor(init?: Partial<MembershipTriggerChanged>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggerChanged';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggerEnabled {
    public constructor(init?: Partial<MembershipTriggerEnabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggerEnabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggerDisabled {
    public constructor(init?: Partial<MembershipTriggerDisabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggerDisabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggerDeleted {
    public constructor(init?: Partial<MembershipTriggerDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggerDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggersProcessingStarted extends TriggersProcessingStarted {
    public constructor(init?: Partial<MembershipTriggersProcessingStarted>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggersProcessingStarted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggerStarted extends TriggerStarted {
    public constructor(init?: Partial<MembershipTriggerStarted>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggerStarted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggerFailed extends TriggerFailed {
    public constructor(init?: Partial<MembershipTriggerFailed>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggerFailed';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggerFinished extends TriggerFinished {
    public constructor(init?: Partial<MembershipTriggerFinished>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggerFinished';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  // @DataContract
  export class MembershipTriggersProcessingStopped extends TriggersProcessingStopped {
    public constructor(init?: Partial<MembershipTriggersProcessingStopped>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'MembershipTriggersProcessingStopped';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class UserRegistered {
    public user: User;

    public constructor(init?: Partial<UserRegistered>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UserRegistered';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class UserUpdated {
    public userId: UserId;
    public from: UserGeneralInfo;
    public to: UserGeneralInfo;

    public constructor(init?: Partial<UserUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UserUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class UserBlocked {
    public user?: UserGeneralInfo;
    public userId: UserId;

    public constructor(init?: Partial<UserBlocked>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UserBlocked';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class UserUnblocked {
    public user?: UserGeneralInfo;
    public userId: UserId;

    public constructor(init?: Partial<UserUnblocked>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UserUnblocked';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class UserInvited {
    public emailAddress: EmailAddress;

    public constructor(init?: Partial<UserInvited>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UserInvited';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class UserVerified {
    public userId: UserId;
    public user?: UserGeneralInfo;

    public constructor(init?: Partial<UserVerified>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UserVerified';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class UserDeleted {
    public user?: UserGeneralInfo;
    public userId: UserId;

    public constructor(init?: Partial<UserDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UserDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class UserNotificationsDeliveryPreferencesSaved {
    public userId: UserId;
    public blockAllMarketingMessages: boolean;
    public subscribedToTags?: { [index: string]: Tag[] };

    public constructor(
      init?: Partial<UserNotificationsDeliveryPreferencesSaved>,
    ) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'UserNotificationsDeliveryPreferencesSaved';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class DatabaseEstablished {
    public constructor(init?: Partial<DatabaseEstablished>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DatabaseEstablished';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class DatabaseEnabled {
    public constructor(init?: Partial<DatabaseEnabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DatabaseEnabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class DatabaseDisabled {
    public constructor(init?: Partial<DatabaseDisabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DatabaseDisabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class DatabaseIntegrationCreated {
    public integration: DatabaseIntegration;

    public constructor(init?: Partial<DatabaseIntegrationCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DatabaseIntegrationCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class DatabaseIntegrationChanged {
    public integration: DatabaseIntegration;

    public constructor(init?: Partial<DatabaseIntegrationChanged>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DatabaseIntegrationChanged';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class DatabaseIntegrationSetAsDefault {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<DatabaseIntegrationSetAsDefault>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DatabaseIntegrationSetAsDefault';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class DatabaseIntegrationDeleted {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<DatabaseIntegrationDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DatabaseIntegrationDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class DatabaseIntegrationEnabled {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<DatabaseIntegrationEnabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DatabaseIntegrationEnabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class DatabaseIntegrationDisabled {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<DatabaseIntegrationDisabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'DatabaseIntegrationDisabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailBatchRegistered {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public startingAfter?: string;

    public constructor(init?: Partial<EmailBatchRegistered>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailBatchRegistered';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailBatchStarted {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public recipients: EmailRecipients;

    public constructor(init?: Partial<EmailBatchStarted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailBatchStarted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailBatchCompleted {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public errors?: ErrorDto[];

    public constructor(init?: Partial<EmailBatchCompleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailBatchCompleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailBatchFailed {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public errors?: ErrorDto[];

    public constructor(init?: Partial<EmailBatchFailed>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailBatchFailed';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailNotificationProcessed {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public campaignBatchNotificationId: NotificationId;
    public sendNotificationResult?: SendNotificationResult;
    public recipients: EmailRecipients;
    public errors?: ErrorDto[];

    public constructor(init?: Partial<EmailNotificationProcessed>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailNotificationProcessed';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailNotificationRead {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public notificationId: NotificationId;

    public constructor(init?: Partial<EmailNotificationRead>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailNotificationRead';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailNotificationClicked {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public notificationId: NotificationId;
    public sourceId?: string;

    public constructor(init?: Partial<EmailNotificationClicked>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailNotificationClicked';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailCampaignCreated extends EventBase {
    public campaign: EmailCampaign;
    public emailTemplate: EmailTemplate;

    public constructor(init?: Partial<EmailCampaignCreated>) {
      super(init);
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailCampaignCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailCampaignScheduled {
    public campaignId: CampaignId;
    public dateTime: UtcDateTime;

    public constructor(init?: Partial<EmailCampaignScheduled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailCampaignScheduled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailCampaignStarted {
    public campaignId: CampaignId;

    public constructor(init?: Partial<EmailCampaignStarted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailCampaignStarted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailCampaignStopped {
    public campaignId: CampaignId;

    public constructor(init?: Partial<EmailCampaignStopped>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailCampaignStopped';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailCampaignCompleted {
    public campaignId: CampaignId;
    public errors?: ErrorDto[];

    public constructor(init?: Partial<EmailCampaignCompleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailCampaignCompleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailCampaignFailed {
    public campaignId: CampaignId;
    public errors: ErrorDto[];

    public constructor(init?: Partial<EmailCampaignFailed>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailCampaignFailed';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailCampaignDeleted {
    public campaignId: CampaignId;

    public constructor(init?: Partial<EmailCampaignDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailCampaignDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailServiceEstablished {
    public defaultTemplates?: EmailTemplate[];

    public constructor(init?: Partial<EmailServiceEstablished>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailServiceEstablished';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailServiceEnabled {
    public constructor(init?: Partial<EmailServiceEnabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailServiceEnabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailServiceDisabled {
    public constructor(init?: Partial<EmailServiceDisabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailServiceDisabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailIntegrationCreated {
    public integration: EmailIntegration;

    public constructor(init?: Partial<EmailIntegrationCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailIntegrationCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailIntegrationUpdated {
    public integration?: EmailIntegration;

    public constructor(init?: Partial<EmailIntegrationUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailIntegrationUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailIntegrationSetAsDefault {
    public integrationId?: IntegrationId;

    public constructor(init?: Partial<EmailIntegrationSetAsDefault>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailIntegrationSetAsDefault';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailIntegrationDeleted {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<EmailIntegrationDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailIntegrationDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailIntegrationEnabled {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<EmailIntegrationEnabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailIntegrationEnabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailIntegrationDisabled {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<EmailIntegrationDisabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailIntegrationDisabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailSignatureSaved {
    public signature: EmailSignature;

    public constructor(init?: Partial<EmailSignatureSaved>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailSignatureSaved';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailSignatureDeleted {
    public id: EmailSignatureId;

    public constructor(init?: Partial<EmailSignatureDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailSignatureDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailTemplateCreated {
    public template: EmailTemplate;

    public constructor(init?: Partial<EmailTemplateCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailTemplateCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailTemplateUpdated {
    public template: EmailTemplate;
    public filesToBeDeleted?: string[];

    public constructor(init?: Partial<EmailTemplateUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailTemplateUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailTemplateDeleted {
    public templateId: TemplateId;
    public filesToBeDeleted?: string[];
    public fileIntegrationId?: IntegrationId;

    public constructor(init?: Partial<EmailTemplateDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailTemplateDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailTemplateArchived {
    public templateId: TemplateId;

    public constructor(init?: Partial<EmailTemplateArchived>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailTemplateArchived';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailTemplateUnArchived {
    public templateId: TemplateId;

    public constructor(init?: Partial<EmailTemplateUnArchived>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailTemplateUnArchived';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailTemplateCloned {
    public templateIdFrom: TemplateId;
    public template: EmailTemplate;

    public constructor(init?: Partial<EmailTemplateCloned>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailTemplateCloned';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailFooterSaved {
    public footer: EmailFooter;

    public constructor(init?: Partial<EmailFooterSaved>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailFooterSaved';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class EmailFooterDeleted {
    public id: EmailFooterId;

    public constructor(init?: Partial<EmailFooterDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'EmailFooterDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushBatchRegistered {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public startingAfter?: string;

    public constructor(init?: Partial<PushBatchRegistered>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushBatchRegistered';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushBatchStarted {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public recipients: PushRecipients;

    public constructor(init?: Partial<PushBatchStarted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushBatchStarted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushBatchCompleted {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public errors?: ErrorDto[];

    public constructor(init?: Partial<PushBatchCompleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushBatchCompleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushBatchFailed {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public errors?: ErrorDto[];

    public constructor(init?: Partial<PushBatchFailed>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushBatchFailed';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushNotificationProcessed {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public campaignBatchNotificationId: NotificationId;
    public sendNotificationResult?: SendNotificationResult;
    public recipients: PushRecipients;
    public errors?: ErrorDto[];

    public constructor(init?: Partial<PushNotificationProcessed>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushNotificationProcessed';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushNotificationRead {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public notificationId: NotificationId;

    public constructor(init?: Partial<PushNotificationRead>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushNotificationRead';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushNotificationClicked {
    public campaignId: CampaignId;
    public campaignBatchId: CampaignBatchId;
    public notificationId: NotificationId;
    public sourceId?: string;

    public constructor(init?: Partial<PushNotificationClicked>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushNotificationClicked';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushCampaignCreated {
    public campaign: PushCampaign;
    public pushTemplate: PushTemplate;

    public constructor(init?: Partial<PushCampaignCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushCampaignCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushCampaignScheduled {
    public campaignId: CampaignId;
    public dateTime: UtcDateTime;

    public constructor(init?: Partial<PushCampaignScheduled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushCampaignScheduled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushCampaignStarted {
    public campaignId: CampaignId;

    public constructor(init?: Partial<PushCampaignStarted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushCampaignStarted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushCampaignStopped {
    public campaignId: CampaignId;

    public constructor(init?: Partial<PushCampaignStopped>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushCampaignStopped';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushCampaignCompleted {
    public campaignId: CampaignId;
    public errors?: ErrorDto[];

    public constructor(init?: Partial<PushCampaignCompleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushCampaignCompleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushCampaignFailed {
    public campaignId: CampaignId;
    public errors: ErrorDto[];

    public constructor(init?: Partial<PushCampaignFailed>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushCampaignFailed';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushCampaignDeleted {
    public campaignId: CampaignId;

    public constructor(init?: Partial<PushCampaignDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushCampaignDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushDeviceCreated {
    public pushDevice: PushDevice;
    public userId: UserId;

    public constructor(init?: Partial<PushDeviceCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushDeviceCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushIntegrationCreated {
    public integration: PushIntegration;

    public constructor(init?: Partial<PushIntegrationCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushIntegrationCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushIntegrationUpdated {
    public integration?: PushIntegration;

    public constructor(init?: Partial<PushIntegrationUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushIntegrationUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushIntegrationSetAsDefault {
    public integrationId?: IntegrationId;

    public constructor(init?: Partial<PushIntegrationSetAsDefault>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushIntegrationSetAsDefault';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushIntegrationDeleted {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<PushIntegrationDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushIntegrationDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushIntegrationEnabled {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<PushIntegrationEnabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushIntegrationEnabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushIntegrationDisabled {
    public integrationId: IntegrationId;

    public constructor(init?: Partial<PushIntegrationDisabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushIntegrationDisabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushServiceEstablished {
    public defaultTemplates?: PushTemplate[];

    public constructor(init?: Partial<PushServiceEstablished>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushServiceEstablished';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushServiceEnabled {
    public constructor(init?: Partial<PushServiceEnabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushServiceEnabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushServiceDisabled {
    public constructor(init?: Partial<PushServiceDisabled>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushServiceDisabled';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushModuleTagSaved {
    public tag: TagDefinition;
    public communicationChannel: CommunicationChannel;

    public constructor(init?: Partial<PushModuleTagSaved>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushModuleTagSaved';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushModuleTagDeleted {
    public tag: Tag;
    public communicationChannel: CommunicationChannel;

    public constructor(init?: Partial<PushModuleTagDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushModuleTagDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushTemplateCreated {
    public template: PushTemplate;

    public constructor(init?: Partial<PushTemplateCreated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushTemplateCreated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushTemplateUpdated {
    public template: PushTemplate;

    public constructor(init?: Partial<PushTemplateUpdated>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushTemplateUpdated';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushTemplateDeleted {
    public templateId: TemplateId;

    public constructor(init?: Partial<PushTemplateDeleted>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushTemplateDeleted';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushTemplateArchived {
    public templateId: TemplateId;

    public constructor(init?: Partial<PushTemplateArchived>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushTemplateArchived';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  export class PushTemplateUnArchived {
    public templateId: TemplateId;

    public constructor(init?: Partial<PushTemplateUnArchived>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'PushTemplateUnArchived';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {}
  }

  /** @description Sign In */
  // @Route("/auth", "GET,POST")
  // @Route("/auth/{provider}", "GET,POST")
  // @Api(Description="Sign In")
  // @DataContract
  export class Authenticate implements IReturn<AuthenticateResponse>, IPost {
    /** @description AuthProvider, e.g. credentials */
    // @DataMember(Order=1)
    public provider: string;

    // @DataMember(Order=2)
    public userName: string;

    // @DataMember(Order=3)
    public password: string;

    // @DataMember(Order=4)
    public rememberMe?: boolean;

    // @DataMember(Order=5)
    public accessToken: string;

    // @DataMember(Order=6)
    public accessTokenSecret: string;

    // @DataMember(Order=7)
    public returnUrl: string;

    // @DataMember(Order=8)
    public errorView: string;

    // @DataMember(Order=9)
    public meta: { [index: string]: string };

    public constructor(init?: Partial<Authenticate>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'Authenticate';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new AuthenticateResponse();
    }
  }

  // @Route("/access-token")
  // @DataContract
  export class GetAccessToken
    implements IReturn<GetAccessTokenResponse>, IPost
  {
    // @DataMember(Order=1)
    public refreshToken: string;

    // @DataMember(Order=2)
    public meta: { [index: string]: string };

    public constructor(init?: Partial<GetAccessToken>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'GetAccessToken';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new GetAccessTokenResponse();
    }
  }

  // @Route("/apikeys")
  // @Route("/apikeys/{Environment}")
  // @DataContract
  export class GetApiKeys implements IReturn<GetApiKeysResponse>, IGet {
    // @DataMember(Order=1)
    public environment: string;

    // @DataMember(Order=2)
    public meta: { [index: string]: string };

    public constructor(init?: Partial<GetApiKeys>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'GetApiKeys';
    }
    public getMethod() {
      return 'GET';
    }
    public createResponse() {
      return new GetApiKeysResponse();
    }
  }

  // @Route("/apikeys/regenerate")
  // @Route("/apikeys/regenerate/{Environment}")
  // @DataContract
  export class RegenerateApiKeys
    implements IReturn<RegenerateApiKeysResponse>, IPost
  {
    // @DataMember(Order=1)
    public environment: string;

    // @DataMember(Order=2)
    public meta: { [index: string]: string };

    public constructor(init?: Partial<RegenerateApiKeys>) {
      (Object as any).assign(this, init);
    }
    public getTypeName() {
      return 'RegenerateApiKeys';
    }
    public getMethod() {
      return 'POST';
    }
    public createResponse() {
      return new RegenerateApiKeysResponse();
    }
  }
}
