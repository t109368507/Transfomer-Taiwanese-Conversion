# 台羅轉漢台在Transformer實現

Transformer 漢羅轉台羅<br />
資料集:<br />
台語文數位典藏資料庫<br />
Total files: 2168 tbks<br />
  ![image](https://user-images.githubusercontent.com/93703407/210074703-962a9741-827d-4a95-aac8-d93c2d61e81a.png)

# 數據資料集問題
* 數據分割台羅、漢羅。<br />
* 刪除多餘的字標籤，如:＜BR＞、＜CL＞、＜/CL＞、＜HL＞、＜/HL＞。< br />
* 標點符號移除，如:”-！,':!?[].()“「」，。？（）：﹙﹚‘、；;…。<br />
* 漢羅台羅字對字對齊問題。<br />
* 台羅數據夾雜漢羅字串，如:『那也要妳有來上課才行.』A-mui5 the5-chhenn2 A-lan5,。<br />
* 多餘的空白行。<br />
* 台羅、漢羅每行的字數量不相稱。<br />

# 原始數據<CL>台羅</CL>、<HL>漢羅</HL>
  ![image](https://user-images.githubusercontent.com/93703407/210075640-37962814-630e-4f5f-8d2a-2d2b8804287f.png)

# 刪除字標籤
  ![image](https://user-images.githubusercontent.com/93703407/210075872-b1e406cb-5bcc-4874-8206-b7215785cdca.png)

# 數據分割台羅、漢羅
raw.cl，raw.hl
![image](https://user-images.githubusercontent.com/93703407/210077139-b24bb4b7-16d6-48b8-ac33-1b53bc13c91a.png)

# 漢羅台羅字對字對齊問題、多餘的空白行

    SCRIPTS=~/fairseq/mosesdecoder/scripts
    NORM_PUNC=${SCRIPTS}/tokenizer/normalize-punctuation.perl

    perl ${NORM_PUNC} -l cl < ${data_dir}/raw.cl > ${data_dir}/norm.cl
    perl ${NORM_PUNC} -l hl < ${data_dir}/raw.hl > ${data_dir}/norm.hl
    

