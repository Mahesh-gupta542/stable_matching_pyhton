import sys
import time

current_milli_time = lambda: int(round(time.time() * 1000))

tot_num_of_exctn=0
tot_time_taken =0

def menPreferCheck(W,pref_numbr,man,man1):
    #this function will check whether a particular woman prefers M over M1 or not.
    for each in W[pref_numbr]:
        if(each==man):
            return True
        elif(each==man1):
           return False


def stableMatching(M, W, MI, WI,out_file_name):
    menFreeList=list(MI.keys())
    outWomnPair={}
    global tot_num_of_exctn
    global tot_time_taken
    for each1 in list(WI.keys()):
        outWomnPair[each1]='free'

    loopCounter=len(MI)

    no_of_execution=0
    start_time= current_milli_time()
    while(loopCounter>0):
        #get the first free man
        man=menFreeList.pop()
        #get the the woman in order of preference list
        for each2 in M[MI[man]]:
            if man in list(outWomnPair.values()):
                break
            # if woman is free then pair m and w and mark m as not free
            if (outWomnPair[each2]=='free'):
                outWomnPair[each2]=man
                loopCounter=loopCounter-1
            #if woman w is not free then check for the preference of m over m'
            else:
                man1=outWomnPair[each2]
                pref_nmbr=WI[each2]
                if menPreferCheck(W,pref_nmbr,man,man1):
                    outWomnPair[each2]=man 
                    #loopCounter=loopCounter-1
                    menFreeList.append(man1)
                no_of_execution=no_of_execution+1
    end_time=current_milli_time()
    tot_num_of_exctn=tot_num_of_exctn+no_of_execution
    tot_time_taken=tot_time_taken+(end_time-start_time)
    with open(out_file_name,'a') as out_file:
          print(outWomnPair,file=out_file)
          print('no_of_execution: '+str(no_of_execution), file=out_file)
          print('time_taken: '+str(end_time-start_time), file=out_file)
          print('--------------------------------------------------------', file = out_file)
          print('', file=out_file)
    

def main(filename_M,filename_W,filename_MI,filename_WI,out_file_name):
    M={}
    W={}
    MI={}
    WI={}
    #creating array M from the input file
    cntr=1
    data=open(filename_M)
    for each_line in data:
        key= 'prefer'+str(cntr)
        data=each_line.strip().split(',')
        M[key]=data
        cntr=cntr+1
    #creating array w from the input file
    cntr=1
    data=open(filename_W)
    for each_line in data:
        key= 'prefer'+str(cntr)
        data=each_line.strip().split(',')
        W[key]=data
        cntr=cntr+1
    #creating the array MI from the input file 
    cntr=1
    data=open(filename_MI)
    for each_line in data:
        key= 'M'+str(cntr)
        data=each_line.strip()
        MI[key]=data
        cntr=cntr+1
    #creating array WI from the input file
    cntr=1
    data=open(filename_WI)
    for each_line in data:
        key= 'W'+str(cntr)
        data=each_line.strip()
        WI[key]=data
        cntr=cntr+1
    
    stableMatching(M, W, MI, WI,out_file_name)

if __name__ == '__main__':
    n=sys.argv[1]
    k=sys.argv[2]
    out_file_name='out_data_for_n_'+n+'_k_'+k+'.txt'
    with open(out_file_name,'w') as out_file:
        print('Execution result for n= %s and k= %s' %(n,k),file=out_file)
    for l in range(1,11):
        filename_M='input_files/inputW_n_k_'+n+'_'+k+'_'+str(l)+'.txt'
        filename_W='input_files/inputM_n_k_'+n+'_'+k+'_'+str(l)+'.txt'
        filename_MI='input_files/inputMI_n_k_'+n+'_'+k+'_'+str(l)+'.txt'
        filename_WI='input_files/inputWI_n_k_'+n+'_'+k+'_'+str(l)+'.txt'
        main(filename_M,filename_W,filename_MI,filename_WI,out_file_name)
    with open(out_file_name,'a') as out_file:
          print('Average no of execution : ' + str(tot_num_of_exctn/10),file=out_file)
          print('Average time taken : ' + str(tot_time_taken/10),file=out_file)
