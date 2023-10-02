# On vérifie qu'on fonctionne bien sur un système Windows 10 ou 11
if ([System.Environment]::OSVersion.Version.Major -lt 10) {
    [System.Windows.MessageBox]::Show("Ce programme ne fonctionne que sur Windows 10 ou 11.", "Erreur", "OK", "Error")
    exit
}

# On vérifie que l'utilisateur utilise bien le script en tant qu'administrateur
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    [System.Windows.MessageBox]::Show("Ce programme doit être exécuté en tant qu'administrateur.", "Erreur", "OK", "Error")
    exit
}

# On vérifie que le script est bien exécuté en PowerShell
if ($host.Name -ne "ConsoleHost") {
    [System.Windows.MessageBox]::Show("Ce programme doit être exécuté en PowerShell.", "Erreur", "OK", "Error")
    exit
}

# On ferme tous les navigateurs web (meme s'il n'y en a pas)
Stop-Process -Name chrome -Force -ErrorAction SilentlyContinue
Stop-Process -Name firefox -Force -ErrorAction SilentlyContinue
Stop-Process -Name msedge -Force -ErrorAction SilentlyContinue
Stop-Process -Name opera -Force -ErrorAction SilentlyContinue

$elements = @(
    @{
        Name = 'Nettoyage de Windows Update'
        Command = 'Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase'
    },
    @{
        Name = 'Nettoyage de Windows Defender'
        Command = 'Remove-MpPreference -ExclusionPath "C:\Windows\SoftwareDistribution\Download"'
    },
    @{
        Name = 'Nettoyage des fichiers journaux de la mise à jour de Windows'
        Command = 'Remove-Item -Path "C:\Windows\Logs\WindowsUpdate\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage des fichiers programmes téléchargés'
        Command = 'Remove-Item -Path "$env:USERPROFILE\Downloads\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage des fichiers Internet temporaires'
        Command = 'Remove-Item -Path "$env:USERPROFILE\AppData\Local\Microsoft\Windows\INetCache\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage du fichier de vidange mémoire d''erreur système'
        Command = 'Remove-Item -Path "C:\Windows\Memory.dmp" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage des rapports d''erreurs Windows et commentaires'
        Command = 'Remove-Item -Path "C:\ProgramData\Microsoft\Windows\WER\ReportArchive\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage du cache de nuanceur DirectX'
        Command = 'Remove-Item -Path "$env:USERPROFILE\AppData\Local\Temp\D3DSCache\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage des fichiers d''optimisation de livraison'
        Command = 'Remove-Item -Path "$env:USERPROFILE\AppData\Local\Microsoft\Windows\DeliveryOptimization\Downloads\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage des packages de pilotes de périphériques'
        Command = 'pnputil.exe /delete-driver * /uninstall /force'
    },
    @{
        Name = 'Nettoyage des fichiers de ressource linguistique'
        Command = 'Remove-Item -Path "$env:USERPROFILE\AppData\Local\Microsoft\Windows\MUI\Cache\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage de la corbeille'
        Command = 'Clear-RecycleBin -Force -Recurse'
    },
    @{
        Name = 'Nettoyage des fichiers temporaires'
        Command = 'Remove-Item -Path "$env:TEMP\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage des fichiers d''installation temporaires de Windows'
        Command = 'Remove-Item -Path "C:\Windows\SoftwareDistribution\Download\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage des miniatures'
        Command = 'Remove-Item -Path "$env:USERPROFILE\AppData\Local\Microsoft\Windows\Explorer\*.db" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage du dossier de téléchargement'
        Command = 'Remove-Item -Path "$env:USERPROFILE\Downloads\*" -Force -or Remove-Item -Path "$env:USERPROFILE\Downloads\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage des anciennes données Prefetch'
        Command = 'Remove-Item -Path "C:\Windows\Prefetch\*" -Force -Recurse'
    }
    @{
        Name = 'Nettoyage du cache de Microsoft Edge'
        Command = 'Remove-Item -Path "$env:USERPROFILE\AppData\Local\Microsoft\Edge\User Data\Default\Cache\*" -Force -Recurse -and Remove-Item -Path "$env:USERPROFILE\AppData\Local\Microsoft\Edge\User Data\Default\CacheStorage\*" -Force -Recurse'
    }, 
    @{
        Name = 'Nettoyage du cache de Google Chrome'
        Command = 'Remove-Item -Path "$env:USERPROFILE\AppData\Local\Google\Chrome\User Data\Default\Cache\*" -Force -Recurse -and Remove-Item -Path "$env:USERPROFILE\AppData\Local\Google\Chrome\User Data\Default\CacheStorage\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage du cache de Mozilla Firefox'
        Command = 'Remove-Item -Path "$env:USERPROFILE\AppData\Local\Mozilla\Firefox\Profiles\*\cache2\entries\*" -Force -Recurse -and Remove-Item -Path "$env:USERPROFILE\AppData\Local\Mozilla\Firefox\Profiles\*\cache2\doomed\*" -Force -and Remove-Item -Path "$env:USERPROFILE\AppData\Local\Mozilla\Firefox\Profiles\*\cache2\index\*" -Force -Recurse'
    },
    @{
        Name = 'Nettoyage du cache de Opera'
        Command = 'Remove-Item -Path "$env:USERPROFILE\AppData\Roaming\Opera Software\Opera Stable\Cache\*" -Force -Recurse'
    }
)

foreach ($element in $elements) {
    Write-Host $element.Name
    Invoke-Expression $element.Command
}

Write-Host "Nettoyage terminé."