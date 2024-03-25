while getopts u:p: flag
do
    case "${flag}" in
        u) username=${OPTARG};;
        p) password=${OPTARG};;
    esac
done

# This command installs xcode command line tools
xcode-select --install

# This command installs homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# These two  command set the correct path so you can run homebrew commands
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> $HOMEDIR_PATH/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# This command install wget via hombrew
brew install wget

# This command pulls down Sonoma from Apple's CDN
wget https://swcdn.apple.com/content/downloads/62/37/052-40759-A_C4UWOSGC4S/ww0ftcbuatweg276cglca3e2d7g5hpvl2u/InstallAssistant.pkg

# This command prepares the Sonoma installer
sudo softwareupdate --fetch-full-installer --full-installer-version 14.4

echo $password | sudo /Applications/Install\ macOS\ Sonoma.app/Contents/Resources/startosinstall --agreetolicense --forcequitapps --user $username --stdinpass

#Add timer to notify end users update is complete
setalarm() {
    sleep $(echo "$1 * 60" | bc)
    say "Update complete system restart in 5 minutes"
    sleep $(echo "$1 * 3000" | bc)
}
setalarm .1
