function Write-Color() {
    Param (
        [string] $text = $(Write-Error "You must specify some text"),
        [switch] $NoNewLine = $false
    )

    $startColor = $host.UI.RawUI.ForegroundColor;

    $text.Split( [char]"{", [char]"}" ) | ForEach-Object { $i = 0; } {
        if ($i % 2 -eq 0) {
            Write-Host $_ -NoNewline;
        } else {
            if ($_ -in [enum]::GetNames("ConsoleColor")) {
                $host.UI.RawUI.ForegroundColor = ($_ -as [System.ConsoleColor]);
            }
        }

        $i++;
    }

    if (!$NoNewLine) {
        Write-Host;
    }
    $host.UI.RawUI.ForegroundColor = $startColor;
}

Start-Sleep -Seconds 1.5

Write-Host "Loading..."

Write-Host "Enter total amount of money in Portfolio:"

python .\stock.py

Write-Host "`n"

`Write-Color "{yellow}All Done!"`

Write-Host "`n"

`Write-Color "{green}New file called {blue}'stocks-data.csv' {green}generated"`

Write-Host "`n"

$AllDone = Read-Host "Press 'Enter' to exit!"
