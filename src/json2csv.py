import csv
import json
import os

def ReadJSON(jfld, jname):
  if jfld is None:
    jfullname = os.path.join(os.getcwd(), jname)
  else:
    jfullname = os.path.join(jfld, jname)
  if not os.path.exists(jfullname):
    raise FileNotFoundError(f'"{jfullname}" doesn\'t exist!')
  with open(jfullname, 'r') as f:
    jdict = json.load(f)
  return jdict

def ListLangs(jdict):
  return list(jdict.keys())

def ListItems(jdict, lang):
  return list(jdict[lang].keys())

def JSON2CSV(jdict):
  langs = ListLangs(jdict)
  nlangs = len(langs)
  lang = langs[0]
  items = ListItems(jdict, lang)
  ctbl = [[''] + langs]
  for item in items:
    row = [item]
    row.extend([jdict[langs[i]][item] for i in range(nlangs)])
    ctbl.append(row)
  return ctbl

def WriteCSV(ctbl, cfld, cname, overwrite=False):
  if cfld is None:
    cfullname = os.path.join(os.getcwd(), cname)
  else:
    cfullname = os.path.join(cfld, cname)
  if os.path.exists(cfullname):
    if not overwrite:
      raise FileExistsError(f'"{cfullname}" already exists!')
  with open(cfullname, 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(ctbl)
  print(f'"{cfullname}" has been successfully created!')

def main(jfld, jname, cfld, cname, overwrite=False):
  jdict = ReadJSON(jfld, jname)
  ctbl = JSON2CSV(jdict)
  WriteCSV(ctbl, cfld, cname, overwrite)

if __name__ == '__main__':
  json_folder = None
  json_file = r'data.json'
  csv_folder = None
  csv_file = r'data.csv'
  overwrite = False
  main(json_folder, json_file, csv_folder, csv_file, overwrite)

