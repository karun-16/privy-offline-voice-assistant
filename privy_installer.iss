[Setup]
AppName=Privy Voice Assistant
AppVersion=1.0
DefaultDirName={pf}\Privy Assistant
DefaultGroupName=Privy Assistant
OutputDir=output
OutputBaseFilename=PrivySetup
Compression=lzma
SolidCompression=yes
SetupIconFile=D:\KARUNYA\Privy_Assistant\privy.ico

[Files]
Source: "D:\KARUNYA\Privy_Assistant\dist\Privy Assistant V1\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Privy Assistant"; Filename: "{app}\main.exe"
Name: "{autodesktop}\Privy Assistant"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "Launch Privy Assistant"; Flags: nowait postinstall skipifsilent
