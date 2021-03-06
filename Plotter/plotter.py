#example of use: 
# python plotter.py -f histo_singlePhoton_5k_EB --doClusterAnalysis --doEB



from ROOT import TH1F, TGraph, TGraph2D, TCanvas, TLegend, TFile, TTree, gROOT, TF1, TLatex, gStyle, TH2D, gPad, TColor,TMultiGraph, TH1
from ROOT import kRed, kBlue, kGray, kGreen, kPink, kYellow, kBlack, kWhite, kPink, kMagenta, kTRUE, kFALSE, kOrange, kViolet, kAzure, kSpring
from ROOT import TEfficiency
import itertools
import sys
import os
sys.path.append('utils')
sys.path.append('./')
#from spares import *
#import graphUtils as gU
from array import *
from analyzeRecHits import beautify1DPlot


colors = [   kOrange+1, kRed, kMagenta+2, kViolet+8, kAzure-8, kAzure+6 ,
             kGreen+1, kSpring+4, kYellow -5, kYellow -3, kYellow, kOrange ]


if __name__ == "__main__":

    from argparse import ArgumentParser
    parser = ArgumentParser(description='', add_help=True)
    parser.add_argument('-f', '--inputFile', type=str, dest='inputFile', help='e.g. path/to/file/filename', default=None)
    parser.add_argument('--doClusterAnalysis', dest='doClusterAnalysis', help='beautify 1D plot', action='store_true', default=False)
    parser.add_argument('--doEB', dest='doEB', help='plot EB', action='store_true', default=False)
    parser.add_argument('--doEE', dest='doEE', help='plot EE', action='store_true', default=False)



options = parser.parse_args()


		  #gStyle.SetOptStat('emMrRo')
TH1.StatOverflows(kTRUE) # if false stats will be calculated without overflow, must be set also at filling time
TH1.SetDefaultSumw2()

		  ####################################
		  ## Define input, output and parameters
		  ####################################
#version = '{}_{}'.format(options.prodVersion, options.ecalVersion)
		  #inputfile = '{a}_{v}_numEvent{n}.root'

inputFile = options.inputFile
inputfile = '../Analyzer/outputfiles/{f}.root'.format(f=inputFile)

outputdir_superCluster = 'myPlots/{f}/superCluster'.format(f=inputFile)
outputdir_pfCluster = 'myPlots/{f}/pfCluster_caloMatched'.format(f=inputFile)
outputdir_caloParticle = 'myPlots/{f}/caloParticle'.format(f=inputFile)
os.system('mkdir myPlots/{f}'.format(f=inputFile))
os.system('mkdir {}'.format(outputdir_superCluster))
os.system('mkdir {}'.format(outputdir_pfCluster))
os.system('mkdir {}'.format(outputdir_caloParticle))


		  ####################################
		  ## Do analysis
		  ####################################


if options.doClusterAnalysis:
   if options.doEB:

		  #inputfile = inputfile.format(a=anaName, s=1.0, g=1.0, n=150000, v=version)
        inputfile = inputfile.format(f=inputFile)

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_energy_EB', xtitle='caloMatched PFCluster energy [GeV]', ytitle='Entries', xrange=None)    

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_size_EB', xtitle='number of caloMatched PFClusters per event', ytitle='Entries', xrange=(0.,10.))

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_nRecHit_EB', xtitle='number of crystals per caloMatched PFCluster', ytitle='Entries', xrange=(0.,40.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_nXtals_EB', xtitle='number of crystals per caloParticle', ytitle='Entries', xrange=(0.,45.))

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_et_EB', xtitle='caloMatched PFCluster ET [GeV]', ytitle='Entries', xrange=None)
        
        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_eta_EB', xtitle='caloMatched PFCluster eta', ytitle='Entries', xrange=(-4.,4.))

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_phi_EB', xtitle='caloMatched PFCluster phi', ytitle='Entries', xrange=(-3.2,3.2))

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_eOverEtrue_EB', xtitle='inclusive E/Etrue', ytitle='Entries', xrange=(0.,1.5))
        
        


        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBM_energy', xtitle='EBM caloMatched PFCluster energy [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBM_size', xtitle='EBM number of caloMatched PFClusters per event', ytitle='Entries', xrange=(0.,10.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBM_nXtals', xtitle='EBM number of crystals per caloParticle', ytitle='Entries', xrange=(0.,45.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBM_et', xtitle='EBM caloMatched PFCluster ET [GeV]', ytitle='Entries', xrange=None)
        
        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBM_eta', xtitle='EBM caloMatched PFCluster eta', ytitle='Entries', xrange=(-4.,4.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBM_phi', xtitle='EBM caloMatched PFCluster phi', ytitle='Entries', xrange=(-3.2,3.2))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBM_eOverEtrue', xtitle='EBM E/Etrue', ytitle='Entries', xrange=(0.,1.5))
       

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBP_energy', xtitle='EBP caloMatched PFCluster energy [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBP_size', xtitle='EBP number of caloMatched PFClusters per event', ytitle='Entries', xrange=(0.,10.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBP_nXtals', xtitle='EBP number of crystals per caloParticle', ytitle='Entries', xrange=(0.,45.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBP_et', xtitle='EBP caloMatched PFCluster ET [GeV]', ytitle='Entries', xrange=None)
        
        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBP_eta', xtitle='EBP caloMatched PFCluster eta', ytitle='Entries', xrange=(-4.,4.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBP_phi', xtitle='EBP caloMatched PFCluster phi', ytitle='Entries', xrange=(-3.2,3.2))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EBP_eOverEtrue', xtitle='EBP E/Etrue', ytitle='Entries', xrange=(0.,1.5))
       



        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_genEnergy_EB', xtitle='caloParticle energy [GeV]', ytitle='Entries', xrange=None)    

        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_simEnergy_EB', xtitle='caloParticle energy (sim) [GeV]', ytitle='Entries', xrange=None)    

        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_size_EB', xtitle='number of caloParticle per event', ytitle='Entries', xrange=(0.,11.))

        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_et_EB', xtitle='caloParticle ET [GeV]', ytitle='Entries', xrange=None)
        
        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_genEta_EB', xtitle='caloParticl eta', ytitle='Entries', xrange=(-4.,4.))

        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_genPhi_EB', xtitle='caloParticle phi', ytitle='Entries', xrange=(-3.2,3.2))



        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBM_energy', xtitle='EBM caloParticle energy [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBM_simEnergy', xtitle='EBM caloParticle energy (sim) [GeV]', ytitle='Entries', xrange=None)    
 
        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBM_size', xtitle='EBM number of caloParticle per event', ytitle='Entries', xrange=(0.,10.))

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBM_et', xtitle='EBM caloParticle ET [GeV]', ytitle='Entries', xrange=None)
        
        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBM_eta', xtitle='EBM caloParticle eta', ytitle='Entries', xrange=(-4.,4.))

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBM_phi', xtitle='EBM caloParticle phi', ytitle='Entries', xrange=(-3.2,3.2))

       

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBP_energy', xtitle='EBP caloParticle energy [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBP_simEnergy', xtitle='EBP caloParticle energy (sim) [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBP_size', xtitle='EBP number of caloParticle per event', ytitle='Entries', xrange=(0.,10.))

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBP_et', xtitle='EBP caloParticle ET [GeV]', ytitle='Entries', xrange=None)
        
        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBP_eta', xtitle='EBP caloParticle eta', ytitle='Entries', xrange=(-4.,4.))

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EBP_phi', xtitle='EBP caloParticle phi', ytitle='Entries', xrange=(-3.2,3.2))
       

        #superCluster
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_energy_EB', xtitle='superCluster energy EB [GeV]', ytitle='Entries', xrange=None)    
        
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_eta_EB', xtitle='superCluster eta EB', ytitle='Entries', xrange=(-4.,4.))

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_phi_EB', xtitle='superCluster phi EB', ytitle='Entries', xrange=(-3.2,3.2))

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_r9_EB', xtitle='superCluster r9 EB', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_sigmaIetaIeta_EB', xtitle='superCluster sigmaIetaIeta EB', ytitle='Entries', xrange=None)
       
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_sigmaIetaIphi_EB', xtitle='superCluster sigmaIetaIphi EB', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_sigmaIphiIphi_EB', xtitle='superCluster sigmaIphiIphi EB', ytitle='Entries', xrange=None)

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_full5x5_r9_EB', xtitle='superCluster full5x5 r9 EB', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_full5x5_sigmaIetaIeta_EB', xtitle='superCluster full5x5 sigmaIetaIeta EB', ytitle='Entries', xrange=None)
       
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_full5x5_sigmaIetaIphi_EB', xtitle='superCluster full5x5 sigmaIetaIphi EB', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_full5x5_sigmaIphiIphi_EB', xtitle='superCluster full5x5 sigmaIphiIphi EB', ytitle='Entries', xrange=None)



        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_energy_EB', xtitle='caloMatched superCluster energy EB [GeV]', ytitle='Entries', xrange=None)    
        
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_eta_EB', xtitle='caloMatched superCluster eta EB', ytitle='Entries', xrange=(-4.,4.))

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_phi_EB', xtitle='caloMatched superCluster phi EB', ytitle='Entries', xrange=(-3.2,3.2))

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_r9_EB', xtitle='caloMatched superCluster r9 EB', ytitle='Entries', xrange=(0.,1.5))
       
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_sigmaIetaIeta_EB', xtitle='caloMatched superCluster sigmaIetaIeta EB', ytitle='Entries', xrange=None)
       
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_sigmaIetaIphi_EB', xtitle='caloMatched superCluster sigmaIetaIphi EB', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_sigmaIphiIphi_EB', xtitle='caloMatched superCluster sigmaIphiIphi EB', ytitle='Entries', xrange=None)

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_full5x5_r9_EB', xtitle='caloMatched superCluster full5x5 r9 EB', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_full5x5_sigmaIetaIeta_EB', xtitle='caloMatched superCluster full5x5 sigmaIetaIeta EB', ytitle='Entries', xrange=None)
       
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_full5x5_sigmaIetaIphi_EB', xtitle='caloMatched superCluster full5x5 sigmaIetaIphi EB', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_full5x5_sigmaIphiIphi_EB', xtitle='caloMatched superCluster full5x5 sigmaIphiIphi EB', ytitle='Entries', xrange=None)


   if options.doEE:

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_energy_EE', xtitle='caloMatched PFCluster energy [GeV]', ytitle='Entries', xrange=None)    

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_size_EE', xtitle='number of caloMatched PFClusters per event', ytitle='Entries', xrange=(0.,10.))

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_nRecHit_EE', xtitle='number of crystals per caloMatched PFCluster', ytitle='Entries', xrange=(0.,40.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_nXtals_EE', xtitle='number of crystals per caloParticle', ytitle='Entries', xrange=(0.,45.))

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_et_EE', xtitle='caloMatched PFCluster ET [GeV]', ytitle='Entries', xrange=None)
        
        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_eta_EE', xtitle='caloMatched PFCluster eta', ytitle='Entries', xrange=(-4.,4.))

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_phi_EE', xtitle='caloMatched PFCluster phi', ytitle='Entries', xrange=(-3.2,3.2))

        beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_eOverEtrue_EE', xtitle='inclusive E/Etrue', ytitle='Entries', xrange=(0.,1.5))
        
        

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEM_energy', xtitle='EEM caloMatched PFCluster energy [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEM_size', xtitle='EEM number of caloMatched PFClusters per event', ytitle='Entries', xrange=(0.,10.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEM_nXtals', xtitle='EEM number of crystals per caloParticle', ytitle='Entries', xrange=(0.,45.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEM_et', xtitle='EEM caloMatched PFCluster ET [GeV]', ytitle='Entries', xrange=None)
        
        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEM_eta', xtitle='EEM caloMatched PFCluster eta', ytitle='Entries', xrange=(-4.,4.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEM_phi', xtitle='EEM caloMatched PFCluster phi', ytitle='Entries', xrange=(-3.2,3.2))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEM_eOverEtrue', xtitle='EEM E/Etrue', ytitle='Entries', xrange=(0.,1.5))
       


        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEP_energy', xtitle='EBP caloMatched PFCluster energy [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEP_size', xtitle='EBP number of caloMatched PFClusters per event', ytitle='Entries', xrange=(0.,10.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEP_nXtals', xtitle='EBP number of crystals per caloParticle', ytitle='Entries', xrange=(0.,45.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEP_et', xtitle='EBP caloMatched PFCluster ET [GeV]', ytitle='Entries', xrange=None)
        
        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEP_eta', xtitle='EBP caloMatched PFCluster eta', ytitle='Entries', xrange=(-4.,4.))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEP_phi', xtitle='EBP caloMatched PFCluster phi', ytitle='Entries', xrange=(-3.2,3.2))

        #beautify1DPlot(outputdir=outputdir_pfCluster, inputfile=inputfile, inputdir='PFCluster_caloMatched', histoname='h_PFClusters_caloMatched_EEP_eOverEtrue', xtitle='EBP E/Etrue', ytitle='Entries', xrange=(0.,1.5))
       




        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_genEnergy_EE', xtitle='caloParticle energy [GeV]', ytitle='Entries', xrange=None)    

        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_simEnergy_EE', xtitle='caloParticle energy (sim) [GeV]', ytitle='Entries', xrange=None)    

        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_size_EE', xtitle='number of caloParticle per event', ytitle='Entries', xrange=(0.,11.))

        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_et_EE', xtitle='caloParticle ET [GeV]', ytitle='Entries', xrange=None)
        
        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_genEta_EE', xtitle='caloParticl eta', ytitle='Entries', xrange=(-4.,4.))

        beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_genPhi_EE', xtitle='caloParticle phi', ytitle='Entries', xrange=(-3.2,3.2))



        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEM_energy', xtitle='EEM caloParticle energy [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEM_simEnergy', xtitle='EEM caloParticle energy (sim) [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEM_size', xtitle='EEM number of caloParticle per event', ytitle='Entries', xrange=(0.,10.))

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEM_et', xtitle='EEM caloParticle ET [GeV]', ytitle='Entries', xrange=None)
        
        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEM_eta', xtitle='EEM caloParticle eta', ytitle='Entries', xrange=(-4.,4.))

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEM_phi', xtitle='EEM caloParticle phi', ytitle='Entries', xrange=(-3.2,3.2))


        

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEP_energy', xtitle='EBP caloParticle energy [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEP_simEnergy', xtitle='EBP caloParticle energy (sim) [GeV]', ytitle='Entries', xrange=None)    

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEP_size', xtitle='EBP number of caloParticle per event', ytitle='Entries', xrange=(0.,10.))

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEP_et', xtitle='EBP caloParticle ET [GeV]', ytitle='Entries', xrange=None)
        
        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEP_eta', xtitle='EBP caloParticle eta', ytitle='Entries', xrange=(-4.,4.))

        #beautify1DPlot(outputdir=outputdir_caloParticle, inputfile=inputfile, inputdir='caloParticle', histoname='h_caloParticle_EEP_phi', xtitle='EBP caloParticle phi', ytitle='Entries', xrange=(-3.2,3.2))
       

       
        #superCluster
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_energy_EE', xtitle='superCluster energy EE [GeV]', ytitle='Entries', xrange=None)    

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_eta_EE', xtitle='superCluster eta EE', ytitle='Entries', xrange=(-4.,4.))

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_phi_EE', xtitle='superCluster phi EE', ytitle='Entries', xrange=(-3.2,3.2))

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_r9_EE', xtitle='superCluster r9 EE', ytitle='Entries', xrange=(0.,1.5))
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_sigmaIetaIeta_EE', xtitle='superCluster sigmaIetaIeta EE', ytitle='Entries', xrange=None)
       
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_sigmaIetaIphi_EE', xtitle='superCluster sigmaIetaIphi EE', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_sigmaIphiIphi_EE', xtitle='superCluster sigmaIphiIphi EE', ytitle='Entries', xrange=None)

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_full5x5_r9_EE', xtitle='superCluster full5x5 r9 EE', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_full5x5_sigmaIetaIeta_EE', xtitle='superCluster full5x5 sigmaIetaIeta EE', ytitle='Entries', xrange=None)
       
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_full5x5_sigmaIetaIphi_EE', xtitle='superCluster full5x5 sigmaIetaIphi EE', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_full5x5_sigmaIphiIphi_EE', xtitle='superCluster full5x5 sigmaIphiIphi EE', ytitle='Entries', xrange=None)




        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_energy_EE', xtitle='caloMatched superCluster energy EE [GeV]', ytitle='Entries', xrange=None)    
        
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_eta_EE', xtitle='caloMatched superCluster eta EE', ytitle='Entries', xrange=(-4.,4.))

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_phi_EE', xtitle='caloMatched superCluster phi EE', ytitle='Entries', xrange=(-3.2,3.2))

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_r9_EE', xtitle='caloMatched superCluster r9 EE', ytitle='Entries', xrange=(0.,1.5))
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_sigmaIetaIeta_EE', xtitle='caloMatched superCluster sigmaIetaIeta EE', ytitle='Entries', xrange=None)
       
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_sigmaIetaIphi_EE', xtitle='caloMatched superCluster sigmaIetaIphi EE', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_sigmaIphiIphi_EE', xtitle='caloMatched superCluster sigmaIphiIphi EE', ytitle='Entries', xrange=None)

        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_full5x5_r9_EE', xtitle='caloMatched superCluster full5x5 r9 EE', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_full5x5_sigmaIetaIeta_EE', xtitle='caloMatched superCluster full5x5 sigmaIetaIeta EE', ytitle='Entries', xrange=None)
       
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_full5x5_sigmaIetaIphi_EE', xtitle='caloMatched superCluster full5x5 sigmaIetaIphi EE', ytitle='Entries', xrange=None)
 
        beautify1DPlot(outputdir=outputdir_superCluster, inputfile=inputfile, inputdir='SuperCluster', histoname='h_superCluster_caloMatched_full5x5_sigmaIphiIphi_EE', xtitle='caloMatched superCluster full5x5 sigmaIphiIphi EE', ytitle='Entries', xrange=None)







