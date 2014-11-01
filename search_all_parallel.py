# -*- coding: utf8 -*-

from libsearch import *
import csv
import threading
import time

books = set()
complete = False

readerLock = threading.Lock()
writerLock = threading.Lock()

class searchThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        print self.threadID, " start."

    def run(self):
        global reader, writer
        try:
            while 1:
                readerLock.acquire()
                row = reader.next()
                readerLock.release()

                new_row = search_in_universities(row)
                
                writerLock.acquire()
                writer.writerow(new_row)
                writerLock.release()
        except StopIteration:
            print self.threadID, " done."
            readerLock.release()
            return




def search_in_universities(row):

    ''' Given a row in csv, search ISBN 
    in all schools, appending the result then 
    return
    '''
#    row.append( search_in_IU(row [ISBN_idx]) )
#    row.append( search_in_Illinois(row [ISBN_idx]) )
#    row.append( search_in_UW(row [ISBN_idx]) )
#    row.append( search_in_SYR(row [ISBN_idx]) )
#    row.append( search_in_UMICH(row [ISBN_idx]) )
#    row.append( search_in_UTEXAS(row [ISBN_idx]) )
#    row.append( search_in_IUB(row [ISBN_idx]) )
#    row.append( search_in_SIMMONS(row [ISBN_idx]) )
#    row.append( search_in_DREXEL(row [ISBN_idx]) )
    row.append( search_UNC(row[ISBN_idx]) ) 
#    row.append( search_RUTGERS(row[ISBN_idx]) ) 
    return row

def main():
    global reader, writer, ISBN_idx
    print "Main thread start."

    csv_file = 'lib.csv'
    out_file = 'result.csv'
    ISBN_idx = 4
    with open(csv_file) as infile, \
            open(out_file, 'w') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        threads = []
        for i in range(4):
            threads.append(searchThread(i))
            threads[i].start() 

        for t in threads:
            t.join()
        
        print "Main thread done."


if __name__ == '__main__':
    main()
