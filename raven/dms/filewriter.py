import raven.dms.formatter as frmttr

class FileWriter:
  output_format = None
  file_name = None
  file_loc  = None
  write_file_type = "a"
  def __init__(self,format_obj):
    print 'Created FileWriter '
    self.output_format = frmttr.DataFormatter(format_obj)
    self.file_name=format_obj["file_name"]
    self.file_loc=format_obj["file_loc"]

  def write_data(self,timestamp,x,y):
    self.output_format.write_data(str(self.file_loc+"/"+self.file_name),self.write_file_type,timestamp,x,y)
   
  def write_img(self,timestamp,img):
    self.output_format.write_img(str(self.file_loc+"/"+self.file_name),timestamp,img) 
