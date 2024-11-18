import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
    
    def InitializeComponent(self):
        self._components = System.ComponentModel.Container()
        resources = System.Resources.ResourceManager("Slot_Machine.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._pictureBox1 = System.Windows.Forms.PictureBox()
        self._pictureBox2 = System.Windows.Forms.PictureBox()
        self._pictureBox3 = System.Windows.Forms.PictureBox()
        self._pictureBox4 = System.Windows.Forms.PictureBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._pictureBox5 = System.Windows.Forms.PictureBox()
        self._pictureBox6 = System.Windows.Forms.PictureBox()
        self._pictureBox7 = System.Windows.Forms.PictureBox()
        self._pictureBox8 = System.Windows.Forms.PictureBox()
        self._pictureBox9 = System.Windows.Forms.PictureBox()
        self._pictureBox10 = System.Windows.Forms.PictureBox()
        self._pictureBox11 = System.Windows.Forms.PictureBox()
        self._timer1 = System.Windows.Forms.Timer(self._components)
        self._pictureBox1.BeginInit()
        self._pictureBox2.BeginInit()
        self._pictureBox3.BeginInit()
        self._pictureBox4.BeginInit()
        self._pictureBox5.BeginInit()
        self._pictureBox6.BeginInit()
        self._pictureBox7.BeginInit()
        self._pictureBox8.BeginInit()
        self._pictureBox9.BeginInit()
        self._pictureBox10.BeginInit()
        self._pictureBox11.BeginInit()
        self.SuspendLayout()
        # 
        # pictureBox1
        # 
        self._pictureBox1.BackColor = System.Drawing.Color.White
        self._pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox1.Location = System.Drawing.Point(13, 10)
        self._pictureBox1.Name = "pictureBox1"
        self._pictureBox1.Size = System.Drawing.Size(129, 175)
        self._pictureBox1.TabIndex = 0
        self._pictureBox1.TabStop = False
        # 
        # pictureBox2
        # 
        self._pictureBox2.BackColor = System.Drawing.Color.White
        self._pictureBox2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox2.Location = System.Drawing.Point(169, 10)
        self._pictureBox2.Name = "pictureBox2"
        self._pictureBox2.Size = System.Drawing.Size(129, 175)
        self._pictureBox2.TabIndex = 1
        self._pictureBox2.TabStop = False
        # 
        # pictureBox3
        # 
        self._pictureBox3.BackColor = System.Drawing.Color.White
        self._pictureBox3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox3.Location = System.Drawing.Point(323, 10)
        self._pictureBox3.Name = "pictureBox3"
        self._pictureBox3.Size = System.Drawing.Size(129, 175)
        self._pictureBox3.TabIndex = 2
        self._pictureBox3.TabStop = False
        # 
        # pictureBox4
        # 
        self._pictureBox4.Image = resources.GetObject("pictureBox4.Image")
        self._pictureBox4.Location = System.Drawing.Point(13, 191)
        self._pictureBox4.Name = "pictureBox4"
        self._pictureBox4.Size = System.Drawing.Size(439, 208)
        self._pictureBox4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox4.TabIndex = 3
        self._pictureBox4.TabStop = False
        self._pictureBox4.Visible = False
        self._pictureBox4.Click += self.PictureBox4Click
        # 
        # button1
        # 
        self._button1.BackgroundImage = resources.GetObject("button1.BackgroundImage")
        self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._button1.Location = System.Drawing.Point(482, 10)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(298, 251)
        self._button1.TabIndex = 4
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Papyrus", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(483, 263)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(296, 38)
        self._button2.TabIndex = 5
        self._button2.Text = "Pickpocket"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Papyrus", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(486, 303)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(148, 39)
        self._label1.TabIndex = 6
        self._label1.Text = "Bet:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(656, 304)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(123, 38)
        self._textBox1.TabIndex = 7
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.SeaShell
        self._label2.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(656, 345)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(124, 34)
        self._label2.TabIndex = 8
        self._label2.Text = "100"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Papyrus", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(486, 345)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(148, 36)
        self._label3.TabIndex = 9
        self._label3.Text = "Cash:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.SeaShell
        self._label4.Location = System.Drawing.Point(471, 383)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(333, 21)
        self._label4.TabIndex = 10
        # 
        # pictureBox5
        # 
        self._pictureBox5.BackColor = System.Drawing.Color.Gainsboro
        self._pictureBox5.BackgroundImage = resources.GetObject("pictureBox5.BackgroundImage")
        self._pictureBox5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox5.Location = System.Drawing.Point(26, 200)
        self._pictureBox5.Name = "pictureBox5"
        self._pictureBox5.Size = System.Drawing.Size(54, 50)
        self._pictureBox5.TabIndex = 11
        self._pictureBox5.TabStop = False
        self._pictureBox5.Visible = False
        # 
        # pictureBox6
        # 
        self._pictureBox6.BackColor = System.Drawing.Color.Gainsboro
        self._pictureBox6.BackgroundImage = resources.GetObject("pictureBox6.BackgroundImage")
        self._pictureBox6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox6.Location = System.Drawing.Point(111, 200)
        self._pictureBox6.Name = "pictureBox6"
        self._pictureBox6.Size = System.Drawing.Size(54, 50)
        self._pictureBox6.TabIndex = 12
        self._pictureBox6.TabStop = False
        self._pictureBox6.Visible = False
        # 
        # pictureBox7
        # 
        self._pictureBox7.BackColor = System.Drawing.Color.Gainsboro
        self._pictureBox7.BackgroundImage = resources.GetObject("pictureBox7.BackgroundImage")
        self._pictureBox7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox7.Location = System.Drawing.Point(199, 200)
        self._pictureBox7.Name = "pictureBox7"
        self._pictureBox7.Size = System.Drawing.Size(54, 50)
        self._pictureBox7.TabIndex = 13
        self._pictureBox7.TabStop = False
        self._pictureBox7.Visible = False
        # 
        # pictureBox8
        # 
        self._pictureBox8.BackColor = System.Drawing.Color.Gainsboro
        self._pictureBox8.BackgroundImage = resources.GetObject("pictureBox8.BackgroundImage")
        self._pictureBox8.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox8.Location = System.Drawing.Point(282, 200)
        self._pictureBox8.Name = "pictureBox8"
        self._pictureBox8.Size = System.Drawing.Size(54, 50)
        self._pictureBox8.TabIndex = 14
        self._pictureBox8.TabStop = False
        self._pictureBox8.Visible = False
        # 
        # pictureBox9
        # 
        self._pictureBox9.BackColor = System.Drawing.Color.Gainsboro
        self._pictureBox9.BackgroundImage = resources.GetObject("pictureBox9.BackgroundImage")
        self._pictureBox9.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox9.Location = System.Drawing.Point(370, 200)
        self._pictureBox9.Name = "pictureBox9"
        self._pictureBox9.Size = System.Drawing.Size(54, 50)
        self._pictureBox9.TabIndex = 15
        self._pictureBox9.TabStop = False
        self._pictureBox9.Visible = False
        # 
        # pictureBox10
        # 
        self._pictureBox10.BackColor = System.Drawing.Color.Gainsboro
        self._pictureBox10.BackgroundImage = resources.GetObject("pictureBox10.BackgroundImage")
        self._pictureBox10.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox10.Location = System.Drawing.Point(26, 331)
        self._pictureBox10.Name = "pictureBox10"
        self._pictureBox10.Size = System.Drawing.Size(54, 50)
        self._pictureBox10.TabIndex = 16
        self._pictureBox10.TabStop = False
        self._pictureBox10.Visible = False
        # 
        # pictureBox11
        # 
        self._pictureBox11.BackColor = System.Drawing.Color.Gainsboro
        self._pictureBox11.BackgroundImage = resources.GetObject("pictureBox11.BackgroundImage")
        self._pictureBox11.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox11.Location = System.Drawing.Point(102, 331)
        self._pictureBox11.Name = "pictureBox11"
        self._pictureBox11.Size = System.Drawing.Size(54, 50)
        self._pictureBox11.TabIndex = 17
        self._pictureBox11.TabStop = False
        self._pictureBox11.Visible = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.PeachPuff
        self.ClientSize = System.Drawing.Size(832, 411)
        self.Controls.Add(self._pictureBox11)
        self.Controls.Add(self._pictureBox10)
        self.Controls.Add(self._pictureBox9)
        self.Controls.Add(self._pictureBox8)
        self.Controls.Add(self._pictureBox7)
        self.Controls.Add(self._pictureBox6)
        self.Controls.Add(self._pictureBox5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._pictureBox4)
        self.Controls.Add(self._pictureBox3)
        self.Controls.Add(self._pictureBox2)
        self.Controls.Add(self._pictureBox1)
        self.Name = "MainForm"
        self.Text = "Slot Machine"
        self._pictureBox1.EndInit()
        self._pictureBox2.EndInit()
        self._pictureBox3.EndInit()
        self._pictureBox4.EndInit()
        self._pictureBox5.EndInit()
        self._pictureBox6.EndInit()
        self._pictureBox7.EndInit()
        self._pictureBox8.EndInit()
        self._pictureBox9.EndInit()
        self._pictureBox10.EndInit()
        self._pictureBox11.EndInit()
        self.ResumeLayout(False)
        self.PerformLayout()



























    def Button2Click(self, sender, e):
        rnd = System.Random()
        money = rnd.Next(1, 51)
        if money > 25:
            MessageBox.Show("You failed to steal money")
        else:
            cmoney = float(self._label2.Text)
            self._label2.Text = str(round(cmoney + money, 2))
        pass

    def Button1Click(self, sender, e):
        image1 = self._pictureBox5.BackgroundImage
        image2 = self._pictureBox6.BackgroundImage
        image3 = self._pictureBox7.BackgroundImage
        levOff = self._pictureBox8.BackgroundImage
        levOn = self._pictureBox9.BackgroundImage
        rnd = System.Random()
        num1 = 0
        num2 = 0
        num3 = 0
        
        if self._textBox1.Text == "":
            MessageBox.Show("You must enter an amount to bet first")
            return
    
    
    money = float(self._textBox1.Text)
    bet = float(self._textBox1.Text)
    newmoney = money - bet
    
    if money == 0:
        MessageBox.Show("You have no money left")
    elif bet < 1:
        MessageBox.Show("You must bet at least $1")
    elif bet > money and bet > newmoney:
        MessageBox.Show("You don't have enough money")
    else:
        
        pass

    def PictureBox4Click(self, sender, e):
        pass