from flask import Flask, jsonify, request
import csv

allArticles=[]
with open("articles.csv",encoding='utf-8')as f:
    csvreader=csv.reader(f)
    data=list(csvreader)
    allArticles=data[1:]

likedArticles=[]
notLikedArticles=[]

app=Flask(__name__)

@app.route("/get-articles")
def getArticle():
    return jsonify({
        "data":allArticles[0],
        "status":"success"
    })

@app.route('/likes-article',methods=["POST"])
def likedArticle():
    article=allArticles[0]
    allArticles=allArticles[1:]
    likedArticles.append(article)
    return jsonify({
        "status":"success"
    }),201


@app.route("/notliked-article",methods=["POST"])
def notLikedArticle():
    article=allArticles[0]
    allArticles=allArticles[1:]
    notLikedArticles.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()