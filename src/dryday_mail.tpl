<p>The open items are as follows:</p>
<table border="1">

tomorrow is dry in <br>
%for row in tResult:
  %for col in row:
	{{col}} <br>
  %end
%end

<br>
Here is the list of all dry days in states you subscribed for - 
%for row in tstate:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>
