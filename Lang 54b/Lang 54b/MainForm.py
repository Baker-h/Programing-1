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
        self._textBox4 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Azure
        self._textBox1.Font = System.Drawing.Font("MV Boli", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(160, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(160, 38)
        self._textBox1.TabIndex = 0
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Azure
        self._textBox2.Font = System.Drawing.Font("MV Boli", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(160, 56)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(160, 38)
        self._textBox2.TabIndex = 1
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.Azure
        self._textBox3.Font = System.Drawing.Font("MV Boli", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(160, 100)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(160, 38)
        self._textBox3.TabIndex = 2
        self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.Azure
        self._textBox4.Font = System.Drawing.Font("MV Boli", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(160, 144)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(160, 38)
        self._textBox4.TabIndex = 3
        self._textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._button1.Font = System.Drawing.Font("MS UI Gothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(17, 378)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(131, 61)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._button2.Font = System.Drawing.Font("MS UI Gothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(175, 378)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(131, 61)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._button3.Font = System.Drawing.Font("MS UI Gothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(325, 378)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(131, 61)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Ivory
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Segoe Marker", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(139, 243)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(291, 37)
        self._label1.TabIndex = 7
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Ivory
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Segoe Marker", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(139, 293)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(291, 37)
        self._label2.TabIndex = 8
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Ivory
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Segoe Marker", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(35, 243)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(70, 37)
        self._label3.TabIndex = 9
        self._label3.Text = "Sum"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Ivory
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Segoe Marker", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(35, 293)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(70, 37)
        self._label4.TabIndex = 10
        self._label4.Text = "Ave"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(468, 452)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Lang 54b"
        self.ResumeLayout(False)
        self.PerformLayout()













    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = int(self._textBox3.Text)
        num4 = int(self._textBox4.Text)
        Sum = num1 + num2 + num3 + num4
        Ave = Sum / 4.0

        self._label1.Text = str(Sum)
        self._label2.Text = str(Ave)
        
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label1.Text = ""
        self._label2.Text = ""


    def Button3Click(self, sender, e):
        Application.Exit()
