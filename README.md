# HBP-Heroku

HBP-Heroku is a version of HyperUBot that was patched for Heroku and has [HyperBot++](https://github.com/userbot8895/HyperBot_Plus) preinstalled.

**Keep in mind that this repo won't be always up to date with the latest HyperUBot and HyperBot++ updates.** If you can run it on somewhere other than Heroku (preferably a PC/VPS or phone) install the regular HyperUBot and update it to HyperBot++ using its installation guide.

# HyperUBot

A customizable, modular Telegram userbot, with innovative components.

Copyright (C) 2020 nunopenim\
Copyright (C) 2020 prototype74

> Licensed under [PEL](https://github.com/nunopenim/HyperUBot/blob/master/LICENSE.md)

All rights reserved.

## What is this?

HyperUBot is a modular Telegram userbot written in Python which uses 
[Telethon](https://github.com/LonamiWebs/Telethon)'s API library by [LonamiWebs](https://github.com/LonamiWebs).
It does not require any form of database. It has support to be fully translatable, contains it's own package manager,
with an [official repo](https://github.com/nunopenim/module-universe) and the possibility to configure multiple extra community repos.
It contains also a sideloader for `.py` files sent in chat. The aim of this userbot is to become an extension of it's own user.
Instead of coming cluttered with all kinds of packages, it is fully customizable, aiming to be fast.

## Compatibility

HyperUBot works with Windows, macOS, Linux and Termux (although it's kinda the same as Linux). Right now, unfortunately Heroku is not supported. This is due to the way how Heroku handles bash processes, something needed for commands like .sysd, .rtt, .status or .ping.

We recommend using Ubuntu 18.04 or 20.04, as it's setup is a lot easier, and straight forward (there is no need of installing a package manager, such as apt-get, since it comes by default.)

## How to configure it

| Platforms | Guides |
| - | - |
| Android ([Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en)) | [SETUP_Termux.md](https://github.com/nunopenim/HyperUBot/blob/master/GUIDES/SETUP_Termux.md) |
| Arch Based Distros (Native Linux) | [SETUP_ArchBasedLinux.md](https://github.com/nunopenim/HyperUBot/blob/master/GUIDES/SETUP_ArchBasedLinux.md) |
| Debian Based Distros (Native Linux, WSL) | [SETUP_DebianBasedLinux.md](https://github.com/nunopenim/HyperUBot/blob/master/GUIDES/SETUP_DebianBasedLinux.md) |
| Red Hat Based Distros (Native Linux) | [SETUP_RHELBasedLinux](https://github.com/nunopenim/HyperUBot/blob/master/GUIDES/SETUP_RHELBasedLinux.md) |
| macOS | [SETUP_macOS.md](https://github.com/nunopenim/HyperUBot/blob/master/GUIDES/SETUP_MacOS.md) |
| Windows (PowerShell) | [SETUP_Windows.md](https://github.com/nunopenim/HyperUBot/blob/master/GUIDES/SETUP_Windows.md) |
| Unsupported Platforms | [Read this...](https://github.com/nunopenim/HyperUBot/blob/master/GUIDES/SETUP_Unsupported.md) |

## Report a bug

### How to proper report a bug

A bug report can be done either in the [Issues](https://github.com/nunopenim/HyperUBot/issues) section of this repository or
in our Telegram Support Group. In order to solve the bug or issue report from you as fast as possible, please answer the following requirements as detailed as possible (this can be used as a template):

- Which HyperUBot, Python and Telethon versions are you running?
- On which platform(s) did you run it?
- Describe the bug or issue as good as possible
- Provide the log which the bot did generate!

HyperUBot generates a log `hyper.log` in the bot's root directory automatically everytime you run the bot.
Please provide us this log, as it helps us a lot to figure out the bug or issue faster.\
Bugs or issues caused in user modules from [HyperUBot's modules universe](https://github.com/nunopenim/module-universe)
should be reported in [it's Issues](https://github.com/nunopenim/module-universe/issues) section.

### What we don't accept as a bug

We only provide support, if the bug or issue was **NOT** caused by third party modules or sources, that means only bugs that are caused from HyperUBot's official sources.
Bugs caused by non-official sources for example from sideloads are irrelevant and will be ignored (or closed in `Issues` section)

## Developing modules

A small, introductory guide in how to develop your modules can be found [here](https://github.com/nunopenim/HyperUBot/blob/master/GUIDES/DEV_DevelopingModules.md). This explains the basics in how to setup your module's .py file, so that HyperUBot can load it and run it when it is called.

## Support Groups and Channels

Currently we have a [News Channel](https://t.me/HyperUBotNews) (Click to join). Here you can find news about bot updates, changes in modules and releases in the [module-universe](https://github.com/nunopenim/module-universe).

We also have a [Support Group](https://t.me/HyperUBotSupport) (Click to join), where we will be there to discuss about the bot, fix some issues, and help you set up the bot, if you are stuck in a specific step.

## Maintainers

- [nunopenim](https://github.com/nunopenim)
- [prototype74](https://github.com/prototype74)

## Credits

### Special thanks

- [KebapciEBY](https://github.com/KebapciEBY), for the support and ideas he gave during development.

### Translators

- [nunopenim](https://github.com/nunopenim), for the Portuguese translation
