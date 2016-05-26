#coding=utf-8
class excel_config:
	
	def __init__(self,book,dataInput_helper):
		self.__dIn=dataInput_helper
		self.__projectFormat=book.add_format({'bold':True,'font_name':'宋体'}) 
		self.__keyFormat=book.add_format({'bold':True,'font_name':'宋体','border':1,'border_color':'black','text_wrap':True})  
		self.__ValueFormat=book.add_format({'bold':False,'font_name':'宋体','border':1,'border_color':'black','text_wrap':True}) 	
		self.__formTitle=book.add_format({'bold':True,'font_name':'宋体','border':1,'border_color':'black','bg_color':'yellow','align':'center'})                     
		self.__sheet=book.add_worksheet('config')			
	def write_project(self):
		self.__sheet.write(self.__dIn.get_projectRow(),self.__dIn.get_projectCol(),self.__dIn.get_projectTitle(),self.__projectFormat)
		self.__sheet.write(self.__dIn.get_projectRow(),self.__dIn.get_projectCol()+1,self.__dIn.get_projectName())
		self.__sheet.set_column(0,100,8)
	def write_gValue(self):
		index=0
		while 1:
			if self.__dIn.get_globalValueTitle(index)==-1:
				break
			self.__sheet.write(self.__dIn.get_globalValueRow(index),self.__dIn.get_globalValueCol(index),self.__dIn.get_globalValueTitle(index),self.__keyFormat)
			self.__sheet.write(self.__dIn.get_globalValueRow(index),self.__dIn.get_globalValueCol(index)+1,self.__dIn.get_globalValueName(index),self.__ValueFormat)
			index+=1			
	def write_lvalue(self):	
		index=0
		while 1:
			if self.__dIn.get_localValueTitle(index)==-1:
				break
			self.__sheet.merge_range(self.__dIn.get_localValueRow(index),self.__dIn.get_localValueCol(index),\
						self.__dIn.get_localValueRow(index),self.__dIn.get_localValueCol(index)+2,self.__dIn.get_localValueTitle(index),self.__formTitle)
			self.__sheet.write_column(self.__dIn.get_localValueRow(index)+1,self.__dIn.get_localValueCol(index)+0,self.__dIn.get_localValueCol0(index),self.__ValueFormat)
			self.__sheet.write_column(self.__dIn.get_localValueRow(index)+1,self.__dIn.get_localValueCol(index)+1,self.__dIn.get_localValueCol1(index),self.__ValueFormat)
			self.__sheet.write_column(self.__dIn.get_localValueRow(index)+1,self.__dIn.get_localValueCol(index)+2,self.__dIn.get_localValueCol2(index),self.__ValueFormat)
			self.__sheet.write(self.__dIn.get_localValueRow(index)+1,self.__dIn.get_localValueCol(index)+0,self.__dIn.get_localValueCol0(index)[0],self.__keyFormat)
			self.__sheet.write(self.__dIn.get_localValueRow(index)+1,self.__dIn.get_localValueCol(index)+1,self.__dIn.get_localValueCol1(index)[0],self.__keyFormat)
			self.__sheet.write(self.__dIn.get_localValueRow(index)+1,self.__dIn.get_localValueCol(index)+2,self.__dIn.get_localValueCol2(index)[0],self.__keyFormat)
			index+=1	
class excel_bw:
	def __init__(self,book,dataInput_helper):
		self.__dIn=dataInput_helper
		self.__projectFormat=book.add_format({'bold':True,'font_name':'宋体'}) 
		self.__keyFormat=book.add_format({'bold':True,'font_name':'宋体','border':1,'border_color':'black','text_wrap':True,'align':'center','valign':'vcenter','bg_color':'#006633'})  
		self.__keyFormat_ip=book.add_format({'bold':True,'font_name':'宋体','border':1,'border_color':'black','align':'center','valign':'vcenter','text_wrap':True,'bg_color':'#ffffff'})  
		self.__ValueFormat=book.add_format({'bold':False,'font_name':'宋体','border':1,'border_color':'black','align':'center','valign':'vcenter','text_wrap':True}) 
		self.__Red_ValueFormat=book.add_format({'bold':False,'font_name':'宋体','font_color':'red','border':1,'border_color':'black','text_wrap':True}) 
		self.__Red_ValueFormat_sc1=book.add_format({'bold':False,'font_name':'宋体','font_color':'red','border':1,'border_color':'black','text_wrap':True,'bg_color':'#ffffcc'}) 
		self.__Red_ValueFormat_tit=book.add_format({'bold':True,'font_name':'宋体','font_color':'black','border':1,'border_color':'black','text_wrap':True,\
								'align':'center','valign':'vcenter','bg_color':'#cccc00'}) 	
		self.__formTitle=book.add_format({'bold':True,'font_name':'宋体','border':1,'border_color':'black','bg_color':'yellow','align':'center'})    
		self.__default=book.add_format() 
		self.__cell_border=book.add_format({'border':1,'border_color':'black','text_wrap':True})                 
		self.__sheet=book.add_worksheet('BW')	
	def write_ip(self):
		i=4
		self.__sheet.write_string(3,0,'IP',self.__keyFormat)
		for ip_index in range(len(self.__dIn.get_ipStyleNumL())):
			if self.__dIn.get_ipStyleNumL()[ip_index][1]>1:
				self.__sheet.merge_range(i,0,i+self.__dIn.get_ipStyleNumL()[ip_index][1]-1,0,self.__dIn.get_ipStyleNumL()[ip_index][0],self.__keyFormat_ip)
			else:
				self.__sheet.write(i,0,self.__dIn.get_ipStyleNumL()[ip_index][0],self.__keyFormat_ip)
			#self.__sheet.set_row(i,25)
			i+=self.__dIn.get_ipStyleNumL()[ip_index][1]
	def write_mode(self):
		i=4
		self.__sheet.write_string(3,1,'Mode',self.__keyFormat)
		for mode in self.__dIn.get_mode():
			self.__sheet.write(i,1,mode,self.__ValueFormat)
			i+=1
								
	def write_param(self):
		i=4
		self.__sheet.write_string(3,2,'Param',self.__keyFormat)
		self.__sheet.set_column(2,2,15)
		for param in self.__dIn.get_param():
			self.__sheet.write(i,2,param,self.__Red_ValueFormat)
			i+=1	
	def write_input(self):
		i=4
		self.__sheet.write_string(3,3,'Input',self.__keyFormat)
		self.__sheet.set_column(3,3,15)
		for ginput_i in range(len(self.__dIn.get_input())):
			substr=[]
			formats=[]
			#rich_string=''
			substr_i=0
			for index,chars in enumerate(self.__dIn.get_input()[ginput_i]):
				if chars==','or chars=='*'or chars=='=':
					if self.__dIn.get_input()[ginput_i][substr_i:index] in self.__dIn.get_param()[ginput_i]:
						formats.append(self.__Red_ValueFormat)
					else:
						formats.append(self.__default)	
					substr.append(self.__dIn.get_input()[ginput_i][substr_i:index])
					formats.append(self.__ValueFormat)	
					substr.append(self.__dIn.get_input()[ginput_i][index:index+1])
					substr_i=index+1
				elif index==len(self.__dIn.get_input()[ginput_i])-1:
					if self.__dIn.get_input()[ginput_i][substr_i:index] in self.__dIn.get_param()[ginput_i]:
						formats.append(self.__Red_ValueFormat)
					else:
						formats.append(self.__default)
					substr.append(self.__dIn.get_input()[ginput_i][substr_i:])
			#rich_string=rich_string+formats.pop()+substr.pop()
			#print substr,formats
			
			if len(formats)==0:
				self.__sheet.write(i,3,'',self.__cell_border)
			if len(formats)==1:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],self.__cell_border)
			if len(formats)==2:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],self.__cell_border)
			if len(formats)==3:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],self.__cell_border)
			if len(formats)==4:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],self.__cell_border)
			if len(formats)==5:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],self.__cell_border)
			if len(formats)==6:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],\
								substr[5],self.__cell_border)
			if len(formats)==7:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],self.__cell_border)
			if len(formats)==8:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],self.__cell_border)
			if len(formats)==9:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],self.__cell_border)
			if len(formats)==10:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],self.__cell_border)
			if len(formats)==11:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],self.__cell_border)
			if len(formats)==12:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],\
								formats[11],substr[11],self.__cell_border)
			if len(formats)==13:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],self.__cell_border)
			if len(formats)==14:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],self.__cell_border)
			if len(formats)==15:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],self.__cell_border)
			if len(formats)==16:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],self.__cell_border)
			if len(formats)==17:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],self.__cell_border)
			if len(formats)==18:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],\
								formats[17],substr[17],self.__cell_border)
			if len(formats)==19:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],self.__cell_border)
			if len(formats)==20:
				self.__sheet.write_rich_string(i,3,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],self.__cell_border)
			i+=1	
	def write_output(self):
		i=4
		col=4
		self.__sheet.write_string(3,4,'Output',self.__keyFormat)
		self.__sheet.set_column(col,col,15)
		for goutput_i in range(len(self.__dIn.get_output())):
			substr=[]
			formats=[]
			#rich_string=''
			substr_i=0
			for index,chars in enumerate(self.__dIn.get_output()[goutput_i]):
				if chars==','or chars=='*'or chars=='=':
					if self.__dIn.get_output()[goutput_i][substr_i:index] in self.__dIn.get_param()[goutput_i]:
						formats.append(self.__Red_ValueFormat)
					else:
						formats.append(self.__default)	
					substr.append(self.__dIn.get_output()[goutput_i][substr_i:index])
					formats.append(self.__ValueFormat)	
					substr.append(self.__dIn.get_output()[goutput_i][index:index+1])
					substr_i=index+1
				elif index==len(self.__dIn.get_output()[goutput_i])-1:
					if self.__dIn.get_output()[goutput_i][substr_i:index] in self.__dIn.get_param()[goutput_i]:
						formats.append(self.__Red_ValueFormat)
					else:
						formats.append(self.__default)
					substr.append(self.__dIn.get_output()[goutput_i][substr_i:])
			#rich_string=rich_string+formats.pop()+substr.pop()
			#print substr,formats
			
			if len(formats)==0:
				self.__sheet.write(i,col,'',self.__cell_border)
			if len(formats)==1:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],self.__cell_border)
			if len(formats)==2:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],self.__cell_border)
			if len(formats)==3:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],self.__cell_border)
			if len(formats)==4:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],self.__cell_border)
			if len(formats)==5:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],self.__cell_border)
			if len(formats)==6:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],\
								substr[5],self.__cell_border)
			if len(formats)==7:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],self.__cell_border)
			if len(formats)==8:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],self.__cell_border)
			if len(formats)==9:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],self.__cell_border)
			if len(formats)==10:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],self.__cell_border)
			if len(formats)==11:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],self.__cell_border)
			if len(formats)==12:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],\
								formats[11],substr[11],self.__cell_border)
			if len(formats)==13:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],self.__cell_border)
			if len(formats)==14:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],self.__cell_border)
			if len(formats)==15:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],self.__cell_border)
			if len(formats)==16:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],self.__cell_border)
			if len(formats)==17:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],self.__cell_border)
			if len(formats)==18:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],\
								formats[17],substr[17],self.__cell_border)
			if len(formats)==19:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],self.__cell_border)
			if len(formats)==20:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],self.__cell_border)
			i+=1	
	def write_formula(self):
		i=4
		col=5
		self.__sheet.write_string(3,col,'BW Formula',self.__keyFormat)
		self.__sheet.set_column(col,col,30)
		for gformula_i in range(len(self.__dIn.get_formula())):
			substr=[]
			formats=[]
			#rich_string=''
			substr_i=0
			del_space=self.__dIn.get_formula()[gformula_i].replace(' ','')
			for index,chars in enumerate(del_space):
				if chars==','or chars=='*'or chars=='='or chars=='('or chars==')'or chars=='+'or chars=='-'or chars=='/':
					
					if del_space[substr_i:index] in self.__dIn.get_param()[gformula_i] and len(del_space[substr_i:index])>=4:
						#print del_space[substr_i:index],self.__dIn.get_param()[gformula_i]
						formats.append(self.__Red_ValueFormat)
					else:
						formats.append(self.__default)	
					substr.append(del_space[substr_i:index])
					formats.append(self.__ValueFormat)	
					substr.append(del_space[index:index+1])
					substr_i=index+1
				elif index==len(del_space)-1:
					if del_space[substr_i:index] in self.__dIn.get_param()[gformula_i]:
						formats.append(self.__Red_ValueFormat)
					else:
						formats.append(self.__default)
					substr.append(del_space[substr_i:])
			#rich_string=rich_string+formats.pop()+substr.pop()
			#print substr,formats
			
			if len(formats)==0:
				self.__sheet.write(i,col,'',self.__cell_border)
			if len(formats)==1:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],self.__cell_border)
			if len(formats)==2:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],self.__cell_border)
			if len(formats)==3:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],self.__cell_border)
			if len(formats)==4:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],self.__cell_border)
			if len(formats)==5:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],self.__cell_border)
			if len(formats)==6:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],\
								substr[5],self.__cell_border)
			if len(formats)==7:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],self.__cell_border)
			if len(formats)==8:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],self.__cell_border)
			if len(formats)==9:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],self.__cell_border)
			if len(formats)==10:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],self.__cell_border)
			if len(formats)==11:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],self.__cell_border)
			if len(formats)==12:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],\
								formats[11],substr[11],self.__cell_border)
			if len(formats)==13:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],self.__cell_border)
			if len(formats)==14:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],self.__cell_border)
			if len(formats)==15:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],self.__cell_border)
			if len(formats)==16:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],self.__cell_border)
			if len(formats)==17:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
								,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],self.__cell_border)
			if len(formats)==18:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],\
								formats[17],substr[17],self.__cell_border)
			if len(formats)==19:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],self.__cell_border)
			if len(formats)==20:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],self.__cell_border)
			if len(formats)==21:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],self.__cell_border)
			if len(formats)==22:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],self.__cell_border)
			if len(formats)==23:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],self.__cell_border)
			if len(formats)==24:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],self.__cell_border)
			if len(formats)==25:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],formats[24],substr[24],self.__cell_border)
			if len(formats)==26:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],formats[24],substr[24],formats[25],substr[25],self.__cell_border)
			if len(formats)==27:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],formats[24],substr[24],formats[25],substr[25],formats[26],substr[26],self.__cell_border)
			if len(formats)==28:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],formats[24],substr[24],formats[25],substr[25],formats[26],substr[26],formats[27],substr[27],self.__cell_border)
			if len(formats)==29:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],formats[24],substr[24],formats[25],substr[25],formats[26],substr[26],formats[27],substr[27],\
							formats[28],substr[28],self.__cell_border)
			if len(formats)==30:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],formats[24],substr[24],formats[25],substr[25],formats[26],substr[26],formats[27],substr[27],\
							formats[28],substr[28],formats[29],substr[29],self.__cell_border)
			if len(formats)==31:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],formats[24],substr[24],formats[25],substr[25],formats[26],substr[26],formats[27],substr[27],\
							formats[28],substr[28],formats[29],substr[29],formats[30],substr[30],self.__cell_border)
			if len(formats)==32:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],formats[24],substr[24],formats[25],substr[25],formats[26],substr[26],formats[27],substr[27],\
							formats[28],substr[28],formats[29],substr[29],formats[30],substr[30],formats[31],substr[31],self.__cell_border)
			if len(formats)==33:
				self.__sheet.write_rich_string(i,col,formats[0],substr[0],formats[1],substr[1],formats[2],substr[2],formats[3],substr[3],formats[4],substr[4],formats[5],substr[5],\
							       formats[6],substr[6],formats[7],substr[7],formats[8],substr[8],formats[9],substr[9],formats[10],substr[10],formats[11],substr[11]\
							,formats[12],substr[12],formats[13],substr[13],formats[14],substr[14],formats[15],substr[15],formats[16],substr[16],formats[17],substr[17],\
								formats[18],substr[18],formats[19],substr[19],formats[20],substr[20],formats[21],substr[21],formats[22],substr[22],\
							formats[23],substr[23],formats[24],substr[24],formats[25],substr[25],formats[26],substr[26],formats[27],substr[27],\
							formats[28],substr[28],formats[29],substr[29],formats[30],substr[30],formats[31],substr[31],formats[32],substr[32],self.__cell_border)
			i+=1	
	def write_scenario(self):
		
		col=6
		for sc_i in range(len(self.__dIn.get_scenarioStyleNum())):
			i=4	
			
			
			#print self.__dIn.set_scenrioParam(sc_i)
		#	if sc_i%2==0:
			#	style=self.__Red_ValueFormat_sc1
			#elif sc_i%2==1:
				#style=self.__Red_ValueFormat_sc2
			self.__sheet.write_string(3,col+sc_i,self.__dIn.get_scenarioStyleNum()[sc_i],self.__Red_ValueFormat_tit)
			self.__sheet.set_column(col+sc_i,col+sc_i,16)
			for param in self.__dIn.set_scenrioParam(sc_i):
				self.__sheet.write(i,col+sc_i,param,self.__Red_ValueFormat_sc1)
				i+=1
