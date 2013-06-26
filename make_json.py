import sys
import json

def convert_escseq_file(inDir, outDir):
  name = 'escape_sequences'
  with open(inDir + '/{0}.txt'.format(name), 'r') as f:
    with open(outDir + '/{0}.js'.format(name), 'w') as out:
      out.write('var {0} = \n'.format(name)) #assign to js variable
      lis = []
      for line in f:
        line = line.strip()
        words = line.split()
        seq = words[0]
        desc = ' '.join(words[1:])

        lis.append({'seq': seq, 'desc': desc})
      out.write( json.dumps(lis) )

def convert_colors_file(inDir, outDir):
  name = 'colors'
  with open(inDir + '/{0}.txt'.format(name), 'r') as f:
    with open(outDir + '/{0}.js'.format(name), 'w') as out:
      out.write('var {0} = \n'.format(name))
      lis = []
      for line in f:
        words = line.strip().split('\t')
        color = words[0]
        code = ' '.join(words[1:])

        lis.append({'color': color, 'code': code})
      out.write( json.dumps(lis) )





def convert_all(inDir, outDir):
  converters = [convert_escseq_file, convert_colors_file]
  for c in converters:
    c(inDir, outDir)


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print "specify input dir, output dir"
    sys.exit()
  convert_all(*(sys.argv[1:3]))
