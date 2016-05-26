#! /usr/bin/env python
#coding=utf-8
import sys
import xlrd
import xlwt
import xlsxwriter
#sys.path.append(r'/home/D-disk/') 
from DataInput_Helper import DataInput_Helper
from DataOutput_Helper import DataOutput_Helper
from rewrite_excel import excel_config
from rewrite_excel import excel_bw
from xlutils.copy import copy
from copy import deepcopy

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
	
			
class readexcel:

	def __init__(self,filename='scenario3.xls'):
		self.__filename__=filename
		self.__book__=xlrd.open_workbook(filename,formatting_info=True)
		self.__sheetnames__=[]#sheet名字
		dataIn=DataInput_Helper()
		for i in self.__book__.sheet_names():
			if i.lower()=='config'or i.lower()=='bw':
				sheet=self.__book__.sheet_by_name(i)
				for row in range(0,sheet.nrows):
					for col in range(0,sheet.ncols):
		                ###-----------读取config参数---------------------------
						if sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='project':
							dataIn.set_project(('Project',(row,col),sheet.cell_value(row,col+1)))#(NAME,row,col,projectName)
						elif sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='#key':
							for key_row in range(row+1,sheet.nrows):
								#if sheet.cell_value(key_row,col)!='':
								if sheet.cell_type(key_row,col+1)==xlrd.XL_CELL_TEXT:
									dataIn.set_globalValue((sheet.cell_value(key_row,col),(key_row,col),sheet.cell_value(key_row,col+1)))
					                        elif sheet.cell_type(key_row,col+1)==xlrd.XL_CELL_NUMBER:
									dataIn.set_globalValue((sheet.cell_value(key_row,col),(key_row,col),\
									       DataOutput_Helper.float_to_int(sheet.cell_value(key_row,col+1))))
								#elif sheet.cell_value(key_row,col)=='':
									#dataIn.set_globalValue((sheet.cell_value(key_row,col),(key_row,col),'NA'))
						elif sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='#form':
							#读取表格参数formx 自动判定宽度和高度
							formx_width=1
							formx_height=1
							col0=[]
							col1=[]
							col2=[]
							for formx_col in range(col,sheet.ncols):
								if sheet.cell_value(row+2,formx_col)=='':
									formx_width=formx_col-col
									break
								elif formx_col==sheet.ncols-1:
									formx_width=formx_col-col+1
							for formx_row in range(row+3,sheet.nrows):
								if sheet.cell_value(formx_row,col)=='':
									formx_height=formx_row-row
									break
								elif formx_row==sheet.nrows-1:
									formx_height=formx_row-row		

								if sheet.cell_value(formx_row,col)!='':
									col0.append(sheet.cell_value(formx_row,col))
									col1.append(DataInput_Helper.float_to_int(sheet.cell_value(formx_row,col+1)))
									col2.append(sheet.cell_value(formx_row,col+2))
							dataIn.set_localValue((sheet.cell_value(row+1,col),(row+1,col),\
							       sheet.cell_value(row+2,col),\
						               col0,\
							       sheet.cell_value(row+2,col+1),\
							       col1,\
							       sheet.cell_value(row+2,col+2),\
							       col2))#form title,module,note,ms
				###-----------读取BW参数---------------------------
						elif sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='ip':	
							ip=[]
							i=0
							for r in range(row+1,sheet.nrows):
								if sheet.cell_value(r,col)=='':
									ip.append(ip[i-1])
									dataIn.set_ipValue(ip[i-1])
								else:
									ip.append(sheet.cell_value(r,col))
									dataIn.set_ipValue(sheet.cell_value(r,col))
								i+=1	
						elif sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='mode':
							for r in range(row+1,sheet.nrows):
								if sheet.cell_value(r,col)=='':
									dataIn.set_mode('NA')
								else:
									dataIn.set_mode(int(sheet.cell_value(r,col)))
						elif sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='param':
							for r in range(row+1,sheet.nrows):
									if sheet.cell_value(r,col)=='':
										dataIn.set_param(' ')
									else:
										dataIn.set_param(sheet.cell_value(r,col))
										
						elif sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='input':
							for r in range(row+1,sheet.nrows):
								if sheet.cell_value(r,col)=='':
									dataIn.set_input('NA')
								else:
									dataIn.set_input(sheet.cell_value(r,col))		
						elif sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='output':
							for r in range(row+1,sheet.nrows):
								if sheet.cell_value(r,col)=='':
									dataIn.set_output('NA')
								else:
									dataIn.set_output(sheet.cell_value(r,col))			 					
						elif sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='bw formula':	
							for r in range(row+1,sheet.nrows):
								if sheet.cell_value(r,col)=='':
									dataIn.set_formula('NA')
								else:
									dataIn.set_formula(sheet.cell_value(r,col))
						elif sheet.cell_type(row,col)==xlrd.XL_CELL_TEXT and sheet.cell_value(row,col).lower()=='#sce':
							for c in range(col,sheet.ncols):
								if sheet.cell_value(row+1,c)!='':
									param=[]						
									for r in range(row+2,sheet.nrows):	 					
											param.append(sheet.cell_value(r,c))
					                                dataIn.set_scenario(sheet.cell_value(row+1,c),param)               
							
			
	
		#******************************绘制表格**************************************************************#
		#********Scenario*********************#
		dataIn.set_ipStyleNum()
		dataIn.set_scenarioStyleNum()
		dataIn.set_scenarioParamNum()
		workbook=xlsxwriter.Workbook('xxxxx.xlsx')
                config=excel_config(workbook,dataIn)
		config.write_gValue()
		config.write_project()
		config.write_lvalue()
		bww=excel_bw(workbook,dataIn)
		bww.write_ip()
		bww.write_mode()
		bww.write_param()
		bww.write_input()
		bww.write_output()
		bww.write_formula()
		bww.write_scenario()
		bg_brown=workbook.add_format({'bold':False,'font_name':'宋体','border':1,'border_color':'black','text_wrap':True,'align':'center','valign':'vcenter','bg_color':'#999933'}) 
		bg_yellow=workbook.add_format({'bold':False,'font_name':'宋体','border':1,'border_color':'black','text_wrap':True,'align':'center','valign':'vcenter','bg_color':'#ffffcc'})
		bg_white=workbook.add_format({'bold':False,'font_name':'宋体','border':1,'border_color':'black','text_wrap':True,'align':'center','valign':'vcenter','bg_color':'#ffffff'}) 
		bg_grey=workbook.add_format({'bold':False,'font_name':'宋体','border':1,'border_color':'black','text_wrap':True,'align':'center','valign':'vcenter','bg_color':'#cccccc'}) 
		bg_green_title=workbook.add_format({'bold':True,'font_name':'宋体','border':1,'border_color':'black','text_wrap':True,'align':'center','valign':'vcenter','bg_color':'#339966'}) 
		bg_purple_title=workbook.add_format({'bold':True,'font_name':'宋体','border':1,'border_color':'black','text_wrap':True,'align':'center','valign':'vcenter','bg_color':'#996699'}) 
		'''self.__Wbook__=copy(self.__book__)
		xlwt.add_palette_colour('style1',22)
		self.__Wbook__.set_colour_RGB(22,189,183,107)
		xlwt.add_palette_colour('style2',23)
		self.__Wbook__.set_colour_RGB(23,25,25,112)
		xlwt.add_palette_colour('style3',24)
		self.__Wbook__.set_colour_RGB(24,240,230,140)
		style1 = xlwt.easyxf('pattern: pattern solid, fore_colour style1,back_colour black;'
					      'font: colour style2, bold True;'
						'borders: left 0x0d , right 0x0d, top 0x0d, bottom 0x0d;'
						'alignment: horz center,vert center')
		style2 = xlwt.easyxf(
					      'font: colour style2, bold False;'
						'borders: left 0x0d,left_colour black , right 0x0d, top 0x0d, bottom 0x0d;'
						'alignment: horz center,vert center')
		style3 = xlwt.easyxf('pattern: pattern solid, fore_colour style3,back_colour black;'
					      'font: colour style2, bold True;'
						'borders: left 0x0d , right 0x0d, top 0x0d, bottom 0x0d;'
						'alignment: horz center,vert center')
		style4 = xlwt.easyxf('pattern: pattern solid, fore_colour green,back_colour black;'
					      u'font: colour black,height 250,name 宋体;'
						'borders: left 0x0d , right 0x0d, top 0x0d, bottom 0x0d;'
						'alignment: horz center,vert center')
		style5 = xlwt.easyxf(
					      u'font: colour black,height 215,name 宋体;'
						'borders: left 0x0d , right 0x0d, top 0x0d, bottom 0x0d;'
						'alignment: horz center,vert center')
		style6 = xlwt.easyxf(
					      u'font: colour black,height 205,name 宋体;'
						'borders: left 0x0d , right 0x0d;'
						'alignment: horz center,vert center')
		style7 = xlwt.easyxf(
					      u'font: colour black,height 205,name 宋体;'
						'borders: left 0x0d , right 0x0d,bottom 0x0d;'
						'alignment: horz center,vert center')
		style8 = xlwt.easyxf('pattern: pattern solid, fore_colour orange;'
					      u'font: colour black,height 215,name 宋体;'
						'borders: left 0x0d , right 0x0d, top 0x0d, bottom 0x0d;'
						'alignment: horz center,vert center')
		dataIn.set_ipStyleNum()
		dataIn.set_scenarioStyleNum()
		dataIn.set_scenarioParamNum()'''
		bw=DataOutput_Helper(dataIn)
		
		
		for scen_name in bw.get_scen_name():#scen
			sheet=workbook.add_worksheet(scen_name)
			
			#构建表格，构建固定位置内容
			sheet.write(0,0,'Scenario\n'+scen_name,bg_brown)
			sheet.set_row(0,40)
			#sheet.row(0).height=700
			sheet.set_column(0,0,15)
			#sheet.col(0).width=7000
			sheet.set_column(2,2,70)
			#sheet.col(2).width=17000  #BW formula
			sheet.set_column(3,3,10)
			#sheet.col(3).width=4000
			sheet.set_column(4,4,15)
			#sheet.col(4).width=7000
			sheet.merge_range(0,1,0,6,'BW Requirement',bg_brown)
			
			
			sheet.write(1,1,'Master',bg_brown)
			sheet.merge_range(1,2,1,3,'BW(MB/s)',bg_brown)
			sheet.write(1,5,'Master',bg_brown)
			sheet.write(1,6,'BW(MB/s)',bg_brown)
			
			index=0
			data=bw.get_data_by_index(scen_name)
			#print data
			for num in range(bw.get_data_num(scen_name)):
				total=0			
				#sheet.row(2+num).height=800
				for irow in range(num+1):
					sheet.write(2+irow,1,data[irow][0],bg_yellow)
					data_r=data[irow][1].replace('*','x')
					#print data[irow][1]
					sheet.write(2+irow,2,data_r,bg_yellow)
					sheet.write(2+irow,3,round(eval('1.0*'+data[irow][1]),3),bg_yellow)
					total+=eval(data[irow][1])
					#print total
					sheet.write(2+irow,5,'',bg_yellow)
					sheet.write(2+irow,6,'',bg_yellow)	
			sheet.merge_range(1,0,bw.get_data_num(scen_name)+2,0,bw.get_project_name()+'\n estimate \nBW(MB/s)',bg_white)
			sheet.merge_range(1,4,bw.get_data_num(scen_name)+2,4,bw.get_project_name()+'\n simulation \nBW(MB/s)',bg_white)	
			#填写Total	
			for t in [1,5]:
				sheet.write(bw.get_data_num(scen_name)+2,t,'Total',bg_yellow)
				sheet.write(bw.get_data_num(scen_name)+2,t+1,'',bg_yellow)
			#sheet.row(bw.get_data_num(scen_name)+2).height=600
			sheet.write(bw.get_data_num(scen_name)+2,3,round(total,3),bg_yellow)#计算总和
			
		
		#************************master************************************#
		sheet=workbook.add_worksheet('Master')
		sheet.set_column(1,2,15)
		sheet.set_column(3,3,20)
		sheet.set_column(4,4,90)
		
		#sheet.col(1).width=6000
		#sheet.col(2).width=6000
		#sheet.col(3).width=8000
		#sheet.col(4).width=26000
		m=0
		i=3
		j=3
		sheet.set_row(2,25)
		for n in [u'Master',u'Owner',u'Freq(MHz)',u'编号',u'Log名称']:
			sheet.write(2,m,n,bg_green_title)
			m+=1
		for index in bw.get_ipStyle():
			log=bw.retrieval_log_by_ip(index)
		#	print log
			rg=len(log)-1
			print rg
			#print i,i+rg,index
		#	sheet.write_merge(i,i+rg,0,0,index,bg_white)
			if rg>0:
				sheet.merge_range(i,0,i+rg,0,index,bg_white)
			else:
				sheet.write(i+rg,0,index,bg_white)
			for num in range(len(log)):
				if num==len(log)-1:
					sheet.write(j,4,log[num][3],bg_grey)
					sheet.write(j,3,'Scen_'+index+'_Log_'+'%02d'%num,bg_grey)
					bw.add_info_to_log(log[num],'Scen_'+index+'_Log_'+'%02d'%num)
					sheet.write(j,2,'',bg_grey)
					sheet.write(j,1,'',bg_grey)
				else:
					sheet.write(j,4,log[num][3],bg_grey)
					sheet.write(j,3,'Scen_'+index+'_Log_'+'%02d'%num,bg_grey)
					bw.add_info_to_log(log[num],'Scen_'+index+'_Log_'+'%02d'%num)
					sheet.write(j,2,'',bg_grey)
					sheet.write(j,1,'',bg_grey)
				sheet.set_row(j,18)
				j+=1
			i+=rg+1
		
		#*******************Scenario*******************************************#
		#sheet=self.__Wbook__.add_sheet('Scenario',cell_overwrite_ok=True)
		sheet=workbook.add_worksheet('Scenario')
		sheet.set_column(0,0,20)
		sheet.set_column(2,2,20)
		sheet.set_column(3,3,90)
	#	sheet.col(0).width=10000
		#sheet.col(2).width=8000
		#sheet.col(3).width=26000
		m=0
		i=3
		j=3
		sheet.set_row(2,25)
		for n in [u'Scenario',u'Master',u'Log ID',u'Log Name']:
			sheet.write(2,m,n,bg_purple_title)
			m+=1
		for index in bw.get_scen_name():
			log=bw.retrieval_log_by_scen(index)
			#print log
			rg=len(log)-1
			#print i,i+rg,index
		#	sheet.write_merge(i,i+rg,0,0,index,bg_white)
			if rg>0:
				sheet.merge_range(i,0,i+rg,0,index,bg_white)
			else:
				sheet.write(i+rg,0,index,bg_white)
			#sheet.merge_range(i,0,i+rg,0,index,bg_white)
			for num in range(len(log)):
				
				if num==len(log)-1:
					if log[num][1]>=2:
						sheet.write(j,1,log[num][0]+' '+str(int(log[num][1])),bg_grey)
						sheet.write(j,2,log[num][4],bg_grey)
						sheet.write(j,3,log[num][3],bg_grey)
					else:
						sheet.write(j,1,log[num][0],bg_grey)
						sheet.write(j,2,log[num][4],bg_grey)
						sheet.write(j,3,log[num][3],bg_grey)
				else:
					if log[num][1]>=2:
						sheet.write(j,1,log[num][0]+' '+str(int(log[num][1])),bg_grey)
						sheet.write(j,2,log[num][4],bg_grey)
						sheet.write(j,3,log[num][3],bg_grey)
					else:
						sheet.write(j,1,log[num][0],bg_grey)
						sheet.write(j,2,log[num][4],bg_grey)
						sheet.write(j,3,log[num][3],bg_grey)
				sheet.set_row(j,18)
				j+=1
			i+=rg+1
	
		#self.__Wbook__.save(filename)
		workbook.close()
		
n=readexcel()


