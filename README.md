# ti-falsepositives
A hash generator for typical false positive hashes

## Why?

Over the years, I've compiled a list of typical false positive hashes that are often included in IOC lists 

My favourites are: 
- file that contains 1 byte 0x0a 
- empty Word documents 
- 1x1 JPEG tracking pixel
- 404 error page

The script contains some of them as a static list and generates the rest.

## Automatic Hash Generation

The script generates hashes for typical false positive files. The current version supports the hash generation for zero byte fillled files (0x00) that are often falsely included into IOC lists.

## Usage

```
    usage: fp-hashes.py [-h] [--python | --misp | --withcomment ]

    False Positive Hash Generator

    optional arguments:
      -h, --help     show this help message and exit
      --python       Print as Python list
      --misp         Print as misp-warninglist
      --withcomment  Print comment lines
```

## Output

It supports different forms of output.

Hashes Only (default)
```
f5f88e70bfe94f473aacdcbe8a45ea7d
6ca66bcff8e4ae2df463f984fdb5ddb68b7bf3d0
03bf6d70689c3c5eb4e86fdb08467925ac64068e8b8f0be16234de8974f8eff6
cc43c3ab42377751527011f6cb252955
a1a5678b4e3210613e6fdd2093c877d39e11a348
bef21a11f6e9183084552128b0f71add387763033e9330dc2bf6bc376510bee5
85c0a1ac905af10774b1d36b834ef4f1
1a265342eeac3086d82dc9163d8327b3b629f822
1a1faf2a980f6a2fb5bd44ee8eba0c8b41e26197d6cd1b25f8fbd285a29decee
afe413c24e7992f2acf0e26b9d4925d5
1872c75dddd446a0c8649565589eb700de60915c
c2a889060ed3454408bd8c4282436b5e4bc37cb6f9c2743f281b638887a406d4
7a5b9baf9a4d159445e4404177206bd5
e4cbd17334f4f9494e237381446e7f6fcc2a1136
018accf59c4975cb89aace1259ca12b4bda46f661088381db828eae2f8a8a966
```

Python code (--python)
```
{'1024 bytes 0x00': ['0f343b0931126a20f133d67c2b018a3b',
                     '60cacbf3d72e1e7834203da608037b1bf83b40e8',
                     '5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef'],
 '1x1 pixel JPEG': ['c5e389341a0b19b6f045823abffc9814',
                    'c82cee5f957ad01068f487eecd430a1389e0d922',
                    '995c770caeb45f7f0c1bc3affc60f11d8c40e16027df2cf711f95824f3534b6f'],
 '1x1 tracking pixel GIF': ['325472601571f31e1bf00674c368d335',
                            '2daeaa8b5f19f0bc209d976c02bd6acb51b00b0a',
                            'b1442e85b03bdcaf66dc58c7abb98745dd2687d86350be9a298a1d9382ac849b'],
 '2048 bytes 0x00': ['c99a74c555371a433d121f551d6c6398',
                     '605db3fdbaff4ba13729371ad0c4fbab3889378e',
                     'e5a00aa9991ac8a5ee3109844d84a55583bd20572ad3ffcd42792f3c36b183ad'],
 '404 error message': ['8e325dc2fea7c8900fc6c4b8c6c394fe',
                       '1b3291d4eea179c84145b2814cb53e6a506ec201',
...
```

Hashes with Comment Lines (--withcomment)
```
# Hashes of 8186 b'\x00'
4f2c66a2a83e533dabe81c52699c040f
8f1831db7eff45f7af7ec4e482ffbac70e8d27c3
7d93845d4010b57319dfb61e80eee24e63c946940113eeee9ac976efa76030e7
# Hashes of 8187 b'\x00'
f5f88e70bfe94f473aacdcbe8a45ea7d
6ca66bcff8e4ae2df463f984fdb5ddb68b7bf3d0
03bf6d70689c3c5eb4e86fdb08467925ac64068e8b8f0be16234de8974f8eff6
# Hashes of 8188 b'\x00'
cc43c3ab42377751527011f6cb252955
a1a5678b4e3210613e6fdd2093c877d39e11a348
bef21a11f6e9183084552128b0f71add387763033e9330dc2bf6bc376510bee5
# Hashes of 8189 b'\x00'
85c0a1ac905af10774b1d36b834ef4f1
1a265342eeac3086d82dc9163d8327b3b629f822
1a1faf2a980f6a2fb5bd44ee8eba0c8b41e26197d6cd1b25f8fbd285a29decee
# Hashes of 8190 b'\x00'
afe413c24e7992f2acf0e26b9d4925d5
1872c75dddd446a0c8649565589eb700de60915c
c2a889060ed3454408bd8c4282436b5e4bc37cb6f9c2743f281b638887a406d4
# Hashes of 8191 b'\x00'
7a5b9baf9a4d159445e4404177206bd5
e4cbd17334f4f9494e237381446e7f6fcc2a1136
018accf59c4975cb89aace1259ca12b4bda46f661088381db828eae2f8a8a966
...
```


misp-warninglist (--misp)
```
{
  "description": "Hashes that are often included in IOC lists but are false positives.",
  "list": [
    "d41d8cd98f00b204e9800998ecf8427e",
    "da39a3ee5e6b4b0d3255bfef95601890afd80709",
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "...",
    "7a5b9baf9a4d159445e4404177206bd5",
    "e4cbd17334f4f9494e237381446e7f6fcc2a1136"
    "018accf59c4975cb89aace1259ca12b4bda46f661088381db828eae2f8a8a966"
  ],
  "matching_attributes": [
    "md5",
    "sha1",
    "sha256",
    "filename|md5",
    "filename|sha1",
    "filename|sha256"
  ],
  "name": "Hashes that are often included in IOC lists but are false positives.",
  "type": "string",
  "version": 0.1
}
```
