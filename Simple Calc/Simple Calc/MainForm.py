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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.PaleTurquoise
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("MingLiU-ExtB", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(10, 10)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(107, 39)
        self._label1.TabIndex = 0
        self._label1.Text = "Number 1:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.PaleTurquoise
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("MingLiU-ExtB", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(10, 89)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(107, 39)
        self._label2.TabIndex = 1
        self._label2.Text = "Operation:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.PaleTurquoise
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("MingLiU-ExtB", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(10, 179)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(107, 39)
        self._label3.TabIndex = 2
        self._label3.Text = "Number 2:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.PaleTurquoise
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("MingLiU-ExtB", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(10, 267)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(107, 39)
        self._label4.TabIndex = 3
        self._label4.Text = "Result:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Teal
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("MingLiU-ExtB", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Location = System.Drawing.Point(154, 89)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(48, 39)
        self._label5.TabIndex = 4
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightBlue
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label6.Font = System.Drawing.Font("MingLiU_HKSCS-ExtB", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(123, 267)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(173, 39)
        self._label6.TabIndex = 5
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.Info
        self._textBox1.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(123, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(173, 33)
        self._textBox1.TabIndex = 6
        self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.SystemColors.Info
        self._textBox2.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(123, 179)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(173, 33)
        self._textBox2.TabIndex = 7
        self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("MS PGothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(313, 22)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(56, 49)
        self._button1.TabIndex = 8
        self._button1.Text = "+"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("MS PGothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(375, 22)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(56, 49)
        self._button2.TabIndex = 9
        self._button2.Text = "-"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("MS PGothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(437, 22)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(56, 49)
        self._button3.TabIndex = 10
        self._button3.Text = "="
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Font = System.Drawing.Font("MS PGothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(313, 89)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(56, 49)
        self._button4.TabIndex = 11
        self._button4.Text = "^"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.Font = System.Drawing.Font("MS PGothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(375, 89)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(56, 49)
        self._button5.TabIndex = 12
        self._button5.Text = "/"
        self._button5.UseVisualStyleBackColor = True
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.Font = System.Drawing.Font("MS PGothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(437, 89)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(56, 49)
        self._button6.TabIndex = 13
        self._button6.Text = "//"
        self._button6.UseVisualStyleBackColor = True
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.Font = System.Drawing.Font("MS PGothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(357, 154)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(92, 49)
        self._button7.TabIndex = 14
        self._button7.Text = "MOD"
        self._button7.UseVisualStyleBackColor = True
        self._button7.Click += self.Button7Click
        # 
        # button8
        # 
        self._button8.Font = System.Drawing.Font("MS PGothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(330, 218)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(144, 49)
        self._button8.TabIndex = 15
        self._button8.Text = "Clear"
        self._button8.UseVisualStyleBackColor = True
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.Font = System.Drawing.Font("MS PGothic", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(330, 280)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(144, 49)
        self._button9.TabIndex = 16
        self._button9.Text = "Exit"
        self._button9.UseVisualStyleBackColor = True
        self._button9.Click += self.Button9Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Honeydew
        self.ClientSize = System.Drawing.Size(501, 341)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Simple Calc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button9Click(self, sender, e):
        Application.Exit()

    def Button8Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label6.Text = ""
        self._label5.Text = ""
        

    def Button1Click(self, sender, e):
        self._label5.Text = "+"
        
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        
        Add = Num1 + Num2

    def Button2Click(self, sender, e):
        self._label5.Text = "-"
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        Sub = Num1 - Num2
        
    def Button3Click(self, sender, e):
        self._label5.Text = "="
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        Eq = Num1 == Num2
        
    def Button4Click(self, sender, e):
        self._label5.Text = "^"
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        Car = Num1 ^ Num2

    def Button5Click(self, sender, e):
        self._label5.Text = "/"
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        Div = Num1 / Num2

    def Button6Click(self, sender, e):
        self._label5.Text = "//"
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        Double = Num1 // Num2

    def Button7Click(self, sender, e):
        Num1 = int(self._textBox1.Text)
        Num2 = int(self._textBox2.Text)
        
        if self._label5.Text == "+":
            Add = Num1 + Num2
            self._label6.Text = str(Add)
            
        if self._label5.Text == "-":
            Sub = Num1 - Num2
            self._label6.Text = str(Sub)
            
        if self._label5.Text == "+":
            Add = Num1 + Num2
            self._label6.Text = str(Add)
            
            