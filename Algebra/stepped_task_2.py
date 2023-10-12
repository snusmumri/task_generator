from pytexit import py2tex
import re
import random
import math
from sympy import *
import numpy as np

def transformation_task(string):
    while True:
        elements = []
        start_index = string.find('C_')

        while start_index != -1:
            end_index = string.find(']', start_index)
            element = string[start_index : end_index + 1]
            elements.append(element)
            start_index = string.find('C_', end_index)

        values = []
        for element in elements:
            start_index = element.find('[') + 1
            end_index = element.find(']')
            range_string = element[start_index : end_index]
            range_values = list(map(int, range_string.split(', ')))
            random_value = random.randint(range_values[0], range_values[1])
            values.append(random_value)

        updated_string = string
        for i, el in enumerate(elements):
            updated_string = updated_string.replace(el, str(values[i]))

        answer = eval(updated_string)
        task = 'Вычислите: '+py2tex(updated_string, print_formula = False, print_latex = False)

        if abs(answer * 1000 - int(answer * 1000)) < 0.0001 or abs(int(answer * 1000) - answer * 1000) < 0.0001:
            if answer <= 10000 and answer >= -10000:
                break

    return task, round(answer, 3)

prototype_14815 = transformation_task('pow( C_1[1, 10] / C_2[1, 10], C_5[2, 5])*C_4[2, 30] + pow(0.1, C_6[2, 5])*(C_3[1, 10]*1000)')

prototype_14784 = transformation_task('pow( (C_1[1, 8] / C_2[1, 8]), C_3[1, 8])*( C_4[1, 8] + C_5[1, 8] / C_1[1, 8] )')

prototype_14785 = transformation_task('pow( (C_1[1, 40] / 10), C_3[2, 5]) / C_2[2, 51]')

prototype_14809 = transformation_task('C_1[2, 10]*pow(C_2[2, 10], C_3[2, 6]) + C_2[2, 10]*pow(C_2[2, 10], C_4[2, 6])')

prototype_14814 = transformation_task('C_1[2, 10]*pow(C_2[2, 10], C_3[2, 5]) + C_2[2, 10]*pow(C_2[2, 10], C_4[2, 5])')

prototype_14816 = transformation_task('C_1[10, 101] / pow(C_2[2, 11], C_7[2, 5]) - pow( (C_5[1, 11] / C_6[1, 11]), C_3[2, 5])*C_4[2, 500]')

prototype_14817 = transformation_task('pow( ( C_4[1, 11]+(C_1[1, 7]/C_2[1, 7]) ), C_6[2, 5]) - pow( ( C_5[1, 11]+( C_3[1, 7]  / C_2[1, 7]) ), C_7[2, 5])')

prototype_14819 = transformation_task('-pow(-C_1[2, 10], C_5[2, 5]) / C_2[2, 10] - pow(C_3[2, 10], C_6[2, 5])*C_4[2, 10]')

prototype_14836 = transformation_task('pow(C_1[-1, 1], C_4[2, 70]) + pow(C_2[-1, 1], C_5[2, 70]) + pow(C_3[-1, 1], C_6[2, 70])')

prototype_14839 = transformation_task('pow(C_1[-1, 1], C_5[2, 503]) - pow(C_2[-1, 1], C_6[2, 503]) + pow(C_3[-1, 1], C_7[2, 503]) + pow(C_4[-1, 1], C_8[2, 503])')

prototype_14841 = transformation_task('pow(-1, C_2[2, 10]) - pow(-1, C_3[2, 10]) - pow(-1, C_4[2, 10]) - pow(-1, C_5[2, 10])')

prototype_14842 = transformation_task('pow(C_1[-1, 1], C_5[2, 30]) + pow(C_2[-1, 1], C_6[2, 30]) - pow(C_3[-1, 1], C_7[2, 30]) - pow(C_4[-1, 1], C_8[2, 30])*pow(C_2[-1, 1], C_7[2, 30])')

prototype_15021 = transformation_task('( pow(C_1[2, 20], C_2[1, 15]) * pow(C_1[2, 20], C_3[1, 15]) )/pow(C_1[2, 20], C_4[1, 15])')

prototype_15024 = transformation_task('( pow(C_1[10, 50], C_2[1, 15]) / pow(C_1[10, 50], C_3[1, 15]) )*pow(C_1[10, 50], C_4[1, 15])')

prototype_15025 = transformation_task('( pow( (C_1[1, 9]/10), C_2[1, 15])*pow( (C_1[1, 9]/10), C_3[1, 15]) ) / pow( (C_1[1, 9]/10), C_4[1, 15])')

prototype_15026 = transformation_task('( pow( (C_1[1, 9] / C_2[1, 9]) , C_3[1, 15])*pow( (C_1[1, 9] / C_2[1, 9]), C_4[1, 15]) )/pow( (C_1[1, 9] / C_2[1, 9]), C_5[1, 15])')

prototype_15046 = transformation_task('pow(pow(C_1[2, 10], C_2[2, 5]), C_3[2, 5])')

prototype_15164 = transformation_task('pow(C_1[2, 16], C_2[2, 10])*pow( (1/C_1[2, 16]), C_2[2, 10])')

prototype_15165 = transformation_task('pow(C_1[2, 16], C_2[2, 10])*pow( (1/C_1[2, 16]), C_2[2, 10])')

prototype_15166 = transformation_task('pow(C_1[2, 16], C_2[2, 10])*pow( (C_3[1, 5]/C_1[2, 16]), C_2[2, 10])')

prototype_15167 = transformation_task('pow( (5/C_1[2, 10]), C_3[2, 10])*pow(2*C_1[2, 10], C_3[2, 10])')

prototype_15168 = transformation_task('(-pow( ( C_1[2, 10]/C_2[2, 10] ), C_3[2, 10]))*(-pow( ( C_2[2, 10]/C_1[2, 10] ), C_3[2, 10]))')

prototype_15169 = transformation_task('(-pow( ( C_1[2, 10]/C_2[2, 10] ), C_3[2, 15]))*(-pow( ( C_2[2, 10]/C_3[2, 15] ), C_3[2, 15]))')

prototype_15170 = transformation_task('pow( ( C_1[2, 10]/C_2[2, 10] ), C_3[2, 15])*pow( ( 2*C_2[2, 10]/C_1[2, 10] ), C_3[2, 15])')

prototype_15171 = transformation_task('pow( ( C_1[2, 10]/C_2[2, 10] ), C_3[2, 15])*pow( ( 2*C_2[2, 10]/C_1[2, 10] ), C_3[2, 15])')

prototype_15172 = transformation_task('( pow(C_1[2, 5], C_3[3, 10])*pow(C_2[4, 12], C_3[3, 10]) ) / pow( (C_1[2, 5]*C_2[4, 12]), C_4[2, 9]) ')

prototype_15173 = transformation_task('( pow(C_1[2, 5], C_3[3, 10])*pow(C_2[4, 12], C_3[3, 10]) ) / pow( (C_1[2, 5]*C_2[4, 12]), C_4[2, 9])')

prototype_15174 = transformation_task('( pow(C_1[3, 9], C_3[3, 12])*pow(C_2[5, 15], C_3[3, 12]) ) / pow( (C_1[3, 9]*C_2[5, 15]), C_4[2, 10])')

prototype_15175 = transformation_task('( pow(C_1[3, 9], C_3[3, 12])*pow(C_2[5, 15], C_3[3, 12]) ) / pow( (C_1[3, 9]*C_2[5, 15]), C_4[2, 10])')

prototype_15176 = transformation_task('( pow(C_1[10, 20], C_3[2, 5])*pow(C_2[2, 6], C_3[2, 5]) ) / pow( (C_1[10, 20]*C_2[2, 6]), C_4[2, 4])')

prototype_15177 = transformation_task(' pow( (C_1[2, 8]*C_2[3, 10]), C_4[3, 15]) / ( pow(C_1[2, 8], C_3[2, 5])*pow(C_2[3, 10], C_3[2, 5]) ) ')

prototype_15178 = transformation_task('( pow(C_1[2, 7], C_3[11, 17])*pow(C_2[2, 8], C_3[11, 17]) ) / pow( (C_1[2, 7]*C_2[2, 8]), C_4[11, 17])')

prototype_15179 = transformation_task(' pow( (C_1[2, 8]*C_2[3, 10]), C_4[3, 9]) / ( pow(C_1[2, 8], C_3[2, 5])*pow(C_2[3, 10], C_3[2, 5]) )')

prototype_15057 = transformation_task(' pow( C_1[10, 19], C_3[3, 9]) / ( pow(C_2[2, 8], C_4[5, 11])*(C_1[10, 19]*C_2[2, 8]) )')

prototype_15207 = transformation_task('pow(C_1[2, 10], C_4[2, 5]) + pow(C_2[2, 10], C_5[3, 9]) + pow(C_3[2, 10], C_6[0, 0])')

prototype_15209 = transformation_task('pow(C_1[2, 10], C_2[0, 0])*pow(C_3[2, 10], C_4[3, 9]) + pow(C_5[6, 15], C_6[2, 5])')

prototype_15050 = transformation_task(' ( pow(C_1[2, 4], C_2[2, 7])*(pow( pow(C_1[2, 4], C_3[2, 5]), C_4[3, 6])) ) / pow(C_1[2, 4], C_5[12, 20]) ')

prototype_15051 = transformation_task(' (pow( pow(C_1[2, 5], C_3[2, 7]), C_4[2, 4])) / pow(C_1[2, 5], C_2[2, 4])*pow(C_1[2, 5], 2) ')

prototype_15052 = transformation_task('( (pow( pow(C_1[2, 4], C_3[2, 5]), C_4[3, 6]))*pow(C_1[2, 4], C_2[2, 7]) ) / pow(C_1[2, 4], C_5[12, 20]) ')

prototype_15053 = transformation_task(' pow(C_1[2, 5], C_2[2, 4])*pow(C_1[2, 5], 2)/(pow( pow(C_1[2, 5], C_3[2, 7]), C_4[2, 4])) ')

prototype_15054 = transformation_task(' (pow(C_1[2, 6], C_2[2, 8])*pow(C_1[2, 6], 3))/ pow(pow(C_1[2, 6], 2), C_3[2, 5]) ')

prototype_15055 = transformation_task(' (pow(C_1[2, 6], C_2[5, 12])*pow(C_1[2, 6], 3))/ pow(pow(C_1[2, 6], 2), C_3[3, 10]) ')

prototype_15056 = transformation_task(' (pow(C_1[2, 6], C_2[2, 5])*pow(C_1[2, 6], 3))/ pow(pow(C_1[2, 6], 2), C_3[2, 6]) ')

prototype_15227 = transformation_task(' ( pow(C_1[11, 19]/10, C_6[2, 5])-pow(C_2[31, 49]/10, 0)*C_1[11, 19]*(C_3[1, 9]/10) + pow(C_3[1, 9]/10, C_6[2, 5]) ) / ( C_4[101, 199]/100 - pow(C_5[1, 9]/10, C_6[2, 5]) ) ')

prototype_15228 = transformation_task(' C_1[2, 5]/C_2[2, 8] + pow(pow(C_3[9, 20], 0), C_1[2, 5]) -  pow((C_4[1, 4]+C_5[1, 1]/C_6[2, 2]), C_6[2, 2]) + pow(C_4[2, 5], C_1[2, 5])*(C_8[1, 9]/10) ')

prototype_15229 = transformation_task(' ( pow((C_1[11, 19]/10), 2) - pow((C_2[11, 19]/10), 2) ) / ( pow((C_1[11, 19]/10), 0)*(C_3[1, 9]/10) - pow((C_2[11, 19]/10), 0)*(C_4[91, 99]/10)  ) ')

prototype_15230 = transformation_task(' pow(pow(-C_1[2, 10], 0), C_4[4, 9]) - C_2[3, 9]*(1/C_2[3, 9]) - C_3[2, 7]*(1/C_3[2, 7]) ')
