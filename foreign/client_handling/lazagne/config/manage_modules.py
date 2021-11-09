# Browsers
from foreign.client_handling.lazagne.softwares.browsers.chromium_based import chromium_browsers
from foreign.client_handling.lazagne.softwares.browsers.ie import IE
from foreign.client_handling.lazagne.softwares.browsers.mozilla import firefox_browsers
from foreign.client_handling.lazagne.softwares.browsers.ucbrowser import UCBrowser
# Chats
from foreign.client_handling.lazagne.softwares.chats.pidgin import Pidgin
from foreign.client_handling.lazagne.softwares.chats.psi import PSI
from foreign.client_handling.lazagne.softwares.chats.skype import Skype
# Databases
from foreign.client_handling.lazagne.softwares.databases.dbvis import Dbvisualizer
from foreign.client_handling.lazagne.softwares.databases.postgresql import PostgreSQL
from foreign.client_handling.lazagne.softwares.databases.robomongo import Robomongo
from foreign.client_handling.lazagne.softwares.databases.sqldeveloper import SQLDeveloper
from foreign.client_handling.lazagne.softwares.databases.squirrel import Squirrel
# Games
from foreign.client_handling.lazagne.softwares.games.galconfusion import GalconFusion
from foreign.client_handling.lazagne.softwares.games.kalypsomedia import KalypsoMedia
from foreign.client_handling.lazagne.softwares.games.roguestale import RoguesTale
from foreign.client_handling.lazagne.softwares.games.turba import Turba
# Git
from foreign.client_handling.lazagne.softwares.git.gitforwindows import GitForWindows
# Mails
from foreign.client_handling.lazagne.softwares.mails.outlook import Outlook
from foreign.client_handling.lazagne.softwares.mails.thunderbird import Thunderbird
# Maven
from foreign.client_handling.lazagne.softwares.maven.mavenrepositories import MavenRepositories
# Memory
from foreign.client_handling.lazagne.softwares.memory.keepass import Keepass
from foreign.client_handling.lazagne.softwares.memory.memorydump import MemoryDump
# Multimedia
from foreign.client_handling.lazagne.softwares.multimedia.eyecon import EyeCON
# Php
from foreign.client_handling.lazagne.softwares.php.composer import Composer
# Svn
from foreign.client_handling.lazagne.softwares.svn.tortoise import Tortoise
# Sysadmin
from foreign.client_handling.lazagne.softwares.sysadmin.apachedirectorystudio import ApacheDirectoryStudio
from foreign.client_handling.lazagne.softwares.sysadmin.coreftp import CoreFTP
from foreign.client_handling.lazagne.softwares.sysadmin.cyberduck import Cyberduck
from foreign.client_handling.lazagne.softwares.sysadmin.filezilla import Filezilla
from foreign.client_handling.lazagne.softwares.sysadmin.filezillaserver import FilezillaServer
from foreign.client_handling.lazagne.softwares.sysadmin.ftpnavigator import FtpNavigator
from foreign.client_handling.lazagne.softwares.sysadmin.opensshforwindows import OpenSSHForWindows
from foreign.client_handling.lazagne.softwares.sysadmin.openvpn import OpenVPN
from foreign.client_handling.lazagne.softwares.sysadmin.iiscentralcertp import IISCentralCertP
from foreign.client_handling.lazagne.softwares.sysadmin.keepassconfig import KeePassConfig
from foreign.client_handling.lazagne.softwares.sysadmin.iisapppool import IISAppPool
from foreign.client_handling.lazagne.softwares.sysadmin.puttycm import Puttycm
from foreign.client_handling.lazagne.softwares.sysadmin.rdpmanager import RDPManager
from foreign.client_handling.lazagne.softwares.sysadmin.unattended import Unattended
from foreign.client_handling.lazagne.softwares.sysadmin.vnc import Vnc
from foreign.client_handling.lazagne.softwares.sysadmin.winscp import WinSCP
from foreign.client_handling.lazagne.softwares.sysadmin.wsl import Wsl
# Wifi
from foreign.client_handling.lazagne.softwares.wifi.wifi import Wifi
# Windows
from foreign.client_handling.lazagne.softwares.windows.autologon import Autologon
from foreign.client_handling.lazagne.softwares.windows.cachedump import Cachedump
from foreign.client_handling.lazagne.softwares.windows.credman import Credman
from foreign.client_handling.lazagne.softwares.windows.credfiles import CredFiles
from foreign.client_handling.lazagne.softwares.windows.hashdump import Hashdump
from foreign.client_handling.lazagne.softwares.windows.ppypykatz import Pypykatz
from foreign.client_handling.lazagne.softwares.windows.lsa_secrets import LSASecrets
from foreign.client_handling.lazagne.softwares.windows.vault import Vault
from foreign.client_handling.lazagne.softwares.windows.vaultfiles import VaultFiles
from foreign.client_handling.lazagne.softwares.windows.windows import WindowsPassword


def get_categories():
    category = {
        'browsers': {'help': 'Web browsers supported'},
        'chats': {'help': 'Chat clients supported'},
        'databases': {'help': 'SQL/NoSQL clients supported'},
        'games': {'help': 'Games etc.'},
        'git': {'help': 'GIT clients supported'},
        'mails': {'help': 'Email clients supported'},
        'maven': {'help': 'Maven java build tool'},
        'memory': {'help': 'Retrieve passwords from memory'},
        'multimedia': {'help': 'Multimedia applications, etc'},
        'php': {'help': 'PHP build tool'},
        'svn': {'help': 'SVN clients supported'},
        'sysadmin': {'help': 'SCP/SSH/FTP/FTPS clients supported'},
        'windows': {'help': 'Windows credentials (credential manager, etc.)'},
        'wifi': {'help': 'Wifi'},
    }
    return category


def get_modules():
    module_names = [

        # Browser
        IE(),
        UCBrowser(),

        # Chats
        Pidgin(),
        Skype(),
        PSI(),

        # Databases
        Dbvisualizer(),
        Squirrel(),
        SQLDeveloper(),
        Robomongo(),
        PostgreSQL(),

        # games
        KalypsoMedia(),
        GalconFusion(),
        RoguesTale(),
        Turba(),

        # Git
        GitForWindows(),

        # Mails
        Outlook(),
        Thunderbird(),

        # Maven
        MavenRepositories(),

        # Memory
        MemoryDump(),  # retrieve browsers and keepass passwords
        Keepass(),  # should be launched after memory dump

        # Multimedia
        EyeCON(),

        # Php
        Composer(),

        # SVN
        Tortoise(),

        # Sysadmin
        ApacheDirectoryStudio(),
        CoreFTP(),
        Cyberduck(),
        Filezilla(),
        FilezillaServer(),
        FtpNavigator(),
        KeePassConfig(),
        Puttycm(),
        OpenSSHForWindows(),
        OpenVPN(),
        IISCentralCertP(),
        IISAppPool(),
        RDPManager(),
        Unattended(),
        WinSCP(),
        Vnc(),
        Wsl(),

        # Wifi
        Wifi(),

        # Windows
        Autologon(),
        Pypykatz(),
        Cachedump(),
        Credman(),
        Hashdump(),
        LSASecrets(),
        CredFiles(),
        Vault(),
        VaultFiles(),
        WindowsPassword(),
    ]
    return module_names + chromium_browsers + firefox_browsers
