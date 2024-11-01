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
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(11, 14)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(117, 55)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(178, 14)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(117, 55)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(342, 14)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(117, 55)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Control
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Monotype Corsiva", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 87)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(198, 32)
        self._label1.TabIndex = 3
        self._label1.Text = "Enter Speed Limit:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Control
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Monotype Corsiva", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 136)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(198, 32)
        self._label2.TabIndex = 4
        self._label2.Text = "Enter Vehicle Speed:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.InfoText
        self._textBox1.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.SystemColors.Window
        self._textBox1.Location = System.Drawing.Point(241, 90)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(206, 30)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.SystemColors.InfoText
        self._textBox2.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.SystemColors.Window
        self._textBox2.Location = System.Drawing.Point(241, 139)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(206, 30)
        self._textBox2.TabIndex = 6
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.Control
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Monotype Corsiva", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(94, 198)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(75, 32)
        self._label3.TabIndex = 7
        self._label3.Text = "Fine:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.Control
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Monotype Corsiva", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Red
        self._label4.Location = System.Drawing.Point(215, 198)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(198, 32)
        self._label4.TabIndex = 8
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(471, 265)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Program 82 a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        SpeedLimit = int(self._textBox1.Text)
        VSpeed = int(self._textBox2.Text)
        OverAmount = VSpeed - SpeedLimit
        Fine = OverAmount * 5.00 + 20.00
        
        self._label4.Text = str(Fine)
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()
        
        
        
        