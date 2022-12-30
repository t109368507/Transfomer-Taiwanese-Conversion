# 台羅轉漢羅在Transformer實現

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
raw.cl，raw.hl<br />
![image](https://user-images.githubusercontent.com/93703407/210077139-b24bb4b7-16d6-48b8-ac33-1b53bc13c91a.png)

# 漢羅台羅字對字對齊問題、多餘的空白行

    SCRIPTS=~/fairseq/mosesdecoder/scripts
    NORM_PUNC=${SCRIPTS}/tokenizer/normalize-punctuation.perl

    perl ${NORM_PUNC} -l cl < ${data_dir}/raw.cl > ${data_dir}/norm.cl
    perl ${NORM_PUNC} -l hl < ${data_dir}/raw.hl > ${data_dir}/norm.hl
norm.cl，narm.hl
![image](https://user-images.githubusercontent.com/93703407/210079072-2bddf18c-af05-4a74-9494-a32ffbee3ed5.png)
 
    
# 台羅數據夾雜漢羅字串
分析發現只有在符號’『……..』’才會出現，直接刪除符號內文。<br />
![image](https://user-images.githubusercontent.com/93703407/210078124-13198c10-3ad2-4bab-8b8d-cd4695fecf7e.png)


# 台羅、漢羅每行的字數量不相稱
用行數的判斷，若不相同則直接刪除tbk檔案，總共有10個檔案發生此現象。<br />
＜CL＞重覆出現文本
![image](https://user-images.githubusercontent.com/93703407/210078062-aa0177e2-e1ae-48fb-93a9-3e3a5e1c0798.png)

# 運行tbks.py對以上敘述問題做資料預處理
    python tbks.py

# 驗證對齊方式
在分割資料時比對Source與Target。<br />
![image](https://user-images.githubusercontent.com/93703407/210078711-436b0d92-aa74-4138-bd60-d5dd9f0557bd.png)
<br />
分割資料比對最後數據Source與Target。<br />
![image](https://user-images.githubusercontent.com/93703407/210078796-b2d7ee94-5b34-40ea-93e7-4af0709c5780.png)

# Transformer目錄結構
    ~
    |── mosesdecoder
    |── fairseq
    └── nmt_taiwanese
        |── data
        |   └── taiwanese
        |      |── result          # 存放翻譯結果
        |      └── data-bin        # 存放二進制文件
        |── models                  # 保存訓練過程中的model文件和checkpoint
        |  └── taiwanese
        |      └── checkpoints     # 保存checkpoints
        |── utils                   # 一些其他工具
        |  |── split.py            # 劃分train,valid,test
        |  └── tbk.py             # 劃分src,tgt
        └── scripts                 # 一些腳本



