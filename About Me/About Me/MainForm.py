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
        self._button1.BackColor = System.Drawing.SystemColors.Info
        self._button1.Font = System.Drawing.Font("Comic Sans MS", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(409, 374)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(139, 57)
        self._button1.TabIndex = 0
        self._button1.Text = "About Me"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(76, 32)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(851, 20)
        self._textBox1.TabIndex = 1
        self._textBox1.Text = "Hello, my name is Harrison, I am a senior at Craig high school."
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(968, 443)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "About Me"
        self.ResumeLayout(False)
        self.PerformLayout()
def Button1Click(self, sender, e):
    self.label1.text = 

    def Button1Click(self, sender, e):
        pass

    def TextBox1TextChanged(self, sender, e):
        pass