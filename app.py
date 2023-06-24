# app.py
import os, sys

from flask import Flask, request, render_template, redirect, url_for
from myeasyocr import OCR
from recommend import I_P, C_P, C_G, Custom_vec, Recommend_search


import pandas as pd

app = Flask(__name__)
app.debug=True

# 전역변수로 지정 ( 추천에도 써야함 )
ocr_result = []

# Main page
@app.route('/')
def start():
    return render_template('index0.html')

@app.route('/main')
def main():
    return render_template('index1.html')

@app.route('/ques_type')
def question():
    return render_template('index2.html')

@app.route('/ques_concern', methods=['GET', 'POST'])
def question_type():        
    return render_template('index3.html')

@app.route('/typeResult', methods=['GET', 'POST'])
def typeResult():
    # 앞에서 체크한 피부고민 받아오기
    type = request.args.get('type')
    concern_list = request.args.get('concern_list')
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('error.html')
        file = request.files.get('file')
        if not file:
            return render_template('error.html')

        img_bytes = file.read()
        
        # txt 파일 불러오기 : user_dictionary는 전역으로 불러와야함
        with open("data/user_dictionary.txt", "r", encoding='utf-8') as file:
            strings = file.readlines()
        user_dictionary = [x.replace('\n','') for x in strings]
        
        ocr = OCR()
        ocr_result = ocr.ocrWord(img_bytes, user_dictionary)  # OCR결과 전역변수에 저장 (추천시스템에서 사용)
        print(ocr_result)
        
        # 사용자의 피부타입과 피부고민에 안좋은 성분 리스트
        cp = C_P(concern_list, type)
        ingred_list = cp.c_p()
        print(ingred_list)
        
        # 성분 설명 파일 불러오기
        df = pd.read_csv('./ingred_info.csv', encoding="CP949")
        
        # 안좋은 성분 리스트
        result = []
        
        # 안좋은 성분 설명 리스트
        result_info = []
        
        for i in ocr_result:
            if i in ingred_list:
                result.append(i)
                desc = df.loc[df['성분명'] == i, '성분 설명'].values
                if len(desc) > 0:
                    result_info.append(':'+ str(desc[0]).replace('[','').replace(']',''))
                else:
                    result_info.append('')

        # 안좋은 성분 갯수
        cnt = len(result)
        
        return render_template('index5.html', type=type, cnt=cnt, result=result, result_info=result_info, concern_list=concern_list)

    return render_template('index4.html')

@app.route('/select', methods=['GET', 'POST'])
def select() :
    type = request.args.get('type')
    concern_list = request.args.get('concern_list')  
    concern_list = eval((concern_list))    # 배열로 변환
    
    prod_type = request.args.get('prod_type')
    
    if request.method == 'GET':

        cp = C_P(concern_list, type)
        cg = C_G(concern_list, type)
        # concern_list를 추천시스템에 넘겨주고 결과값 받아와서 render_template 으로 넘겨주기
        # if (recom_prod에 값이 있으면):
        # return render_template('index7.html', 제품 리스트, 가격, 등등 화면에 표시할 것 넘겨주기)
        
        prod_list = prod_type
    
        return render_template('index6.html', type=type, concern_list=concern_list, prod_type=prod_type, prod_list=prod_list)
    
    return render_template('index6.html', type=type, concern_list=concern_list , prod_type=prod_type)

@app.route('/test', methods=['GET', 'POST'])
def test() :
    return render_template('index7.html')

# 파이썬 명령어로 실행할 수 있음
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)