﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Teal
        self._button1.Font = System.Drawing.Font("NSimSun", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(12, 21)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(147, 78)
        self._button1.TabIndex = 0
        self._button1.Text = "Ring Ring"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Teal
        self._button2.Font = System.Drawing.Font("NSimSun", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(12, 185)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(147, 78)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Teal
        self._button3.Font = System.Drawing.Font("NSimSun", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(12, 355)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(147, 78)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Gainsboro
        self._label1.Font = System.Drawing.Font("Tempus Sans ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(179, 30)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(261, 55)
        self._label1.TabIndex = 3
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Gainsboro
        self._label2.Font = System.Drawing.Font("Tempus Sans ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(179, 107)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(261, 55)
        self._label2.TabIndex = 4
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Gainsboro
        self._label3.Font = System.Drawing.Font("Tempus Sans ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(179, 195)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(261, 55)
        self._label3.TabIndex = 5
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Gainsboro
        self._label4.Font = System.Drawing.Font("Tempus Sans ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(179, 281)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(261, 55)
        self._label4.TabIndex = 6
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Gainsboro
        self._label5.Font = System.Drawing.Font("Tempus Sans ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(179, 367)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(261, 55)
        self._label5.TabIndex = 7
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DimGray
        self.ClientSize = System.Drawing.Size(470, 454)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Phone Numbers"
        self.ResumeLayout(False)

    def Button1Click(self, sender, e):
        self._label1.Text = "(608) 314-1344"
        self._label2.Text = "(608) 756-5511"
        self._label3.Text = "(608) 756-4343"
        self._label4.Text = "(847) 903-4446"
        self._label5.Text = "(414) 278-2728"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""

    def Button3Click(self, sender, e):
        Aplication.Exit()