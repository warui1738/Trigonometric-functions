# the python pythogras system
import math
def area():
  '''This calculates the area of the triangle that is using the pythagoras theroem'''
  a = int(input("Please enter  a:"))
  b= int(input("Please enter b:"))
  # c= int(input("Please enter c:"))
  AreaAns = 1/2 *(b*a)
  print("The area is {}".format(AreaAns))

def findmissingPart():
  """This now calculates and finds out the missing part either the part a b or c """
  Missingpoint = str(input("Please enter the missing part either a ,b,c"))

  if Missingpoint == "a":
    b= int(input("Please enter b:"))
    c= int(input("Please enter c:"))
    a = math.sqrt(math.pow(c,2) - math.pow(b,2))
    print("The missing part a is {}".format(a))
  elif Missingpoint =="b":
    a= int(input("Please enter a:"))
    c= int(input("Please enter c:"))
    b = math.sqrt(math.pow(c,2) - math.pow(a,2))
    print("The missing part b is {}".format(b))
  elif Missingpoint == "c":
    a= int(input("Please enter a:"))
    b= int(input("Please enter b:"))
    c = math.sqrt(math.pow(a,2) + math.pow(b,2))
    print("The missing part c is {}".format(c))

def sinRule():
  '''This is aprogram that deals with working with the sin rule to get the missing angle
  or the missing value part SINRULE  = a/sin(a)=b/sin(b)=c/sin(c)'''
  def getMissingpart():
    MissingValue = str(input("Please enter the missing value part\neither a ,b or c:"))
    if MissingValue == "a":
      Angle = int(input("Please enter the angle of side a:"))
      b = int(input("Please enter the value of side b:"))
      Bngle = int(input("Please enter the angle  of side b:"))
      a = (math.sin(Angle) * b) / math.sin(Bngle)
      print("The value of missingpart {} is {}".format(MissingValue,a))
    elif MissingValue == "b":
      Angle = int(input("Please enter the angle of side a:"))
      b= int(input("Please enter the value of side a:"))
      Bngle = int(input("Please enter the angle  of side b:"))
      b = (math.sin(Bngle) * a) / math.sin(Angle)
      print("The value of missingpart {} is {}".format(MissingValue,b))
    elif MissingValue == "c":
      Angle = int(input("Please enter the angle of side a:"))
      a = int(input("Please enter the value of side a:"))
      Cngle = int(input("Please enter the angle  of side c:"))
      c = (math.sin(Cngle) * a) / math.sin(Angle)
      print("The value of missingpart {} is {}".format(MissingValue,c))
  def getMissingAngle():
    MissingAngle = str(input("Please enter the name of the missing side\n either a,b,c:"))
    if MissingAngle == "a":
      a = int(input("Please enter the value of side a:"))
      b= int(input("Please enter the value of side b:"))
      Bngle = int(input("Please enter the angle of side a:"))
      Angle= math.sinh((math.sin(Bngle) * a) / b)
      print("The Angle of missingpart {} is {}".format(MissingAngle,Angle))
    elif MissingAngle == "b":
      b = int(input("Please enter the value of side b:"))
      a = int(input("Please enter the value of side a:"))
      Angle = int(input("Please enter the angle of side a:"))
      Bngle= math.sinh((math.sin(Angle) * b) / a)
      print("The Angle of missingpart {} is {}".format(MissingAngle,Bngle))
    elif MissingAngle == "c":
      c = int(input("Please enter the value of side c:"))
      a = int(input("Please enter the value of side a:"))
      Angle = int(input("Please enter the angle of side a:"))
      Cngle=math.degrees((math.sinh(Angle) * c) / a)
      print("The Angle of missingpart {} is {}".format(MissingAngle,Cngle))
  print("What dou you want to do:")
  print("1.getValueofMissingpart")
  print("2.getAngleofMissingpart")
  Operationchoicevalue = str(input("Please enter the operation you want to accomplish:"))
  if Operationchoicevalue == "1":
    getMissingpart()
  elif Operationchoicevalue =="2":
    getMissingAngle()
print(" |\  ")
print(" | \ ")
print("a|  \ c")
print(" |   \ ")
print(" |__b_\ ")
print("1.get_area")
print("2.get Missing part")
print("3.sin rule")
Operationchoice = str(input("Please enter your choice:"))
if Operationchoice == "1":
  area()
elif Operationchoice =="2":
  findmissingPart()
elif Operationchoice == "3":
  sinRule()
elif Operationchoice == "0":
  exit(0)



