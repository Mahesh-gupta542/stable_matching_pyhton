import random
import sys

def main():

    n =int(sys.argv[1])
    k =int(sys.argv[2])
    for l in range(1,11):
        file_nameW='inputW_n_k_'+str(n)+'_'+str(k)+'_'+str(l)+'.txt'
        file_nameM='inputM_n_k_'+str(n)+'_'+str(k)+'_'+str(l)+'.txt'
        file_namekM='inputMI_n_k_'+str(n)+'_'+str(k)+'_'+str(l)+'.txt'
        file_namekW='inputWI_n_k_'+str(n)+'_'+str(k)+'_'+str(l)+'.txt'
        WI=[]
        tempk=''
        for i in range(1,(k+1)):
            M=[]
            cntrW = n
            tempW=''
            while cntrW > 0:
                tempW='W' +str(random.randint(1,n))
                if tempW not in M:
                    M.append(tempW)
                    cntrW=cntrW-1
            if i==1:
                with open(file_nameW,'w') as file_open:
                    print(','.join(M), file=file_open)
            else:
                with open(file_nameW,'a') as file_open:
                    print(','.join(M), file=file_open)
            W=[]
            cntrM = n
            tempM=''
            while cntrM > 0:
                tempM='M' +str(random.randint(1,n))
                if tempM not in W:
                    W.append(tempM)
                    cntrM=cntrM-1
            if i==1:
                with open(file_nameM,'w') as file_open:
                    print(','.join(W), file=file_open)
            else:
                with open(file_nameM,'a') as file_open:
                    print(','.join(W), file=file_open)
        for i in range(1,(n+1)):
            tempkM='prefer'+str(random.randint(1,k))
            tempkW='prefer'+str(random.randint(1,k))
            if i==1:
                with open(file_namekM,'w') as file_open:
                    print(tempkM, file=file_open)
                with open(file_namekW,'w') as file_open:
                    print(tempkW, file=file_open)
            else:
                with open(file_namekM,'a') as file_open:
                    print(tempkM, file=file_open)
                with open(file_namekW,'a') as file_open:
                    print(tempkW, file=file_open)
        
if __name__=="__main__":
    main()
                
        
    
