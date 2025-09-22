function Show-Spinner {
    param (
        [int]$Duration = 3,
        [string]$Message = "Preparing project..."
    )

    $spinner = "/-\|"
    $startTime = Get-Date
    Write-Host -NoNewline "$Message "
    $i = 0

    while ((Get-Date) - $startTime).TotalSeconds -lt $Duration) {
        $char = $spinner[$i % $spinner.Length]
        Write-Host -NoNewline $char
        Start-Sleep -Milliseconds 100
        Write-Host -NoNewline "`b"
        $i++
    }
    Write-Host " Done!"
}

Show-Spinner -Duration 3 -Message "Preparing project..."

$envName = "env"

if (-Not (Test-Path $envName)) {
    Write-Host "Creating virtual environment..."
    python -m venv $envName
} else {
    Write-Host "Virtual environment already exists."
}

Write-Host "Activating virtual environment..."
& "$envName\Scripts\Activate.ps1"

if (Test-Path "requirements.txt") {
    Write-Host "Installing requirements..."
    pip install -r requirements.txt
}

Write-Host "Well Done! Virtual environment is ready."
