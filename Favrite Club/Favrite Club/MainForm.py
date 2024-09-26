import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._button1.Font = System.Drawing.Font("MS UI Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(373, 338)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(196, 79)
        self._button1.TabIndex = 0
        self._button1.Text = "Favrite Club or activity"
        self._button1.UseVisualStyleBackColor = False
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.InactiveCaption
        self._textBox1.Location = System.Drawing.Point(100, 63)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(767, 20)
        self._textBox1.TabIndex = 1
        self._textBox1.Text = "JSOL"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(959, 431)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Favrite Club"
        self.ResumeLayout(False)
        self.PerformLayout()

