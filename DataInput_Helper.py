#coding=utf-8
class DataInput_Helper:
	#从表格中读入数据
	@staticmethod
	def float_to_int(float_data):
                if float_data=='':
			return 	float_data
		elif float_data==int(float_data):
			return str(int(float_data))
		else:
			return str(float_data)	
			
	def __init__(self):
		self.__project=''
		self.__globalValue=[]
		self.__localValue=[]
		self.__ipValue=[]
		self.__mode=[]
		self.__param=[]
		self.__input=[]
		self.__output=[]
		self.__formula=[]
		self.__scenario=[]
		self.__ipStyleNumD={}
		self.__ipStyleNumL=[]
		self.__scenarioStyleNum=[]
		self.__scenarioParamNum={}
	#project--------------------
	def set_project(self,project):
		self.__project=project
	def get_projectTitle(self):
		return self.__project[0]
	def get_projectRow(self):
		return self.__project[1][0]
	def get_projectCol(self):
		return self.__project[1][1]
	def get_projectName(self):
		return self.__project[2]
	#gvalue---------------------
	def set_globalValue(self,globalValue):
		self.__globalValue.append(globalValue)
	def get_globalValueTitle(self,index):
		if index>len(self.__globalValue)-1:
			return -1
		else:
			return self.__globalValue[index][0]
	def get_globalValueRow(self,index):
		return self.__globalValue[index][1][0]
	def get_globalValueCol(self,index):
		return self.__globalValue[index][1][1]
	def get_globalValueName(self,index):
		return self.__globalValue[index][2]
	def get_globalValue(self):
		gvalueL=[]
		for gvalue in range(len(self.__globalValue)):
			gvalueL.append((self.__globalValue[gvalue][0],self.__globalValue[gvalue][2]))	
		return gvalueL
	#lvalue-----------------------	
	def set_localValue(self,localValue):
		#print localValue
		self.__localValue.append(localValue)
	def get_localValueTitle(self,index):
		if index>len(self.__localValue)-1:
			return -1
		else:
			return self.__localValue[index][0]
	def get_localValueRow(self,index):
		return self.__localValue[index][1][0]
	def get_localValueCol(self,index):
		return self.__localValue[index][1][1]
	def get_localValueCol0(self,index):
		col0=self.__localValue[index][3][:]
		col0.insert(0,self.__localValue[index][2])
		return col0
	def get_localValueCol1(self,index):
		col1=self.__localValue[index][5][:]
		col1.insert(0,self.__localValue[index][4])
		return col1
	def get_localValueCol2(self,index):
		col2=self.__localValue[index][7][:]
		col2.insert(0,self.__localValue[index][6])
		return col2
	def get_localValue(self):
		lvalueL=[]
		for lvalue in range(len(self.__localValue)):
				for index in range(len(self.__localValue[lvalue][7])):
					if self.__localValue[lvalue][7][index]!='':
						lvalueL.append((self.__localValue[lvalue][7][index],self.__localValue[lvalue][5][index]))
		return lvalueL
        #--------------------
	def set_ipValue(self,ipValue):
		self.__ipValue.append(ipValue)
	def set_mode(self,mode):
		self.__mode.append(mode)
	def set_input(self,ginput):
		self.__input.append(ginput)
	def set_output(self,goutput):
		self.__output.append(goutput)
	def set_formula(self,formula):
		
		self.__formula.append(formula)	
		#print self.__formula,'###'
	def set_scenario(self,scenario,param):
		self.__scenario.append((scenario,param))
	def set_ipStyleNum(self):
		ipStyleNumD={}
		ipStyleNumL=[]
		ipName=''
		mode=1
		for num in range(len(self.__ipValue)):
			if self.__ipValue[num]==ipName and self.__mode[num]>mode:
				ipStyleNumD.pop(self.__ipValue[num])
				ipStyleNumD.setdefault(self.__ipValue[num],self.__mode[num])
				ipStyleNumL.pop()
				ipStyleNumL.append((self.__ipValue[num],self.__mode[num]))
				mode=self.__mode[num]
			elif self.__ipValue[num]==ipName and self.__mode[num]==mode:
				ipStyleNumD.setdefault(self.__ipValue[num],self.__mode[num])
			elif self.__ipValue[num]!=ipName:
				ipStyleNumD.setdefault(self.__ipValue[num],self.__mode[num])
				ipStyleNumL.append((self.__ipValue[num],self.__mode[num]))
				ipName=self.__ipValue[num]
				mode=self.__mode[num]
		self.__ipStyleNumD=ipStyleNumD
		self.__ipStyleNumL=ipStyleNumL
	def set_param(self,param):
		self.__param.append(param)
	#-----------scenario---------------------------------
	def set_scenarioStyleNum(self):
		for num in range(len(self.__scenario)):
			self.__scenarioStyleNum.append(self.__scenario[num][0])#场景名称
		#print self.__scenarioStyleNum
	def set_scenarioParamNum(self):
		for num in range(len(self.__scenario)):
			number=0
			for enum in range(len(self.__scenario[num][1])):
				if self.__scenario[num][1][enum]!='x':
					number+=1
			self.__scenarioParamNum.setdefault(self.__scenario[num][0],number)#每个场景拥有多少行？
			#print self.__scenarioParamNum
	def set_scenrioParam(self,scenario_index):
		return self.__scenario[scenario_index][1]
	def get_ipValue(self):
		return self.__ipValue
	#def get_projectName(self):
		#return self.__project
	#def get_globalValue(self):
		#return self.__globalValue
	#def get_localValue(self):
		#return self.__localValue
	def get_mode(self):
		return self.__mode
	def get_param(self):
		return self.__param
	def get_scenario(self):
		return self.__scenario
	def get_formula(self):
		return self.__formula
	def get_input(self):
		return self.__input
	def get_output(self):
		return self.__output
        
	def get_ipStyleNumD(self):
		return self.__ipStyleNumD
	def get_ipStyleNumL(self):
		return self.__ipStyleNumL
	def get_scenarioStyleNum(self):
		return self.__scenarioStyleNum
	def get_scenarioParamNum(self):
		return self.__scenarioParamNum
