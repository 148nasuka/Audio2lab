import os
import shutil
import subprocess

if not os.path.exists("../Data_in"):
    os.mkdir("../Data_in")
    print("Data_in : set")
if not os.path.exists("../Data_out"):
    os.mkdir("../Data_out")
    print("Data_out : set")
if not os.path.exists("../Data_out/error"):
    os.mkdir("../Data_out/error")
    print("Data_out/error : set")
if not os.path.exists("../Music2lab/lab_out"):
    os.mkdir("../Music2lab/lab_out")
    print("Music2lab/lab_out : set")
if not os.path.exists("../Music2lab/xml_in"):
    os.mkdir("../Music2lab/xml_in")
    print("Music2lab/xml_in : set")
if not os.path.exists("../temp"):
    os.mkdir("../temp")
    print("temp : set")
if not os.path.exists("../temp/convert"):
    os.mkdir("../temp/convert")
    print("temp/convert : set")
if not os.path.exists("../temp/downscaling"):
    os.mkdir("../temp/downscaling")
    print("temp/downscaling : set")

print("\n************************************************\n" + \
      "Vocal2labに必要なライブラリをインストールします" + \
      "\n************************************************\n")

subprocess.check_output(["pip3", "install", "-r", "requirements.txt"], cwd="./")

print("\n**********************************************\n" + \
      "pysinsy 音素辞書ファイルの確認をします"
      "\n**********************************************\n")

import pysinsy

sinsy_location = str(pysinsy.__file__)
dic_location = sinsy_location.replace("__init__.py", "_dic")
if not os.path.exists(dic_location):
    os.mkdir(dic_location)
copy_location = "./Sinsy_dic"

if os.path.exists(dic_location):
    print("pysinsy インストール先 : " + dic_location)
    if os.path.isfile(dic_location + "\japanese.euc_jp.conf"):
        print("japanese.euc_jp.conf : check")
    else:
        shutil.copy(copy_location + "\japanese.euc_jp.conf", dic_location + "\japanese.euc_jp.conf")
        print("japanese.euc_jp.conf : set")

    if os.path.isfile(dic_location + "\japanese.euc_jp.table"):
        print("japanese.euc_jp.table : check")
    else:
        shutil.copy(copy_location + "\japanese.euc_jp.table", dic_location + "\japanese.euc_jp.table")
        print("japanese.euc_jp.table : set")

    if os.path.isfile(dic_location + "\japanese.shift_jis.conf"):
        print("japanese.shift_jis.conf : check")
    else:
        shutil.copy(copy_location + "\japanese.shift_jis.conf", dic_location + "\japanese.shift_jis.conf")
        print("japanese.shift_jis.conf : set")

    if os.path.isfile(dic_location + "\japanese.shift_jis.table"):
        print("japanese.shift_jis.table : check")
    else:
        shutil.copy(copy_location + "\japanese.shift_jis.table", dic_location + "\japanese.shift_jis.table")
        print("japanese.shift_jis.table : set")

    if os.path.isfile(dic_location + "\japanese.utf_8.conf"):
        print("japanese.utf_8.conf : check")
    else:
        shutil.copy(copy_location + "\japanese.utf_8.conf", dic_location + "\japanese.utf_8.conf")
        print("japanese.utf_8.conf : set")

    if os.path.isfile(dic_location + "\japanese.utf_8.table"):
        print("japanese.utf_8.table : check")
    else:
        shutil.copy(copy_location + "\japanese.utf_8.table", dic_location + "\japanese.utf_8.table")
        print("japanese.utf_8.table : set")

    if os.path.isfile(dic_location + "\japanese.macron"):
        print("japanese.macron : check")
    else:
        f = open(dic_location + "\japanese.macron", "w")
        f.close()
        print("japanese.macron : set")

else:
    print("pysinsy のインストールに失敗している可能性があります\nライブラリの再インストールをしてください")

print("\n*****************\n" + \
      "インストール完了"
      "\n*****************\n")
