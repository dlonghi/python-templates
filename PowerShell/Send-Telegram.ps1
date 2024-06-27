[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$TelegramToken = "xxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$TelegramChatID = "-xxxxxxxxxx"

$Hostname = [System.Net.Dns]::GetHostName()
$TelegramMessage = "$Hostname booted"
$TelegramURL = "https://api.telegram.org/bot$TelegramToken/sendMessage?chat_id=$TelegramChatID&text=$TelegramMessage"

$TelegramOk = 0
$BreakLoop = 0
while ($TelegramOk -eq 0) {
    try {
        $resp = Invoke-RestMethod -Method Post -Uri $TelegramURL
        if ($resp.ok -eq "True") {
            $TelegramOk = 1
        }
    } catch {
        Write-Host "not ok"
    }

    Start-Sleep -s 30

    $BreakLoop = $BreakLoop + 1
    Write-Host "BreakLoop = $BreakLoop"
    if ($BreakLoop -eq 20) {
        break
    }
}

# New-NetFirewallRule -DisplayName "Block_Telegram" -Direction Outbound -LocalPort Any -Protocol Any -Action Block -RemoteAddress 149.154.167.220/16
# Get-netfirewallrule -DisplayName "Block_Telegram"
# Remove-NetFirewallRule -DisplayName "Block_Telegram"


# -ExecutionPolicy Bypass
