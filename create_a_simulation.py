import ocean_functions as oc
import numpy
import os

my_ocean_file = oc.Ocean("my_sample_script.ocn")
my_ocean_file.simulator()
my_ocean_file.design("design1")
my_ocean_file.model_files()
my_ocean_file.add_analysis(sim="dcOp")
my_ocean_file.add_analysis(sim="ac",low_freq="10",high_freq="1G")
my_ocean_file.add_analysis(sim="tran",stop_time="1n")
my_ocean_file.desvar("WSU3","5u")
my_ocean_file.set_temp(temp="29")
my_ocean_file.set_temp()
my_ocean_file.add_param(var1="R",min1="7",max1="100k",step1="170",var2="W",min2="12",max2="19283",step2="16")
my_ocean_file.add_run()
my_ocean_file.add_param_run()
my_ocean_file.select_result(result="dcOpInfo")
my_ocean_file.add_exit()
my_ocean_file.run_sim()
