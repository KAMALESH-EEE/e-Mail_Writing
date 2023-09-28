from TextVoice import voice,speech
cont=[]

def text():
    try:
        t=voice()
        return t
    except:
        print('Re_Try')
        text()

def details():
    speech('For Who?')
    print('For Who?')
    global cont
    cont.append("From:\n\tR KAMALESH\n")
    ta = voice()
    cont.append("To:\n\t"+ta+'\n')
    cont.append('Respected: Sir/Madam\n\t')
    speech("Subject")
    ta=voice()
    cont.append('Sub:'+ta+'-reg.\n')
def WriteMail():
    tex='\t'
    while True:
        
        ta=text()
        
        if ta =='end':
            cont.append(tex+'.')
            break
        elif ta=='new line':
            tex+='\n'
            cont.append(tex)
            tex='\t'
        elif ta == 'show':
            print(tex)
        else:
            tex+=ta
            tex+='. '
    cont.append('\n\t\t\t Thank You.\n')

details()
WriteMail()

fil=open('email.txt','w')
fil.writelines(cont)
fil.close()
fil=open('email.txt','r')
cont=fil.readlines()
for i in cont:
    print(i)
    speech(i)
