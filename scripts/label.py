#add remaining labels
import re
import string

ofile=open('list_of_all_good_utterances.txt', encoding='utf8')
good=ofile.read()
ofile.close()

ofile=open('complete.TextGrid', encoding='utf8')
tg=ofile.read()
ofile.close()

ofile=open('../PROMPTS.TXT', encoding='utf8')
prompts=ofile.read()
ofile.close()

prompts=prompts.replace(')', '')
print(prompts)
prompts={prompt.split('(')[1]: prompt.split('(')[0] for prompt in prompts.split('\n')[:-1]}
print(prompts)


good=[line for line in good.split('\n')]


tg=tg.split('\n\n')
for block in range(len(tg)):
    tg[block]=tg[block].split('\n')

tg=tg[1:]


for block in range(len(tg)):
    if tg[block][2]=='"Speech"':
        if int(good[0])<3:
            out='sa{}'.format(good[0])
        elif int(good[0])<453:
            out='sx{}'.format(good[0])
        else:
            out='si{}'.format(good[0])
        tg[block][2]=out
        good=good[1:]

for block in range(len(tg)):
    try:
        out='{} {}'.format(prompts[tg[block][2]], tg[block][2])
        tg[block][2]=out
    except:
        pass

#print(tg)

#Write output
output=open('complete_annotated.TextGrid', 'w+', encoding='utf8')
output.write("\"Praat chronological TextGrid text file\"\n0 4520   ! Time domain.\n1   ! Number of tiers.\n\"IntervalTier\" \"silences\" 0 4520")

for block in tg:
    out='\n\n{}\n{}\n{}'.format(block[0], block[1], block[2])
    output.write(out)





        




