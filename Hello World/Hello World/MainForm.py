﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(108, 43)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(643, 280)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button1.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 354)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(202, 63)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button2.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(740, 354)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(202, 63)
        self._button2.TabIndex = 3
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button3.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(371, 354)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(202, 63)
        self._button3.TabIndex = 4
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(954, 443)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Hello World"
        self.ResumeLayout(False)
        

    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        pass
    self_label1.Text = "Hello, World!"

    def Button3Click(self, sender, e):
        pass
    Self._label1.Text = ""

    def Button2Click(self, sender, e):
        pass
    Aplication.Exit()
    