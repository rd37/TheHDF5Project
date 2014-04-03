import subprocess
import h5py
import numpy as np

class DataFormatter:
  formatter = None
  def __init__(self,data_type):
    print 'Created Data Formater ',data_type
    if data_type["type"] == 'hdf5':
      self.formatter=HDF5Format(data_type["hdf5_key"])
    elif data_type["type"] == 'binary':
      self.formatter=BinaryFormat()
    elif data_type["type"] == 'text':
      self.formatter=TextFormat()

  def write_data(self,file_name,write_access,timestamp,x,y):
    self.formatter.write_data(file_name,write_access,timestamp,x,y)

  def write_img(self,file_name,timestamp,img):
    self.formatter.write_img(file_name,timestamp,img)

class HDF5Format:
  hdf5_key = None
  file = None

  def __init__(self,hdf5_key):
    print 'HDF5 Formatter Created ',hdf5_key
    self.hdf5_key=hdf5_key

  def write_data(self,file_name,write_access,timestamp,x,y):
    if self.file is None:
        self.file=h5py.File( file_name,'w' )
    grp = None
    if self.hdf5_key in self.file:
        grp = self.file[self.hdf5_key]
    else:
        grp = self.file.create_group(self.hdf5_key)
    subgrp = grp.create_group(str(timestamp) )
    dsetx = subgrp.create_dataset( 'x' , ( len(x) ,  ) , dtype='f' ) 
    dsety = subgrp.create_dataset( 'y' , ( len(y) ,   ) , dtype='f' ) 
    
    dsetx[:] = x
    dsety[:] = y

  def write_img(self,file_name,timestamp,img):
    if self.file is None:
        self.file=h5py.File( file_name,'w' )
    grp = None
    if self.hdf5_key in self.file:
        grp = self.file[self.hdf5_key]
    else:
        grp = self.file.create_group(self.hdf5_key)
    print 'create timestamp sub group ',str(timestamp)
    try:
      subgrp = grp.create_group(str(timestamp) )
      dt=h5py.special_dtype(vlen=bytes)
      dsetimg = subgrp.create_dataset( 'png_img' , ( len(img)   ) , dtype=dt )
      #dsetimg[:] = np.void( img )
      dsetimg[i] = np.void(img)
      print 'image persisted!',len(img)
    except Exception:
      print 'exception occured'
      pass

class BinaryFormat:  
  def __init__(self):
    print 'Binary Formatter Created'

  def write_data(self,data):
    print 'Writing Binary Data'

class TextFormat:
  def __init__(self):
    print 'Text Formatter Created'

  def write_data(self,file_name,write_access,timestamp,x,y):
    file=open(file_name,write_access)
    file.write("    "+str(timestamp)+" \n")
    file.write("                x "+str(x)+"\n")
    file.write("                y "+str(y)+"\n")
    file.write("\n\n")
    file.close()

