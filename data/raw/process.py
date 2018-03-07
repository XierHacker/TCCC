import numpy as np
import pandas as pd

#从.csv文件里面抽取出评论字符串,写到文件中
def extractText(inFile,outFile):
    frame=pd.read_csv(filepath_or_buffer=inFile)
    comment=frame["comment_text"]
    f=open(file=outFile,mode="w",encoding="utf-8")
    for i in range(comment.shape[0]):
        s=comment[i].replace("\n"," ")+"\n"
        f.write(s)
    f.close()

if __name__=="__main__":
    extractText(inFile="train.csv",outFile="./comments.txt")


