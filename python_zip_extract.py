import sys, string
import zipfile, os

#info
#check namelist in .zip : zip.namelist()
#called cmd : subprocess.call(["python", "Checkdds.py", module_name + ".c", init_file + ".m", "excel_output" + .csv])

def unzip(path, zip):
  isdir = os.path.isdir 
  join = os.path.join 
  norm = os.path.normpath 

  each_cnt = 0
  
  #need password to extract file
  zip.setpassword('123456')
  
  #print zip.namelist()
  #print len(zip.namelist())
  for each in zip.namelist():
    #print each + "   " + str(each_cnt)
    #zip have folder inside
    root, name = string.split(each,"/")
    #print root
    if len(name) == 0:
      continue
    else:
      directory = norm(join(path, root)) # result is .zip name, str type
      if not os.path.exists(directory): #check folder exist
        os.makedirs(directory) #build folder
      b = open(directory + '\\' + name, 'wb') #
      b.write(zip.read(each))
      b.close()
    print (name)
    each_cnt+=1
  print ("extracting is finish")


if __name__ == '__main__':
  #sample
  #zip = zipfile.ZipFile('hide_pass.zip', 'r') #.zip only
  #unzip("", zip) #extract in same folder
  
  #user
  zip_file = input('Put zip file name to extract: ')
  program_part = os.getcwd() #get current directory path
  if zip_file == '':
    zip_file = raw_input('try input zip file name again: ')
  #zip_part = raw_input('Put zip extract part (if you extract in same folder, not put part): ')
  #if program_part[1:3] is not ':\\':
  #  print "please change program part"
  #if program_part[0] == '\\': #shared drive network
  #  input('please change program part')
  #elif program_part[0] is not ('C' and 'D' and 'E'): #only user drive
  #  input('please change program part')
  else:
    zip = zipfile.ZipFile(zip_file, 'r') #.zip only
    #unzip(zip_path,zip); #if you extract in same folder, you should put "" in path
    print (program_part)
    unzip("", zip)
    zip.close()
    input('extract zip complete!!!')
  #if zip_part == '' and program_part[1:3] == ':\\':
  #  zip_path = ''
  #elif zip_file[1:3] is not ':\\':
  #  zip_part = raw_input('Please zip file path is not in shared drive: ')
  
  
  #print zip.namelist() #check namelist in .zip
  #print len(rezipe('hide.zip'))

