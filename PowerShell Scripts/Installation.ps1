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

`Write-Color "{green}Installing Dependencies..."`

Write-Host "`n"

pip install -r .\requirements.txt

Start-Sleep -Seconds 1

pip3 install yahoo-fin

Write-Host "`n"

`Write-Color "{green}Dependencies Installed!"`

Write-Host "`n"

$AllDone = Read-Host "Press 'Enter' to exit!"