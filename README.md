## Installation 
- go in your favorite CMSSW release repository, e.g CMSSW_10_6_1_patch1
- cd CMSSW_10_6_1_patch1/src
- cmsenv
- git clone git@github.com:pfclustering/ECALPFClusterAnalysis.git


## Merge EEclose and EEfar
```
python EEmerger.py --f1 file_name_1.root --f2 file_name_2.root
```

## AnalyserLauncher

Both the Analyser and the Plotter are monitored in AnalyserLauncher.sh 

All the options are to be set directly inside the file, in the User's decision board.


### Utilisation

Run locally

```
source AnalyserLauncher.sh
```

or on the batch

```
sbatch -p wn --account=cn-test -o logs/analyser.log -e logs/analyser.log --job-name=analyser --ntasks=10 AnalyserLauncher.sh
```

### Options

- Choose what you want to do with `doAnalyser` and `doPlotter`. Both can be set to true at the same time
- Enter the dumped files that you want to work on
- Enter the directory where those files are stored
- Choose which matching strategy to use (choose one at a time)

If you want to run the Plotter:
- `do_resolutionPlot`, `do_scalePlot`, `do_efficiencyPlot`, `do_fakeRatePlot`: more than one option can be turn to true
- `do_efficiencyPlotOnly`: the previous options will run the fit, which can be time consuming. If you only want to see the efficiency plot (which doesn't need the fit), turn this option to True. No need to turn to False the previous options. 
NB: if `do_fakeRatePlot`is also set to True, then the fakeRate plots are also going to be produced (they don't rely on the fit neither).
- `do_ratioPlot`: makes the ratio between two files
- `do_useDifMatching`: (requires `do_ratioPlot=true`) makes the ratio between samples with different matching. In this case, write the inputfilename with the matching name appended.
- `do_scanThrs`: produces the plots looping on all the fileNames, at fixed energy or eta 
- `do_popUpPlot`: do you want to see the plot while the code is running? 


## Tuning
Add files that you want to study and which plots to produce in TuningLauncher.sh and do
```
source TuningLauncher.sh
```

### Get ratio maps
Write filenames of samples that you wish to compare, and do
```
python doRatioMaps.py
```

### Validator

Before launching a new production with significant changes, it is worth to check the basic distributions compared to previous productions.
This tool will produce comparison plots of basic distrbucions, starting from two outputs of the Analyzer.

Example of usage:
```
cd Validator
python validate.py -f1 /work/mratti/validation/histo_photon_E1to100GeV_closeEcal_EEclose_noPU_pfrhRef_seedRef_thrXtalEBXtalEE_y2021_new2021_n1000_simFraction_EE.root -f2 /work/mratti/validation/histo_photon_E1to100GeV_closeEcal_EEclose_noPU_pfrhRef_seedRef_thrXtalEBXtalEE_y2023_new2023_n1000_simFraction_EE.root -l1 new_2021 -l2 new_2023 -o 2021_vs_2023 --doNorm --doLog --rebin 2
```

### NoisePlotter
Multiple tasks are handled by this sub-package:
* determine ring-averages starting from xtal-dep thresholds
* write in txt files values of proposed thresholds to be sent to conveners for tag creation
* plot noise curves


1) Start from noise tags produced by Amina, with x-tal dependent thresholds, e.g. EcalPFRecHitThresholds_TL235_mixed
and get corresponding txt files following /work/mratti/cmssw_workarea/RECORD_DEVs/CMSSW_10_6_0/src/usercode/useful.sh
and copy EB and EE txt files to RecoSimStudies/Dumpers/data/noise/

2) for EB only, perform the average over the ring; the outliers, aka crystals more than 5 sigma away from the average, keep their own threshold.
The file for the ring average will be created, copied to $CMSSW_BASE/src/RecoSimStudies/Dumpers/data/noise/ and used for the sample production

```
for i in TL235 TL315 TL400 TL550;
do
  echo "*********************************"
  echo $i
  cd Plotter/noisePlotter/getEBRingAverage
  cp $CMSSW_BASE/src/RecoSimStudies/Dumpers/data/noise/PFRecHitThresholds_EB_$i.txt .
  root -l -b -q plotObject_untouched_ringaverage.cxx\(\"PFRecHitThresholds_EB_$i.txt\"\)
  root -l -b -q root2txt.C
  cp productCleaned.txt $CMSSW_BASE/src/RecoSimStudies/Dumpers/data/noise/PFRecHitThresholds_EB_ringaveraged_$i.txt
  cat $CMSSW_BASE/src/RecoSimStudies/Dumpers/data/noise/PFRecHitThresholds_EB_ringaveraged_$i.txt $CMSSW_BASE/src/RecoSimStudies/Dumpers/data/noise/PFRecHitThresholds_EE_$i.txt > ../PFRecHitThresholds_EB_ringaveraged_EE_$i.txt
  cd ../../..
  #
done
```


Now we can plot the thresholds and create new txt files with different noise multipliers.
Keep in mind that for EB we will always assume that the ring average has been performed with the correct outlier treatment, while for EE not.

3) Make the noise curves and produce a txt file with proposed thresholds. 
This will produce an intermediate directory with the outputs within.
```
cd Plotter/noisePlotter
root -l -b -q plotNoiseAverage.cxx\(\"PFRecHitThresholds_EB_ringaveraged_EE_${i}.txt\"\)
```

4) Then smooth the noise graph and merge EB and EE in a single one.
```
python getMergedGraph.py -t PFRecHitThresholds_EB_ringaveraged_EE_${i}
```
Output is in ```PFRecHitThresholds_EB_ringaveraged_EE_TL235/mergedGraphs.root```
Graphs to be used are ```merged_smooth_i``` where i is the multiplier of the sigma noise, to be drawn with "AL" options.

### SingleEventAnalyzer
Used to analyze and plot PFClusters in a single event.

Will produce histograms for all events chosen and for each pfcluster in the event, with x-tal level information on the energy of the rechits, fractions, best-matched caloparticle, energy of the cluster, etc.

* Choose an event number to check and add it in ```eventsToCheck``` in ```SingleEventPFClusterAnalyzer.C```; 
* note the convention on the event number is: evt=eventId-1
* define input and output in ```start_SingleEventPFClusterAnalyzer.C```
* run with ```root -l -b -q start_SingleEventPFClusterAnalyzer.C+```

Do the plotting:

* specify the events and clusters of your choice in ```eventPlotter.py```
* run with ```python eventPlotter.py```


### SCAnalyzer
To study the shower shapes in g+jets EM enriched samples.





