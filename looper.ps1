# Cyberdrop-DL looper.ps1

$loop_count = 0
$loop_limit = 10

while ($true) {
    Clear-Host
    Write-Host "Cyberdrop-DL looper.ps1"

    python py/upgrade_pip_package.py cyberdrop-dl
    Clear-Host
    python py/latest_thread_to_urls.py
    Clear-Host
    python py/archive_logs.py
    Clear-Host

    $cdl_ver = (cyberdrop-dl --version).Split(' ')[1]
    $Host.UI.RawUI.WindowTitle = "${cdl_ver}: Looped (${loop_count}) times. -- $(Get-Date -Format 'hh:mm tt')"
    cyberdrop-dl --config-file config.yaml
    $loop_count++

    if ($loop_count -eq $loop_limit) {
        Write-Host "Sleeping for 3 hours..."
        Start-Sleep -Seconds 10800
        $loop_count = 0
    }
} 
