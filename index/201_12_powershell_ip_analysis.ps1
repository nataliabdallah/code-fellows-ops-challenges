$target = "network_report.txt"
$path = "C:\Users\natali\Documents\"
ipconfig /all > $path$target

echo "created report"

Select-String -Path $path$target -Pattern 'IPv4'
