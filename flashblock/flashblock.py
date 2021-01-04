#!/usr/bin/python3

import sys
import yaml
import os



def LoadYAML(yamlfile : str, checkroutine=None):

    r = {}

    try:
        hfile = open(yamlfile)
        r = yaml.safe_load(hfile)

        if checkroutine:
            flagCheck = checkroutine(r)
            if flagCheck:
                return r

    except Exception as exc:
        print(exc)

    return r


def Assemble(fnameyaml : str) -> bool:

    if not os.path.isfile(fnameyaml):
        print("Wrong file given {}".format(fnameyaml))
        return False

    rdir = os.path.dirname(os.path.abspath(fnameyaml))
    jprj = LoadYAML(fnameyaml)
    flds = ['content', 'result']

    for fld in flds:
        if fld not in jprj:
            print('Field {} not found in YAML'.format(fld))
            return False

    prjfiles = jprj['content']
    arrfiles = []
    for fileitem in prjfiles:
        fname = os.path.join(rdir, fileitem)
        arrfiles.append(fname)

    for idx in range(len(arrfiles)):
        fileitem = arrfiles[idx]
        if not os.path.isfile(fileitem):
            print('File not found: {} , check the project content'.format(fileitem))
            return False
        else:
            fstat = os.stat(fileitem)
            arrfiles[idx] = [fileitem, fstat.st_size]
            print("{} {}".format(fstat.st_size, fileitem))

    foutfile = jprj['result']

    # Assemble block
    print("Writing output to {}".format(foutfile))

    # Prepare header 256
    binhdr = bytearray(256)
    offset = 256
    for idx in range(len(arrfiles)):
        fs = arrfiles[idx][1]

        binhdr[idx*8+0] = offset & 0xFF
        binhdr[idx*8+1] = (offset >> 8) & 0xFF
        binhdr[idx*8+2] = (offset >> 16) & 0xFF
        binhdr[idx*8+3] = (offset >> 24) & 0xFF

        binhdr[idx*8+4] = fs & 0xFF
        binhdr[idx*8+5] = (fs >> 8) & 0xFF
        binhdr[idx*8+6] = (fs >> 16) & 0xFF
        binhdr[idx*8+7] = (fs >> 24) & 0xFF


    fout = open(foutfile, 'wb')
    fout.write(binhdr)

    for fileitem in arrfiles:

        fin = open(fileitem[0], 'rb')
        binfile = fin.read()
        fin.close()

        fout.write(binfile)

    fout.close()

    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("flashblock.py <project.yml>")
    else:
        yfile = sys.argv[1]
        print("Packing project: ", yfile)
        print("Ok" if Assemble(yfile) else "Assemble failed")
