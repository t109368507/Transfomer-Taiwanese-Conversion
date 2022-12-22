import random
import sys

'''
Usage:
python split.py src_fpath tgt_fpath new_data_dir
'''

def split(src_fpath, tgt_fpath, nsrc='cl', ntgt='hl', ratio=(0.9, 0.05, 0.05), new_data_dir=''):
  src_fp = open(src_fpath, encoding='utf-8')
  tgt_fp = open(tgt_fpath, encoding='utf-8')

  src_train, src_test, src_val = open(new_data_dir + 'train.' + nsrc, 'w', encoding='utf-8'), \
    open(new_data_dir + 'test.' + nsrc, 'w', encoding='utf-8'), open(new_data_dir + 'valid.' + nsrc, 'w', encoding='utf-8')
  tgt_train, tgt_test, tgt_val = open(new_data_dir + 'train.' + ntgt, 'w', encoding='utf-8'), \
    open(new_data_dir + 'test.' + ntgt, 'w', encoding='utf-8'), open(new_data_dir + 'valid.' + ntgt, 'w', encoding='utf-8')

  src, tgt = src_fp.readlines(), tgt_fp.readlines()
  for s, t in zip(src, tgt):
      rand = random.random()
      if 0 < rand <= ratio[0]:
        src_train.write(s)
        tgt_train.write(t)
        print("src_train: ",s)
        print("tgt_train: ",t)
      elif ratio[0] < rand <= ratio[0] + ratio[1]:
        src_test.write(s)
        tgt_test.write(t)
        print("src_test: ",s)
        print("tgt_test: ",t)
      else:
        src_val.write(s)
        tgt_val.write(t)
        print("src_val: ",s)
        print("tgt_val: ",t)

  src_fp.close()
  tgt_fp.close()
  src_train.close()
  src_test.close()
  src_val.close()
  tgt_train.close()
  tgt_test.close()
  tgt_val.close()

if __name__ == '__main__':
    split(src_fpath=sys.argv[1], tgt_fpath=sys.argv[2], nsrc='hl', ntgt='cl', ratio=(0.95, 0.025, 0.025), new_data_dir=sys.argv[3])
    #split(src_fpath=sys.argv[1], tgt_fpath=sys.argv[2], nsrc='cl', ntgt='hl', ratio=(0.95, 0.025, 0.025), new_data_dir=sys.argv[3])
    #split(src_fpath=sys.argv[1], tgt_fpath=sys.argv[2], nsrc='cl', ntgt='hl', ratio=(0.15, 0.025, 0.025), new_data_dir=sys.argv[3])
