Import-Module NTFSSecurity

function symlink($path,$target) {
     New-NTFSSymbolicLink -Path $path -Target $target
}
function multisymlink([array]$paths,$target)
{
    foreach($p in $paths)
    {
        symlink $p $target
    }
   
        if (! (Test-Path $paths))
        {
            return $Error
        }
}
