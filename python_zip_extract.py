import sys
import string
import zipfile
import os

#info
#check namelist in .zip : zip.namelist()
#called cmd : subprocess.call(["python", "Checkdds.py", module_name + ".c", init_file + ".m", "excel_output" + .csv])

def unzip(path, zip):
  join = os.path.join 
  norm = os.path.normpath 

  #need password to extract file
  #convert password string to bype
  pwd = b"123456"
  zip.setpassword(pwd)
  
 #extract zip file with password
  for each in zip.namelist():
    #have directory in zip file
    if (each.find("/") >= 0):
      #root is directory name
      #name is file content in zip
      root, name = each.split("/")
    #have content only
    else:
      root = ""
      name = each

    if len(name) == 0: 
      continue
    else:
      #result is .zip name, str type
      directory = norm(join(zip_name, root))
      #check folder exist
      if not os.path.exists(directory):
        #build folder
        os.makedirs(directory)
      b = open(directory + "\\" + name, 'wb')
      b.write(zip.read(each))
      b.close()
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

