# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:59:01 2018

@author: Rakshith G
"""

import string
import random
from tkinter import *
from tkinter import ttk
window=Tk()
gender=IntVar()
gender.set(1)
num_char=IntVar()
rashi=StringVar()
#rashi.set('libra')
def createw():
    
    l1=Label(window,text="Welcome..")
    l1.grid(row=0,column=1)
    l2=Label(window,text="Baby's Gender:")
    l2.grid(row=1,column=0)
    r1=Radiobutton(window, text="Male",value=1,variable=gender).grid(row=1,column=2,sticky=W)
    r2=Radiobutton(window, text="Female",value=2,variable=gender).grid(row=1,column=1,sticky=E)
    l3=Label(window,text="lenght of the name:")
    l3.grid(row=2,column=0)
    e1=Entry(window, textvariable = num_char)
    e1.grid(row=3,column=1)
    
    l4=Label(window,text="Choice the " )
    l4.grid(row=4,column=0)
    s1=ttk.Combobox(window,width=15, textvariable = rashi)
    s1['values'] = ('Aries','Aquarius','Cancer','Capricorn','Gemini','Libra','Pisces','Scorpio','Saggitarius','Taurus','Leo','Virgo')
    s1.grid(row=5,column=1)    
    b1=Button(window, text="click",command=getdata) 
    b1.grid(row=6,column=1)
    
    
def textgen():
    a=random.choice(string.ascii_lowercase - 'f')
    #print(a)
    return a
def getdata():
   ln=Label(window, text="a")
   ln.grid(row=8,column=0)
   genderf=gender.get()
   num_charf=num_char.get()
   rashif=rashi.get()
   if rashif == "Libra":
       #print("12")
       li=['Ra','Re','Ro','Ta','Te','To']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
          
           
       print(name1) 
       print(name2)
       print(name3)
       print(name4)
       print(name5)
   if rashif == "Aries":
       li=['Cho','Che','La','Le','Lo','Aa']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
          
           
       print(name1) 
       print(name2)
       print(name3)
       print(name4)
       print(name5)
   if rashif =="Taurus":
       li=['Ia','Ua','Ea','Oa','Wa','We','Wo']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
   if rashif =="Gemini":
       li=['Ka','Ke','Koo','Gh','An','Ch','Ha']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"           
           
       print(name1) 
       print(name2)
       print(name3)
       print(name4)
       print(name5)
   if rashif == "Cancer":
       li=['He','Ho','Da','De','Do']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
       print(name1) 
       print(name2)
       print(name3)
       print(name4)
       print(name5)
   if rashif == "Leo":
       li=['Mo','Ma','Me','Ta','Te','To']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
       print(name1) 
       print(name2)
       print(name3)
       print(name4)
       print(name5)
   if rashif == "Virgo":
       li=['To','Pa','Pe','Po','Sh','Th']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
       print(name1) 
       print(name2)
       print(name3)
       print(name4)
       print(name5)
   if rashif == "Scorpio":
       li=['To', 'Na', 'Ne', 'No', 'Yu','Ya','Ye']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
       print(name1) 
       print(name2)
       print(name3)
       print(name4)
       print(name5)  
   if rashif == "Saggitarius":
       li=['Ye', 'Yo', 'Bha', 'Bho', 'Dha', 'Pha', 'Ta', 'Bhe']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
       print(name1) 
       print(name2)
       print(name3)
       print(name4)
       print(name5)  
        
   if rashif == "Capricorn":
       li=['Bho', 'Ja', 'Jee', 'Khe', 'Kho', 'Khe', 'Kho', 'Ga', 'Ge']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
   if rashif == "Aquarius":
       li=['Go', 'Ge', 'Go', 'Sa', 'Se', 'So', 'Se', 'So',' Da']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra"
   if rashif == "Pisces":
       li=['Th', 'Jh', 'Yan', 'De', 'Do', 'Cha', 'Che']
       name1=random.choice(li)
       name2=random.choice(li)
       name3=random.choice(li)
       name4=random.choice(li)
       name5=random.choice(li)
       for i in range(num_charf-4):
           name1=name1+ran()  
           name2=name2+ran()
           name3=name3+ran()
           name4=name4+ran()
           name5=name5+ran()
       if genderf == 1:
           name1=name1+"th"  
           name2=name2+"in"
           name3=name3+"th"
           name4=name4+"an"
           name5=name5+"al"
       else:
           name1=name1+"ya"  
           name2=name2+"ni"
           name3=name3+"ta"
           name4=name4+"ma"
           name5=name5+"ra" 
   ln.configure(text = name1+"\n"+name2+"\n"+name3+"\n"+name4+"\n"+name5)

           
def ran():
    return random.choice(string.ascii_lowercase)
createw()     
window.mainloop()