import os, json
import shutil
import re


years = ["2025"]
#month = "06"

def judgement_filter(year,month) :
    count = 0

    path_to_root_dir = "C:/Users/User/Desktop/論文/裁判書資料/"+year+"/"+year+month+"/"
    path_to_target_dir = "C:/Users/User/Desktop/論文/酒駕/"+year+month+"/"

    #sub_dirs_name => 法院+不同種類(刑事民事行政)案件的資料夾
    sub_dirs_names = [sub_dir_name for sub_dir_name in os.listdir(path_to_root_dir) if '.' not in sub_dir_name]
    result_sub_str = "主文"
    reason_sub_str = "事實"

    #確認目的地資料夾存不存在
    if not os.path.exists(path_to_target_dir):
        # Create the directory
        os.makedirs(path_to_target_dir)
        print("Directory created successfully!")
    else:
        print("Directory already exists!")


    #遍歷每個法院
    for sub_dir_name in sub_dirs_names:
        
        json_file_names = [filename for filename in os.listdir(path_to_root_dir+"/"+sub_dir_name) if filename.endswith('.json')]
        target_json_list = []


        #遍立這個法院裡面的案件
        for json_file_name in json_file_names:

            #打開案件json檔案 
            with open(os.path.join(path_to_root_dir,sub_dir_name, json_file_name),encoding="utf-8") as json_file:
                json_text = json.load(json_file)
                json_text['JFULL'] = re.sub('\r\n','',json_text['JFULL'])
                full_json_text = re.sub(' ','',json_text['JFULL'])

                #事實及理由 事實(犯罪事實) 理由 這三種可能
                if(reason_sub_str not in full_json_text):
                    reason_sub_str = "理由"
                
                if(json_text['JCASE'][-2:] == "交簡"  and
                    json_text['JTITLE'] == "公共危險" and
                    "酒駕" in json_text['JFULL'] ):
                            try:
                                #print(json_file_name)
                            #print(json_text['JID'] )
                            #print(full_json_text)
                                result_text = full_json_text[full_json_text.index(result_sub_str):full_json_text.index(reason_sub_str)]
                                if(("致人於死" not in result_text and "致人死亡" not in result_text and "致人重傷" not in result_text and "處有期徒刑" in result_text )):
                                    shutil.copyfile(os.path.join(path_to_root_dir,sub_dir_name, json_file_name), path_to_target_dir+json_file_name)
                                    count += 1
                            except:
                                print(json_file_name)
                                print(os.path.join(path_to_root_dir,sub_dir_name, json_file_name))
                    #如果有找到符合條件的案件
                    #shutil.copyfile("C:/Users/User/Desktop/論文/裁判書資料/2013/201312/"+sub_dir_name+"/"+json_file_name, "C:/Users/User/Desktop/論文/酒駕/201312/"+json_file_name)

                    #記得先建新資料夾

    print(year+month+"done")
    print("共找到",count,"份一般酒駕的判決書")

def new_func(years, judgement_filter):
    for year in  years:
        for month in range(1,4):
            if month < 10:
                month = "0"+str(month)
            else:
                month = str(month)
            
            import time
            print(f"開始跑{year}年{month}月的判決書篩選")
            #取得執行前時間
            start = time.time()
            judgement_filter(year,month)
            print(f"跑完{year}年{month}月的判決書篩選")
            #取得執行後時間
            end = time.time()
            print("執行時間：%f 秒" % (end - start))

new_func(years, judgement_filter)





