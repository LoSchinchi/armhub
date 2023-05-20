import os, time

def getLineModified(l: str):
    t = l[-1] == '\n'
    if t:
        l = l[:-1]
    l = l.rstrip()  # tolgo gli spazi alla fine
    return '\t'.join(l.split(' ' * 4)) + ('\n' if t else '')

def main():
    fw = open('dati/isRunning.txt', 'w')
    fw.write('run')
    fw.close()
    time.sleep(0.2) # attente che termini il thread che esegue main.py
    fr = open('python/run.py', 'r')
    lines = fr.readlines()
    fr.close()

    tempFile = open('dati/tempEditorLines.txt', 'w')
    fw = open('python/run.py', 'w')
    fw.write('from mainActions import *\nimport modules.gestException as exception\nimport sys\n\n')
   # fw.write('def reset():\n\tresetMotors()\n\n')
    fw.write('try:\n\tclearFile(\'editorException.txt\')\n')
    fw.write('\tstart()\n\n')
    for l in lines:
        l = getLineModified(l)
        fw.write('\t' + l)
        tempFile.write(l)
    fw.write("\nexcept BaseException as e:  # eccezione madre di tutti gli Error e le Exception")
    fw.write('\n\shutdown()\n\texception.onExcept(sys.exc_info(), lcd)\n')

    fw.close()
    tempFile.close()

    os.system('python3 python/run.py')


if __name__ == '__main__':
    main()