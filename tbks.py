import sys
import os
import re

#修改的語料庫資料夾，將原始資料用檔案總管搜尋*.tbk檔案，新增tbks資料夾把檔案放到根目錄下
dirpath = "/tbks/"

#可使用少量tbk檔做測試
# dirpath = "/台語文數位典藏資料庫-20221117T065608Z-001_tbk_test0/"
# dirpath = "/台語文數位典藏資料庫-20221117T065608Z-001_tbk_test1/"
# dirpath = "/台語文數位典藏資料庫-20221117T065608Z-001_tbk_test2/"

#輸出台羅漢羅raw data
outfile_CL = "raw.cl"
outfile_HL = "raw.hl"

#判斷台羅開始抓取文本
start_CL = 0

#去除標點符號列表
characters = "”-－！,':!?[].()“「」，。？（）：﹙﹚‘、；;…" #過濾半形全形符>號

#判斷處理後漢羅台羅行數是否一致，不相同則刪除檔案
check_CL = 0
check_HL = 0

#紀錄漢羅台羅行數不同刪除檔案數量
delete_file_num = 0

#預處理後最終輸出文本
lua_CL = ''
lua_HL = ''

skip = 0
skip_num = 0
skip_symbol = 0
skip_CL = 0
skip_CL_line = 0

#每行的字元索引
index = 0

#獲取當前路徑
current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)

#將檔案名稱轉為列表
file = os.listdir(current_directory+dirpath)

#刪除上次預處理後的檔案
if os.path.isfile(current_directory+'/'+ outfile_CL):
    os.remove(current_directory+'/'+outfile_CL)
if os.path.isfile(current_directory + '/' + outfile_HL):
    os.remove(current_directory + '/' + outfile_HL)
    
#刪除檔案列表    
delete_list = []

#print(file)

for opf in file:
    print(opf)
    #開啟檔案
    with open(current_directory + dirpath + opf, "r", encoding='cp950') as f:
        #一次讀取檔案行做處理
        for line in f.readlines():
        
            index = 0
            skip = 0
            skip_num = 0
            
            # print(line)
            #刪除每行頭的空白
            line = line.strip()
            
            #空白行不處裡
            if len(line) == 0:
                continue
                
            #開始處理台羅文本    
            if line == "<CL>" and start_CL == 0:
                start_CL = 1
                continue
            elif line == "<CL>" and start_CL == 1:
                skip_CL = 1
                skip_CL_line = skip_CL_line + 1
                continue
            #開始處理漢羅文本，台羅文本處理結束 
            elif line == "</CL>":   
                start_CL = 0
                skip_CL = 0
                skip_CL_line = 0
                continue
            elif line == "<HL>" or line == "</HL>":
                continue
            
            #將tag刪除
            line = line.replace("<BR>", "")
            
            # print(line)
            for x in range(len(characters)):
                line = line.replace(characters[x], " ")
            # print(line)
            if start_CL == 1:
                if skip_CL == 1:
                    skip_CL_line = skip_CL_line - 1
                    if skip_CL_line != 0:
                        continue
                    else:
                        skip_CL = 0
                else:
                    skip_CL_line = skip_CL_line + 1
                check_CL = check_CL + 1
                for c in line:
                    l = len(line)
                    index = index + 1
                    if c == '『':
                        # print(c)
                        skip_symbol = 1
                        symbolL = line.index('『')
                    elif c == '』':
                        # print(c)
                        skip_symbol = 0
                        symbolR = line.index('』')
                        line = ' ' + line[:symbolL] + ' ' + line[symbolR+1:]
                        index = 0
                        # print(line)
                    elif skip_symbol == 1 and index == len(line):
                        skip_symbol = 0
                        index = 0
                        line = ' '
                # lua_CL = lua_CL +"###"+str(opf)+"### " + str(line) + '\n'
                lua_CL = lua_CL + str(line) + '\n'
                lua_CL = lua_CL.lower()
            else:
                line = re.findall(".{1}", line)
                # print(line)
                # print(line_temp)
                check_HL = check_HL + 1
                for c in line:
                    if c >= u'\u4e00' and c <= u'\u9fa5':
                        # print("yes: ",c)
                        if skip_symbol == 1:
                            line[index] = ' '
                        if skip > 1:
                            for i in range(skip - 1):
                                line[index - int(skip)] = line[index - int(skip)] + line[index - int(skip) + i + 1]
                                line[index - int(skip) + i + 1] = ' '
                        elif skip_num != 0:
                            for i in range(skip_num - 1):
                                line[index - int(skip_num)] = line[index - int(skip_num)] + line[
                                    index - int(skip_num) + i + 1]
                                line[index - int(skip_num) + i + 1] = ' '
                        skip = 0
                        skip_num = 0
                    else:
                        if c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z':
                            # print("no:eng:",index,c)
                            # c[5] = c[5] + c[6]
                            if skip_symbol == 1:
                                line[index] = ' '
                            skip = skip + 1
                            index = index + 1
                            continue

                        if c == " ":
                            # print("skip: ",skip)
                            # print("c: ",index,c,)
                            if skip != 0:
                                if skip_symbol == 1:
                                    line[index] = ' '
                                for i in range(skip):
                                    line[index - int(skip)] = line[index - int(skip)] + line[index - int(skip) + i + 1]
                                    line[index - int(skip) + i + 1] = ' '

                            if skip_num != 0:
                                for i in range(skip_num - 1):
                                    line[index - int(skip_num)] = line[index - int(skip_num)] + line[
                                        index - int(skip_num) + i + 1]
                                    line[index - int(skip_num) + i + 1] = ' '

                            skip_num = 0
                            skip = 0
                            # print(line)

                        if c >= '0' and c <= '9':
                            # print("no:num:",index,":",skip,": ", c)
                            if skip != 0:
                                for i in range(skip):
                                    line[index - int(skip)] = line[index - int(skip)] + line[
                                        index - int(skip) + i + 1]
                                    line[index - int(skip) + i + 1] = ' '
                                skip = 0
                                skip_num = 0
                            else:
                                skip_num = skip_num + 1

                        if c == '『':
                            # print(c)
                            skip_symbol = 1
                        elif c == '』':
                            # print(c)
                            skip_symbol = 0
                            line[index] = ' '

                        if skip_symbol == 1:
                            line[index] = ' '
                    index = index + 1
                index = 0
                # print(line)
                # lua_HL = lua_HL + str(line) + '\n'
                lua_HL =  lua_HL+" ".join(line) + '\n'
                lua_HL = lua_HL.lower()
                
    #刪除漢羅台羅行數不相同檔案
    if check_CL != check_HL:
        print(opf)
        #台羅漢羅行數
        print("check_CL:",check_CL)
        print("check_HL:",check_HL)
        delete_list.append(opf)
        #紀錄刪除檔案數量
        delete_file_num = delete_file_num + 1
        check_CL = 0
        check_HL = 0
        #刪除檔案，windows執行會有錯誤訊息
        # os.remove(current_directory+dirpath+opf)
        # sys.exit("結束程式")
    else:
        check_CL = 0
        check_HL = 0


with open(outfile_CL,'w') as file:
    file.write(lua_CL)

with open(outfile_HL,'w') as file:
    file.write(lua_HL)
print(delete_list)
print(delete_file_num)