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
        self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Font = System.Drawing.Font("Papyrus", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(345, 348)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(268, 87)
        self._button1.TabIndex = 0
        self._button1.Text = "Craig what?"
        self._button1.UseVisualStyleBackColor = False
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.InactiveBorder
        self._textBox1.Location = System.Drawing.Point(156, 63)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(642, 20)
        self._textBox1.TabIndex = 1
        self._textBox1.Text = "Craig Rules!"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self.ClientSize = System.Drawing.Size(951, 449)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Craig Rules"
        self.ResumeLayout(False)
        self.PerformLayout()

