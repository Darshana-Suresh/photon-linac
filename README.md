

This is an updated version of a linac head simulation from https://github.com/OpenGATE/GateContrib/tree/master/dosimetry/Radiotherapy/example12  The first part
aims at obtaining a phase-space (PhS) from electron source to a plane
just before the MLC. The second part makes use of this PhS as a
source.

- part1.mac : write a phase space in root format
- part2.mac : read a root phase space file as a source

Pre - Requisites
- Gate v8.2  https://opengate.readthedocs.io/en/latest/compilation_instructions.html#compilation-instructions-label
- Root 6.10.04
- python 3.6.9 (Only for output analysis)
- vv (Again, for analysing .mhd 3d output files)
   https://www.creatis.insa-lyon.fr/rio/vv/ 

How to run

    $ cd photon_linac  
    $ source <PATH TO GATE INSTALL DIRECTORY>/bin/gate_env.sh  
    $ mkdir output
    $ Gate mac/main.mac --qt

main.mac displays the geometric simulation of the linac. To run the beam production -

    $ Gate mac/part1.mac --qt

This creates output-PhS-g.root file in output folder. The phase space can be analyzed using root command.  

    $ root  
    $ root [0] TBrowser t 

Navigate to the phase space root file in the browser and analyze its components. Other graphs for analysis can also be viewed using -  

    $ root [1] .x PhS-Analysis.C

Use .q to exit from root. The root file is used as the source for transportation of the photon beams to the phantom. The second part is executed as follows - 

    $ Gate mac/part2.mac --qt

This creates the output files in the output folder.
These files can be analyzed using python graphs -

    $ python3 py/plot.py

The .mhd files can be opened using vv

    $ vv output/<filename>.mhd

To obtain a grid view of the .mhd files, run

    $ Gate mac/results.mac --qt

The present code opens output-full-Edep.mhd, you can change accordingly.

For more details, check out the references in the sources.md file in the main directory.

