# \usr\bin\ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("Ans.UI")

from System.Drawing import *
from System.Windows.Forms import *

import sys
from System import *
from System.ComponentModel import *
from System.Windows.Forms import *
from System.Drawing import *
from System.IO import *
from System.Windows.Forms import Form, DockStyle, WebBrowser, TextBox, Keys

import Ansys.UI
from Ansys.UI import UIManager
global Form1

import math, random, copy

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		
	def InitializeComponent(self):
		self._tabcontrol1 = TabControl()
		self._Geometry = TabPage()
		self._Particles = TabPage()
		self._label12 = Label()
		self._label13 = Label()
		self._label10 = Label()
		self._label11 = Label()
		self._label9 = Label()
		self._label8 = Label()
		self._maxz = TextBox()
		self._label4 = Label()
		self._maxy = TextBox()
		self._label5 = Label()
		self._maxx = TextBox()
		self._label6 = Label()
		self._minz = TextBox()
		self._label3 = Label()
		self._miny = TextBox()
		self._label2 = Label()
		self._minx = TextBox()
		self._label1 = Label()
		self._bbox = Label()
		self._vof = TextBox()
		self._label7 = Label()
		self._Parcels = TabPage()
		self._label14 = Label()
		self._constsize = RadioButton()
		self._psdfile = RadioButton()
		self._label15 = Label()
		self._sizeorfile = TextBox()
		self._label16 = Label()
		self._generate = RadioButton()
		self._radioButton2 = RadioButton()
		self._label17 = Label()
		self._sizeornumber = TextBox()
		self._injfile = Label()
		self._outfile = TextBox()
		self._label18 = Label()
		self._button1 = Button()
		self._label19 = Label()
		self._density = TextBox()
		self._browse = Button()
		self._tabcontrol1.SuspendLayout()
		self._Geometry.SuspendLayout()
		self._Particles.SuspendLayout()
		self._Parcels.SuspendLayout()
		self.CenterToScreen()
		self.SuspendLayout()
		# 
		# tabcontrol1
		# 
		self._tabcontrol1.Controls.Add(self._Geometry)
		self._tabcontrol1.Controls.Add(self._Particles)
		self._tabcontrol1.Controls.Add(self._Parcels)
		self._tabcontrol1.Location = Point(0, 1)
		self._tabcontrol1.Name = "tabcontrol1"
		self._tabcontrol1.SelectedIndex = 0
		self._tabcontrol1.Size = Size(609, 263)
		self._tabcontrol1.TabIndex = 0
		# 
		# Geometry
		# 
		self._Geometry.Controls.Add(self._label12)
		self._Geometry.Controls.Add(self._label13)
		self._Geometry.Controls.Add(self._label10)
		self._Geometry.Controls.Add(self._label11)
		self._Geometry.Controls.Add(self._label9)
		self._Geometry.Controls.Add(self._label8)
		self._Geometry.Controls.Add(self._maxz)
		self._Geometry.Controls.Add(self._label4)
		self._Geometry.Controls.Add(self._maxy)
		self._Geometry.Controls.Add(self._label5)
		self._Geometry.Controls.Add(self._maxx)
		self._Geometry.Controls.Add(self._label6)
		self._Geometry.Controls.Add(self._minz)
		self._Geometry.Controls.Add(self._label3)
		self._Geometry.Controls.Add(self._miny)
		self._Geometry.Controls.Add(self._label2)
		self._Geometry.Controls.Add(self._minx)
		self._Geometry.Controls.Add(self._label1)
		self._Geometry.Controls.Add(self._bbox)
		self._Geometry.Location = Point(4, 22)
		self._Geometry.Name = "Geometry"
		self._Geometry.Padding = Padding(3)
		self._Geometry.Size = Size(601, 237)
		self._Geometry.TabIndex = 0
		self._Geometry.Text = "Geometry"
		self._Geometry.UseVisualStyleBackColor = True
		# 
		# Particles
		# 
		self._Particles.Controls.Add(self._sizeorfile)
		self._Particles.Controls.Add(self._label15)
		self._Particles.Controls.Add(self._psdfile)
		self._Particles.Controls.Add(self._constsize)
		self._Particles.Controls.Add(self._label14)
		self._Particles.Controls.Add(self._vof)
		self._Particles.Controls.Add(self._label7)
		self._Particles.Controls.Add(self._density)
		self._Particles.Controls.Add(self._label19)
		self._Particles.Controls.Add(self._browse)
		self._Particles.Location = Point(4, 22)
		self._Particles.Name = "Particles"
		self._Particles.Padding = Padding(3)
		self._Particles.Size = Size(601, 237)
		self._Particles.TabIndex = 1
		self._Particles.Text = "Particles"
		self._Particles.UseVisualStyleBackColor = True
		# 
		# label12
		# 
		self._label12.Location = Point(521, 60)
		self._label12.Name = "label12"
		self._label12.Size = Size(25, 23)
		self._label12.TabIndex = 42
		self._label12.Text = "m"
		# 
		# label13
		# 
		self._label13.Location = Point(520, 32)
		self._label13.Name = "label13"
		self._label13.Size = Size(25, 23)
		self._label13.TabIndex = 41
		self._label13.Text = "m"
		# 
		# label10
		# 
		self._label10.Location = Point(339, 57)
		self._label10.Name = "label10"
		self._label10.Size = Size(25, 23)
		self._label10.TabIndex = 40
		self._label10.Text = "m"
		# 
		# label11
		# 
		self._label11.Location = Point(339, 33)
		self._label11.Name = "label11"
		self._label11.Size = Size(25, 23)
		self._label11.TabIndex = 39
		self._label11.Text = "m"
		# 
		# label9
		# 
		self._label9.Location = Point(156, 59)
		self._label9.Name = "label9"
		self._label9.Size = Size(25, 23)
		self._label9.TabIndex = 38
		self._label9.Text = "m"
		# 
		# label8
		# 
		self._label8.Location = Point(156, 34)
		self._label8.Name = "label8"
		self._label8.Size = Size(25, 23)
		self._label8.TabIndex = 37
		self._label8.Text = "m"
		# 
		# maxz
		# 
		self._maxz.Location = Point(416, 59)
		self._maxz.Name = "maxz"
		self._maxz.Size = Size(99, 20)
		self._maxz.TabIndex = 34
		self._maxz.Text = "1.0"
		# 
		# label4
		# 
		self._label4.Location = Point(370, 62)
		self._label4.Name = "label4"
		self._label4.Size = Size(50, 22)
		self._label4.TabIndex = 33
		self._label4.Text = "Max Z"
		# 
		# maxy
		# 
		self._maxy.Location = Point(233, 59)
		self._maxy.Name = "maxy"
		self._maxy.Size = Size(100, 20)
		self._maxy.TabIndex = 32
		self._maxy.Text = "1.0"
		# 
		# label5
		# 
		self._label5.Location = Point(187, 62)
		self._label5.Name = "label5"
		self._label5.Size = Size(50, 22)
		self._label5.TabIndex = 31
		self._label5.Text = "Max Y"
		# 
		# maxx
		# 
		self._maxx.Location = Point(50, 60)
		self._maxx.Name = "maxx"
		self._maxx.Size = Size(100, 20)
		self._maxx.TabIndex = 30
		self._maxx.Text = "1.0"
		# 
		# label6
		# 
		self._label6.Location = Point(4, 63)
		self._label6.Name = "label6"
		self._label6.Size = Size(50, 22)
		self._label6.TabIndex = 29
		self._label6.Text = "Max X"
		# 
		# minz
		# 
		self._minz.Location = Point(416, 33)
		self._minz.Name = "minz"
		self._minz.Size = Size(99, 20)
		self._minz.TabIndex = 28
		self._minz.Text = "0.0"
		# 
		# label3
		# 
		self._label3.Location = Point(370, 36)
		self._label3.Name = "label3"
		self._label3.Size = Size(39, 23)
		self._label3.TabIndex = 27
		self._label3.Text = "Min Z"
		# 
		# miny
		# 
		self._miny.Location = Point(233, 33)
		self._miny.Name = "miny"
		self._miny.Size = Size(100, 20)
		self._miny.TabIndex = 26
		self._miny.Text = "0.0"
		# 
		# label2
		# 
		self._label2.Location = Point(187, 36)
		self._label2.Name = "label2"
		self._label2.Size = Size(40, 23)
		self._label2.TabIndex = 25
		self._label2.Text = "Min Y"
		# 
		# minx
		# 
		self._minx.Location = Point(50, 34)
		self._minx.Name = "minx"
		self._minx.Size = Size(100, 20)
		self._minx.TabIndex = 24
		self._minx.Text = "0.0"
		# 
		# label1
		# 
		self._label1.Location = Point(4, 37)
		self._label1.Name = "label1"
		self._label1.Size = Size(40, 23)
		self._label1.TabIndex = 23
		self._label1.Text = "Min X"
		# 
		# bbox
		# 
		self._bbox.Font = Font("Microsoft Sans Serif", 8.25, FontStyle.Bold, GraphicsUnit.Point, 0)
		self._bbox.Location = Point(3, 10)
		self._bbox.Name = "bbox"
		self._bbox.Size = Size(250, 23)
		self._bbox.TabIndex = 22
		self._bbox.Text = "Bounding box of region to be patched"
		# 
		# vof
		# 
		self._vof.Location = Point(190, 14)
		self._vof.Name = "vof"
		self._vof.Size = Size(98, 20)
		self._vof.TabIndex = 38
		self._vof.Text = "0.5"
		# 
		# label7
		# 
		self._label7.Font = Font("Microsoft Sans Serif", 8.25, FontStyle.Bold, GraphicsUnit.Point, 0)
		self._label7.Location = Point(6, 14)
		self._label7.Name = "label7"
		self._label7.Size = Size(178, 40)
		self._label7.TabIndex = 37
		self._label7.Text = "Volume fraction to be patched"
		# 
		# density
		# 
		self._density.Location = Point(190, 129)
		self._density.Name = "density"
		self._density.Size = Size(98, 20)
		self._density.TabIndex = 38
		self._density.Text = "2350.0"
		# 
		# label19
		# 
		self._label19.Font = Font("Microsoft Sans Serif", 8.25, FontStyle.Bold, GraphicsUnit.Point, 0)
		self._label19.Location = Point(6, 129)
		self._label19.Name = "label19"
		self._label19.Size = Size(1198, 22)
		self._label19.TabIndex = 319
		self._label19.Text = "Density of particles"
		# 
		# Parcels
		# 
		self._Parcels.Controls.Add(self._button1)
		self._Parcels.Controls.Add(self._label18)
		self._Parcels.Controls.Add(self._outfile)
		self._Parcels.Controls.Add(self._injfile)
		self._Parcels.Controls.Add(self._sizeornumber)
		self._Parcels.Controls.Add(self._label17)
		self._Parcels.Controls.Add(self._radioButton2)
		self._Parcels.Controls.Add(self._generate)
		self._Parcels.Controls.Add(self._label16)
		self._Parcels.Location = Point(4, 22)
		self._Parcels.Name = "Parcels"
		self._Parcels.Padding = Padding(3)
		self._Parcels.Size = Size(601, 237)
		self._Parcels.TabIndex = 2
		self._Parcels.Text = "Parcels"
		self._Parcels.UseVisualStyleBackColor = True
		# 
		# label14
		# 
		self._label14.Font = Font("Microsoft Sans Serif", 8.25, FontStyle.Bold, GraphicsUnit.Point, 0)
		self._label14.Location = Point(7, 50)
		self._label14.Name = "label14"
		self._label14.Size = Size(178, 22)
		self._label14.TabIndex = 39
		self._label14.Text = "Particle size distribution"
		# 
		# constsize
		# 
		self._constsize.Location = Point(190, 44)
		self._constsize.Name = "constsize"
		self._constsize.Size = Size(104, 40)
		self._constsize.TabIndex = 40
		self._constsize.TabStop = True
		self._constsize.Text = "Constant size"
		self._constsize.UseVisualStyleBackColor = True
		self._constsize.Checked = True

		# 
		# psdfile
		# 
		self._psdfile.Location = Point(310, 44)
		self._psdfile.Name = "psdfile"
		self._psdfile.Size = Size(104, 40)
		self._psdfile.TabIndex = 41
		self._psdfile.TabStop = True
		self._psdfile.Text = "PSD (File input)"
		self._psdfile.UseVisualStyleBackColor = True
		# 
		# label15
		# 
		self._label15.Font = Font("Microsoft Sans Serif", 8.25, FontStyle.Bold, GraphicsUnit.Point, 0)
		self._label15.Location = Point(8, 93)
		self._label15.Name = "label15"
		self._label15.Size = Size(178, 22)
		self._label15.TabIndex = 42
		self._label15.Text = "Particle size/PSD File"
		# 
		# sizeorfile
		# 
		self._sizeorfile.Location = Point(190, 93)
		self._sizeorfile.Name = "sizeorfile"
		self._sizeorfile.Size = Size(98, 20)
		self._sizeorfile.TabIndex = 43
		self._sizeorfile.Text = "0.0003"
		# 
		# label16
		# 
		self._label16.Font = Font("Microsoft Sans Serif", 8.25, FontStyle.Bold, GraphicsUnit.Point, 0)
		self._label16.Location = Point(6, 12)
		self._label16.Name = "label16"
		self._label16.Size = Size(170, 40)
		self._label16.TabIndex = 0
		self._label16.Text = "Particle parcel relationship"
		# 
		# generate
		# 
		self._generate.Location = Point(186, 11)
		self._generate.Name = "generate"
		self._generate.Size = Size(204, 40)
		self._generate.TabIndex = 1
		self._generate.TabStop = True
		self._generate.Text = "Parcels of same size"
		self._generate.UseVisualStyleBackColor = True
		self._generate.Checked = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = Point(340, 11)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = Size(250, 40)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Same number of particle per parcel"
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.Checked = False
		# 
		# label17
		# 
		self._label17.Font = Font("Microsoft Sans Serif", 8.25, FontStyle.Bold, GraphicsUnit.Point, 0)
		self._label17.Location = Point(7, 53)
		self._label17.Name = "label17"
		self._label17.Size = Size(258, 40)
		self._label17.TabIndex = 3
		self._label17.Text = "Parcel size/Number of particles per parcel"
		# 
		# sizeornumber
		# 
		self._sizeornumber.Location = Point(271, 53)
		self._sizeornumber.Name = "sizeornumber"
		self._sizeornumber.Size = Size(100, 20)
		self._sizeornumber.TabIndex = 4
		self._sizeornumber.Text = "0.03"
		# 
		# injfile
		# 
		self._injfile.Font = Font("Microsoft Sans Serif", 8.25, FontStyle.Bold, GraphicsUnit.Point, 0)
		self._injfile.Location = Point(7, 95)
		self._injfile.Name = "injfile"
		self._injfile.Size = Size(100, 23)
		self._injfile.TabIndex = 5
		self._injfile.Text = "Output file"
		# 
		# outfile
		# 
		self._outfile.Location = Point(114, 95)
		self._outfile.Name = "outfile"
		self._outfile.Size = Size(300, 20)
		self._outfile.TabIndex = 6
		self._outfile.Text = r'D:\users\lsm\new.inj'
		# 
		# label18
		# 
		self._label18.Location = Point(377, 53)
		self._label18.Name = "label18"
		self._label18.Size = Size(100, 23)
		self._label18.TabIndex = 7
		self._label18.Text = "m"
		# 
		# button1
		# 
		self._button1.Location = Point(219, 187)
		self._button1.Name = "button1"
		self._button1.Size = Size(152, 23)
		self._button1.TabIndex = 8
		self._button1.Text = "Generate Injection File"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.genInjectionFile
		# 
		# browse
		# 
		self._browse.Location = Point(308, 93)
		self._browse.Name = "browse"
		self._browse.Size = Size(152, 23)
		self._browse.TabIndex = 876
		self._browse.Text = "Browse ..."
		self._browse.UseVisualStyleBackColor = True
		self._browse.Click += self.mybrowse
		# 
		# MainForm
		# 
		self.ClientSize = Size(609, 266)
		self.Controls.Add(self._tabcontrol1)
		self.Name = "MainForm"
		self.Text = "Volume Injection"
		self._tabcontrol1.ResumeLayout(False)
		self._Geometry.ResumeLayout(False)
		self._Geometry.PerformLayout()
		self._Particles.ResumeLayout(False)
		self._Particles.PerformLayout()
		self._Parcels.ResumeLayout(False)
		self._Parcels.PerformLayout()
		self.ResumeLayout(False)

	def mybrowse(self, sender, e):
		if self._psdfile.Checked == True:
			dialog = OpenFileDialog()
        
			if dialog.ShowDialog() == DialogResult.OK:
				self._sizeorfile.Text = dialog.FileName
		else:
			self._sizeorfile.Text = "0.0003"


	def genInjectionFile(self, sender, e):
		gmax = [float(self._maxx.Text), float(self._maxy.Text), float(self._maxz.Text)]
		gmin = [float(self._minx.Text), float(self._miny.Text), float(self._minz.Text)]

		number = 0.0
		dia = 0.0
		
		if (self._constsize.Checked == True):
			constdia = 1
			dia = float(self._sizeorfile.Text)
		else:
			constdia = 0
			psdfile = self._sizeorfile.Text

		print (gmax, gmin, dia, number)

		vof_pack = float(self._vof.Text)
		density = float(self._density.Text)
		parcel_dia = float(self._sizeornumber.Text)
		
		injfile = self._outfile.Text

		# Calculations

		print (parcel_dia)

		if self._constsize.Checked == False:
			infile = open(psdfile, "r")	
		outfile = open(injfile, "w+")

		if constdia == 0:
			# reading PSD from a file
			dia_range = []
			volume_frac_cum = []
 
			for line in infile:
				x, y = line.split()
				if (float(y) > 1e-8):
					dia_range.append(float(x))
					volume_frac_cum.append(float(y))
 
			count = []
 
			for i in range(len(dia_range)):
				count.append(0)
 
			for i in range(0, len(volume_frac_cum)):
				volume_frac_cum[i] /= 100.0

			print (dia_range, volume_frac_cum)

				
		vof_cubic = 0.52
		number_of_parcels = 6.0*vof_pack*(gmax[0] - gmin[0])*(gmax[1] - gmin[1])*(gmax[2] - gmin[2])/(math.pi*parcel_dia**3)
		stretch = math.pow((vof_cubic/vof_pack), 0.333333)
		total = [(gmax[i] - gmin[i])/(parcel_dia*stretch) for i in range(3)]
		part = 0

		print (number_of_parcels, vof_pack, parcel_dia)

		u, v, w, temp, mass = 0.0, 0.0, 0.0, 300.0, math.pi*parcel_dia**3.0/6.0*density/1e-8
		for k in range(int(total[2])):
			if (k % 2 == 0):
				shift = 0.5
			else:
				shift = 0.0
			z = gmin[1] + k*parcel_dia*stretch
			for j in range(int(total[1])):
				y = gmin[1] + (j + shift)*parcel_dia*stretch
				for i in range(int(total[0])):
					x = gmin[0] + (i + shift)*parcel_dia*stretch
					part += 1
					if not constdia:
						rand = random.uniform(0, 1)
						for no in range(len(volume_frac_cum) - 1, 0, -1):
							if rand > volume_frac_cum[no]:
								dia = dia_range[no + 1]
								count[no + 1] += 1
								break
					outfile.write("((%f %f %f %f %f %f %10.5g %f %e) injection:0)\n" %(x, y, z, u, v, w, dia, temp, mass))
		
		parcels_remaining = int(number_of_parcels) - part

		if parcels_remaining > 0:
			x = random.uniform(gmin[0], gmax[0])
			y = random.uniform(gmin[1], gmax[1])
			z = random.uniform(gmin[2], gmax[2])
			if not constdia:
				rand = random.uniform(0, 1)
				for no in range(len(volume_frac_cum) - 1, 0, -1):
					if rand > volume_frac_cum[no]:
						dia = dia_range[no + 1]
						count[no + 1] += 1
						break
			outfile.write("((%f %f %f %f %f %f %10.5g %f %e) injection:0)\n" %(x, y, z, u, v, w, dia, temp, mass))
			--parcels_remaining
		
		outfile.close()
		

#Open the panel

def startGui():
	global Form1
	Form1 = MainForm()
	Form1.Show()
	
UIManager.Instance.InvokeOperation("Custom Gui", startGui, True)
