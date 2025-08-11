# 中興資管 112級 蔡宜宸 論文

## 資料：原始判決書(所有判決書->酒駕判決書) => LLM處理後的案件結構化資料 => 文字內容編碼處理後的結構化資料

> 每一筆row的資料，就代表一個案件

- <b>最原始資料：原始司法判決書 (可以去司法院opendata取得) -> 要用程式把酒駕的篩選出來</b>
  - 因為所有判決書跟酒駕判決書，檔案太大，所以我就不放了，但所有判決書可以去開放資料抓，然後跑 <b>copyFile.py</b> 就會得到酒駕判決書了，所有判決跟酒駕判決都要注意路徑的地方，從哪來跟要放哪裡
- <b>案件結構化資料(還是文字內容)</b>
  - 編碼後的案件結構化資料就是把：判決結構化資料+酒駕前案紀錄+法官，所有欄位全部串起來，再轉數字型態，讓模型看得懂
  - 檔案：[案件結構化資料(還是文字內容)](https://github.com/yc-chen10/112-yichentsai-thesis/tree/main/%E6%A1%88%E4%BB%B6%E7%B5%90%E6%A7%8B%E5%8C%96%E8%B3%87%E6%96%99(%E9%82%84%E6%98%AF%E6%96%87%E5%AD%97%E5%85%A7%E5%AE%B9))
- <b>編碼後的案件結構化資料：都轉成數字型態（也就是模型訓練的X和Y）</b>
  - 檔案：[2016to22_判決結構化資料_清洗整理後_有序資料編碼修正後v2_含法官_含酒駕前案紀錄.csv](https://github.com/yc-chen10/112-yichentsai-thesis/blob/main/2016to22_%E5%88%A4%E6%B1%BA%E7%B5%90%E6%A7%8B%E5%8C%96%E8%B3%87%E6%96%99_%E6%B8%85%E6%B4%97%E6%95%B4%E7%90%86%E5%BE%8C_%E6%9C%89%E5%BA%8F%E8%B3%87%E6%96%99%E7%B7%A8%E7%A2%BC%E4%BF%AE%E6%AD%A3%E5%BE%8Cv2_%E5%90%AB%E6%B3%95%E5%AE%98_%E5%90%AB%E9%85%92%E9%A7%95%E5%89%8D%E6%A1%88%E7%B4%80%E9%8C%84.csv)
  - 只抓2016～2022年的原因：這個區間的刑罰上限是一樣的（論文我有寫修法歷程），資料量也比較足夠，所以才只取16～22年


## 程式：篩選酒駕判決和LLM處理用本地跑，論文實驗一和二都是colab
### 前處理／研究方法

> 除了編碼規則和描述統計的程式以外，不建議為了復現再跑一次，除非是有新資料要照這個流程處理，因為篩選+萃取花費時間24小時不間斷大概就要花兩個禮拜，萃取的部分要另外花錢，所以也不建議為了單純復現去跑。

- 篩選酒駕判決書：[copyFile.py](https://github.com/yc-chen10/112-yichentsai-thesis/blob/main/copyFile.py)
- LLM 萃取：[LLM萃取案件事實特徵.ipynb](https://github.com/yc-chen10/112-yichentsai-thesis/blob/main/LLM%E8%90%83%E5%8F%96%E6%A1%88%E4%BB%B6%E4%BA%8B%E5%AF%A6%E7%89%B9%E5%BE%B5.ipynb)
- 編碼規則：[案件特徵結構化資料預處理.ipynb](https://colab.research.google.com/drive/1URX14VOX4RbAPyzw75-jxTcu9e8q1Wl6?usp=sharing) (檔案太大傳不上來，直接去連結下載或是雲端抓)  
  - 這裡吃的資料就是 <b>案件結構化資料(還是文字內容)</b> 所以這個全部跑完預期是要有 <b>編碼後的案件結構化資料</b>
- 描述統計：[論文描述統計.ipynb](https://github.com/yc-chen10/112-yichentsai-thesis/blob/main/%E8%AB%96%E6%96%87%E6%8F%8F%E8%BF%B0%E7%B5%B1%E8%A8%88.ipynb)
### 正式實驗部分
- 論文實驗一（注意程式碼資料的讀取路徑，有沒有改成資料在你的雲端路徑，理論上就能跑了）
  - [實驗一(含酒精前案紀錄).ipynb](https://github.com/yc-chen10/112-yichentsai-thesis/blob/main/%E5%AF%A6%E9%A9%97%E4%B8%80(%E5%90%AB%E9%85%92%E7%B2%BE%E5%89%8D%E6%A1%88%E7%B4%80%E9%8C%84).ipynb)
  - [實驗一之二(含酒駕前案紀錄).ipynb](https://github.com/yc-chen10/112-yichentsai-thesis/blob/main/%E5%AF%A6%E9%A9%97%E4%B8%80%E4%B9%8B%E4%BA%8C(%E5%90%AB%E9%85%92%E9%A7%95%E5%89%8D%E6%A1%88%E7%B4%80%E9%8C%84).ipynb)
- 論文實驗二（同上)：[實驗二.ipynb](https://github.com/yc-chen10/112-yichentsai-thesis/blob/main/%E5%AF%A6%E9%A9%97%E4%BA%8C.ipynb)
