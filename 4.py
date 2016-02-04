#! /usr/bin/env python2

import md5

if __name__ == '__main__':
  key = 1 
  salt = 'yzbqklnj'
  while True:
    if md5.new(salt + str(key)).hexdigest()[:5] == '00000':
      print key
      break
    else:
      key += 1
    
