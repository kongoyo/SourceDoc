from bs4 import BeautifulSoup

# 您提供的HTML片段
html_content = """[<tbody>
<tr data-hd-audience="AP">
<td class="tdcenter" headers="smlcg__lcg__entry__1">7063-CR1</td>
<td class="tdcenter" headers="smlcg__lcg__entry__2">2017-10-10</td>
<td class="tdcenter" headers="smlcg__lcg__entry__3">2017-10-20</td>
<td class="tdcenter" headers="smlcg__lcg__entry__4">2021-07-31</td>
<td class="tdcenter" headers="smlcg__lcg__entry__5">-</td>
</tr>
<tr data-hd-audience="JPN">
<td class="tdcenter" headers="smlcg__lcg__entry__1">7063-CR1</td>
<td class="tdcenter" headers="smlcg__lcg__entry__2">2017-10-10</td>
<td class="tdcenter" headers="smlcg__lcg__entry__3">2017-10-20</td>
<td class="tdcenter" headers="smlcg__lcg__entry__4">2021-07-31</td>
<td class="tdcenter" headers="smlcg__lcg__entry__5">-</td>
</tr>
<tr data-hd-audience="CAN">
<td class="tdcenter" headers="smlcg__lcg__entry__1">7063-CR1</td>
<td class="tdcenter" headers="smlcg__lcg__entry__2">2017-08-08</td>
<td class="tdcenter" headers="smlcg__lcg__entry__3">2017-09-15</td>
<td class="tdcenter" headers="smlcg__lcg__entry__4">2021-07-31</td>
<td class="tdcenter" headers="smlcg__lcg__entry__5">-</td>
</tr>
<tr data-hd-audience="LA">
<td class="tdcenter" headers="smlcg__lcg__entry__1">7063-CR1</td>
<td class="tdcenter" headers="smlcg__lcg__entry__2">2017-08-08</td>
<td class="tdcenter" headers="smlcg__lcg__entry__3">2017-09-15</td>
<td class="tdcenter" headers="smlcg__lcg__entry__4">2021-07-31</td>
<td class="tdcenter" headers="smlcg__lcg__entry__5">-</td>
</tr>
<tr data-hd-audience="EMEA">
<td class="tdcenter" headers="smlcg__lcg__entry__1">7063-CR1</td>
<td class="tdcenter" headers="smlcg__lcg__entry__2">2017-10-10</td>
<td class="tdcenter" headers="smlcg__lcg__entry__3">2017-10-20</td>
<td class="tdcenter" headers="smlcg__lcg__entry__4">2021-07-31</td>
<td class="tdcenter" headers="smlcg__lcg__entry__5">-</td>
</tr>
<tr data-hd-audience="US">
<td class="tdcenter" headers="smlcg__lcg__entry__1">7063-CR1</td>
<td class="tdcenter" headers="smlcg__lcg__entry__2">2017-08-08</td>
<td class="tdcenter" headers="smlcg__lcg__entry__3">2017-09-15</td>
<td class="tdcenter" headers="smlcg__lcg__entry__4">2021-07-31</td>
<td class="tdcenter" headers="smlcg__lcg__entry__5">-</td>
</tr>
</tbody>, <tbody>
<tr>
<td class="tdcenter" headers="smmsm__entry__1">CR1</td>
<td class="tdcenter" headers="smmsm__entry__2">6 cores</td>
<td class="tdcenter" headers="smmsm__entry__3">2.095 GHz</td>
<td class="tdcenter" headers="smmsm__entry__4">32 GB</td>
<td class="tdcenter" headers="smmsm__entry__5">2 x 2 TB SATA</td>
<td class="tdcenter" headers="smmsm__entry__6">N/A</td>
</tr>
</tbody>]"""

# 创建BeautifulSoup对象
soup = BeautifulSoup(html_content, "html.parser")

# 找到所有<tr>元素，这些是每一行的数据
rows = soup.find_all("tr", {"data-hd-audience": "EMEA"})

# 遍历每一行，提取<td>元素的内容并打印
for row in rows:
    tds = row.find_all("td", class_="tdcenter", headers="smlcg__lcg__entry")
    for td in tds:
        print(td.get_text())
