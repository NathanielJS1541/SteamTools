
|Code Style| |Black| |Dependabot| |Bandit| |ReviewDog|

SteamTools
==========
A collection of tools written in Python with a textual TUI to access data from
Steam. This is basically a TUI for `ValvePython/steam`_, and will likely be in
development for a while.

=============
Prerequisites
=============
This repo uses `poetry`_ as a dependency manager, so you should have it
installed for using this repo. My recommended install method is to use
`pipx`_.

I recommend `pipx`_ as it installs applications in isolated environments,
so you won't end up causing dependency conflicts, and each application can
have dependencies of different versions of the same library.

.. role:: bash(code)
   :language: bash

.. role:: powershell(code)
    :language: PowerShell

---------------
Install `pipx`_
---------------
For more information and troubleshooting, please see `pipx`_.

- On Linux:

  1. :bash:`python3 -m pip install --user pipx`
  2. :bash:`python3 -m pipx ensurepath`

- On Windows:
  (Replace :powershell:`python` with :powershell:`python3` if you got Python
  from the Microsoft Store)

  1. :powershell:`python -m pip install --user pipx`
  2. Navigate to :powershell:`C:\<USER>\AppData\Roaming\Python\Python3x\Scripts`
     in a Terminal. This assumes you didn't install Python with a package manager.
  3. :powershell:`.\pipx ensurepath`

- On macOS:

  1. :bash:`brew install pipx`
  2. :bash:`pipx ensurepath`

-----------------
Install `poetry`_
-----------------
Once `pipx`_ is installed, installing poetry is trivial: :bash:`pipx install poetry`

It can also be upgraded with :bash:`pipx upgrade poetry`

==================
Running SteamTools
==================
1. Clone the repo: :bash:`git clone https://github.com/NathanielJS1541/SteamTools.git`
2. Navigate to the repo root in a terminal: :bash:`cd SteamTools`
3. Initialise `poetry`_: :bash:`poetry install`
4. Run the application: (Replace with :bash:`python3` if necessary) :bash:`poetry run python -m steamtools`

======================
Configuring SteamTools
======================
You can create a config file for SteamTools to use in a TOML file manually, or through the TUI.
To write the config from the TUI, press the "Config" button from the dashboard.
To write the config manually, see below.

1. Create the directory :code:`~/.config/steamtools/`. This is consistent across all platforms.
2. Create the file :code:`~/.config/steamtools/config.toml`.
3. Add in the contents of the example config below, and change them as necessary.

---------------------------
Example :code:`config.toml`
---------------------------

.. code:: TOML

  # This section contains details about your user account.
  # This file can optionally be generated from the TUI.
  [account]
  # The API key for your steam account.
  # To get one, see https://steamcommunity.com/dev/apikey
  api = "API Key"
  # Your steam username (From your community URL).
  # For example, https://steamcommunity.com/id/username1
  username = "username1"
  # The user ID linked with your steam account.
  userid = "1234567"

.. _ValvePython/steam: https://github.com/ValvePython/steam

.. _poetry: https://python-poetry.org/

.. _pipx: https://pypa.github.io/pipx/

.. |Code Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: The Python coding style used in this repo

.. |Black| image:: https://github.com/NathanielJS1541/SteamTools/actions/workflows/black_format.yml/badge.svg?event=push
    :target: https://github.com/NathanielJS1541/SteamTools/actions/workflows/black_format.yml
    :alt: Status of the black format checker

.. |Dependabot| image:: https://badgen.net/github/dependabot/NathanielJS1541/SteamTools
    :target: https://github.com/NathanielJS1541/SteamTools/actions/dependabot.yml
    :alt: Dependabot Status

.. |Bandit| image:: https://github.com/NathanielJS1541/SteamTools/actions/workflows/bandit.yml/badge.svg
    :target: https://github.com/NathanielJS1541/SteamTools/actions/workflows/bandit.yml
    :alt: Bandit Status

.. |ReviewDog| image:: https://github.com/NathanielJS1541/SteamTools/actions/workflows/reviewdog.yml/badge.svg
    :target: https://github.com/NathanielJS1541/SteamTools/actions/workflows/reviewdog.yml
    :alt: ReviewDog Status
