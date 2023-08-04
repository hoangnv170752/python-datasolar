import requests

x = requests.get('https://hocpython.org/data/')

html = x.text

vitridaubang = html.find("<table>")
vitricuoibang = html.find("</table>")

html = html[vitridaubang+7:vitricuoibang] 

html = html.replace("<tbody>","")
html = html.replace("</tbody>","")
html = html.replace("<tr>","")
html = html.replace("</tr>","\n")
html = html.replace("<td>","")
html = html.replace("</td>",",")
html = html.replace(",\n","\n")

f = open("DataNV.csv","w", encoding="utf8")
f.write(html)
f.close()


