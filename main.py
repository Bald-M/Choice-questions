# -*- coding:utf-8 -*-
# 作者：张子涵
# 时间：2022/3/20

from openpyxl import load_workbook
from random import randint

def read_data(min_col,max_col):
    data_list = []
    for datas in ws.iter_cols(min_col=min_col, max_col=max_col):
        for data in datas:
            data_list.append(data.value)
        return data_list

def ask_question(rand):
    question = questions[rand]
    option = options[rand]
    print(question)
    print(option)
    answer_question = input("请输入答案：")
    return answer_question


if __name__ == '__main__':
    wb = load_workbook("题库.xlsx")
    ws = wb.active

    questions = read_data(1, 1)
    options = read_data(2, 2)
    answers = read_data(3, 3)

    rand = randint(1, int(ws.max_row) - 1)
    while True:
        answer = answers[rand]
        answer_question = ask_question(rand)

        if answer_question.lower() == answer.lower():
            print("您的答案正确！")
            rand = randint(1, int(ws.max_row) - 1)
        elif answer_question.lower() != answer.lower():
            print("您的答案错误！")
        else:
            print("请输入正确的字符")









