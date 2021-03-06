#!/bin/bash
# run locally: 
# source AnalyserLauncher.sh

# to run on the batch:
# sbatch -p wn --account=cn-test -o logs/analyser.log -e logs/analyser.log --job-name=analyser --ntasks=10 AnalyserLauncher.sh



#----------- USER'S DECISION BOARD --------------//

user="mratti"

# Enter the production label of the files that you want to analyse
declare -a FilesArray=(
                        #"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi150_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_y2021_T12_v1_t33_n30000_njd0"
                        #"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi150_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_y2021_T12_v1_t44_n30000_njd0"
                        #"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi235_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_y2021_T13_v1_t33_n30000_njd0"
                        #"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi235_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_y2021_T13_v1_t44_n30000_njd0"
                        #"photon_E1to200GeV_closeEcal_EEMerged_noPU_thrsLumi150_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_y2021_T12_v2_t33_n30000_njd0"
                        #"photon_E1to200GeV_closeEcal_EEMerged_noPU_thrsLumi150_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_y2021_T12_v2_t44_n30000_njd0"
                        #"photon_E1to200GeV_closeEcal_EEMerged_noPU_thrsLumi235_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_y2021_T13_v2_t33_n30000_njd0"
                        #"photon_E1to200GeV_closeEcal_EEMerged_noPU_thrsLumi235_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_y2021_T13_v2_t44_n30000_njd0"

# first batch
#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi180_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l235_T14_v1_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi180_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l235_T14_v1_t44_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi180_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l235_T14_v2_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi180_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l235_T14_v2_t44_n30000_njd0"

#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi235_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l180_T17_v1_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi235_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l180_T17_v1_t44_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi235_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l180_T17_v2_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi235_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l180_T17_v2_t44_n30000_njd0"

#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi400_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l450_T16_v1_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi400_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l450_T16_v1_t44_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi400_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l450_T16_v2_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi400_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l450_T16_v2_t44_n30000_njd0"

#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi450_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l400_T15_v1_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi450_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l400_T15_v1_t44_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi450_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l400_T15_v2_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi450_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l400_T15_v2_t44_n30000_njd0"


# second batch
"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi180_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l180_T170_v1_t33_n30000_njd0"
"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi180_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l180_T170_v1_t44_n30000_njd0"
"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi180_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l180_T170_v2_t33_n30000_njd0"
"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi180_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l180_T170_v2_t44_n30000_njd0"

#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi235_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l235_T140_v1_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi235_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l235_T140_v1_t44_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi235_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l235_T140_v2_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi235_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l235_T140_v2_t44_n30000_njd0"

#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi400_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l400_T150_v1_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi400_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l400_T150_v1_t44_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi400_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l400_T150_v2_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi400_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l400_T150_v2_t44_n30000_njd0"

#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi450_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l450_T160_v1_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EB_noPU_thrsLumi450_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l450_T160_v1_t44_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi450_pfrh3.0_seed3.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l450_T160_v2_t33_n30000_njd0"
#"photon_E1to100GeV_closeEcal_EEMerged_noPU_thrsLumi450_pfrh4.0_seed4.0_noMargin_thrRingEBXtalEE_shs1.0_maxd10.0_l450_T160_v2_t44_n30000_njd0"

)

#label="_T14_l235_thl180"
#label="_T17_l180_thl235"
#label="_T16_l450_thl400"
#label="_T15_l400_thl450"
#
#label="_T170_l180_thl180"
label="_T140_l235_thl235"
#label="_T150_l400_thl400"
#label="_T160_l450_thl450"

do_writeFiles=false

doMatching_simFraction=true
doMatching_simFraction_withHF=false
doMatching_deltaR=false



do_resolutionPlot='False'
do_scalePlot='False'
do_efficiencyPlot='False'
do_noiseRatePlot='False'
do_rankingPlot='False'
do_summaryPlot='True'
do_decisionPlot='False'
do_chi2Plot='False'

do_resoOverScale='True'
do_popUpPlot='False'

# -----  2. Advanced parameters ----- #

# Here you may want to leave the default parameters

# This option turned to true means Etrue=caloParticle_simEnergy. Otherwise, Etrue=caloParticle_energy 
use_simEnergy=true

# Choose whether you want to bin in ET or energy
do_binningEt=false

# Choose whether to use a finner binning or not
do_fineBinning_energy=true
do_fineBinning_eta=true

# This function turned to true fits the peak only, otherwise fits the whole distribution
do_fitPeak=true

# Choose one of the following fit (Crystal Ball, double-sided Crystal Ball or Bifurcated Gaussian)
do_CBfit=false
do_doubleCBfit=true
do_BGfit=false

#######################################################################

echo "Start" 

for iFile in ${FilesArray[@]}; do
   fileNameforPlotter="histo_"$iFile
   if [ "$doMatching_simFraction" = true ] ; then
      fileNameforPlotter=$fileNameforPlotter"_simFraction"
   fi
   if [ "$doMatching_simFraction_withHF" = true ] ; then
      fileNameforPlotter=$fileNameforPlotter"_simFraction_wHF"
   fi
   if [ "$doMatching_deltaR" = true ] ; then
      fileNameforPlotter=$fileNameforPlotter"_deltaR"
   fi
   echo $fileNameforPlotter
   echo $fileNameforPlotter >> fileSamples.txt
done


if [ "$do_writeFiles" = true ] ; then
   if [ "$do_popUpPlot" = 'False' ] ; then     
      root -l -q -b "../Plotter/EoverEtrue_fit.C+(\"$do_fineBinning_energy\", \"$do_fineBinning_eta\", \"$use_simEnergy\", \"$do_binningEt\", \"$do_CBfit\", \"$do_doubleCBfit\", \"$do_BGfit\", \"$do_fitPeak\", "false", "false", "false", "false", "false", "false", "false", "false", \"$do_writeFiles\", \"$user\")"
   fi
   if [ "$do_popUpPlot" = 'True' ] ; then
      root -l -q "../Plotter/EoverEtrue_fit.C+(\"$do_fineBinning_energy\", \"$do_fineBinning_eta\", \"$use_simEnergy\", \"$do_binningEt\", \"$do_CBfit\", \"$do_doubleCBfit\", \"$do_BGfit\", \"$do_fitPeak\", "false", "false", "false", "false", "false", "false", "false", "false", \"$do_writeFiles\", \"$user\")"
   fi 


fi

python 2DPlotProducer.py --doResolutionPlot=$do_resolutionPlot --doScalePlot=$do_scalePlot --doEfficiencyPlot=$do_efficiencyPlot --doNoiseRatePlot=$do_noiseRatePlot --doRankingPlot=$do_rankingPlot --doSummaryPlot=$do_summaryPlot --doDecisionPlot=$do_decisionPlot --doPopUpPlot=$do_popUpPlot --doResoOverScale=$do_resoOverScale --doChi2Plot=$do_chi2Plot --label=$label

rm fileSamples.txt
 
echo "Done"





