$scheduleObject = New-Object -ComObject schedule.service
$scheduleObject.connect()
$rootFolder = $scheduleObject.GetFolder("\")
$rootFolder.CreateFolder("RGRTech")

$Trigger = New-ScheduledTaskTrigger -AtStartup
$User = "NT AUTHORITY\SYSTEM"
$Action= New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -File C:\RGRTech\Powershell\Send-Telegram.ps1"

Register-ScheduledTask -TaskName "SendTelegramOnBoot" -Trigger $Trigger -User $User -Action $Action -TaskPath "RGRTech"


# Set-ExecutionPolicy Bypass
