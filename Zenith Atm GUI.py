from tkinter import *
from PIL import ImageTk, Image
import time
import re

class ATM:
   #Main variables needed   
   def __init__(self):
      #Flag purpose is to stop the other statement to trigger that causes an error
      self.flag = True
      self.wrong_label_flag = True
      self.wrong_flag = True
      self.wlabel_flag = True
      self.rg_flag = True
      self.rg_label_flag = False
      self.error_rg_flag = True
      self.is_zero = False
      self.login_flag = True
      self.coin_img_flag = False
      self.rec_label_flag = False
      self.off = 5
      self.acc_flag = 0
      self.balance = 0
      
      #2D Dictonaries and Dictonaries of Accounts and Usernames
      self.accounts = {"jeranmerino147@gmail.com" : {"admin123": 5000}, 
      "ZenithSUS@gmail.com" : {"420@72": 6000},
      "admin@yahoo.com" : {"admin2002": 3000}
      }
      
      self.usernames = { "jeranmerino147@gmail.com" : "Agent Z",
      "ZenithSUS@gmail.com" : "*Zenith*",
      "admin@yahoo.com" : "admin"
      }
      
      self.passwords = {"jeranmerino147@gmail.com" : "admin123",
      "ZenithSUS@gmail.com" : "420@72",
      "admin@yahoo.com" : "admin2002"}
      
      self.username_values = self.usernames.values()
      self.regex = "[^@]+@[^@]+\.[^@]+"
       
   
   #Withdraw Button and Behaviors
   def submit(self, val, flag,  _user, _pass): 	
      	try:
      		if self.wlabel_flag == True:
      		    self.wlabel = Label(bg = "blue", fg = "#00FF00", font = ("Arial", 12))
      		    self.wlabel_flag = False
      		    
      		    
      		amt = int(val)
      		if amt != None and amt <= self.balance and flag == 1:
      		    self.balance = self.balance - amt
      		    self.update_bal(_user, _pass)
      		    self.wblabel = Label(text = "Your new balance is {}".format(self.balance), bg = "blue", fg =  "#00FF00", font = ("Arial", 12))
      		    self.wblabel.place(anchor = "c" , relx = 0.5, rely = 0.35)
      		    self.delete_btn(flag)
      		    self.decision_display(_user, _pass)
      
      		       
      		if amt > 0 and flag == 2:
      		    self.balance = self.balance + amt
      		    self.update_bal(_user, _pass)
      		    self.wblabel= Label(text = "Your new balance is {}".format(self.balance), bg = "blue", fg =  "#00FF00", font = ("Arial", 12))
      		    self.wblabel.place(anchor = "c" , relx = 0.5, rely = 0.35)
      		    self.delete_btn(flag)
      		    self.decision_display(_user, _pass)
      		   
      		             
      		
      		if amt > self.balance and flag == 1 and self.balance != 0:
      		    self.wblabel =Label(text = "Balance is not enough!", bg = "blue", fg =  "#00FF00", font = ("Arial", 12))
      		    self.wblabel.place(anchor = "c" , relx = 0.5, rely = 0.35)
      		    self.delete_btn(flag)
      		    self.decision_display(_user, _pass)
      		
      		if self.is_zero == True and self.balance == 0:
      		  self.zero_bal()
      		  self.delete_btn(flag)
      		  self.decision_display(_user, _pass)
     	    
      	   
      		          
         #Catches error if the values is not an integer
      	except:
      			self.wlabel["text"]="Invalid input!\n Please enter a number"
      			self.wlabel.place(x = 120, y = 900)
      			      	
      	
      
   def zero_bal(self):
      if self.is_zero == True:
      	self.wblabel =Label(text = "You have no credits!", bg = "blue", fg =  "#00FF00", font = ("Arial", 12))
      	self.wblabel.place(anchor = "c" , relx = 0.5, rely = 0.35)
      	
      	
      	
   def decision_display(self, _user, _pass):
        #Display Coin Image
         if self.coin_img_flag == False:
            #Coin Image and Frame
            self.coin_img_frame = Frame(window, width = 250, height = 250)
            self.coin_img_frame.place(anchor = "c", relx = 0.5, rely = 0.22)
            
            self.coin_img = ImageTk.PhotoImage(Image.open("Coin.png"))
            self.coin_display = Label(self.coin_img_frame, image = self.coin_img)
            self.coin_display.pack()
            self.coin_img_flag = True
      	   
         #Decision Transaction
         self.dlabel = Label(text = "Do you want to continue\nthe transaction?", bg = "blue", fg = "#00FF00", font = ("Arial", 8))
         self.dlabel.place(x=200, y = 600)
         
         self.bt_yes = Button(text = "Yes", bg = "blue", fg = "#00FF00", bd = 5, font = ("Arial", 8), command = lambda: self.decision(1, _user, _pass))
         self.bt_yes.place(x = 200, y = 700)
         
         self.bt_no = Button(text = "No", bg = "blue", fg = "#00FF00", bd = 5, font = ("Arial", 8), command = lambda: self.decision(None, _user, _pass))
         self.bt_no.place(x = 400, y = 700)
   
      
   #Fill the transaction chosen      
   def fill(self, flag, _user, _pass):
      		self.delete_main()
      		
      		if flag == 1:
      		   self.tlabel = Label(text = " Withdraw ", bg = "blue", fg = "#00FF00", font = ("Arial", 12), pady = 5, padx = 5)
      		   self.tlabel.place(anchor = "c", relx = 0.5, rely = 0.4)
      		   c = flag
      		elif flag == 2:
      		   self.tlabel = Label(text = " Deposit ", bg = "blue", fg = "#00FF00", font = ("Arial", 12), pady = 5, padx = 5)
      		   self.tlabel.place(anchor = "c", relx = 0.5, rely = 0.4)
      		   c = flag
      		else:
      		   pass
      		
      		#Fill Frame
      		self.fill_frame = Frame(window, highlightbackground = "#00FF00", borderwidth = 20, background =  "black", relief = "solid")
      		self.fill_frame.place(anchor = "c", relx = 0.5, rely = 0.5)
      		 
      		 #Amount Entry
      		self.enter_amount = Label(self.fill_frame, text = "Enter an amount:", bg = "black", fg = "#00FF00", font = ("Arial", 10))
      		self.enter_amount.grid(row = 0, column = 0, pady = 5)
      		
      		self.entry = Entry(self.fill_frame)
      		self.entry.grid(row = 0, column = 1, padx = 5, pady = 5)
      		
      		#Comfirm frame
      		self.cm_frame = Frame(window, highlightbackground = "#00FF00", borderwidth = 20, background =  "black", relief = "solid")
      		self.cm_frame.place(anchor = "c", relx = 0.5, rely = 0.60)
      		
      		#Confirm Button
      		self.s_btn = Button(self.cm_frame, text = "Confirm", bg = "blue", fg = "#00FF00", font = ("Arial", 8), command = lambda: self.submit(self.entry.get(), c, _user, _pass), bd = 5)
      		self.s_btn.pack()
      		
      		
      		#Delete and Backspacs Frame
      		self.db_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
      		self.db_frame.place(anchor = "c", relx = 0.5, rely = 0.67)
      		
      		#Delete and Backspace Button
      		self.d_btn = Button(self.db_frame, text = "Delete", bg = "blue", fg = "#00FF00", font = ("Arial", 8), command = lambda: self.delete(self.entry), bd = 5)
      		self.d_btn.grid(row = 1, column = 0, padx = 2, pady = 5)
      			
      		self.bs_btn = Button(self.db_frame, text = "Backspace", bg = "blue", fg = "#00FF00", font = ("Arial", 8), command = lambda: self.backspace(self.entry), bd = 5)
      		self.bs_btn.grid(row = 1, column = 1, padx = 2, pady = 5)
      		
      		
   def delete_btn(self, flag):
      		time.sleep(2)
      		if flag != self.off:
      		   self.fill_frame.destroy()
      		   self.cm_frame.destroy()
      		   self.db_frame.destroy()
      		   self.wlabel.destroy()
      		   self.tlabel.destroy()
      		   self.s_btn.destroy()
      		   self.entry.destroy()
      		   self.enter_amount.destroy()
      		   self.d_btn.destroy()
      		   self.bs_btn.destroy()

   def delete(self, entry):
   	self.entry.delete(0, END)
   
   def delete_entry_pass(self, _pass):
      self.password_entry.delete(0, END)
   
   def delete_main(self):
   	self.transaction_frame.destroy()
   	self.wbutton.destroy()
   	self.dbutton.destroy()
   	self.title.destroy()
   	self.welcome_label.destroy()
   	self.display_balance.destroy()
   	
   def backspace(self, entry):
      		self.entry.delete(len(entry.get())-1, END)
   
   def decision(self, opt, _user, _pass):
       if self.balance == 0:
          self.is_zero = True
       else:
          self.is_zero = False
          
       if opt == 1:
           time.sleep(2)
           self.wlabel_flag = True
           self.coin_img_flag = False
           self.wblabel.destroy()
           self.dlabel.destroy()
           self.bt_yes.destroy()
           self.bt_no.destroy()
           self.transactions(self.off, _user, _pass)
           self.coin_img_frame.destroy()
           self.coin_display.destroy()
       else:
           window.quit()
           
   def terminate(self):
   		   window.quit()
	  		   
   def main(self):
   	#Title 
   	self.title_atm = Label(window, text = "Zenith Atm Machine", bg = "blue", fg = "#00FF00", font = ("Symbol", 16, "bold"), padx = 5, pady = 10, relief = "solid", borderwidth = 4)
   	self.title_atm.place(x = 80, y = 350)
   	
   	#Logo 
   	self.logo_frame = Frame(window, width = 500, height = 600)
   	self.logo_frame.pack()
   	self.logo_frame.place(anchor = "c", relx = 0.5, rely = 0.15)
   	
   	self.logo = ImageTk.PhotoImage(Image.open("Logo.png"))
   	self.display_logo =  Label(self.logo_frame, image = self.logo)
   	self.display_logo.pack()
   	
   	#Title Login Frame
   	self.title_login_frame = Frame(window, highlightbackground = "#00FF00", background = "black")
   	self.title_login_frame.pack()
   	self.title_login_frame.place(x = 130, y = 500)
   	
   	#Login Label
   	self.login_label = Label(self.title_login_frame, text = "Login to your account", bg = "blue", fg = "#00FF00", font = ("Arial", 12), padx = 5, relief = "solid", borderwidth = 4)
   	self.login_label.pack(pady = 5)
   	
   	#Login and Register Frame
   	self.frame_btns = Frame(window, highlightbackground = "black", background = "black", borderwidth = 8, relief = "solid")
   	self.frame_btns.pack()
   	self.frame_btns.place(anchor = "c", relx = 0.5, rely = 0.65)
   	
   	#Login Button
   	self.login_btn = Button(self.frame_btns, text = "Login", bg = "blue", fg = "#00FF00", bd = 5, command = lambda: self.check_pass(self.username.get(), self.password.get()), font = ("Arial", 8))
   	self.login_btn.grid(row = 0, column = 0, padx = 10, pady = 10)
   	
   	#Reigister Button
   	self.register_btn = Button(self.frame_btns, text = "Register", bg = "blue", fg = "#00FF00", bd = 5, command = lambda: self.register(), font = ("Arial", 8))
   	self.register_btn.grid(row = 0, column = 1, padx = 10, pady = 10)
   	
   	#Exit Frame
   	self.exit_frame = Frame(window, highlightbackground = "black", background = "black", borderwidth = 10, relief = "solid")
   	self.exit_frame.pack()
   	self.exit_frame.place(anchor = "c", relx = 0.5, rely = 0.72)
   	
   	#Exit Button
   	self.exit_btn = Button(self.exit_frame, text = "Exit", bg = "blue", fg = "#00FF00", bd = 5, command = lambda: self.terminate(), font = ("Arial", 8))
   	self.exit_btn.pack()
   	
   	#Login Frame
   	self.login_frame = Frame(window, background = "black", borderwidth = 10, relief = "solid")
   	self.login_frame.pack()
   	self.login_frame.place(anchor = "c", relx = 0.5, rely = 0.5)
   	   
   	
   	#Username Label
   	self.username_label = Label(self.login_frame, text = "Email", bg = "black", fg = "#00FF00", font = ("Arial", 12), padx = 5)
   	self.username_label.grid(row = 0, column = 0)
   	
   	#Username Entry
   	self.username = StringVar()
   	self.username_entry = Entry(self.login_frame, textvariable = self.username)
   	self.username_entry.grid(row = 0, column = 1)
   	
   	#Password Label
   	self.password_label = Label(self.login_frame, text = "Password", bg = "black", fg = "#00FF00", font = ("Arial", 12), padx = 5)
   	self.password_label.grid(row = 1, column = 0)
   	
   	#Password Label
   	self.password = StringVar()
   	self.password_entry = Entry(self.login_frame, textvariable = self.password, show = "*")
   	self.password_entry.grid(row = 1, column = 1)
   	
   	#Recover Password Frame
   	self.rec_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
   	self.rec_frame.place(anchor = "c", relx = 0.50, rely = 0.95)
   	
   	#Recover Label
   	self.rec_label = Label(self.rec_frame, text = "Forgot account?\n Click here ==>", fg = "#00FF00", bg = "blue", font = ("Arial", 8, "bold"))
   	self.rec_label.grid(row = 0, column = 0, padx = 5, pady = 5)
   	
   	#Recover Button
   	self.rec_btn = Button(self.rec_frame, text = "Recover Account", fg = "#00FF00", bg = "blue", bd = 5, font = ("Arial", 8), command = lambda : self.recover_acc())
   	self.rec_btn.grid(row = 0, column = 1, padx = 5, pady = 5)
   	
   	
   
   #Check if Username and Password is exist and matched
   def check_pass(self, _user, _pass):
      if _user in self.accounts and _pass in self.accounts.get(_user):
         self.balance =  self.accounts.get(_user).get(_pass)
         self.transactions(0, _user, _pass)
      
      else:
         self.delete_entry_pass(_pass)
         if self.flag == True:
            if self.wrong_label_flag == True:
               self.wrong = Label(fg =  "#00FF00", bg = "blue", font = ("Arial", 12), bd = 5)
               self.wrong.place(anchor = "c", relx = 0.5, rely = 0.82)
               self.wrong_label_flag = False
             
            
            #Email and Password errors
            if len(_user) == 0 and len(_pass) == 0:
               self.wrong["text"]="Please input\nan email and password"
                  
            if not re.match(self.regex, _user) and len(_user) > 0:
                  self.wrong["text"]="Invalid email"
             
            if re.match(self.regex, _user) and len(_pass) == 0:
                  self.wrong["text"]="Password is required!"
            
            else:
                  if len(_user) > 0 and len(_pass) > 0:
                     self.wrong["text"]="Wrong Email\n or Password!"
   
            self.wrong_flag = False
                   
    
   #Recover Account                    
   def recover_acc(self):
      if self.login_flag == True:
         self.destroy_login()
         
      #Recover Title Frame
      self.recover_title_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
      self.recover_title_frame.place(anchor = "c", relx = 0.5, rely = 0.40)
      
      #Recover Label
      self.recover_label = Label(self.recover_title_frame, text = "Recover your account", fg = "#00FF00", bg = "blue", font = ("Arial",12))
      self.recover_label.pack()
      
      #Recover Fill Frame
      self.rec_fill_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
      self.rec_fill_frame.place(anchor = "c", relx = 0.5, rely = 0.5)
      
      #Account Recover Entry
      self.acc_rec_label = Label(self.rec_fill_frame, text = "Enter email address", bg = "black", fg = "#00FF00", font = ("Arial", 8))
      self.acc_rec_label.grid(row = 0, column = 0, padx = 5, pady = 5)
      
      self.acc_rec_entry = Entry(self.rec_fill_frame)
      self.acc_rec_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
      
      #Confirm and Back  Button Frame
      self.cm_btn_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
      self.cm_btn_frame.place(anchor = "c", relx = 0.5, rely = 0.60)
      
      #Confirm Button
      self.cm_btn = Button(self.cm_btn_frame, text = "Confirm", bg = "blue", fg = "#00FF00", bd = 5, command = lambda: self.recover_check(self.acc_rec_entry.get()), font = ("Arial", 8))
      self.cm_btn.grid(row = 0, column = 0, padx = 5, pady = 5)
      
      #Back Button
      self.bk_btn = Button(self.cm_btn_frame, text = "Back", bg = "blue", fg = "#00FF00", bd = 5, command = lambda: self.back(), font = ("Arial", 8))
      self.bk_btn.grid(row = 0, column = 1, padx = 5, pady = 5)
                                                                 
    #Check Account if exists
   def recover_check(self, _user):
      time.sleep(2)
      self.recover_delete()
      _pass = str(self.passwords.get(_user))
      #If Found
      if _user in self.accounts:
         self.rec_found_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
         self.rec_found_frame.place(anchor = "c", relx = 0.5, rely = 0.35)
         
         self.rec_found = Label(self.rec_found_frame, text = "Account Found!", bg = "blue", fg = "#00FF00", font = ("Arial", 14, "bold"))
         self.rec_found.pack()
         
         self.rec_cm_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
         self.rec_cm_frame.place(anchor = "c", relx = 0.5, rely = 0.5)
         
         self.rec_cm_us = Label(self.rec_cm_frame, text = "Your username is " + self.usernames.get(_user), fg = "#00FF00", bg = "blue", font = ("Arial",12))
         self.rec_cm_us.pack(padx = 5, pady = 5)
         
         self.rec_cm_ps = Label(self.rec_cm_frame, text = "Your password is {}".format(_pass), fg = "#00FF00", bg = "blue", font = ("Arial",12))
         self.rec_cm_ps.pack(padx = 5, pady = 5)
         self.rec_label_flag = True
         
       #Not Found  
      else:
         self.rec_found_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
         self.rec_found_frame.place(anchor = "c", relx = 0.5, rely = 0.5)
         
         self.rec_found = Label(self.rec_found_frame, text = "Account not found", bg = "blue", fg = "#00FF00", font = ("Arial", 14, "bold"))
         self.rec_found.pack()
      
      #Decison Recover Frame
      self.decision_rec_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
      self.decision_rec_frame.place(anchor = "c", relx = 0.5, rely = 0.63)
      
      #Decison Recover Label
      self.decision_rec_label = Label(self.decision_rec_frame, text = "Do you want to\n recover account again?", bg = "blue", fg = "#00FF00", font = ("Arial", 12))
      self.decision_rec_label.pack()
      
      #Decison Recover Button Frame
      self.decision_btn_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 12, relief = "solid")
      self.decision_btn_frame.place(anchor = "c", relx = 0.5, rely = 0.76)
      
      #Yes Button
      self.rec_yes_btn = Button(self.decision_btn_frame, text = "Yes", bg = "blue", fg = "#00FF00", bd = 5, command = lambda: self.recover_decision(self.off), font = ("Arial", 8))
      self.rec_yes_btn.grid(row = 0, column = 0, padx = 5, pady = 5)
      
      #No Button
      self.rec_no_btn = Button(self.decision_btn_frame, text = "No", bg = "blue", fg = "#00FF00", bd = 5, command = lambda: self.recover_decision(None), font = ("Arial", 8))
      self.rec_no_btn.grid(row = 0, column = 1, padx = 5, pady = 5)
      
      
   #Delete Recover Group
   def recover_delete(self):
       self.recover_title_frame.destroy()
       self.recover_label.destroy()
       self.rec_fill_frame.destroy()
       self.acc_rec_label.destroy()
       self.acc_rec_entry.destroy()
       self.cm_btn_frame.destroy()
       self.cm_btn.destroy()
       self.bk_btn.destroy()
   
   #Delete Recover Check Group
   def recover_check_delete(self):
       self.rec_found_frame.destroy()
       if self.rec_label_flag == True:
          self.rec_found.destroy()
          self.rec_cm_frame.destroy()
          self.rec_cm_us.destroy()
          self.rec_cm_ps.destroy()
       self.decision_rec_frame.destroy()
       self.decision_rec_label.destroy()
       self.decision_btn_frame.destroy()
       self.rec_yes_btn.destroy()
       self.rec_no_btn.destroy()
       
    #Decision Recover Account   
   def recover_decision(self, flag):
       time.sleep(2)
       if flag == self.off:
           self.recover_check_delete()
           self.login_flag = False
           self.rec_label_flag = False
           self.recover_acc()
       else:
           self.recover_check_delete()
           self.login_flag = True
           self.main()
                          
    #Back to Main Program       
   def back(self):
          time.sleep(2)
          self.login_flag = True
          self.recover_delete()
          self.main()
                                                                                                                              
   #Updates the balance on the dictonary      
   def update_bal(self, _user, _pass):
      self.u_bal = { _user : {_pass : self.balance}}
      self.accounts.update(self.u_bal)
   
   #Create Account   
   def create_acc(self, _email, _us, _ps):
      self.ct_acc = {_email : {_ps : 0}}
      self.ct_us = {_email : _us}
      self.ct_ps = {_email :   _ps}
      self.accounts.update(self.ct_acc)
      self.usernames.update(self.ct_us)
      self.passwords.update(self.ct_ps)
   
   #Register an account
   def register(self):
      if self.login_flag == True:
         self.destroy_login()
      
      #Register Fill up Frame
      self.register_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
      self.register_frame.place(anchor = "c", relx = 0.5, rely = 0.45)
      
      #Title Register Frame
      self.register_title_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
      self.register_title_frame.place(anchor = "c", relx = 0.5, rely = 0.30)
      
      #Title Register
      self.register_title = Label(self.register_title_frame, text = "Register an account", bg = "blue", fg = "#00FF00", font = ("Arial", 12, "bold"))
      self.register_title.pack()
      
      #Email 
      self.email_label = Label(self.register_frame, text = "Enter your email address", bg = "black", fg = "#00FF00", font = ("Arial", 8))
      self.email_label.grid(row = 0, column = 0, padx = 5, pady = 5)
      
      self.email_entry = Entry(self.register_frame)
      self.email_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
      
      #Username
      self.us_label = Label(self.register_frame, text = "Enter your username", bg = "black", fg = "#00FF00", font = ("Arial", 8))
      self.us_label.grid(row = 1, column = 0, padx = 5, pady = 5)
      
      self.us_entry = Entry(self.register_frame)
      self.us_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
      
      #Password 
      self.ps_label = Label(self.register_frame, text = "Enter password", bg = "black", fg = "#00FF00", font = ("Arial", 8))
      self.ps_label.grid(row = 2, column = 0, padx = 5, pady = 5)
      
      self.ps_entry = Entry(self.register_frame, show = "*")
      self.ps_entry.grid(row = 2, column = 1, padx = 5, pady = 5)
      
      #Confirm Password 
      self.cps_label = Label(self.register_frame, text = "Confirm password", bg = "black", fg = "#00FF00", font = ("Arial", 8))
      self.cps_label.grid(row = 3, column = 0, padx = 5, pady = 5)
      
      self.cps_entry = Entry(self.register_frame, show = "*")
      self.cps_entry.grid(row = 3, column = 1, padx = 5,  pady = 5)
      
      #Register Frame buttons
      self.rg_btn_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
      self.rg_btn_frame.place(anchor = "c", relx = 0.5, rely = 0.6)
      
      #Register Button 2
      self.register2_btn = Button(self.rg_btn_frame, text = "Register", bg = "blue", fg = "#00FF00", bd = 5, command = lambda: self.check_register(self.email_entry.get(), self.us_entry.get(), self.ps_entry.get(), self.cps_entry.get()), font = ("Arial", 8))
      self.register2_btn.grid(row = 0, column = 0, padx = 10, pady = 10)
      
      #Cancel Button
      self.cancel_btn = Button(self.rg_btn_frame, text = "Cancel", bg = "blue", fg = "#00FF00", bd = 5, command = lambda: self.delete_register(self.off), font = ("Arial", 8))
      self.cancel_btn.grid(row = 0, column = 1, padx = 10, pady = 10)
      
      
   def check_register(self, _email, _us, _ps, _cps):
      if re.match(self.regex, _email) and _ps == _cps and len(_ps) > 6 and _email not in self.accounts and _us not in self.username_values:
          self.create_acc(_email, _us, _ps)
          self.decision_rg()
         
         
      else:
         if self.rg_flag == True:
                  
               if self.error_rg_flag == True:
                  self.rg_invalid = Label(fg = "#00FF00", bg = "blue", font = ("Arial", 12))
                  self.rg_invalid.place(anchor = "c", relx = 0.5, rely = 0.7)
                  self.error_rg_flag = False
                  self.rg_label_flag = True
               
               if not re.match(self.regex, _email):
                  self.rg_invalid["text"]="Please fill a valid email address"
                                 
               if len(_ps) < 7 and re.match(self.regex, _email) and _us not in self.username_values and _email not in self.accounts:
                  self.rg_invalid["text"]="Password required\nmore than 7 characters"
               
               if _us in self.username_values and _ps == _cps:
                  self.rg_invalid["text"]="Username already taken!"
               
               if (_ps != _cps and len(_ps) > 6) and (len(_cps) > 6 and re.match(self.regex, _email)):
                  self.rg_invalid["text"]="Password does not match"
                  
               if _email in self.accounts and re.match(self.regex, _email):
                  self.rg_invalid["text"]="The account is already registered!"
                  
               if (len(_email) == 0 and len(_us) == 0) and (len(_ps) == 0 and len(_cps) ==  0):
                  self.rg_invalid["text"]="Fill up all the fields"
               
                                        
               
   def decision_rg(self):
          self.login_flag = False
          self.delete_register(0)
          
          #Decison Frame
          self.decision_label_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
          self.decision_label_frame.place(anchor = "c", relx = 0.5, rely = 0.40)
          
          self.decision_label = Label(self.decision_label_frame, text = "Do you want to register\nanother account?", fg = "#00FF00", bg = "blue", font = ("Arial", 12))
          self.decision_label.pack()
          
          #Account Added Label
          self.acc_label = Label(text = "Account registered successfully!", fg = "#00FF00", bg = "blue", font = ("Arial", 12))
          self.acc_label.place(anchor = "c", relx = 0.5, rely = 0.30)
          
          #Register Decision Frame
          self.decision_rg_frame = Frame(window, highlightbackground = "#00FF00", background = "black", borderwidth = 10, relief = "solid")
          self.decision_rg_frame.place(anchor = "c", relx = 0.5, rely = 0.5)
          
          #Yes Button
          self.yes_rg_btn = Button(self.decision_rg_frame, text = "Yes", fg = "#00FF00", bg = "blue", bd = 5, font = ("Arial", 8), command = lambda : self.decision_rg_btn(1))
          self.yes_rg_btn.grid(row = 0, column = 0, padx = 5, pady = 5)
          
          #No Button
          self.no_rg_btn = Button(self.decision_rg_frame, text = "No", fg = "#00FF00", bg = "blue", bd = 5, font = ("Arial", 8), command = lambda : self.decision_rg_btn(None))
          self.no_rg_btn.grid(row = 0, column = 1, padx = 5, pady = 5)
          
          
          
   def decision_rg_btn(self, flag):
          time.sleep(2)
          if flag == 1:
             self.login_flag = False
             self.rg_label_flag = False
             self.decision_rg_delete()
             self.register()
          else:
             self.login_flag = True
             self.decision_rg_delete()
             self.main()
             
   def decision_rg_delete(self):
          self.decision_label_frame.destroy()
          self.decision_label.destroy()
          self.acc_label.destroy()
          self.decision_rg_frame.destroy()
          self.yes_rg_btn.destroy()
          self.no_rg_btn.destroy()
                                      
                                
   #Delete Register Group         
   def delete_register(self, flag):
      time.sleep(2)
      if self.login_flag == False:
         self.login_flag = True
      if self.rg_label_flag == True:
         self.rg_invalid.destroy()
      self.register_frame.destroy()
      self.register_title_frame.destroy()
      self.register_title.destroy()
      self.email_label.destroy()
      self.email_entry.destroy()
      self.us_label.destroy()
      self.us_entry.destroy()
      self.ps_label.destroy()
      self.ps_entry.destroy()
      self.cps_label.destroy()
      self.cps_entry.destroy()
      self.rg_btn_frame.destroy()
      self.register2_btn.destroy()
      self.cancel_btn.destroy()
      self.acc_flag = 0
      if flag == self.off:
         self.main()
            
   #Destroy whole login groups
   def destroy_login(self):
      time.sleep(3)
      if self.wrong_flag == False:
         self.wrong.destroy()
      self.logo_frame.destroy()
      self.display_logo.destroy()
      self.title_atm.destroy()
      self.title_login_frame.destroy()
      self.login_frame.destroy()
      self.login_label.destroy()
      self.frame_btns.destroy()
      self.login_btn.destroy()
      self.register_btn.destroy()
      self.exit_frame.destroy()
      self.exit_btn.destroy()
      self.username_label.destroy()
      self.username_entry.destroy()
      self.password_label.destroy()
      self.password_entry.destroy()
      self.rec_frame.destroy()
      self.rec_label.destroy()
      self.rec_btn.destroy()
    
    #Logout to the ATM and destroys the transaction groups
   def logout(self):
      self.delete_btn(self.off)
      self.transaction_frame.destroy()
      self.wbutton.destroy()
      self.dbutton.destroy()
      self.title.destroy()
      self.welcome_label.destroy()
      self.display_balance.destroy()
      self.flag = True
      self.wrong_label_flag = True
      self.wrong_flag = True
      self.main()
   
   #Go to transactions and checks if the flag is not equal to off to destroy login group
   def transactions(self, flag, _user, _pass):
   	if flag != self.off:
   	   self.destroy_login()
   	   
   	#Transaction Frame
   	self.transaction_frame = Frame(window, background = "black", highlightbackground = "#00FF00", borderwidth = 25, relief = "solid")
   	self.transaction_frame.pack()
   	self.transaction_frame.place(anchor =  "c", relx = 0.5, rely = 0.5)
   	
   	#Title of Program
   	self.title = Label(self.transaction_frame, text = "Zenith Atm Machine", bg = "blue", fg = "#00FF00", font = ("Arial", 10, 'bold'), padx = 10, pady = 5)
   	self.title.pack(pady = 30)
   	
   	self.wbutton = Button(self.transaction_frame, text = "Withdraw", bg = "blue", fg = "#00FF00", font = ("Arial", 8), command = lambda: self.fill(1, _user, _pass), padx = 50, pady = 10, bd = 5)
   	self.wbutton.pack(pady = 10)
   	
   	self.dbutton = Button(self.transaction_frame, text = "Deposit", bg = "blue", fg = "#00FF00", font = ("Arial", 8), command = lambda: self.fill(2, _user, _pass), padx = 50, pady = 10, bd = 5)
   	self.dbutton.pack(pady = 10)
   	
   	self.lbutton = Button(self.transaction_frame, text = "Logout", bg = "blue", fg = "#00FF00", font = ("Arial", 8), command = lambda : self.logout(), padx = 70, pady = 10, bd = 5)
   	self.lbutton.pack(pady = 10)
   	
   	self.welcome_label = Label(text = "Hello " + self.usernames.get(_user) + "!", bg = "blue", fg = "#00FF00", padx = 20, pady = 10, font = ("Arial", 12))
   	self.welcome_label.place(anchor = "c", relx = 0.5, rely = 0.75)
   	
   	self.display_balance = Label(text = "Balance: {}".format(self.balance), bg = "blue", fg = "#00FF00", padx = 20, pady = 10, font = ("Arial", 12))
   	self.display_balance.place(anchor = "c", relx = 0.5, rely = 0.82)
      		


#Tkinter activation
window = Tk()

window.geometry("780x420")
window.title("Zenith Atm")
window.config(bg = "black")

bg = PhotoImage(file="Background.png")
bg_img =  Label(window, image = bg).pack()
atm = ATM()
atm.main()

window.mainloop()