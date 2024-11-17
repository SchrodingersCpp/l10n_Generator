import csv
import json
import os

def ReadCSV(cfld, cname):
  if cfld is None:
    cfullname = os.path.join(os.getcwd(), cname)
  else:
    cfullname = os.path.join(cfld, cname)
  if not os.path.exists(cfullname):
    raise FileNotFoundError(f'"{cfullname}" doesn\'t exist!')
  with open(cfullname, 'r') as f:
    csv_reader = csv.reader(f)
    ctbl = []
    for row in csv_reader:
      ctbl.append(row)
  return ctbl

def ListLangs(ctbl):
  return ctbl[0][1:]

def ListItems(ctbl):
  return [ctbl[i][0] for i in range(1, len(ctbl))]

def CSV2JSON(ctbl):
  langs = ListLangs(ctbl)
  nlangs = len(langs)
  items = ListItems(ctbl)
  pdict = {lang: '' for lang in langs}
  for i in range(1, nlangs+1):
    pdict[langs[i-1]] = {items[j-1]: ctbl[j][i] for j in range(1, len(ctbl))}
  jdict = json.dumps(pdict, indent=2, ensure_ascii=False)
  return jdict

def WriteJSON(jdict, jfld, jname, overwrite=False):
  if jfld is None:
    jfullname = os.path.join(os.getcwd(), jname)
  else:
    jfullname = os.path.join(jfld, jname)
  if os.path.exists(jfullname):
    if not overwrite:
      raise FileExistsError(f'"{jfullname}" already exists!')
  with open(jfullname, 'w') as f:
    f.write(jdict)
  print(f'"{jfullname}" has been successfully created!')

def main(cfld, cname, jfld, jname, overwrite=False):
  ctbl = ReadCSV(cfld, cname)
  jdict = CSV2JSON(ctbl)
  WriteJSON(jdict, jfld, jname, overwrite)

if __name__ == '__main__':
  csv_folder = None
  csv_file = r'data.csv'
  json_folder = None
  json_file = r'out.json'
  overwrite = False
  main(csv_folder, csv_file, json_folder, json_file, overwrite)

