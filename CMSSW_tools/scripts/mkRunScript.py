#!/usr/bin/env python
import argparse
import os


parser = argparse.ArgumentParser()
####Set options###                                                                                                                             
parser.add_argument("--tag", help="name of this job")
parser.add_argument("--fragment", help="fragment file")
parser.add_argument("--nevent", help="# of events for this job")
parser.add_argument("--gridpack", help="gridpack path for this job")
parser.add_argument("--seed", help="seed number")


args = parser.parse_args()

if args.fragment:
    fragment=args.fragment
else:
    print "need --fragment option"
    exit()
if args.nevent:
    nevent=args.nevent
else:
    print "need --nevent option"
    exit()

if args.seed:
    seed=args.seed
else:
    print "need --seed option"
    exit()

if args.tag:
    tag=args.tag
else:
    print "need --tag option"
    exit()

if args.gridpack:
    gridpack=args.gridpack
else:
    print "need --gridpack option"
    exit()

os.system('mkdir -p '+'JOBDIR__'+tag+'__'+nevent+'evt/')
os.chdir('JOBDIR__'+tag+'__'+nevent+'evt/')
f=open('run_'+tag+'__'+seed+'__'+nevent+'evt_cfg.sh','w')
if os.getenv('CMSSW_BASE'):
    CMSSW_BASE=os.getenv('CMSSW_BASE')
else: exit()
f_userconfig=open(CMSSW_BASE+'/src/Gen_validation/CMSSW_tools/scripts/user_config.py')
exec(f_userconfig)
f_userconfig.close()
'''
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
export X509_USER_PROXY=/cms/ldap_home/jhchoi/.proxy
voms-proxy-info
export SCRAM_ARCH=slc7_amd64_gcc700
source $VO_CMS_SW_DIR/cmsset_default.sh

'''
f.write('#!/bin/bash\n')
f.write('StartTime=$(date +%s)\n')
f.write('export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n')
f.write('export SCRAM_ARCH='+os.getenv('SCRAM_ARCH')+'\n')
f.write('source $VO_CMS_SW_DIR/cmsset_default.sh\n')
#f.write('cd '+CMSSW_BASE+'/src\n')
f.write('echo "==Extract Tarball=="\n')
f.write('tar -xf INPUT__submit__run_'+tag+'__'+seed+'__'+nevent+'evt_cfg.tar.gz\n')
f.write('cd CMSSW'+CMSSW_BASE.split('CMSSW')[-1]+'/src\n'   )
f.write('scram build ProjectRename\n')
f.write('eval `scramv1 runtime -sh`\n')
f.write('cd ../../\n')
#f.write('cd '+MYWORKDIR+'\n')
#f.write('mkdir -p JOBDIR__'+tag+'__'+nevent+'evt/\n')
#f.write('cd JOBDIR__'+tag+'__'+nevent+'evt/\n')
f.write('make_fragment.py --fragment '+fragment+' --nevent '+nevent+' --seed '+seed+' --tag '+tag+' --gridpack '+gridpack+'\n')
#f.write('mkdir -p WORKDIR__'+tag+'__'+seed+'__'+nevent+'evt\n')
#f.write('cd WORKDIR__'+tag+'__'+seed+'__'+nevent+'evt\n')
#f.write('cmsRun '+'../run_'+tag+'__'+seed+'__'+nevent+'evt_cfg.py\n')
f.write('cmsRun '+'run_'+tag+'__'+seed+'__'+nevent+'evt_cfg.py\n')
#f.write('cd '+MYWORKDIR+'\n')
#f.write('mv JOBDIR__'+tag+'__'+nevent+'evt/WORKDIR__'+tag+'__'+seed+'__'+nevent+'evt /xrootd/store/user/jhchoi/Generator_group/validation_GEN/\n' )
f.write('EndTime=$(date +%s)\n')
f.write('echo "runtime : $(($EndTime - $StartTime)) sec"\n')
f.write('echo "@@JOB FINISHED@@"\n')
#f.write('mv *.root '+MYWORKDIR+'/JOBDIR__'+tag+'__'+nevent+'evt/\n')
f.write('xrdfs '+XROOTD_ADDRESS+' mkdir '+MYSTORAGEPATH+'/OUTPUTS__'+tag+'__'+nevent+'\n')
f.write('xrdcp *.root '+XROOTD_ADDRESS+'/'+MYSTORAGEPATH+'/OUTPUTS__'+tag+'__'+nevent+'/\n')
f.close()


os.system('chmod u+x '+'run_'+tag+'__'+seed+'__'+nevent+'evt_cfg.sh')
