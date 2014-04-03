import raven.dms.filereader as fr
import raven.dms.amqplistener as amqp
import raven.dms.decoder as dec
import raven.dms.filewriter as fw

##
# This is the Main Class for the Data Management system.
# This class reads in a json config file and creates
# a pipeline to process data from the AMQP broker
# and output as a HDF5 file
#
class DMS:
  cfg_data = None
  amqp_ptr = []
  def __init__(self,cfg_json):
    print 'DMS is initializing 1'
    self.cfg_data = fr.FileReader().gethandle(cfg_json);
    amqp_addr=self.cfg_data["amqp_address"]
    amqp_exchange=self.cfg_data["amqp_exchange"]
    amqp_exchange_type=self.cfg_data["amqp_exchange_type"]
    datastreams = self.cfg_data["data_streams"]

    ds_factory=DataStreamFactory();
    for ds in datastreams:
      topic_key=ds["amqp_topic_key"]
      data_src_name=ds["data_src_name"]
      stream_enc=ds["stream_encoding"]
      file_format_obj=ds["output_file_format"]
      file_wrtr=ds_factory.createFileWriter(file_format_obj)
      data_decoder=ds_factory.createDecoder(stream_enc,file_wrtr)
      amqp_src=ds_factory.createAMQPListener(amqp_addr,amqp_exchange,amqp_exchange_type,topic_key,data_src_name,data_decoder)
      self.amqp_ptr.append(amqp_src)
      
class DataStreamFactory:
  def __init__(self):
    print 'created the Data stream factory'

  def createDecoder(self,stream_enc,file_wrtr):
    decoder=dec.DataDecoder(stream_enc,file_wrtr)
    return decoder

  def createAMQPListener(self,amqp_addr,amqp_exchange,amqp_exchange_type,topic_key,data_src_name,data_decoder):  
    amqp_list=amqp.AMQPListener(amqp_addr,amqp_exchange,amqp_exchange_type,topic_key,data_src_name,data_decoder)
    return amqp_list

  def createFileWriter(self,file_format_obj):
    file_wtr=fw.FileWriter(file_format_obj)
    return file_wtr


      
