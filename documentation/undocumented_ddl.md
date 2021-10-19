Here is the knowledge I could gather on some undocumented functionality that
can be used in the "ddl" (json) file interpreted by the IPOL demo system.


The general section
-------------------

### "requirements" key

It can contain "DR1", to avoid the green server.


The build section
-----------------

### Python virtual environments

Example build section
```json
  "build": {
    "build1": {
      "url": "http://boucantrin.ovh.hw.ipol.im/static/hessel/itsr-ipol-demo/itsr_a69a41b.tar.gz",
      "virtualenv": "itsr_a69a41b/requirements.txt",
      "construct": "",
      "move": "itsr_a69a41b"
    }
  },
```
and associated run.sh
```bash
# activate virtualenv
# (the requirements for the code have already been installed by the system)
if [ -d $virtualenv ]
then
    1>&2 echo "source $virtualenv/bin/activate"
    source $virtualenv/bin/activate
else
    1>&2 echo "Could not active the virtual environment. Stopping now."
    exit 0
fi

# install (in the virtualenv) some other required packages for the run.py script
if python -c "import magic; import iio"
then
    1>&2 echo "Demoextras dependencies already satisfied."
else
    1>&2 echo "Installing demoextras dependencies."
    python -m pip install python-magic iio
fi

# Install itsr if needed.
if python -c "import itsr"
then
    1>&2 echo Package itsr already installed.
else
    1>&2 echo Installing package itsr
    python -m pip install -e ${bin}/itsr_a69a41b
fi
```

#### Comments

The virtual environment is *not* activated when the "construct" part of the
"build" section is executed.

Miguel said that no python packages should be installed there because they'll
be installed for the whole system.





The inputs section
------------------


### The "data" type

...



The params section
------------------


### The "checkbox" type

To se the default value to "false" (unchecked), use

    "default_value": ""

because the other false values, like "false" or "0" strangely evaluate to true.
Removing the "default_value" attribute from the description however also makes
the box unchecked.

