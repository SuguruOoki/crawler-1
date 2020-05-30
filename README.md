# クローラー/スクレイピング

 1. 収集(crawler)
 2. 解析(parser)
 3. 抽出(extractor)
 4. 加工(prosessor)
 5. 保存

```python
import json
import requests

r = requests.get("URL", params={"key1": "value1", "key2": "value2"})
requests.post("URL", data=json.dumps({"key1": "value1", "key2": "value2"}))
```

```python
import requests
import lxml.html


r = requests.get("http://www.shoeisha.co.jp/book/detail/9784798146072")
html = r.text
root = lxml.html.fromstring(html)

title_h1 = root.xpath("html/body/div[1]/section/h1")
print(title_h1[0].text)

qa_a = root.cssselect('#qa > p > a')
for a in qa_a:
    print(a.attrib['href'])
```