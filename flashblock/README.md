### Run from command line

```

    $ python3 flashblock.py project.yml
    
```


### YML file structure

```

# Block content
content:
    - file1
    - file2
    - filen

# Store result to file
result: outfile.bin

# Align files to page in bytes
align : 256 

```

### Output File Format: 

    1. Header page, 256 bytes
    2. Files data space


### Header table

    256-bytes tbl ( 64 files max ) :

    0000 0000  [offset32 , length32]] ... [ ][ ]   
    0000 0000
    .........

### TODO

    Align page 256, 512 , 1024 bytes etc ...

    Adding 'align' field to yaml file. For example 'align' : 256   
