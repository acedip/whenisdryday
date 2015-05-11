<html>
<body>
<p>
                      _                                       
                     (_)                                      
   ___ ___  _ __ ___  _ _ __   __ _   ___  ___   ___  _ __    
  / __/ _ \| '_ ` _ \| | '_ \ / _` | / __|/ _ \ / _ \| '_ \   
 | (_| (_) | | | | | | | | | | (_| | \__ | (_) | (_) | | | |_ 
  \___\___/|_| |_| |_|_|_| |_|\__, | |___/\___/ \___/|_| |_(_)
                               __/ |                          
                              |___/                           
</p>

<p>Hi {{dUserInfo['name']}}
	</p>
<p>Thanks for signing up to receive updates for {{dUserInfo['state']}}
	</p>
<p>via email on {{dUserInfo['email']}}
	</p>
<p>via phone on {{dUserInfo['phone']}}
	</p>
<p>
% if sUserNxtDryDayDtl['id']=='main':
	<p>{{sUserNxtDryDayDtl['msg']}} {{sUserNxtDryDayDtl['day1']}} {{sUserNxtDryDayDtl['date1']}} {{sUserNxtDryDayDtl['month1']}}{{sUserNxtDryDayDtl['day2']}} {{sUserNxtDryDayDtl['date2']}} {{sUserNxtDryDayDtl['month2']}}</p>
%else:
	<p>{{sUserNxtDryDayDtl['msg']}} {{sUserNxtDryDayDtl['day']}} {{sUserNxtDryDayDtl['date']}} {{sUserNxtDryDayDtl['month']}}</p>
%end
<p>List of all Dry Days in {{dUserInfo['state']}} </p>
<table border="1">
<tr>
<td>Reason</td><td>date</td>
</tr>
%for row in sUserAllDryDay:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>

</body>
</html>
