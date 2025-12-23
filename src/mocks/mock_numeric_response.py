MockNumericResponse = """<html>
<head>
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Cache-Control" content="no-store">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Content-TYPE" content="text/html" charset="iso-8859-1">
<script language="JavaScript" type="text/javascript" src="/frs/klserver.js"></script>
<title>Numeric Registers</title>

</head>
<div style="margin-left:2em"><font size=+1>
<h2>Numeric Registers</h2>
<hr size=4>
</div>

<body bgcolor= #FFF9e3>
<input type="button" value = "Refresh Numeric Registers"
onclick="JavaScript:comToolLink(28)" >

<form id="formTable" name="formTable" LANGUAGE=javascript>
<table border="2" cellpadding="1" cellspacing="1" 
style="border-collapse: collapse" bordercolor="#FFFF00" width="100%">

<tr>
<td width="10%"><p align="center"><b>Register</b></td>
<td width="25%"><p align="center"><b>Comment</b></td>
<td width="25%"><p align="center"><b>Value</b></td>
</tr>
<tr>
<td width="10%"><p align="center">R[1]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment1"  
  value="RADIUS"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal1"  
 value="20"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[2]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment2"  
  value="WELD_PROC"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal2"  
 value="14"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[3]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment3"  
  value="WELD_SCHEDULE"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal3"  
 value="1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[4]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment4"  
  value="WEAVE_SCHEDULE"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal4"  
 value="3"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[5]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment5"  
  value="UFRAME"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal5"  
 value="2"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[6]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment6"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal6"  
 value="1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[7]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment7"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal7"  
 value="1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[8]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment8"  
  value="KOMUNIKAT"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal8"  
 value="1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[9]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment9"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="rVal9"  
 value="-394.0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[10]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment10"  
  value="TRIGGER"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal10"  
 value="1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[11]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment11"  
  value="SZEROKOSC"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal11"  
 value="550"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[12]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment12"  
  value="DLUGOSC"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal12"  
 value="550"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[13]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment13"  
  value="WYSOKOSC"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal13"  
 value="60"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[14]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment14"  
  value="GRUBOSC"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal14"  
 value="20"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[15]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment15"  
  value="UF"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal15"  
 value="1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[16]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment16"  
  value="WYSOKOSC_ODJ"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal16"  
 value="320"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[17]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment17"  
  value="OBLICZ_X"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal17"  
 value="-1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[18]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment18"  
  value="OBLICZ_Y"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal18"  
 value="552"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[19]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment19"  
  value="OBLICZ_Z"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="rVal19"  
 value="-71.0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[20]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment20"  
  value="Wait TIME"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal20"  
 value="6"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[21]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment21"  
  value="Cycles_ran"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal21"  
 value="17303"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[22]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment22"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="rVal22"  
 value="30.0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[23]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment23"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal23"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[24]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment24"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal24"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[25]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment25"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal25"  
 value="-25"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[26]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment26"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal26"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[27]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment27"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal27"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[28]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment28"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal28"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[29]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment29"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal29"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[30]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment30"  
  value="LICZNIK"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal30"  
 value="1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[31]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment31"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal31"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[32]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment32"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal32"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[33]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment33"  
  value="NR OF CYCLES"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal33"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[34]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment34"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal34"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[35]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment35"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal35"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[36]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment36"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal36"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[37]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment37"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal37"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[38]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment38"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal38"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[39]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment39"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal39"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[40]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment40"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal40"  
 value="40"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[41]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment41"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal41"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[42]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment42"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal42"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[43]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment43"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal43"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[44]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment44"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal44"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[45]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment45"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal45"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[46]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment46"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal46"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[47]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment47"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal47"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[48]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment48"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal48"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[49]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment49"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal49"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[50]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment50"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal50"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[51]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment51"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal51"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[52]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment52"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal52"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[53]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment53"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal53"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[54]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment54"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal54"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[55]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment55"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal55"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[56]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment56"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal56"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[57]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment57"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal57"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[58]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment58"  
  value="Nr of cycles"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal58"  
 value="4"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[59]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment59"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal59"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[60]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment60"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal60"  
 value="2"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[61]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment61"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal61"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[62]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment62"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal62"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[63]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment63"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal63"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[64]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment64"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal64"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[65]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment65"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal65"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[66]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment66"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal66"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[67]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment67"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal67"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[68]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment68"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal68"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[69]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment69"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal69"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[70]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment70"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal70"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[71]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment71"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal71"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[72]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment72"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal72"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[73]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment73"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal73"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[74]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment74"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal74"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[75]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment75"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal75"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[76]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment76"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal76"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[77]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment77"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal77"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[78]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment78"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal78"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[79]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment79"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal79"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[80]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment80"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal80"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[81]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment81"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal81"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[82]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment82"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal82"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[83]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment83"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal83"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[84]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment84"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal84"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[85]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment85"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal85"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[86]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment86"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal86"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[87]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment87"  
  value="CLEAN_SET"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal87"  
 value="7"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[88]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment88"  
  value="CLEAN"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal88"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[89]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment89"  
  value="CURRENT_TOOL"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal89"  
 value="1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[90]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment90"  
  value="CURRENT_FRAME"
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal90"  
 value="2"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[91]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment91"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal91"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[92]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment92"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal92"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[93]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment93"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal93"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[94]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment94"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal94"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[95]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment95"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal95"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[96]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment96"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal96"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[97]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment97"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal97"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[98]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment98"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal98"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[99]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment99"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal99"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[100]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment100"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal100"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[101]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment101"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal101"  
 value="1"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[102]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment102"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal102"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[103]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment103"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal103"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[104]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment104"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal104"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[105]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment105"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal105"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[106]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment106"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal106"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[107]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment107"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal107"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[108]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment108"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal108"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[109]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment109"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal109"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[110]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment110"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal110"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[111]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment111"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal111"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[112]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment112"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal112"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[113]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment113"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal113"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[114]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment114"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal114"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[115]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment115"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal115"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[116]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment116"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal116"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[117]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment117"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal117"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[118]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment118"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal118"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[119]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment119"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal119"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[120]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment120"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal120"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[121]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment121"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal121"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[122]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment122"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal122"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[123]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment123"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal123"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[124]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment124"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal124"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[125]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment125"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal125"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[126]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment126"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal126"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[127]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment127"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal127"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[128]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment128"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal128"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[129]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment129"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal129"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[130]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment130"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal130"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[131]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment131"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal131"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[132]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment132"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal132"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[133]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment133"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal133"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[134]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment134"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal134"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[135]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment135"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal135"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[136]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment136"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal136"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[137]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment137"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal137"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[138]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment138"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal138"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[139]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment139"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal139"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[140]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment140"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal140"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[141]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment141"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal141"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[142]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment142"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal142"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[143]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment143"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal143"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[144]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment144"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal144"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[145]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment145"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal145"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[146]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment146"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal146"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[147]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment147"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal147"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[148]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment148"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal148"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[149]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment149"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal149"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[150]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment150"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal150"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[151]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment151"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal151"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[152]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment152"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal152"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[153]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment153"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal153"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[154]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment154"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal154"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[155]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment155"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal155"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[156]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment156"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal156"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[157]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment157"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal157"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[158]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment158"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal158"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[159]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment159"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal159"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[160]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment160"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal160"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[161]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment161"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal161"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[162]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment162"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal162"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[163]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment163"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal163"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[164]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment164"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal164"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[165]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment165"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal165"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[166]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment166"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal166"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[167]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment167"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal167"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[168]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment168"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal168"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[169]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment169"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal169"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[170]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment170"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal170"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[171]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment171"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal171"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[172]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment172"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal172"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[173]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment173"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal173"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[174]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment174"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal174"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[175]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment175"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal175"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[176]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment176"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal176"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[177]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment177"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal177"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[178]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment178"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal178"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[179]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment179"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal179"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[180]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment180"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal180"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[181]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment181"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal181"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[182]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment182"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal182"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[183]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment183"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal183"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[184]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment184"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal184"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[185]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment185"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal185"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[186]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment186"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal186"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[187]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment187"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal187"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[188]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment188"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal188"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[189]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment189"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal189"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[190]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment190"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal190"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[191]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment191"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal191"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[192]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment192"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal192"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[193]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment193"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal193"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[194]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment194"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal194"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[195]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment195"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal195"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[196]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment196"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal196"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[197]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment197"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal197"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[198]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment198"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal198"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[199]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment199"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal199"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

<tr>
<td width="10%"><p align="center">R[200]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment200"  
  value=""
onchange="sendComment(this.value,this.name,1)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal200"  
 value="0"
onchange="sendRegValue(this.value,this.name,2)" size="32" maxlength="16"></td>
</tr>

</table>
</form>
</body>
</html>"""
