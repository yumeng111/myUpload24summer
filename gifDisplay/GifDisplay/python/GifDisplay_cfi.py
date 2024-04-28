import FWCore.ParameterSet.Config as cms

GifDisplay = cms.EDAnalyzer('GifDisplay',
#rootFileName = cms.untracked.string("output_me11_test27_oct30.root"),
rootFileName = cms.untracked.string("output.root"),

stripDigiTagSrc = cms.untracked.InputTag("muonCSCDigis","MuonCSCStripDigi"),
wireDigiTagSrc = cms.untracked.InputTag("muonCSCDigis","MuonCSCWireDigi"),
compDigiTagSrc = cms.untracked.InputTag("muonCSCDigis", "MuonCSCComparatorDigi"),
cscRecHitTag = cms.InputTag("csc2DRecHits",""),
alctDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCALCTDigi'),
clctDigiTagSrc = cms.untracked.InputTag('muonCSCDigis', 'MuonCSCCLCTDigi'),
corrlctDigiTag = cms.InputTag('muonCSCDigis', 'MuonCSCCorrelatedLCTDigi'),

#directory for eventdisplay
eventDisplayDir = cms.untracked.string("displayplots/"),
#eventDisplayDir = cms.untracked.string("/home/mhl/public_html/2017/20171201_cscSeg/"),
#chamber type: ME1/1-11, ME2/1-21
chamberType = cms.untracked.string('21')
)


