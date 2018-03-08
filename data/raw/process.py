import numpy as np
import pandas as pd

#从.csv文件里面抽取出评论字符串,写到文件中
def extractText(inFile,outFile):
    frame=pd.read_csv(filepath_or_buffer=inFile)
    #插入一个列"comment_pure"用来接收处理后的评论字符串
    frame["comment_pure"]="null"
    comment=frame["comment_text"]
    f=open(file=outFile,mode="w",encoding="utf-8")
    for i in range(comment.shape[0]):
        #去掉每行文本不相关换行符
        s=comment[i].replace("\n"," ")
        #去掉文本引号
        s=s.replace("\"","")
        #去掉文本首尾空格
        s=s.strip(" ")+"\n"
        frame["comment_pure"][i]=s
        #写入到.txt文件(便于观察)
        f.write(s)
    f.close()
    #写入新的.csv文件
    frame.to_csv(path_or_buf="./new_test.csv",encoding="utf-8",index=False)

if __name__=="__main__":
    extractText(inFile="test.csv",outFile="./test_comments.txt")


