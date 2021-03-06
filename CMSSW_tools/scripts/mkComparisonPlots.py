#!/usr/bin/env python                                                                                                                                                            

import os

CMSSW_BASE = os.getenv('CMSSW_BASE')


#--Load Configurations


f_userconfig=open(CMSSW_BASE+'/src/Gen_validation/CMSSW_tools/scripts/user_config.py')
exec(f_userconfig)
f_userconfig.close()


f_HistoConfigForReweight=open(CMSSW_BASE+'/src/Gen_validation/CMSSW_tools/scripts/HistoConfigForReweight.py')
exec(f_HistoConfigForReweight)
f_HistoConfigForReweight.close()


f_PlotConfigForReweight=open(CMSSW_BASE+'/src/Gen_validation/CMSSW_tools/scripts/PlotConfigForReweight.py')
exec(f_PlotConfigForReweight)
f_PlotConfigForReweight.close()

#-test
#os.system('runComparisonPlot.py --deno_config mg260LO --deno_proc dyellell01234j_5f_LO_MLM --nume_config mg261LO --nume_proc dyellell01234j_5f_LO_MLM --x Zmuon_pt --var muRmuF_default --yaxis_ratio mg261/mg260 --yaxis "#Events" --title muRmuF_default --dirname test --deno_alias MG260 --nume_alias MG261')

##--Compare MG261,265/MG260



dyellell01234j_5f_LO_MLM__261_over_260={
    'title':'DY01234j_LO_261_over_260',
    'deno':{'config':'mg260LO','process':'dyellell01234j_5f_LO_MLM','alias':'MG260'},
    'nume':{'config':'mg261LO', 'process':'dyellell01234j_5f_LO_MLM','alias':'MG261' }
}
dyellell01234j_5f_LO_MLM__265_over_260={
    'title':'DY01234j_LO_265_over_260',
    'deno':{'config':'mg260LO','process':'dyellell01234j_5f_LO_MLM','alias':'MG260'},
    'nume':{'config':'mg265LO', 'process':'dyellell01234j_5f_LO_MLM','alias':'MG265' }
}
dyellell01234j_5f_LO_MLM__265_over_261={
    'title':'DY01234j_LO_265_over_261',
    'deno':{'config':'mg261LO','process':'dyellell01234j_5f_LO_MLM','alias':'MG261'},
    'nume':{'config':'mg265LO', 'process':'dyellell01234j_5f_LO_MLM','alias':'MG265' }
}


dyellell01234j_5f_LO_MLM_pdfwgt_T__265_over_261={
    'title':'DY01234j_LO__True_pdfwgt__265_over_261',
    'deno':{'config':'mg261LO','process':'dyellell01234j_5f_LO_MLM_pdfwgt_T','alias':'MG261'},
    'nume':{'config':'mg265LO', 'process':'dyellell01234j_5f_LO_MLM_pdfwgt_T','alias':'MG265' }
}
dyellell01234j_5f_LO_MLM_pdfwgt_T__261_over_260={
    'title':'DY01234j_LO__True_pdfwgt__261_over_260',
    'deno':{'config':'mg260LO','process':'dyellell01234j_5f_LO_MLM_pdfwgt_T','alias':'MG260'},
    'nume':{'config':'mg261LO', 'process':'dyellell01234j_5f_LO_MLM_pdfwgt_T','alias':'MG261' } 
}
dyellell01234j_5f_LO_MLM_pdfwgt_T__265_over_260={
    'title':'DY01234j_LO__True_pdfwgt__265_over_260',
    'deno':{'config':'mg260LO','process':'dyellell01234j_5f_LO_MLM_pdfwgt_T','alias':'MG260'},
    'nume':{'config':'mg265LO', 'process':'dyellell01234j_5f_LO_MLM_pdfwgt_T','alias':'MG265' }
}

#dyellell012j_5f_NLO_FXFX
dyellell012j_5f_NLO_FXFX__261_over_260={
    'title':'DY012j_NLO__261_over_260',
    'deno':{'config':'mg260NLO','process':'dyellell012j_5f_NLO_FXFX','alias':'MG260'},
    'nume':{'config':'mg261NLO', 'process':'dyellell012j_5f_NLO_FXFX','alias':'MG261' }
}
dyellell012j_5f_NLO_FXFX__265_over_260={
    'title':'DY012j_NLO__265_over_260',
    'deno':{'config':'mg260NLO','process':'dyellell012j_5f_NLO_FXFX','alias':'MG260'},
    'nume':{'config':'mg265NLO', 'process':'dyellell012j_5f_NLO_FXFX','alias':'MG265' } 
}
dyellell012j_5f_NLO_FXFX__265_over_261={
    'title':'DY012j_NLO__265_over_261',
    'deno':{'config':'mg261NLO','process':'dyellell012j_5f_NLO_FXFX','alias':'MG261'},
    'nume':{'config':'mg265NLO', 'process':'dyellell012j_5f_NLO_FXFX','alias':'MG265' }
}



#--pdfwgt T/F
#----mg260
mg260__dyellell01234j_5f_LO_MLM__pdfwgt__T_over_F={
    'title':'MG260__DY01234j_LO__pdfwgt__T_over_F',
    'deno':{'config':'mg260LO','process':'dyellell01234j_5f_LO_MLM','alias':'pdfwgt_F'},
    'nume':{'config':'mg260LO', 'process':'dyellell01234j_5f_LO_MLM_pdfwgt_T','alias':'pdfwgt_T' }
}
#---mg261
mg261__dyellell01234j_5f_LO_MLM__pdfwgt__T_over_F={
    'title':'MG261__DY01234j_LO__pdfwgt__T_over_F',
    'deno':{'config':'mg261LO','process':'dyellell01234j_5f_LO_MLM','alias':'pdfwgt_F'},
    'nume':{'config':'mg261LO', 'process':'dyellell01234j_5f_LO_MLM_pdfwgt_T','alias':'pdfwgt_T' }
}
#---mg265
mg265__dyellell01234j_5f_LO_MLM__pdfwgt__T_over_F={
    'title':'MG265__DY01234j_LO__pdfwgt__T_over_F',
    'deno':{'config':'mg265LO','process':'dyellell01234j_5f_LO_MLM','alias':'pdfwgt_F'},
    'nume':{'config':'mg265LO', 'process':'dyellell01234j_5f_LO_MLM_pdfwgt_T','alias':'pdfwgt_T' }
}




mg260test__dyellell012j_5f_NLO_FXFX={
    'title':'MG260__DY012j_NLO_test_diff_seed',
    'deno':{'config':'mg260NLO_1','process':'dyellell012j_5f_NLO_FXFX','alias':'seed1'},
    'nume':{'config':'mg260NLO_2', 'process':'dyellell012j_5f_NLO_FXFX','alias':'seed2' }
}



ToRun=[

#dyellell01234j_5f_LO_MLM__261_over_260,
#dyellell01234j_5f_LO_MLM__265_over_260,
#dyellell01234j_5f_LO_MLM__265_over_261,

#dyellell01234j_5f_LO_MLM_pdfwgt_T__261_over_260,
#dyellell01234j_5f_LO_MLM_pdfwgt_T__265_over_260,
#dyellell01234j_5f_LO_MLM_pdfwgt_T__265_over_261,

#dyellell012j_5f_NLO_FXFX__261_over_260,
#dyellell012j_5f_NLO_FXFX__265_over_260,
#dyellell012j_5f_NLO_FXFX__265_over_261,

mg260__dyellell01234j_5f_LO_MLM__pdfwgt__T_over_F,
mg261__dyellell01234j_5f_LO_MLM__pdfwgt__T_over_F,
mg265__dyellell01234j_5f_LO_MLM__pdfwgt__T_over_F,

]


#for nume_config in list_nume_config:
for dic in ToRun:
    print '=================[deno]',dic['deno'],'====================='
    print '=================[nume]',dic['nume'],'====================='
    deno_config = dic['deno']['config']
    nume_config = dic['nume']['config']

    deno_proc = dic['deno']['process']
    nume_proc = dic['nume']['process']

    deno_alias = dic['deno']['alias']
    nume_alias = dic['nume']['alias']
    #for proc in rwgt_info[deno_config]['process']:
    #    print '[denominator]',deno_config,'[numerator]',nume_config,'[proc]',proc
    for x in HistoConfig:
        jobname=nume_config+'_'+nume_proc+'_over_'+deno_config+'_'+deno_proc+'__'+x
        os.chdir(MYWORKDIR)
        os.system('mkdir -p '+'JOBDIR__'+jobname)
        os.chdir('JOBDIR__'+jobname)
        f=open(jobname+'.sh','w')
        if os.getenv('CMSSW_BASE'):
            CMSSW_BASE=os.getenv('CMSSW_BASE')
        else: exit()
        f.write('#!/bin/bash\n')
        f.write('StartTime=$(date +%s)\n')
        f.write('export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n')
        f.write('export SCRAM_ARCH='+os.getenv('SCRAM_ARCH')+'\n')
        f.write('source $VO_CMS_SW_DIR/cmsset_default.sh\n')
        f.write('echo "==Extract Tarball=="\n')
        f.write('tar -xf INPUT__submit__'+jobname+'.tar.gz\n')
        f.write('cd CMSSW'+CMSSW_BASE.split('CMSSW')[-1]+'/src\n'   )
        f.write('scram build ProjectRename\n')
        f.write('eval `scramv1 runtime -sh`\n')
        f.write('cd ../../\n')
        for variation in rwgt_info[deno_config]['variation']:
            command='runComparisonPlot.py --deno_config "'+deno_config+'" --deno_proc "'+deno_proc+'" --nume_config "'+nume_config+'" --nume_proc "'+nume_proc+'" --x "'+x+'" --var "'+variation+'" --yaxis_ratio "'+nume_alias+'/'+deno_alias+'" --yaxis "Normalized Nevents" --title "'+rwgt_info[deno_config]['variation'][variation]['name']+'__'+dic['title']+'" --dirname "'+nume_config+'__'+nume_proc+'__over__'+deno_config+'__'+deno_proc+'" --deno_alias "'+deno_alias+'" --nume_alias "'+nume_alias+'"'+' --test_stat Chi2Test'
            f.write(command+'\n')
            command='runComparisonPlot.py --deno_config "'+deno_config+'" --deno_proc "'+deno_proc+'" --nume_config "'+nume_config+'" --nume_proc "'+nume_proc+'" --x "'+x+'" --var "'+variation+'" --yaxis_ratio "'+nume_alias+'/'+deno_alias+'" --yaxis "Normalized Nevents" --title "'+rwgt_info[deno_config]['variation'][variation]['name']+'__'+dic['title']+'" --dirname "'+nume_config+'__'+nume_proc+'__over__'+deno_config+'__'+deno_proc+'" --deno_alias "'+deno_alias+'" --nume_alias "'+nume_alias+'"'+' --test_stat KolmogorovTest'
            f.write(command+'\n')
        f.write('EndTime=$(date +%s)\n')
        f.write('echo "runtime : $(($EndTime - $StartTime)) sec"\n')
        f.write('echo "@@JOB FINISHED@@"\n')
        f.close()
        os.system('chmod u+x '+jobname+'.sh')
        os.system('mkBatch.py --exe '+jobname+'.sh')
        #name='submit__'+''.join(exe.split('.sh')[:-1])
        command='condor_submit submit__'+jobname+'.jds > submit__'+jobname+'.jid'
        print "[JOB Submitted]"+command 
        os.system(command)
      

        

        
            


        
