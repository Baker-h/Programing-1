import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.Info
        self._button1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(111, 43)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(139, 57)
        self._button1.TabIndex = 0
        self._button1.Text = "About Me"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Tempus Sans ITC", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(86, 146)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(795, 238)
        self._label1.TabIndex = 2
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.Info
        self._button2.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(418, 43)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(139, 57)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.Info
        self._button3.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(708, 43)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(139, 57)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlLight
        self.ClientSize = System.Drawing.Size(968, 443)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "About Me"
        self.ResumeLayout(False)


   
    
def Label1Click(self, sender, e):
    self._label1.Text = ""
  

def Button1Click(self, sender, e):
    self._label1.Text = "Hello, my name is Harrison, I am a senior at Craig high school."

def Button2Click(self, sender, e):
    self._label1.Text = ""

def Button3Click(self, sender, e):
    Aplication.Exit()

def TextBox1TextChanged(self, sender, e):
   pass

