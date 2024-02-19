KAPE (KROLL) Easy MFT Extract Script
==================================================

# EXECUTION GUIDELINES

## TEMPORARILY CHANGE FOR SESSION
To temporarily bypass the execution policies, either execute the following command in the command line (CMD) or start 'shell.bat', if necessary with administration rights.

powershell.exe -ExecutionPolicy Bypass

## CHANGE FOR CURRENT USER PROFILE
A user with administrative rights can change the execution policy for their user profile without changing the policy system-wide. RemoteSigned allows the execution of scripts created on the local computer and requires a digital signature for scripts downloaded from the Internet. To change the execution policy, the command must be executed outside the script and before it is executed in a PowerShell session with administrator rights. 

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# MANUAL BACKUP

## DUMP MFT
.\kape.exe --tsource SOURCE --target FileSystem --tdest TARGET --vhdx

SOURCE = source $MFT, usually C:\, D:\ etc.
TARGET = target directory, where should the dump be stored?

## MFTECMD
MFTECmd.exe --f SOURCE\$MFT --csv TARGET --csvf FILE.csv

SOURCE = Where is the previously created $MFT dump located?
TARGET = Where should the CSV file be saved?
FILE = How should the CSV file be saved?

# DELETED FILES
The Master File Table (MFT) of an NTFS file system can actually contain entries for previously existing (deleted) files. These files are no longer actively present in the file system, but information about them may still be present in the MFT until the specific MFT entry is overwritten. This is particularly useful in forensic investigations as it can provide insight into previous activity on a drive. When viewing the MFT with tools such as Eric Zimmerman's TimelineExplorer (EZ Tools), deleted files can be identified by certain characteristics:

## $I30-ENTRIES
Deleted files and folders can be found in the index attributes (known as $I30 entries) of the parent directory. These entries often contain references to the original name of the file or folder and the timestamp of the deletion.

## PREFIX "$" ENTRIES
Some special MFT entries that begin with "$", such as $LogFile or $Bitmap, contain information about the file system itself and can record changes, including the deletion of files.

## FILE STATUS
The TimelineExplorer and similar tools can sometimes show the status of a file, including whether it has been deleted. This can be visible through special markers or in the detailed views of the file properties.

## SEQUENCE NUMBERS
Timestamps such as date created, date last accessed, date last modified and date entered into the MFT can provide clues. Deleted files often retain their original timestamps. Sequence numbers in MFT entries can also provide clues. If a file is deleted and a new file with the same name is created, the sequence number of the MFT entry changes.

