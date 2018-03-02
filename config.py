import csv

class config():
  def __init__(self):
    self.orange_paths = []
    self.seminole_paths = []
    self.alachua_paths = []
    self.records = []
    
  def add_orange(self, path):
    self.orange_paths.append(path)
    self.import_orange()
    
  def add_seminole(self, path):
    self.seminole_paths.append(path)
    self.import_seminole()
    
  def add_alachula(self, path):
    self.alachua_paths.append(path)
    
  def import_orange(self):
    for path in self.orange_paths:
      record = open(path)
      record_r = record.readlines()
      record.close()
      for row in record_r:
	entry_dic = {}
	entry_dict = {}
	entry_dict['regnum'] = row[0:8].rstrip()
	entry_dict['county'] = row[9:16].rstrip()
	entry_dict['fName'] = row[17:34].rstrip()
	entry_dict['mName'] = row[35:52].rstrip()
	entry_dict['lName'] = row[53:74].rstrip()
	entry_dict['party'] = row[75:79].rstrip()
	entry_dict['birthDate'] = row[80:91].rstrip()
	entry_dict['sex'] = row[92:94].rstrip()
	self.records.append(entry_dict)
	
	
  def import_seminole(self):
    for path in self.seminole_paths:
      record = open(path)
      record_r = record.readlines()
      record.close()
      for row in record_r:
	entry = row.split('\t')
	entry_dict = {}
	entry_dict['regnum'] = entry[0]
	entry_dict['county'] = entry[1]
	entry_dict['fName'] = entry[2]
	entry_dict['mName'] = ""
	entry_dict['lName'] = entry[3]
	entry_dict['party'] = entry[4]
	entry_dict['birthDate'] = entry[5]
	entry_dict['sex'] = entry[6].rstrip()
	#print("{}, {}".format(row, entry_dict))
	self.records.append(entry_dict)
	
  def import_alachua(self):
    for path in self.alachua_paths:
      with open(path) as record:
	reader = csv.DictReader(record)
	for row in reader:
	  entry_dict = {}
	  entry_dict['regnum'] = row['regnum']
	  entry_dict['county'] = row['county']
	  entry_dict['fName'] = row['first']
	  entry_dict['mName'] = row['middle']
	  entry_dict['lName'] = row['last']
	  entry_dict['party'] = row['party']
	  entry_dict['birthDate'] = row['bdate']
	  entry_dict['sex'] = row['sex']
	  #print("{}, {}".format(row, entry_dict))
	  self.records.append(entry_dict)
  
  def write_csv(self):
      writer = csv.DictWriter(open('voters.csv', 'wb'), delimiter='\t', fieldnames=['regnum', 'county', 'fName', 'mName', 'lName', 'party', 'birthDate', 'sex'])
      writer.writeheader()
      for record in self.records:
	writer.writerow(record)
		 
	  