#!/bin/sh

#src=cl
#tgt=hl
src=hl
tgt=cl

SCRIPTS=~/fairseq/mosesdecoder/scripts
TOKENIZER=${SCRIPTS}/tokenizer/tokenizer.perl
DETOKENIZER=${SCRIPTS}/tokenizer/detokenizer.perl
LC=${SCRIPTS}/tokenizer/lowercase.perl
TRAIN_TC=${SCRIPTS}/recaser/train-truecaser.perl
TC=${SCRIPTS}/recaser/truecase.perl
DETC=${SCRIPTS}/recaser/detruecase.perl
NORM_PUNC=${SCRIPTS}/tokenizer/normalize-punctuation.perl
CLEAN=${SCRIPTS}/training/clean-corpus-n.perl
BPEROOT=~/fairseq/subword-nmt/subword_nmt
MULTI_BLEU=${SCRIPTS}/generic/multi-bleu.perl
MTEVAL_V14=${SCRIPTS}/generic/mteval-v14.pl

data_dir=~/fairseq/nmt_taiwanese/data/taiwanese
model_dir=~/fairseq/nmt_taiwanese/models/taiwanese
utils=~/fairseq/nmt_taiwanese/utils

echo $SCRIPTS
