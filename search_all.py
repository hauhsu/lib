# -*- coding: utf8 -*-

from libsearch import *
import csv



def main():
    csv_file = 'lib.csv'
    out_file = 'result.csv'
    ISBN_idx = 4
    with open(csv_file) as infile, \
            open(out_file, 'w') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            idx = 0
            for row in reader:
                if idx == 0:
                    row.append('印地安那大學伯明頓分校')
                    row.append('伊利諾大學厄巴納香檳分校')
                    row.append('華盛頓大學')
                    row.append('雪城大學')
                    row.append('密西根大學安娜堡分校')
                    row.append('德州大學奧斯汀分校')
                    row.append('印地安那大學伯明頓分校')
                    row.append('西蒙學院')
                    row.append('卓克索大學')
                    writer.writerow(row)
                else: 
                    row.append( search_in_IU(row [ISBN_idx]) )
                    row.append( search_in_Illinois(row [ISBN_idx]) )
                    row.append( search_in_UW(row [ISBN_idx]) )
                    row.append( search_in_SYR(row [ISBN_idx]) )
                    row.append( search_in_UMICH(row [ISBN_idx]) )
                    row.append( search_in_UTEXAS(row [ISBN_idx]) )
                    row.append( search_in_IUB(row [ISBN_idx]) )
                    row.append( search_in_SIMMONS(row [ISBN_idx]) )
                    row.append( search_in_DREXEL(row [ISBN_idx]) )
                    writer.writerow(row)
                idx += 1;
                #if (idx > 2):
                 #   break
            



if __name__ == '__main__':
    main()
