#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      p2-1020
#
# Created:     31-01-2014
# Copyright:   (c) p2-1020 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re

#Fonction random pour loader le dictionnaire et chercher dedans
#Pas utile pour l'instant

def printme( str1 ) :

   for line in open("dictionnaire.txt", 'r'):
        if str1 in line:
            print line

#Test values

str1 = "cat"
str2 = "cat"

#Test si on a un match du premier character jusqu'? l'avant dernier
#Ca marche sauf que ca fait pas la substution d'une lettre au millieu donc pas vraiment utile
matchObj = re.search( 'a', 'abc')
if matchObj:
   print "search --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

#Test si on a un match du deuxieme character jusqu'au dernier
matchObj = re.search( str1[1:], str2, re.M|re.I)
if matchObj:
   print "search --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"

#Tentative de while/regular expression pour faire la substition lettre par lettre et comparer
#Algo naif, pas super efficace
var = 0

count = len (str1)
while (var < count ):
   matchObj = re.search( str1 , str2)
   if matchObj:
     print matchObj.group()





