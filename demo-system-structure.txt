This is the structure I could reverse engineer from my workshop
333330010008.

The ${bin} folder is:

    /home/ipol/ipolDevel/ipol_demo/modules/demorunner/binaries/333330010008/bin/

and its content is:

    cloud-detectors/
    venv

that is, the moved items indicated in the ddl (the cloud-detectors dir here),
the virtualenv directory venv.

The ${demoextras} folder is:

    /home/ipol/ipolDevel/shared_folder/demoExtras/333330010008

and its content is the unpacked demoxetra archive upploaded in the control
panel, i.e.:

    run.py
    run.sh
    tonemap.py
    unarchive.py

The directory in which the code (of the demoextra at least) is executed is

    /home/ipol/ipolDevel/shared_folder/run/333330010008/9A91A7E9ED746B3C2F77C68AB19A0F80

and it contains

    algo_info.txt
    input_0
    params.json
    stderr.txt
    stdout.txt
    tmp.tar.gz
    unpacked

That is, the downloaded input "input_0", the parameters, stdout and stderr.
This is the place where the "algo_infot.txt" has to be created (in ${bin} for
example, I won't work). The rest has been created by my code.

Variables accessible from the ddl:

    ${demoextras}
    ${bin}
    ${virtualenv}
    What else?

The $PATH variable is set as follows:

    /home/ipol/ipolDevel/ipol_demo/modules/demorunner/binaries/333330010007/bin/venv/bin:
    /home/ipol/ipolDevel/ipol_demo/modules/demorunner/binaries/333330010007/bin/:
    /home/ipol/ipolDevel/ipol_demo/modules/demorunner/venv/bin:
    /bin:
    /usr/bin:
    /usr/local/bin:
    /usr/local/matlab/R2015b:
    /home/ipol/ipolDevel/ipol_demo/modules/demorunner/Tools/PythonTools/

That is, the ${bin} is added to $PATH.

The sources (unpacked archive) are in:

    /home/ipol/ipolDevel/ipol_demo/modules/demorunner/binaries/333330010007/src/

The "construct" part of the ddl is run from this directory.
However, the virtualenv is not created yet and the $virtualenv variable is not
set.

If the "execution successful" appears but the "run" animated icon is still
thre, it means that there is an issue somewhere when interpreting the ddl.
Start by verifying your algo_info.txt if you have one...

--> Email to IPOL team...(?) DDL errors should make the demo fail and give an
    error message...
















0) dl code
1) construct: compile code
2) move

  --> /home/ipol/ipolDevel/ipol_demo/modules/demorunner/binaries/333330010008/bin/
  --> path available as $bin

3) execute code

  --> pwd=/home/ipol/ipolDevel/shared_folder/run/333330010008/9A91A7E9ED746B3C2F77C68AB19A0F80




/home/ipol/ipolDevel/
  --> ipol_demo
      --> modules
          --> demorunner
              --> binaries
                  --> <demo_id>
                      --> bin                   <-- moved code
                      --> src                   <-- unpacked archive
                      --> dl                    <-- dl archive
  --> shared_folder
      --> demoExtras
          --> <demo_id>
      --> run
          --> <demo_id>
              --> <demo_exec_id_random>



Code is downloaded in (...)/ipol_demo/modules/demorunner/binaries/<demo_id>/dl.

It is then decompressed in (...)/ipol_demo/modules/demorunner/binaries/<demo_id>/src.
WARNING! The consecutive build sections in the ddl overrite the src directory.
This means that if you've more than one build, only the last one remains.

There is a "build.log" in (...)/ipol_demo/modules/demorunner/binaries/build.log.
It contains the stdout of the "construct" section (e.g. cd machin && make truc)






