#!/usr/bin/python3
'''
PyNav - Directory traversal management module for python3 (Linux)
Author: Jacques "Lawrenz" Fernandes

TL;DR version of code:
 - See __main__ at bottom for example of usage
 - init flags:
  - root : path string (if blank, will take current directory as root)
  - verbose : if set (True) the code will be, well, verbose... (pretty obvious, isn't it?)
'''


import os;

class DirectoryNavigator:
	
	def __init__(self,root=os.getcwd(),verbose=False):
		self.root = root+"/";
		self.verbose = verbose;
		self.print("Root : "+self.root);
		self.dir_stack = list();
		self.print("Dir stack initialized...");
		self.print("starting...");
		#self.cd(root);
		
	def print(self,msg,**args):
		if self.verbose:
			print(msg,**args);
	
	def cd(self,path):
		path=path.strip(" ").rstrip("/");
		path_set = path.split("/");
		for loc in path_set:
			if loc == "..":
				if len(self.dir_stack) > 0:
					self.dir_stack.pop();
				else:
					self.print(" :: ERROR: Cannot go above set root...");
			else:
				dir_list = os.listdir();
				if loc in dir_list:
					self.dir_stack.append(loc);
					self.print("moved to ",end="");
					self.print_path();
					self.print("");
				else:
					self.print(" :: ERROR: Not a valid Directory...");
	
	
	def print_path(self):
		path_string = self.root;
		for loc in self.dir_stack:
			path_string+=loc+"/";
		self.print(path_string);
	
	def prompt(self):
		self.print_path();
		new_path = input(" -> ");
		self.cd(new_path);
				
if __name__ == "__main__":
	nav = DirectoryNavigator(verbose=True);
	try:
		while True:
			nav.prompt();
	except KeyboardInterrupt:
		print("\nExiting...");
