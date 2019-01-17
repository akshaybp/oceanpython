#########################################################
#########################################################
# Small library of functions to quickly create ocean
# scripts with python.
# Code written by Hershel Millman
#
# NOTE: PATHS MUST BE CHANGED IN DESIGN() FUNCTION
#
# NOTE: PATHS MUST BE CHANGED IN MODEL_FILES() FUNCTION
#
# To create script, ocean_functions.Ocean("filename.ocn"),
# where filename is the name of the script to be created
#
#########################################################
#########################################################

import os
import numpy

class Ocean:
	#############################################
	# Creates instance. Must pass file name
	#############################################
	def __init__(self,filename):
		self.file = filename
		os.system("rm " + filename)

	#############################################
	# Defines simulator. Default is spectre
	#############################################
	def simulator(self,**kwargs):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		# default simulator is spectre
		simulator = kwargs.get('simulator')
		if simulator == None:
			oceanfile.write("simulator( 'spectre )\n")
		# if passed an argument, use the argument as simulator
		else:
			oceanfile.write("simulator( '" + simulator + " )\n")
		oceanfile.close()

	#############################################
	# Defines design. Must pass name of cell
	#############################################
	def design(self,design_name):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		# declaring the beginning and end of path
		start_of_path = "design( \"~/cadence/simulation/"
		end_of_path = "/spectre/schematic/netlist/netlist\")\n"
		# creating full path
		full_path = start_of_path + design_name + end_of_path
		# Writing the whole line to the file
		oceanfile.write(full_path)
		oceanfile.close()

	#############################################
	# Defines model files. Alter code below to correct path (i moved my model files)
	#############################################
	def model_files(self,**kwargs):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		# write models to file
		oceanfile.write("modelFile(\n\t\'(\"~/cadence5/models/tsmc25N.m\" \"\")\n\t\'(\"~/cadence5/models/tsmc25P.m\" \"\")\n)\n")
		oceanfile.close()

	#############################################
	# Adds analysis. See below for parameters to pass
	#############################################
	def add_analysis(self,**kwargs):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		
		sim = kwargs.get('sim')
		if sim == "dcOp":
			oceanfile.write("analysis(\'dc ?saveOppoint t  )\n")
		
		if sim == "ac":
		# For ac, pass 'low_freq' and 'high_freq'
			oceanfile.write("analysis(\'ac ?start \"" + kwargs.get('low_freq') + "\" ?stop \"" + kwargs.get('high_freq') + "\" )\n")

		if sim == "tran":
		# For tran, pass 'stop_time'
			oceanfile.write("analysis(\'tran ?stop \"" + kwargs.get('stop_time') + "\" ?errpreset \"conservative\")\n")
		oceanfile.close()

	#############################################
	# Declares variable. Pass name and value as strings
	#############################################
	def desvar(self,variable_name,variable_value):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		# write variable value to file
		oceanfile.write("desVar( \"" + variable_name + "\" " + variable_value + " )\n" )
		oceanfile.close()

	#############################################
	# Sets temp. Default is 27
	#############################################
	def set_temp(self,**kwargs):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		
		# Default temp is 27
		temp = kwargs.get('temp')
		if temp == None:
			oceanfile.write("temp( 27 )\n")
		else:
			oceanfile.write("temp( " + temp + " )\n")		
		
		oceanfile.close()

	#############################################
	# adds run command to file. No args
	#############################################
	def add_run(self):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		oceanfile.write("run()\n")		
		oceanfile.close()

	#############################################
	# adds 1 or 2 param simulations
	#############################################
	def add_param(self,**kwargs):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")

		# Getting all values
		var1 = kwargs.get('var1')
		min1 = kwargs.get('min1')
		max1 = kwargs.get('max1')
		step1 = kwargs.get('step1')
		var2 = kwargs.get('var2')
		min2 = kwargs.get('min2')
		max2 = kwargs.get('max2')
		step2 = kwargs.get('step2')

		# If only one is passed
		if var2 == None:
			oceanfile.write("paramAnalysis(\"" + var1 + "\" ?start " + min1 + " ?stop " + max1 + " ?step " + step1 + ")\n")

		# if two are passed
		else:
			oceanfile.write("paramAnalysis(\"" + var1 + "\" ?start " + min1 + " ?stop " + max1 + " ?step " + step1 + " paramAnalysis(\"" + var2 + "\" ?start " + min2 + " ?stop " + max2 + " ?step " + step2  + "))\n")		
		
		oceanfile.close()

	#############################################
	# adds runParam() command to ocean file
	#############################################
	def add_param_run(self):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		oceanfile.write("paramRun()\n")
		oceanfile.close()

	#############################################
	# add selectResult. Pass result
	#############################################
	def select_result(self,**kwargs):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		oceanfile.write("selectResult(\'" + kwargs.get('result') + " )\n")
		oceanfile.close()

	#############################################
	# add other line. Pass entire line as string
	#############################################
	def add_line(self,line):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		oceanfile.write(line + "\n")
		oceanfile.close()
		
	#############################################
	# add selectResult. Pass result
	#############################################
	def add_exit(self):
		# Open ocean file for appending
		oceanfile = open(self.file,"a")
		oceanfile.write("exit()\n")
		oceanfile.close()

	#############################################
	# Runs simulation
	#############################################
	def run_sim(self):
		os.system("ocean -restore " + self.file)
