$Env:CONDA_EXE = "/home/rreis/python/miniconda3_py313/bin/conda"
$Env:_CONDA_EXE = "/home/rreis/python/miniconda3_py313/bin/conda"
$Env:_CE_M = $null
$Env:_CE_CONDA = $null
$Env:CONDA_PYTHON_EXE = "/home/rreis/python/miniconda3_py313/bin/python"
$Env:_CONDA_ROOT = "/home/rreis/python/miniconda3_py313"
$CondaModuleArgs = @{ChangePs1 = $True}

Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs