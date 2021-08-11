#!/usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
  color: black;
  font-weight: bold;
  font-size: 20px;
}
</style>
''')

import subprocess as sb
import cgi

fs = cgi.FieldStorage()

plate_no = fs.getvalue("plate_no")


if plate_no == "KL 65 K 5455":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : TUSHAR JOSHI
    License No : 341256890218
    Make / Model : FIAT / JEEP
    Registration Date : 1/14/2010
    Registering Authority : KERALA , INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 3/15/2023
    Fitness Upto : 5/10/2032
    </pre>''')
    print("</body>")

elif plate_no == "KA 64 N 0099":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : SURAJ WARBHE
    License No : 923145659012
    Make / Model : VOLKSWAGEN GROUP / SKODA RAPID
    Registration Date : 2/12/2015
    Registering Authority : KARNATAKA, INDIA
    Vehicle Class : MCWG
      Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2025
    Fitness Upto : 5/10/2032
    </pre>''')
    print("</body>")

elif plate_no == "GJ 1HX 7047":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : GANESH BHANGE
    License No : 125638905631
    Make / Model : AUDI / Q7
    Registration Date : 1/12/2016
    Registering Authority : GUJARAT, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2026
    Fitness Upto : 5/10/2032
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No Infomration available for this number...")
    print("</body>")
                                   
