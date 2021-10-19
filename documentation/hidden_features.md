demo_failure.txt
----------------

If a file named "demo_failure.txt" exists, the IPOL demo system will display
its content after warning that the demo failed.
However your script must exit successfully (exit code 0) for this message to be
displayed, so you're in charge of catching the errors.

This allows to catch common situation in wich your demo will fail and give the
user appropriate feedback.

If you have

    set -e

at the beginning of your script, remove it.
Then catch the error, create the file "demo_failure.txt" with your message,
then exit your script with exit code 0.

Example:

    ### unzip the given archive. IPOL demo system will have renamed it input_0
    ### option -q makes it quiet.
    unzip -q input_0
    if [ $? != 0 ]; then # input_0 is not a zip file
      echo "Failed to unzip the uploaded file." > demo_failure.txt
      exit 0
    fi

