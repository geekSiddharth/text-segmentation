import json

jsondata = {
    "word2vecfile": "/datadrive/sid/embedding",
    "choidataset": "/datadrive/sid/text-segmentationl/data/choi",
    "wikidataset": "/datadrive/sid/wiki_727",
}

with open('config.json', 'w') as f:
    json.dump(jsondata, f)
