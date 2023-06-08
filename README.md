# Preparing for the DevNet Associate Certification (BRKCRT-2080)

In this repository you will fine the code that has been presented during the breakout session BRKCERT-2080 during Cisco Live 2023.  This README will serve as a basic set of instructions to use the files included as part of the live recording.
## Cloning the Code

In order to clone this code, change to the location on your computer in which you want the code, then execute the following

```bash
git clone https://github.com/qsnyder/brkcrt-2080
```

This will copy all of the files from this repository and add them locally to your machine

## Virtual Environments

Python's functionality can be extended through the use of packages or modules.  These modules are generally installed through `pip`.  However, because of conflicts that can occur between modules or needing to test between a variety of versions of the same module, it is recommended to separate the packages required for system operation separate from those required for coding or development projects.  This is accomplished through the use of Python virtual environments.

In order to use a virtual environment, Python and PIP must be installed (PIP is required to install the required modules after the creation of the virtual environment).  As of Python 3.5, it is recommended to use the `venv` module to create the virtual environment, and its included as part of the standard Python packaging.

```bash
cd ~/path/to/brkcrt-2080
python -m venv brkcrt2080
source brkcrt2080/bin/activate
```

> Note: it may be required to use `python3` in place of `python`

In the above example, the test `brkcrt2080` can be replaced with any desired name that is significant to you or the project on which you are working.  The `venv` module will install a Python operating environment within the folder bearing its name.  To activate the local Python operating environment, we use the `source` command, pointing to the `activate` binary.  This will change the prompt of your shell and indicate that you are working in a virtual environment and not the system environment.

In order to remove yourself from the virtual environment, you can use the command `deactivate`.  This will remove the virtual environment tag within your shell prompt.

## Installing Packages from a `requirements.txt` file

Once inside the desired virtual environment, we can install packages to support our Python code.  We can do this manually, using `pip` (or `pip3`, depending on how Python is referenced within your shell), or, if a maintainer of code has included a `requirements.txt` file, we can use this to automatically install a set of packages without having to manually type each one.  Once inside our virtual environment, we can install the packages using pip like so (assuming that you are still in the directory containing the cloned code):

```bash
(brkcrt2080)> pip install -r requirements.txt
```

This will install all required packages defined by the list given within `requirements.txt`.  We can execute `pip freeze` to ensure the packages are indeed installed.

## Running the Code

Once you have the virtual environment created and the required packages installed, we can execute the Python code using the Python binary `python 10-meraki-get-orgs.py` or `python 20-meraki-get-devices.py``

## Sample Outputs

### `10-meraki-get-orgs.py`

```
(brkcrt2080) qsnyder@qsnyder-devbox:~/brkcrt-2080 (main) $ python 10-meraki-get-orgs.py
[{'api': {'enabled': True},
  'cloud': {'region': {'name': 'North America'}},
  'id': '575334852396584364',
  'licensing': {'model': 'co-term'},
  'management': {'details': [{'name': 'MSP ID', 'value': '123456'}]},
  'name': 'PM_Test',
  'url': 'https://n22.meraki.com/o/HFyNGaw/manage/organization/overview'},
....
```

### `20-meraki-get-devices.py`

```
(brkcrt2080) qsnyder@qsnyder-devbox:~/brkcrt-2080 (main) $ python 20-meraki-get-devices.py
[{'id': '575334852396584364', 'name': 'PM_Test', 'url': 'https://n22.meraki.com/o/HFyNGaw/manage/organization/overview', 'api': {'enabled': True}, 'licensing': {'model': 'co-term'}, 'cloud': {'region': {'name': 'North America'}}, 'management': {'details': [{'name': 'MSP ID', 'value': '123456'}]}}, {'id': '573083052582915264', 'name': 'Thisisaneworg', 'url': 'https://n18.meraki.com/o/iui3abs/manage/organization/overview', 'api': {'enabled': True}, 'licensing': {'model': 'co-term'}, 'cloud': {'region': {'name': 'North America'}}, 'management': {'details': [{'name': 'MSP ID', 'value': '123456'}]}}, {'id': '575334852396584315', 'name': 'Test 1', 'url': 'https://n22.meraki.com/o/AzTrDcw/manage/organization/overview', 'api': {'enabled': True}, 'licensing': {'model': 'co-term'}, 'cloud': {'region': {'name': 'North America'}}, 'management': {'details': []}},
```

## Questions/Concerns

Please reach out to me via Twitter DM [@qsnyder](https://twitter.com/qsnyder)
