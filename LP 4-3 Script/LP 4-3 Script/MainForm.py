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
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._button1.Font = System.Drawing.Font("SimSun-ExtB", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 132)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(127, 64)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._button2.Font = System.Drawing.Font("SimSun-ExtB", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(12, 240)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(127, 64)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._button3.Font = System.Drawing.Font("SimSun-ExtB", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(12, 353)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(127, 64)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(214, 32)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(215, 20)
        self._textBox1.TabIndex = 3
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MistyRose
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("MV Boli", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(9, 24)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(175, 35)
        self._label1.TabIndex = 4
        self._label1.Text = "Eggs you have :"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MistyRose
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("MV Boli", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(154, 309)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(131, 35)
        self._label3.TabIndex = 6
        self._label3.Text = "Remainders:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MistyRose
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("MV Boli", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(154, 196)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(131, 35)
        self._label4.TabIndex = 7
        self._label4.Text = "Dozens:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Linen
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("MV Boli", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(317, 196)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(131, 35)
        self._label2.TabIndex = 8
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Linen
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("MV Boli", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(317, 309)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(131, 35)
        self._label5.TabIndex = 9
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LavenderBlush
        self.ClientSize = System.Drawing.Size(478, 455)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "LP 4-3 Script"
        self.ResumeLayout(False)
        self.PerformLayout()






    def Button1Click(self, sender, e):
        Eggs = int(self._textBox1.Text)
        Doz = Eggs // 12 
        Rem = Eggs % 12


        self._label2.Text = str(Doz)
        self._label5.Text = str(Rem)


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label2.Text = ""
        self._label5.Text = ""


    def Button3Click(self, sender, e):
        Application.Exit()