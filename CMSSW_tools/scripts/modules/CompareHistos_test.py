import ROOT
import math
import os

ROOT.gROOT.SetBatch(ROOT.kTRUE)


#ROOT.TGraphAsymmErrors

##--No Graphical Window

#ROOT.gROOT.SetBatch(ROOT.kTRUE)




def Ratio(A,B):


    if B==0.:
        return 0.
    else:
        return A/B
#        CompareTGraphAsymmErrorsWithStat(xaxis,yaxis,yaxis_ratio,title,h1,h1stat,label1,color1,h0,h0stat,label0,color0,store_filepath,True)





def CompareTGraphAsymmErrorsWithStat(xaxis,yaxis,yaxis_ratio,title,h1,h1stat,label1,color1,h2,h2stat,label2,color2,store_file_path,do_norm=True):



    nbin=h1.GetN()

    prefix='jhchoi'
    print prefix
    print '[xaxis]',xaxis,' [title]',title,' label1',label1,' label2',label2
    h1__total=h1.Clone(label1+'__total')
    h2__total=h2.Clone(label2+'__total')

    tgr_h1_over_h2=h1.Clone(prefix+'__'+label1+"_over_"+label2)
    tgr_h2_over_h2=h2.Clone(prefix+'__'+label2)    

    tgr_h1stat_over_h2stat=h1stat.Clone(prefix+'__'+label1+"_over_"+label2+'__stat')
    tgr_h2stat_over_h2stat=h2stat.Clone(prefix+'__'+label2+'__stat')

    tgr_h1_over_h2__total=h1stat.Clone(prefix+'__'+label1+"_over_"+label2+'__total')
    tgr_h2_over_h2__total=h2stat.Clone(prefix+'__'+label2+'__total')

    ##compare percentage err##
    tgr_syserr1=ROOT.TGraphAsymmErrors(nbin)
    tgr_syserr2=ROOT.TGraphAsymmErrors(nbin)



    #print "nbin=",nbin


    y1sum=sum(h1.GetY())
    y2sum=sum(h2.GetY())

    if do_norm:
        norm1=1
        norm2=y2sum/y1sum
    else:
        norm1=1
        norm2=1
    print 'norm1=',norm1
    print 'norm2=',norm2

    ymax  =max(h1.GetY())/norm1
    ymin  =max(h1.GetY())/norm1

    syserrmax=0
    #print 'ymax',ymax

    for iBin in range(0,nbin):


        x1=h1.GetX()[iBin]
        ex1_up=h1.GetErrorXhigh(iBin)
        ex1_dn=h1.GetErrorXlow(iBin)

        x2=h2.GetX()[iBin]
        ex2_up=h2.GetErrorXhigh(iBin)
        ex2_dn=h2.GetErrorXlow(iBin)


        y1=h1.GetY()[iBin]/norm1
        #print y1
        ey1_up=h1.GetErrorYhigh(iBin)/norm1
        ey1_dn=h1.GetErrorYlow(iBin)/norm1
        #print ey1_dn
        y2=h2.GetY()[iBin]/norm2
        ey2_up=h2.GetErrorYhigh(iBin)/norm2
        ey2_dn=h2.GetErrorYlow(iBin)/norm2



        x1_stat=h1stat.GetX()[iBin]
        ex1_stat_up=h1stat.GetErrorXhigh(iBin)
        ex1_stat_dn=h1stat.GetErrorXlow(iBin)

        x2_stat=h2stat.GetX()[iBin]
        ex2_stat_up=h2stat.GetErrorXhigh(iBin)
        ex2_stat_dn=h2stat.GetErrorXlow(iBin)

        y1_stat=h1stat.GetY()[iBin]/norm1
        ey1_stat_up=h1stat.GetErrorYhigh(iBin)/norm1
        ey1_stat_dn=h1stat.GetErrorYlow(iBin)/norm1

        y2_stat=h2stat.GetY()[iBin]/norm2
        ey2_stat_up=h2stat.GetErrorYhigh(iBin)/norm2
        ey2_stat_dn=h2stat.GetErrorYlow(iBin)/norm2

        if y1!=y1_stat:
            print "y1!=y1_stat"
        if y2!=y2_stat:
            print "y2!=y2_stat"

        x1_total=x1
        x2_total=x2
        ex1_total_dn=ex1_dn
        ex1_total_up=ex1_up

        ex2_total_up=ex2_up
        ex2_total_dn=ex2_dn
        
        y1_total=y1
        y2_total=y2

        
        ey1_total_up= math.sqrt(ey1_up**2 + ey1_stat_up**2)
        ey1_total_dn= math.sqrt(ey1_dn**2 + ey1_stat_dn**2)

        ey2_total_up= math.sqrt(ey2_up**2 + ey2_stat_up**2)
        ey2_total_dn= math.sqrt(ey2_dn**2 + ey2_stat_dn**2)

        #print "ey1_stat_up=",ey1_stat_up
        if y1 > ymax : ymax=y1
        if y2 > ymax : ymax=y2
        if y1 < ymin and y1!=0 : ymin=y1
        if y2 < ymin and y2!=0 : ymin=y2
        

        h1__total.SetPoint(iBin,x1,y1_total)
        h2__total.SetPoint(iBin,x2,y2_total)
        h1__total.SetPointError(iBin, ex1_total_dn,ex1_total_up, ey1_total_dn, ey1_total_up  )
        h2__total.SetPointError(iBin, ex2_total_dn,ex2_total_up, ey2_total_dn, ey2_total_up  )

        h1.SetPoint(iBin,x1,y1)
        h2.SetPoint(iBin,x2,y2)
        h1.SetPointError(iBin, ex1_dn,ex1_up, ey1_dn, ey1_up  )
        h2.SetPointError(iBin, ex2_dn,ex2_up, ey2_dn, ey2_up  )

        h1stat.SetPoint(iBin,x1,y1)
        h2stat.SetPoint(iBin,x2,y2)
        h1stat.SetPointError(iBin, ex1_stat_dn,ex1_stat_up, ey1_stat_dn, ey1_stat_up  )
        h2stat.SetPointError(iBin, ex2_stat_dn,ex2_stat_up, ey2_stat_dn, ey2_stat_up  )



        tgr_h1_over_h2__total.SetPoint(iBin, x1, Ratio(y1,y2))
        tgr_h1_over_h2__total.SetPointError(iBin, ex1_dn,ex1_up, Ratio(ey1_total_dn,y2), Ratio(ey1_total_up,y2 )   )

        tgr_h2_over_h2__total.SetPoint(iBin, x1, 1  )
        tgr_h2_over_h2__total.SetPointError(iBin, ex1_dn,ex1_up, Ratio(ey2_total_dn,y2), Ratio(ey2_total_up,y2 )   )

        tgr_h1_over_h2.SetPoint(iBin,  x1,  Ratio(y1,y2)  ) #(i,x,y)
        tgr_h1_over_h2.SetPointError(iBin,ex1_dn,ex1_up,Ratio(ey1_dn,y2), Ratio(ey1_up,y2)) #(i,ex_down,ex_up,ey_down,ey_up)

        tgr_h2_over_h2.SetPoint(iBin, x2 ,1) #(i,x,y)
        tgr_h2_over_h2.SetPointError(iBin,ex2_dn,ex2_up,Ratio(ey2_dn,y2), Ratio(ey2_up,y2)) #(i,ex_down,ex_up,ey_down,ey_up)


        tgr_h1stat_over_h2stat.SetPoint(iBin,x1,Ratio(y1,y2)) #(i,x,y)
        tgr_h1stat_over_h2stat.SetPointError(iBin,ex1_stat_dn,ex1_stat_up,Ratio(ey1_stat_dn,y2_stat), Ratio(ey1_stat_up,y2_stat)) #(i,ex_down,ex_up,ey_down,ey_up)

        tgr_h2stat_over_h2stat.SetPoint(iBin,x2_stat,1) #(i,x,y)
        tgr_h2stat_over_h2stat.SetPointError(iBin,ex2_stat_dn,ex2_stat_up,Ratio(ey2_stat_dn,y2_stat), Ratio(ey2_stat_up,y2_stat)) #(i,ex_down,ex_up,ey_down,ey_up)

        ##--percent err(%)
        tgr_syserr1.SetPoint(iBin,x1,0)
        tgr_syserr1.SetPointError(iBin,ex1_dn,ex1_up,Ratio(ey1_dn,y1)*100,Ratio(ey1_up,y1)*100   )

        tgr_syserr2.SetPoint(iBin,x2,0)
        tgr_syserr2.SetPointError(iBin,ex2_dn,ex2_up,Ratio(ey2_dn,y2)*100,Ratio(ey2_up,y2)*100   )

        if Ratio(ey2_dn,y2)*100>syserrmax :
            syserrmax=Ratio(ey2_dn,y2)*100
        if Ratio(ey2_up,y2)*100>syserrmax:
            syserrmax=Ratio(ey2_up,y2)*100
        if Ratio(ey1_dn,y1)*100>syserrmax :
            syserrmax=Ratio(ey1_dn,y1)*100
        if Ratio(ey1_up,y1)*100>syserrmax:
            syserrmax=Ratio(ey1_up,y1)*100





        ##


    #--Set Color--#
    
    h1.SetLineColor(color1)
    h1.SetFillColorAlpha(color1,0.5)
    h1stat.SetLineColor(color1)
    tgr_syserr1.SetFillColorAlpha(color1,0.5)

    h1stat.SetFillColor(0)
    h1__total.SetLineColor(color1)
    h1__total.SetFillColorAlpha(color1,0.5)
    

    
    


    tgr_h1_over_h2.SetLineColor(color1)
    tgr_h1_over_h2.SetFillColorAlpha(color1,0.5)
    tgr_h1stat_over_h2stat.SetLineColor(color1)
    tgr_h1stat_over_h2stat.SetFillColor(0)
    tgr_h1_over_h2__total.SetLineColor(color1)
    tgr_h1_over_h2__total.SetFillColorAlpha(color1,0.5)


    h2.SetLineColor(color2)
    h2.SetFillColorAlpha(color2,0.5)
    h2stat.SetLineColor(color2)
    tgr_syserr2.SetFillColorAlpha(color2,0.5)
    
    h2stat.SetFillColor(0)
    h2__total.SetLineColor(color2)
    h2__total.SetFillColorAlpha(color2,0.5)


    tgr_h2_over_h2.SetLineColor(color2)
    tgr_h2_over_h2.SetFillColorAlpha(color2,0.5)
    tgr_h2stat_over_h2stat.SetLineColor(color2)
    tgr_h2stat_over_h2stat.SetFillColor(0)
    tgr_h2_over_h2__total.SetLineColor(color2)
    tgr_h2_over_h2__total.SetFillColorAlpha(color2,0.5)
    

    #--SetFillStyle for stat--
    h1.SetFillStyle(3001)
    h2.SetFillStyle(3001)
    tgr_syserr1.SetFillStyle(3001)
    tgr_syserr2.SetFillStyle(3001)

    h1__total.SetFillStyle(3004)
    h2__total.SetFillStyle(3004)

    tgr_h1_over_h2.SetFillStyle(3001)
    tgr_h2_over_h2.SetFillStyle(3001)
    
    
    tgr_h1_over_h2__total.SetFillStyle(3004)
    tgr_h2_over_h2__total.SetFillStyle(3004)


    #--SetLineStyle
    h1.SetLineStyle(1)
    h2.SetLineStyle(1)

    h1stat.SetLineStyle(1)
    h2stat.SetLineStyle(1)

    h1__total.SetLineStyle(1)
    h2__total.SetLineStyle(1)

    tgr_h1_over_h2.SetLineStyle(1)
    tgr_h2_over_h2.SetLineStyle(1)

    tgr_h1stat_over_h2stat.SetLineStyle(1)
    tgr_h2stat_over_h2stat.SetLineStyle(1)

    tgr_h1_over_h2__total.SetLineStyle(1)
    tgr_h2_over_h2__total.SetLineStyle(1)

    
    ##--Legend
    tlegend = ROOT.TLegend(0.12, 0.65, 0.88, 0.88)#x1,y1,x2,y2 
    tlegend.SetFillColor(0)
    tlegend.SetTextFont(42)
    tlegend.SetTextSize(0.035)
    tlegend.SetLineColor(0)
    tlegend.SetShadowColor(0)




    

    canvas_name=prefix+'__'+label1+"_over_"+label2+'__'+xaxis+'__'+title
    tcanvas = ROOT.TCanvas(canvas_name,canvas_name,800,800)
    pad1 = ROOT.TPad('pad1_'+canvas_name,'pad1_'+canvas_name, 0, 1-0.72, 1, 1)
    pad1.SetTopMargin(0.098)
    pad1.SetBottomMargin(0.04)
    pad1.Draw()
    pad1.cd()

    pad1_tmr=ROOT.TMultiGraph()
    pad1_tmr.Add(h1,'2')
    pad1_tmr.Add(h2,'2')
    pad1_tmr.Add(h1__total,'2')
    pad1_tmr.Add(h2__total,'2')
    pad1_tmr.Add(h1stat,'p')
    pad1_tmr.Add(h2stat,'p')
    pad1_tmr.SetTitle(title)

    pad1_tmr.Draw('A2')
    pad1_tmr.GetYaxis().SetTitle(yaxis)
    #pad1_tmr.GetYaxis().SetTitleOffset( .4)
    
    #pad1.SetLogy()
    #tcanvas.SaveAs('1log_1.pdf')

    tlegend.AddEntry(h1__total,label1,'L')
    tlegend.AddEntry(h1__total,'Sys.+Stat.','F')  
    tlegend.AddEntry(h1,'Sys.Err.','F')
    tlegend.AddEntry(h1stat, ' Stat.Err.','LE')

    tlegend.AddEntry(h2__total,label2,'L')
    tlegend.AddEntry(h2__total,'Sys.+Stat.','F')
    tlegend.AddEntry(h2,'Sys.Err.','F')
    tlegend.AddEntry(h2stat, ' Stat.Err.','LE')
    tlegend.SetNColumns(4)
    tlegend.Draw()

    tcanvas.cd()
    pad2 = ROOT.TPad('pad2_'+canvas_name,'pad2_'+canvas_name,0,0,1, 1-0.72 )
    pad2.SetTopMargin(0.000)
    pad2.SetBottomMargin(0.39)
    pad2.Draw()
    pad2.cd()

    pad2_tmr=ROOT.TMultiGraph()
    pad2_tmr.Add(tgr_h1_over_h2,'2')
    pad2_tmr.Add(tgr_h2_over_h2,'2')
    pad2_tmr.Add(tgr_h1_over_h2__total,'2')
    pad2_tmr.Add(tgr_h2_over_h2__total,'2')
    pad2_tmr.Add(tgr_h1stat_over_h2stat,'p')
    pad2_tmr.Add(tgr_h2stat_over_h2stat,'p')
    pad2_tmr.Draw('a2')
    

    pad2_tmr.SetMaximum(1.5)
    pad2_tmr.SetMinimum(0.5)
    
    pad2_tmr.GetYaxis().SetTitle(yaxis_ratio)

    pad2_tmr.GetYaxis().SetLabelFont ( 42)
    pad2_tmr.GetYaxis().SetLabelOffset( 0.01)
    pad2_tmr.GetYaxis().SetLabelSize ( 0.1)
    pad2_tmr.GetYaxis().SetNdivisions ( 505)
    pad2_tmr.GetYaxis().SetTitleFont ( 42)
    pad2_tmr.GetYaxis().SetTitleOffset( .4)
    pad2_tmr.GetYaxis().SetTitleSize ( 0.1)

    pad2_tmr.GetXaxis().SetLabelFont ( 42)
    pad2_tmr.GetXaxis().SetLabelOffset( 0.01)
    pad2_tmr.GetXaxis().SetLabelSize ( 0.1)
    pad2_tmr.GetXaxis().SetNdivisions ( 505)
    pad2_tmr.GetXaxis().SetTitleFont ( 42)
    pad2_tmr.GetXaxis().SetTitleOffset( 1.)
    pad2_tmr.GetXaxis().SetTitleSize ( 0.1)

    pad2_tmr.GetXaxis().SetTitle(xaxis)


    pad1_tmr.SetMaximum(ymax*2)

    tcanvas.Update()
    tcanvas.SaveAs(store_file_path+'.pdf')
    tcanvas.SaveAs(store_file_path+'.png')
    tcanvas.SaveAs(store_file_path+'.root')

    
    pad1_tmr.SetMaximum(ymax*1000)
    pad1_tmr.SetMinimum(ymin*0.1)
    pad1.SetLogy()
    tcanvas.Update()
    tcanvas.SaveAs(store_file_path+'_log.pdf')
    tcanvas.SaveAs(store_file_path+'_log.png')
    tcanvas.SaveAs(store_file_path+'_log.root')

    ##---Error Comparison--##
    tcanvas2 = ROOT.TCanvas('pad1_'+canvas_name,'pad1_'+canvas_name,800,600)
    tcanvas2.cd()

    tlegend2 = ROOT.TLegend(0.50, 0.65, 0.88, 0.88)#x1,y1,x2,y2
    tlegend2.SetFillColor(0)
    tlegend2.SetTextFont(42)
    tlegend2.SetTextSize(0.035)
    tlegend2.SetLineColor(0)
    tlegend2.SetShadowColor(0)


    tlegend2.AddEntry(tgr_syserr1,label1,'F')
    tlegend2.AddEntry(tgr_syserr2,label2,'F')

    sys_tmr=ROOT.TMultiGraph()
    sys_tmr.Add(tgr_syserr1,'2')
    sys_tmr.Add(tgr_syserr2,'2')
    sys_tmr.SetTitle(title)

    sys_tmr.Draw('A2')
    sys_tmr.GetYaxis().SetTitle('Sys. Err. (%)')
    sys_tmr.GetXaxis().SetTitle(xaxis)
    sys_tmr.SetMaximum(syserrmax*2.1)
    sys_tmr.SetMinimum(-syserrmax*1.1)
    tlegend.SetNColumns(2)
    tlegend2.Draw()
    tcanvas2.SaveAs(store_file_path+'_sys_percent.pdf')
    tcanvas2.SaveAs(store_file_path+'_sys_percent.png')
    tcanvas2.SaveAs(store_file_path+'_sys_percent.root')


    del tcanvas
    del tcanvas2

    del pad1
    del pad2

    del pad1_tmr
    del pad2_tmr
    del sys_tmr

    del tlegend
    del tlegend2


    del h1stat
    del h2stat
    del h1__total
    del h2__total
    del h1
    del h2

    del tgr_h1_over_h2
    del tgr_h1stat_over_h2stat
    del tgr_h1_over_h2__total


    del tgr_h2_over_h2
    del tgr_h2stat_over_h2stat
    del tgr_h2_over_h2__total


    

if __name__ == "__main__":
    ##-for test-
    CMSSW_BASE=os.getenv('CMSSW_BASE')
    ROOT.gROOT.LoadMacro(CMSSW_BASE+'/src/Gen_validation/CMSSW_tools/scripts/modules/GetHisto.C+')
    h2path='/cms/ldap_home/jhchoi/gridvalidation/mg265_validation/event_gen/workdir/JOBDIR_HistoFactory__GENEVT_mg260_master_dyellell01234j_5f_LO_MLM__5000evt/combined_histo/'
    h1path='/cms/ldap_home/jhchoi/gridvalidation/mg265_validation/event_gen/workdir/JOBDIR_HistoFactory__GENEVT_mg261_dyellell01234j_5f_LO_MLM__5000evt/combined_histo/'

    '''
    h1=ROOT.GetTGraphAsymmErrors(h1path+'/combined_histo__306000__dimuon_mass.root',"Graph")
    h2=ROOT.GetTGraphAsymmErrors(h2path+'/combined_histo__306000__dimuon_mass.root',"Graph")
    h1stat=ROOT.GetTGraphAsymmErrors(h1path+'/combined_histo__306000__dimuon_mass__statonly.root',"Graph")
    h2stat=ROOT.GetTGraphAsymmErrors(h2path+'/combined_histo__306000__dimuon_mass__statonly.root',"Graph")

    #histopath,"DYValidation/"+x+'_'+str(idx)
    CompareTGraphAsymmErrorsWithStat("dimuon_mass",'LHAPDF306000', h1, h1stat,"MG5 v260",ROOT.kRed,h2,h2stat,"MG5 v261",ROOT.kBlue,False)

    '''
    #h1=ROOT.GetTGraphAsymmErrors(h1path+'/combined_histo__306000__dimuon_mass.root',"Graph")
    #h2=ROOT.GetTGraphAsymmErrors(h2path+'/combined_histo__306000__dimuon_mass.root',"Graph")
    #h1stat=ROOT.GetTGraphAsymmErrors(h1path+'/combined_histo__306000__dimuon_mass__statonly.root',"Graph")
    #h2stat=ROOT.GetTGraphAsymmErrors(h2path+'/combined_histo__306000__dimuon_mass__statonly.root',"Graph")
    


    h1=ROOT.GetTGraphAsymmErrors(h1path+'/combined_histo__muRmuF_default__dimuon_mass.root',"Graph")    
    h2=ROOT.GetTGraphAsymmErrors(h2path+'/combined_histo__muRmuF_default__dimuon_mass.root',"Graph")
    h1stat=ROOT.GetTGraphAsymmErrors(h1path+'/combined_histo__muRmuF_default__dimuon_mass__statonly.root',"Graph")
    h2stat=ROOT.GetTGraphAsymmErrors(h2path+'/combined_histo__muRmuF_default__dimuon_mass__statonly.root',"Graph")

    CompareTGraphAsymmErrorsWithStat("dimuon_mass",'norm. nevents','mg261/mg260','muRmuF_default', h1, h1stat,"MG5 v261",ROOT.kRed,h2,h2stat,"MG5 v260",ROOT.kBlue,'./result.pdf',True)

    
    
    
'''
kWhite  = 0,   kBlack  = 1,   kGray    = 920,  kRed    = 632,  kGreen  = 416,
kBlue   = 600, kYellow = 400, kMagenta = 616,  kCyan   = 432,  kOrange = 800,
kSpring = 820, kTeal   = 840, kAzure   =  860, kViolet = 880,  kPink   = 900
'''
