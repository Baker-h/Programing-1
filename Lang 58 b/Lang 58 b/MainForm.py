import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.SteelBlue
        self._textBox1.Font = System.Drawing.Font("Segoe Script", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.Color.White
        self._textBox1.Location = System.Drawing.Point(159, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(294, 33)
        self._textBox1.TabIndex = 0
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.SteelBlue
        self._textBox2.Font = System.Drawing.Font("Segoe Script", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.Color.White
        self._textBox2.Location = System.Drawing.Point(159, 51)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(294, 33)
        self._textBox2.TabIndex = 1
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.SteelBlue
        self._textBox3.Font = System.Drawing.Font("Segoe Script", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.ForeColor = System.Drawing.Color.White
        self._textBox3.Location = System.Drawing.Point(159, 90)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(294, 33)
        self._textBox3.TabIndex = 2
        self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.PaleTurquoise
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(10, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(132, 32)
        self._label1.TabIndex = 3
        self._label1.Text = "int 1:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.PaleTurquoise
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(10, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(132, 32)
        self._label2.TabIndex = 4
        self._label2.Text = "int 2:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.PaleTurquoise
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 91)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(132, 32)
        self._label3.TabIndex = 5
        self._label3.Text = "int 3:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.RoyalBlue
        self._button1.Font = System.Drawing.Font("Rockwell", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(12, 384)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(142, 57)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.RoyalBlue
        self._button2.Font = System.Drawing.Font("Rockwell", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.White
        self._button2.Location = System.Drawing.Point(163, 384)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(142, 57)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.RoyalBlue
        self._button3.Font = System.Drawing.Font("Rockwell", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.White
        self._button3.Location = System.Drawing.Point(311, 384)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(142, 57)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MediumTurquoise
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(74, 196)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(321, 30)
        self._label4.TabIndex = 9
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MediumTurquoise
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(74, 242)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(321, 30)
        self._label5.TabIndex = 10
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightCyan
        self.ClientSize = System.Drawing.Size(465, 453)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Lang 58 b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        A = int(self._textBox1.Text)
        B = int(self._textBox2.Text)
        C = int(self._textBox3.Text)
        
        root1 = (-B + math.sqrt(2))
        root2 = (-B - math.sqrt(2))
        
        self._label4.Text = str(root1)
        self._label5.Text = str(root2)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""



    def Button3Click(self, sender, e):
        Aplication._Exit()








