import System.Drawing
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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MistyRose
        self._button1.Font = System.Drawing.Font("Niagara Solid", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(11, 360)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(127, 57)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MistyRose
        self._button2.Font = System.Drawing.Font("Niagara Solid", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(157, 360)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(127, 57)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MistyRose
        self._button3.Font = System.Drawing.Font("Niagara Solid", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(301, 360)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(127, 57)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(200, 17)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(197, 20)
        self._textBox1.TabIndex = 3
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightCoral
        self._label1.Font = System.Drawing.Font("Poor Richard", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(11, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(169, 34)
        self._label1.TabIndex = 4
        self._label1.Text = "Enter Value:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Modern No. 20", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 18
        self._listBox1.Location = System.Drawing.Point(40, 68)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(356, 256)
        self._listBox1.TabIndex = 5
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.RosyBrown
        self.ClientSize = System.Drawing.Size(440, 430)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Program 152 b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()