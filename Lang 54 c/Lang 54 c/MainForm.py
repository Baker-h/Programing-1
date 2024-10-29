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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MistyRose
        self._button1.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 381)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(138, 58)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MistyRose
        self._button2.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(156, 381)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(155, 58)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MistyRose
        self._button3.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(317, 381)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(138, 58)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Salmon
        self.ClientSize = System.Drawing.Size(467, 451)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Lang 54 c"
        self.ResumeLayout(False)

