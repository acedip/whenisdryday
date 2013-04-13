%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border="1">
<!-- <tr>
	<td>First Name</td>
	<td>Last Name</td>
	<td>Email</td>
	<td>State One</td>
	<td>State Two</td>
	<td>State Three</td>
	<td>Verified_0_1</td>
</tr> -->

%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>
