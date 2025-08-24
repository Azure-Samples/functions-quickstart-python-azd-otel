# Core Modules - DEPRECATED

⚠️ **DEPRECATED**: These modules have been replaced with public Azure Verified Modules (AVM).

The core modules in this directory have been superseded by public Azure Verified Modules from the official Microsoft registry.

## Migration Guide

| Original Module | Replacement Public AVM Module |
|---|---|
| `identity/userAssignedIdentity.bicep` | `br/public:avm/res/managed-identity/user-assigned-identity:0.4.1` |
| `storage/storage-account.bicep` | `br/public:avm/res/storage/storage-account:0.8.3` |
| `message/servicebus.bicep` | `br/public:avm/res/service-bus/namespace:0.9.0` |
| `monitor/loganalytics.bicep` | `br/public:avm/res/operational-insights/workspace:0.11.1` |
| `monitor/applicationinsights.bicep` | `br/public:avm/res/insights/component:0.6.0` |
| `host/appserviceplan.bicep` | `br/public:avm/res/web/serverfarm:0.1.1` |

**Virtual Network**: Uses `br/public:avm/res/network/virtual-network:0.6.1`

## Benefits of Public AVM Modules

- **Official**: Direct from Microsoft's official registry
- **Standardized**: Follow official Microsoft best practices
- **Validated**: Thoroughly tested and maintained by Microsoft
- **Consistent**: Uniform parameter naming and output patterns
- **Enhanced**: Better documentation and metadata
- **Future-proof**: Regular updates and security patches
- **Version Control**: Explicit versioning for stability

## Usage Example

```bicep
module storage 'br/public:avm/res/storage/storage-account:0.8.3' = {
  name: 'storage'
  scope: rg
  params: {
    name: storageAccountName
    location: location
    tags: tags
    skuName: 'Standard_LRS'
    allowSharedKeyAccess: false
  }
}
```

Please use the public AVM modules for new deployments. All existing deployments have been migrated to use the public AVM registry following the Azure-Samples reference pattern.