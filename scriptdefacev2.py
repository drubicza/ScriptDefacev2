import urllib2, cookielib, random, re, sys, socket, time, httplib, ssl, os
b = '\x1b[0;34m'
g = '\x1b[1;32m'
w = '\x1b[1;37m'
r = '\x1b[1;31m'
y = '\x1b[1;33m'
c = '\x1b[0;36m'
lgray = '\x1b[0;37m'
dgray = '\x1b[1;30m'
ir = '\x1b[0;101m'
reset = '\x1b[0m'
print 'loading....'
os.system('sleep1,0')
os.system('clear')
print 'Loading.......'
os.system('sleep;1.,0')
os.system('clear')
print
banner = g + "                   ___         _      _   ___       __                 ___\n                  / __| __ _ _(_)_ __| |_|   \\ ___ / _|__ _ __ _____ _|_  )\n                  \\__ \\/ _| '_| | '_ \\  _| |) / -_)  _/ _` / _/ -_) V // /\n                  |___/\\__|_| |_| .__/\\__|___/\\___|_| \\__,_\\__\\___|\\_//___|"
print banner
print
print
print c + '                       [+]=======================================[+]'
print c + '                       |' + r + '              CreateScriptDefaceV2        ' + c + ' |'
print c + '                       |' + r + '          Author:TuanSadboys               ' + c + '|'
print c + '                       |' + r + '          Wa:6288703041772                 ' + c + '|'
print c + '                       |' + r + '          Youtube:TuanSadboys             ' + c + ' |'
print c + '                       |' + r + '          Team:INDONESIA CYBER MAFIA      ' + c + ' |'
print c + '                       [+]=======================================[+]'
print b + '[S]' + w + 'Masukan Judul Atau Title' + b + '[S]'
title = raw_input(y + '[+]' + g + 'TITLE' + y + '=>>>' + b)
print b + '[A]' + w + 'Masukan alert Atau Peringatan' + b + '[A]'
alert = raw_input(y + '[+]' + g + 'ALERT' + y + '=>>>' + b)
print b + '[D]' + w + 'Masukan Link Logo' + b + '[D]'
img = raw_input(y + '[+]' + g + 'LOGO' + y + '=>>>' + b)
print b + '[B]' + w + 'Masukan Nama Anda Misal (TuanSadboys)' + b + '[B]'
nick = raw_input(y + '[+]' + g + 'NAMA' + y + '=>>>' + b)
print b + '[O]' + w + 'Masukan Pesan pertama  Dan <br> untuk pasan Kedua Dan <br> lagi untuk pesan ketiga:' + b + '[O]'
pesan = raw_input(y + '[+]' + g + 'PESAN' + y + '=>>>' + b)
print b + '[Y]' + w + 'Terima Kasih Untuk:' + b + '[Y]'
thanks = raw_input(y + '[+]' + g + 'THANKS' + y + '=>>>' + b)
print b + '[S]' + w + 'Masukan Link Lagu:' + b + '[S]'
lagu = raw_input(y + '[+]' + g + 'LAGU' + y + '=>>>' + b)
print b + '[+]' + w + 'Masukan Nama File Yang Diakhiri html:' + b + '[+]'
namafile = raw_input(y + '[+]' + g + 'NAMAFILE' + y + '=>>>' + b)
m1 = '<!DOCTYPE html>\n<html>\n<head>\n    <title>'
m2 = title
m3 = '</title>\n    <meta charset="UTF-8">\n    <meta name="Author" content="TuanSadboys<3"/>\n    <meta name="copyright" content="TuanSadboys<3"/>\n    <meta name="description" content="Admin Kerentanan Webmu Membuat Aku Meretasnya,Tolong Perbaiki"/>\n    <link href=\'http://fonts.googleapis.com/css?family=Iceland:400,700\' rel=\'stylesheet\' type=\'text/css\'>\n    <link href=\'http://fonts.googleapis.com/css?family=Iceland:400,700\' rel=\'stylesheet\' type=\'text/css\'>\n    <link href="https://fonts.googleapis.com/css?family=Dokdo|Gloria+Hallelujah|Indie+Flower|Permanent+Marker" rel="stylesheet">\n    <link href="https://fonts.googleapis.com/css?family=Righteous" rel="stylesheet">\n    <link href="https://fonts.googleapis.com/css?family=Fredericka+the+Great|Kaushan+Script|Press+Start+2P|Rationale" rel="stylesheet">\n    <link href="https://fonts.googleapis.com/css?family=Chewy" rel="stylesheet">\n    <link href="https://fonts.googleapis.com/css?family=Londrina+Sketch" rel="stylesheet" type="text/css"> \n    <link href="https://fonts.googleapis.com/css?family=Permanent+Marker|Righteous" rel="stylesheet">\n    <link href="https://fonts.googleapis.com/css?family=Iceberg:400,700" rel="stylesheet" type="text/css">\n <iframe width="0" height="0" src="https://e.top4top.net/m_11870e58k0.mp3" frameborder="0" allowfullscreen></iframe>\n<script>\nalert(\''
m4 = alert
m5 = '\')\n</script>\n<style type="text/css">body{background-image:url(https://thumbs.gfycat.com/ShowyComplexAmericangoldfinch-max-1mb.gif); background-size:cover}</style>\n    <center>\n        <body bgcolor=black><table width=100% height=100%><td align=center><span style=\'font: 60px fantasy;size:60px; color:#FFFAF0; text-shadow: 5px 5px 60px #87CEFA;\'><img src=\''
m6 = img
m7 = '\'width="650"height="650"><br><marquee behavior="scroll" direction="left" scrollamount="90" scrolldelay="40" width="100%">\n\t<font color="Blue">___________________________________________________________</font></marquee><br><font face="Londrina Sketch"><font size="15" \ncolor="Chartreuse">[+]HACKED BY '
m8 = nick
m9 = '[+]</font></font></font></font></marquee></center><br><marquee behavior="scroll" direction="right" scrollamount="90" scrolldelay="40" width="100%">\n\t<font color="Blue">___________________________________________________________</font></marquee>\n      <center>\n\t<div style="text-shadow: 5px 5px 5px #FF0000;">\n\t<font color="SpringGreen" size="8" face="Chewy">\n\t<script language="JavaScript">\n\tvar text=" <br>'
m10 = pesan
m11 = '<br>"\n\tvar delay=50;\n\tvar currentChar=1;\n\tvar destination="[none]";\n\tfunction type()\n\t{\n\t//if (document.all)\n\t{\n\tvar dest=document.getElementById(destination);\n\tif (dest)// && dest.innerHTML)\n\t{\n\tdest.innerHTML=text.substr(0,currentChar)+"<blink>_</blink>";\n\tcurrentChar++;\n\tif (currentChar>text.length)\n\t{\n\tcurrentChar=1;\n\tsetTimeout("type()",5000);\n\t}\n\telse\n\t{\n\tsetTimeout("type()",delay);\n\t}\n\t}\n\t}\n\t} \n\tfunction startTyping(textParam,delayParam,destinationParam)\n\t{\n\ttext=textParam;\n\tdelay=delayParam;\n\tcurrentChar=1;\n\tdestination=destinationParam;\n\ttype();\n\t}\n\t</script>\n\t\n\t<b><div id="textDestination" style="background-color:black"; style="font: 50px Arial color:blue; margin:0px;"></div></b>\n\t<script language="JavaScript">\n\tjavascript:startTyping(text,50,"textDestination");\n\t</script></div>\n\t<br><script type="text/javascript">\n\tfl=1\n\tfunction f1()\n\tfunction f(){\n\tif(fl==1)\n\t{\n\tBn.style.top=100\n\tBn.style.left=600\n\tfl=2\n\t}\n\telse if(fl==2)\n\t{\n\tBn.style.top=600\n\tBn.style.left=50\n\tfl=3\n\t}\n\telse if(fl==5)\n\t{\n\tBn.style.top=200\n\tBn.style.left=500\n\tfl=\n\t}\n\t}\n\t</script></font>\n\t<div style="text-shadow: 0px 0px 10px green;"><span style="color: white;"><font face="Chewy" size="4"><b>Thanks To: <marquee scrollamount="5" direction="left" width="50%"><span style="color: red;"> <span style="color: red;">'
m12 = thanks
m13 = '<span style="color: red;"></b></marquee></font></div><script type="text/rocketscript">/*<![CDATA[*/new TypingText(document.getElementById("message"), 90, function(i){ var ar= new Array("_", " ", "_", " "); return "" +ar[i.length % ar.length]; });//Type out examples:TypingText.runAll();/*]]>*/</script>\n     <audio autoplay="autoplay" controls="controls" width="128px" height="30px"><source src=\''
t1 = lagu
t2 = '\' type="audio/mpeg"></audio><br><br>\n</div> \n</center> '
file = open(namafile, 'w')
file.write(m1)
file.write(m2)
file.write(m3)
file.write(m4)
file.write(m5)
file.write(m6)
file.write(m7)
file.write(m8)
file.write(m9)
file.write(m10)
file.write(m11)
file.write(m12)
file.write(m13)
file.write(t1)
file.write(t2)
os.system('mv ' + namafile + ' /sdcard')
print g + '[+]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[+]'
print lgray + '        Script anda Sudah Selesai Liat Di Penyimpanan Internal Dengan Nama ' + namafile
print g + '[+]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[+]'
file.close()
