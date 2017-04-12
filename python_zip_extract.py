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
  
  #user put zip file and zip path
  zip_file = input('Put zip file name with path to extract: ')
  if len(zip_file) == 0:
    zip_file = input('Try input zip file name again: ')
  else:
    #.zip only
    zip = zipfile.ZipFile(zip_file, 'r')
    unzip(zip_file,zip);
    zip.close()
    print ('extract zip complete!!!')

