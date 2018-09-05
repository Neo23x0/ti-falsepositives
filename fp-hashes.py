# Hashes that are often included in IOC lists but are false positives
HASH_WHITELIST = [
    # Empty file
    'd41d8cd98f00b204e9800998ecf8427e',
    'da39a3ee5e6b4b0d3255bfef95601890afd80709',
    'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    # One byte line break file (Unix) 0x0a
    '68b329da9893e34099c7d8ad5cb9c940',
    'adc83b19e793491b1c6ea0fd8b46cd9f32e592fc',
    '01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b',
    # One byte line break file (Windows) 0x0d0a
    '81051bcc2cf1bedf378224b0a93e2877',
    'ba8ab5a0280b953aa97435ff8946cbcbb2755a27',
    '7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6',
    # One byte file with 0x00
    '93b885adfe0da089cdf634904fd59f71',
    '5ba93c9db0cff93f52b521d7420e43f6eda2784f',
    '6e340b9cffb37a989ca544e6bb780a2c78901d3fb33738768511a30617afa01d',
    # 1024 bytes 0x00
    '0f343b0931126a20f133d67c2b018a3b',
    '60cacbf3d72e1e7834203da608037b1bf83b40e8',
    '5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef',
    # 2048 bytes 0x00
    'c99a74c555371a433d121f551d6c6398',
    '605db3fdbaff4ba13729371ad0c4fbab3889378e',
    'e5a00aa9991ac8a5ee3109844d84a55583bd20572ad3ffcd42792f3c36b183ad',
    # File filled with 99 zeros (probably caused by AV)
    'fa8715078d45101200a6e2bf7321aa04',
    'd991c16949bd5e85e768385440e18d493ce3aa46',
    '4b298058e1d5fd3f2fa20ead21773912a5dc38da3c0da0bbc7de1adfb6011f1c',
    # File filled with 4096 zeros (probably caused by AV)
    '620f0b67a91f7f74151bc5be745b7110',
    '1ceaf73df40e531df3bfb26b4fb7cd95fb7bff1d',
    'ad7facb2586fc6e966c004d7d1d16b024f5805ff7cb47c7a85dabd8b48892ca7',
    # 1x1 pixel JPEG
    'c5e389341a0b19b6f045823abffc9814',
    'c82cee5f957ad01068f487eecd430a1389e0d922',
    '995c770caeb45f7f0c1bc3affc60f11d8c40e16027df2cf711f95824f3534b6f',
    # 1x1 tracking pixel GIF
    '325472601571f31e1bf00674c368d335',
    '2daeaa8b5f19f0bc209d976c02bd6acb51b00b0a',
    'b1442e85b03bdcaf66dc58c7abb98745dd2687d86350be9a298a1d9382ac849b',
    # Empty Word document
    'e617348b8947f28e2a280dd93c75a6ad',
    '125da188e26bd119ce8cad7eeb1fc2dfa147ad47',
    '06f7826c2862d184a49e3672c0aa6097b11e7771a4bf613ec37941236c1a8e20',
    # File that contains the word 'administrator'
    '200ceb26807d6bf99fd6f4f0d1ca54d4',
    'b3aca92c793ee0e9b1a9b0a5f5fc044e05140df3',
    '4194d1706ed1f408d5e02d672777019f4d5385c766a8c6ca8acba3167d36a7b9',
    # File that contains the word 'foo\x0a'
    'd3b07384d113edec49eaa6238ad5ff00',
    'f1d2d2f924e986ac86fdf7b36c94bcdf32beec15',
    'b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c',
    # File that contains the word 'yes'
    'a6105c0a611b41b08f1209506350279e',
    'fb360f9c09ac8c5edb2f18be5de4e80ea4c430d0',
    '8a798890fe93817163b10b5f7bd2ca4d25d84c52739a645a889c173eee7d9d3d',
    # File that contains 2\x0d\x0a
    '10400c6faf166902b52fb97042f1e0eb',
    'f1d2d2f924e986ac86fdf7b36c94bcdf32beec15',
    'df4e26a04a444901b95afef44e4a96cfae34690fff2ad2c66389c70079cdff2b',
    # File that contains 44 43 48 01 18 40 80 25 03 00 06 00 DCH..@.%.... (unknown)
    '4b6c7f3146f86136507497232d2f04a0',
    'deabe082bc0f0f503292e537b2675c7c93dca40f',
    '4a15a6777284035dfd8df4ecf496b4f0557a9cc4ffaaf5887659031e843865e1',
    # WinPCap 4.1.3
    'a11a2f0cfe6d0b4c50945989db6360cd',
    'e2516fcd1573e70334c8f50bee5241cdfdf48a00',
    'fc4623b113a1f603c0d9ad5f83130bd6de1c62b973be9892305132389c8588de',
    # disallowedcertstl.cab
    '16e8e953c65d610c3bfc595240f3f5b7',
    '231a802e6ff1fae42f2b12561fff2767d473210b',
    '048846ed8ed185a26394adeb3f63274d1029bbd59cffa8e73a4ef8b19456de1d',
    # Powerpoint 2010
    'e24133dd836d99182a6227dcf6613d08',
    '72c2dbbb1fe642073002b30987fcd68921a6b140',
    '4dde54cfc600dbd9a610645d197a632e064115ffaa3a1b595c3a23036e501678',
    # Special CAB file
    '41f958d2d3e9ed4504b6a8863fd72b49',
    'f6d380b256b0e66ef347adc78195fd0f228b3e33',
    'c929701c67a05f90827563eedccf5eba8e65b2da970189a0371f28cd896708b8',
    # MS Notepad
    'd378bffb70923139d6a4f546864aa61c',
    'f00aa51c2ed8b2f656318fdc01ee1cf5441011a4',
    'c4232ddd4d37b9c0884bd44d8476578c54d7f98d58945728e425736a6a07e102',
    # MSVCR71.DLL
    '86f1895ae8c5e8b17d99ece768a70732',
    'd5502a1d00787d68f548ddeebbde1eca5e2b38ca',
    '8094af5ee310714caebccaeee7769ffb08048503ba478b879edfef5f1a24fefe',
    # RecordedTV.library-ms
    'b6f9aa44c5f0565b5deb761b1926e9b6',
    '183d0929423da2aa83441ee625de92b213f33948',
    '07c4c7ae2c4c7cb3ccd2ba9cd70a94382395ca8e2b0312c1631d09d790b6db33',
    # 404 error message
    '8e325dc2fea7c8900fc6c4b8c6c394fe',
    '1b3291d4eea179c84145b2814cb53e6a506ec201',
    '0b52c5338af355699530a47683420e48c7344e779d3e815ff9943cbfdc153cf2',
]