# gifDisplay



This packge is used to display CSC hits and CSC local track for CMS events from simulation or data. Later in 2022 the GEM event display is added to display GEM pads and GEM simhits in GE11 chamber. 

## Setup
```
cmsrel CMSSW_12_5_0_pre2
cd CMSSW_12_5_0_pre2/src
cmsenv
git clone https://github.com/tahuang1991/gifDisplay.git
scram b -j 9
```
## How to use CSC event display package 


 1. CSCEventDisplay.py uses "process.source" to get input files.
  By default input rootfiles must have RAW data to be unpacked, using edmDumpEventContent one should 
  see event has "FEDRawDataCollection" type. Configure the process you need.
 
 1. CSCEventDisplay.py needs to read in the run range and event range for each display case from a txt file given by argument eventListFile
 
 1. save event and chamber id for which you want to make eventdisplay for in eventList.txt. by default it would display the neighbor GE11 chamber if it is to display ME11 chamber.  The GE21 part is not consider yet but can be added in future. 


   Format in eventListFile: runNumber eventNumber endcapID stationID ringID chamberID (note: use ringID=1 for both ME11a and ME11b). 
   and below is one example how the format in textfile looks like
```   
1 2002 1 1 1 34
1 2002 1 4 1 17
1 2038 2 1 1 6
1 2038 1 1 1 24
```
## Examples to run CSC display

>```
>./runDisplay.sh
>```

Make sure that sample path, plot directory and eventListFile are replaced with yours


## Reference
original package:
https://github.com/mhl0116/gifDisplay

email hualin.mei@cern.ch if you have any suggestions or questions
