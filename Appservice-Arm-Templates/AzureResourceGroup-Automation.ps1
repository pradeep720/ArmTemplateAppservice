[CmdletBinding()]
Param(
	[Parameter(Mandatory=$true)]$location,
	[Parameter(Mandatory=$true)]$resourceGroupName
)

# $location = 'Australia Central'
# $resourceGroupName = 'pradeep-RG'

Write-Host "Starting to Create the ResourceGroup" 

# Create new resource group if not exists.
$rgAvail = Get-AzResourceGroup -Name $resourceGroupName -Location $location -ErrorAction SilentlyContinue

if(!$rgAvail){
    New-AzResourceGroup -Name $resourceGroupName -Location $location
}
