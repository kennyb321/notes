#Web Scarping / Beautiful Soup Notes

<h3>
Basic Website Scarping</h3>

Example: Scraping Wikkiepedia to get information about Women Computer Scientists


````
	
	import csv
	from bs4 import BeautifulSoup
	import requests
	
	url = 'https://en.wikipedia.org/wiki/Category:Women_computer_scientists'
	page = requests.get(url)
	page_content = page.content
	soup = BeutifulSoup(page_content, "html.parser")
	
````
	
The soup variable will return the html source code for the website
<h4>Inspect</h4>
To see which html tag contains thew informatioin we want, right cvlick on the information and click inspect.
This will bring up the developers tools on your web browser, and you will be able to see which
tag contains the information we need.
<h4>
https://unminify.com/
</h4>
The code that you copy from the raw html will not have any tabs or spaces, and will be hard to read.
If you run the code through https://unminify.com/, you can turn
<h3>This, </h3>

````
<div class="mw-category-group"><h3>A</h3>
<ul><li><a href="/wiki/Karen_Aardal" title="Karen Aardal">Karen Aardal</a></li>
<li><a href="/wiki/Janet_Abbate" title="Janet Abbate">Janet Abbate</a></li>
<li><a href="/wiki/Rediet_Abebe" title="Rediet Abebe">Rediet Abebe</a></li>
<li><a href="/wiki/Sarita_Adve" title="Sarita Adve">Sarita Adve</a></li>
<li><a href="/wiki/Nancy_M._Amato" title="Nancy M. Amato">Nancy M. Amato</a></li>
<li><a href="/wiki/Kathleen_Antonelli" title="Kathleen Antonelli">Kathleen Antonelli</a></li>
<li><a href="/wiki/Gillian_Arnold_(technologist)" title="Gillian Arnold (technologist)">Gillian Arnold (technologist)</a></li>
<li><a href="/wiki/Stella_Atkins" title="Stella Atkins">Stella Atkins</a></li>
<li><a href="/wiki/Terri_Attwood" title="Terri Attwood">Terri Attwood</a></li>
<li><a href="/wiki/Donna_Auguste" title="Donna Auguste">Donna Auguste</a></li>
<li><a href="/wiki/Henriette_Avram" title="Henriette Avram">Henriette Avram</a></li></ul></div>

````

<h3>Into this!</h3>

````
<div class="mw-category-group">
    <h3>A</h3>
    <ul>
        <li><a href="/wiki/Karen_Aardal" title="Karen Aardal">Karen Aardal</a></li>
        <li><a href="/wiki/Janet_Abbate" title="Janet Abbate">Janet Abbate</a></li>
        <li><a href="/wiki/Rediet_Abebe" title="Rediet Abebe">Rediet Abebe</a></li>
        <li><a href="/wiki/Sarita_Adve" title="Sarita Adve">Sarita Adve</a></li>
        <li><a href="/wiki/Nancy_M._Amato" title="Nancy M. Amato">Nancy M. Amato</a></li>
        <li><a href="/wiki/Kathleen_Antonelli" title="Kathleen Antonelli">Kathleen Antonelli</a></li>
        <li><a href="/wiki/Gillian_Arnold_(technologist)" title="Gillian Arnold (technologist)">Gillian Arnold (technologist)</a></li>
        <li><a href="/wiki/Stella_Atkins" title="Stella Atkins">Stella Atkins</a></li>
        <li><a href="/wiki/Terri_Attwood" title="Terri Attwood">Terri Attwood</a></li>
        <li><a href="/wiki/Donna_Auguste" title="Donna Auguste">Donna Auguste</a></li>
        <li><a href="/wiki/Henriette_Avram" title="Henriette Avram">Henriette Avram</a></li>
    </ul>
</div>
````

	

	
	
	
