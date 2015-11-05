import re
import sys
def get_regex_dic(file_lines):
	flag=0
	dic={}
	for line in file_lines:
		if line == '%%':
			if flag:
				return dic
			else:
				flag = 1
				continue
		if flag:
			words=line.split('=',1)
			dic[words[0]]=words[1]

def get_command_dic(file_lines):
	flag=0
	dic={}
	for line in file_lines:
		if line == '%%':
			flag+=1
			continue
		if flag == 2:
			words=line.split('{')
			dic[words[0].strip()]=words[1][:-1].strip()
	if flag == 3:
		return dic

def print_tokens(marking_list):
	for item in marking_list:
		if item:
			print item.strip(),

def get_marking_list(input_file_string,regex_dic):
	marking_list=[None]*len(input_file_string)
	for key in regex_dic:
		regex_result=re.finditer(regex_dic[key],input_file_string)
		indices=[m.start(0) for m in regex_result]
		for index in indices:
			marking_list[index]=key
	return marking_list

def generate_token_command_script(marking_list,command_dic,preprocessor_directives,input_file_name):
	script_file_name=input_file_name.split('.')[0]+"_analyzer.py"
	script_file=open(script_file_name,"w")
	for item in preprocessor_directives:
		script_file.write(item+"\n")
	for item in marking_list:
		if item:
			script_file.write(command_dic[item]+"\n")
	script_file.close()

def get_preprocessor_directives(file_lines):
	flag=0
	preprocessor_directives=[]
	for line in file_lines:
		if line == '%%':
			return preprocessor_directives
		if flag == 0:
			preprocessor_directives.append(line)
	return preprocessor_directives

def main():
	if len(sys.argv)-1:
		print "here"
		i=0
		while(i<len(sys.argv)-1):
			if sys.argv[i] == '-l':
				lex_file_name=sys.argv[i+1]
				i=i+2
			if sys.argv[i] == '-f':
				input_file_name=sys.argv[i+1]
				i=i+2
			i=i+1
	else:
		lex_file_name="pylex-trial.lex"
		input_file_name="input.txt"
	
	lex_file=open(lex_file_name,"r")
	file_lines=lex_file.read().splitlines()
	regex_dic=get_regex_dic(file_lines)
	command_dic=get_command_dic(file_lines)
	input_file_lines=open(input_file_name,"r").read().splitlines()
	input_file_string='!'.join(input_file_lines)
	marking_list=get_marking_list(input_file_string,regex_dic)
	command_dic=get_command_dic(file_lines)
	preprocessor_directives=get_preprocessor_directives(file_lines)
	generate_token_command_script(marking_list,command_dic,preprocessor_directives,input_file_name)

if __name__ == "__main__":
	main()