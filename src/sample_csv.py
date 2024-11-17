import json2csv

'''Create a dummy CSV file to show the expected CSV file structure.'''

def CreateDummyJSON():
  jdict = {'en':
           {'Hello.msg': 'Hello!',
            'Start.btn': 'Start',
            'Continue.btn': 'Continue',
            'Exit': 'Exit'},
           'uk':
           {'Hello.msg': 'Вітаємо!',
            'Start.btn': 'Почати',
            'Continue.btn': 'Продовжити',
            'Exit': 'Вихід'}}
  return jdict

def main(cfld, cname, overwrite=False):
  jdict = CreateDummyJSON()
  ctbl = json2csv.JSON2CSV(jdict)
  json2csv.WriteCSV(ctbl, cfld, cname, overwrite)

if __name__ == '__main__':
  csv_folder = None
  csv_file = r'data.csv'
  overwrite = False
  main(csv_folder, csv_file, overwrite)

