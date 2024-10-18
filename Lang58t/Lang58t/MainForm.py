import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Blue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Viner Hand ITC", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(3, 3)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(203, 25)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Item Price"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Blue
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Viner Hand ITC", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(3, 37)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(203, 25)
        self._label2.TabIndex = 1
        self._label2.Text = "Enter Amount Given"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkOrchid
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Viner Hand ITC", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(3, 125)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(203, 25)
        self._label3.TabIndex = 2
        self._label3.Text = "Dollars"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkOrchid
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Viner Hand ITC", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(3, 159)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(203, 25)
        self._label4.TabIndex = 3
        self._label4.Text = "Quarters"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.DarkOrchid
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("Viner Hand ITC", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label5.Location = System.Drawing.Point(3, 195)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(203, 25)
        self._label5.TabIndex = 4
        self._label5.Text = "Dimes"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.DarkOrchid
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label6.Font = System.Drawing.Font("Viner Hand ITC", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label6.Location = System.Drawing.Point(3, 231)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(203, 25)
        self._label6.TabIndex = 5
        self._label6.Text = "Nickles"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.DarkOrchid
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label7.Font = System.Drawing.Font("Viner Hand ITC", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label7.Location = System.Drawing.Point(3, 266)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(203, 25)
        self._label7.TabIndex = 6
        self._label7.Text = "Pennies"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(214, 7)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(172, 21)
        self._textBox1.TabIndex = 7
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Modern No. 20", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(214, 41)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(172, 21)
        self._textBox2.TabIndex = 8
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.PaleGreen
        self._label8.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(214, 125)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(171, 24)
        self._label8.TabIndex = 9
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.PaleGreen
        self._label9.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(215, 160)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(171, 24)
        self._label9.TabIndex = 10
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.PaleGreen
        self._label10.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(214, 196)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(171, 24)
        self._label10.TabIndex = 11
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.PaleGreen
        self._label11.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(215, 232)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(171, 24)
        self._label11.TabIndex = 12
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.PaleGreen
        self._label12.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(215, 267)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(171, 24)
        self._label12.TabIndex = 13
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightYellow
        self._button1.Font = System.Drawing.Font("Segoe Marker", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(57, 68)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(278, 45)
        self._button1.TabIndex = 14
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightYellow
        self._button2.Font = System.Drawing.Font("Segoe Marker", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(32, 306)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(143, 45)
        self._button2.TabIndex = 15
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightYellow
        self._button3.Font = System.Drawing.Font("Segoe Marker", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(225, 306)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(143, 45)
        self._button3.TabIndex = 16
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Silver
        self.ClientSize = System.Drawing.Size(392, 372)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Lang58t"
        self.ResumeLayout(False)
        self.PerformLayout()



    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        Doll = num2 - num1
        Quar = Doll //.25
        Dim = Quar //.15
        Nic = Dim //.10
        Pen = Nic //.01

       
            
        self._label8.Text = str(Doll)
        self._label9.Text = str(Quar)
        self._label10.Text = str(Dim)
        self._label11.Text = str(Nic)
        self._label12.Text = str(Pen)
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label8.Text = ""
        self._label9.Text = ""
        self._label10.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()











