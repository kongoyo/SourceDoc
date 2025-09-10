# 嘗試取得 HMC 虛擬主機，如果不存在則 vm 會是 null
$vm = Get-VM -Name HMC -ErrorAction SilentlyContinue

# 檢查 $vm 是否為 null
if ($vm -eq $null) {
    $ps = 'Off'
} else {
    $ps = [string]$vm.State
}

$psLow = $ps.ToLower()

# 驗證 $ps 的值
Write-Host "The value of `$ps` is: $psLow"