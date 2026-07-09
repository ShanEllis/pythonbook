# Installing Python

<div style="border-left: 5px solid red; padding: 10px; background-color: #fff3cd;">
<strong>Note:</strong> If you are taking COGS 18, you do not <i>need</i> to install Python on your local machine.
</div>

## Installing Python on a Windows Machine

There are three possible ways to install Python on a windows machine:

1. Through the microsoft store: The most straightforward way to install Python on a windows Machine.

2. Through the Python website: This is the most common way to install Python on a windows machine.

3. Through Anaconda: Anaconda is a distribution of Python that comes with a lot of packages pre-installed. This will include the standard library and additional external packages that we will introduce and use toward the end of the book.

Before we get started, let's check if Python is already installed on your machine. Open your start menu by clicking the `Windows` key on your keyboard. Then type in `powershell` and open the application (if you can't find powershell, type in `command prompt` instead and open that). You should have cool terminal open that makes you feel like a hacker!

![powershell](../images/01-intro/powershell.png)

In the terminal, type in `python --version` and press enter
![Python Not Installed](../images/01-intro/python-not-installed.png)

If you do not have python installed, you would proceed to install it in one of the following ways.

### Installing Python through the Microsoft Store (Windows 10 or 11)

1. Go to the Microsoft Store from your start menu and search for Python.

   a. You will find multiple versions of Python, but for this course we will be using Python 3.XX

2. Install the python version by clicking the `Get` button.

3. Once installed, go back to `powershell/command prompt` and type in `python --version` or `py --version`to confirm that Python has been installed. If it is installed, you will see something like this:

   ![Python Installed](../images/01-intro/python-version.png)

You should be good to go! You now have access to Python in the terminal and Python's IDLE (Integrated Development and Learning Environment).

A quick note about the Microsoft Store install of Python:

According to official docs from the [Python Software Foundation](https://docs.python.org/3/using/windows.html#the-microsoft-store-package) the Microsoft store installation of python is an easily installable version directed for interactive use cases, specifically for Students. For the purposes of this textbook, the Microsoft Store installation of Python is sufficient, however do note that there are issues with the [redirection of local data, registry and temporary paths](https://docs.python.org/3/using/windows.html#the-microsoft-store-package) that may prevent you from write access to certain file locations. It is unlikely that anything in this textbook will require you to modify any such data, but if you run into this issue, you may want to consider the Full installation of Python through their **official** website which we will highlight below.

### Installing Python through the Python Website

1. Go to the [Python website](https://www.python.org/downloads/)

2. Click on the download button to download the latest version of Python.

3. Launch the installer and you should see a screen that look similar to this:

   ![Python Installer](../images/01-intro/python-setup.png)

4. Make sure to check the box that says `Add Python to PATH` and click `Install Now`.

5. You should be able to go into Powershell/Command Prompt and type in `python --version` or `py --version` to confirm that Python has been installed.

## Installing Python on a Mac

As with Windows, before we install anything, let's check whether Python is already on your machine. Open your Terminal by going to `Finder` -> `Applications` -> `Utilities` -> `Terminal` (or press `Cmd + Space` and type `Terminal`). Then, type in `python3 --version` and press enter.

If you see something like `Python 3.12.2`, Python 3 is already installed and you're good to go!

A note before you do this: on a Mac that has never had developer tools installed, typing `python3` may cause a pop-up asking if you'd like to install the "command line developer tools". If you click `Install`, macOS will install a version of Python 3 for you (along with some other useful tools) - a perfectly fine option! If you'd rather install Python directly, click `Cancel` and follow the instructions below.

There are two common ways to install Python on a Mac:

1. Through the Python website: The most straightforward and most common approach.

2. Through Homebrew: A good option *if* you already use the Homebrew package manager.

### Installing Python through the Python Website

1. Go to the [Python website](https://www.python.org/downloads/). The site will detect that you're on a Mac and offer you the latest version of Python.

2. Click the download button to download the macOS installer.

3. Open the downloaded `.pkg` file and follow the prompts in the installer (`Continue`, agree to the license, `Install`). You may be asked for your password.

4. Once the installer finishes, open a **new** Terminal window and type in `python3 --version` to confirm that Python has been installed.

A quick note about `python` vs `python3` on a Mac:

On Macs, you'll want to get in the habit of typing `python3` (rather than just `python`) to launch Python, as the `python` command may not be defined (or, on older machines, may point to a very old Python 2 installation that you do *not* want to use). Similarly, use `pip3` anywhere this book says `pip`.

### Installing Python through Homebrew

[Homebrew](https://brew.sh/) is a popular package manager for macOS - a command line tool for installing software. If you already have Homebrew installed, you can install Python with a single command in your Terminal:

```
brew install python
```

Once it finishes, confirm the installation with `python3 --version`.

If you *don't* already use Homebrew, we recommend sticking with the Python website installation above - it's simpler, and there's no need to install a package manager just for this.
