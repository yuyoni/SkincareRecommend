# 이 클래스는 easyOCR처럼 한번만 인스턴스 만들면 됨
class OCR:
    def __init__(self):
        import easyocr
        import torch
        if torch.cuda.is_available():
            self.reader = easyocr.Reader(['ko', 'en'], gpu=True)
        else:
            self.reader = easyocr.Reader(['ko', 'en'])
    
    def findSimilar(self, words, user_dictionary):
        import numpy as np
        import Levenshtein
        temp = []
        for x in words:
            distances = np.array([Levenshtein.distance(x, w) for w in user_dictionary])
            try:
                index = np.argmin(distances)
                similar_word = user_dictionary[index]
                temp.append((x, similar_word, min(distances)))
            except ValueError:
                temp.append(w)    
        return temp
    
    # 분리된 단어 합치고 거리값 기반으로 수정하기
    def concateUpdate(self, ocr_result, user_dictionary):
        line = []
        word_list = []
        for i in range(len(ocr_result)-1):
            line1 = ocr_result[i].split()
            line2 = ocr_result[i+1].split()
            if len(line1)*len(line2) != 0:
                connected_word = line1[-1]+line2[0]
                word = (line1[-1], line2[0], connected_word)
                word_list.append(word)
            if i == 0:
                line1, line2 = line1[:-1], line2[1:-1]
            elif i == len(ocr_result)-2:
                line1, line2 = line1[1:-1], line2[1:]
            else:
                line1, line2 = line1[1:-1], line2[1:-1]
            line.extend(line1+line2)
            line.append(connected_word)
            tot_sum = list(set(line))
        n = 0
        for wt in word_list:
            res = self.findSimilar(wt, user_dictionary)
            # ICDAR2019 Normalized Edit Distance 계산
            b1 = 1 - res[0][2] / max(len(res[0][0]), len(res[0][1]))
            b2 = 1 - res[1][2] / max(len(res[1][0]), len(res[1][1]))
            before_normED = (b1 + b2) / 2
            after_normED = 1 - res[2][2] / max(len(res[2][0]), len(res[2][1]))
            
            if before_normED >= after_normED:
                tot_sum.pop(tot_sum.index(res[2][0]))
                tot_sum.append(res[0][1])
                tot_sum.append(res[1][1])
                n += 1
            else:
                continue
        calculated_n = 2 * n
        return tot_sum, calculated_n
    
    def ocrWord(self, image, user_dictionary):
        result = self.reader.readtext(image, detail=0)
        updated_result, calculated_n = self.concateUpdate(result, user_dictionary)
        pass_result = updated_result[:-calculated_n]
        if calculated_n == 0:
            pass_result = updated_result
        changed_result = [x[1] for x in self.findSimilar(pass_result, user_dictionary)]
        final_result = changed_result + updated_result[-calculated_n:]
        return final_result