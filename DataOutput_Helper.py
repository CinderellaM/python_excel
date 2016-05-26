#coding=utf-8
class DataOutput_Helper:

	@staticmethod
	def get_scen_param(scen,scen_index,ip_index):
		return scen[scen_index][1][ip_index]

	@staticmethod
	def get_scen_param_arg(scen_param):
		arglist=[]
		ft=filter(lambda x:x!='('and x!=')',scen_param)
		for n in ft.split(','):
			arglist.append(n.split('='))
		return arglist

	@staticmethod
	def replace_by_arg(arglist,repalced):
		#print arglist
		for argnum in range(len(arglist)):
			#print argnum,arglist[argnum][0]
			repalced=repalced.replace(arglist[argnum][0],str(arglist[argnum][1]))
		
		#print repalced	
		return repalced	

	@staticmethod
	def replace_by_arg_Layer(arglist,repalced):
		for argnum in range(len(arglist)):
			repalced=repalced.replace('Layer='+arglist[argnum][0],'L'+arglist[argnum][1])
		return repalced	

	@staticmethod
	def float_to_int(float_data):
		if eval(str(float_data))==int(eval(str(float_data))):
			return str(int(eval(str(float_data))))
		else:
			return str(float_data)			
	@staticmethod
	def set_formula(formula,gvalue,lvalue,scen,ip,mode):
		formula_re=[]
		#print ip **ip is all right
		#print formula
		for ip_index in range(len(ip)):
			for scen_index in range(len(scen)):
				scen_param=DataOutput_Helper.get_scen_param(scen,scen_index,ip_index)
				#print scen_param ** all right
				if scen_param!='x':
					if scen_param!=u'()':
						arglist=DataOutput_Helper.get_scen_param_arg(scen_param)
						#print arglist  **all right
						#print formula_s	
						formula_s=DataOutput_Helper.replace_by_arg(arglist,formula[ip_index])
					#	print formula_s,scen[scen_index][0] **all right
					else:
						formula_s=formula[ip_index]
						#print  formula_s **all right
					formula_s=DataOutput_Helper.replace_by_arg(lvalue,formula_s)
					#print lvalue
					#print formula_s
					formula_s=DataOutput_Helper.replace_by_arg(gvalue,formula_s)
					#print gvalue
					#print formula_s
					formula_re.append((ip[ip_index],mode[ip_index],scen[scen_index][0],formula_s))#(IP,mode,scen,formula)
		#print formula_re
		return formula_re

	@staticmethod	
	def get_logName(ip,mode,scen,inputP,outputP,gvalue):
		nameb=[]
		for ip_index in range(len(ip)):
			namedif=[]
			for scen_index in range(len(scen)):
				scen_param=DataOutput_Helper.get_scen_param(scen,scen_index,ip_index) 
				if scen_param!='x':	
					if scen_param not in namedif:
						#两个场景的参数一样则只算一个					
						namedif.append(scen_param)
						logname=ip[ip_index]+'_IN_'+inputP[ip_index].replace(',','_')+'_OUT_'+outputP[ip_index].replace(',','_')
					#	print logname
						if scen_param!=u'()':
							arglist=DataOutput_Helper.get_scen_param_arg(scen_param)
						#	print arglist
							logname=DataOutput_Helper.replace_by_arg_Layer(arglist,logname)
							logname=DataOutput_Helper.replace_by_arg(arglist,logname)
						#print logname,'#'
						#print gvalue,'*****'
						logname=DataOutput_Helper.replace_by_arg(gvalue,logname)
						#print logname,'@'
						cal_logname=logname.split('_')
						for log_index in range(len(cal_logname)):	
							if '**' in cal_logname[log_index]:
								 cal_logname[log_index]=cal_logname[log_index].replace('**','*')
		                                              #   print  cal_logname[log_index]
								# cal_logname[log_index]=DataOutput_Helper.float_to_int(eval(cal_logname[log_index]))	
						logname='_'.join(cal_logname)
						logname=logname.replace('Layer','L').replace('*','x')		
						nameb.append([ip[ip_index],mode[ip_index],scen[scen_index][0],logname])#(IP,mode,scen,logname)		
		return nameb

	def __init__(self,dataInput_helper):
		self.__project=dataInput_helper.get_projectName()	
		self.__formula=DataOutput_Helper.set_formula(dataInput_helper.get_formula(),dataInput_helper.get_globalValue(),dataInput_helper.get_localValue(),
							     dataInput_helper.get_scenario(),dataInput_helper.get_ipValue(),dataInput_helper.get_mode())
		#print dataInput_helper.get_globalValue() **all right
	#	print dataInput_helper.get_localValue()
		#print self.__formula  *here have wrong--->set_formula
		self.__log=DataOutput_Helper.get_logName(dataInput_helper.get_ipValue(),dataInput_helper.get_mode(),dataInput_helper.get_scenario(),
							 dataInput_helper.get_input(),dataInput_helper.get_output(),dataInput_helper.get_globalValue())
		print  self.__log
		self.__ipStyleNumD=dataInput_helper.get_ipStyleNumD()
		self.__scenarioStyleNum=dataInput_helper.get_scenarioStyleNum()
		self.__scenarioParamNum=dataInput_helper.get_scenarioParamNum()
	def get_ipStyle(self):
		ipStyle=self.__ipStyleNumD.keys()
		return ipStyle        
	def get_scen_name(self):
		scenario=self.__scenarioStyleNum
		return scenario
	def get_data_num(self,scenName):#scen_num
		#print self.__scenarioParamNum.keys()
		for name in self.__scenarioParamNum.keys():
			if scenName==name:
				#print self.__scenarioParamNum[name]
				return self.__scenarioParamNum[name]
	def get_project_name(self):
		return self.__project
	def get_data_by_index(self,scenName):
		data=[]
		for for_index in range(len(self.__formula)):
			if  self.__formula[for_index][2]==scenName:
				#print self.__formula,'$$'
				data.append((self.__formula[for_index][0],self.__formula[for_index][3])) #(ip,formula)
               	return data
	def retrieval_log_by_scen(self,scen):
		log=self.__log[:]
		log=filter(lambda x:x[2]==scen,log)
		return log
	def retrieval_log_by_ip(self,ip):
		log=self.__log[:]
		log=filter(lambda x:x[0]==ip,log)
		return log	
	def add_info_to_log(self,log,log_id):
		for n in range(len(self.__log)):
			if log==self.__log[n]:
				self.__log[n].append(log_id)
