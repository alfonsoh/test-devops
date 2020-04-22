# Creative Cloud CleanerTool
sudo /Volumes/CleanerTool/Adobe\ Creative\ Cloud\ Cleaner\ Tool.app/Contents/MacOS/Adobe\ Creative\ Cloud\ Cleaner\ Tool --eulaAccepted=1 --removeAll=ALL

# Adobe Cleaner
sudo rm -rf /Applications/Adobe* /Applications/Utilities/Adobe* /Library/Application\ Support/Adobe /Library/Preferences/com.adobe.* /Library/PrivilegedHelperTools/com.adobe.* /private/var/db/receipts/com.adobe.* ~/Library/Application\ Support/Adobe* ~/Library/Application\ Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments/com.adobe* ~/Library/Application\ Support/CrashReporter/Adobe* ~/Library/Caches/Adobe ~/Library/Caches/com.Adobe.* ~/Library/Caches/com.adobe.* ~/Library/Cookies/com.adobe.* ~/Library/Logs/Adobe* ~/Library/PhotoshopCrashes ~/Library/Preferences/Adobe* ~/Library/Preferences/com.adobe.* ~/Library/Preferences/Macromedia* ~/Library/Saved\ Application\ State/com.adobe.*

# Check for 60 gb of disk space then run installer

# Run the installer
sudo installer -pkg gameheads_cc_full_Install.pkg -target /
