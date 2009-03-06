import FWCore.ParameterSet.Config as cms

process = cms.Process("myprocess")
process.load("CondCore.DBCommon.CondDBCommon_cfi")

process.CondDBCommon.connect = 'sqlite_file:PhysicsPerformance.db'


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDBCommon,
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('pippo3'),
        tag = cms.string('TEST_TABLE_2'),
        label = cms.string('TEST_TABLE_2')
    ),
cms.PSet(
        record = cms.string('pippo4'),
        tag = cms.string('TEST_TABLE_2_WP'),
        label = cms.string('TEST_TABLE_2_WP')
        ))
)


process.mywriter = cms.EDFilter("PhysicsPerformanceDBWriterFromFile_WPandPayload",
                                inputTxtFile = cms.untracked.string('tableinput_ALL2_phi.txt'),
                                RecordPayload = cms.untracked.string('pippo3'),
                                RecordWP = cms.untracked.string('pippo4')
                                )



process.p = cms.Path(process.mywriter)


