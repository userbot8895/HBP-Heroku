from userbot import log
from os.path import basename

class ConfigClass(object):
    API_KEY = "You thought I'd leak my shit? hell no! not gonna leak my shit lmfao" # required tg Key
    API_HASH = API_KEY # required tg hash
    STRING_SESSION = API_HASH # Userbot Session String
 
    #
    # Userbot display language. Default is english ('en')
    #
    UBOT_LANG = "en"  # must match language code


    ### Optional configurations
    #
    # Logs any bot event to the specific chat
    #
    LOGGING = False  # Enable or disable logging
    LOGGING_CHATID = None  # Chat ID. Must be an integer

    #
    # Skips load specific module(s) e.g. ["admin"]
    #
    NOT_LOAD_MODUES = []  # must be a list or config will not work

    #
    # To store downloaded file(s) (temporary)
    #
    TEMP_DL_DIR = "./downloads"  # Default

    #
    # Community extra repos, leave as list of strings (or not)
    # The format of the repo should be "<github_username>/<github_repo>"
    # Example: "nunopenim/modules-universe" , although this is not a community repo :)
    #
    COMMUNITY_REPOS = ["userbot8895/HyperBot_Plus"]

