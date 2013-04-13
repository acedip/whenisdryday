<!doctype html>
<head>
	<meta charset="utf-8">
	<title>When is Dry Day ?</title>
	<style type='text/css'>
	body {
		background-color: #eee; /* I took an oath never to use flat white backgrounds. */
		text-rendering: optimizeLegibility;
		color: #222;
		margin: 0px;
		padding: 0px;
		margin-top: 5%;
		width: 100%;
		font-family: 'Alegreya'; /* Do you speak German? No? Then STOP USING HELVETICA. */
		text-align: center;
	}
	
	h1 {
		font-weight: normal;
		font-size: 60px;
		margin: 0px;
	}

	h2 {
		font-weight: normal;
  		font-size: 40px;
		margin-left:30%;
		text-align: left;
	}
	#main {
		margin: auto;
		width: 50em;
		text-align: center;
	}
		
	a, a:visited { color: inherit; }
	
	#by {
		color: #888;
	}
	
	em {
		font-style: normal;
		border: 1px solid red;
	}
	</style>
</head>

<body>
<form action="/insertdryday" method="GET"> 
	<div id='main'>
   	     <h1>When is Dry Day</h1>
   	     <h2> For internal use only<br>Insert Dry Days info in db</h2>
		<select name="state" required style="width: 200px; padding: 10px" >
              <option value="">Select A State</option>
              	<option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
                <option value="Andhra Pradesh">Andhra Pradesh</option>
                <option value="Arunachal Pradesh">Arunachal Pradesh</option>
                <option value="Assam">Assam</option>
                <option value="Bihar">Bihar</option>
                <option value="Chandigarh">Chandigarh</option>
                <option value="Chhattisgarh">Chhattisgarh</option>
                <option value="Dadar and Nagar Haveli">Dadar and Nagar Haveli</option>
                <option value="Daman and Diu">Daman and Diu</option>
                <option value="Delhi">Delhi</option>
                <option value="Goa">Goa</option>
<!--                <option value="Gujarat">Gujarat</option> UNTIL FIGURE OUT THE UX FOR THIS -->
                <option value="Haryana">Haryana</option>
                <option value="Himachal Pradesh">Himachal Pradesh</option>
                <option value="Jammu and Kashmir">Jammu and Kashmir</option>
                <option value="Jharkhand">Jharkhand</option>
                <option value="Karnataka">Karnataka</option>
                <option value="Kerala">Kerala</option>
                <option value="Lakshadeep">Lakshadeep</option>
                <option value="Madya Pradesh">Madya Pradesh</option>
                <option value="Maharashtra">Maharashtra</option>
                <option value="Manipur">Manipur</option>
                <option value="Meghalaya">Meghalaya</option>
                <option value="Mizoram">Mizoram</option>
                <option value="Nagaland">Nagaland</option>
                <option value="Orissa">Orissa</option>
                <option value="Punjab">Punjab</option>
                <option value="Rajasthan">Rajasthan</option>
                <option value="Sikkim">Sikkim</option>
                <option value="Tamil Nadu">Tamil Nadu</option>
                <option value="Tripura">Tripura</option>
                <option value="Uttar Pradesh">Uttar Pradesh</option>
                <option value="Uttaranchal">Uttaranchal</option>
                <option value="West Bengal">West Bengal</option>
            </select><br>
            <br>
		<input type="text" name="drydate" placeholder="Dry Date" required style="width: 200px; padding: 8px" > <br>
		<input type="submit" name="save" value="Save" style="width: 100px; padding: 5px; background-color: #3682B4; color: #FFFFFF; border-radius:10px">
		<p>Date format YYYY-MM-DD. For Eg 2012-01-01<br>
	</div>
</form>
</body>
</html>

