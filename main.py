from tkinter import *
import random
names = []
score = 0
global questions_answers
asked = []


questions_answers = {
 1:["When was Cold War Released?", '13 November 2020', '26 April 2019','21 June 2020', '1 August 2020',1],   
  2:["When does Cold War take place in the game?", '2020 to 2012', '1859 to 1920', '1981 to 1984', '1400 to 1500,' '1981 to 1984',3], 
  3:["How many guns are in a mystery box?", '5', '2','6', '12', '11',4], 
  4:["What's the max level in Cold War?", 'Level 55', 'Level 69','Level 100', 'Level 10' 'Level 55',1],
  5:["Is Cold War Crossplatform?", 'Yes', 'No', 'Yes',1]
  
 } 

def randmomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked: 
    asked.append(qnum)
  elif qnum in asked:
    randmomiser()      

class QuizBegin:
    
    def __init__(self, parent):
      background_color = '#67697C'
          #frame set up
      self.quiz_frame=Frame(parent, bg=background_color, padx=100, pady=100)
      self.quiz_frame.grid()

    #widget for header
      self.heading_label = Label(self.quiz_frame, text='Cold War Quiz!', font=('Tw Cen MT', '18', 'bold'), bg=background_color,)
      self.heading_label.grid(row=0, padx=20)
      self.var1 = IntVar()

      self.user_label=Label(self.quiz_frame, text="Please enter your name:", bg=background_color)
      self.user_label.grid(row=1, padx=20)

      #Entry Box
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=2, padx=20, pady=20)

      #Create a Button
      self.continue_button=Button (self.quiz_frame, text="Continue", font=('Helvetica', '13', 'bold'), bg="#A6E1FA",command=self.name_collection)
      self.continue_button.grid(row=3, padx=20, pady=20)

    #Label for user name prompt

    def name_collection(self):
        name = self.entry_box.get()
        names.append(name)  # add name to names list declared at the beginning
        self.quiz_frame.destroy()
        Quiz(root)


class Quiz:        
    def __init__(self, parent):
      background_color = "Black"
          #frame set up
      self.quiz_frame=Frame(parent, bg=background_color)
      self.quiz_frame.grid()

      #randmomiser will randomly pick a question number which is qnum 
      randmomiser()

      self.question_label=Label(self.quiz_frame, text= questions_answers[qnum][0], fg = "white",
      bg = background_color,
      font = "Verdana 16 bold")
      self.question_label.grid(row=0, pady=50, padx=50)

      self.var1=IntVar()

      #first radio button to hold first choice answer
      self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12", "bold"),fg="#A6E1FA", bg=background_color, value=1, variable=self.var1, pady=10)
      self.rb1.grid(row=1, pady=20) 
  
      self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12", "bold"),fg="#A6E1FA", bg=background_color, value=2, variable=self.var1, pady=10)
      self.rb2.grid(row=2, pady=20) 

      self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12", "bold"),fg="#A6E1FA", bg=background_color, value=3, variable=self.var1, pady=10)
      self.rb3.grid(row=3, pady=20) 

      self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12", "bold"),fg="#A6E1FA", bg=background_color, value=4, variable=self.var1, pady=10)
      self.rb4.grid(row=4, pady=20) 

      
      self.confirm_button = Button(self.quiz_frame, text="Confirm", font=("Helvetica","13","bold"), bg="#A6E1FA", command=self.test_progress)
      self.confirm_button.grid(row=7, padx=5, pady=1)

      self.confirm_button = Label(self.quiz_frame,text="Score", font=("Tw Cen MT", "16"), bg=background_color,)

      self.scr_label = Label(self.quiz_frame)
      self.scr_label.grid(row=6, pady=1)

    def questions_setup(self):
      randmomiser()
      self.var1.set(0)
      self.question_label.config(text=questions_answers[qnum][0])
      self.rb1.config(text=questions_answers[qnum][1])
      self.rb2.config(text=questions_answers[qnum][2]) 
      self.rb3.config(text=questions_answers[qnum][3])
      self.rb4.config(text=questions_answers[qnum][4])

    def test_progress(self):
        global score
        scr_label = self.scr_label
        choice = self.var1.get()
        if len(asked)>9:#if it is the last question
            if choice==questions_answers[qnum][6]:#if last question is right answer
              score +=1
              scr_label.configure(text=score)
              self.confirm_button.config(text="confirm")
              self.end_frame()
            else: #is last question is wrong answer
                score+=0
                scr_label.config(text="The correct answer was " + questions_answers[qnum][5])
                self.confirm_button.config(text="Confirm")
                self.end_frame()
        else:#If its not last question
            if choice==0:#check if user has made a choice
                self.confirm_button.configure(text="Try Again Please, You Didn't Select Anything ")
                choice==self.var1.get()
            else:#If they made a choice and its not last question
              if choice==questions_answers[qnum][6]:#If their choice is right
                score +=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="Confirm")
                self.questions_setup()#run this method to move to next question
              else:
                score +=0
                scr_label.configure(text="The Correct Answer Was: " + questions_answers[qnum][5])
                self.confirm_button.configure(text="Confirm")
                self.questions_setup()

    def end_frame(self):
      root.withdraw()
      name=names[0]
      file=open("LeaderBoard.txt","a")
      file.write(str(score))
      file.write(" - ")
      file.write(name+"\n")
      file.close()

      inputFile = open("LeaderBoard.txt", "r")
      lineList = inputFile.readlines()
      lineList.sort()
      top=[]
      print(top)
      top5=(lineList[-5:])
      for line in top5:
          point=line.split(" - ")
          top.append((int(point[0]), point[1]))
      file.close()
      top.sort()
      top.reverse()
      return_string=""
      for i in range(len(top)):
            return_string +="{} - {}\n".format(top[i][0], top[i][1])
      print(return_string)

      open_endscrn=End()
      open_endscrn.listLabel.config(text=return_string)
      

class End:
  def __init__(self):
      background="OldLace"
      self.end_box= Toplevel(root)
      self.end_box.title("End Box")

      self.end_frame = Frame (self.end_box, width=1000, height=1000, bg=background)
      self.end_frame.grid()

      end_heading = Label (self.end_frame, text="Good Stuff!", font=("Tw Cen MT", 22, "bold"), bg=background, pady=15)
      end_heading.grid(row=0)

      exit_button = Button (self.end_frame, text="Exit", width=10, bg="IndianRed1", font=("Tw Cen MT", 12, "bold"), command=self.close_end)
      exit_button.grid(row=4, pady=20)
      self.listLabel = Label(self.end_frame, text="1st Place Avaliable", font=("Tw Cen MT", 18), width=40, bg=background, padx=10, pady=10)
      self.listLabel.grid(column=0, row=2)

      self.quit= Button(self.end_frame, text="Quit", font=("Helvetica", "13", "bold"))
    
  def close_end(self):
        self.end_box.destroy()
        root.destroy()
 

#starting point of the program
if __name__ =="__main__":
    root = Tk()#creating a window
    root.title("Cold War Quiz!")#title of the window
    open_quiz=QuizBegin(root)
    root.mainloop() #keep showing the window untill we close import