MockStringResponse = """<html>
<head>
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Cache-Control" content="no-store">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Content-TYPE" content="text/html" charset="iso-8859-1">
<script language="JavaScript" type="text/javascript" src="/frs/klserver.js"></script>
<title>String Registers</title>

</head>
<div style="margin-left:2em"><font size=+1>
<h2>String Registers</h2>
<hr size=4>
</div>

<body bgcolor= #FFF9e3>
<input type="button" value = "Refresh String Registers"
onclick="JavaScript:comToolLink(30)" >

<form id="formTable" name="formTable" LANGUAGE=javascript>
<table border="2" cellpadding="1" cellspacing="1" 
style="border-collapse: collapse" bordercolor="#FFFF00" width="100%">

<tr>
<td width="10%"><p align="center"><b>String Register</b></td>
<td width="25%"><p align="center"><b>Comment</b></td>
<td width="25%"><p align="center"><b>Value</b></td>
</tr>
<tr>
<td width="10%"><p align="center">SR[1]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment1"  
  value="ODWROC123"
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal1"  
 value="ODWROC"
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[2]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment2"  
  value="ZMIEN DETAL"
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal2"  
 value="ZMIEN DETAL"
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[3]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment3"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal3"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[4]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment4"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal4"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[5]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment5"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal5"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[6]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment6"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal6"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[7]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment7"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal7"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[8]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment8"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal8"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[9]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment9"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal9"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[10]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment10"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal10"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[11]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment11"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal11"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[12]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment12"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal12"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[13]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment13"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal13"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[14]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment14"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal14"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[15]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment15"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal15"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[16]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment16"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal16"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[17]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment17"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal17"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[18]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment18"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal18"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[19]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment19"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal19"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[20]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment20"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal20"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[21]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment21"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal21"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[22]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment22"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal22"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[23]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment23"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal23"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[24]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment24"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal24"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

<tr>
<td width="10%"><p align="center">SR[25]</td>
<td width="25%"><p align="center">
<input type="text" name="strComment25"  
  value=""
onchange="sendComment(this.value,this.name,14)" size="32" maxlength="16"></td>
<td width="25%"><p align="center">
<input type="text" name="iVal25"  
 value=""
onchange="sendValue(this.value,this.name,15)" size="32" maxlength="254"></td>
</tr>

</table>
</form>
</body>
</html>"""