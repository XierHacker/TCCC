import numpy as np
import pandas as pd
from textblob import TextBlob

#从.csv文件里面抽取出评论字符串,写到文件中
def extractText(inFile,outFile):
    frame=pd.read_csv(filepath_or_buffer=inFile)
    #插入一个列"comment_pure"用来接收处理后的评论字符串
    frame["comment_pure"]="null"
    comment=frame["comment_text"]
    f=open(file=outFile,mode="w",encoding="utf-8")
    print('total comments: ', comment.shape[0])
    count = 0
    for i in range(comment.shape[0]):
        s = TextBlob(comment[i])
        s_ = ' '.join(s.words)
        s_ = s_.replace("n't", "not")
        s_ = s_.replace("'m", "am")
        frame["comment_pure"][i]=s_
        #写入到.txt文件(便于观察)
        f.write(s_)
        count += 1
        if i % 100 == 0:
            print(count)
        if count == 2000:
            break
    f.close()
    #写入新的.csv文件
    frame.to_csv(path_or_buf="/home/cooli/Documents/DataSets/comments/train_xz.csv",encoding="utf-8",index=False)

if __name__=="__main__":
    extractText(inFile="/home/cooli/Documents/DataSets/comments/train.csv",outFile="/home/cooli/Documents/DataSets/comments/train_comments_xz.txt")


