import copy
Dictinary = {'а':1,'б':2,'в':3,'г':4,'д':5,'е':6,'ё':7,'ж':8,'з':9,'и':10,'й':11,'к':12,'л':13,'м':14,'н':15,'о':16,'п':17,'р':18,'с':19,'т':20,'у':21,'ф':22,'х':23,'ц':24,'ч':25,'ш':26,'щ':27,'ъ':28,'ы':29,'ь':30,'э':31,'ю':32,'я':33,'№':34,'+':35,'-':36,' ':37,}
def minor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M
def opred(A):
    n = len(A[0])
    if n == 1:
        return A[0][0]
    signum = 1
    opredelitel = 0
    for j in range(n):
            opredelitel += A[0][j]*signum*opred(minor(A, 0, j))
            signum *= -1
    return opredelitel
def evklid(d,b):
    x,xx,y,yy=1,0,0,1
    while b:
        q=d//b
        d,b=b,d%b
        x,xx=xx,x-xx*q
        y,yy=yy,y-yy*q
    return (x)

def minor_matrix (A):
    minor_matrix= [0]*int(len(A))
    for i in range(int(len(A))):
        minor_matrix[i] = [0]*int(len(A))     
    M = copy.deepcopy(A)
    for r in range(len(A)**2):
        for i in range(len(A)):
            for n in range(len(A)):
                del M[i]
                for j in range(len(A)-1):
                    del M[j][n]
                if((i+n)%2==0):
                    minor_matrix[i][n]=opred(M)
                else:
                    minor_matrix[i][n]=-opred(M)
                M = copy.deepcopy(A)
    return minor_matrix
def delenie_matric(minor_matrix,n):
    for i in range(len(minor_matrix)):
            for j in range(len(minor_matrix)):
                if( minor_matrix[i][j]<0):
                    minor_matrix[i][j]=-(abs(minor_matrix[i][j])%n)
                else:
                    minor_matrix[i][j]=minor_matrix[i][j]%n   
    return minor_matrix
def umnogenie_matric(codeword,origword,shifro_matrica):
    if len(origword) % int(len(codeword)**0.5) == 0:
        word_blok = [0]*int(len(origword))
    else:
        origword+=chr(32)*(int(len(codeword)**0.5)-len(origword) % int(len(codeword)**0.5))
        word_blok = [0]*int(len(origword))
    for i in range(int(len(origword))):
        word_blok[i] = Dictinary.get(origword[i])
    word_blok_1 = [0]*int(len(origword))
    k=0
    for l in range(int(len(origword))//int(len(codeword)**0.5)):
        for i in range(int(len(codeword)**0.5)):
            v=l*int(len(codeword)**0.5)  
            for j in range(int(len(codeword)**0.5)):
                word_blok_1[k]+=word_blok[v]*shifro_matrica[j][i] 
                v+=1          
            k+=1    
    return word_blok_1
def output(word_blok_1):
    for val in word_blok_1:
        for key,value in Dictinary.items():
            if (val%37)==value:
                print(key, end='')    
           
def transponir(minor_matrix):
    A = [0]*int(len(minor_matrix))
    for i in range(int(len(minor_matrix))):
        A[i] = [0]*int(len(minor_matrix))     
    for i in range(len(minor_matrix)):
        for j in range(len(minor_matrix)):
            A[j][i]=minor_matrix[i][j]
    return A
                
codeword = input("Введите кодовое слово, его длина должна быть квадратом целого числа ")
shifro_matrica = [0]*int(len(codeword)**0.5)
for i in range(int(len(codeword)**0.5)):
    shifro_matrica[i] = [0]*int(len(codeword)**0.5) 
k=0
for i in range(int(len(codeword)**0.5)):
    for j in range(int(len(codeword)**0.5)):
        shifro_matrica[i][j] = Dictinary.get(codeword[k])   
        k+=1
vibor = int(input("Шифруем- 1, дешифруем - 2, ничего - 0\n"))
if vibor == 1:
    origword=input("Что шифруем?")
    output(umnogenie_matric(codeword,origword,shifro_matrica))
elif vibor ==2:
    origword=input("Что дешифруем?")
    opredelitel=opred(shifro_matrica)
    x=evklid(opredelitel,37)
    if(opredelitel<0 and x>0):
        obrat_opred=x
    elif(opredelitel>0 and x<0):
        obrat_opred=37+x
    elif(opredelitel>0 and x>0):
        obrat_opred=x
    elif(opredelitel<0 and x<0):
        obrat_opred=-x
    minor_matrix=minor_matrix(shifro_matrica)    
    delenie_matric(minor_matrix,37)
    for i in range(len(minor_matrix)):
        for j in range(len(minor_matrix)):
            minor_matrix[i][j]=minor_matrix[i][j]*obrat_opred   
    delenie_matric(minor_matrix,37)
    for i in range(len(minor_matrix)):
        for j in range(len(minor_matrix)):
            if(minor_matrix[i][j]<0):
                minor_matrix[i][j]=37+minor_matrix[i][j]   
    minor_matrix=transponir(minor_matrix)
    output(umnogenie_matric(codeword,origword,minor_matrix))