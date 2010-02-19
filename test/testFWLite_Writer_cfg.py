import FWCore.ParameterSet.Config as cms

process = cms.Process("myprocess")
process.load("CondCore.DBCommon.CondDBCommon_cfi")

process.CondDBCommon.connect = 'sqlite_file:PhysicsPerformance.db'

process.load ("RecoBTag.PerformanceDB.BtagPerformanceESProducer_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.TFileService = cms.Service("TFileService", fileName = cms.string("TrackCountingHigheffBlah.root") )

process.PoolDBESSource = cms.ESSource("PoolDBESSource",
                                      process.CondDBCommon,
                                      toGet = cms.VPSet(
    cms.PSet(
    record = cms.string('PerformanceWPRecord'),
    tag = cms.string('TEST_TABLE_1_WP'),
    label = cms.untracked.string('TEST_TABLE_1_WP')
    ),
                                                        cms.PSet(
    record = cms.string('PerformancePayloadRecord'),
    tag = cms.string('TEST_TABLE_1'),
    label = cms.untracked.string('TEST_TABLE_1')
    ))

)


process.myrootwriter = cms.EDAnalyzer("BTagPerformaceRootProducerFromSQLITE",
                                  name = cms.string('TrackCountingHigheffBlah'),
                                  index = cms.uint32(1001)
                                  )

#
# change inside the source
#
process.BtagPerformanceESProducer_test.ComponentName = "TrackCountingHigheffBlah"
process.BtagPerformanceESProducer_test.PayloadName = "TEST_TABLE_1"
process.BtagPerformanceESProducer_test.WorkingPointName = "TEST_TABLE_1_WP"

process.p = cms.Path(process.myrootwriter)
