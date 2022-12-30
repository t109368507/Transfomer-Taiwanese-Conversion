# 台羅轉漢台在Transformer實現

Transformer 漢羅轉台羅<br />
資料集:<br />
台語文數位典藏資料庫<br />
Total files: 2168 tbk<br />

![image](https://user-images.githubusercontent.com/93703407/210074703-962a9741-827d-4a95-aac8-d93c2d61e81a.png)

# 數據資料集問題
* 數據分割台羅、漢羅。<br />
* 刪除多餘的字標籤，如:<BR>、<CL>、</CL>、<HL>、</HL>。<br />
* 標點符號移除，如:”-！,':!?[].()“「」，。？（）：﹙﹚‘、；;…。<br />
* 漢羅台羅字對字對齊問題。<br />
* 台羅數據夾雜漢羅字串，如:『那也要妳有來上課才行.』A-mui5 the5-chhenn2 A-lan5,。<br />
* 多餘的空白行。<br />
* 台羅、漢羅每行的字數量不相稱。<br />
