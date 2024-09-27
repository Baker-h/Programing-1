import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.Menu
        self._textBox1.Location = System.Drawing.Point(120, 179)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(729, 20)
        self._textBox1.TabIndex = 0
        self._textBox1.Text = "Generally good things happen to bad people, and bad things happen to good people"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self.ClientSize = System.Drawing.Size(959, 431)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Favrite Quote"
        self.ResumeLayout(False)
        self.PerformLayout()

